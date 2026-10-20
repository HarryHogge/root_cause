# VXEP-1220: VXE 674 PLZ 50 m away

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-04-21
- **Updated:** 2025-09-16
- **Resolved:** 2025-09-16
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Alexander Alan Arnold
- **Creator:** Alexander Alan Arnold
- **Labels:** Edge_Asset, Weekly-incident-tracker
- **Links:** relates to RMA-682 (VXE-674 250502-1)
- **Part Number(s):** VXE 674
- **Vehicle Tail Number:** 674
- **Vehicle Configuration:** VXE 30 Fuel Cell
- **Corrective Action:** Retrain Operator, review published Operator Manuals
- **Plan:** @Alexander Alan Arnold will generate report based on findings
- **Root Cause:** System behaved as expected, operator error
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

PLZ 50 m away from takeoff location, AV not responding to pause/nudge commands
Operator statement
Both Hadley and the 1st Cav operator are saying at some point the PLZ and Orbit 2 changed to a different location, I think this was preventable and they paused too late before it hit a tree branch. Hadley was with the ground crew, Anthony was with the operator.

674(SOFC) had PLZ 50 m from takeoff location. Not sure if it inadvertently moved, the operator set it wrong, or erroneously moved it. following pause, our team gave the 1st cav operator nudge commands. Not sure if aircraft did not respond or operator error on the nudging. Anthony was calling commands to the operator and couldn't see if he was making them correctly.

## Comments (27)

### Alexander Alan Arnold, 2025-04-21

We are adding data and will update description as more information comes in. @Greg Fryer This just happened at a demo.

### David Grosher, 2025-04-21

@Ted Trowbridge Can you look into this incident?

### Alexander Alan Arnold, 2025-04-21

@Ted Trowbridge Added mission file

### Alexander Alan Arnold, 2025-04-22

attached mishap form with operator statement @Ted Trowbridge @David Grosher

### Ted Trowbridge, 2025-04-22

@Alexander Alan Arnold @David Grosher 
- VTOL logs indicate the vehicle was never nudged, but it was paused.
- GCS logs indicate the joystick left stick was moved twice to the right to command a nudge, but that was not received by the aircraft.

I’m continuing to investigate why the nudge commands were not sent as well as why the PLZ was moved.
Questions:
- What joystick was being used?
- Was the land override dialog activated and was it indicating “Position Nudge” mode was active?

### Alexander Alan Arnold, 2025-04-22

- What joystick was being used? Do you mean what type of controller was being used or left joystick vs right joystick?
- Was the land override dialog activated and was it indicating “Position Nudge” mode was active?- I am asking the operators about this. @Ted Trowbridge

### Ted Trowbridge, 2025-04-22

@Alexander Alan Arnold yes, what type of controller was being used and how many controllers were plugged in.

### Jackson Riley Curvin, 2025-04-22

@Ted Trowbridge according to the logs it was an Xbox controller but we will double check
[embedded: image-20250422-205859.png]

### Ted Trowbridge, 2025-04-22

@Jackson Riley Curvin According to the GCS logs there were possibly 3 different controllers connected, one of which was the XBOX controller
```
Time: 005:30.312  INFO: Xbox controller with device ID 'VID_1532&PID_0A29' disconnected.
Time: 005:31.297  WARNING: Xbox controller with device ID 'VID_046D&PID_C077' not found in approved list.
Time: 005:31.297  INFO: HID-compliant game controller with device ID 'VID_046D&PID_C077' disconnected.
Time: 009:52.687  WARNING: Xbox controller with device ID 'VID_05E3&PID_0749' not found in approved list.
Time: 009:52.687  WARNING: HID-compliant game controller with device ID 'VID_05E3&PID_0749' connected.
Time: 009:54.953  WARNING: Xbox controller with device ID 'VID_046D&PID_C077' not found in approved list.
Time: 009:54.953  WARNING: HID-compliant game controller with device ID 'VID_046D&PID_C077' connected.
Time: 009:58.359  INFO: Xbox controller with device ID 'VID_1532&PID_0A29' connected.
```

### Jackson Riley Curvin, 2025-04-22

