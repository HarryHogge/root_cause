# ENG-3040: VXE 489 fuse 408 CW Forward Rotors not Starting On Landing Transition

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-04-15
- **Updated:** 2025-10-20
- **Resolved:** 2025-05-05
- **Reporter:** Daniel Lloyd
- **Assignee:** Scott Stuckey
- **Creator:** Daniel Lloyd
- **Labels:** 8-28-Sprint, TIQUILA-Blocker
- **Links:** relates to RMA-114 (VXE 489 Fuse Case 230418); relates to RMA-98 (VXE-489 Wing Case: 230219 ); relates to ENG-1763 (Find a AES-256 encryption Linux application that will accept a 32 byte key and permit mounting a device (mount dev) ); relates to ENG-3056 (V499 Lift ESC transition startup anomaly investigation); relates to VA-239 (VXE 489  Hands on troubleshooting. Identify cause and corrective actions.); relates to VA-240 (VXE 489 Discuss and Determine Containment); relates to VXEP-8 (TPTR-6 VXE 489 fuse 408 CW VTOL Motor delayed start); relates to VA-362 (TPTR-6 VXE 489 VTOL Motor delayed start with Drop Payload); relates to RMA-214 (VXE 408 Wing Case 230418 (Flown with 489 Fuse)); relates to VXEP-426 (VXE 489 Erratic Landing Behavior)

## Description

Files https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Investigations/VIT2-272%20VXE%20489%20Forward%20Rotors%20not%20Starting%20On%20Landing%20Transition?csf=1&web=1&e=Yo8Xqm 
Aircraft 489, operating with 408 wing set, transitioned for vertical landing and the forward rotors did not immediately start. Aircraft pitched hard nose down, lost 100 feet of altitude and then recovered to vertical flight. Aircraft climbed back to landing pattern altitude, 200+ feet, and then taxied back to the PLZ where it performed a normal descent. AAR posted to web site. Garret was the pilot and should be providing a narrative. Aircraft shipped to SLO.  
397059507608

## Comments (53)

### Dustin Gamble, 2023-04-15

Thanks Dan for getting the data and shipping the equipment back to Edge. If the transition would have been at 200 ft we probably would have lost the aircraft.

From the AAR, looks like we are missing the vtol csv files. We should download those off the wing when it arrives at Edge Monday.

From the xcomm log, it shows it commanding throttle to the front two motors (vtThr1 and vtThr2) as it enters the dive. It dives from 258 ft to 128 ft reaching 91 ft/s of air speed. VTOL power comes up in the dive, probably as the front motors are waking up. It climbs back up and does a normal landing.

Recommend inspection and qualification testing of the front two motors. 

Note: this aircraft is needed to support UK MOD demo in Palmdale in a week, April 25th.

@Sam Miller @Former user @John Clark @matthew.curran @Kurt Burian

### Kurt Burian, 2023-04-15

Will look more on Monday, but should have had all motors spinning. VTOL Throttle was there, rearm message in the logs with success ack. Thanks for requesting the VTOL logs Dustin. Exactly what we need next. I want to check the boom currents. Total VTOL current was nonzero.
[19:23:09.318 8844.318] ap dbg: vt re-arm success
[embedded: image-20230416-062503.png]

### John Clark, 2023-04-17

@Kurt Burian vtThr3 is flat (right rear) in the sharp decent. Also a bit slow to come up. I did check another flight and it seems different.

### Kurt Burian, 2023-04-17

@John Clark You woudn't want to rears to be firing during the pitch down. I think that would cause a front flip. Need the fronts going high power to ‘catch’ the dip.

### matthew.curran, 2023-04-17

Assets are here. 489 Fuselage with 408’s CW.  
When you are ready, can we get an inspection and SCO flight test this week?

### Sean Odell, 2023-04-18

@Kurt Burian The assets are now in the RMA area near Carson. Do you need me to bring them over to your team to evaluate? Edge is test flying RMA’s and New assets this Thursday, I believe. Maybe they can be test flown then if you can check them out on your end?

