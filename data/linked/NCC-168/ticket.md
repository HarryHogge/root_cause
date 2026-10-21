# NCC-168: FLOPS - MCM Hard Drive Resizing

- **Issue type:** Bug
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-08-01
- **Updated:** 2025-08-04
- **Resolved:** 2025-08-04
- **Reporter:** Alan Burnsworth
- **Assignee:** Alan Burnsworth
- **Creator:** Alan Burnsworth
- **Labels:** DriveByTasking
- **Links:** clones NCC-161 (JAM - MCM Hard Drive Resizing)
- **Sprint:** NCC Sprint 3
- **Current Behavior:** MCM “/” partition too small/not correct size.
- **Expected Behavior:** MCM “/” partition should be expanded to utilize the remaining unused space on the hard drive.

## Description

Found issue on HIL Sim 4062 where MCM hard drive was not fully expanded for the “/” (root) partition. Ran connect to expand the partition to utilize the remaining unused space. 
Because of this issue, DTED was not fully loaded. Correcting that as well.

## Comments (5)

### Alan Burnsworth, 2025-08-01

Corrected MCM hard drive sizes on HIL Sim 4062.

### Alan Burnsworth, 2025-08-01

Still need to push DTED.

### Alan Burnsworth, 2025-08-01

@Jo Brown FYI, had another MCM drive sizing issue. Starting to accumulate. How many have we not found yet? Thoughts?

### Alan Burnsworth, 2025-08-04

DTED updated.

### Alan Burnsworth, 2025-08-04

HIL Sim 4062 MCM
- Resized partition
- Uploaded DTED
- Uploaded Maps: World and Courtland, AL

## Attachments (0)
