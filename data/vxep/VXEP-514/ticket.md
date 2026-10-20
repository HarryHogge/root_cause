# VXEP-514: VXE 696 - Software release 6.3.2 Asset 696 Takeoff Failure

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-07-25
- **Updated:** 2024-12-23
- **Resolved:** 2024-08-23
- **Reporter:** Scott Whitney
- **Assignee:** David Grosher
- **Creator:** Scott Whitney
- **Links:** relates to FS2-2114 (VXEP-514 - v696 Investigation - Software Regression Flight test incident); relates to VXEP-429 (SW Release 6.3.0 Asset 481 Takeoff Failure); relates to VXEP-845 (Remove and tag hardware from 696 incident)
- **Severity:** 1 - Flight Critical

## Description

Ref: VXEP-514 SW 6.3.2 Asset 696 Takeoff Failure 20240725.pptx
Fishbone:  VXEP-514 SW 6.3.2 Asset 696 Takeoff Failure 20240725.pptx
Photos & Video: 
Folder: VXEP-514 (SW Release 6.3.0 Asset 696 Takeoff Failure)

## Corrective Action

Short term: VTOL AP will be reset by launch wizard. Minor change in TCB trace table to push memory corruption out of critical data space. 
Long Term: Task consolidation, create timer based callbacks and File I/o refactor.

## Plan

- Data review. See https://jenaero.atlassian.net/browse/FS2-2114
- Inspect electronics for power or motor assy failure evidence @Mark Squillante

## Issue Status

Issue was identified. There is memory corruption in the Config Manager that occurs after 161 TCB task events occur (creation/deletion).  This could be related to new features but it is unlikely, it is most likely due to the dynamic memory allocation associated with task creation and deletion across the course of a flight.

## Root Cause

Issue was identified. There is memory corruption in the Config Manager that occurs after 161 TCB task events occur (creation/deletion).  This could be related to new features but it is unlikely, it is most likely due to the dynamic memory allocation associated with task creation and deletion across the course of a flight.

## Comments (2)

### Scott Whitney, 2024-07-25

@Cameron Chapman @Laszlo Juhasz @Mark Squillante

### Cody Smisek, 2024-10-07

@Greg Fryer I see this issue is closed. Can we dispose of damaged hardware and salvage anything worth keeping? Currently stored under engineering stairwell area.

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| C1002.MP4 | video | 613349 | 2024-07-25 | listed only |
| DATALOG_VTOL_696 1.zip | archive | 8716 | 2024-07-25 | listed only |
| DATALOG_VTOL_696.zip | archive | 8716 | 2024-07-25 | listed only |
| DATALOG_XCOMM_696 1.zip | archive | 10615 | 2024-07-25 | listed only |
| DATALOG_XCOMM_696.zip | archive | 10615 | 2024-07-25 | listed only |
| image-20240725-224055.png | image | 3964 | 2024-07-25 | listed only |
| image-20240725-224120.png | image | 5698 | 2024-07-25 | listed only |
