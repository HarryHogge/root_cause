# VXEP-268: Add reasonableness test to total magnetometer magnitude in order to prevent grossly erroneous mag measurements from corrupting heading state.

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-02-07
- **Updated:** 2024-08-23
- **Resolved:** 2024-08-23
- **Reporter:** Eric Brewer
- **Creator:** Eric Brewer
- **Links:** relates to VXEP-263 (VXE-604 crash during SCO/ Flight test)

## Description

During AV604 incident, it was noted that a grossly erroneous magnetic field was used for aiding in the yaw solution.  Rejecting this grossly incorrect magnetometer data could have prevented the incident.

## Comments (0)

## Attachments (0)
