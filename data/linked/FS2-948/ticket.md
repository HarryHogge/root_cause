# FS2-948: Investigate Debug Assertion that has been disabled to enable Debugging with ICE

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2023-09-15
- **Updated:** 2023-09-25
- **Resolved:** 2023-09-25
- **Reporter:** David Grosher
- **Assignee:** John Clark
- **Creator:** David Grosher
- **Parent:** FS2-806 Embedded SW Evaluation of VTOL AP
- **Links:** relates to VXEP-67 (Firmware release process is inadequate and results in improper testing of semaphore allocation. )
- **Epic Link:** FS2-806
- **Sprint:** FS2 Sprint 7

## Comments (2)

### John Clark, 2023-09-21

Change xSemaphoreTake/GiveSafe Macros so Take/Give of NULL Semaphores can be traced. Find and fix the occurrences of NULL Takes/Gives. To be done in a corrective branch off of main starting in autopilot_202

### John Clark, 2023-09-21

@David Grosher both XComm and VTOL AP built and tested with no NULL Semaphore protection. Let’s discuss what was done in the WD meeting, 9/22/2023

## Attachments (0)
