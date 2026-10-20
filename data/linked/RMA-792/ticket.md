# RMA-792: VXE-697 250820-1

- **Issue type:** Aircraft
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2025-08-20
- **Updated:** 2026-01-08
- **Resolved:** 2025-10-30
- **Due:** 2025-10-17
- **Reporter:** Lauren Velasquez
- **Assignee:** Samuel Lopez
- **Creator:** Lauren Velasquez
- **Labels:** Industrial_SD-Card_Installed
- **Environment:** “We need to RMA 697 for abnormal launch behaviors.  No physical damage other than scratches on wing tip, pads, and payload. “
- **Links:** relates to VXEP-1484 (VXE 697 - Incorrect Baro data leading to aborted launch)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 697
- **Corrective Action:** All teams must be informed that removed parts, particularly PCB boards, cannot be scrapped until RMAs have been closed.
- **Received Date:** 2025-09-03
- **Warranty Status:** In Warranty

## Description

Aircraft requested by Doug Baker for evaluation due to failed launch on 8/19/2025. Launch data files provided to Dave Grosher.

## Root Cause

Microcontroller pulled zero values for barometer readings.  Inconclusive as to whether this was component failure or quality issue original board was removed from the AC and scrapped before investigation could be completed.

## Comments (7)

### Lauren Velasquez, 2025-09-04

Per Dave G- I will be requesting Electrical assistance to see it the Baro sensor can be repaired on the VTOL board.

### Lauren Velasquez, 2025-09-09

Per EShop- Replace VTOL board
@Drew Hildreth has a warranty determination been made?

### Drew Hildreth, 2025-09-09

@Lauren Velasquez Updated

### Lauren Velasquez, 2025-10-23

Being Sealed

### Lauren Velasquez, 2025-10-28

CofC Requested

### Lauren Velasquez, 2025-10-30

Packing Slip obtained

### Samuel Lopez, 2026-01-07

Aircraft has been shipped back to customer.  VTOL board that was removed has been scrapped and is not available for investigation.  Root cause can be speculated to be
- Component failure.  Either U11, the supply voltage through the resistor R97, or SCLK and SDI resistors R98 and R99.
- Firmware corruption.  Could be tested by re-flashing board.

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [697 RMA FORM.pdf](attachments/31627_697%20RMA%20FORM.pdf.md) | pdf | 177 | 2025-08-20 | converted |
| 697 CW ..jpg | image | 556 | 2025-09-23 | listed only |
| 697 CW.jpg | image | 555 | 2025-09-23 | listed only |
| 697 L wing tip delam..jpg | image | 387 | 2025-09-23 | listed only |
| 697 L wing tip delam.jpg | image | 344 | 2025-09-23 | listed only |
| 697 lift booms.jpg | image | 681 | 2025-09-23 | listed only |
| [RMA WARRANTY QUOTE 250820-1 TIQ VXE-697 AMENDED.pdf](attachments/32609_RMA%20WARRANTY%20QUOTE%20250820-1%20TIQ%20VXE-697%20AMENDED.pdf.md) | pdf | 176 | 2025-09-26 | converted |
