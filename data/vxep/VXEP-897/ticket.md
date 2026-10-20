# VXEP-897: VXE-674 Auto abort on launch IMU failure message displayed

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-01-13
- **Updated:** 2025-01-21
- **Resolved:** 2025-01-21
- **Reporter:** Pat Wells
- **Assignee:** Cody Smisek
- **Creator:** Pat Wells
- **Labels:** Edge_Asset, Weekly-incident-tracker
- **Links:** relates to VXEP-813 (E140 Octopus/VXE30 Isolation Issues: Arcing to Fuselage, mag interference suspected)
- **Vehicle Tail Number:** 674
- **Vehicle Configuration:** VXE30 Stalker Standard Battery config with E140ZG2
- **Corrective Action:** To be captured in https://jenaero.atlassian.net/browse/VXEP-813
- **Incident Type:** Mission Failure/Abort
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Edge FLOPS asset, issue occured during internal FLOPS training

During launch phase of aircraft 674, we experienced an auto-abort due to an IMU failure. We noticed the message in the VTOL control window. At about 50 feet off the ground, the aircraft started to immediately weathervane into the wind. This could be a potential reason for the "IMU failure." 

AAR attached

## Plan

- @Calvin Rogers  Any previous anomalies? Changes from last flight? 
- Previous AARs for this aircraft would be appreciated.

## Issue Status

Data review complete
Suspected mag interference due to E140 payload (awaiting confirmation on aircraft configuration). 
Data shows attitude mismatch in xcomm logs, AP vs VTOL roll, pitch and yaw all show disagreement during launch, leading to abort.  

Recommend to discontinue E140 flights until mag and ground issues are resolved for the fleet but as an alternative if E140 flights are a must the following can be performed. Place E140 in a common STOW position. Verify cardinal directions for appropriate mag readouts and if required perform fixed wing mag cal per mx manual. For preflight, takeoff and landing, E140 to remain in STOW position. During fixed wing flight, operate gimbal as required.

## Root Cause

Fixed wing magnetometer interference due to E140ZG2 payload caused disagreement between FW and VTOL APs leading to launch abort.

## Comments (3)

### Cameron Chapman, 2025-01-13

@Eric Brewer

### Cody Smisek, 2025-01-13

[embedded: image-20250113-224427.png]

### Cody Smisek, 2025-01-13

[embedded: image-20250113-230009.png]

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V674_250113_122132_pack.zip | archive | 1635 | 2025-01-13 | listed only |
| image-20250113-224427.png | image | 2 | 2025-01-13 | listed only |
| image-20250113-230009.png | image | 102 | 2025-01-13 | listed only |
