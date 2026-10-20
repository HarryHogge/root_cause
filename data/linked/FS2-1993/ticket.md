# FS2-1993: VXEP-416 Failure to Launch - Vehicle Investigation

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-06-19
- **Updated:** 2026-10-12
- **Resolved:** 2026-10-12
- **Reporter:** Scott Whitney
- **Assignee:** Jason Scherer
- **Creator:** Scott Whitney
- **Components:** Vehicle Incident Support 
- **Links:** relates to VXEP-416 (VXE 539 Failure to launch)

## Description

Requirements:
- Investigate
- Identify C/CA
- Implement fixes (if applicable)
- Test Fixes
- Create Progression test procedures
- Add tests to Regression test matrix


CAs:
1.Update software to ensure delivery of SAFE ON/OFF commands between XComm and VTOL. 
- https://jenaero.atlassian.net/browse/FS2-2320

2.Fix logging software to positively confirm transmission of the SAFE OFF message. 
- https://jenaero.atlassian.net/browse/FS2-2205

3.Update software to reset VTOL autopilot during software resets. 
- The GCS now does this in the new release.

## Comments (0)

## Attachments (0)
