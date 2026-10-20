# VXEP-146: VXE-401 Loss of operator control during aborted landing

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-10-18
- **Updated:** 2026-03-02
- **Resolved:** 2024-08-23
- **Due:** 2023-10-19
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** INL
- **Links:** is blocked by VA-796 (Investigate VXE-401 loss of control); relates to VXEP-154 (VXE-401 - Wing oscillation with antennas attached); relates to FS2-1099 (v401 RACE condition investigation); relates to RMA-174 (VXE-401 231023-1); is blocked by VA-929 (Release 2023Q4 (Version 6.2.x) Software)
- **Customer:** INL
- **Vehicle Tail Number:** 401
- **Problem Type:** Other (explain in description)
- **Incident Type:** Aircraft Damage
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

This issue is for the loss of control. 
created a separate issue to investigate the wobble on the same flight. It should be tracked separate than the loss of control. It doesn’t seem like the wobble caused the loss of control, but we can relink if needed.
https://jenaero.atlassian.net/browse/VXEP-154

Storage for files and reports: VXE-401 - Drift on landing, user unable to control (INL, heavy)
>>>>>>>>>>>>>>>>>>>>>>>>>>
@Greg Fryer this is a hot one if we can get a preliminary look at the data that would be very helpful.
From the customer: 
Re-cap:  We are testing a payload in heavy weight configuration with antennas mounted on the outer wings.  We have noticed that when in VTOL, there is oscillations causing the wings to flap up and down. The pilot aborted take-off and tried to move the aircraft.  From the pilots perspective, he said he no longer had control of it at that point.  It stayed in the air and wouldn’t come down and he couldn’t adjust its location.  The plane hovered for a while and then started to drift towards a building near the runway.  Once it was over the building it then began to descend trying to land.  It softly landed on the building but then slid down the gable and hit the ground.  Damage included breaking a tail and props.  Further analysis is needed to check structure of components.  We are trying to source repair parts but one concern is the autopilot in 401, we have lost confidence unless we know what caused the lack of control.
 
We need answers as soon as possible on this so we would appreciate any effort for a quick turnaround.
Report Uploaded to SharePoint: Flight Safety - VXE-401 - Drift on landing, user unable to control (INL, heavy) - All Documents (sharepoint.com)

## Vehicle Configuration

VXE30 battery. Previously used XE25 batt. 
For this flight weight was 51 lbs.  When we were flying the Block 25 battery, the Total mass was 45.9 lbs
Mass of entire payload is about 3.3 lbs
What was the CG of the aircraft?  ~4.65
Firmware Versions:
XComm: V4.67.XEVT
VTOL: V1.52

## Corrective Action

Implement new firmware update, estimated late Q4 or early Q1 release (next).
CONSIDER: Do pause and abort functions overlap to much on controller? (Could a pause be a mistake.)
CONSIDER: Notify pilot to not continue to pause (unknown if this was intentional - e.g. a desire to nudge, or not).

## Plan

- Complete report on bug
- Track closure of CA per SW release.

## Issue Status

Problem replicated and fix implemented, to be incorporated into the next release, expected late Q4 early Q1 depending on overall test time.

## Root Cause

The landing drift occurred due to a software bug. If a “Land Immediately!” command is issued from the GCS during an active launch abort state, the aircraft will become stuck in an attitude update only mode. In this mode the aircraft will not update the horizontal position to maintain desired position.
The vehicle did not descend, during the aborted launch, due to receiving continuous pause commands sent to the aircraft from the GCS.

## Comments (33)

### Greg Fryer, 2023-10-18

