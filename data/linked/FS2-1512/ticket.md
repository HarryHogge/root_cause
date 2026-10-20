# FS2-1512: VTOL Abort logic fix

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-02-21
- **Updated:** 2024-08-14
- **Resolved:** 2024-08-14
- **Reporter:** David Grosher
- **Assignee:** Jason Scherer
- **Creator:** David Grosher
- **Components:** Vehicle Incident Support 
- **Fix versions:** Release 6.3.4
- **Links:** relates to VXEP-282 (VXE 533 VTOL power issue on transition led to Uncontrolled drift and crash on landing); relates to VXEP-233 (VXE-496 with 550 wing- abnormal behavior after transition to VTOL led to crash); relates to VXEP-283 (VXE-533 Uncontrolled drift and crash after failed VTOL abort); relates to FS2-1446 (FW AP Landing Abort Bug Fix)

## Description

Potential RACE conditions in VTOL abort that lead to FW and VTOL APs trying to fly the aircraft at the same time. This appears to be related to the bug that @Jason Scherer found while running HIL tests on Xkit. 
v533 appeared to show the VTOL AP having successfully aborted and then it spooled up the motors.  HostState returns to FWFlight and then motors spool up, indicating a RACE condition within the VTOL AP. 
We need to analyze all potential abort code paths and test them in the HIL to ensure they work correctly. Any fix needs to address them all. The initial fix did not address all failures and resulted in continued aborts being issued.

## Comments (2)

### David Grosher, 2024-02-21

@Scott Whitney FYSA, this will be a high priority fix

### Scott Whitney, 2024-03-29

Plan
- address the main bug end of today - then need code review
- address a majority of the cases
- test team can start next week - set up brief with test team
- 13 land abort scenarios to test
- other things to address - conflicting states, infinite retry, land now, and other - these need to be address
- 21 additional findings can be address in separate testing

## Attachments (0)
