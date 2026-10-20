# VXEP-426: VXE 489 Erratic Landing Behavior

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-06-06
- **Updated:** 2026-05-05
- **Resolved:** 2026-05-05
- **Reporter:** Pat Wells
- **Assignee:** Everett Werner
- **Creator:** Pat Wells
- **Labels:** FlightSystems, LM_asset, Weekly-incident-tracker
- **Links:** relates to ENG-3046 (489 Erratic Landing Behavior ); relates to FS2-1943 (v489 Erratic Landing Behavior); relates to RMA-299 (VXE-489 RMA 240726 (LM)); relates to VXEP-103 (VXE-473 Crash on landing, failed to transition to VTOL); relates to ENG-3040 (VXE 489 fuse 408 CW Forward Rotors not Starting On Landing Transition); relates to VXEP-1566 (VXE-828 Rough Transition to VTOL)
- **Customer:** LM, LM_Asset
- **Vehicle Tail Number:** 489
- **Corrective Action:** Tune loop and ESC FW settings, see report for details.
- **Issue Status:** review and clean up the ppt when you get a chance, and provide recommendations for CAs and next steps?
- **Incident Type:** Other (Record"Event Type: XXXXXX" in the description)
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Files: (none currently) VXE489_TransitionBehavior
Investigation: VXE-489 Investigation Report Draft 01.pptx
From LM FSR:
On two successive flights, following the landing transition, the aircraft swapped directions, rapidly lost altitude, and then recovered to a nominal landing. Constraints of the landing zone necessitated landing with a tailwind so weathervaning was expected. Landing on 4 June winds were 7 mph and winds on 5 June were 2.5 mph. The aircraft’s behavior was the same even with lighter winds. Would like an analysis of this behavior to determine if the aircraft is safe to continue flight operations.
This is an LM asset not associated with the Tiquila program.

AAR’s attached.

## Plan

- Report submitted. @Jacob Troyerplease complete fields below (add links to CAs) and set Jira state and actionee appropriately.

## Root Cause

VTOL AP process of commands to motors with existing configuration and settings in ESC FW is causing a delay.  See report for details.

## Comments (84)

### Jackson Riley Curvin, 2025-09-16

@Steve Gonzales any updates on this?

### Steve Gonzales, 2025-09-16

@Jackson Riley Curvin Yes, I have been actively working this.  PPT is about 7 days lagging.  So far this is what we know:  #3 motor tested noisy or bad in production re-test. Motor homing is about 186deg. from zero. No delay has been observed with this motor.  125ms standard delay only. Flight Logs are showing 1.2 and a 3.1 sec delay and almost no delay during the landing sequence.  Motors are producing negative current before transitioning, possible some spin, but brake should be latched.  ESC is sensitive to noise.  In addition, known issue with microchip causing delay on the analog comparator in Rev L errata.  I believe we have rev L chips.

### Drew Hildreth, 2025-09-22

@Steve Gonzales How are we looking on this one? This ticket is very old and I am catching a lot of questions from the customer on this? Are we to a point where RMA can have the aircraft back to get ESC’s or Motors replaced. I know you were still trying to nail down what all was effected. 

@Lauren Velasquez FYSA

### Steve Gonzales, 2025-09-22

@Drew Hildreth Hi, see updated notes above from Friday.  It looks like the VTOL had a flag that purposely sent #3 motor to standby/brake state, causing the delay seen.  The motor and esc are not perfect but did not cause the delay.   We ticket needs to go back to FW to understand the logic for control of the A/V.  This does not seem to be a glitch in the code but that is our current state.  I would replace all 4 esc/motor combos and replace the VTOL pcb and sensor inputs to the VTOL, but this will not address the FW control logic.  That may be a long-time FW revision fix.  Note this issue could be upstream of the FW logic and coming from a sensor input.  This behavior is not new.  It was seen in 2023 but not fully recognized or examined.  I see the same issue in the plots from 4/2023, although without plotting the flags or state condition of the vtol, the same motor 3 dark blue goes to standby/brake the flat blue lines near 0.  
[embedded image-20250922-173936.png]

### Drew Hildreth, 2025-09-22

@Steve Gonzales Awesome. Thank you.

### Steve Gonzales, 2025-10-01

@Scott Whitney @Eric Brewer @Drew Hildreth  Hi Eric, this report is ready for you to review.  I believe the flight control command sent to the motor to go to steady state is causing the delay in current seen.  VXE-489 Investigation Report Draft 01.pptx

### Steve Gonzales, 2025-10-27

Report is up to date. Performed setup for flight replay 10/24/25

### Steve Gonzales, 2025-10-28

Completed dyno testing 10/27

### Steve Gonzales, 2025-10-29

Report completed, moved to D4 RCR @Drew Hildreth FYSA @Eric Brewer @Cameron Chapman

### Eric Brewer, 2025-10-29

@Steve Gonzales thanks for running the testing.  I created an associated ticket that we can try to get into the next software release as a corrective action.  @David Grosher @Scott Whitney FYI.
Jira

