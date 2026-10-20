# RMA-722: VXE-519 RMA 250701-1

- **Issue type:** Aircraft
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-07-01
- **Updated:** 2026-02-06
- **Resolved:** 2026-01-27
- **Due:** 2026-01-23
- **Reporter:** Rodney Linch
- **Assignee:** Lauren Velasquez
- **Creator:** Rodney Linch
- **Links:** relates to VXEP-1446 (VXE-519 Power Fluctuations)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 519
- **Corrective Action:** Scrapped parts should not be discarded until troubleshooting is complete
- **RMA Number:** 250701-1
- **Serial Number:** 519
- **Received Date:** 2025-07-21
- **Warranty Status:** In Warranty

## Description

Stalker 519 Power Reading Fluctuations. Incident report sent via email and is attached to this ticket.

## Root Cause

Fixed Wing AP failure likely due to microcontroller corruption.  Removed board was scrapped so troubleshooting was not completed.

## Comments (19)

### Pat Wells, 2025-07-16

@Rodney Linch @Lauren Velasquez have we received this?
@Alexander Alan Arnold @Jackson Riley Curvin is there a VXEP ticket on this?

### Rodney Linch, 2025-07-16

@Pat Wells - We have not received this aircraft.  Last correspondence referencing this AC was on 6/30, Kev Hinchley (delivery manager) stating: I will start the process for shipping the vehicle back with the customer and have raised an accompanying Work Order on our Help Desk System (ref WO0000000002606 Return EAGLE AV 519 due to power reading fluctuations). Will follow up.

### Rodney Linch, 2025-07-16

@Pat Wells - Kev Hinchley sent me a document (attached to ticket).  Looks like it was processed in Hethrow on July 14, 2025.  On the form, it lists Virgin Airlines VSO 23/17. I believe this means the intended flight for these cases is July 17th.  Not sure how long it’ll take to clear US customs, but I do know it’s en route.  
[embedded: image-20250716-143706.png]

### Lauren Velasquez, 2025-07-21

VXE-519 has arrived in SLO

### Lauren Velasquez, 2025-07-22

Power is fluctuating as stated by customer- Swapped nose cone to narrow down issue- issue persists- Requesting engineering oversight- seems to be similar issue as VXE-542. @Drew Hildreth FYSA

### Rodney Linch, 2025-07-22

@Jackson Riley Curvin - please open a VXEP ticket for RMA.  It came in due to ‘power fluctuations’ and confirmed Main Power Supply Voltage (within the Launch wizard) at 17 V and 0%. Carson B recommended I swap out the nose cone and check values. Same numbers: 17 V and 0%.  Maintenance logs are also attached to the ticket.

### Jackson Riley Curvin, 2025-07-23

@Rodney Linch Please pull The data off the aircraft by following the procedure i had you do before then up load it in the ticket please.https://jenaero.atlassian.net/browse/VXEP-1446

### Rodney Linch, 2025-07-23

@Jackson Riley Curvin Roger.  Will tag you once it’s uploaded.

### Lauren Velasquez, 2025-07-23

Quote sent to finance- Electronics working on replacing Green AP- SB updates needed, including RF Cables. Loose ODU being repaired by FAL with no material cost. 
@Drew Hildreth @Rodney Linch FYSA

### Lauren Velasquez, 2025-08-13

STILL PENDING POL SCHEDULE- WORK IN WIP

### Lauren Velasquez, 2025-09-19

Amended quote pricing pending after electronics evaluation from Eshop

### Lauren Velasquez, 2025-09-22

Work completed based off Amended Quote up to this point. 
Back in RMA area- Pending VXEP- resolution/ guidance.

### Lauren Velasquez, 2025-09-22

Items in RED have been completed, Pending CW WIP currently
[embedded: image-20250922-184730.png]

### Lauren Velasquez, 2025-09-26

Pending Engineering Disposition to continue with work.

### Samuel Lopez, 2025-12-09

2025-12-09
- Tote box containing travelers and replaced parts has not been located, despite an extensive search.
- Root cause was almost certainly the replacement of the FW AP.
- UPDATE:  SD Card on VTOL AP was also replaced, with industrial sd card 2120068-01.
- UPDATE: Fuse 100-105396 was replaced in nose cone.  This was done to observe whether there was any damage to the old fuse.  There was NO observable damage to the used fuse, eliminating possibility that fuse was root cause issue.
- After Material Disposition, this unit will go to Carson B for verification testing/flight testing.

### Samuel Lopez, 2025-12-09

Final Summary
VXE 519 arrive in SLO on July 21, 2025 due to ‘power fluctuations’ as described by customer – behavior which was promptly confirmed on the bench.  The Edge technician recognized the behavior from a previous aircraft and diagnosed the AP w/mag board as root cause issue.  The transponder port also failed to detect CAN in the XCOMM.
On September 22, the AP w/mag board was replaced along with a few other items.  The list is as follows.
- AP w/ Mag Board 965-1-01-2004

