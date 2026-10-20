# FS2-1758: v523 Investigation Fuel Cell and HLB issue seems to be Faulty Air Speed Data

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-04-18
- **Updated:** 2024-05-30
- **Resolved:** 2024-05-30
- **Reporter:** David Grosher
- **Assignee:** Jason Scherer
- **Creator:** David Grosher
- **Parent:** FS2-1759 Fuel cell and HLB state of charge
- **Links:** relates to VXEP-368 (VXE 523 multiple faults with HLB discharging while in fuel cell configuration); relates to FS2-1759 (Fuel cell and HLB state of charge)
- **Epic Link:** FS2-1759
- **Sprint:** FS2 Sprint 19, FS2 Sprint 18, FS2 Sprint 17

## Comments (8)

### David Grosher, 2024-04-18

@Scott Whitney FYSA

### Jason Scherer, 2024-04-19

Plots from the fuel cell log
[embedded: image-20240419-172935.png]

### Jason Scherer, 2024-04-19

VTOL Log: IBatt and Battery State during flight
[embedded: IBatt_BattState.png]

### Jason Scherer, 2024-04-19

VTOL Log: IBatt1, IBatt2, SysIb, FcIb
Vehicle current consumption appears to almost always exceed fuel cell power output.
[embedded: IBatt1-2_SysIBatt_FCIBatt.png]
Same Plot with Battery State (percentage) added.
[embedded: IBatt1-2_SysIBatt_FCIBatt_BattState.png]

### Jason Scherer, 2024-04-19

3D rendering of flight path:
[embedded: image-20240419-183446.png]

### Pat Wells, 2024-04-19

@Jason Scherer do we have any guidance I can pass along to the operators?  Currently they have ceased flight ops pending some guidance or resolution.

### Jason Scherer, 2024-05-09

@Pat Wells I got pulled into a few other tasks, but my investigation was leading me to believe that the air speed data was reporting lower than actual. I base this on the comparison with ground speed consistently higher, the motor throttle higher, the altitude is reported as commanded, and the vehicle is pitching down more significantly than normal. If the vehicle thinks it’s flying slow it will increase throttle to maintain the commanded altitude. But if it’s flying faster than it thinks, it will need to pitch down to maintain the same altitude.
I will try to put the relevant data into the report today if I don’t get pulled off task again. I don’t know yet why the air speed data is low. My guess is it could be as simple as a bad calibration, but I’m still digging into the code pertaining to how the pitot is calibrated.

### Scott Whitney, 2024-05-30

Marking this task as complete. The investigation notes (comment below) describe it as an air speed data issue not Fuel cell and HLB state of charge

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IBatt1-2_SysIBatt_FCIBatt.png | image | 128 | 2024-04-19 | listed only |
| IBatt1-2_SysIBatt_FCIBatt_BattState.png | image | 148 | 2024-04-19 | listed only |
| IBatt_BattState.png | image | 112 | 2024-04-19 | listed only |
| image-20240419-172935.png | image | 117 | 2024-04-19 | listed only |
| image-20240419-183446.png | image | 76 | 2024-04-19 | listed only |
