# FS2-2114: VXEP-514 - v696 Investigation - Software Regression Flight test incident

- **Issue type:** Epic
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Highest
- **Created:** 2024-07-25
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Scott Whitney
- **Assignee:** Scott Whitney
- **Creator:** Scott Whitney
- **Components:** Vehicle Incident Support 
- **Fix versions:** Release 6.3.4, Release 6.4
- **Links:** relates to VXEP-514 (VXE 696 - Software release 6.3.2 Asset 696 Takeoff Failure); is a child of VXEP-610 (Release of 6.4 Software)

## Description

- Path 1:
- Create a new branch 1.55.03 (Scott)
- change the TCB table to 200. (Scott)
- Regression Test. (Liam and/or Brandon)
- Path 2:
- Create a new branch 1.55.04 (Scott)
- Change the TCB table to 200. (Scott)
- Cherry pick Gabe's change that converted temporary actuator tasks to functions triggered by the system timer. (Gabriel Staples)
- Test against Script, Check for memory leak
- Move code from infinite for loops to modulated conditional checks in MC cycle task (Kurt)
- MC Launch
- MC Land
- MC RTLand
- MC Brake
- MC Stop/Safe
- Landing wrapup
- Check for others
- Test Against Script, Check for memory Leak
- Cherry pick the file I/O consolidation (Gabriel)
- Regression Test (Liam and/or Brandon)
- In Parallel:
- GCS to stop querying for version number while in flight. (Michael)


Initial Information (7/25/24):
[12:28 PM] Ruysser Gabler - VTOL cut on take off again. at 80 ft this time 
[12:29 PM] Ruysser Gabler - HSV is informed and holding flight 
 
[embedded: image-20240725-200954.png]
[embedded: image-20240725-200947.png]

## Comments (6)

### Scott Whitney, 2024-07-25

@Mark Squillante @Laszlo Juhasz @Cameron Chapman

### Mark Squillante, 2024-07-26

I found the green wire on pin 3 of J4 on the VTOL Interface PCBA could potentially have an intermittent connection. This corresponds to “SERVO4” and goes to the VTOL CPU board through a voltage divider and into the VTOL CPU at pin 124, labeled “RF0_SRV4”. This is going to one of the lift motors I believe. Doing a tug test and wiggle test on the wire I do not see a break in continuity so likely not a problem. Most likely that connection is fine and too much insulation was stripped from the wire.
[embedded: J4 wire.jpg]

### Mark Squillante, 2024-07-26

Doing a resistance check on the AS150 contact passes, showed 169uohms (limit is 235 uohms). No evidence of solder reflow.

### Mark Squillante, 2024-07-26

Able to connect to web pages via VTOL, nothing looks out of the ordinary there.

### Mark Squillante, 2024-07-26

Getting this error during Launch Wizard, tried with 2 other ADPs and get the same message.

[embedded: image-20240726-225755.png]

### Mark Squillante, 2024-07-29

Got same error on iron bird using V696 avionics box. @Connor Peebles mentioned this could be due to the avionics not being more or less in the same position relative to VTOL ala assembled plane

## Attachments (9)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| C1002.MP4 | video | 613349 | 2024-07-25 | listed only |
| DATALOG_VTOL_696 1.zip | archive | 8716 | 2024-07-25 | listed only |
| DATALOG_VTOL_696.zip | archive | 8716 | 2024-07-25 | listed only |
| DATALOG_XCOMM_696 1.zip | archive | 10615 | 2024-07-25 | listed only |
| DATALOG_XCOMM_696.zip | archive | 10615 | 2024-07-25 | listed only |
| image-20240725-200947.png | image | 3964 | 2024-07-25 | listed only |
| image-20240725-200954.png | image | 5698 | 2024-07-25 | listed only |
| J4 wire.jpg | image | 1010 | 2024-07-26 | listed only |
| image-20240726-225755.png | image | 262 | 2024-07-26 | listed only |