@Ted Trowbridge this is the last message about a controller being atttached
[embedded: image-20250422-211533.png]

### Alexander Alan Arnold, 2025-04-22

From Anthony (on site instructor)

The User Landing Control Override panel was open. At first, he was attempting to click the options in the panel and not using the controller. To be fair, I wasn’t watching him as he was clicking in the panel to see if he was indeed clicking nudge right. I turned around to look at the plane and it didnt look like the aircraft was moving right. 

It was the aftermarket Xbox one style controller. the laptop was hooked into a couple network switches and running off the Max’s SGCS1 radio. There was only one controller plugged in and one mouse. 

-Anthony 
@Ted Trowbridge

### Ruysser Gabler, 2025-04-23

To add on the panel nudging. If the user was “clicking” it would very likely not move very far at all. 
As “clicking” is on/off/on/off, the user has to click and hold to get it to continue moving. Also the manel nudge does not allow for much movement in general compared to the Xbox controller. The controller is fine tunable and has larger available inputs compared to the screen. 
Example: screen right is “bank 3 deg” where the Xbox full stick is “bank 8 deg”.
While in position mode it is not a “bank” command it is rather a move x amount this direction it is the same jist of the screen is less capable. 

@Alexander Alan Arnold @Ted Trowbridge

### Ted Trowbridge, 2025-04-23

@Ruysser Gabler Thanks for that info.  I agree, but ultimately the VTOL logs show no nudges were ever received.  I see some evidence of position nudge being turned on, but both directions are 0 for all of the available logs.

### Ruysser Gabler, 2025-04-23

@Ted Trowbridge They likely missed the button on screen then if they were indeed clicking and it was open.

### Jackson Riley Curvin, 2025-04-23

@Ted Trowbridge  for the FSR’s SA and to help with further investigations what would a nudge command look like in the VTOL log?

### Ted Trowbridge, 2025-04-23

@Jackson Riley Curvin looking back over the logs I actually am seeing some nudges.  Let me take a look at this again and I’ll provide updates and where to look to find this in the logs as another update today.

### Ted Trowbridge, 2025-04-23

@Alexander Alan Arnold @David Grosher 
Updates after another dive into the VTOL logs.  I was mistaken in saying no nudges were commanded… here is a corrected analysis of what happened:
- Operator clicked nudge RIGHT a single time via the user interface.
- Operator began pausing and logs indicated they nudged LEFT and FORWARD at this time.
- Vehicle impacted tree branch

[embedded: image-20250423-202437.png]
This is consistent with written description of events from Hadley:
At approximately 50 feet, I commanded “Pause and Nudge”.  The aircraft did not pause until it was practically in the trees, approximately 25 feet AGL, it did not appear to take any nudging commands.  When it finally did pause, it shifted a couple of feet to the left and collided with the branch of the tree.  It then rolled out of the tree and impacted the ground.

The VTOL logs show nudge commands in the columns labeled:
- ovrMode The Nudge mode
- 1101 = Position Nudge
- 1102 = Attitude (Manual Nudge)
- 0 = Timed Out or Inactive
- ovrX The longitudinal (forward/back) nudge in the range [-1, 1]
- ovrY The lateral (left/right) nudge in the range [-1, 1]

### Alexander Alan Arnold, 2025-04-23

Based on this is it safe to assume that the operator potentially paused too late in the descent and the commands they input via the stick pushed the aircraft into the trees instead of away from the trees? @Ted Trowbridge

### Ted Trowbridge, 2025-04-23

@Alexander Alan Arnold Yes - that would be my conclusion.

### Alexander Alan Arnold, 2025-04-23

@Ted Trowbridge So part 2 for us will be to determine if the SW moved the PLZ or if it was moved by an operator by mistake because I believe that is one of the claims in the mishap statement. Any chance you can recommend which logs to or files to look into to see that? @Jackson Riley Curvin

### Ted Trowbridge, 2025-04-23

@Alexander Alan Arnold
- Did the operator click ‘Use Vehicle Location’ when creating the Primary LZ?  If so, the vehicle may have had inaccurate GPS if it had just been booted up or there was signal interference (trees, buildings).  EIther way, it would have been visually obvious on the map display that the LZ was near the trees.
- The GCS does not change the LZ position unless the operator moved it manually.  Furthermore, the change would need to run through mission simulation and a mission sync to be pushed to the aircraft.

