# VXEP-160: VXE-501 drift on landing

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-10-30
- **Updated:** 2026-09-14
- **Resolved:** 2025-06-02
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** No_crash, PMA263, Training
- **Links:** relates to RMA-183 (VXE-501  231027-7  Drift Incident); relates to FS2-1156 (v501 Landing drift vehicle investigation); relates to FS2-1392 (Evaluate MC FW helper control loops.)
- **Customer:** PMA263
- **Problem Type:** Other (explain in description)
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Customer states:

Aircraft displayed uncontrolled drift on landing.
FDR attached.
Please expedite data analysis if possible.  Pat Wells will be on site with customer this week.

## Corrective Action

The short term recommended courses of action:
- Avoid takeoff and landing in winds > 17 kt
- Determine guidelines for landing procedures in high winds if landing in high winds is unavoidable. 
- Update documentation
- Update training

In the longer term, we will evaluate our control algorithms to better handle high winds during VTOL flight.  https://jenaero.atlassian.net/browse/FS2-1392

## Plan

@David Grosher to review C/CA and link to CAs issues in CA field. Need to add ppt link back to description. 
FYI @Ben Triplett

## Issue Status

See powerpoint for more details: V501 Vehicle Investigation December 2023.pptx
The behavior of the AV is better described as an excursion rather than drift. On the map it looks like a drift but closer inspection shows that the air vehicle turns 90 degrees to the right and then flies in typical fixed wing fashion to a position about 150 meters from the target landing spot.  The following video is clearer if downloaded to your local computer. 
[embedded: vxe30smooth.mp4]

The FW helper aileron to roll control loop is inverted. Insufficient information available to determine whether or not this is intentional. This is a cascaded loop in which a roll rate setpoint is computed from the roll angle error, and then the aileron response is proportional to the subsequent roll rate error. See lines 401 to 438 in McFwHelper.c. 
The FW helper roll control was not inverted during the excursion. On second look, the right wing appears to have stalled leading to the hard roll to the right. The evidence for this is the high windspeed at low groundspeed, greater than 20kt, combined with greater than 10 degree pitch angle leading to the main wing carrying most of the weight of the AV. In this situation, the VTOL control spools down near zero. A small roll to the right increases the relative AoA of the right wing compared to the left wing, and the response to this which is to move the right aileron down. This downward deflection of the right aileron increases its camber which shifts the stall angle of the wing in that section down. All together, this puts the AV in a situation in which one wing will stall before the other, and was in conditions in which stall was likely. 
The following figure shows pitch angle and estimated AoA of the vehicle, as well as the AoA at each wingtip (difference due to rollrate):
[embedded: image-20240125-000050.png]

## Root Cause

The root cause of the excursion is complex. The AV has found itself in a situation in which most of the weight of the AV is carried by the main wing due to an apparently high AoA and high airspeed due to high prevailing winds, over 20kt estimated. At the time of the excursion, the AV had little control authority from the rotors, and some control authority, in roll, from the ailerons. The current hypothesis is that the right wing experienced stall due to flow separation from high relative angle of attack higher camber than the left wing, resulting in significant unintended roll right, leading to the AV to turn right, lose relative airspeed, descend and fly off away from the target landing point.

## Comments (8)

### David Grosher, 2023-10-30

@Jason Scherer  can you take a quick look at this to see if it is the same issue as v401.  Thanks

### Jason Scherer, 2023-10-30

@David Grosher I don’t see the same behavior in this flight. This landing was in position hold mode until it landed.
[embedded: image-20231030-183257.png]

### Pat Wells, 2023-11-01

@David Grosher @Jason Scherer 
I’ve added a video of the GCS screen during the incident that was provided by the customer.

### Cameron Chapman, 2023-11-01

@Pat Wells I don’t see a video. Is the video for the 501 incident or the 401 one? Please upload if this one. Unlikely to resolve while on site this week. 499 seems higher priority for FW team.

### Pat Wells, 2023-11-01

@Cameron Chapman  Looks like it didn’t attach earlier. Should be there now. It’s from 501 incident.

### Cameron Chapman, 2023-11-01

Thanks @Pat Wells helpful narration of the after action GCS track. Were there any high winds or other severe conditions?

### Pat Wells, 2023-11-01

@Cameron Chapman no severe weather conditions noted.  I spoke to the operator in person today at Camp Lejeune.

### Cameron Chapman, 2024-01-30

@David Grosher to review C/CA and link to CAs issues in CA field. 
FYI @Ben Triplett

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| FDR- VXE-501 Drift 10-30-23.zip | archive | 4118 | 2023-10-30 | listed only |
| image-20231030-183257.png | image | 206 | 2023-10-30 | listed only |
| 71700832893__C433B783-78C9-4C36-B651-63986B608C6C.MOV | video | 18583 | 2023-11-01 | listed only |
| vxe30smooth.mp4 | video | 46521 | 2023-12-11 | listed only |
| image-20240125-000050.png | image | 295 | 2024-01-24 | listed only |
