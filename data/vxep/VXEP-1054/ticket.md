# VXEP-1054: VXE 490 going off task after Waypoint 1 on two flights in a row

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-02-27
- **Updated:** 2026-01-26
- **Resolved:** 2026-01-26
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Jason Scherer
- **Creator:** Alexander Alan Arnold
- **Labels:** Edge_Asset, Weekly-incident-tracker
- **Links:** relates to FS2-2854 (Jason's Open Investigations); relates to FS2-3040 (Investigate VXEP-1054 VXE 490 going off task after Waypoint 1 on two flights in a row)
- **Vehicle Configuration:** VXE 30 Main Battery, E140G2 (6288)
- **Incident Type:** Mission Failure/Abort
- **Severity:** 1 - Flight Critical

## Description

EDGE ASSET 
INCIDENT DATE FEB 26 2025
CONFIGURATION VXE 30 Main Battery, Gimbal E140G2 (6288)
On two flights in a row, aircraft 490 went off task from its primary mission, after reaching Waypoint 1. The aircraft was launched with a Waypoint 1 to the East of the launch area, and was commanded to go to an orbit further east. Instead of proceeding to the planned Primary Mission, the aircraft did a 180 degree turn in the opposite direction and ignored the next primary mission element. The site was about 630 feet from a 460 foot tall radio? tower (unsure of its usage), which was directly west of the launch site. On the second flight, the PIC was ready in case the situation occurred again (as the flight before), in which the PIC reported the same behavior. These flights were 2 and 3 of the day, with no issues with the same plane on the first flight. Additionally, the aircraft on its 3rd flight did have aircraft 734’s left wing due to abnormal servo behavior during the 3rd flight’s preflight checklist.

3/3/2025 - Discussion between Cody, Anthony, Brian
Anthony - I was the PIC for the second flight of the day, the first time the aircraft went off task. We were doing a demo for the Border Patrol and had one of their agents physically sitting in the seat. I was walking him through the launch wizard (I built the mission from Brian's first flight, changing a couple things). I was sitting next to him, as if he was a student (same way we teach)
Anthony - I dont recall having the "student" change anything from the point the launch button was hit to the point it went off task after Waypoint 1. I was describing what was happening throughout the vertical climb, start of transition and transition complete. I dont think I have ever in my life ever changed the mission or simulate anything until after it already passes Waypoint 1
Anthony - no problem. As for antenna set up, we had a GCS2 set up on a mast, and it was being relayed through a mobile mount antenna with a GCS1 4200 radio, connected to the laptop. I am not sure if this is important information 
Anthony - the only other odd behavior I noticed is that during that first occurrence flight, the aircraft was no longer recognizing the primary mission when I was moving the plane and updating the mission. The simulation was showing as if I had no primary mission loaded, and was giving simulation warnings for possible lack of endurance. you can probably see this later in the logs around the 40 minute flight mark or later. When I was sync'ing the mission (after making mission changes) the simulation window popped up and there was nothing showing under "mission". It was as if the aircraft did not see the mission for simulation purposes, and was "failing" the simulation check for endurance, even though the main battery level exceeded our mission. The aircraft would physically move as commanded and fly the orbits/racetracks as planned

Sharepoint: VXEP-1054 VXE490 Off Course
Report: Vehicle Investigation VXEP-1054.pptx

## Plan

Look into other ways ‘vt lch wp set’ can occur after launch.  Could be related to the GCS simulation and mission changing during transition.

## Issue Status

‘vt lch wp set’ indicates aircraft was sent to W1 after launch. Absence of ‘changing active waypoint’ in GCS debug indicates the simple method of using GoTo tool may not have occurred and something other initiated the change. 
replicated events (but not the what initiated it) in HIL sim. Was presented with similar debug logs by moving W1 and syncing mission plan. Operators indicate they did not make any changes between launch and when they took over with U-Drive.

## Comments (16)

### Alexander Alan Arnold, 2025-02-27

@Greg Fryer This is from EDGE Flight Ops. They are currently on the road for the next five weeks doing demos and only have three aircraft. Please have someone look at this so we can get them answers. I noticed that 490 also has a total of three open investigations as well I can link them if you think it would be beneficial. 

@Pat Wells FYSA

### David Grosher, 2025-02-27

@Jason Scherer can you put this issue next in the queue above remaining 29 palms incidents.

### Cody Smisek, 2025-02-27

@Alexander Alan Arnold can they provide the mission file they utilized?

### Alexander Alan Arnold, 2025-02-27

The one titled Casey CBP Demo. I believe he saved over the mission from the second flight when launching for the third flight. 
@Cody Smisek @Jason Scherer

### Cody Smisek, 2025-02-27

@Alexander Alan Arnold AARs do not contain the mission files. They are stored locally on the PC.

### Cody Smisek, 2025-02-27

First Flight
[embedded: image-20250228-013803.png]
2nd Flight w/ position of antenna marked as W0 (also contains trail of first flight)
[embedded: image-20250228-014214.png]

### Alexander Alan Arnold, 2025-02-28

Added a .vmis and a .zol to the attachments is that what you need? @Cody Smisek

### Cody Smisek, 2025-02-28

Mission file provided with trail overlay
[embedded: image-20250228-164948.png]
@Alexander Alan Arnold thanks.

### Cody Smisek, 2025-02-28

appears operator commanded a GoTo W1 after launch for both flights. this would result in aircraft navigating to the L waypoint (initial launch location) and not the W1 point. working on creating a few slides to show.

### Cody Smisek, 2025-02-28

@Pat Wells @David Grosher @Alexander Alan Arnold 
I’m working on cleaning up the presentation after conferring with @Jason Scherer on proper report etiquette (probably a Monday thing at this point in the day). Jason said he’ll also corroborate the findings when time permits. Based on replicating what I believe happened, I feel pretty confident in the current conclusion. 
Edit: I noticed that the GCS debug log does not contain the line ‘changing active waypoint’ prior to ‘vt lch wp set’. This seems to indicate that the GoTo tool wasn’t used via the GCS to command W1. I also noticed that for some reason a simulation is being performed during the transition and the mission plan is being modified during this time (for both flights). It might save Engineering a lot of time if the flight ops team could provide any additional information regarding what the user was doing between selecting launch and noticing the aircraft was off mission. 

Current plan: Looking into other ways ‘vt lch wp’ set can occur after launch. 
Possible theory, moving W1 with the move tool might lead to this behavior. Need to test on HIL.

### Cody Smisek, 2025-03-03

@Michael Berger could you assist on this ticket? Sending teams message. 
Trying to figure out what are all the possible options leading to ‘TrackingLayerRepaint’ debug message, and any other ways a simulation can occur without user input.

### Cody Smisek, 2025-03-04

@Alexander Alan Arnold If the aircraft has not been flown since the last of the 3 flights during this incident day, can we ask the team to pull the mission direct from the aircraft?
- power on fuselage
- connect GCS to aircraft
- Select File > Save mission from vehicle
- Name file
- Send file to SLO Eng

### Alexander Alan Arnold, 2025-03-04

I pinged the flight ops team, what are the next steps if they have flown it? @Cody Smisek

### Cody Smisek, 2025-03-04

Next steps would be to completely disregard my message as the flight plan will have been disturbed. @Alexander Alan Arnold 
Right now data shows that GCS performed a mission sim/sync after launch prior to reach W1. Waiting on GCS SW team to provide additional information on how this can occur without user input.

### Cody Smisek, 2025-03-05

Mission was pulled from vehicle, does not match what was previously provided by operators. Unsure why or if it is relevant to the investigation. [embedded: Mission Pulled From Aircraft.vmis] 
[embedded: image (9).png]

### Scott Lovett, 2026-01-26

Operator error.

## Attachments (10)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Mishap Reporting - Aircraft Goes Off Task - Anthony Hansen.docx](attachments/26565_Mishap%20Reporting%20-%20Aircraft%20Goes%20Off%20Task%20-%20Anthony%20Hansen.docx.md) | docx | 53 | 2025-02-27 | converted |
| T95_V490_250226_150719_pack.zip | archive | 3471 | 2025-02-27 | listed only |
| T95_V490_250226_185817_pack.zip | archive | 6614 | 2025-02-27 | listed only |
| image-20250228-013803.png | image | 109 | 2025-02-27 | listed only |
| image-20250228-014214.png | image | 142 | 2025-02-27 | listed only |
| Casey CBP demo.vmis | other | 4 | 2025-02-28 | listed only |
| CurrentOverlay.zol | other | 2 | 2025-02-28 | listed only |
| image-20250228-164948.png | image | 172 | 2025-02-28 | listed only |
| Mission Pulled From Aircraft.vmis | other | 4 | 2025-03-05 | listed only |
| image (9).png | image | 54 | 2025-03-05 | listed only |
