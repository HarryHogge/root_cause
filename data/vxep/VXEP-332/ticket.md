# VXEP-332: VXE-522 / VXE-529 / VXE-508 Follow up testing: Investigate BT1 storage life and use cases on XCOMM. Investigate charge and discharge rate.

- **Issue type:** Sub-task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-04-08
- **Updated:** 2025-02-28
- **Resolved:** 2025-02-05
- **Reporter:** Connor Peebles
- **Assignee:** Connor Peebles
- **Creator:** Connor Peebles
- **Parent:** VXEP-236 Systemic SD card Investigation VXE-522 XCOM board failures at LM Source inspection
- **Links:** relates to RMA-230 (VXE 508 240325-2)
- **Job Number:** J100084 - VXE Incident Investigation

## Description

BT1 on both VTOL and XCOMM, MFG PN: MS621FE-FL11E
https://www.sii.co.jp/en/me/files/2024/01/MicroBattery_E_20230330_rev05-security.pdf

[embedded: image-20241028-221941.png]

## Comments (4)

### Connor Peebles, 2024-09-16

probably not related to SD Card problems, investigate and close as you see fit

### Connor Peebles, 2024-10-28

Power from coincell batt only keeps RTC chip up. When coincell batt dies, RTC chip can report erroneous dates until GPS UTC signal is acquired.
Note that this Coincell batt can fall below minumum voltage after sitting in storage for more than 2 months.

### Connor Peebles, 2024-11-01

@Adrian Garcia I would like you to measure the current on all the data lines going to the SD card, when the XCOMM is powered and un-powered. We are looking for leakage currents from BT1 to the SD card datalines

[embedded: image-20241101-173435.png]

### Connor Peebles, 2025-02-05

leakage currents not seen on SPI bus

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20241028-221941.png | image | 152 | 2024-10-28 | listed only |
| image-20241101-173435.png | image | 243 | 2024-11-01 | listed only |
