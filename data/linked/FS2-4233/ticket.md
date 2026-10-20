# FS2-4233: Stress testing of UDP, FTP, CAN and UART interfaces

- **Issue type:** Story
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2026-02-02
- **Updated:** 2026-04-08
- **Resolved:** 2026-04-08
- **Reporter:** Scott Whitney
- **Assignee:** Logan Wright
- **Creator:** Scott Whitney
- **Parent:** FS2-3875 B40 Investigations 
- **Epic Link:** FS2-3875
- **Sprint:** FS2 Sprint 37, FS2 Sprint 36

## Description

Config
- Build:Git Hash: commit 834225 fd396b2d7f97bf6cda1b7516455015c951 (HEAD -> FS2-4207-xcomm-4.75_rc3-reset-investigat, tag: DoubleStacks4Network
- Vehicle: Blk40
- Power Source: Power Supply
- Script
- Based on Stress Test below
- Power cycle?: NO


Stress Tests
- Ethernet Network
- UDP & FTP
- UDP (only)
- FTP (only)
- CAN
- UART


| Stress Test | 882 | 913 | HIL 882 | AV 882 Fuse: 913 | AV 913 Fuse: 882 |
| FTP |  |  |  |  |  |
| UDP |  |  |  |  |  |
| FTP & UDP (.5 delay) | Run 1 Complete: v882_FTP&UDP-Stress Test | Run 1 Complete: v913_FTP&UDP-Stress Test |  |  |  |
| CAN |  |  |  |  |  |
| FTP & UDP & CAN |  |  |  |  |  |

Data Folder: WD Investigation

## Comments (4)

### Scott Whitney, 2026-02-03

FYSA: @Brandon Slater

### Brandon Slater, 2026-02-03

Cartman HIL Host configuration as of 2026-02-03@Logan Wright @Scott Whitney @David Grosher 
Devices:
- Switch
- TP-Link Model: TL-SG1024S 24 port gigabit switch
- Vehicle 
- currently fuse 913 with avionics 882
- Scott Hunter’s test build 2026-02-02
- HIL Host
- Webpower
- LinuxLaptop

Switch Connections:
- Vehicle
- HIL Host
- Webpower
- LinuxLaptop

HIL Host info:
[embedded: Screenshot 2026-02-03 122601.png]
[embedded: Screenshot 2026-02-03 122628.png]

### Logan Wright, 2026-02-03

Kyle (HIL Host connected to v882 fuselage hood connector) as of 2026-02-03 @David Grosher @Scott Whitney  @Brandon Slater  @Scott Hunter 
Devices:
- Switch
- LinkSys Model by Cisco: EZXS88W ver. 3.4 8 port gigabit switch
- Vehicle
- currently fuse 882 with avionics 913
- Scott Hunter’s test build 2026-02-02
- HIL Host
- Webpower
- LinuxLaptop
- KVaser Leaf v2 (not currently running anything, but powered on and connected to avionics via Linux Laptop 2)

Switch Connections (8 port LinkSys network switch):
- Vehicle
- HIL Host
- Webpower
- LinuxLaptop

[embedded: image-20260203-202934.png]
[embedded: image-20260203-203903.png]

### Scott Whitney, 2026-04-08

Closing task and marking as complete

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Screenshot 2026-02-03 122601.png | image | 58 | 2026-02-03 | listed only |
| Screenshot 2026-02-03 122628.png | image | 71 | 2026-02-03 | listed only |
| image-20260203-202934.png | image | 68 | 2026-02-03 | listed only |
| image-20260203-203903.png | image | 19 | 2026-02-03 | listed only |
