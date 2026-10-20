# VXEP-1776: VXE-641 Uncontrolled Landing Incident (Crash)

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2026-03-17
- **Updated:** 2026-05-20
- **Resolved:** 2026-05-05
- **Reporter:** Michael Mohr
- **Assignee:** Eric Brewer
- **Creator:** Michael Mohr
- **Labels:** RCCA, TIQUILA, Weekly-incident-tracker
- **Links:** relates to RMA-946 (VXE-641 RMA 260318-1)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** VXE-641
- **Problem Type:** Discovered Issue
- **Issue Status:** Investigation Presentation.
- **Incident Type:** Aircraft Loss
- **Severity:** 1 - Flight Critical
- **Components (EA Aircraft):** Aircraft, full assembly

## Description

Operator statement:
At 16:30, the detachment deployed. The mission was planned with a maximum operating height of 800ft AGL. The detachment was fully briefed, and all personnel were alert, well-rested. The aircraft, EAGLE VXE30 tail number 641, launched successfully and entered its designated orbit. At the time of the incident, the aircraft had been in flight for 1 hour and 7 minutes, with 2 hours and 30 minutes endurance remaining to complete the task. Weather conditions were within operational limits, with a steady wind speed of 22.2 knots from 118° SE, below the maximum allowable limit of 26 knots. The temperature was recorded at 21°C. 
At 19:02, while the aircraft was in its orbit at 800ft AGL, it was observed to bank excessively to the left. The aircraft then looked as if it rolled over, and it appeared to lose stability. The payload footage showed the aircraft rolling over completely, with the camera momentarily pointing upwards towards the sky. The footage then displayed the aircraft continuing to roll multiple times, indicating a loss of controlled flight. Simultaneously, the Ground Control Station (GCS) populated a GPS warning, which cleared after a few seconds. The pilot immediately issued a positive command to return the aircraft to its current orbit in an attempt to stabilize it. However, this action was unsuccessful, and the aircraft continued to lose altitude. Shortly after, the GCS displayed a red "loss of link" warning, indicating that communication with the aircraft had been lost. The detachment continued to monitor the situation closely. At approximately 300ft AGL, all telemetry and video feed from the aircraft had paused, and the detachment were unable to regain control. The aircrafts last known position was recorded, and the incident was promptly reported through the appropriate channels, including the chain of command and relevant authorities. 
Following the loss of the aircraft, the detachment initiated a search and recovery operation. The team proceeded to the aircrafts last known position and located the aircraft. Upon arrival, the team documented the scene by taking photographs of the aircraft and its surroundings. The area was immediately cordoned off to ensure safety, preserve evidence, and prevent unauthorized access. The detachment then moved back 400m from the site to maintain a safe distance while awaiting further instructions. 
Damage/Injuries: The aircraft sustained significant damage, classified as Category 5 (CAT 5).No injuries to personnel were reported.
Weather Conditions: Wind: 22.2 knots from 118° SE.Temperature: 21°C.
Immediate Actions Taken:
A positive command was given straight away to the aircraft when it started to lose stability. The detachment recorded the aircrafts last known position and reported the incident through the appropriate channels. A search and recovery operation was initiated to locate the aircraft. Upon locating the aircraft, the detachment documented the scene with photographs and cordoned off the area to ensure safety and preserve evidence.
Date of Occurrence: 15/03/2026
Time of Occurrence: 19:02
Aircraft Type and Tail Number: EAGLE VXE30-641
GCS Number: SCGS1-218
Flight Phase: During flight whilst in Orbit
Aircraft height during incident: 800ft AGL
Time remaining in current orbit: 11 minutes
Weather Conditions: Clear, winds speed 22.2 Kts, wind direction 118 SE, temp 21 Degrees Celsius.

## Vehicle Configuration

Standard VXE30
Battery

## Corrective Action

None.  This was a failure of a flight critical sensor that is a single point of failure in the current system.
The FWAP IMU is going obsolete with advanced nav becoming default for B30 and 40.

## Plan

- Aircraft returned 3/31. @Madeleine Masiello please inspect the FWAP gyro and other components for damage.
- If none observed, see if/what seems safe to power up to test gyro operation.

## Root Cause