### David Grosher, 2025-10-29

@Eric Brewer @Steve Gonzales I don’t understand the analysis or the corrective action here, more detail will need to be added to the report to connect the dots, show additional code analysis and follow on testing to confirm the hypothesis.

### Eric Brewer, 2025-10-29

@David Grosher I think slides 20/21 show the relevant dyno data that reproduces delays with the inputs from the flight.  I think more characterization of the exact conditions that recreate the issue and subsequently what can correct the issue will be required.  I think the reproduction is sufficient to move from investigation to corrective actions.

Agree the report needs some consolidation/cleanup to make it more clear.

### Steve Gonzales, 2025-10-30

@David Grosher @Eric Brewer I updated slide 6,9 for clarity.  Improved slide 15.  Added slide 20 for code explanation.

### Cameron Chapman, 2025-11-04

Pasting info that no longer belongs in the plan field. 


10/29/25
Plan to have CA accepted or move to closed D8.  
10/28/25
Plan to update report by 10/28 from completed dyno testing on 10/27.
10/23/25
Plan to do a verification dyno flight profile test on 10/24/25 and 10/27/25 as a first step before considering tuning.  
10/7/25
Plan to review and respond to Eric’s comments by end of week.
9/22/25
Plan to update report and give to FW team for further evaluation. Please notify team when ready to review. 

9/11/25
Plan to possibly add load, lower voltage and retest for motor delay.  Understand if ESC or motor related or neither.  Scope timing from software command to input at esc to output at esc to motor open commutation to closed loop commutation cycle.  Understand if comm related or where the breakdown takes place.

9/2/25
Prepping to test today.
8/20
Plan to test by the end of the month. 
8/5/25
Extending testing to 8/11 to 8/15.  Sharing O-scope with Block 35-40 development and other priorities.
7/23/25
Plan to retest motor this week and send to Magicall afterwards.
7/15/25
Plan to send unit out to Magicall for further troubleshooting by the end of the week.  I may perform one additional test before that.  
7/9/25
Plan to characterize the SPI communication lines between the ESC and Motor (this may be the cause of the delay) by 07/14/25
Some potential causes:
- Task or processor lock up on either the VTOL AP or motor ESC. @Eric Brewer is this possible, or would more tasks lock up/not recover in this case?
- Loose connection in either harness or one of the PCBs. EEs can investigate.
- @Eric Brewer do vbatt and other VTOL AP power signals look normal during this period?

Recommended next step options for aircraft . Discussed with @Eric Brewer and he agrees. 
- If LM operators are comfortable with the motor test page, they could test each motor sequentially, paying close attention to motor 3 to see if there is a lag from the command to the activation, or any other issues. If observed, replace motor assy 3 and see if fixed.  If not, see below.
- Return whole aircraft for inspection and troubleshooting.
- Return just motor assembly 3. Ground that center wing and boom until investigation has more information. I don’t think we have yet proved it is isolated to the motor assembly.

Above steps completed.  Lockheed ran motor tests and saw significant delays on motor 3.  See description here:
https://jenaero.atlassian.net/browse/VXEP-426?focusedCommentId=37781 
Step 1: see if we can reproduce this behavior.  If we can and it is repeatable, we’ll want to go about instrumenting the system to isolate where the motor delay is coming from.
isolate between AP VTOL and Motor 3 ESC 
- Hook up V489 CW to Iron Bird and perform Safety Motor test using webpage 
- If VTOL AP issue then motor 3 should lag on launch 
- VTOL webpage would not load up - potentially SD card issue? 
- fixed by switching to new industrial sd card
- Hook up V489 Booms to Iron Bird and perform Safety Motor test using webpage 
- If Motor 3 is bad then the issue should be replicated
- No issues seen with motor 3. Motor 1 would restart when initially given throttle
- Retest V489 motors and try to replicate issue

### Cameron Chapman, 2025-11-04

Pasting info that no longer belongs in status field. 
10/16/25
Report is up to date. Replied to all comments.
9/19/25
Found flag state(s) in the vtol FW on motor 3 which brought down throttle command to idle before sending it to 93% causing the delay in current draw seen specific to motor 3.  In addition, a general delay has been found from the vtol fw control mixer to at least 3/4 motors after 1957.
[embedded image-20250919-190452.png]
 

9/11/25
#3 motor tested distorted at low speed (THD ~2%) 2x good motor, higher 2nd harmonic, noisier FFT floor, some mechanical imbalance or winding asymmetry possible.  8 captured runs did not cause a delay with manual PWM injection from RC controller direct to ESC.  10+ informal runs did not cause a delay.  High speed harmonics ok.  Delay seen was 125ms, ok.  Need to check if homing is ok. 
8/5/25
Received magnet wire insulation removal tools.
7/21/25
Performed more testing with mixed results.  Not obtaining good conductivity.  Ordered proper tools to remove the insulation on the magnet wire.  
7/15/25
On motor #3, tested back emf on phase AB, AC, and BC.  Found reduced amplitude and waveform distortion all phases.  Possible rotor/magnet issue(s), defect(s) from the OEM.  Possible root cause found for delay seen.   

