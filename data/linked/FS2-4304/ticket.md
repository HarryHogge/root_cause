# FS2-4304: VXEP-864 : CBP v864 Investigation

- **Issue type:** Epic
- **Status:** In Review
- **Priority:** Highest
- **Created:** 2026-02-24
- **Updated:** 2026-04-30
- **Reporter:** Scott Whitney
- **Assignee:** Scott Whitney
- **Creator:** Scott Whitney
- **Links:** relates to RMA-929 (VXE-864 RMA 260226-2); relates to FS2-4388 (XCOMM Encryption Key Capture); covers VXEP-1780 (VXE 864 Crash)

## Description

Sharepoint: VXEP-## CBP VXE30 Standard Incident
Investigation Sheet: VXEP-### CBP VXE30 Incident
Additional Reference Data: Investigation of production eShop Escape.xlsx
XCOMM SD Encryption Key:
[21:44:02.110 2.110] 0 0x26c6d574
[21:44:02.111 2.111] 1 0x2a8b157e
[21:44:02.112 2.112] 2 0xea81d939
[21:44:02.113 2.113] 3 0xaa55aa55
[21:44:02.114 2.114] 4 0xaa55aa55
[21:44:02.115 2.115] 5 0xaa55aa55
[21:44:02.116 2.116] 6 0xc6267e15
[21:44:02.117 2.117] 7 0x7e7cafc2
[embedded: image-20260317-215112.png]

Configuration: BLK30 Standard
Firmware: 6.6.1
GCS: Jennings?
- Initial information Findings
- XCOMM reset and never recovered
- Battery connect could be issue
- Forward esc stopped spinning
- CBP has new drone safety team that is going to build out the procedures for their investigation process

## Plan

- Run endurance test of 6.6.1 on BLK30 Standard
- Grep all testing from 6.6.1 - flight test, safety of flight, etc
- Burn in 10 BLK30 Standard xcomm
- Vehicle_Type: 95
- Firmware: 6.6.1
- Test length: 48 hours

## Issue Status

@Scott Whitney  @Lauren Velasquez what is the status of this investigation? Are we waiting for this HW to replace the XCOM?
- @Cameron Chapman  - we are waiting on AARs and Hardware. While we were are waiting for additional information, Dave has requested we search across all SCO, Eng, and FLOPs data to see if we can determine if there are additional failing xcomms with WDs (current theory, while waiting to look at data)

2026-03-13 - v864 is in engineering. The Avionics is significantly damaged. SW team is working with Ben Norris to recover XCOMM data (-S. Whitney)
- XCOMM board needs to be repaired to recover encryption key
- XCOMM board has failed internal layers, powered 3.3V externally to enable pulling the keys - C.P.


CAs:
- Production Engineer to save the encryption key
- engineering to provide tool pull encryption key and allow for easy copy/paste into traveler
-

## Comments (3)

### Scott Whitney, 2026-03-12

XCOMM was significantly damage. To get data, we will need to 
- Find the key to un-encrypt the sd card
- repair the xcomm

[embedded: image-20260313-035512.png]

### Scott Whitney, 2026-03-19

XCOMM Data recovered. Link to data: v864 Flight Data

### Scott Whitney, 2026-03-19

WD BOOT grep results
[embedded: image-20260319-191614.png]

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20260313-035512.png | image | 3217 | 2026-03-12 | listed only |
| image-20260317-215112.png | image | 7 | 2026-03-17 | listed only |
| image-20260319-191614.png | image | 51 | 2026-03-19 | listed only |
