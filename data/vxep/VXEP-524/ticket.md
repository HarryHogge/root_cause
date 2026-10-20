# VXEP-524: VXE 444 uncontrolled climbing and descending.  Aircraft unable to descend to VTOL recovery altitude

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-08-05
- **Updated:** 2026-08-14
- **Resolved:** 2024-09-05
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** MARSOC, Training, Weekly-incident-tracker
- **Customer:** MARSOC
- **Vehicle Tail Number:** 444
- **Issue Status:** Closed
- **Root Cause:** Windy/Gusty Environment with thermals that made it difficult for the aircraft to maintain altitude
- **Incident Type:** Other (Record"Event Type: XXXXXX" in the description)
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

From the operator:
I experienced uncontrolled climbing and descending, as well as the aircraft not wanting to come down to recovery alt leading it to start VTOL at around 500ft AGL. It seemed like it thought it was higher in alt than it actually was.
AAR file attached

## Comments (9)

### Greg Fryer, 2024-08-05

@David Grosher just re-assigned this to you since first thing is to look at the AAR.

### David Grosher, 2024-08-08

@Everett Werner Can you start on this investigation.

### Everett Werner, 2024-08-09

Altitude Control:
Altitude appears to be normal/ everything agrees on altitude (AV knows where it is)
Altitude control does look a little bit wonky with some almost 800 foot errors, I will investigate this next.

[embedded image-20240809-201756.png]

Landing:
It exits the downward orbit early and starts its landing.
The message GoTo m,w 1 3 appears in the xcomm logs and that seems to trigger the exit from the downward orbit and the approach on the final landing. This is signifying that the mission is to land at the lz primary and to go to waypoint 3. It appears that the operator commanded a GoTo waypoint 3 and exited the descent.

The image below (will clean up for final report) shows the location of the goto command and the subsequent entry into the landing pattern. The final landing pattern only checks 2d position to confirm that it is close enough for landing and so continued with the landing regardless of the altitude mismatch. This incident looks due to operator impatience, if they had waited for the aircraft to continue its descent it would have entered the landing pattern normally.

[embedded Artifact1.png]

### Pat Wells, 2024-08-14

@Everett Werner any updates, specifically on Altitude Control? 
Operator is currently deployed and hoping for some feedback.

### Everett Werner, 2024-08-15

All sensors appear good, the AV was trying to do everything it could to bleed off altitude (airspeed increase, no throttle, spoiler) but it continued to gain altitude, nothing jumps out as a cause of this behavior. There are signs of significant winds during the flight as well as flying at a high density altitude so my only theory is that it is thermals and a windy/gusty environment contributing to the performance issues,

### Pat Wells, 2024-08-15

@Everett Werner thank you for the update.  I will pass this along to the operator. 
@David Grosher I think we can probably close this out unless you needed to implement a CA?

### David Grosher, 2024-08-15

@Pat Wells That is fine with me. It doesn’t look like it would be required. Do you need a report?

### Everett Werner, 2024-08-15

@Pat Wells If you want it formatted with axis labels and such I am able to provide that.

### Eric Brewer, 2025-03-03

@David Grosher report completed here.  VXEP524.pptx
FYI @Everett Werner @Pat Wells

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V444_240804_042445_pack.zip | archive | 2687 | 2024-08-05 | listed only |
| Artifact1.png | image | 125 | 2024-08-09 | listed only |
| image-20240809-201756.png | image | 58 | 2024-08-09 | listed only |