### Sean Odell, 2023-04-18

Photos of Wing and Fuse case uploaded on RMA.

### John Clark, 2023-04-19

@Former user @matthew.curran @Sean Odell I have connected the center wing and fuselage to power and attempted recovery of VTOL Logs. As everyone can see the SD appears corrupted. While I am open to any input regards how we might recover these files. I am now very concerned that file corruption is, once again, a problem. I will continue to search the available FDR to obtain further evidence. I can also try and answer any questions asked. Some further background on the history of the airplane might prove useful as well. Clearly the center wing and fuselage were swapped for a reason. Did I miss the history on that?

### matthew.curran, 2023-04-19

408 CW was used with 489 fuselage due to shortage of parts.
489 CW was damaged during Regression testing and currently in Edge for warranty service.   This was the crash resulting from the vibration filtering.  REF https://jenaero.atlassian.net/browse/VIT2-217  for history on 489 CW.

### Sean Odell, 2023-04-19

@John Clark Please see https://jenaero.atlassian.net/browse/RMA-98 for more clarity into the past of this Aircraft. Hope this helps. @Sean Odell apologies, I should have looked at that.

### John Clark, 2023-04-19

I’ve been looking at the logs on the center wing. Files have been produced for some time that are date stamped 2828. I checked one at random, and it’s coherent. Files become incoherent in 11/2022

### Greg Fryer, 2023-05-15

@John Clark per discussion to take a look. @David Grosher FYI on the other piece of John’s workload.

### John Clark, 2023-05-16

@Hayden Jeanor , please comment 
[embedded: image-20230516-222057.png]
[embedded: image-20230516-224639.png]

### Hayden Jeanor, 2023-05-16

Even though the fwd motor throttle’s spike to ‘catch’ the pitching forward, it seems that they still lack thrust given the throttle command. Coming into the transition, the pitch of the vehicle maxes out at ~6 degrees when it should reach the set pitch of 10 degrees… Assuming the VTOL AP commanded the vehicle to pitch up 10 deg like it is supposed to. The cause could definitely be the lift system, but per our conversation, John, it is also worth it to investigate other noise/external factors that could have been introduced to the control loop to have caused such a large overshoot in the system response.

### John Clark, 2023-05-17

Calculated checksums match the expected values. While the log files themselves display strong evidence of corruption the configuration parameters do not.

### Hayden Jeanor, 2023-05-17

Something that I would be interested in seeing from the VTOL log is the set pitch and roll during transition. I found there was a flight control fault on the roll axis (variable - fltapRoll) that started at cpu time 8788 and ended at cpu time 8843 which is when the vehicle began transition. This could have caused inaccurate set pitch and set roll values into transition and out of the fault.

### John Clark, 2023-05-19

@Hayden Jeanor I have fully investigated attempting to recover the corrupted VTOL logs that would help with this investigation. It does not appear I can recover those at this time. I will, however, create a Jira Engineering project to more fully investigate the possibility of mounting an AES-256 device under Linux. We have the keys, and with Kurt B’s help yesterday I was able to create a build that would accept any key I programmed and use that. Lacking further evidence I would ask that we check at least the forward motors. As per @Kurt Burian there was some indication to me those might have caused the pitch forwards when the VTOL was engaged through delay. @David Grosher @Greg Fryer

### Kurt Burian, 2023-05-19

My guess aligns with John. The front motors, 1 and 2, were making no power at 8848 when the rears turned on. Vtol current is very low while the front throttles are railed from 8848-8850. Pitch down starts to recover at 8848.5 from one of both of the fronts starting to help? Current still shows lower then I would expect. I think at 8849.5 motor 1, FL, might come on. Vehicle starts rolling right and motor 2 is throttled up further as the roll is recovered followed by the huge pitch rate change. 
[embedded: image-20230520-050540.png]

### Kurt Burian, 2023-05-19