The only reasonable explanation right now is operator error in moving or incorrectly placing the LZ.

### Alexander Alan Arnold, 2025-04-24

@Ted Trowbridge The only reasonable explanation right now is operator error in moving or incorrectly placing the LZ. 
We are in agreement on that, I Just wanted to verify that there was no chance the there was an error on the VXE/GCS side of the house. I am not aware of any reported issues where the GCS moves the PLZ. Are you? 
I believe there was a SIM ran right before the RTB command. 
This is the part of the mishap report I am referencing. 
 During Pre Mission flight checks while on I was on the phone with my Ground Crew they
reminded me to geographically sync vehicle position with launch and landing point which I did. During
flight I had to move my orbit out to the west which I did. I then commanded RTB and when it did the
orbit went back to its original position when it wasn’t commanded too. The aircraft then began landing
VTOL over the treeline which it crashed into. Anthony who was with me had comms with Hadley and
SGT white who were my landing ground crew they instructed me to pause position and nudge right
which I did , but it was too late.

I am inclined to believe that during the “Orbit change” in the statement above is potentially where the operator error is. He claims he moved the orbit but there is no mention of simulation and sync of the updated mission. But since they are claiming it was an error in the software, I figured it was worth an ask.

### Ted Trowbridge, 2025-04-24

@Alexander Alan Arnold I agree with your assessment that the ‘orbit change’ is potentially where the operator error occurred.
During Pre Mission flight checks while on I was on the phone with my Ground Crew they
reminded me to geographically sync vehicle position with launch and landing point which I did.

This seems to me like the operator placed the LZ at the reported vehicle position.  It could be that GPS was not accurate and the position was reporting over the trees instead of the intended safe LZ position.
I am not aware of any way the GCS will automatically move the LZ without operator interaction.  I ran the question by FLOPs and they agreed it’s not possible.

### Alexander Alan Arnold, 2025-04-24

@Jason Scherer When you get a chance are you able to confirm the suspicion that there was not a sync command sent to the AV after the SIM was ran right before RTB? I would like this to further the Root Cause into the Operator error thought process we currently have going. It would explain the operator Statement that the AV went to the “old” orbit even though he changed it.

### Drew Hildreth, 2025-05-01

@Jason Scherer @Ted Trowbridge have you had a chance to take a look at what Alex wrote below? The FLOPS team has returned from AEWE and we are getting ready to send this aircraft to SLO.

### Alexander Alan Arnold, 2025-05-05

Revisiting the Operator statement there is mention that it overshot the PLZ? Is there any evidence to support this claim or what logs would I need to look at into this? @Ted Trowbridge

### David Grosher, 2025-08-15

@Alexander Alan Arnold I don’t think there is anything else to investigate here. It seems to me that if the PLZ was nudged away that the operator statement that it was overshot is not factually correct. At this point there is no corrective action identified then this ticket should probably proceed to closure.

## Attachments (12)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Image (26).jpg | image | 2155 | 2025-04-21 | listed only |
| Image (27).jpg | image | 2039 | 2025-04-21 | listed only |
| Image (28).jpg | image | 1415 | 2025-04-21 | listed only |
| Image (29).jpg | image | 1729 | 2025-04-21 | listed only |
| Image (30).jpg | image | 2155 | 2025-04-21 | listed only |
| T95_V674_250421_110556_01_pack.zip | archive | 3765 | 2025-04-21 | listed only |
| T95_V674_250421_110556_pack.zip | archive | 3765 | 2025-04-21 | listed only |
| aewe02.vmis | other | 4 | 2025-04-21 | listed only |
| [4-21 Mishap Reporting Procedure.docx](attachments/28379_4-21%20Mishap%20Reporting%20Procedure.docx.md) | docx | 56 | 2025-04-22 | converted |
| image-20250422-205859.png | image | 5 | 2025-04-22 | listed only |
| image-20250422-211533.png | image | 2 | 2025-04-22 | listed only |
| image-20250423-202437.png | image | 758 | 2025-04-23 | listed only |