7/9/25
VTOL motor 3 tested 3x in production per ESC/Motor checkout procedure.  Deemed as a reject due to scratchy noise while running, un-smooth manual operation, different overall tonality while running.  

6/13/25
FW check on ESC initial code check seems ok.  XTAL on ESC PCB measures 15.4Mhz or 15.94Mhz pending confirmation picture and stable through hot and cold.  

5/9/25
Investigating VTOL current delay to PWM output of VTOL pcb to ESC-motors 1-4.  Added slide #9. 

5/22/25
VTOL motor 3 right rear esc may have not gotten programmed incorrectly and that may be why there was a delay on during the flight. Ran motor through production FW checkout test only and no issues were seen.

Motor 3 slow to respond on transition. Cause unknown. See powerpoint here:
https://jenaero.sharepoint.com/:p:/r/sites/FlightSafety/Shared%20Documents/Incident%20Reports/VXE489_TransitionBehavior/AV489_TransitionBehavior.pptx?d=w08391b63f9d74495832b366250a34f71&csf=1&web=1&e=mGlFLj 

VTOL AP board will not boot up to webpage 3/10/25
- Most likely SD card issue 
- Replacing old SD Card with newest one and uploading newest firmware to motor test


- Tested booms on the Iron Bird with Iron Bird’s VTOL Board and did not see an issue with motor 3. However, when initially spinning Motor 1 the ESC would reset and then I was able to command throttle normally. 
- If the VTOL Board connects to the webpage and spins the motors normally, I believe the issue would be isolated down to the ESC/Motor

3/12/25 Morning 
SD card replaced with new Industrial card and is able to boot up webpage. Old SD card is on my (Adrian G) workbench 
- Have not updated Firmware or flashed new SD Card. CW tested on the Iron Bird with Iron Bird’s VTOL motor and each motor spun up normally and expected. I did not see any delay in motor 3 nor did I experience any of the resets I motor 1 had when I initially tested.

3/12/25 1:46 PM
### Update: V489 SD Card and Motor Testing on Iron Bird

- V489 SD Card & Firmware: The SD card was not flashed, and the firmware was not updated.
- Iron Bird Motor Test: The CW was connected to the Iron Bird, and the IB motors were spun. No anomalies were observed, and the issue could not be replicated.

### V489 Motors on IB AP Board

- Motor #1 reset upon the first command but subsequently responded immediately when commanded.
- Motor #3 did not exhibit any issues and could not replicate any previous anomalies.

### V489 CW and ESC/Motors on IB

- The previously reported issue where Motor #3 exhibited a 2-3 second lag could not be reproduced.
- Various motor sequences were tested, with all motors spinning up immediately.

### Motor Test Sequences & Results

| Test # | Sequence | Result |
| 1 | #1, #2, #3, #4 | All motors started immediately (required two clicks to start) |
| 2 | #1, #2, #3, #4 | All motors started immediately (required two clicks to start) |
| 3 | #2, #1, #3, #4 | Initial motor command caused webpage refresh |
| 4 | #2, #1, #3, #4 | All motors started immediately |
| 5 | #3, #1, #2, #4 | Initial motor command caused webpage refresh |
| 6 | #3, #1, #2, #4 | All motors started immediately |
| 7 | #4, #1, #2, #3 | All motors started immediately |
| 8 | #4, #1, #2, #3 | All motors started immediately |

### Observations:

- Instances where the webpage refreshed appeared to be caused by issuing commands too quickly.
- No significant delays or abnormalities were observed across the motor tests.


4/1/25 Has not moved forward; no resources allocated.

### Cody Smisek, 2025-11-18

@Jacob Troyer @Drew Hildreth cases are over in engineering, can it be returned to RMA?

### Drew Hildreth, 2025-11-18

@Cody Smisek I have the report for that aircraft too. I am good with it going back to RMA.

### Everett Werner, 2026-02-17

I was able to cause a vxe30 esc and motor to fail to start with the following throttle input:
[embedded image-20260217-230747.png]
I tried again later in the day and could not get it with the same level of regularity. I recommend the next motor that has this issue be given to engineering for testing and hopeful replication on the dyno stand. It is worth noting that this isnt the exact same profile as we see in flight as the motor isnt delayed but not starting at all.

### Everett Werner, 2026-02-20

NCR List - AC 995 - Flight Test - Abnormal transition

### Eric Brewer, 2026-05-05

Incident investigation is closed.  Root cause analysis/corrective actions for the slow motor startup are ongoing but this investigation is closed.

### Eric Brewer, 2024-07-22

@Pat Wells yes if they’re able I think it’s worth getting to the bottom of the issue.  If they can’t we may want to look internally to see if we are able to reproduce on another bird.  @Sean Odell

### Pat Wells, 2024-07-22

@Eric Brewer I will make the request.

### Pat Wells, 2024-07-25

Customer shipped aircraft to SLO on 7/25

### Pat Wells, 2024-07-26