@Hayden Jeanor The control loop drives the output. The output is trying really hard to stop the nose down so it seems to be doing its job. The only other place I can see to blame is that the PWM signal isn't being generated during a very specific duration(unlikely). I didnt think the previous PWM investigations on motor start issues showed any issues with what the AP generates, but maybe you can get creative and think of a cycle test if you get convinced its not the motor/esc failing to produce expected power or failing to start completely.

### Hayden Jeanor, 2023-05-23

@Kurt Burian I agree, the current is way too low at 8848-8850 when the front motors are commanded to max throttle. I think this warrants the need for further investigation on the front lift ESC/motor assemblies. I have never seen an issue with the PWM signal generated differ from the throttle reading on the logs, so i also doubt that is it. This investigation has a very similar incident profile to https://jenaero.atlassian.net/browse/VIT2-291 , so i plan to look further into V489 after V407

### Sean Odell, 2023-06-07

@Hayden Jeanor @Scott Stuckey @Greg Fryer @Kurt Burian   I noticed no one is assigned to this RMA/Incident. What is the next steps? Any conclusions? Looking to start a quote to repair but need to verify what is the next steps. Thank you all for your hard work!

### matthew.curran, 2023-06-20

Can we get this back soon?

### Daniel Lloyd, 2023-06-28

How is this done?
@matthew.curran

### John Clark, 2023-06-28

@Daniel Lloyd @matthew.curran this aircraft has corrupted VTOL log files. The file system needs the Flash Reformat and File Recovery procedures attached. In addition to firmware.

### matthew.curran, 2023-06-28

Is the firmware corrupt and needs to be reinstalled, or is there is a firmware update to a new version?  Is this and Edge task, or something we do?

### Daniel Lloyd, 2023-06-28

I guess the part I don’t understand is that this aircraft within a few feet of crashing and Jira shows no investigation plan, no investigation status, no root cause, but it is flagged as Done. Did the corrupted VTOL log files cause the mishap?
@matthew.curran

### Sam Miller, 2023-07-10

@Hayden Jeanor @Scott Stuckey @Greg Fryer @Kurt Burian , Per Sean Odell below, where are we at on analyzing the front motor/ESC for this aircraft.  The TIQUILA customer is setting this as a Severity 1 Problem Tracking Report (PTR), which is becoming a potential block for our upcoming Factory Acceptance Testing (FAT).  Please provide me with an ECD to close this out.

### John Clark, 2023-07-10

@matthew.curran @Daniel Lloyd I did the original work on this aircraft and was unable to make any meaningful conclusions because the VTOL logs are corrupted. The firmware needs update. Because the file system was corrupted that should be reformatted as well. I do not see evidence the VTOL configuration has been corrupted, just the logs. If that is saved it can be reapplied after the reformat.

### Hayden Jeanor, 2023-07-11

@Jeremy Kostel and I will pull both lift motor/ESC assys 1 and 2 from the aircraft for further testing. After inspection of the rest of the lift power system, we will return the booms to final assembly to install replacement lift ESC/motors assys. FYI @John Clark

### John Clark, 2023-07-11

@Hayden Jeanor @Greg Fryer @David Grosher Incident Report attached. Hayden, please let me know when aircraft is available for reformatting and reprogramming.

### Greg Fryer, 2023-07-11

@Sean Odell Please see the comments!

### Hayden Jeanor, 2023-07-11

@John Clark we pulled the ESC/motor assys. Centerwing is available for reprogramming, it is currently next to my workbench in the engineering bay

### Sam Miller, 2023-07-11

@John Clark @David Grosher thank you for preparing the report.  However, the conclusion does not seem to indicate any sort of root cause and the odds of TWO front motor/esc’s failing simultaneously seems improbable.  The corrupt VTOL log is highly suspect.  Due to schedule constraints, I recommend replacement of the SD card and possibly the VTOL controller.  I think we should run further tests on the VTOL controller as time permits.  Maybe a good intern project.  Thoughts?

### Hayden Jeanor, 2023-07-12

