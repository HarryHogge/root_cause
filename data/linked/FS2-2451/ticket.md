# FS2-2451: Investigate VXEP-732 - Crash on VTOL Descent

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-10-21
- **Updated:** 2025-02-11
- **Resolved:** 2025-02-11
- **Reporter:** Scott Whitney
- **Assignee:** Jason Scherer
- **Creator:** Scott Whitney
- **Components:** Vehicle Incident Support 
- **Links:** relates to VXEP-732 (VXE 628 Crash on VTOL descent); relates to FS2-2321 (Create a consolidated report on mismatched SW/FW versions for VXE-572/573/574/628/688/594)
- **Sprint:** FS2 Sprint 26, FS2 Sprint 29

## Description

SharePoint Folder: VXEP-732 - Crash on VTOL Descent

Investigation Report: Vehicle Investigation VXEP-732.pptx

## Comments (10)

### Scott Whitney, 2024-10-23

@Jason Scherer  - 501 is downstairs (it is under other vehicles)

### Scott Whitney, 2024-10-23

@Ryan Smith - will pull the AAR and attach it to this task

### Ryan Smith, 2024-10-23

Would love to see what to look for in this if you have time for me to shadow but no problem if not.

### Ryan Smith, 2024-10-23

Working on getting more info for FDR rn

### Ryan Smith, 2024-10-23

[embedded: T95_V501_241023_090348_01_pack.zip]
This is the correct AAR with the FDR data.

### Jason Scherer, 2024-10-24

@Scott Whitney 
Vehicle was running old firmware. I checked with John and the VTOL/XComm versions were released before Edge Autonomy. Best guess is ~2022. The Fixed Wing is the same version that we were using when I started around September last year.
Based on initial analysis the fixed wing ap issued a land abort due to exceeding attitude limits during transition to VTOL for landing. VTOL data stops updating on XComm logs about the same time as CAN timeouts are recorded for both VTOL and Air data. This is about the impact time. Prior to the stale VTOL data and CAN timeouts an airspeed fault is logged. The Airspeed and Ground speed data in the FDR differ a decent amount.  I did see IAS data dropouts in the FDR during the fixed wing flight phase. Could be a bad ADP. Overall battery and current levels look ok. 
Bottom line. Something bad happened during transition from fixed wing to VTOL which caused the vehicle to fall quickly. VTOL throttles looked ok, until they stopped.
Based on the old firmware it sounds like we might not need to look any further. Standing by for further direction on this ticket.
Firmware Versions
- AP 6.05m
- XComm: 4.60
- VTOL: 1.44

### David Grosher, 2024-10-28

@Scott Whitney @Jason Scherer The data above is for vehicle 501, why is this being linked to the investigation for v628?

### Jason Scherer, 2024-10-28

@David Grosher The fuse with tail number 628 and the CW with tail 501 is what produced the AAR. So, the 628 fuse was re-configured at some point to assume the 501 tail.

### Jason Scherer, 2025-02-11

Moving ticket from Done to In Process. An investigation has been requested to support the miss-match firmware report. The investigation was previously not completed due to outdated firmware.

### Jason Scherer, 2025-02-11

Investigation updated. CW stopped functioning during VTOL transition resulting in a failed land abort. Hardware team needs to investigate further to determine cause of CW failure.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V501_241023_090348_01_pack.zip | archive | 1760 | 2024-10-23 | listed only |
