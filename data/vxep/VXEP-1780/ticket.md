# VXEP-1780: VXE 864 Crash

- **Issue type:** Incident (8D)
- **Status:** D6 - Implementing Corrective Actions
- **Priority:** Highest
- **Created:** 2026-03-20
- **Updated:** 2026-10-05
- **Reporter:** Drew Hildreth
- **Assignee:** David Grosher
- **Creator:** Drew Hildreth
- **Labels:** GS_Closed, Hardware, USBP, Weekly-incident-tracker
- **Links:** covered by FS2-4304 (VXEP-864 : CBP v864 Investigation); relates to RMA-929 (VXE-864 RMA 260226-2); relates to VXEP-1775 (VXE-937 Crashed after briefly losing link.); relates to VXEP-1978 (VXE 863 Loss of Link warning resulted in uncontrolled descent ); relates to FS2-4473 (Investigate and Implement Detection and Handling of Stale Air Data in FW AP)
- **Customer:** USBP
- **Vehicle Tail Number:** VXE 864
- **Problem Type:** Discovered Issue
- **Root Cause:** Xcomm WDT creates stale FWAP data resulting in aircraft loss
- **Severity:** 1 - Flight Critical
- **Executive Summary:** Suffered Xcomm WDT. Customer receiving bailment aircraft to continue operations. Probable cause Software.

## Description

** GS Ticket for USBP Crash VXE-864 ** 
** Linked to engineering investigation ticket. **

Aircraft did not RTB after it went lost comms. Operators attempted to go to the location of the lost comms orbit with an SGCS1 Radio in an attempt to reconnect to the aircraft but were unsuccessful. Ultimately aircraft crashed.

## Corrective Action

- Production Engineer to save the encryption key
- engineering to provide tool pull encryption key and allow for easy copy/paste into traveler  Not Accepted. This can be copied and pasted from the original log files. [dgrosher]
- https://jenaero.atlassian.net/browse/FS2-4473
- Additional Diagnostics for Memory Corruption Debugging @Scott Whitney Can you link existing tasks to this CA?
- Safe String operations @Scott Whitney Can you link existing tasks to this CA?

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

## Comments (4)

### Pat Wells, 2026-08-11

Requested update on CA 8/11/2026

### Jackson Riley Curvin, 2026-08-18

@David Grosher has the corrective action been completed?

### David Grosher, 2026-08-18

@Jackson Riley Curvin The one that is linked is done in v6.7.1. The other one is not accepted. It can be copied and pasted from the log file as it currently is.

### Zachary Mann, 2026-10-05

@David Grosher All of the linked issues seem to have been completed with only the investigation under review, are we able to move this to D7?

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20260313-035512.png | image | 3217 | 2026-03-20 | listed only |
| image-20260317-215112.png | image | 7 | 2026-03-20 | listed only |
| image-20260319-191614.png | image | 51 | 2026-03-20 | listed only |
| v864_xcomm_DATALOG.zip | archive | 40738 | 2026-03-20 | listed only |
| vtol_864.zip | archive | 1229 | 2026-03-20 | listed only |
| [VXEP-1780_VXE-864_Vehicle Investigation_20260527 (1).pdf](attachments/63948_VXEP-1780_VXE-864_Vehicle%20Investigation_20260527%20(1).pdf.md) | pdf | 593 | 2026-08-07 | converted |