@Eric Brewer aircraft arrived in SLO today 7/26
@Sean Odell will be delivering it today so that you can continue your investigation.

### David Grosher, 2024-08-12

@Eric Brewer Did you get any additional data here from the AV? Did we get EE support for it (may be difficult until TIQ deliveries are met)

### Eric Brewer, 2024-08-12

@David Grosher no I haven’t done anything with this one yet.  I think first step is to try to reproduce the issues that LM observed, then we’ll have to try to see if we can isolate the root cause (autopilot interaction, ESC, motor, other).  Who should I reach out to for EE and/or ground test support?

### David Grosher, 2024-08-12

@Eric Brewer Cameron can help secure support when it is available.

### Eric Brewer, 2024-08-12

@Cameron Chapman FYI, let’s tag up once you have some bandwidth freed up from MAGNSS.

### Eric Brewer, 2024-08-27

@Cameron Chapman do you have some time to do debugging on this now?

### Cameron Chapman, 2024-08-27

@Eric Brewer not really. Have to resolve a battery issue that is shutting down production now. @Rajesh Budhabhatti may be available soon.

### Rajesh Budhabhatti, 2024-08-28

I noticed that ibatt2 current is consistently lower than ibatt1 by about 20 amps. I will run some tests on engineering asset motors by current limiting the motor and see if I find similar behavior. There could be an issue with wiring harness to motor 3. It seems that motor 4 is working normally which means that if this is the problem, it would be localized to the motor 3 connection jacks.

### Rajesh Budhabhatti, 2024-08-28

@Eric Brewer Hi Eric, I am wondering why you suspect motor 3 specifically?

### Eric Brewer, 2024-08-28

@Rajesh Budhabhatti see plot, let me know if you’d like to discuss.

[embedded image-20240828-190117.png]

### Rajesh Budhabhatti, 2024-08-28

@Eric Brewer Hi Eric, I saw the same thing and interestingly another aircraft VXE545 has similar problem. I suspected bad connection on wire harness and ran a dyno test with current limiting. I have some more ideas and will keep digging and keep you updated. Is the motor coming back?

### Rajesh Budhabhatti, 2024-08-28

VXE489 June 4 Investigation.pptx

### Eric Brewer, 2024-08-28

@Rajesh Budhabhatti yes it does appear that all the rotors come back on and the airplane lands as normally.  If you can, please consolidate your investigation slides with the existing slides linked above.
https://jenaero.sharepoint.com/:p:/r/sites/FlightSafety/Shared%20Documents/Incident%20Reports/VXE489_TransitionBehavior/AV489_TransitionBehavior.pptx?d=w08391b63f9d74495832b366250a34f71&csf=1&web=1&e=mGlFLj

### Rajesh Budhabhatti, 2024-09-03

@Eric Brewer I have 489 set up in dyno room and powered by 2 power supplies. 
AP motor test page: 
I am seeing erratic behavior that is not repeatable. I see that one motor, typically 1 or 3 that is slow to respond first time I command it on but a. rest of them will respond and b. next go around they will all respond. 
Typically if I Safe and Unsafe motors, the can be repeated. It also seems like the order of motors commanded matters.
GCS motor test always works.
Both GCS and AP pages: 
Turning safety off 1,2,4 motors would shake and jiggle. #3 motor gives a slight jerk but not jiggle like others.
Turning safety On, motors 1,2,4 home correctly while motor 3 is off by about 5 degrees.

### Rajesh Budhabhatti, 2024-09-03

@Eric Brewer Today I will compile our findings, run motor tests and download AARs./logs for software team. Hopefully this will make it easy for them to locate the issue.

### Pat Wells, 2024-09-16

@Rajesh Budhabhatti @Eric Brewer  checking in for any updates ahead of the Air Worthiness brief with TIQ on Wed 9/18

### Eric Brewer, 2024-09-16

None from me, @Rajesh Budhabhatti were you able to run any more testing?

### Rajesh Budhabhatti, 2024-09-16

No update from me. I have been working on 545.
Thank you

### Eric Brewer, 2024-12-06

@Rajesh Budhabhatti are we able to continue the testing on 489? We have experienced similar issues on other aircraft with motors not spooling up on transition so I think it’s important to get to the bottom of this one.  It looks like as of September 3 you had recreated the issue and we were hoping to get some more detailed logs of the events.  Based upon what we see on the logs we may want to do more testing with additional instrumentation.
@David Grosher FYI.

### Rajesh Budhabhatti, 2024-12-06

As I remember, we did some testing on this aircraft. I was pulled off to other project and we did not fine a conclusive root cause at that time.
I will find this aircraft and set it up in Dyno room for further testing. I am wrapping up SA camera issue and will have some time to work on this intermittently.
I will get back to you as things progress.
Can you tell me the other aircrafts that are having similar issues so I can look them up and see if we can derive some useful information on this issue?
Thank you Eric,
Raj

### Alexander Alan Arnold, 2024-12-10

@Rajesh Budhabhatti Were you able to complete dyno testing on this aircraft?

