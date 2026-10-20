# FS2-2390: VXEP-292 Crash on take off

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-10-04
- **Updated:** 2025-09-24
- **Resolved:** 2025-09-23
- **Reporter:** Scott Whitney
- **Creator:** Scott Whitney
- **Components:** Vehicle Incident Support 
- **Links:** relates to VXEP-292 (VXE-477 Crash on take off ); relates to VXEP-368 (VXE 523 multiple faults with HLB discharging while in fuel cell configuration)

## Description

Requirements:
- Investigate VXEP-292
- Determine Cause and Corrective Actions
- Implement Corrective Actions (if needed)
- Test implementation
- Add test steps to Regression test matrix

## Comments (3)

### Eric Brewer, 2024-10-07

@Scott Whitney , The investigation on this incident is complete with root cause identified, and Ted is working GCS updates to make the launch wizard protect against a bad airspeed cal.  Let me know if I’m missing something but I’m not tracking any immediate actions for me.

### Scott Whitney, 2024-10-07

@Eric Brewer - I created an epic to capture all the tasks that were involved in this incident. I took you off the assignee, since your work seems to be complete

### Scott Whitney, 2025-02-02

Moving out to 6.6 release. This work was not completed in 6.4

## Attachments (0)
