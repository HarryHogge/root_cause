# VXEP-1290: VXE 528 aborted launch after 10 feet

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-05-16
- **Updated:** 2026-08-21
- **Resolved:** 2026-08-11
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Josh Burrell
- **Creator:** Alexander Alan Arnold
- **Labels:** GS_Closed, Software, USASOC, Weekly-incident-tracker
- **Links:** relates to VXEP-1982 (VXE 897Failure to launch same error each time)
- **Customer:** USASOC
- **Vehicle Tail Number:** VXE 528
- **Vehicle Configuration:** VXE 30, standard, no gimbal
- **Incident Type:** Mission Failure/Abort
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

During the VTOL sequence aircraft aborted launch.

Workaround: This should not ground the aircraft, but it is a very time-consuming issue for operations to have to deal with, namely after going to through preflight and launching, only to have the vehicle land immediately.  The workaround used in OGCS is to specify a slightly lower launch altitude, perhaps 5 to 10% lower, such that the margin in the AP will accommodate the requested (and adjusted) altitude.  The recommended workaround for the Jennings GCS is the same.

## Corrective Action

AN to document workaround, first decrease transition out altitude then second the workaround outlined by Craig in the comments below. (Probably need more details from Craig) @Josh Burrell

## Issue Status

- Write RCR for customer.
- Determine corrective actions to ensure the work around is not required and that the vertical operation does not surpass the height plus the safety factor when transitioning.

## Root Cause

he Jennings GCS was loaded with factory DTED and the launch altitude was specified as 300 ft exactly.  This issue appears to have the same symptoms as the but in MCM, namely a slightly negative reported AGL on the ground is additive to the launch altitude goal, which exceeds the climb limit + margin in the autopilot.  In this case, the reported altitude was -1 to -5 feet:
 
[embedded: slightly-negative-agl (51204c15-c816-420b-9b18-60c3600cc775).png]

## Comments (12)

### David Grosher, 2025-05-19

[21:27:10.273 1737.273] alt request too high, RTL 333
[21:27:10.274 1737.275] DebugMsg Altitude request too high, launch aborted
[embedded: image-20250519-153340.png]
@Alexander Alan Arnold This was observed during the OGCS development, you may want to talk with @Craig Burton.  I believe it had to do with the initial altitude calibration and slight errors with the DTED data. The threshold was 331 feet but the request was for 333.

### Alexander Alan Arnold, 2025-05-19

@David Grosher I will talk with him. We really are making sure that there is nothing grounding this aircraft so we can continue training. I haven't seen anything that I think would keep it grounded I just wanted a second opinion.

### Craig Burton, 2025-05-19

Alexander and I communicated via email.  The Jennings GCS was loaded with factory DTED and the launch altitude was specified as 300 ft exactly.  This issue appears to have the same symptoms as the but in MCM, namely a slightly negative reported AGL on the ground is additive to the launch altitude goal, which exceeds the climb limit + margin in the autopilot.  In this case, the reported altitude was -1 to -5 feet:

[embedded: slightly-negative-agl.png]
This should not ground the aircraft, but it is a very time-consuming issue for operations to have to deal with, namely after going to through preflight and launching, only to have the vehicle land immediately.  The workaround used in OGCS is to specify a slightly lower launch altitude, perhaps 5 to 10% lower, such that the margin in the AP will accommodate the requested (and adjusted) altitude.  The recommended workaround for the Jennings GCS is the same.
@Ted Trowbridge FYSA, I believe that this is the first time I’ve observed this with the Jennings GCS.

### Josh Burrell, 2026-01-20

@Alexander Alan Arnold @David Grosher @Craig Burton I don’t believe “work arounds” are things we want to put into the manual. In this case an Advisory Notice (AN) would be the proper way to handle this until the problem is properly corrected.
@Mark Spence @Drew Cunnien @William Doupis

### David Grosher, 2026-01-20

@Josh Burrell Agree that an AN is more appropriate.

### David Grosher, 2026-01-20

@Craig Burton @Ted Trowbridge Is there a structural fix to this issue that could be implemented? Does changing the default transition altitude reduce the impact of this bug?

### Ted Trowbridge, 2026-01-20

@David Grosher Yes, changing the default transition altitude significantly reduces the likelihood this will occur (potentially completely eliminating).  When you’re right up against the limit there is a small chance of this happening based on the vehicle being at a “negative” AGL altitude during launch.
I think the issue is completely eliminated once (maximumAlt - transitionAlt) is greater than whatever altitude would trigger a POS_MATCH error, but that would need to be confirmed.

### Pat Wells, 2026-08-11

@Josh Burrell are we still planning to release an AN for this?
@Alexander Alan Arnold FYSA

### Alexander Alan Arnold, 2026-08-11

@Ted Trowbridge @David Grosher @Craig Burton Is this still a relevant bug/issue or has it been addressed in recent releases?

### Ted Trowbridge, 2026-08-11

@Alexander Alan Arnold No change has been made to Jennings GCS, I believe the issue could still occur but is unlikely.
OGCS has a default launch altitude of 200ft and maximum launch altitude of 300feet, so in theory it could happen but only if the vehicle is reporting -31ft AGL or more at the beginning of takeoff and the operator overrides to use the maximum value of 300.

### Josh Burrell, 2026-08-11

@Pat Wells after talking to @Ted Trowbridge he felt like this was such a rare occurrence that it shouldn’t warrant an AN.

### Pat Wells, 2026-08-11

Decision made not to release an AN based on software updates that have occured since this was reported along with low likelyhood of occurance.

## Attachments (11)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 16MAY25 Flight mission issue.vmis | other | 4 | 2025-05-16 | listed only |
| Launch Abort 528 Snip 16MAY25.PNG | image | 2174 | 2025-05-16 | listed only |
| T95_V528_250516_142707_pack.zip | archive | 1260 | 2025-05-16 | listed only |
| 528 VTOL task timing.png | image | 51 | 2025-05-17 | listed only |
| Screenshot 2025-05-16 180831.png | image | 61 | 2025-05-17 | listed only |
| Screenshot 2025-05-17 173628.png | image | 51 | 2025-05-17 | listed only |
| Screenshot 2025-05-17 174054.png | image | 102 | 2025-05-17 | listed only |
| IMG_7949.mov | video | 47248 | 2025-05-19 | listed only |
| image-20250519-153340.png | image | 39 | 2025-05-19 | listed only |
| slightly-negative-agl.png | image | 149 | 2025-05-19 | listed only |
| slightly-negative-agl (51204c15-c816-420b-9b18-60c3600cc775).png | image | 149 | 2025-08-15 | listed only |