@Pat Wells I have created the investigation task and will get someone assigned. Could you please follow up with INL and get the details of the configuration? The initial data would be config (did they use a smaller battery as has been discussed?), mass, and CG properties. What was the total mass of the aircraft, mass of the additional payload, and what was the CG at? They should have all that logged for an out-of-spec flight (which is how I’m interpreting “heavy weight”.

### Greg Fryer, 2023-10-18

@Cameron Chapman FYI, this is the new highest priority item. I planned it and am finding someone to analyze data.

### Pat Wells, 2023-10-18

@Greg Fryer will do
@Sean Odell FYSA

### Pat Wells, 2023-10-18

@Greg Fryer 
Additional information from customer as requested:
Were you using a smaller battery as has been discussed in the past?  For this flight we were using the Block 30 battery.  We have switched back and forth between Block 25 and Block 30.  Interestingly, we have flown two flights with the Block 25 battery and two flights with the Block 30 battery.  For each configuration, we had one that was steady and one that was “flapping”
What was the total mass of the aircraft?  For this flight weight was 51 lbs.  When we were flying the Block 25 payload, the Total mass was 45.9 lbs
What was the mass of the additional payload? Mass of entire payload is about 3.3 lbs. 
What was the CG of the aircraft?  ~4.65

### Greg Fryer, 2023-10-18

@Pat Wells @Sean Odell Sorry for the back and forth on this one, should have been more explicit. They mentioned antennas on the outer wings, what was the weight of each. e.g. how much payload weight at each mount.
Note: we should probably draft some standard questions, this would be one of them.
Also, we are familiar with the flapping, assuming it was a relative small total movement. It can happen in particular combinations of equipment, winds, and landing state. When they say “for each configuration” are they referring to different aircraft, or with the different batteries installed. Likely a table would be a good response. 
Last follow up, when they say “flying the block 25 payload” do they actually mean “flying the block 25 battery”? (e.g a typo happened somewhere along the line)

### David Grosher, 2023-10-18

@Greg Fryer @Cameron Chapman It looks like there is substantial feedback on the roll gyro and Y and z accelerometers. That is feeding through to the lift throttle commands at a about 2Hz (Need to verify with PSD of the signals)
[embedded: image-20231018-173511.png]
[embedded: image-20231018-173656.png]
[embedded: image-20231018-173832.png]
I see the RTL in the event log and then I see a lot of land paused entries in the VTOL event log. 
vtNudge, vtLeft and vtRight, show no nudge commands. unclear if they are logging correctly. Or perhaps they are ignored when landing is paused. 
There does appear to be a change in the commanded position in the local tangential plane. It is unclear what led to the change at this point. 
[embedded: image-20231018-174837.png]
I think @Ryan Christino and @Jason Scherer might have some cycles they can spare to help.

### Jason Scherer, 2023-10-18

Operator Notes from the AAR
“Crash, couldnt control aircraft, Pressed pause button, couldnt move aircraft
When pause button was pressed the it shiftted backwards quickly about 2 feet
After I tried to move aircraft I issued a command immediate.
Didnt go into full udrive mode, I was in nudge mode the entire time.
Maybe I should have gone into udrive immediatly but I was trying to
move it down or give it input to move it away from the shed
AP Version: Ver. 6.05m
AP Build: 0x605000d
XComm Info:
0x04000043
4.67
XCOMM V4.67.XEVT
2023/02/06 11:24:40
0x154F
GCS Info:
Version: 6.0 b12.0 - 20 VTOL COT AES TRIL
Build: 6012
GCS ID: 10
DA at landing: 5759 ft
Estimated range, bearing from vehicle to LZ: 1066 feet  38 degrees”

### Jason Scherer, 2023-10-18

@David Grosher @John Clark Are these VTOL GPS errors “Normal”?
[embedded: image-20231018-181239.png]

### Jason Scherer, 2023-10-18

Also should we see HIL in the messages logs at all for real flights?
[embedded: image-20231018-181344.png]

### Cameron Chapman, 2023-10-18

Everyone, I updated the fields above. You should too as you continue. 
Questions for customer:
- Were there oscillations on each flight? How severe were the oscillations (can be hard to quantify. Concern for wing integrity, or just odd)?

Questions for EA:
- Starting a standard question list here. @Greg Fryer @Pat Wells https://jenaero.atlassian.net/browse/VXEP-146
- @David Grosher@John Clark 
- do you think the accel feedback is related to the vibrations from the wing flapping, or something else? Would this impact location accuracy and cause the drift?
- Can we test if nudge commands are ignored when landing is paused? That seems like exactly when someone would want to nudge.
- Are VTOL GPS errors normal? If not, could these have contributed to the drift?
- Also should we see HIL in the messages logs at all for real flights?
- Good time to start an investigation ppt, or too early? Please save link in description if so.

@Jason Scherer

### Pat Wells, 2023-10-18

@Cameron Chapman @Greg Fryer @David Grosher @John Clark 

Customer provided video of the mishap
 https://photos.app.goo.gl/YnQCSLnEcUNyUWTU9

### Pat Wells, 2023-10-18

Repsonse from customer:
Please be reminded that we have flown this same antenna configuration where the wings were very stable.
Weight of antennas on wings:
8.1 oz left wing
12.7 oz right wing

From customer: 
What was the total mass of the aircraft?  For this flight weight was 51 lbs.  When we were flying the Block 25 payload, the Total mass was 45.9 lbs
 
When you say Block 25 payload did you mean Block 25 battery?

 This was a typo and they meant block 25 battery 




@Cameron Chapman @Greg Fryer @David Grosher @John Clark

### Pat Wells, 2023-10-18

More from customer, debug logs attached to this ticket:
Just to give you some more information on the flight. Attached is the debug log for the crashed flight and one we did yesterday with the same configuration. I can upload my flight logs and videos of the launches wherever you would like.
 
We did a flight yesterday with this same configuration. It was quite windy up high and was drawing lots of power on the front prop (~900W),  I brought it back early. Its launch and land were stable.
 
This morning I started the flight;  I activated Lauch control by clicking on the popup on the laptop. It went up to about 25-30ft to its typical first pause height to make sure sensors are good.  The wings were oscillating so I issued an abort launch via the controller. The aircraft went backwards about 10ft which it's supposed to do to avoid the stand. It kindove went backwards twice.
 
After the aircraft went backwards it just hovered there 25-30ft up. It then started uncontrolled drifting towards the shed. I tried multiple times to nudge it over but I couldn't move the aircraft. I hit abort vtol launch on the gui but it didn't seem to take effect. The aircraft landed down on the shed and slid off, breaking the tail and some props. Maybe I should have tried attitude nudge but by the time I tried nudging it multiple times and checking the coms it came down. Power draw on vtol motors ~3.8kw
@Cameron Chapman @Greg Fryer @David Grosher @John Clark

### David Grosher, 2023-10-18

A bit more data on the position drift. It appears that the system did not track the setpoints.  It did initially and then it veered off. 
[embedded: image-20231018-212200.png]

### Jason Scherer, 2023-10-18

Here is the flight sequence
[embedded: image-20231018-212726.png]

### Jack Waeschle, 2023-10-18

@Greg Fryer @David Grosher  I would classify this as high wobble. In the wobble wing investigation (https://jenaero.atlassian.net/browse/VIT2-225) we never added the mod payload antenna to the wingtips, but this appears to be a similar behavior. The plane is taking off with a crosswind (it drifts towards the shed, indicating wind direction) which lines up with what typically produces wing oscillations. In all the past observed wobble flights, the aircraft never lost control. There are multiple videos attached to the ticket linked above that show aircraft responding to nudges during wobble.
For an additional summary of past testing efforts, see Wing Vibration Report.docx
Even in “high wobble” wing loads should not be anywhere near 9g. If we wanted to pursue tuning out the oscillatory behavior the next steps would be investigating burst data from my testing last spring @Ryan Christino @Everett Werner

### Jason Scherer, 2023-10-18

[embedded: image-20231018-224445.png]

### David Grosher, 2023-10-18

@Jack Waeschle Thanks for the link. Here is some data on the frequency of the oscillation, it appears to be at 1.7Hz (assuming no aliasing, which is certainly possible given the sample rate was <10Hz). Gx is roll rate. 
[embedded: image-20231018-223929.png]

### Cameron Chapman, 2023-10-18

@David Grosher @Jack Waeschle @Greg Fryer @Ryan Christino @Everett Werner I created a separate issue to investigate the wobble. It should be tracked separate than the loss of control. It doesn’t seem like the wobble caused the loss of control, but we can relink if needed. 
https://jenaero.atlassian.net/browse/VXEP-154

### Jason Scherer, 2023-10-19

[embedded: image-20231019-230054.png]

### Pat Wells, 2023-10-20

@Greg Fryer @David Grosher @Jack Waeschle @Cameron Chapman 
FYSA-
Received the following from the INL customer this morning. They have assembled another aircraft and are continuing to fly.  
Wanted to pass along as he mentions behavior related to the wing oscillation issue.

From customer: 
To give you an update we took baby steps yesterday with 464/398 bird.  Tested the following in order:  test flight; take off and abort landing, added antennas only on the wings and did take off and landing (wings oscillates a little but not bad); added full payload with Block25 battery (took off and had full flight,  wings were steady as a rock).  Today we are moving forward with caution but hope all continues to go well.

### Cameron Chapman, 2023-10-20

Thanks @Pat Wells . Reminder, the oscillation issue is being addressed here, as it does not seem related to the loss of flight control. 
https://jenaero.atlassian.net/browse/VXEP-154

### Greg Fryer, 2023-10-20

@Pat Wells Please also make sure they know that winds are a factor in it occurring, we don’t want them putting a bunch of effort trying to diagnose it - only to rediscover what we know already. You may have told them already, but want to be sure.

### Pat Wells, 2023-10-20

@Greg Fryer  understood.  I have communicated with them on winds. 
I don’t believe they are trying to solve the oscillation issue. More than likely they’re just being overly cautious.

### Greg Fryer, 2023-10-25

@Cody Smisek Put any information about 401 here.

### Cody Smisek, 2023-10-25

additional information from customer (attaching other AARs to ticket)

“Hi Cody,
T95_V401_231016_161210_pack_Scetchy_Landing
T95_V401_231018_071556_pack_Crash
T95_V401_231017_072149_pack_Good_Flight_High_Power
These were the 3 Flights I did With 401 Heavy (51lbs). The first one was 231016_161210, on that one I also aborted the launch because of oscillation. Looking at the log it seems to show a lot of the same issues as 231018_071556, the one that actually crashed. Thinking back on it I just got lucky on 231016, I thought I was controlling the aircraft but it just happened to drift the same way I thought I was telling it to. Also, I had to commanded cut the props like 2 feet off the ground because the aircraft lightly bounced off the ground and wasn't landing properly. If I realized how sketchy and not in control that flight was, I wouldn't have done subsequent flights.
The next day we went again 231017_072149. This time the wings didn't oscillate and we did a quick 35min flight due to high power draw and it was getting very windy. Who knows maybe that flight would have shown a similar issue but I didn't abort the flight so we won't know
Again, I think 231016 has the same error as 231018 I just got lucky on the first one.
Best,
Kendel
443-295-5210”

### Cameron Chapman, 2023-10-26

Sean: @Cameron Chapman @David Grosher @Greg Fryer Aircraft evaluated, photos taken, added to RMA ticket for reference. I am bringing over the aircraft today.

### Jason Scherer, 2023-11-01

@David Grosher @Cameron Chapman Per instruction from @Greg Fryer I updated the state of this ticket to “Implementing Corrective Action”. I have identified a bug in the firmware that is triggered by issuing a land immediately command after starting a launch abort. This puts the aircraft into an attitude update only mode and allows for the horizontal drift to occur. I have re-created this issue three times on a HIL. I have a technical discussion scheduled with members of the Flight Systems team to discuss the findings, and determine the appropriate resolution. The ongoing effort for this bug will be tracked on https://jenaero.atlassian.net/browse/FS2-1099.

### Cameron Chapman, 2023-11-08

@Jason Scherer great work! For each investigation, can you please keep the fields above updated as you go (investigation plan, status, C/CA, etc.). 
Is this equipment ready to return to RMA? It seems so. Jason, can you confirm? 
@Sean Odell

### Jason Scherer, 2023-11-08

@Cameron Chapman Understood. I’ll update the tickets status on incidents going forward. 
I don’t need the aircraft, but I believe @Ryan Christino may still be investigating the osculation that occurred in the wing on takeoff.
@David Grosher Any thoughts on starting the RMA?

### Cameron Chapman, 2023-11-08

I asked Ryan in the linked oscillation ticket. Agreed we should clear for both investigations before RMA.

### Jason Scherer, 2023-11-08

I have attached the landing drift investigation report. A bug was identified and recreated in a Hardware in the Loop simulation. A patch for the bug was created and tested in the HIL with success. The software update is now going through the code review process.

### Greg Fryer, 2023-11-09

@Jason Scherer Last request, I promise. Can you please update the root cause to also include that the vehicle did not descend because the abort trigger on the controller became the pause button, so the pilot was holding it in pause? (assuming that is correct) You explained why it drifted, but did not explain why it failed to descend.
And another thing, please put a ticket in with @Craig Burton to consider updating the GCS functionality to not become pause until the trigger is released, or at least evaluate that function and figure out if there is a better way.

## Attachments (17)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [T95_V401_231017_072149_debuglog.txt](attachments/16931_T95_V401_231017_072149_debuglog.txt.md) | text | 83 | 2023-10-18 | converted |
| [T95_V401_231018_071556_debuglog_crash.txt](attachments/16932_T95_V401_231018_071556_debuglog_crash.txt.md) | text | 92 | 2023-10-18 | converted |
| T95_V401_231018_071556_pack.zip | archive | 1951 | 2023-10-18 | listed only |
| image-20231018-173511.png | image | 147 | 2023-10-18 | listed only |
| image-20231018-173656.png | image | 124 | 2023-10-18 | listed only |
| image-20231018-173832.png | image | 382 | 2023-10-18 | listed only |
| image-20231018-174837.png | image | 58 | 2023-10-18 | listed only |
| image-20231018-181239.png | image | 167 | 2023-10-18 | listed only |
| image-20231018-181344.png | image | 48 | 2023-10-18 | listed only |
| image-20231018-182157.png | image | 5 | 2023-10-18 | listed only |
| image-20231018-212200.png | image | 40 | 2023-10-18 | listed only |
| image-20231018-212726.png | image | 167 | 2023-10-18 | listed only |
| image-20231018-223929.png | image | 110 | 2023-10-18 | listed only |
| image-20231018-224445.png | image | 546 | 2023-10-18 | listed only |
| image-20231019-230054.png | image | 1108 | 2023-10-19 | listed only |
| T95_V401_231016_161210_pack.zip | archive | 2527 | 2023-10-25 | listed only |
| T95_V401_231017_072149_pack.zip | archive | 2391 | 2023-10-25 | listed only |
