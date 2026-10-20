# VXEP-604: VXE 600 Land at ELZ was un-enabled

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-09-05
- **Updated:** 2026-03-02
- **Resolved:** 2025-02-25
- **Reporter:** Pat Wells
- **Assignee:** Josh Burrell
- **Creator:** Pat Wells
- **Labels:** GCS, TIQUILA, Weekly-incident-tracker
- **Links:** relates to ENG-3144 (Land at ELZ was un-enabled); relates to SMUP-68 (Any time the launch wizard is opened it will disable the ‘Land at ELZ’ behavior and select ‘Land at PLZ’.  Operators should always re-select ‘Land at ELZ’ after opening the launch wizard.); relates to RMA-459 (VXE-600 Card Swap & Expansion 250429-9)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 600
- **Root Cause:** Behaves as expected
- **Incident Type:** Near Miss
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

From LM FSR:
On 27 August, during the MOD Reiver Look 2 T&E in the UK, Land at ELZ was enabled before launch of V600 and was somehow disabled (not by the operator).  One operator told the PIC operator to check it before landing because he had seen it become un-enabled before.
In order to have a backup GCS standing by, after uploading the mission to the aircraft in the Launch Wizard, the operator disconnected the 1st GCS from the plane, connected a 2nd GCS, saved the mission from the plane onto the 2nd GCS, then disconnected and re-connected with the 1st GCS.  Land at ELZ on the 1st GCS might have been un-enabled during the disconnecting and reconnecting. 
AAR Attached

## Corrective Action

Ensure manual captures the following: Any time the launch wizard is opened it will disable the ‘Land at ELZ’ behavior and select ‘Land at PLZ’. Operators should always re-select ‘Land at ELZ’ after opening the launch wizard. https://jenaero.atlassian.net/browse/SMU-135

## Comments (5)

### Pat Wells, 2024-09-16

@Greg Fryer checking in for any updates ahead of the Air Worthiness brief with TIQ on Wed 9/18

### David Grosher, 2024-09-18

@Ted Trowbridge FYSA

### Pat Wells, 2024-12-05

@Ted Trowbridge @David Grosher any updates on this?

### Ted Trowbridge, 2024-12-06

@Pat Wells @David Grosher 
The system is behaving as designed.  Any time the launch wizard is opened it will disable the ‘Land at ELZ’ behavior and select ‘Land at PLZ’.  Operators should always re-select ‘Land at ELZ’ after opening the launch wizard.
I’m not sure if that is covered in any manuals/documentation, perhaps an update is necessary?

### Alexander Alan Arnold, 2024-12-10

If it is behaving as designed, should we just identify the corrective action (update manual as required) and then move to close out this item? @Ted Trowbridge @Pat Wells @David Grosher

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V600_240827_094150_pack.zip | archive | 5468 | 2024-09-05 | listed only |