### Rajesh Budhabhatti, 2024-12-10

@Alexander Alan Arnold We did some ground testing and noticed anomalies during the motor test. VTOL motors were never removed and run on Dyno. I was taken off this task shortly after we started testing and found that under some conditions the VTOL motors would not run when commanded through motor test from GCS.

### Alexander Alan Arnold, 2024-12-10

@Cameron Chapman Is the corrective action portion still accurate or are you waiting on anything from the RMA area/global support?

### Cameron Chapman, 2024-12-10

@Adrian Garcia can you please review this issue, Raj’s test data, update fields, and work with @Eric Brewer for next steps?

### Eric Brewer, 2024-12-10

@Rajesh Budhabhatti 473 linked above was the most similar, although there were some other cases that had slightly different signatures that could be related depending what we find here.

### Rodney Linch, 2025-03-03

@Eric Brewer , @Adrian Garcia - gentlemen, looks like the trail went cold on December 10th. Were you able to revisit and diagnose the issue(s)?

### Eric Brewer, 2025-03-03

@Rajesh Budhabhatti @Cameron Chapman I am not sure what the status is of the testing of this vehicle.
@Rodney Linch @Adrian Garcia FYI.

### Sam Miller, 2025-03-07

@Adrian Garcia and @Pat Wells Based on the report info, activity chain, and testing results from Dan Lloyd below, I request that we load the latest released firmware set 6.3.4 and reconduct the ground-based VTOL motor run tests.  If the same issue occurs where any of the motors have a delayed start or the webpage stops responding (or any other anomaly), replace the VTOL autopilot and conduct the tests again. If we are still experiencing a delay in motor start on #2 or #3 motor after autopilot replacement, replace those ESC/motors and retest.

### Adrian Garcia, 2025-03-10

When connecting the CW to the Iron Bird I could not get the web page to load up. May be an SD card issue but can not confirm. @Jason Scherer Can you take a look at the CW for me and deduce if not being able to load the webpage is a SD card issue. 
FYSA @Cameron Chapman @David Grosher

### Adrian Garcia, 2025-03-10

Tested V489 motors on the iron bird and every time, on its first spin up, Motor 1 (from the VTOL Webpage) would restart and then upon testing motor 1 would spin on command. No other motor did this and all spun on command. Below I attached a video to show what happened. 
Motor 1 is the Clock-Wise Left wing in this case 
[embedded MicrosoftTeams-video.mp4]
@Cameron Chapman @David Grosher @Eric Brewer

### Eric Brewer, 2025-03-11

@Adrian Garcia thanks.  Was this updated to 6.3.4 as suggested by Sam or still existing software version?  Also to confirm - you are not seeing the motor 3 lag that Dan at LM observed?  @David Grosher @Cameron Chapman

### Adrian Garcia, 2025-03-11

@Eric Brewer This was still with its existing software version. And correct I am not seeing any lag in motor 3

### Adrian Garcia, 2025-03-12

Switched SD card to the new industrial one and the CW was able to connect to the webpage. I still need to flash and will update with newest firmware and proceed with motor testing.

### Adrian Garcia, 2025-03-12

Copied from Issue Status 
### Update: V589 SD Card and Motor Testing on Iron Bird

- V589 SD Card & Firmware: The SD card was not flashed, and the firmware was not updated.
- Iron Bird Motor Test: The CW was connected to the Iron Bird, and the IB motors were spun. No anomalies were observed, and the issue could not be replicated.

### V589 Motors on IB AP Board

- Motor #1 reset upon the first command but then responded immediately when commanded.
- Motor #3 did not exhibit any issues and could not replicate any previous anomalies.

### V589 CW and ESC/Motors on IB

- The previously reported issue where Motor #3 exhibited a 2-3 second lag could not be reproduced.
- Various motor sequences were tested, with all motors spinning up immediately.

### Motor Test Sequences & Results

| Test # | Sequence | Result |
| 1 | #1, #2, #3, #4 | All motors started immediately (required two clicks to start) |
| 2 | #1, #2, #3, #4 | All motors started immediately (required two clicks to start) |
| 3 | #2, #1, #3, #4 | Initial motor command caused webpage refresh |
| 4 | #2, #1, #3, #4 | All motors started immediately |
| 5 | #3, #1, #2, #4 | Initial motor command caused webpage refresh |
| 6 | #3, #1, #2, #4 | All motors started immediately |
| 7 | #4, #1, #2, #3 | All motors started immediately |
| 8 | #4, #1, #2, #3 | All motors started immediately |

### Observations:

- Instances where the webpage refreshed appeared to be caused by issuing commands too quickly.
- No significant delays or abnormalities were observed across the motor tests.

FYSA @Cameron Chapman @David Grosher

### Christa Meck, 2025-08-05

@Steve Gonzales  and/or @Pat Wells What is the status of this investigation?
Leaving open until 12 Aug for feedback.

### Steve Gonzales, 2025-08-05

@Christa Meck Hi, see top of page. status and plan sections have been updated.