[embedded: image-20230712-155736.png]
Here is data from running both forward lift motor/ESC assys on the dyno. Both have similar responsiveness and performance to that of an Iron Bird motor/ESC assy. As another note: during testing, the software parsed the flight profile script incorrectly and ran motor 2 (front right) from 408 at 95% throttle for 10s longer than expected causing motor failure, likely due to overheating the windings. I do not think this should be attributed towards the investigation, considering how the motor was performing before the failure.  However, I would be interested to see the last time the 408 booms were serviced to determine if a service interval was possibly missed.

### Hayden Jeanor, 2023-07-12

@Kyle England I delivered the lift booms from this investigation to Final Assembly to be reassembled with new lift ESC/motor assys. Please allocate appropriately and return to eng. Let me know if you have any questions. Thanks!

### John Clark, 2023-07-13

@Hayden Jeanor can we replace the red board in the CW as well? Per @David Grosher request. Let me know if I can help there. We will a production reflash and config on that, I think.

### Hayden Jeanor, 2023-07-13

Upon removal of the red interface board, we were able to inspect the bottom side. See photos of the inspection below. 
[embedded: IMG_0219-20230714-003923.jpg]
[embedded: IMG_0220-20230714-001539.jpg]
[embedded: IMG_0005-19800101-070000.jpg]
[embedded: IMG_0001-19800101-070000.jpg]
[embedded: IMG_0002-19800101-070000.jpg]
The nylon screw (p/n: 100-102984) that fastens the ballast weight (p/n: 107-102859) to the red AP interface board broke free, likely due to vibration. This allowed the conductive brass weight to swing freely causing a potential short along the scar that it inflicted on the PCB. In fact, it was so damaging that a resistor (R32) got dislodged from the solder pads. Working on an analysis to determine a direct relationship between this non-conformance and the behavior we saw during the investigation.

### Daniel Lloyd, 2023-07-13

Great find

### Hayden Jeanor, 2023-07-17

returned 408 Centerwing and lift booms to RMA area per @Kyle England 's request. Centerwing needs VTOL AP board and VTOL AP interface board replacements. Lift booms need motor/ESC assys replacements. @Desiray Johnston please insert this high priority vehicle return into production queue to address aforementioned dispositions as well as an SCO. Let me know if any clarification is needed. Thanks! FYI @Sean Odell

### Sean Odell, 2023-07-25

@Hayden Jeanor Can you verify the part numbers of the parts needing replacement please? - VTOL AP board and VTOL AP interface board?
Also, are the Motor/ESC replacement for all 4 motors/ESC’s? Or a single motor? Is the replacement due to the evaluation, incident, or maintenance?  Thank you for your assist and hard work!

### Hayden Jeanor, 2023-07-25

After some quick analysis, this is my theory for what happened during this incident: 
Somehow the nylon screw (P/N: 100-102984) that fastens the ballast weight (p/n: 107-102859) to the VTOL AP interface board (P/N: 107-107306) sheared off, likely due to vibration. I'm am not sure how long before the incident the screw was sheared, but it was long enough to leave a visible scar on the board and dislodge resistor (R32). Most of the damage was sustained in the circuit that includes Q2 and R32, but this circuit is not used in the production version of the aircraft. J26 and J24 are unpopulated.
[embedded: IMG_0001-19800101-070000 (2f6ab2f2-1a11-4eb0-bc43-7da756835f26).jpg]
[embedded: image-20230724-214535.png]

At the end of the ballast weight’s arc, it barely makes contact with pin 8 of T4 while also making contact with the GND pad of C60. Overtime, the conformal coat must have worn down from the ballast weight making contact on those pads which exposed conductor. 
[embedded: IMG_0002-19800101-070000 (8a746e0b-5881-4d9a-b13b-7c0923b3947d).jpg]
[embedded: image-20230724-223349.png]
During the incident flight when the vehicle pitched up to transition to VTOL landing, the ballast weight swung to the extreme of its arc, making contact with pin 8 of T4 and the GND pad of C60. This would cause the TX5_N ethernet line that is designated for main vehicle communication to be pulled to ground. This likely caused any data being transferred on this line to be garbage or lost. This likely also explains how the VTOL logs were corrupted. Although it seemed like only the fore lift motors did not perform as expected, I think all lift motors were affected by this non-conformance. When they did not produce enough or erratic thrust, the vehicle’s nose dove which would have caused the ballast weight to swing back towards its original position on the AP interface board, removing the short between pin 8 of T4 and the GND pad of C60 and allowing the VTOL avionics to function properly again.

