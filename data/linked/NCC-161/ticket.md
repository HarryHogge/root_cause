# NCC-161: JAM - MCM Hard Drive Resizing

- **Issue type:** Bug
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-07-21
- **Updated:** 2025-09-03
- **Resolved:** 2025-07-22
- **Reporter:** Alan Burnsworth
- **Assignee:** Alan Burnsworth
- **Creator:** Alan Burnsworth
- **Labels:** DriveByTasking
- **Parent:** CYBER-1 Project JAM: Initial Artifacts Delivery
- **Links:** is cloned by NCC-168 (FLOPS - MCM Hard Drive Resizing)
- **Epic Link:** CYBER-1
- **Sprint:** NCC Sprint 3
- **Current Behavior:** MCM “/” partition too small/not correct size.
- **Expected Behavior:** MCM “/” partition should be expanded to utilize the remaining unused space on the hard drive.

## Description

Found issue on Tail Number 828, 881, and on HIL Sim 4060 where MCM hard drive was not fully expanded for the “/” (root) partition. Ran connect to expand the partition to utilize the remaining unused space. 
Because of this issue, DTED was not fully loaded. Correcting that as well.

## Comments (4)

### Alan Burnsworth, 2025-07-21

Corrected MCM hard drive sizes on Tail Number 828, 881, and HIL Sim 4060.

### Alan Burnsworth, 2025-07-21

Redeployed DTED on HIL Sim 4060. Still deploying on Tail Numbers 828 & 881.

### Alan Burnsworth, 2025-07-22

Tail Numbers 828, 881, and HIL SIM 4060
- MCM hard drive “/” partition resized
- DTED reloaded

### Jo Brown, 2025-09-03

@Addison Osborn new MCM’s should not have this issue. We are updating the MCM image to a new Jetpack version shortly. See https://jenaero.atlassian.net/browse/NCC-177. With this update, we will be implementing a check in Electronics to ensure the drives are formatted correctly, implementing cyber hardening, and implementing DTED updates at the image level.

## Attachments (0)
