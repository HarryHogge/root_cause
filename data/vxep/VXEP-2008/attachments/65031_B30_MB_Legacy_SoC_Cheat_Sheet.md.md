# B30_MB_Legacy_SoC_Cheat_Sheet.md

Attachment 65031, text, 5 KB, added 2026-10-02 by Jeremy Kostel.

# B30 MB SoC — Legacy Cheat Sheet (B30's Actual Configuration)

A simplified, no-code explanation of how the firmware calculates the Main Battery (MB) percentage **as actually configured on B30**. This is a trimmed-down variant of `B30_MB_SoC_Cheat_Sheet.md` — that doc describes everything the firmware *supports*, including a smart-BMS-connected pack; **B30 does not have a smart Main Battery / BMS at all.** It's a legacy, "dumb" pack — just cells wired straight to the aircraft's own analog voltage/current sensing, with no onboard battery-management chip talking back over CAN. So all of the smart-battery-specific logic (BMS telemetry preference, the 2-D current/temperature ESR table, EEPROM-sourced override bits) never comes into play for this airframe. This doc only covers the code path that's actually live on B30.

---

## The big picture

MB's percentage is computed on the **legacy "green board" fixed-wing autopilot** (`fixed-wing-ap`), in `Energy::CalcVBLife()` — a completely separate codebase from HLB's (which runs on the VTOL "red board," `autopilot_202`).

Like the general/smart-battery-capable version of this algorithm, MB's estimate is **voltage-only** — no coulomb-counting, no blending, no feedback loop. The difference on B30 is simply *where the voltage and ESR numbers come from*: since there's no smart battery to ask, the firmware always falls back to its own raw analog sensor and a single fixed config value, never the BMS-preferred path.

---

## Where the voltage comes from

Just the aircraft's own analog voltage sensor (`sensors->VBatt()`). There's no competing "preferred" smart-battery reading to choose between — the smart-battery data path simply never reports anything valid on this airframe, so the firmware is always on what would otherwise be called the "fallback."

---

## Step 1: IR-drop correction (estimating no-load voltage)

Same concept as HLB: battery voltage sags under load, so the firmware adds back an estimate of the drop across the battery's internal resistance:

$$V_{corrected} = V_{batt} + I_{batt} \times ESR$$

Without a smart battery to report live current/temperature-dependent ESR, `ESR` here is just **one fixed configured number**: `Batt ESR (mOhm) = 20` on B30. No lookup table, no temperature dependence — just a constant.

---

## Step 2: Linear map between empty and full

$$life_{linear} = \frac{V_{corrected} - V_{zero}}{V_{full} - V_{zero}} \times 100\%$$

On B30:
- `V_{full}` = **28.7 V**
- `V_{zero}` = **23.5 V**

These come straight from the fixed-wing AP's own local config (`FW-BLK30-Flight.txt`) — there's no BMS EEPROM to send alternate values, so these numbers are simply fixed for the life of the config file.

The result is clamped to 0–100% before the next step.

---

## Step 3: Nonlinear correction curve

A straight line between empty and full voltage doesn't match a real Li-ion discharge curve, so a hand-tuned correction is added on top, looked up in 5%-wide buckets:

$$life_{final} = \text{clamp}\big(life_{linear} + Table\left[\tfrac{life_{linear}+2}{5}\right],\ 0,\ 100\big)$$

B30 uses **`LiPoTable30`** ("block30 monster pack") — confirmed active via the `Use VXE30 Discharge Curve = 1` config flag. This table was specifically hand-tuned for this pack and is a fixed, hardcoded set of 22 correction values — it doesn't change at runtime.

---

## What about capacity / energy used? (`BattWTotal` / Endurance)

Same as the general version of this algorithm: the firmware tracks a running energy-used total against a configured capacity (**1400 Wh** on B30 — `Batt Capacity = 5040 ×1000 W·s`), but **this only drives the Endurance-in-minutes estimate, never the displayed SoC%.**

**Practical consequence (same as before):** MB's percentage can't be biased by a worn/faded pack's real capacity being lower than the nameplate number, because the percentage calculation never divides by capacity at all — that's purely a voltage calculation. HLB's "stale nameplate capacity" root cause doesn't apply here.

---

## What's fixed vs. what's live, at a glance

| This... | ...is fixed (config, never changes on B30) | ...is live (recalculated constantly) |
|---|---|---|
| `V_{full}` / `V_{zero}` (28.7 V / 23.5 V) | ✅ | |
| `ESR` (20 mOhm, single constant) | ✅ | |
| Correction curve (`LiPoTable30`) | ✅ | |
| `BattWTotal` (1400 Wh capacity) | ✅ | |
| Live voltage/current from the aircraft's own analog sensor | | ✅ |
| `BattVLife` — final displayed MB percentage | | ✅ |
| `Endurance` (minutes remaining) — separate from `BattVLife` | | ✅ |

---

## One-paragraph summary

On B30, MB's displayed battery percentage comes from the aircraft's own analog voltage/current sensing only — there's no smart battery/BMS hardware in the loop at all, so the more sophisticated current/temperature ESR table and EEPROM-sourced override values described in the general software reference simply never apply here. The calculation is: IR-drop-corrected voltage (using one fixed ESR constant), linearly mapped between fixed empty/full voltages (23.5 V / 28.7 V), then nudged by the hand-tuned, pack-specific `LiPoTable30` correction curve. As with the general version, this percentage is completely decoupled from the separate energy-used/capacity bookkeeping, so it can't suffer from HLB's stale-capacity bias — but it likely still carries HLB's other risk (trusting a voltage reading before it's fully settled after a load change), unconfirmed against a real MB flight log.
