# RMA-230: VXE 508 240325-2

- **Issue type:** Aircraft
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-03-25
- **Updated:** 2024-06-13
- **Resolved:** 2024-06-05
- **Reporter:** Sean Odell
- **Assignee:** Sean Odell
- **Creator:** Sean Odell
- **Links:** relates to VXEP-319 (VXE-522 / VXE-529 Corrective Action: Provide instructions to customers to identify and replace SD Card, or RMA to Edge); relates to VXEP-320 (VXE-522 / VXE-529 Corrective Action: Add code to automatically timeout upon SD Card read and automatically reformat SD Card); relates to VXEP-321 (VXE-522 / VXE-529 Corrective Action: Add power down recognition, refrain from writing or reading to SD Card during power down); relates to VXEP-331 (VXE-522 / VXE-529 / VXE-508 Follow up testing: Test SD Card connection while on shaker table); relates to VXEP-332 (VXE-522 / VXE-529 / VXE-508 Follow up testing: Investigate BT1 storage life and use cases on XCOMM. Investigate charge and discharge rate.); relates to VXEP-333 (VXE-522 / VXE-529 / VXE-508 Follow up testing: Investigate SD Card new and old PN's. Investigate how speed difference could affect XCOMM.)
- **Customer:** FBI
- **Vehicle Tail Number:** 504

## Description

FBI Aircraft that the LM FSR attempted to troubleshoot a lack of connection by GCS. In the end, it needs to be evaluated, reworked, and shipped back.


LM HANDLING SHIPPING TO AND FROM Customer

## Comments (8)

### Matt Philley, 2024-04-03

@Sean Odell @Steve Stack it will be good to see if these aircraft connection issues are similar to the XCOMM issues that happened on AC522 and AC529 that are still in investigation from TIQ
https://jenaero.atlassian.net/browse/VXEP-236
https://jenaero.atlassian.net/browse/VXEP-237

### Matt Philley, 2024-04-05

@Ben Norris @Katherine Duberg Aircraft is exhibiting similar behavior as VXE30 AC 522 and 529 where AC tested fine through SCO checkout and flight test, was delivered and sat around for months, then would not connect. Troubleshooting for those was XCOMM issues. Can yall check out AC 508 Avi Box (handed off to Ben) to see if its a similar issue which might point to a trend?
Jira tickets are linked in my comment below here for reference to those issues and investigations. 
NCRs from AC 522 and 529 here:
AC 522 - Source Insp (RMA) - Misc Source Snags & AC Wont Connect to GCS
AC 529 - Source Insp (RMA) - Misc Source Snags & AC Wont Connect to GCS

### Matt Philley, 2024-04-08

@Katherine Duberg @Ben Norris there is an investigation report linked here for the results of Connor’s investigation of AC 522 and AC 529 XCOMs. Page 6 has some steps he went thru to figure out the loop it was stuck in and by removing the SD card it was able to boot to the webpage, so we should try that. @Connor Peebles said he could help answer questions too. 
VXE-522 & VXE-529 XCOMM board failures at LM Source inspection.pptx

### Katherine Duberg, 2024-04-08

Removed SD card from XComm 5-5277 and reflashed, which allowed it to connect to webpage. Replaced with a new SD card, reperformed programming procedure. Xcomm now connecting properly to network. Performed functional checkout on AV box and found a faulty transponder cable; replaced transponder cable. AV box now passing all functional checkouts.

### Katherine Duberg, 2024-04-09

Per Connor’s request I also tested battery on Xcomm, after charging maintained a voltage of >2.7V (Xcomm procedure)

### Sean Odell, 2024-04-17

Aircraft hardware and software correct and up to date. Reworked Avionics by swapping out SD-card. Aircraft is now awaiting expanded payload cutout completed once BOM and procedure are ready.

@Pat Wells FYI

### Sean Odell, 2024-05-31

508 is complete and awaiting 504 completion before given to LM to ship to FBI.

### Sean Odell, 2024-06-05

Hand Delivered to Lockheed for shipment back to the customer.

## Attachments (36)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 20240404_130901.jpg | image | 2333 | 2024-04-09 | listed only |
| 20240404_130912.jpg | image | 2162 | 2024-04-09 | listed only |
| 20240404_130918.jpg | image | 2227 | 2024-04-09 | listed only |
| 20240404_130925.jpg | image | 2150 | 2024-04-09 | listed only |
| 20240404_130927.jpg | image | 1846 | 2024-04-09 | listed only |
| 20240404_130933.jpg | image | 1949 | 2024-04-09 | listed only |
| 20240404_131305.jpg | image | 2413 | 2024-04-09 | listed only |
| 20240404_131313.jpg | image | 2093 | 2024-04-09 | listed only |
| 20240404_131320.jpg | image | 2771 | 2024-04-09 | listed only |
| 20240404_131344.jpg | image | 2024 | 2024-04-09 | listed only |
| 20240404_131355.jpg | image | 1952 | 2024-04-09 | listed only |
| 20240404_131411.jpg | image | 1819 | 2024-04-09 | listed only |
| 20240404_131418.jpg | image | 1689 | 2024-04-09 | listed only |
| 20240404_131611.jpg | image | 1300 | 2024-04-09 | listed only |
| 20240404_131614.jpg | image | 1509 | 2024-04-09 | listed only |
| 20240404_131617.jpg | image | 1488 | 2024-04-09 | listed only |
| 20240404_131634.jpg | image | 1581 | 2024-04-09 | listed only |
| 20240404_131638.jpg | image | 1596 | 2024-04-09 | listed only |
| 20240404_131807.jpg | image | 1724 | 2024-04-09 | listed only |
| 20240404_131811.jpg | image | 1614 | 2024-04-09 | listed only |
| 20240404_131818.jpg | image | 1601 | 2024-04-09 | listed only |
| 20240404_131847.jpg | image | 2058 | 2024-04-09 | listed only |
| 20240404_131851.jpg | image | 1662 | 2024-04-09 | listed only |
| 20240404_131901.jpg | image | 1661 | 2024-04-09 | listed only |
| 20240404_131930.jpg | image | 3182 | 2024-04-09 | listed only |
| 20240404_131934.jpg | image | 2422 | 2024-04-09 | listed only |
| 20240404_131937.jpg | image | 2594 | 2024-04-09 | listed only |
| 20240404_131941.jpg | image | 2259 | 2024-04-09 | listed only |
| 20240404_131943.jpg | image | 2538 | 2024-04-09 | listed only |
| 20240404_132010.jpg | image | 2816 | 2024-04-09 | listed only |
| 20240404_132014.jpg | image | 2618 | 2024-04-09 | listed only |
| 20240404_132018.jpg | image | 3568 | 2024-04-09 | listed only |
| 20240404_132023.jpg | image | 2592 | 2024-04-09 | listed only |
| 20240404_132045.jpg | image | 2464 | 2024-04-09 | listed only |
| [VXE-508 Induction Paperwork 4-4-2024.pdf](attachments/19966_VXE-508%20Induction%20Paperwork%204-4-2024.pdf.md) | pdf | 1428 | 2024-04-09 | converted |
| VXE 508 Software Version 4-17-2024.JPG | image | 29 | 2024-04-17 | listed only |
