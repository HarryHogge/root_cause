# VXEP-478: Create HILs to support SW troubleshooting.

- **Issue type:** Major Project
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-08-17
- **Updated:** 2025-02-28
- **Resolved:** 2024-09-10
- **Reporter:** Cameron Chapman
- **Assignee:** John Clark
- **Creator:** Cameron Chapman
- **Labels:** 8-28-Sprint
- **Parent:** VXEP-573 Sustainment: VXE30 Incident Investigation
- **Links:** relates to ENG-1063 (107-111666 AUTOPILOT HILS Create stripped down version for SW testing. ); relates to ENG-2990 (VXE 407 Error during transition for landing); relates to VA-123 (Modify HIL set 105 to include 515's XCOM, add GPS, magnetometer, ADP, and current sense)
- **Start date:** 2023-08-17
- **Other Stakeholder (as required):** John Clark
- **Job Number:** J100084 - VXE Incident Investigation

## Description

Mark, Cameron, these are the mods we need to HIL 105 (Aircraft 515) and the new one I requested Mark build up from the VTOL AP from V407. 
Time estimate to complete 515 HIL modification: 6 hours
Mark, for HIL 407 we want it as original as possible. Any of the below parts that can be taken from the V407 aircraft itself, we should. Software Engineering will also attempt to keep configurations (tail #) and so on, unchanged as well. 
- 407 VTOL HIL build completed 8/22 (MS)
- Working on Fixed Wing HIL today (8/25)

Please, let me know and questions or anything we can do to help.
Turn HIL into Iron Bird config​
- Add air data board (includes LRF) (​I have a volunteer)
- Add Magnetometer​
- Add GPS ​
- Current Sensor​
- Turn off HIL flag​ (this is a software activity)

--jc
 
John Clark
Software Engineer
Edge Autonomy
P: +1-805-544-0932
Email: jclark@edgeautonomy.io

## Comments (8)

### Mark Squillante, 2023-08-21

ADP, magnetometer, GPS and current sense board have been removed from 407’s center wing.

### Mark Squillante, 2023-08-21

I pulled 407’s center wing harness out of the center wing. Now will work on building the HIL.

### Mark Squillante, 2023-08-22

407 VTOL HIL is complete. @John Clark let me know who to deliver it to.

### Mark Squillante, 2023-08-22

407 VTOL HIL delivered to @Brandon Slater

### Cameron Chapman, 2023-08-24

Linking subtasks to parent

### Mark Squillante, 2023-08-24

HIL 105 modification complete. Will deliver to either @John Clark or @Brandon Slater

### Mark Squillante, 2023-08-25

Completed build of 407 Fixed Wing HIL. Delivering to @Brandon Slater

### Mark Squillante, 2023-08-25

@Cameron Chapman this task is ready for review. Who should I assign it to?

## Attachments (0)
