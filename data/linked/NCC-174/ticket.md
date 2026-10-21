# NCC-174: TN-880 MCM Resizing Issue

- **Issue type:** Bug
- **Status:** DONE
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2025-08-05
- **Updated:** 2025-09-04
- **Resolved:** 2025-09-04
- **Reporter:** Alan Burnsworth
- **Assignee:** Alan Burnsworth
- **Creator:** Alan Burnsworth
- **Labels:** DriveByTasking
- **Sprint:** NCC Sprint 4, NCC Sprint 5, NCC Sprint 6

## Description

Found issue on Tail Number 880 where MCM hard drive was not fully expanded for the “/” (root) partition. Ran connect to expand the partition to utilize the remaining unused space. 
Because of this issue, DTED was not fully loaded. Correcting that as well.

## Comments (5)

### Alan Burnsworth, 2025-08-05

Just FYI @Jo Brown

### Alan Burnsworth, 2025-08-05

MCM drive was resized. DTED and maps still need to be installed.

### Alan Burnsworth, 2025-08-09

TN-880 is being used to troubleshoot possible Gimbal/Power induced MCM reset.
Maps and DTED need a long period of uninterrupted power on time to upload.
Blocking task until I return from SLO, Aug-18.

### Alan Burnsworth, 2025-08-20

TN-880 is still being used for Gimbal/Power induced MCM reset troubleshooting.
Remaining blocked and to be carried over to next Sprint.

### Alan Burnsworth, 2025-09-04

OBE
I attempted to load DTED and Maps on the MCM of TN-880, however the connection kept dropping out before the transfers finished.
This task is no longer a priority due to the whole Avionics enclosure (containing the MCM) needing to be sent back to SLO for reassembly and inspection due to a parallel task having taken it apart.

## Attachments (0)
