# FS2-952: Do any of the flight logs list what equipment was connected? If not, could we add this feature?

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-09-08
- **Updated:** 2023-09-21
- **Resolved:** 2023-09-21
- **Reporter:** Cameron Chapman
- **Assignee:** John Clark
- **Creator:** Cameron Chapman
- **Labels:** 8-28-Sprint, TIQUILA, TIQUILA-Blocker
- **Links:** relates to ENG-2983 (511 LW motor test failed. 511 and 516 center wings damaged. ); relates to VA-31 (EA Internal: 516 center wing damaged. 511 fuselage+516CW LW motor test failed. ); relates to VXEP-12 (TPTR-87 VXE 511 VTOL Connector Issues 516 CW. Contains Main connector/contact C/CAs)
- **Sprint:** VXE-1 Cameron's Team 9-17, VXE-1 EE Team Sprint 8/28-9/17

## Description

Ex: Date, FWAP tail number, VTOL AP tail number, ADB SN, BMS SN, etc. 
Operators mix and match equipment a lot, so this would be very helpful. 
@Adrian Garcia@Connor Peebles

## Comments (1)

### John Clark, 2023-09-21

@Cameron Chapman , You may be aware already? The CW configuration is reflected in the file name of the VTOL logs in the AAR. The information is also available in the VTOL log itself here:
[08:39:44.879] AP SN: APB-1-1253
[08:39:44.879] Tail number: VC0499
This is at boot. 
Hybrid lift battery info is in the Flight Data Log (latest release)
ADP SN is currently only available through the web pages.

## Attachments (0)
