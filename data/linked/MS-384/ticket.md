# MS-384: VXE 691 Failed take off - 2 attempts during During PreMAGNSS Verification Test Flight

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2024-08-15
- **Updated:** 2026-08-21
- **Resolved:** 2026-03-30
- **Reporter:** Scott Whitney
- **Assignee:** Wesley Reynolds
- **Creator:** Scott Whitney
- **Labels:** Pre-MAGNSS
- **Parent:** MS-419 Mission Systems: Incident Investigation
- **Links:** relates to MS-383 (MCM Operation Manual); relates to VXEP-1982 (VXE 897Failure to launch same error each time)
- **Epic Link:** MS-419
- **Sprint:** MS Sprint 21, MS Sprint 22

## Description

NCR: AC697-SCO-No power to Right Wing Tip
cc @Ted Trowbridge @Craig Burton  
Files: VXE 691 Failed take off - 2 attempts during During PreMAGNSS Verification Test Flight
On the 4th flight, the autopilot self-aborted the launch.  It landed gently/nominally and Ruysser is pulling the AAR.  The VSM collected some faults:
 
19:35:57.723775:  vtol_status     Takeoff
19:36:02.667334:  oper            Vehicle reporting reference altitude of 746 ft MSL.
19:36:08.607497:  vtol_status     Altitude request too high, launch aborted
19:36:08.611403:  vtol_status     Altitude request too high, launch aborted
19:36:08.615452:  vtol_status     Altitude request too high, launch aborted
19:36:08.765189:  vtol_status     Entering RTL mode
19:36:08.883215:  vtol_status     Start of climb
19:36:16.909253:  vtol_status     Climb abort, low climb rate
19:36:27.466187:  vtol_status     Launch abort, VTOL controller failure
19:36:27.888462:  vtol_status     Starting descent
19:36:32.443064:  vtol_status     Landing complete

4th flight 2nd attempt ditto:
19:52:59.005662:  oper            Vehicle reference altitude has been set to 745 ft MSL.
19:53:02.015998:  vtol_status     Launch Prep
19:53:02.482985:  vtol_status     Takeoff
19:53:08.581779:  oper            Vehicle reporting reference altitude of 745 ft MSL.
19:53:13.431456:  vtol_status     Altitude request too high, launch aborted
19:53:13.435448:  vtol_status     Altitude request too high, launch aborted
19:53:13.439408:  vtol_status     Altitude request too high, launch aborted
19:53:13.806272:  vtol_status     Start of climb
19:53:13.980797:  vtol_status     Entering RTL mode
19:53:20.791639:  vtol_status     Climb abort, low climb rate
19:53:42.567432:  vtol_status     Launch abort, VTOL controller failure
19:53:42.910942:  vtol_status     Starting descent
19:53:46.444825:  vtol_status     Landing complete
Files saved here (not accessible below): VXE 691 Failed take off - 2 attempts during During PreMAGNSS Verification Test Flight
Launch abort failure data: T95_V691_240814_144004_pack.zip 
Flight logs from earlier in the day:
T95_V691_240814_144004_01_pack.zip
T95_V691_240814_144004_02_pack.zip
T95_V691_240814_144004_03_pack.zip

## Comments (8)

### Cameron Chapman, 2024-08-15

@Matt Philley to link NCR

### Matt Philley, 2024-08-15

NCR linked in description

### Scott Whitney, 2024-08-15

Plan to move forward:
- investigate flight logs@Craig Burton @Ted Trowbridge
- Propose change for MCM software (if applicable)
- Implement change
- SW HIL Regression testing  - @Wesley Reynolds
- PreMAGNSS MCM Verification Testing
- If fix is Missions Critical,the  then continue the test from last flight
- If the fix is Flight Critical, then restart Verification test

### Scott Whitney, 2024-08-15

Update:
- Investigation shows there is a 20-25ft delta in prelaunch altitude between the aircraft sensors and software (DTED + aircraft calibration).
- Plan
- Lower the launch altitude to 200ft
- Continue Verification testing
- Update Operations Manual https://jenaero.atlassian.net/browse/MS-383
- After release, continue investigating the discrepancy in altitudes.

### Scott Whitney, 2024-09-09

Can we answer questions like:
- How is the altitude calculated?
- Is there a difference in how the edge gcs is handling altitude compared to VSM/OGCS
-

### Wesley Reynolds, 2024-11-04

This investigation was concluded through the https://jenaero.atlassian.net/browse/MS-447 ticket. I am not working on this ticket anymore, so I will move it back to To-Do. I don’t want to close this ticket until we have made a change that resolves the issue that this ticket outlines.

### Wesley Reynolds, 2025-01-06

After a brief chat with Ted today:
- We know what the root cause is.
- See: https://jenaero.atlassian.net/browse/MS-447
- A “Band-Aid solution” has been implemented.
- The tolerance for the difference between reference and takeoff altitude was increased by 50 ft.
- This issue was not observed during the Flight Testing phase of the MCM v1.1.0 testing (which was done at approximately the same location as the MCM 1.0.0 testing), so it seems to not necessarily be an issue right now.
- There is no immediate plan to implement a “proper solution” in the immediate future.
- With the “Band-Aid solution” in place, this is not a high-priority issue right now.

Because of this, I will move this ticket to the Backlog. I don’t want to mark it as DONE and there is no immediate plan to further resolve this issue.

### Christa Meck, 2026-03-30

No work in over 1 year.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V691_240814_144004_01_pack.zip | archive | 2203 | 2024-08-15 | listed only |
| T95_V691_240814_144004_02_pack.zip | archive | 2393 | 2024-08-15 | listed only |
| T95_V691_240814_144004_03_pack.zip | archive | 1554 | 2024-08-15 | listed only |
| T95_V691_240814_144004_04_pack.zip | archive | 1424 | 2024-08-15 | listed only |
| T95_V691_240814_144004_pack.zip | archive | 3218 | 2024-08-15 | listed only |
