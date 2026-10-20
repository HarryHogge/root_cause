# VXEP-605: VXE 572 Multiple uncommanded aborted launches

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-09-05
- **Updated:** 2026-09-14
- **Resolved:** 2025-02-14
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** Mismatched_SW/FW, No_crash, PMA263, Training, Weekly-incident-tracker
- **Links:** relates to VXEP-611 (VXE 688 on landing transitioned to VTOL, aircraft continues forward flight and crashes into a mountain); relates to FS2-2321 (Create a consolidated report on mismatched SW/FW versions for VXE-572/573/574/628/688/594); relates to RMA-365 ( VXE-572 241003-1); relates to VXEP-896 (CLONE - VXE 688 Launch Aborts ); relates to FS2-2837 (Investigate VXEP-605)
- **Customer:** PMA263
- **Vehicle Tail Number:** 572
- **Plan:** None
- **Issue Status:** Closed
- **Incident Type:** Mission Failure/Abort
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

This issue is from the larger group of issues that were reported recently from Operator at 29 Palms training event. 

Operator reported multiple uncommanded aborted launches.  

AAR files attached

## Root Cause

Operator Error: Firmware was not up to date or consistent across XCOMM, VTOL AP and FW AP. Errors that resulted in launch aborts would not have caused an abort in the latest software.

## Comments (16)

### David Grosher, 2024-09-05

@Pat Wells 
There is a mismatch of versions on v572.  This will likely lead to interface differences between the different components leading to unintended behaviors. The Launch abort itself was reported as LRF and Mag faults. There have been multiple updates to the drivers handling these sensors in more recent updates. The team clearly does not understand the released documentation and updates on the maintenance of their vehicles.  
GCS: v6.1.2
VTOL: 1.44  (From GCS - v5.0.6.4)
XCOMM: 4.60 (From GCS - v5.0.6.4)
FW AP: 6.05m (From GCS - v6.0.1.2)
[08:51:41.716 1126.716] vtol fault during climb, RTL
[08:51:41.717 1126.717] DebugMsg RTL
[08:51:41.718 1126.718] aux servo cycle start
[08:51:41.719 1126.720] trillium park cmd sent
[08:51:41.818 1126.818] vtol fault during climb, RTL
[08:51:41.822 1126.822] DebugMsg RTL
[08:51:41.923 1126.923] vtol fault during climb, RTL
[08:51:41.926 1126.926] DebugMsg RTL
[08:51:42.029 1127.029] vtol fault during climb, RTL
[08:51:42.030 1127.030] DebugMsg RTL
[08:51:42.131 1127.131] vtol fault during climb, RTL
[08:51:42.132 1127.132] DebugMsg Climb abort, VTOL controller fault
[08:51:42.133 1127.134] DebugMsg   Sensor: magnetometer fault
[08:51:42.135 1127.135] DebugMsg   Sensor: laser range finder fault

### David Grosher, 2024-09-06

@Pat Wells Same result as v688. The VTOL aborts triggered in this code (v144 of VTOL) would have passed in the newer releases. One thing to note is that this CW is also numbered 1, which is strange because that would indicate that it is the same as that flown on v688. 

[embedded: image-20240906-154852.png]

[embedded: image-20240906-154859.png]

### David Grosher, 2024-09-18

@Pat Wells I suggest we cancel this ticket, there really isn’t a workflow here where we know what happened but are taking no action.

### Pat Wells, 2024-09-18

@David Grosher I concur. 
Would it be possible to produce a very basic report to cover this.  I think the PM will want this to provide to the customer since this was such a significant emotional event when it was first reported.

### David Grosher, 2024-09-18

@Pat Wells Yes, we can create a report.

### David Grosher, 2024-09-18

@Scott Hunter We will want to pull together a report for the customer outlining that it was operator error and that the new SW would have resulted in successful launches based on the reported Mag data.  There were also a few LRF issues and I know that a lot of work went in to making it more reliable in 1.52, so if we can find some history there to support that as well that would be good.

### Sean Odell, 2024-10-22

@Scott Hunter   @Greg Fryer@David Grosher @Pat Wells Aircraft evaluated (Paperwork in case) and delivered to Engineering for your investigation efforts.

### Cody Smisek, 2024-11-07

@David Grosher @Scott Hunter @Greg Fryer should aircraft be returned to RMA or held in engineering?

### Scott Hunter, 2024-11-07

I don’t see any reason to hold the aircraft.

### Greg Fryer, 2024-11-07

@Cody Smisek @Scott Hunter We need to disposition the hardware, not just get the root cause. That goes to @Sean Odell via the linked ticket https://jenaero.atlassian.net/browse/RMA-365 
Is that done? I do not see anything in either spot - unless Sean already knows based on the evaluation?

### David Grosher, 2024-12-05

@Pat Wells Closing due to mismatched SW.

### David Grosher, 2024-12-05

Mismatched Software

### Cody Smisek, 2024-12-18

returning hardware to RMA

### Jason Scherer, 2025-02-11

Moving ticket from cancelled to In Process. An investigation has been requested to support the miss-match firmware report. The investigation was previously not completed due to outdated firmware.

### David Grosher, 2025-02-14

@Jason Scherer Closing this as the Land Aborts have been explained.

### David Grosher, 2025-02-14

The land aborts would have been fixed in previous releases.

## Attachments (16)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V572_240820_015906_pack.zip | archive | 1281 | 2024-09-05 | listed only |
| T95_V572_240820_020827_pack.zip | archive | 1731 | 2024-09-05 | listed only |
| T95_V572_240820_022013_pack.zip | archive | 2582 | 2024-09-05 | listed only |
| T95_V572_240820_055508_pack.zip | archive | 1318 | 2024-09-05 | listed only |
| T95_V572_240820_061043_pack.zip | archive | 1858 | 2024-09-05 | listed only |
| T95_V572_240820_203903_pack.zip | archive | 1105 | 2024-09-05 | listed only |
| T95_V572_240820_204708_pack.zip | archive | 1544 | 2024-09-05 | listed only |
| T95_V572_240820_210026_pack.zip | archive | 926 | 2024-09-05 | listed only |
| T95_V572_240820_210827_pack.zip | archive | 1298 | 2024-09-05 | listed only |
| T95_V572_240820_212000_pack.zip | archive | 1400 | 2024-09-05 | listed only |
| T95_V572_240821_005013_pack.zip | archive | 2831 | 2024-09-05 | listed only |
| T95_V572_240821_010404_pack.zip | archive | 1434 | 2024-09-05 | listed only |
| T95_V572_240821_015639_pack.zip | archive | 3227 | 2024-09-05 | listed only |
| T95_V572_240821_042204_pack.zip | archive | 2032 | 2024-09-05 | listed only |
| image-20240906-154852.png | image | 1289 | 2024-09-06 | listed only |
| image-20240906-154859.png | image | 1203 | 2024-09-06 | listed only |
