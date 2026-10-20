# VXEP-1526: Wing Utility Pylon Comms Modification

- **Issue type:** Epic
- **Status:** New
- **Priority:** Low
- **Created:** 2025-09-30
- **Updated:** 2025-09-30
- **Reporter:** Grant Goodman
- **Assignee:** Scott Whitney
- **Creator:** Grant Goodman
- **Links:** relates to FS2-3688 (Resolve issues found in Wing Utility Pylon Drop Test)

## Description

Wing Utility Pylon system was observed to have message loss during flight testing.
Modify existing software/firmware on associated systems to eliminate or reduce message loss to acceptable levels.
Modifications should take into account that there will be existing Wing Utility Pylon system out in the field and their PCB firmware will not be field upgradeable. The system modifications will need to be able to support legacy firmware, that will already be present in the field, and will not necessarily be replaced at the same time as software rollout.

Existing message path outlined below:
For Custom Payload Control data path is: GCS <=> XComm <=> Dropper. 
For Manual Payloads (in Mission) data path is: GCS <=> XComm <=> FW-AP <=> XComm <=> Dropper.

## Comments (0)

## Attachments (0)