FWAP Gyro Bias caused AHRS to report an inaccurate roll.  That in turn caused the vehicle to depart controlled flight and crash.

## Comments (25)

### Eric Brewer, 2026-03-20

@Drew Hildreth yes to me looks like a gyro failure.  @David Grosher FYI.

### Eric Brewer, 2026-03-20

@Drew Hildreth at @David Grosher's request I ran a quick test just to prove that for reasonable gyro bias changes the estimation will work - but the behavior in the logs seems indicative of a step change in the gyro measurement (i.e. gyro failure).  

The first test I increase the gyro measurement by 5.7 deg/s (0.1 rad/s), and the ahrs estimate changes but eventually converges out the bias.  On the second test I decrease the gyro bias by 20 deg/s (the amount of discrepancy we saw between fw and vtol gyro measurements) and the ahrs goes unstable as we saw in flight.

Recording of the test attached above.

### Drew Hildreth, 2026-03-23

@Eric Brewer @David Grosher Good morning, Dhruti just called again about this. She is stating they are looking at Grounding the TIQUILA Fleet now.

Based on the above, what can I relay to her? 

She wants to know if this is a Tail issue or a Fleet issue as well. Alex and I told her already this morning that it seems to be a tail only.

### David Grosher, 2026-03-23

@Drew Hildreth It is a tail issue.

### Ryan Smith, 2026-03-31

AAR pulled with Matt on 2026-03-31 with an FDR retrieval error aar plus the manually downloaded xcomm logs.

[embedded file] [embedded file]

### Eric Brewer, 2026-04-01

@Ryan Smith thanks.  The roll rate and roll rate bias appear within normal limits (roll rate bias < 1 deg/s).  Pitch rate bias is just under 2 deg/s which is a little larger than typical but not out of what would be considered flyable.  Whatever happened to the gyro looks like something transient during the flight.  Note it is not atypical that a gyro might read normal in a lab setting despite having an issue in flight.


[embedded image-20260401-203915.png]

### Matthew Aguirre, 2026-04-01

Performed a couple tests today to get an understanding of how the IMU functions. While doing so, noticed some interesting readings and made note of them in this test document. Attached are the datalogs. 
Main findings:
- Focused on testing roll and yaw readings based off flight data from the crash. As those two plots seemed to be the most deviated or abnormal.
- Roll readings (roll rate and roll value) both seemed to perform accurately.
- Yaw readings, on the other hand, seemed to behave abnormally.
- In the motionless tests, there was a steady increase in the yaw value of about ~0.073°/s (worst case). Over 5 minute time span, there was a deviation of +22° deviation in yaw axis.


@Eric Brewer not too sure if the deviation in the yaw axis is normal behavior, would like to confirm to continue investigation. Any ideas or tips on how to proceed would be greatly appreciated!
[embedded file]

### Matthew Aguirre, 2026-04-03

@Matthew Aguirre @David Grosher Just seen that Eric left yesterday on PTO for about a week. Who would be the next POC after Eric to assign the investigation and direct my questions to?

### Drew Hildreth, 2026-04-14

@Eric Brewer where are you on this one? Do you need anything from us?

### Eric Brewer, 2026-04-14

@Drew Hildreth thanks for reaching out.  Unfortunately based upon what I’m seeing the IMU is performing normally in lab testing.  We have seen this before in other IMU failure incidents - we will get some bad readings from the gyro in flight and then it tests normally in the lab.  

Just FYI @Matthew Aguirre heading drift in the absence of magnetometer readings is normal.  You don’t see drift in pitch and roll because the unit can measure gravity to keep the errors on pitch and roll bounded.

### Drew Hildreth, 2026-04-14

@Eric Brewer well that makes it super easy to run down what is really going on… you can insert sarcasm anywhere in there…

### Matthew Aguirre, 2026-04-14

@Eric Brewer Thanks for breaking that down for me. Took me a while to get a basic understanding of how the IMU functions. Not sure if I’m needed for anything else at this point, but if there’s any other tests you recommend me doing or if there’s somewhere I could support, just let me know and I’d more than happy to help out!

### Eric Brewer, 2026-04-21

@Drew Hildreth do you need anything else from me on this one?

