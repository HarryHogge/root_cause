# FS2-1983: v533 NCR Aborted TO after start of transition

- **Issue type:** Story
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-06-17
- **Updated:** 2024-06-17
- **Resolved:** 2024-06-17
- **Reporter:** Jason Scherer
- **Assignee:** Jason Scherer
- **Creator:** Jason Scherer
- **Links:** relates to VXEP-282 (VXE 533 VTOL power issue on transition led to Uncontrolled drift and crash on landing)
- **Sprint:** MS Sprint 16

## Description

•V533 successfully launched and climbed to the commanded altitude of ~310’ AGL before the fixed wing autopilot detected a loss of uplink and commanded a launch abort. The vehicle was in launch state 13 “wait for threshold airspeed, monitor timeout, health” prior to the abort.
•Launch abort resulted in a successful landing.
•GCS logs don’t really show indication of loss of datalink during time of abort. However, XComm logs do show indication of a drop in traffic on the network port connecting XComm to the datalink radio.
•Fixed Wing maintains uplink status by updating a timestamp variable when various GCS messages are received. If one of the monitored messages are not received with ~5 second window the uplink is considered lost.
Initial Analysis attached
[embedded: Initial-Analysis.pptx]

## Comments (0)

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Initial-Analysis.pptx](attachments/21006_Initial-Analysis.pptx.md) | pptx | 695 | 2024-06-17 | converted |