### Pat Wells, 2025-08-05

@Drew Hildreth @Jackson Riley Curvin @Alexander Alan Arnold See below from Christa
Please advise and close out if necessary.

### Drew Hildreth, 2025-08-20

@Steve Gonzales have you had a chance to work on this?

### Steve Gonzales, 2025-08-20

@Drew Hildreth not yet but we should be able to finish testing by months end.

### Drew Hildreth, 2025-08-21

@Steve Gonzales Can we get the aircraft back and you keep what you need only to continue to investigate this motor. This RMA is ancient and the customer is asking about it.

@Lauren Velasquez FYI

### Steve Gonzales, 2025-08-21

@Drew Hildreth The problem is if an additional motor/esc/pcb is marginal.  If you want to send it back replace all the vtol esc/motors and the vtol pcb and the harness(es) going to the vtol esc/motors.

### Jackson Riley Curvin, 2025-09-16

@Steve Gonzales any updates on this?

### Steve Gonzales, 2025-09-16

@Jackson Riley Curvin Yes, I have been actively working this.  PPT is about 7 days lagging.  So far this is what we know:  #3 motor tested noisy or bad in production re-test. Motor homing is about 186deg. from zero. No delay has been observed with this motor.  125ms standard delay only. Flight Logs are showing 1.2 and a 3.1 sec delay and almost no delay during the landing sequence.  Motors are producing negative current before transitioning, possible some spin, but brake should be latched.  ESC is sensitive to noise.  In addition, known issue with microchip causing delay on the analog comparator in Rev L errata.  I believe we have rev L chips.

### Drew Hildreth, 2025-09-22

@Steve Gonzales How are we looking on this one? This ticket is very old and I am catching a lot of questions from the customer on this? Are we to a point where RMA can have the aircraft back to get ESC’s or Motors replaced. I know you were still trying to nail down what all was effected. 

@Lauren Velasquez FYSA

### Steve Gonzales, 2025-09-22

@Drew Hildreth Hi, see updated notes above from Friday.  It looks like the VTOL had a flag that purposely sent #3 motor to standby/brake state, causing the delay seen.  The motor and esc are not perfect but did not cause the delay.   We ticket needs to go back to FW to understand the logic for control of the A/V.  This does not seem to be a glitch in the code but that is our current state.  I would replace all 4 esc/motor combos and replace the VTOL pcb and sensor inputs to the VTOL, but this will not address the FW control logic.  That may be a long-time FW revision fix.  Note this issue could be upstream of the FW logic and coming from a sensor input.  This behavior is not new.  It was seen in 2023 but not fully recognized or examined.  I see the same issue in the plots from 4/2023, although without plotting the flags or state condition of the vtol, the same motor 3 dark blue goes to standby/brake the flat blue lines near 0.  
[embedded image-20250922-173936.png]

### Drew Hildreth, 2025-09-22

@Steve Gonzales Awesome. Thank you.

### Steve Gonzales, 2025-10-01

@Scott Whitney @Eric Brewer @Drew Hildreth  Hi Eric, this report is ready for you to review.  I believe the flight control command sent to the motor to go to steady state is causing the delay in current seen.  VXE-489 Investigation Report Draft 01.pptx

### Steve Gonzales, 2025-10-27

Report is up to date. Performed setup for flight replay 10/24/25

### Steve Gonzales, 2025-10-28

Completed dyno testing 10/27

### Steve Gonzales, 2025-10-29

Report completed, moved to D4 RCR @Drew Hildreth FYSA @Eric Brewer @Cameron Chapman

### Eric Brewer, 2025-10-29

@Steve Gonzales thanks for running the testing.  I created an associated ticket that we can try to get into the next software release as a corrective action.  @David Grosher @Scott Whitney FYI.
Jira

### David Grosher, 2025-10-29

@Eric Brewer @Steve Gonzales I don’t understand the analysis or the corrective action here, more detail will need to be added to the report to connect the dots, show additional code analysis and follow on testing to confirm the hypothesis.

### Eric Brewer, 2025-10-29

@David Grosher I think slides 20/21 show the relevant dyno data that reproduces delays with the inputs from the flight.  I think more characterization of the exact conditions that recreate the issue and subsequently what can correct the issue will be required.  I think the reproduction is sufficient to move from investigation to corrective actions.

Agree the report needs some consolidation/cleanup to make it more clear.

### Steve Gonzales, 2025-10-30

@David Grosher @Eric Brewer I updated slide 6,9 for clarity.  Improved slide 15.  Added slide 20 for code explanation.

### Cameron Chapman, 2025-11-04

Pasting info that no longer belongs in the plan field. 


10/29/25
Plan to have CA accepted or move to closed D8.  
10/28/25
Plan to update report by 10/28 from completed dyno testing on 10/27.
10/23/25
Plan to do a verification dyno flight profile test on 10/24/25 and 10/27/25 as a first step before considering tuning.  
10/7/25
Plan to review and respond to Eric’s comments by end of week.
9/22/25
Plan to update report and give to FW team for further evaluation. Please notify team when ready to review. 

