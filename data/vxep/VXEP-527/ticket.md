# VXEP-527: VXE 469 Uncommanded aborted VTOL launch at 100ft AGL

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-08-06
- **Updated:** 2026-08-14
- **Resolved:** 2024-08-07
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** MARSOC, Software
- **Links:** relates to VXEP-1066 (VXE 448 Multiple Aborted takeoffs)
- **Customer:** MARSOC
- **Vehicle Tail Number:** 469
- **Corrective Action:** None required
- **Other Stakeholder (as required):** David Grosher
- **Issue Status:** Complete
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

From operator:
Aircraft performed an uncommanded aborted launch at 100 ft AGL.

Operator received “Climb abort, VTOL controller fault Sensor: GPS Fault” On VTOL Control panel. 

Note:  Operator stated that they have a Raspberry pie, HackRF One, and a GPS antenna puck with magnetic mount attached to tailboom.  https://greatscottgadgets.com/hackrf/one/ 
AAR Attached

## Plan

- @Pat Wells to get and fill in more details about payload configuration. Operator reported GPS fault. HackRF one is known to interfere with GPS. This behavior may be expected.
- Data review

## Root Cause

Degradation of GPS below threshold caused launch abort, per design. Likely cause is the listed extra equipment, some known to cause GPS interference.

## Comments (5)

### Greg Fryer, 2024-08-06

Moved to you @David Grosher . @Pat Wells Also get a location and strength of the magnet on the boom, if it was close to avionics it could have messed up the magentometer.

### Pat Wells, 2024-08-07

@David Grosher operator provided another AAR from an aborted launch today 8/7. Also a screenshot from VTOL Control window on GCS. 
I took a quick look at both logs and noted that during VTOL climbout the CNo dropped deep into the 30’s in both instances.  At that point the aircraft began descending and landed.

### David Grosher, 2024-08-07

@Pat Wells The aircraft will abort when the average of the top three CN0 values drop below 40. It is behaving as designed. They need to inspect the hardware they are putting on the vehicle and do proper interference checks. I suggest we cancel this ticket.

### Pat Wells, 2024-08-07

@David Grosher yes I was tracking that it would abort under those circumstances.  That’s what led me to look where I did. 
@Greg Fryer are you ok with closing this out?

### Greg Fryer, 2024-08-07

@Pat Wells Absolutely. I’ll fill in the fields and close.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V469_240806_095846_pack.zip | archive | 1399 | 2024-08-06 | listed only |
| Image.jfif | image | 1673 | 2024-08-07 | listed only |
| T95_V469_240807_062121_pack.zip | archive | 937 | 2024-08-07 | listed only |
