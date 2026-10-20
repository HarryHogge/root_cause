# FS2-2854: Jason's Open Investigations

- **Issue type:** Story
- **Status:** To Do
- **Priority:** Highest
- **Created:** 2025-02-12
- **Updated:** 2026-09-04
- **Reporter:** Jason Scherer
- **Assignee:** Jason Scherer
- **Creator:** Jason Scherer
- **Links:** relates to VXEP-555 (VXE 530 Anomalies on Launch and in flight); relates to VXEP-916 (VTOL Controller stopped talking during EMC emission ground tests (aircraft not radiated)); relates to VXEP-416 (VXE 539 Failure to launch); relates to FS2-2337 (Unexpected pause during takeoff (VXEP-555)); relates to FS2-2336 (Mission Failed to Sync (VXEP-555)); relates to FS2-2339 (Investigate Delay in GCS accuracy during landing (VXEP-555)); relates to VXEP-844 (VXE724 VTOL Climb Abort Lift System Fault); relates to FS2-2616 (Climb abort FC fault but AC did not abort take off); relates to FS2-2321 (Create a consolidated report on mismatched SW/FW versions for VXE-572/573/574/628/688/594); relates to VXEP-1054 (VXE 490 going off task after Waypoint 1 on two flights in a row); relates to FS2-3040 (Investigate VXEP-1054 VXE 490 going off task after Waypoint 1 on two flights in a row); relates to FS2-3092 (VXEP-555 20-30 second lag in vehicle position on GCS); relates to FS2-3093 (NCR-250311 - CW 642 - 5665 - CW WDT Resets); relates to RMA-563 (VXE-529 SD CARD RMA 250305-6); relates to VXEP-1149 (VXE 529 SD Card failure while following power cycling Advisory notice)
- **Sprint:** FS2 Sprint 40, FS2 Sprint 31, FS2 Sprint 32, FS2 Sprint 34, FS2 Sprint 29, FS2 Sprint 30, FS2 Sprint 33

## Description

Priority list:
- Training SIL for LRR
- https://jenaero.atlassian.net/browse/FS2-3425
- https://jenaero.atlassian.net/browse/VXEP-1054
- https://jenaero.atlassian.net/browse/FS2-3040
- https://jenaero.atlassian.net/browse/VXEP-555 Investigating Issues 1 & 5 with new data
- https://jenaero.atlassian.net/browse/FS2-2336
- https://jenaero.atlassian.net/browse/FS2-3092
- https://jenaero.atlassian.net/browse/FS2-2337
- https://jenaero.atlassian.net/browse/FS2-2339
- UAP Development
- 29 Palms miss-match firmware report incidents
- Other High Priority Incidents

## Comments (27)

### Jason Scherer, 2025-02-18

Request from Dave: NCR 813 Added this morning to top of the list

### Jason Scherer, 2025-02-18

Request from Dave: VXE 337 re-priorities to #2 moving 29 Palms down to #3

### David Grosher, 2025-02-19

@Jason Scherer I added an RMA request to your list in priority #3.

### Jason Scherer, 2025-02-19

Added VXEP-835

### Jason Scherer, 2025-02-20

Added https://jenaero.atlassian.net/browse/FS2-2993 Work ticket in support of https://jenaero.atlassian.net/browse/VXEP-900

### Jason Scherer, 2025-02-20

NCR 813 is blocked waiting for HW rework. Switching to https://jenaero.atlassian.net/browse/VXEP-900 investigation.

### Jason Scherer, 2025-02-22

https://jenaero.atlassian.net/browse/VXEP-900 Report needs HW team review. Looks like a propulsion failure on motor 4. Switching to https://jenaero.atlassian.net/browse/VXEP-835

### Jason Scherer, 2025-02-22

Initial updates made to https://jenaero.atlassian.net/browse/VXEP-835 report. Probably needs more work. Switching back to https://jenaero.atlassian.net/browse/VXEP-900 to plot expected/actual motor consumption based on Camerons documentation.

### Jason Scherer, 2025-02-24

Added https://jenaero.atlassian.net/browse/VXEP-600 with higher priority than completing the 29 Palms report as requested by Dave.

### Jason Scherer, 2025-02-24

Per Dave https://jenaero.atlassian.net/browse/VXEP-900 (V337) will be reviewed and updated further by Eric B.

### Jason Scherer, 2025-02-25

Removed https://jenaero.atlassian.net/browse/VXEP-835 since the investigation and report are complete, and the ticket has been closed.

### Jason Scherer, 2025-02-25

Added NCR-250225 - 5538 & put UAP development above 29 Palms report in priority.

### Jason Scherer, 2025-02-28

https://jenaero.atlassian.net/browse/VXEP-366 Correct report format created with investigation report information added. Waiting for review.

### Jason Scherer, 2025-03-10

Added https://jenaero.atlassian.net/browse/VXEP-1061 since I spent some time over a few days looking into the data and creating the report which is now in review.

### Jason Scherer, 2025-03-11

Added https://jenaero.atlassian.net/browse/VXEP-555 to number 4 on list. Added https://jenaero.atlassian.net/browse/FS2-3093 to top of list.

### Jason Scherer, 2025-03-12

Added NCR for CW 642. Blocked waiting for firmware update and retest

### Jason Scherer, 2025-03-12

Currently working the requirements analysis for the Training SIL project, so my investigation time is limited.

### Jason Scherer, 2025-03-20

https://jenaero.atlassian.net/browse/VXEP-600 Report ready for review.

### Jason Scherer, 2025-03-22

Linked https://jenaero.atlassian.net/browse/RMA-563 & https://jenaero.atlassian.net/browse/VXEP-1149

### Jason Scherer, 2025-03-22

Unlinking https://jenaero.atlassian.net/browse/VXEP-651 since the issue was determined to be operator error, the CA will be accomplished by updating GCS software, and the report for this incident is included in the 29 Palms software mismatch report.

### Jason Scherer, 2025-03-22

Unlinking https://jenaero.atlassian.net/browse/VXEP-155. We don’t have sufficient log data to proceed further, and all software related tasks have been complete.

### Jason Scherer, 2025-03-22

Unlinked https://jenaero.atlassian.net/browse/FS2-2837 Since the report has been included in the 29 Palms Software Mismatch report.

### Jason Scherer, 2025-03-22

Completed subtask https://jenaero.atlassian.net/browse/VXEP-377. Unlinking from this ticket.

### Jason Scherer, 2025-03-22

Unlinking https://jenaero.atlassian.net/browse/VXEP-732 Software investigation complete. Loss of CW cause is unknown. Report has been added to 29 Palms software mismatch report.

### Jason Scherer, 2025-03-22

Unlinking https://jenaero.atlassian.net/browse/VXEP-1061 Report is complete and pending review. So far no feedback has been received which I think is good news.

### Jason Scherer, 2025-03-22

Unlinking https://jenaero.atlassian.net/browse/VXEP-600 and https://jenaero.atlassian.net/browse/FS2-3023 since the report is complete and I have not received any further requests.

### Jason Scherer, 2025-03-22

Unlinking https://jenaero.atlassian.net/browse/VXEP-220 due to understanding root cause. CAs reside on GCS. Unlinking https://jenaero.atlassian.net/browse/FS2-2332 due to same reasons. Root cause for ap link faults is GCS mission simulation blocking uplink messages due to a single threaded system.

## Attachments (0)
