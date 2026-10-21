# Report 03: Image trial on 10 tickets

- **Prompt:** `prompts/03_image_trial.md`
- **Branch:** `agent/wednesday`
- **Started from commit:** `c3a669c`
- **Outputs:** `results/03_image_trial.jsonl` (10 lines) and this report. `scripts/check_results.py` was extended for image evidence; it passes on the new file and still passes on `results/02_all.jsonl`.
- **Method:** done in this session without sub-agents, as asked. Each result starts from `results/02_all.jsonl`, and each image was looked at once. No ticket text had to be re-read. Image evidence is my reading of the image, except where a quote is marked as text printed on the image.

## Results

| Ticket | What the image showed | Effect | Outcome 02 to 03 |
| --- | --- | --- | --- |
| VXEP-1066 (plot) | GPS speed and horizontal accuracy (sAcc about 13 against 1.5, hAcc about 5.7 against 5.0) tripped the abort at the top of the climb. Signal strength (C/N0) stayed above 40 until after the abort. | narrowed_further | narrowed, unchanged |
| VXEP-897 (plot) | FWAP and VTOL AP attitudes split at 18:21:35: heading sharply, roll by about 20 degrees, pitch by 10 to 27 degrees. No magnetometer channel. | supports | narrowed, unchanged |
| VXEP-1462 (plot) | VTOL GPS satellite count stepped from 33 straight to 0 and stayed there. No heartbeat trace. | supports | narrowed, unchanged |
| VXEP-231 (plot) | For about 17 s the BMS read about 27.6 V while the VTOL side fell to 19 to 27 V, a gap of up to about 8 V. | supports | narrowed, unchanged |
| VXEP-1489 (plot) | At the landing transition, lift throttles were commanded to 0.6 to 0.95 with battery current near 0 A and the voltage sagging about 2 V. | supports | narrowed, unchanged |
| VXEP-426 (plot) | Motor 3 (rear right) command held at the bottom for about 3.5 s, then stepped up. No y-axis values, no motor current. | supports | narrowed, unchanged |
| VXEP-1977 (plot) | Motor 3 (rear right) command saturated at about 0.9 from 791.5 s while motor 1 dropped, just before the pitch up to 33.75 degrees. | supports | narrowed, unchanged |
| VXEP-279 (photo) | A charred heat-shrink and wire lump in the nose bay. No board or part can be identified. | no_help | narrowed, unchanged |
| VXEP-1458 (photo) | The fire aftermath laid out on concrete: several burned battery packs, chargers and cables. The blue power supplies are mostly intact. | no_help | not_determined, unchanged |
| VXEP-538 (photo) | The cutter handle's steel shank snapped where it enters the grip; jaws and pivot intact; label 100-104453. | narrowed_further | narrowed, unchanged |

## Counts

| Effect | All 10 | Plots (7) | Photos (3) |
| --- | --- | --- | --- |
| settled | 0 | 0 | 0 |
| narrowed_further | 2 | 1 | 1 |
| supports | 6 | 6 | 0 |
| contradicts | 0 | 0 | 0 |
| no_help | 2 | 0 | 2 |

No outcome or confidence changed. The two `narrowed_further` results changed only `component` and `failure_mode`.

## What this changes in report 02

- **VXEP-1066.** The abort tripped on GPS accuracy, not signal strength. Report 02 grouped it with "GNSS quality" aborts; within that group, signal strength and accuracy are different checks, and this one was accuracy.
- **VXEP-897.** The plot shows roll and pitch disagreeing by up to about 20 degrees as well as heading. A disturbed magnetometer explains heading most directly, so the gimbal interference reading stays a suspicion, as report 02 said.
- **VXEP-231 and VXEP-1489.** The plots show what the team described (an 8 V battery-to-VTOL gap; voltage sag with no current). This firms up "the HLB power path" but cannot pick a contact.
- **File names.** Two images were exported with a different extension from the ticket (`image-20240217-054529.png` became `.jpg`; `MAIN fire (1).jpeg` became `.jpg`). Worth knowing when matching files to `would_settle_it`.

## Recommendation

Not worth doing the rest of the list as it stands.
- **Plots** firm up results that were already right, but never got past the open question. That question is usually which part, which a plot of a symptom cannot show.
- **Photos** of fire damage could not show the origin, though the one fracture photo did show where the part broke.

If any more are done, I suggest only a short list:
- **Mechanical damage photos** where the open question is where or how a part broke: VXEP-1506, 1902 and 1889 from the report 02 list. (VXEP-2024 is an HLB fire, so it is left out.)
- **Plots whose `would_settle_it` asks which input or which check tripped**, where the image is likely to name the channel: VXEP-1465, 1906, 1929, 1566 and 1881.

That is 8 tickets, not 59. The bigger open questions (which contact, which board, why) need the AAR data or the hardware, which images do not replace.

## Cost

The 10 tickets used a small part of the session: about 50,000 tokens of context in all, including reading the prompt and extending the check script. The ten images were about 15,000 of that, and no sub-agents were used. At that rate the other 59 would cost about 6 times this trial, so they would likely need more than one session under the current limits. The short list above would fit in one session like this one.
