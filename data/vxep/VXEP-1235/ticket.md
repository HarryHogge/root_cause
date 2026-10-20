# VXEP-1235: Release of 6.6 Software

- **Issue type:** Major Project
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-05-01
- **Updated:** 2026-02-18
- **Resolved:** 2026-02-18
- **Reporter:** Scott Whitney
- **Assignee:** Scott Whitney
- **Creator:** Scott Whitney
- **Parent:** VXEP-572 Sustainment: Autopilot & VMS
- **Links:** is a parent of AV-84 (Update to lower 200' VTOL transition to support increased MGTOW); is a parent of GCSS-271 (Restore forward dash speed to VXE30); is a parent of FS2-3649 (Remove Turret Code); is a parent of FS2-3126 (Ensure that common passwords are not used for different services (XCOMM & VTOL webpages))

## Description

### 6.6.0/1 - [Complete]  (November 2025)

- AP
- File I/O on XCOMM
- Remove any Priority Inheritance from: (move to 6.7)
- File I/O
- Webserver or related Tasks
- Remove Internal Airspeed Support (move to 6.7 - john has latest update on status)
- Note: I don't want to use John's solution in the HIL airdata driver.
- Stop sampling the high and low signals at 1kHz
- Update WCA Alerts for Nav Faults
- BLUE UAS - cannot store passwords as strings (webpages) - https://jenaero.atlassian.net/browse/FS2-3126
- Tech Debt:
- Data Scrub
- Remove unused fields, add desired fields, update docs, tooling updates (done by levi?)
- Need to continue to find data that can be cut out or stored less frequently (continues in 6.7)
- File Management
- Delete Old Logs to prevent Disk from filling up
- Need to delete once 50% of disc space is taken up (continues in 6.7)
- Remove turret code
- Fix XCOMM log pollution "MESSAGE_VTOL 2  6"
- Bug Fixes:
- Reject subsequent land immediately commands leading to VTOL being left in Attitude hold
- VTOL - cannot be left in Attitude hold
- Print-f -Wno-format fix on XCOMM (nice to have - levi)
- Adv Nav timestamp is wrong on GCS side panel (Kurt)
- Land Immediately Override Window fix (levi)
- GCS
- MGTOW input by Operator
- Dash Restoration
- for VXE 30 STD vehicles (and preMAGNSS)
- Firmware Version Confirmation/Check
- Upload/delete Mission.txt in handover process
- BLUE UAS - cannot store passwords as strings (GCS)
- Include the latest MediaClient in the 6.6.0 Installer
- Sim Flight Fix
- Using SIL as a base to simulate flights
- Bug Fixes:
- NDAA Compliant controller (simplified version for PMA was released in 6.4)
- Potentially a bug with inverted controls (seen at APEX)

## Comments (1)

### Scott Whitney, 2026-02-18

Completed and released Jan 2026

## Attachments (0)