### Hayden Jeanor, 2023-07-26

@Sean Odell please see the investigation plan field for my disposition. @Greg Fryer  please let me know if this requires review

### Greg Fryer, 2023-07-26

Moved back to Hayden, no need to reassign. Will review and close out or add new actions in review board 7/27.

### John Clark, 2023-07-28

Attached Incident Log Analysis with additional findings. @Hayden Jeanor @David Grosher @Greg Fryer there were numerous losses of Ethernet coms, possibly due to failures found. Because the timings do not align to the incident it is not possible to conclude those electrical failures (short) contributed to the pitch and resulting loss of altitude.
[embedded: Vehicle 489 incident report (0971d2a7-5945-46bd-85a6-f9a11270ccfa).pptx]

### Cameron Chapman, 2023-08-02

New theory:
Since forward left and right did not respond and back ones did, the new theory is that the swinging bar interfered with pins for SERVO1 and SERVO2 signals highlighted below. This is supported by the data, as the throttles from the VTOL AP go up to attempt to power these motors, but they get no motor response in measured power. The reporting of these throttles also indicates the VTOL AP was powered and communicating during the event. @Hayden Jeanor can you either check if this interference is possible, or find someone else to check that. 
[embedded: image-20230802-225541.png]
Other potential causes: 
- Simultaneous failures in the harness or ESCs (unlikely)

### Hayden Jeanor, 2023-08-04

[embedded: image-20230804-154836.png]
Working off @Cameron Chapman's theory. There would have been a mechanical disturbance within these two traces. Upon first glance it does not look like the arc of the weight would make contact with the vias of these traces, but i will check monday when I get back in office and can more thoroughly inspect the board again. A short between these two traces would likely cause loss of throttle telemetry to both fore lift ESC systems.

### Cameron Chapman, 2023-08-04

I agree. The arc does not seem to cross servo 1-2 traces. It is on the other side of the board when it does. 
[embedded: image-20230804-163512.png]

### Hayden Jeanor, 2023-08-08

After inspection of the board, it does not look like the ballast weight made any contact with Servo 1 and 2 traces:
[embedded: IMG_0008-19800101-070000.jpg]
[embedded: IMG_0009-19800101-070000.jpg]
[embedded: image-20230809-003053.png]
Coming up with more possiblities

### Cameron Chapman, 2023-08-09

Measure servo 1-2 outputs then apply vibration to simulate the loose weight to see if the signals get interrupted?

### Hayden Jeanor, 2023-08-10

Performed testing where @Jeremy Kostel and I connected V408CW VTOL AP avionics into Iron Bird. The goal was to create a disturbance in Servo lines 1 or 2 from the loose ballast weight. From our testing, the weight did not interfere with Servo lines 1 or 2. It also did not interfere with the Ethernet traces on T4 that I had suspected before. No conclusive results were found from this testing.

### Hayden Jeanor, 2023-08-11

After further investigation, we are unable to replicate what was observed during the incident. No amount of vibration or disturbance of the PCB by the ballast eight causes failures in Servo lines 1 and 2. However, I still believe that the issue has an extremely high likelihood that it originated from the hardware of 408 center wing avionics:

