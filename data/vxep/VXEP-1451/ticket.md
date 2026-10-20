# VXEP-1451: Fuel Cell Erroneous Update message for 6.5

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Won't Do
- **Priority:** Highest
- **Created:** 2025-07-24
- **Updated:** 2026-08-18
- **Resolved:** 2026-08-18
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Ted Trowbridge
- **Creator:** Alexander Alan Arnold
- **Labels:** GS_Closed, Software, USASOC, Weekly-incident-tracker
- **Links:** relates to GCSS-444 (Fuel Cell Erroneous Update Detected); relates to RMA-758 (D4500604 RMA 250805-1 )
- **Customer:** USASOC
- **Vehicle Tail Number:** VXE-557
- **Severity:** 3 - Degraded Performance - With Workaround
- **Executive Summary:** Awaiting fix from software team. No other issues reported. RMA was completed.

## Description

We are seeing with a 3rd Group-owned Fuel Cell. We were unable to take-off the aircraft due to a possible false "error" that is displaying in the Aircraft Status Panel.

## Comments (8)

### Ted Trowbridge, 2025-07-29

@Alexander Alan Arnold 
It would appear there are two issues here:
- There is a legitimate fuel cell fault present.
- Both AARs contain fuel cell logs with the following error: 25632 Temperature inside Fuel Cell Below Operational Threshold.
- On Ground Action: Fuel Cell below threshold for safe startup, allow to soak at elevated temperature (greather than -20°C).
- In Flight Action: Command Aircraft to Return to Base (RTB), and Select "Start" in Fuel Cell Dialog
- There is an issue detecting fuel cell firmware updates.
- We will need to investigate why the firmware update detection uses the wrong ‘Build Name’.
- Any fix would likely need to be part of a GCS release.  It is possible an INI change could be used as a workaround but that needs investigation.

### Drew Hildreth, 2025-08-26

@Jackson Riley Curvin @Michael Mohr What is going on here? Do we need to RMA the SOFC for the AA Team to look into more?

### Michael Mohr, 2025-08-26

@Drew Hildreth Rodney sent out the RMA on 08/05/25 to get this and others shipped back for the AN-25-005. @Sean Wendling Did AA ever receive this fuel cell and/or the other seven? (D4500598, D4500523, D4500594, D4500624, D4500518, D4500603, D4500601)

### Jackson Riley Curvin, 2026-01-20

@Ted Trowbridge  are there any updates with this?

### Ted Trowbridge, 2026-08-18

@Jackson Riley Curvin @Alexander Alan Arnold 
Is this still an issue?  Can we transition this issue towards being closed?

### Alexander Alan Arnold, 2026-08-18

@Ted Trowbridge I haven't heard or received other reports of this if your recommendation is to close it we will. We can reopen if it happens again with the next fuel cell update. should I put it in a canceled status?

### Ted Trowbridge, 2026-08-18

@Alexander Alan Arnold it has been over a year with no updates and the original fuel cell from the report seemed to have other issues.  I would recommend closing and only re-open if we get more info.

### Alexander Alan Arnold, 2026-08-18

Closing ticket since fuel cell generating error has been RMAd. will reopen if issue appears again

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Error Message final.PNG | image | 539 | 2025-07-24 | listed only |
| T95_V557_250723_110639_pack (1).zip | archive | 1347 | 2025-07-24 | listed only |
| T95_V557_250723_141823_pack (1).zip | archive | 847 | 2025-07-24 | listed only |
| Update Screenshot.PNG | image | 201 | 2025-07-24 | listed only |
| Version.PNG | image | 205 | 2025-07-24 | listed only |
