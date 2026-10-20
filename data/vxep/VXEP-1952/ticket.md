# VXEP-1952: MAIM will not see satellites from novatel, aircraft attitude indicators do not update

- **Issue type:** Bug
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2026-07-07
- **Updated:** 2026-09-15
- **Resolved:** 2026-09-15
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Scott Whitney
- **Creator:** Alexander Alan Arnold
- **Links:** relates to FS2-4232 (MAIM/XCOMM - Handle Novatel Reset in Launch Wizard); relates to FS2-4877 (MAIM fix Progression Test)

## Description

Tested a MAIM on SW rev 30202 on an aircraft that had the 6.6.1 FW (VXE30 ADV ANV) loaded and were unable to see satellites on the MAIM GUI (241212) this happened inside using repeaters and outside the HSV office with real-world satellites. Verified in SUAV and OGCS the aircraft was reporting position data inside and outside the building. 
we swapped to an avionics that had AP FW version 6.05t, and XCOMM 4.73 and we were able to see satellites and aircraft attitude updates in the MAIM GUI inside using repeaters and outside the building. The CW was on 1.58.00 0x1d26 since I did not have time to revert a test CW to 6.5.1 Firmware 

MAIM GUI installed on SGCS1-383 with hardened image close to customer that first said they had issues (USAACE, 2/13th)
VXE 1002 is the 30 ADV NAV on 6.6.1 
VXE 818 is 35x with 6.5.1 FW 

Please let us know if the AARs need to be longer or other testing needs to be done

## Comments (4)

### Greg Fryer, 2026-07-07

@Scott Whitney Believe you have this already, so if it duplicates work already documented you can cancel this or just move it to whatever state is apropriate.
@Alexander Alan Arnold FYI

### Alexander Alan Arnold, 2026-07-07

@Scott Whitney If this work is already being tracked can you please provide a link to the work items so we can be made aware of it to bettter provide updates to vendors and customers as they encounter this issue?

### Scott Whitney, 2026-07-08

@Alexander Alan Arnold link https://jenaero.atlassian.net/browse/FS2-4232 . We are currently working on addressing the issue

### Alexander Alan Arnold, 2026-09-15

closed as new maim FW and VXE SUAV build alleviate issue

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 4.73 xcomm with MAIM.jpg | image | 4185 | 2026-07-07 | listed only |
| AAR_V1002_B30N_20260707T205047Z.zip | archive | 55605 | 2026-07-07 | listed only |
| AAR_V818_B35X_20260707T221821Z.zip | archive | 10159 | 2026-07-07 | listed only |
| MAIM_NO_SATS.png | image | 79 | 2026-07-07 | listed only |
| MAIM_SW.jpg | image | 8641 | 2026-07-07 | listed only |
| T115_V1002_260707_122407_pack.zip | archive | 5056 | 2026-07-07 | listed only |
