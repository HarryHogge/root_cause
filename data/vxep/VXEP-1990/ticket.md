# VXEP-1990: B40 1023 TW power flipped in CW

- **Issue type:** Problem
- **Status:** Document C/CA
- **Priority:** Medium
- **Created:** 2026-09-08
- **Updated:** 2026-09-09
- **Reporter:** Cameron Chapman
- **Assignee:** Alexander Alan Arnold
- **Creator:** Cameron Chapman
- **Links:** relates to XKIT-5113 (B40 Non Flight-blocker flight test issue collector/Squawk List); relates to VXEP-1991 (Test all contacts on all ports accessible to customer prior to shipment (ex: payloads)); relates to VXEP-1992 (Ensure all cables are tested on the automatic tester prior to aircraft installation)

## Description

- Interconnect https://jennings-aeronautics-2.365.altium.com/designs/0D457246-7BFE-43ED-9595-19E723DA4D77

Team, please see the write up below. I am hoping the testing was completed in a way that makes sense and proves the issue is with 1023 CW. 
During ground checks we encountered an issue using the TW Module SN: CRP009 on aircraft 1023. I pulled local engineering support to assist with troubleshooting.
 
We started by tapping into TWJ1 with a multimeter to check for 28 volts on pin 6 (wing payload power) and pin 5 (wing payload return). We saw a -28V read out. This caused us to jump over to TN1078 and TN1092 which both read +28V. We then referenced the B35/40 interconnect and traced the pin out back to CW connections verifying the pinout through TN 1023 Wing Tip and Lift Boom. 
 
[embedded: image-20260908-223858.png]
From here, we began testing the CWJ1 blindmate connector coming from the SRR board. A multimeter was connected to aircraft with power applied to pin 11 (WP power return) and Pin 12 (WP power). TN 1023 read -28V confirming the pinout is reversed coming from the SRR Board. We also checked TN1078 and TN1092 and both read +28 volts as expected. 
 
[embedded: image-20260908-223907.png]
[embedded: image-20260908-223920.png]
Note: TW Module SN: CRP009 was confirmed to be working on TN1078 and TN1092. All testing was done with the same batteries and Same GCS.

## Plan

- 1023 fixed. Working on CAs
- Discussing here https://teams.microsoft.com/l/message/19:2df527170f4646d0a99ecbd2df00a370@thread.v2/1788908265892?context=%7B%22contextType%22%3A%22chat%22%7D

Recommended CAs
- Working on: TBD if required to complete before closing this issue. https://jenaero.atlassian.net/browse/VXEP-1991 
https://jenaero.atlassian.net/browse/VXEP-1992

## Issue Status

216023-01 harness looks like it has a pin swap. 
1023: Seems resolved: tested after swapping pins we were able to power on the trellis ware and pull up the web gui and management tool for the device 
[embedded: image-20260909-155442.png]
Standard 
[embedded: image-20260909-155457.png]

## Comments (1)

### Alexander Alan Arnold, 2026-09-09

removed B35 CW panel and inspected SSR board against 2160234 Rev01 as reference and visual inspection showed 2 connections
[embedded: image (16).png]
 removing SRR breakout cable to run continuity check on all pins to confirm cause of issue 
DRAWING
[embedded: image-20260909-155755.png]
continuity test ran after removing ssr board that held connections. connections swapped and ran continuity test after to confirm successful swap 
reinstalled SSR board in CW and then installed CW on 1023 and applied power to test connection on CW to lift boom saw expected results (positive and negative where they were expected) then installed booms, wingtips and trellis ware then turned aircraft back and were able to get into the trellisware

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20260908-223858.png | image | 133 | 2026-09-08 | listed only |
| image-20260908-223907.png | image | 13 | 2026-09-08 | listed only |
| image-20260908-223920.png | image | 183 | 2026-09-08 | listed only |
| image (16).png | image | 349 | 2026-09-09 | listed only |
| image-20260909-155442.png | image | 263 | 2026-09-09 | listed only |
| image-20260909-155457.png | image | 8321 | 2026-09-09 | listed only |
| image-20260909-155755.png | image | 6 | 2026-09-09 | listed only |
