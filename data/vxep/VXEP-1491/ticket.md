# VXEP-1491: VXE-732 having difficulty in maintaining the radius of orbits

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-08-28
- **Updated:** 2026-07-07
- **Resolved:** 2026-07-07
- **Reporter:** Jackson Riley Curvin
- **Assignee:** Jackson Riley Curvin
- **Creator:** Jackson Riley Curvin
- **Labels:** GS_Closed, TIQUILA, Weekly-incident-tracker
- **Customer:** TIQUILA
- **Vehicle Tail Number:** VXE-732
- **Corrective Action:** None
- **Problem Type:** Other (explain in description)
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

During flight testing of the latest version of VCSi and OGCS aircraft 732 was having difficulty in maintaining the radius of orbits. The aircraft passed all launch wizard checks. The issue was first noted during flight in manual mode. Full joystick deflection did not result in the expected tight radius turns, turns were very wide. The aircraft could not maintain a 250 m radius orbit in Route mode nor a 220 m radius orbit in Loiter mode. The landing pattern performance was poor with large radii. Post flight inspection of the ailerons and servos noted no issues. I would have expected this performance in very high winds but the is no evidence to support that. It was noted that the aircraft reported high ground speeds but airspeed plus wind speed did not equal ground speed. Airspeed = 37mph. Wind speed = 6mph. Ground speed = 67mph. Actual wind speed on the ground was <4mph.

## Root Cause

Airspeed calibration was incorrect leading to poor lateral tracking and difficulty maintaining the desired radius of the loiter. Winds would be a complicating factor.

## Comments (14)

### Jackson Riley Curvin, 2025-08-28

[embedded file, not matched to an attachment]

### Jackson Riley Curvin, 2025-08-28

[embedded file, not matched to an attachment]

### Jackson Riley Curvin, 2025-08-28

Awaiting Data

### Jackson Riley Curvin, 2025-08-28

averaged around 75 the entire flight
[embedded: image-20250828-213333.png]

### Jackson Riley Curvin, 2025-08-28

ias averaged above 50 throughout the flight
[embedded: image-20250828-213520.png]

### Jackson Riley Curvin, 2025-08-28

@David Grosher Looks they were operating in high winds which is the reason the aircraft could not handle the orbit radius, but they are saying the actual ground speed was less than 4?

### David Grosher, 2025-08-28

@Jackson Riley Curvin If the ground speed doesn’t average out at the airspeed while doing an orbit then it may be that there airspeed calibration is off. Looking at the airspeed it seems like there is more wind on the ground being picked up after the pitot press.  This could cause some flying quality issues.

### Jackson Riley Curvin, 2025-08-28

@David Grosher would there be a way to tell if their calibration was off?

### David Grosher, 2025-11-05

@Jackson Riley Curvin There appears to be an airspeed calibration issue on this vehicle. 
@Eric Brewer Would this result in poor flying qualities when tracking a loiter?
[embedded: image-20251105-162142.png]

### Eric Brewer, 2025-11-05

@David Grosher yes.  The minimum radius would need to be increased with a ground speed that high.

### David Grosher, 2025-11-05

@Jackson Riley Curvin See Eric’s comment. I think this should close the investigation.

### Jackson Riley Curvin, 2025-11-05

@David Grosher @Eric Brewer so is it a combination of bad airspeed calibration and high winds?

### David Grosher, 2025-12-11

@Jackson Riley Curvin If you have released a report for this issue then I think we can close it. There will be no CAs resulting from this issue. I’ll assign it to you.

### Jackson Riley Curvin, 2026-07-07

Closing due to customer being briefed during weekly meeting.

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 2025-08-27_TIQU-4318_001(DL).zip | archive | 30196 | 2025-08-28 | listed only |
| VXE-732.png | image | 899 | 2025-08-28 | listed only |
| VXE732.png | image | 803 | 2025-08-28 | listed only |
| image-20250828-213333.png | image | 29 | 2025-08-28 | listed only |
| image-20250828-213520.png | image | 27 | 2025-08-28 | listed only |
| image-20251105-162142.png | image | 256 | 2025-11-05 | listed only |