o   Root Cause Issue
- AP Mount 106-101310

o   Original mount broke during investigation
- Transponder cable 106-103720

o   Component Failure
- Fuselage New ‘Industrial’ SD-Card 2120068-01

o   Maintenance issue
- New Long Fuselage RF Cable 100-114534

o   Maintenance issue
- New Short Fuselage RF Cable 100-114532

o   Maintenance issue
On November 5, the investigation was continued by Sammy Lopez since the previous technician and engineer are no longer with the company.  Unfortunately, a tote box containing travelers and replaced parts has not been located, despite an extensive search. 
On the bench, aircraft was observed to no longer exhibit ‘power fluctuations – either with DC power supply, or with Main Battery and Hybrid Lift Battery.  Two additional components were replaced.
- VTOL AP ‘Industrial’ SD-Card 2120068-01

o   Maintenance
- Nose Cone Harness Assembly Fuse 100-105396

o   Testing
The fuse was replaced to observe whether there was any damage to the old fuse. There was NO observable damage to the used fuse, eliminating possibility that fuse was root cause issue.
On December 8, the unit was dispositioned to undergo SCO and flight checks.  Awaiting on this now.

### Lauren Velasquez, 2025-12-15

Revised quote sent to Finance and production teams. 
Ready for SCO.

### Samuel Lopez, 2025-12-29

Root cause highly suspected to be AP board, hence why functionality returned when AP board was replaced.  Customer has been given an explanation.  This aircraft is in the queue to be tested by Flight on 1/16/2025.

### Lauren Velasquez, 2026-01-27

Sourced

## Attachments (20)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [INC000000229849 Stalker 519 Pwoer Reading Fluctuations.pdf](attachments/30260_INC000000229849%20Stalker%20519%20Pwoer%20Reading%20Fluctuations.pdf.md) | pdf | 357 | 2025-07-01 | converted |
| [Return Merchandise Authorization (RMA) Request Form (TIQ VXE519).pdf](attachments/30261_Return%20Merchandise%20Authorization%20(RMA)%20Request%20Form%20(TIQ%20VXE519).pdf.md) | pdf | 165 | 2025-07-01 | converted |
| image-20250716-143706.png | image | 19 | 2025-07-16 | listed only |
| [sharp-export@strategic-shipping.com_20250714_160248.pdf](attachments/30663_sharp-export@strategic-shipping.com_20250714_160248.pdf.md) | pdf | 191 | 2025-07-16 | converted |
| 519.1.jpg | image | 1155 | 2025-07-21 | listed only |
| 519.1 (4e503d84-2d9d-4c7a-89e7-e4cf8fd79ba6).jpg | image | 489 | 2025-07-22 | listed only |
| 519.2.jpg | image | 622 | 2025-07-22 | listed only |
| 519.3.jpg | image | 558 | 2025-07-22 | listed only |
| 519.4.jpg | image | 532 | 2025-07-22 | listed only |
| 519.5.jpg | image | 482 | 2025-07-22 | listed only |
| 519.6.jpg | image | 392 | 2025-07-22 | listed only |
| 519.7.jpg | image | 495 | 2025-07-22 | listed only |
| 519.8.jpg | image | 436 | 2025-07-22 | listed only |
| 519.jpg | image | 552 | 2025-07-22 | listed only |
| [VXE519_maintenance.txt](attachments/30876_VXE519_maintenance.txt.md) | text | 27 | 2025-07-22 | converted |
| [VXE-519  WARRANTY REPLACEMENT 250701-1 7.23.2025.pdf](attachments/30910_VXE-519%20%20WARRANTY%20REPLACEMENT%20250701-1%207.23.2025.pdf.md) | pdf | 184 | 2025-07-23 | converted |
| [VXE-519 INTAKE.pdf](attachments/30906_VXE-519%20INTAKE.pdf.md) | pdf | 3140 | 2025-07-23 | converted |
| [CF-855-004 Diagnostic Evaluation Request Form VXE-519.docx](attachments/32396_CF-855-004%20Diagnostic%20Evaluation%20Request%20Form%20VXE-519.docx.md) | docx | 43 | 2025-09-19 | converted |
| image-20250922-184730.png | image | 31 | 2025-09-22 | listed only |
| [VXE-519  WARRANTY REPLACEMENT 250701-1 FINAL WITH PRICING.pdf](attachments/37335_VXE-519%20%20WARRANTY%20REPLACEMENT%20250701-1%20FINAL%20WITH%20PRICING.pdf.md) | pdf | 193 | 2025-12-15 | converted |
