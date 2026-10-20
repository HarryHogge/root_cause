# VXEP-1416: VXE-542 RMA # 250630-1 - Investigation

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2025-07-16
- **Updated:** 2025-12-31
- **Resolved:** 2025-12-30
- **Reporter:** Camron Richardson
- **Assignee:** Samuel Lopez
- **Creator:** Camron Richardson
- **Links:** relates to VXEP-1368 (VXE-542 Voltage issues); relates to RMA-721 (VXE-542 RMA # 250630-1)
- **Issue color:** purple

## Description

https://jenaero.sharepoint.com/sites/FlightSafety/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FFlightSafety%2FShared%20Documents%2FIncident%20Reports%2FVXEP%2D1416%20VXE%2D542%20%2D%20Low%20Forward%20Motor%20Voltage&sortField=Modified&isAscending=false&viewid=7181a7a2%2Dd286%2D47c9%2Dbdd3%2D9195ef18282c&csf=1&web=1&e=uWSk6G&ovuser=1876f61a%2D3bdb%2D4843%2Dae70%2D75ed0ccb7404%2Ccrichardson%40edgeautonomy%2Eio&OR=Teams%2DHL&CT=1752874542635&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiI0OS8yNTA3MDMxODgwNiIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D&CID=8e7225ac%2Db27d%2D4532%2D8665%2D4bdcc710029d&cidOR=SPO&FolderCTID=0x012000D03119522A011A40817D7F0F59E3A7EF 
Low current readings in VXE - 542 Forward Motor, analysis shows that the Nose is most likely not the issue, however I am not ruling it out as it still showed significantly lower readings. Current plan is to take apart the nose to inspect CSB and ESC, if findings concur everything is fine in the nose, I will work my way back tracing power and ESC Signal to Avionics Box. Initial Assumption is that there is a problem with both CSB and Avionics box as the problem gets worse when using fuse 542 and Nose 542, and get’s slightly better when using alternate fuse. There are no boards/PCBs in between the avionics box and the nose cone, so unless the physical cable is damage, likely suspects are Avionics Box, CSB, or ESC

Would like to verify if actual current draw is consistent with readings on GCS. Verifying low current draw would eliminate current sense board.
[embedded image-20250717-033410.png]

To rule out avionics box, I believe the best course of action would be to take it out of the plane and plug it in to the Iron Bird in the electronics shop to verify proper readings using equipment proven to be working.

7/18/2025 - Camron Richardson tested the avionics box on iron bird and found similar results to using a different nose and #542 fuse. This may indicate a problem with the avionics box, at idle the average power is about half of the instant power and a little more than half of the expected idle power, in contrast, the iron bird avionics box had similar average power and instant power and had a power of about 19.5 and 19.7
Videos attached of the test

## Issue Status

- Aircraft reported returned to customer. (asked about avbox location)
- Investigation summarized here VXE-542 RMA # 250630-1 - Investigation Findings.xlsx
- From info in the sheet, issue seems to follow 542 avbox.


2025-12-31
This issue has been closed, please see [VXEP-1368] VXE-542 Voltage issues - Jira

## Comments (0)

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20250717-033410.png | image | 271 | 2025-07-16 | listed only |
| VXE - 542 Avionics Box Test.MOV | video | 63329 | 2025-07-18 | listed only |
| XE-102 Control.MOV | video | 61587 | 2025-07-18 | listed only |
