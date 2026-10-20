# FS2-2196: VXEP-529 - Investigate inability to send operator commands

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-08-23
- **Updated:** 2024-09-25
- **Resolved:** 2024-09-25
- **Reporter:** Jason Scherer
- **Assignee:** Jason Scherer
- **Creator:** Jason Scherer
- **Links:** relates to VXEP-529 (VXE 674 Erractic landing behavior, not accepting operator commands)
- **Sprint:** FS2 Sprint 24

## Description

The operator reported two types of abort input
- Commanded landing abort using “hand controller” which I am guessing is the xbox controller.
- I don’t see any evidence in any of the logs (GCS Debug/GCS Event/XComm Event) of this abort.
- Commanded Go To with a primary mission waypoint.
- This command was logged, but the landing state machine on the fixed wing autopilot had already passed the state that allows aborts. Since the abort was not valid for the state of the fixed wing when the message was received the landing abort command was ignored. This is the expected behavior.

## Comments (0)

## Attachments (0)