The amount of power drawn form the lift system did not match what we would expect to see:
[embedded: image-20230811-232115.png]
[embedded: image-20230811-232125.png]
It is a little difficult to tell due to the low resolution of the data, but it is evident that the power draw barely responds to a huge throttle command at the beginning of the incident flight. 
There three possibilities that the ESC was not pulling power during the incident:
- The ESC/motor assy was malfuncitoning
- already tested and verified to be operating at expected performance on dyno
- There is a problem with the power delivery harness 
- It is highly improbable that the two forward sections of each boom harness would fail simultaneously
- if a failure occurred further upstream, the rear lift ESCs would have also failed.
- There is a problem with the servo PWM command lines
- highly unlikely that it occurred simultaneously in each harness
- Highly likely that problem occurred before the signals physically split apart from each other which would be on the VTOL avionics


Note: these possibilities are assuming that the description was correct that the forward lift motors did not start and the rears did. 

Recommended to replace avionics as planned and close out the incident investigation. If anyone can think of any additional tests or techniques i could implement, please let me know. Otherwise, i will close this out.

### Hayden Jeanor, 2023-08-14

@David Grosher assigning to you for review. I assume we will go over this ticket during the next investigation meeting. We can discuss further then.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent.

## Attachments (28)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V489_230414_122125_pack.zip | archive | 1826 | 2023-04-15 | listed only |
| image-20230416-062503.png | image | 115 | 2023-04-15 | listed only |
| 20230418_125350.zip | archive | 231745 | 2023-04-18 | listed only |
| LogFilePage.png | image | 111 | 2023-04-19 | listed only |
| image-20230516-222057.png | image | 212 | 2023-05-16 | listed only |
| image-20230516-224639.png | image | 70 | 2023-05-16 | listed only |
| image-20230520-050540.png | image | 121 | 2023-05-19 | listed only |
| [FlashReformat.docx](attachments/15234_FlashReformat.docx.md) | docx | 649 | 2023-06-28 | converted |
| [Vehicle 489 incident report.pptx](attachments/15404_Vehicle%20489%20incident%20report.pptx.md) | pptx | 648 | 2023-07-11 | converted |
| image-20230712-155736.png | image | 119 | 2023-07-12 | listed only |
| IMG_0001-19800101-070000.jpg | image | 4414 | 2023-07-13 | listed only |
| IMG_0002-19800101-070000.jpg | image | 4161 | 2023-07-13 | listed only |
| IMG_0005-19800101-070000.jpg | image | 4405 | 2023-07-13 | listed only |
| IMG_0219-20230714-003923.jpg | image | 440 | 2023-07-13 | listed only |
| IMG_0220-20230714-001539.jpg | image | 448 | 2023-07-13 | listed only |
| IMG_0001-19800101-070000 (2f6ab2f2-1a11-4eb0-bc43-7da756835f26).jpg | image | 4414 | 2023-07-25 | listed only |
| IMG_0002-19800101-070000 (8a746e0b-5881-4d9a-b13b-7c0923b3947d).jpg | image | 4161 | 2023-07-25 | listed only |
| image-20230724-214535.png | image | 19 | 2023-07-25 | listed only |
| image-20230724-223349.png | image | 28 | 2023-07-25 | listed only |
| [Vehicle 489 incident report (0971d2a7-5945-46bd-85a6-f9a11270ccfa).pptx](attachments/15621_Vehicle%20489%20incident%20report%20(0971d2a7-5945-46bd-85a6-f9a11270ccfa).pptx.md) | pptx | 777 | 2023-07-31 | converted |
| image-20230802-225541.png | image | 1427 | 2023-08-02 | listed only |
| image-20230804-154836.png | image | 161 | 2023-08-04 | listed only |
| image-20230804-163512.png | image | 493 | 2023-08-04 | listed only |
| IMG_0008-19800101-070000.jpg | image | 6552 | 2023-08-08 | listed only |
| IMG_0009-19800101-070000.jpg | image | 6262 | 2023-08-08 | listed only |
| image-20230809-003053.png | image | 3664 | 2023-08-08 | listed only |
| image-20230811-232115.png | image | 140 | 2023-08-11 | listed only |
| image-20230811-232125.png | image | 123 | 2023-08-11 | listed only |
