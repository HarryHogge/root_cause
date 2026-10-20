# VXEP-2008: V979 OGCS and Battery Checker Discrepancy

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2026-09-25
- **Updated:** 2026-10-05
- **Resolved:** 2026-10-05
- **Reporter:** Jeremy Kostel
- **Assignee:** Ben Norris
- **Creator:** Jeremy Kostel
- **Links:** relates to VXEP-720 (VXE 490 main battery percentage reporting incorrectly during flight with MB's (S/N's 1967 and 1737)); relates to SMUP-50 (Guidance and manual updates for battery checker based on SoC being for wrong battery chemistry)

## Description

Customer reports significant discrepancies between physical battery testers and the OGCS/SUAV GUI battery capacity readings on multiple batteries and aircraft.
Initial report from AV 979 shows a 33% difference between post‑flight GUI and tester readings (GUI reading much higher).
Follow‑on testing with a second battery (SN: 3‑2641) confirms a persistent 14–15% GUI over‑report bias, independent of software version.
Field support hinted this may be a systemic issue, but engineering has no prior awareness — needs clarification.
Observed data:
- Battery SN: 3‑2620, flight 1.6 hrs at 1500 AGL
- Pre‑flight: 97% tester / 96% GUI
- Post‑flight: 14% tester / 47% GUI
- Battery SN: 3‑2641 follow‑on test:
- 57% tester → 71% GUI → 70% GUI (older SW) → 55% tester after disconnect

Customer seeks explanation for the discrepancy and guidance on next steps.

## Plan

- Gather standard B30 HLB and MB
- Charge both to full
- Perform full discharge to establish capacity and SoC curve
- Charge both to full
- Check batteries via production battery checker
- Record all reported values
- Connect batteries to Iron bird and OGCS
- Record all reported battery values
- Discharge batteries to 75%
- Record batt values from OGCS
- Record batt values from batt checker
- Discharge batteries to 50%
- Record batt values from OGCS
- Record batt values from batt checker
- Discharge batteries to 25%
- Record batt values from OGCS
- Record batt values from batt checker
- Discharge batteries to 10%
- Record batt values from OGCS
- Record batt values from batt checker

## Issue Status

Closing this ticket - see linked tickets. This has already been addressed and should have been corrected by new verbiage in the ops manual. Battery Checker assumes different battery chemistry and should not be used to evaluate SoC independently (still useful for voltage, cell voltages and imbalance, and any temps it may show)

## Comments (4)

### Jeremy Kostel, 2026-09-25

@Jackson Riley Curvin Can we get info from customer on cycle count of these batteries?

### Scott Whitney, 2026-09-28

FYSA:@Taylor Warner @Ted Trowbridge

### Jeremy Kostel, 2026-10-02

Ive traced down in the software how the aircraft calculates SoC. Attached are two markdown files explaining the basics behind the principles. 
Note for HLB: we use a fixed battery capacity value (batt.wh=175) this does NOT account for pack degradation over various cycles which can lead to an over estimation
Note for MB: we use a fixed ESR constant along with a lookup table

Ben and Kurt mentioned battery checkers we sell use a generic discharge curve, and likely arent very accurate for our batteries.
Discrepancy might come from a mix of voltage checker under reporting and aircraft overreporting. Needs testing to verify

[embedded: B30_HLB_SoC_Cheat_Sheet.md][embedded: B30_MB_Legacy_SoC_Cheat_Sheet.md]

### Jeremy Kostel, 2026-10-02

@Ben Norris this will be a good task to get started next week. I laid out a pretty basic plan in the field above, feel free to check it out and modify as needed

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V979_20260923T180441Z.zip | archive | 21132 | 2026-09-25 | listed only |
| [AE674129XT Cell Spec Sheet 3300 70C (1).pdf](attachments/64886_AE674129XT%20Cell%20Spec%20Sheet%203300%2070C%20(1).pdf.md) | pdf | 3230 | 2026-09-25 | converted |
| [B30_HLB_SoC_Cheat_Sheet.md](attachments/65030_B30_HLB_SoC_Cheat_Sheet.md.md) | text | 8 | 2026-10-02 | converted |
| [B30_MB_Legacy_SoC_Cheat_Sheet.md](attachments/65031_B30_MB_Legacy_SoC_Cheat_Sheet.md.md) | text | 5 | 2026-10-02 | converted |
