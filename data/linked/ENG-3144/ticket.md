# ENG-3144: Land at ELZ was un-enabled

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-08-27
- **Updated:** 2025-06-02
- **Resolved:** 2025-02-25
- **Reporter:** Garret Moose
- **Assignee:** Pat Wells
- **Creator:** Garret Moose
- **Links:** relates to VXEP-604 (VXE 600 Land at ELZ was un-enabled)

## Description

On 27 August, during the MOD Reiver Look 2 T&E in the UK, Land at ELZ was enabled before launch of V600 and was somehow disabled (not by the operator).  One operator told the PIC operator to check it before landing because he had seen it become un-enabled before.
In order to have a backup GCS standing by, after uploading the mission to the aircraft in the Launch Wizard, the operator disconnected the 1st GCS from the plane, connected a 2nd GCS, saved the mission from the plane onto the 2nd GCS, then disconnected and re-connected with the 1st GCS.  Land at ELZ on the 1st GCS might have been un-enabled during the disconnecting and reconnecting. 
I will try to get and attach the AAR.

## Comments (5)

### Pat Wells, 2024-08-28

@Garret Moose acknowledged.  Will action when AAR’s are uploaded.

### Pat Wells, 2024-09-05

@Garret Moose added AAR and will open investigation.

### Pat Wells, 2024-12-10

@Garret Moose 
The system is behaving as designed. Any time the launch wizard is opened it will disable the ‘Land at ELZ’ behavior and select ‘Land at PLZ’. Operators should always re-select ‘Land at ELZ’ after opening the launch wizard.

### Pat Wells, 2025-02-04

Implementing corrective actions.

### Pat Wells, 2025-02-25

Corrective action complete. Manual update

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V600_240827_094150_pack.zip | archive | 5468 | 2024-09-05 | listed only |
