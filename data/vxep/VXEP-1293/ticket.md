# VXEP-1293: VXE 758 Aborted Launch at 30 feet AGL

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-06-05
- **Updated:** 2026-07-13
- **Resolved:** 2026-07-13
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Stephen Peters
- **Creator:** Alexander Alan Arnold
- **Labels:** GS_Closed, HLB_bad_cell, Weekly-incident-tracker
- **Links:** relates to RMA-708 (VXE-758 RMA # 250606-1); Linked issue cannot finish until this issue finishes. VXEP-1449 (Systemic Hybrid lift battery unexplained cell failures in flight)
- **Customer:** Redwire
- **Vehicle Tail Number:** VXE 758
- **Vehicle Configuration:** Standard VXE, Battery Config, 140G2Z Gimbal
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

Operator Statement
aircraft 758 mishap occurred at approximately 30ft during VTOL climb. Aircraft GCS displayed a cell imbalance of approximately 3 volts, and auto-aborted launch. VTOL motors fluctuated in rpm/ throttle as the AV descended at a moderate to high rate and landed about 3ft aft of the stand with damage to the payload, left VTOL boom, tail boom, Vertical stabilizer. 
This occurred during USBP initial training. This was the first flight of 758 for the day. Winds calm.
AV 758, Battery config
Gimbal 6219
main battery 3-2088
HLB 2-3490
Laptop/ GCS JAI-1
Silvus 10.127.1.1
Student: USBP
Instructor: Hadley
METAR K9A4 051855Z AUTO 00000KT 10SM BKN044 28/19 A3006 RMK AO2

## Plan

- Cam recommends starting a sharepoint folder, investigation ppt and placing some basic info in there. See https://jenaero.atlassian.net/wiki/spaces/EF/pages/23363854/Incident+Troubleshooting+and+Resolution+Tracking.
- Where is this HLB now? Agreed that seems to be a likely cause. AA could open and inspect it.
- Are you able to gather history of the battery from the operators, logs, etc? Does the bms have any history of how the battery was used and where?
- Sharepoint folder here:2025-06-05 VXE-758 VXEP-1293 Aborted Launch

[embedded file]

## Comments (16)

### Jackson Riley Curvin, 2025-06-05

[embedded image-20250605-203423.png]

### Jackson Riley Curvin, 2025-06-05

[embedded image-20250605-203707.png]

### Alexander Alan Arnold, 2025-06-05

[embedded image-20250605-203820.png]

### Jackson Riley Curvin, 2025-06-05

[embedded image-20250605-203845.png]

### Alexander Alan Arnold, 2025-06-05

[embedded image-20250605-204027.png]

### David Grosher, 2025-06-05

@Jackson Riley Curvin This is likely the issue here. FYSA @Cameron Chapman @Tom Westrich @Stephen Peters

### David Grosher, 2025-06-05

@Stephen Peters I assigned this to you because initial analysis is implicating one of the battery cells. Let me know if you need additional help.

### Matt Philley, 2025-06-06

Info on that HLB, SN 2-3490
Production Order List Entry: 114-106085
This was delivered by SLO to FLOPs as a spare HLB for an LRR Flyoff in July of 2024. 
No NCR history found in SLO.

### Alexander Alan Arnold, 2025-06-06

Added pictures of HLB to CW connection on Battery

### Cameron Chapman, 2025-06-06

Great work @Alexander Alan Arnold see my recommendations in the plan field.

### Pat Wells, 2025-06-06

@Jackson Riley Curvin or @Michael Mohr can one of you pick this up since Alex will be out on travel for the next two weeks.

### Michael Mohr, 2025-06-09

@Sean Wendling We have the HLB here in HSV. Do you want me to send it to you for testing?

### Sean Wendling, 2025-06-09

@Michael Mohr  (And All on this chain) Please do not ship this battery. I need to check with our Shipping Team, but in general we should not send malfunctioning batteries at least until I can confirm that it is safe to put onto a fedex truck.

### Sean Wendling, 2025-06-09

All, I discussed with the team here. This one should be safe to ship back, @Michael Mohr please ship via ground and make sure its packed according to lithium ion battery shipping requirements. Sorry for the alarm, just wanted to make sure we were in the clear based on the issue that it won’t get us in legal trouble to ship. Feel free to reach out any time youre unsure about shipping a malfunctioning / defective battery. Thanks!!

### Michael Mohr, 2025-06-10

HLB has been sent to Ann Arbor for evaluation.

### Jackson Riley Curvin, 2026-07-13

Closed, Tracked by Master Ticket.

## Attachments (20)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IMG_8898.jpg | image | 1923 | 2025-06-05 | listed only |
| IMG_8899.jpg | image | 1592 | 2025-06-05 | listed only |
| IMG_8900.jpg | image | 678 | 2025-06-05 | listed only |
| IMG_8901.jpg | image | 984 | 2025-06-05 | listed only |
| IMG_8902.jpg | image | 1027 | 2025-06-05 | listed only |
| IMG_8903.jpg | image | 921 | 2025-06-05 | listed only |
| IMG_8904.jpg | image | 872 | 2025-06-05 | listed only |
| IMG_8905.jpg | image | 880 | 2025-06-05 | listed only |
| IMG_8907.jpg | image | 801 | 2025-06-05 | listed only |
| IMG_8908.jpg | image | 728 | 2025-06-05 | listed only |
| [MishapReport_5JUN25_USBPCourtland.pdf](attachments/29646_MishapReport_5JUN25_USBPCourtland.pdf.md) | pdf | 462 | 2025-06-05 | converted |
| T95_V758_250605_134358_pack.zip | archive | 1781 | 2025-06-05 | listed only |
| image-20250605-203423.png | image | 31 | 2025-06-05 | listed only |
| image-20250605-203707.png | image | 62 | 2025-06-05 | listed only |
| image-20250605-203820.png | image | 51 | 2025-06-05 | listed only |
| image-20250605-203845.png | image | 110 | 2025-06-05 | listed only |
| image-20250605-204027.png | image | 70 | 2025-06-05 | listed only |
| HLB Connector 2-3490(1).jpg | image | 4557 | 2025-06-06 | listed only |
| HLB Connector 2-3490.jpg | image | 4578 | 2025-06-06 | listed only |
| [VXEP-1293.pptx](attachments/29930_VXEP-1293.pptx.md) | pptx | 4693 | 2025-06-16 | converted |