### Eric Brewer, 2026-04-27

@Drew Hildreth @David Grosher report is up here.  Let me know if you have questions or want anything additional.  

https://jenaero.sharepoint.com/:p:/r/sites/FlightSafety/_layouts/15/Doc.aspx?sourcedoc=%7B0C093AE8-3307-4BDD-8CA8-8D51281597CB%7D&file=V641Investigation.pptx&action=edit&mobileredirect=true

### Drew Hildreth, 2026-04-27

@Eric Brewer This is great! Thank you!

### Eric Brewer, 2026-05-05

@Drew Hildreth are we good to close this one out?

### Drew Hildreth, 2026-05-05

@Eric Brewer I am good with it to be closed.

### Eric Brewer, 2026-05-05

Root cause found to be FWAP gyro failure.

### Cameron Chapman, 2026-05-20

@Eric Brewer should this investigation be closed? We know it failed due to the FWAP gyro, but we don’t know why it failed.
- Should we keep investigating, or list that the FWAP IMU is going obsolete with advanced nav becoming default, often fails, and is not priority to investigation?
- We could list in CA that  FWAP IMU is going obsolete with advanced nav becoming default.

### Eric Brewer, 2026-05-20

@Cameron Chapman I think it should be closed.  These do not fail often, and it is one of many single points of failure in the system. If we get in a bunch more of a similar failure mode we can look into it but for now I vote we close the investigation.

### Eric Brewer, 2026-05-05

@Drew Hildreth are we good to close this one out?

### Drew Hildreth, 2026-05-05

@Eric Brewer I am good with it to be closed.

### Eric Brewer, 2026-05-05

Root cause found to be FWAP gyro failure.

### Cameron Chapman, 2026-05-20

@Eric Brewer should this investigation be closed? We know it failed due to the FWAP gyro, but we don’t know why it failed.
- Should we keep investigating, or list that the FWAP IMU is going obsolete with advanced nav becoming default, often fails, and is not priority to investigation?
- We could list in CA that  FWAP IMU is going obsolete with advanced nav becoming default.

### Eric Brewer, 2026-05-20

@Cameron Chapman I think it should be closed.  These do not fail often, and it is one of many single points of failure in the system. If we get in a bunch more of a similar failure mode we can look into it but for now I vote we close the investigation.

## Attachments (18)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IMG-20260316-WA0001.jpg | image | 161 | 2026-03-17 | listed only |
| IMG-20260316-WA0002.jpg | image | 167 | 2026-03-17 | listed only |
| IMG-20260316-WA0003.jpg | image | 174 | 2026-03-17 | listed only |
| IMG-20260316-WA0004.jpg | image | 168 | 2026-03-17 | listed only |
| IMG-20260316-WA0005.jpg | image | 201 | 2026-03-17 | listed only |
| IMG-20260316-WA0006.jpg | image | 202 | 2026-03-17 | listed only |
| IMG-20260316-WA0007.jpg | image | 295 | 2026-03-17 | listed only |
| IMG-20260316-WA0008.jpg | image | 271 | 2026-03-17 | listed only |
| IMG-20260316-WA0009.jpg | image | 317 | 2026-03-17 | listed only |
| MicrosoftTeams-video (1).mp4 | video | 2244 | 2026-03-17 | listed only |
| T95_V641_260317_090239_pack.zip | archive | 6831 | 2026-03-18 | listed only |
| image-20260318-161533.png | image | 386 | 2026-03-18 | listed only |
| Recording 2026-03-20 083029.mp4 | video | 95569 | 2026-03-20 | listed only |
| T95_V641_260331_151321_02_pack_failed_getfdr.zip | archive | 581 | 2026-03-31 | listed only |
| xcomm_files_v641_03_31_2026.zip | archive | 2310 | 2026-03-31 | listed only |
| TestReport4-1-26.zip | archive | 2705 | 2026-04-01 | listed only |
| image-20260401-203915.png | image | 34 | 2026-04-01 | listed only |
| [VXEP-1776_VXE-641_Vehicle Investigation_20260511.pptx](attachments/56413_VXEP-1776_VXE-641_Vehicle%20Investigation_20260511.pptx.md) | pptx | 829 | 2026-05-12 | converted |