9/11/25
Plan to possibly add load, lower voltage and retest for motor delay.  Understand if ESC or motor related or neither.  Scope timing from software command to input at esc to output at esc to motor open commutation to closed loop commutation cycle.  Understand if comm related or where the breakdown takes place.

9/2/25
Prepping to test today.
8/20
Plan to test by the end of the month. 
8/5/25
Extending testing to 8/11 to 8/15.  Sharing O-scope with Block 35-40 development and other priorities.
7/23/25
Plan to retest motor this week and send to Magicall afterwards.
7/15/25
Plan to send unit out to Magicall for further troubleshooting by the end of the week.  I may perform one additional test before that.  
7/9/25
Plan to characterize the SPI communication lines between the ESC and Motor (this may be the cause of the delay) by 07/14/25
Some potential causes:
- Task or processor lock up on either the VTOL AP or motor ESC. @Eric Brewer is this possible, or would more tasks lock up/not recover in this case?
- Loose connection in either harness or one of the PCBs. EEs can investigate.
- @Eric Brewer do vbatt and other VTOL AP power signals look normal during this period?

Recommended next step options for aircraft . Discussed with @Eric Brewer and he agrees. 
- If LM operators are comfortable with the motor test page, they could test each motor sequentially, paying close attention to motor 3 to see if there is a lag from the command to the activation, or any other issues. If observed, replace motor assy 3 and see if fixed.  If not, see below.
- Return whole aircraft for inspection and troubleshooting.
- Return just motor assembly 3. Ground that center wing and boom until investigation has more information. I don’t think we have yet proved it is isolated to the motor assembly.

Above steps completed.  Lockheed ran motor tests and saw significant delays on motor 3.  See description here:
https://jenaero.atlassian.net/browse/VXEP-426?focusedCommentId=37781 
Step 1: see if we can reproduce this behavior.  If we can and it is repeatable, we’ll want to go about instrumenting the system to isolate where the motor delay is coming from.
isolate between AP VTOL and Motor 3 ESC 
- Hook up V489 CW to Iron Bird and perform Safety Motor test using webpage 
- If VTOL AP issue then motor 3 should lag on launch 
- VTOL webpage would not load up - potentially SD card issue? 
- fixed by switching to new industrial sd card
- Hook up V489 Booms to Iron Bird and perform Safety Motor test using webpage 
- If Motor 3 is bad then the issue should be replicated
- No issues seen with motor 3. Motor 1 would restart when initially given throttle
- Retest V489 motors and try to replicate issue

### Cameron Chapman, 2025-11-04

Pasting info that no longer belongs in status field. 
10/16/25
Report is up to date. Replied to all comments.
9/19/25
Found flag state(s) in the vtol FW on motor 3 which brought down throttle command to idle before sending it to 93% causing the delay in current draw seen specific to motor 3.  In addition, a general delay has been found from the vtol fw control mixer to at least 3/4 motors after 1957.
[embedded image-20250919-190452.png]
 

9/11/25
#3 motor tested distorted at low speed (THD ~2%) 2x good motor, higher 2nd harmonic, noisier FFT floor, some mechanical imbalance or winding asymmetry possible.  8 captured runs did not cause a delay with manual PWM injection from RC controller direct to ESC.  10+ informal runs did not cause a delay.  High speed harmonics ok.  Delay seen was 125ms, ok.  Need to check if homing is ok. 
8/5/25
Received magnet wire insulation removal tools.
7/21/25
Performed more testing with mixed results.  Not obtaining good conductivity.  Ordered proper tools to remove the insulation on the magnet wire.  
7/15/25
On motor #3, tested back emf on phase AB, AC, and BC.  Found reduced amplitude and waveform distortion all phases.  Possible rotor/magnet issue(s), defect(s) from the OEM.  Possible root cause found for delay seen.   

7/9/25
VTOL motor 3 tested 3x in production per ESC/Motor checkout procedure.  Deemed as a reject due to scratchy noise while running, un-smooth manual operation, different overall tonality while running.  

6/13/25
FW check on ESC initial code check seems ok.  XTAL on ESC PCB measures 15.4Mhz or 15.94Mhz pending confirmation picture and stable through hot and cold.  

5/9/25
Investigating VTOL current delay to PWM output of VTOL pcb to ESC-motors 1-4.  Added slide #9. 

5/22/25
VTOL motor 3 right rear esc may have not gotten programmed incorrectly and that may be why there was a delay on during the flight. Ran motor through production FW checkout test only and no issues were seen.

Motor 3 slow to respond on transition. Cause unknown. See powerpoint here:
https://jenaero.sharepoint.com/:p:/r/sites/FlightSafety/Shared%20Documents/Incident%20Reports/VXE489_TransitionBehavior/AV489_TransitionBehavior.pptx?d=w08391b63f9d74495832b366250a34f71&csf=1&web=1&e=mGlFLj 

VTOL AP board will not boot up to webpage 3/10/25
- Most likely SD card issue 
- Replacing old SD Card with newest one and uploading newest firmware to motor test


