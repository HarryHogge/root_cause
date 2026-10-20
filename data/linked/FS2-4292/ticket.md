# FS2-4292: Corrupt SD Card data  (B40 WD Investigation)

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2026-02-18
- **Updated:** 2026-09-04
- **Resolved:** 2026-09-04
- **Reporter:** Scott Whitney
- **Assignee:** Brandon Slater
- **Creator:** Scott Whitney
- **Parent:** FS2-4309 B40 WD Investigation
- **Links:** relates to VXEP-1692 (B40/30 XCOM WDT resets )
- **Epic Link:** FS2-4309
- **Sprint:** FS2 Sprint 37, FS2 Sprint 39, FS2 Sprint 38

## Description

During the investigation of WD in BLK40, SD cards start to show signs of corruption. 
XCOMM SN: 5-6320: corrupted 3 SD Cards over 5 days. Seem to happen more frequently while EE probing SPI bus
XCOMM SN: 5-6321: Corrupted 1 SD card over the weekend (2/14-2/16). This SD was inside the avionics (not exposed) and was running endurance test of B40 incremental firmware. There were no extensive/stress test being run during curroption

Investigation Summary-B40 increased XCOM WDs.xlsx

## Comments (1)

### Brandon Slater, 2026-02-18

Write script to check for ROM mode in webpage

## Attachments (0)
