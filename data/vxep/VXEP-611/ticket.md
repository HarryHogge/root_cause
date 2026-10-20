# VXEP-611: VXE 688 on landing transitioned to VTOL, aircraft continues forward flight and crashes into a mountain

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-09-05
- **Updated:** 2026-09-14
- **Resolved:** 2025-08-12
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** Crash, Mismatched_SW/FW, PMA263, Training, Weekly-incident-tracker
- **Links:** relates to VXEP-605 (VXE 572 Multiple uncommanded aborted launches); relates to FS2-2321 (Create a consolidated report on mismatched SW/FW versions for VXE-572/573/574/628/688/594); relates to RMA-366 (VXE-688 241003-2); is cloned by VXEP-896 (CLONE - VXE 688 Launch Aborts )
- **Customer:** PMA263
- **Vehicle Tail Number:** 688
- **Corrective Action:** - Follow ADs to properly maintain the aircraft and ensure that all SW/FW is properly updated.
- **Plan:** Get vehicle data for last flight from XCOMM and VTOL AP from crashed vehicle. @Pat Wells @Sean Odell
- **Root Cause:** - Operator Error: Did not follow ADs to maintain the vehicle.
- **Incident Type:** Aircraft Damage
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

This incident is part of the mulitiple incidents recently reported by operator at 29 Palms.

Statement from operator:
Brand new, never been flown before, comes in for a landing, VTOL motors kick on, however it never stops flying forward, it never halts over the landing spot and continues to fly full speed, straight until it impacted a mountain.
Multiple AAR’s attached as operator is unable to determine which file corresponds to the incident.
VXE688 also had numerous launch aborts. The analysis of this shows the VTOL firmware was well out of date and inconsistent with the FW on the XCOMM and FW AP. This will likely play a role in the incident during landing as well. 
Also the CW flown appears to have been a spare that was quite old given the firmware version loaded on it.

## Comments (11)

### David Grosher, 2024-09-05

@Pat Wells 
Initial finding that the versions were changed in the middle of operations on 8/20, but only on the XCOMM.  Similar Mag and LRF issues causing RTL as with 572, perhaps environmental issues in the area of operations. There are no obvious issues with the mag data on the VTOL. GPS looks fine (although CNo is not in the logs in this older version). 
[embedded: image-20240905-215524.png]
Also strange is that the CW number was 1.

### David Grosher, 2024-09-06

@Pat Wells This is analysis from @Scott Hunter 
Every VTOL CSV file from VXEP-611 would fail the ratio test at margin=0.25 and would pass with margin=0.6. There are 6 config files that have ImuConfig.magmargin and they're all set to 0.250. Based on the comment in the GIT log I believe 0.25 is the default for this older version of code (1.44). I didn't bother to take the time to figure out which file represents actual flights etc. since they'd all fail the margin=0.25 test.  This is a change that was delivered in v6.0.12 of the GCS (v1.52 of the VTOL). Perhaps the Mag wasn’t calibrated or there may have been EMI noise in the environment due to the training exercise. 
 
Note: Expected mag field from the event log is logged as [23:28:32.777] field: 0.467139
 
[embedded: image-20240906-143735.png]

### Cody Smisek, 2024-11-07

@David Grosher should aircraft still be held in engineering or is engineering investigation complete?

### Alexander Alan Arnold, 2025-01-10

@David Grosher Since this is apart of the FW/SW mismatch group should this be investigated further/ moved to D6 since we are just waiting on the consolidated report?

### David Grosher, 2025-01-10

@Alexander Alan Arnold Yes, good catch. I moved it as requested.

### David Grosher, 2025-01-10

@Alexander Alan Arnold Giving it a closer look. I think we need to investigate the first few aborted launches prior to the firmware update that led to mismatched software. Things of note: the CW serial number seemed wrong, like it was factory reset.  And the Mag issues that presented prior to the change.

### Alexander Alan Arnold, 2025-01-10

Should we create a separate problems ticket for that investigation so the mismatch problem tickets that are linked together can be moved together? @David Grosher

### David Grosher, 2025-01-10

@Alexander Alan Arnold That sounds like a good idea.

### David Grosher, 2025-05-19

Downgraded from flight critical due to the unsupported configuration of the firmware on the aircraft.

### Christa Meck, 2025-08-05

@David Grosher What is the status of this investigation?
Leaving open until 12 Aug for feedback.

### Christa Meck, 2025-08-12

No additional feedback.  Closing.

## Attachments (12)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V688_240819_234620_pack.zip | archive | 161 | 2024-09-05 | listed only |
| T95_V688_240820_000311_pack.zip | archive | 1820 | 2024-09-05 | listed only |
| T95_V688_240820_001726_pack.zip | archive | 1717 | 2024-09-05 | listed only |
| T95_V688_240820_005554_pack.zip | archive | 1335 | 2024-09-05 | listed only |
| T95_V688_240820_011118_pack.zip | archive | 2010 | 2024-09-05 | listed only |
| T95_V688_240820_093313_pack.zip | archive | 759 | 2024-09-05 | listed only |
| T95_V688_240820_095612_pack.zip | archive | 2599 | 2024-09-05 | listed only |
| T95_V688_240820_102957_pack.zip | archive | 1917 | 2024-09-05 | listed only |
| T95_V688_240820_105200_pack.zip | archive | 1620 | 2024-09-05 | listed only |
| T95_V688_240820_154750_pack.zip | archive | 1173 | 2024-09-05 | listed only |
| image-20240905-215524.png | image | 41 | 2024-09-05 | listed only |
| image-20240906-143735.png | image | 1220 | 2024-09-06 | listed only |
