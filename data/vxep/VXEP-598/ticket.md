# VXEP-598: VXE 574 Aircraft made hard right turn away from PLZ during VTOL landing

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-09-03
- **Updated:** 2026-09-14
- **Resolved:** 2025-02-14
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** Mismatched_SW/FW, No_crash, PMA263, Training, Weekly-incident-tracker
- **Links:** relates to RMA-361 (VXE-574 240925); relates to FS2-2321 (Create a consolidated report on mismatched SW/FW versions for VXE-572/573/574/628/688/594); relates to FS2-2838 (Investigate VXEP-598)
- **Customer:** PMA263
- **Vehicle Tail Number:** 574
- **Corrective Action:** None
- **Plan:** Add flight timeline slide to report
- **Issue Status:** aircraft returned to RMA
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

Note this is from the batch of incidents previously reported at 29 Palms
Received from operator:
Comes in for a landing, VTOL motors kick on, then the bird makes a right hand turn AWAY from the landing spot, then when it realizes it’s off course it turns around to try again, but can only fly backwards. The operator at the time tried to steer the aircraft back toward the landing spot with no results. The aircraft continues to travel backwards until the operator had to abort the launch before we broke airspace and caused a safety of flight issue. 

AAR Attached
Report: Vehicle Investigation VXEP-598.pptx
xcomm & vtol logs downloaded and stored here VXEP-598 VXE574 - C. Smisek 11/12/2024
SW out of date
VTOL = 1.44
XCOMM = 4.60

## Root Cause

Operator Error: Misconfigured SW/FW versions
Loss of control caused by known land abort bug (triggered by lift system power fault, likely caused by IMU sensor)

## Comments (19)

### David Grosher, 2024-09-03

@Pat Wells There is no VTOL data in the AAR

### David Grosher, 2024-09-24

@David Grosher Take a look at configuration of AV.

### David Grosher, 2024-09-25

@Pat Wells This vehicle is also misconfigured, the SW/FW images do not match. 
GCS v6.1.2
xcomm v4.60
FW AP v6.05m
VTOL UNKNOWN - No data

### Pat Wells, 2024-09-25

@David Grosher the aircraft is actaully enroute back to SLO on RMA.
Does your team even need to look at it now given the SW/FW mismatch?

### Cody Smisek, 2024-11-07

@David Grosher Aircraft in SLO engineering awaiting next steps.

### David Grosher, 2024-11-08

@Cameron Chapman Can you pull the VTOL data off of this vehicle and then return to RMA.

### Cameron Chapman, 2024-11-12

@Giovanni Gonzalez or @Cody Smisek are you available to pull data from this aircraft?

### Cody Smisek, 2024-11-12

@Cameron Chapman I will perform Dave’s request.

### Cody Smisek, 2024-11-12

avionics box was already partially removed from fuselage. Removed fully for data downloading and connected to engineering iron bird with associated center wing (vtol). VTOL AP IP wasn’t configured per the tail number (was configured as tail number 1).

### Cody Smisek, 2024-11-12

@David Grosher @Cameron Chapman files downloaded. aircraft returned to RMA.

### Pat Wells, 2024-12-05

@David Grosher is this moving any farther forward or are we closing this due to the software mismatch?

### David Grosher, 2024-12-05

@Pat Wells The data uploaded on 11/12/24 was for vehicle 594. That vehicles SW does not appear to be mismatched. We should investigate that incident. The v574 data shows that the SW was old but there is no VTOL data to see if it is mismatched. At the very least ADs were not implemented.

### Pat Wells, 2024-12-05

@Cody Smisek per @David Grosher it looks like you uploaded the wrong aircraft data set - 594 instead of 574.  Do you still possibly have the correct data that you could add.

### David Grosher, 2024-12-05

@Pat Wells @Cody Smisek My fault, they are correct. This issue can be closed.

### David Grosher, 2024-12-05

Out of date SW. Not maintained with recent ADs

### Jason Scherer, 2025-02-11

Moving ticket from cancelled to In Process. An investigation has been requested to support the miss-match firmware report. The investigation was previously not completed due to outdated firmware.

### Jason Scherer, 2025-02-12

Root cause is known landing abort bug triggered by power fault which seems to be caused by bad IMU sensor data on VTOL.

### David Grosher, 2025-02-14

Given that the issue has been fixed in a SW version that is already released, I will be closing this ticket. @Pat Wells @Alexander Alan Arnold  FYSA.

### David Grosher, 2025-02-14

Fixed in v6.3.4

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V574_240819_195535_pack.zip | archive | 1731 | 2024-09-03 | listed only |
| vtol.zip | archive | 16115 | 2024-11-12 | listed only |
| xcomm.zip | archive | 28225 | 2024-11-12 | listed only |
