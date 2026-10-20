# VXEP-1394: Automatically allow VBN updates in when nav lock is acquired

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-07-09
- **Updated:** 2026-06-09
- **Resolved:** 2026-06-09
- **Reporter:** Levi Purdy
- **Assignee:** Levi Purdy
- **Creator:** Levi Purdy
- **Parent:** VXEP-1248 Apex Wants
- **Epic Link:** VXEP-1248
- **Sprint:** FS2 Sprint 34

## Description

For convivence and to lower the overhead on Flight Ops we want to have the system start using VBN navigation as soon as the system has a good lock. 

Currently the user has to start the flight with Force GPS off set to 0 and then once in the air and with VBN lock set it to 1. We would like this to happen automatically.

VBN data gets streamed to the OEM7 as externalPVAS data, and then the OEM7 integrates that into a kalman filter to provide what looks like GPS information to the VTOL and FWAP system. The system architecture has VTOL checking the uncertainty estimates and then reporting to the FWAP if they are in acceptable margins to use. This happens in the INSPVASDCMP section of gps.cpp.
This is in VTOL gps.cpp 
[embedded image-20250709-203531.png]
This uses GPS_VALID_FLY_FWAP to check that the sigma's are within an acceptable range, and the INS (OEM7) is in a state where it is navigating based on external information. 

The most likely path albeit incomplete is to use the allow_high_variance path to tell the FWAP that the GPS data from VBN is good to use. 

How the allow_high_var state is received on FWAP:
[embedded image-20250709-202004.png]
[embedded image-20250709-202815.png]
A likely path is to have a check in FWAP where if it is in FWAP flight, and allow_high_variance is true for a set amount of time (implying that we probably have VBN lock) then toggle the gain driving ForceGpsOff() to 0. 

A better implementation would be to use this in conjunction with a new state from Craig’s VBN handler app running on the MCM.

## Comments (0)

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20250709-202004.png | image | 82 | 2025-07-09 | listed only |
| image-20250709-202815.png | image | 38 | 2025-07-09 | listed only |
| image-20250709-203531.png | image | 51 | 2025-07-09 | listed only |
