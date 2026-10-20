# VXEP-468: 1809P01A-AP Adapter Board improvement ideas

- **Issue type:** Sub-task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2023-04-21
- **Updated:** 2025-11-04
- **Resolved:** 2025-05-05
- **Reporter:** Cameron Chapman
- **Assignee:** Cameron Chapman
- **Creator:** Cameron Chapman
- **Parent:** VXEP-466 IRAD: Unified Autopilot
- **Links:** relates to ENG-1752 (1409P01D VTOL AP improvements); is blocked by ENG-1662 (Next generation aircraft idea collector (not already included in threshold requirements)); relates to XKIT-2150 (Hardware & PCB Improvement Collector)

## Description

Ideas to help with unified AP:
- CAN connectors.
- Connect transponder cable to give Red AP access to CAN.
- Ethernet switch and connectors.  
- Connect transponder cable to give Red AP access to ethernet.

## Comments (2)

### Ryan Ferguson, 2023-05-18

If this board gets rev’d, we should look at using the onboard ground iso circuit rather than needing an external ground iso board.  If this circuit is not to be trusted, we should move the current design of the ground iso board onto the adapter board.  This will save weight and simplify wiring.

### Cameron Chapman, 2023-05-18

Wrong AP int board. This one may go in the avionics box. I added the idea here. https://jenaero.atlassian.net/browse/ENG-1662 you are welcome to add more.

## Attachments (0)