- Tested booms on the Iron Bird with Iron Bird’s VTOL Board and did not see an issue with motor 3. However, when initially spinning Motor 1 the ESC would reset and then I was able to command throttle normally. 
- If the VTOL Board connects to the webpage and spins the motors normally, I believe the issue would be isolated down to the ESC/Motor

3/12/25 Morning 
SD card replaced with new Industrial card and is able to boot up webpage. Old SD card is on my (Adrian G) workbench 
- Have not updated Firmware or flashed new SD Card. CW tested on the Iron Bird with Iron Bird’s VTOL motor and each motor spun up normally and expected. I did not see any delay in motor 3 nor did I experience any of the resets I motor 1 had when I initially tested.

3/12/25 1:46 PM
### Update: V489 SD Card and Motor Testing on Iron Bird

- V489 SD Card & Firmware: The SD card was not flashed, and the firmware was not updated.
- Iron Bird Motor Test: The CW was connected to the Iron Bird, and the IB motors were spun. No anomalies were observed, and the issue could not be replicated.

### V489 Motors on IB AP Board

- Motor #1 reset upon the first command but subsequently responded immediately when commanded.
- Motor #3 did not exhibit any issues and could not replicate any previous anomalies.

### V489 CW and ESC/Motors on IB

- The previously reported issue where Motor #3 exhibited a 2-3 second lag could not be reproduced.
- Various motor sequences were tested, with all motors spinning up immediately.

### Motor Test Sequences & Results

| Test # | Sequence | Result |
| 1 | #1, #2, #3, #4 | All motors started immediately (required two clicks to start) |
| 2 | #1, #2, #3, #4 | All motors started immediately (required two clicks to start) |
| 3 | #2, #1, #3, #4 | Initial motor command caused webpage refresh |
| 4 | #2, #1, #3, #4 | All motors started immediately |
| 5 | #3, #1, #2, #4 | Initial motor command caused webpage refresh |
| 6 | #3, #1, #2, #4 | All motors started immediately |
| 7 | #4, #1, #2, #3 | All motors started immediately |
| 8 | #4, #1, #2, #3 | All motors started immediately |

### Observations:

- Instances where the webpage refreshed appeared to be caused by issuing commands too quickly.
- No significant delays or abnormalities were observed across the motor tests.


4/1/25 Has not moved forward; no resources allocated.

### Cody Smisek, 2025-11-18

@Jacob Troyer @Drew Hildreth cases are over in engineering, can it be returned to RMA?

### Drew Hildreth, 2025-11-18

@Cody Smisek I have the report for that aircraft too. I am good with it going back to RMA.

### Everett Werner, 2026-02-17

I was able to cause a vxe30 esc and motor to fail to start with the following throttle input:
[embedded image-20260217-230747.png]
I tried again later in the day and could not get it with the same level of regularity. I recommend the next motor that has this issue be given to engineering for testing and hopeful replication on the dyno stand. It is worth noting that this isnt the exact same profile as we see in flight as the motor isnt delayed but not starting at all.

### Everett Werner, 2026-02-20

NCR List - AC 995 - Flight Test - Abnormal transition

### Eric Brewer, 2026-05-05

Incident investigation is closed.  Root cause analysis/corrective actions for the slow motor startup are ongoing but this investigation is closed.

## Attachments (13)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V489_240604_094404_pack.zip | archive | 2281 | 2024-06-06 | listed only |
| T95_V489_240605_084654_pack.zip | archive | 1727 | 2024-06-06 | listed only |
| [VXE489 June 4 Investigation (065c2f8f-3d9f-4157-9e2a-6aa99178f345).pptx](attachments/20866_VXE489%20June%204%20Investigation%20(065c2f8f-3d9f-4157-9e2a-6aa99178f345).pptx.md) | pptx | 17359 | 2024-06-07 | converted |
| [VXE489 June 5 Investigation (2f128297-62ae-4103-9a8c-855647f0ca62).pptx](attachments/20865_VXE489%20June%205%20Investigation%20(2f128297-62ae-4103-9a8c-855647f0ca62).pptx.md) | pptx | 43731 | 2024-06-07 | converted |
| image-20240618-175437.png | image | 61 | 2024-06-18 | listed only |
| T95_V489_240625_113334_pack.zip | archive | 1870 | 2024-06-27 | listed only |
| image-20240828-190117.png | image | 627 | 2024-08-28 | listed only |
| MicrosoftTeams-video.mp4 | video | 4119 | 2025-03-10 | listed only |
| good back emf.png | image | 76 | 2025-07-15 | listed only |
| waveform disturbance back emf.png | image | 94 | 2025-07-15 | listed only |
| image-20250922-173936.png | image | 81 | 2025-09-22 | listed only |
| image-20250919-190452 (9c8ca7cf-53e2-4748-af48-6cafbe1da696).png | image | 27 | 2025-11-04 | listed only |
| image-20260217-230747.png | image | 111 | 2026-02-17 | listed only |
