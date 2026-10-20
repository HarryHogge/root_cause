# VXEP-896: CLONE - VXE 688 Launch Aborts

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-01-10
- **Updated:** 2026-10-08
- **Resolved:** 2026-10-08
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** Crash, PMA263, Training, Weekly-incident-tracker
- **Links:** clones VXEP-611 (VXE 688 on landing transitioned to VTOL, aircraft continues forward flight and crashes into a mountain); relates to VXEP-605 (VXE 572 Multiple uncommanded aborted launches); relates to FS2-2321 (Create a consolidated report on mismatched SW/FW versions for VXE-572/573/574/628/688/594); relates to RMA-366 (VXE-688 241003-2)
- **Customer:** PMA263
- **Vehicle Tail Number:** 688
- **Corrective Action:** Follow published airworthiness directives.
- **Plan:** Get vehicle data for last flight from XCOMM and VTOL AP from crashed vehicle. @Pat Wells @Sean Odell
- **Issue Status:** Closed. The launch aborts were due to the Mag thresholds on the older version of firmware.
- **Root Cause:** The aircraft was using outdated and mismatched software/firmware.
- **Incident Type:** Aircraft Damage
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Created from VXEP 611 to keep all SW mismatch AVs grouped together during investigation and reporting process since David G. recommended looking into the areas below  
”Giving it a closer look. I think we need to investigate the first few aborted launches prior to the firmware update that led to mismatched software. Things of note: the CW serial number seemed wrong, like it was factory reset. And the Mag issues that presented prior to the change.”

Statement from operator:
Brand new, never been flown before, comes in for a landing, VTOL motors kick on, however it never stops flying forward, it never halts over the landing spot and continues to fly full speed, straight until it impacted a mountain.
Multiple AAR’s attached as operator is unable to determine which file corresponds to the incident.
VXE688 also had numerous launch aborts. The analysis of this shows the VTOL firmware was well out of date and inconsistent with the FW on the XCOMM and FW AP. This will likely play a role in the incident during landing as well.
Also the CW flown appears to have been a spare that was quite old given the firmware version loaded on it.

This incident is part of the multiple incidents recently reported by operator at 29 Palms.

This ticket is tracking the multiple launch aborts. 
Note: The aircraft was using outdated and mismatched software/firmware.

## Comments (3)

### Alexander Alan Arnold, 2025-01-10

@David Grosher Created a clone of the original problem ticket for the investigation into the areas you mentioned on the original.

### David Grosher, 2025-02-18

The attached image above clearly shows that all of the aborted launches were because they were running old VTOL software with limits that were failing in their environmental conditions. Had they been using the new firmware then they would have been able to launch.  Note: they downgraded the XCOMM firmware, which is an unsupported process in the middle of their launch aborts. Instead they should have updated the VTOL AP.

### David Grosher, 2025-02-18

@Pat Wells I think we can close this issue.

## Attachments (12)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V688_240819_234620_pack.zip | archive | 161 | 2025-01-10 | listed only |
| T95_V688_240820_000311_pack.zip | archive | 1820 | 2025-01-10 | listed only |
| T95_V688_240820_001726_pack.zip | archive | 1717 | 2025-01-10 | listed only |
| T95_V688_240820_005554_pack.zip | archive | 1335 | 2025-01-10 | listed only |
| T95_V688_240820_011118_pack.zip | archive | 2010 | 2025-01-10 | listed only |
| T95_V688_240820_093313_pack.zip | archive | 759 | 2025-01-10 | listed only |
| T95_V688_240820_095612_pack.zip | archive | 2599 | 2025-01-10 | listed only |
| T95_V688_240820_102957_pack.zip | archive | 1917 | 2025-01-10 | listed only |
| T95_V688_240820_105200_pack.zip | archive | 1620 | 2025-01-10 | listed only |
| T95_V688_240820_154750_pack.zip | archive | 1173 | 2025-01-10 | listed only |
| image-20240905-215524.png | image | 41 | 2025-01-10 | listed only |
| image-20240906-143735.png | image | 1220 | 2025-01-10 | listed only |
