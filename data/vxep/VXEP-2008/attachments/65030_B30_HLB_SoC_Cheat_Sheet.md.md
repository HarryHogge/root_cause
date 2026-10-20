# B30_HLB_SoC_Cheat_Sheet.md

Attachment 65030, text, 8 KB, added 2026-10-02 by Jeremy Kostel.

# B30 HLB SoC — Cheat Sheet (Plain-Language Version)

A simplified, no-code explanation of how the firmware calculates battery percentage. Variable/config names are kept in `code font` so you can cross-reference `B30_HLB_SoC_Software_Reference.md` and `B30_Battery_SoC_Glossary.md`. For the full detail, those two docs are the source of truth — this is the simplified version.

---

## The big picture

The firmware doesn't have a magic "fuel gauge" chip telling it the battery percentage. It only has two raw signals — battery **voltage** (`vb`) and battery **current** (`ib`), sampled 10 times a second. Everything else is calculated from those two numbers, plus a handful of assumptions/settings that were typed into a config file once and never change.

It actually computes **two independent, competing estimates of SoC** every cycle, then blends them together:

1. A **voltage-based guess** ("if the battery reads this voltage, it's probably about this full")
2. A **coulomb-counting guess** ("we've measured X amount of energy leave the battery since it was full, so it should have Y% left")

---

## Estimate #1: Voltage-based (`VBnl` / `VBnlState`)

This is a lookup-table approach, like a car's fuel gauge that reads the float level rather than tracking gallons pumped.

- Raw voltage under load isn't a reliable indicator by itself, because voltage sags under load and recovers when the load is removed. So the firmware first **estimates what the voltage would be if there were no load at all** (`vnl`) by:
  - Adding back a correction for the voltage drop caused by internal resistance (`ESR`) at the current draw.
  - Adding a small correction for outside air temperature (`vtempco`, referenced to `tzero`).
- That corrected "resting" voltage is then run through a **lookup table** (`bnl_volts` → `bnl_life`) — 10 fixed voltage/percentage pairs (e.g. 23.75V→0%, 25.9V→13.6%, 29.32V→100%) that were characterized once for this battery type and hardcoded into the config. Whatever percentage the table says for the current corrected voltage becomes `VBnlState`.
- **This table lookup only actually runs when the aircraft is basically idle** — current draw below `bnl_ilim` (0.5A on this airframe). Under real load, a different, cruder correction table (`table[]`) is used instead, but the concept is the same: voltage in, percentage out, via a table.

**You're always getting a voltage-in/percentage-out lookup — `ib` vs. `bnl_ilim` just decides which of two hardcoded curves is used:**

| Current draw | Method | What it is |
|---|---|---|
| `ib ≤ bnl_ilim` (0.5A, resting) | Direct table interpolation | The 10-point `bnl_volts`→`bnl_life` table described above |
| `ib > bnl_ilim` (loaded) | Straight-line formula + table correction | A straight-line percentage between `batt.vblow`/`batt.vbhigh`, plus an offset added from a *second* hardcoded table (`table[]`, 21 points, one per 5% bucket) to correct for the fact a real discharge curve isn't perfectly straight |

Either way, the input is the same corrected/no-load voltage (`vnl`), and the output feeds `VBnlState` the same way — so conceptually both branches are just "a fixed, pre-characterized voltage→percentage curve," represented two different ways.

**Key thing to know:** this method reacts to voltage, and voltage can rebound/relax upward for a while after a load is removed — even with zero new charge added. The table doesn't know the difference between "genuinely charged more" and "just relaxing."

---

## Estimate #2: Coulomb-counting (`WHused`, `AHused`, `WHState`)

This is the "gas gauge that tracks gallons pumped" approach — much more like accounting.

- Every cycle, the firmware multiplies voltage × current to get power, and adds it up over time: `WHused` (Wh) and `AHused` (Ah) are just running totals of energy/charge that have left the battery since it was armed.
- It also separately tracks `EsrEnergy` — energy that's dissipated as heat inside the battery's own internal resistance, which never shows up as usable output power but still came out of the battery chemically.
- To turn "amount used" into "percent remaining," it needs to know the pack's total capacity to divide by. That number is `batt.wh` — **a single fixed number (175 Wh on this airframe), typed into the config file once, and never changed for any reason.** There's no cycle counter, no aging adjustment, nothing — it's just a constant.

$$WHState = \frac{batt.wh - (WHused + EsrEnergy)}{batt.wh}$$

**Key thing to know:** this method is blind to the physical battery's real, current capacity. If a specific battery has actually degraded and can't really hold 175Wh anymore, this formula has no way to find out — it will always assume the pack is still like-new.

---

## Blending the two: `FusedState` / `BattState` and `LostCap`

This is the part that actually gets displayed to the user (`BattState`), and it's a bit more involved.

Rather than picking one estimate over the other, the firmware tries to make the coulomb-counting estimate "agree" with the voltage-based estimate, whenever the aircraft is resting (current below `bnl_ilim`). It does this with a correction term called `LostCap` (`lostcapacity`):

$$FusedState = \frac{batt.wh - (WHused + EsrEnergy + LostCap)}{batt.wh}$$

- `LostCap` starts at zero and is continuously nudged up or down (a simple feedback/PI controller, gains `bsfkp`/`bsfki`) so that the formula above keeps landing close to whatever the voltage-table estimate (`VBnlState`) currently says.
- **This nudging only happens while resting.** Once the aircraft is drawing real current again (flying), `LostCap` freezes at whatever value it last reached and just rides along unchanged until the next rest period.
- On this airframe's config, `BattState` (what you see on the GUI) is set to be **identical** to `FusedState` — they're the same number.

**Net effect in plain terms:** whenever the aircraft sits still after landing, the displayed battery percentage will keep chasing the resting-voltage estimate, even though `WHState` (pure coulomb counting, no `LostCap` term) stays put. That's the mechanism behind the two numbers drifting apart the longer the aircraft sits.

---

## What's fixed vs. what's live, at a glance

| This... | ...is fixed (never changes) | ...is live (recalculated constantly) |
|---|---|---|
| `batt.wh` (175 Wh) — the capacity everything divides by | ✅ | |
| `batt.ah` (6.5 Ah) — configured but **not actually used** in the real calculation at all | ✅ | |
| The voltage↔percentage lookup tables (`bnl_volts`/`bnl_life`, `table[]`, `topv`/`toplife`) | ✅ | |
| `ESR`, `vtempco`, `bnl_ilim`, PI gains (`bsfkp`/`bsfki`) — all the tuning knobs | ✅ | |
| `WHused`, `AHused`, `EsrEnergy` — running totals since arm | | ✅ |
| `VBnl`, `VBnlState` — voltage-based estimate | | ✅ |
| `LostCap` — the correction term, but only updates while resting | | ✅ (partially — frozen while flying) |
| `FusedState`/`BattState` — final displayed number | | ✅ |

---

## One-paragraph summary

The GUI's battery percentage is really two different math approaches (a voltage lookup table, and an energy-accounting running total) blended together by a feedback loop that forces them to agree whenever the aircraft is sitting still. Both approaches ultimately divide by the same single hardcoded capacity number (`batt.wh` = 175 Wh) that never adjusts for how worn a specific battery actually is, and the voltage-based side is additionally sensitive to normal battery voltage rebound after landing — which the blending logic can't distinguish from real charge.
