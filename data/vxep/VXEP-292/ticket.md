# VXEP-292: VXE-477 Crash on take off

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-02-29
- **Updated:** 2026-08-14
- **Resolved:** 2025-02-21
- **Reporter:** Pat Wells
- **Assignee:** Eric Brewer
- **Creator:** Pat Wells
- **Labels:** Airspeed-Cal, GCS, MARSOC, Training, Weekly-incident-tracker
- **Links:** relates to FS2-1673 (v477 Incident Investigation); relates to FS2-1751 (v477 Investigation (Crash after transition to FW flight)); relates to VXEP-368 (VXE 523 multiple faults with HLB discharging while in fuel cell configuration); relates to RMA-331 (VXE-477 RMA 240829); relates to FS2-2390 (VXEP-292 Crash on take off); is fixed by GCSS-368 (Add delay in the LW between shielding and testing the pitot); relates to SMUP-43 (Evaluate Manuals for accurate pitot calibration procedure); relates to GCSS-465 (Update GCS software to force delay time in between pressure and shield steps, or change order of steps.)
- **Customer:** MARSOC
- **Vehicle Tail Number:** 477
- **Corrective Action:** Be sure to follow preflight procedures and shield pitot during ‘shield pitot’ step. @Josh Burrell
- **Problem Type:** Other (explain in description)
- **Issue Status:** Investigation completed.
- **Incident Type:** Aircraft Loss
- **Severity:** 1 - Flight Critical

## Description

Event occurred at an OCONUS deployed location with MARSOC
Summary of incident as reported:
“They had finished a flight, swapped batteries and attempted to launch again and during that second launch attempt it failed and came down hard.
The way the operator described the attempted launch was as if the aircraft was overweight, significantly, as it had a slow ascent, to an arrested ascent, then finally started to descend back down to the ground. He did not describe the amount of damage and tried to get him to pull the logs but he sent me the GCS data only and then as a follow-up was just the flight datalog, excel with the logfile of the days the aircraft flew. The reported date was around the 12th of Feb. “
 
Damage:
Aircraft and payload are a total loss.
Working with customer to obtain usable flight data logs
Received data logs on 3/29

I made contact with the on-site Precision FSR. Turns out he mislabeled the file and it was in fact from v477.
To clear up the confusion on the date. The actual crash occurred on 2/27. Apparently the confusion was that the operator had a similar event on 2/12 but did not crash and continued to use the v477 up until the crash on 2/27.

## Plan

None - Investigation completed.
Complete slides for release to customer.

## Root Cause

Low airspeed measurement caused vehicle to fly too fast, resulting in not enough thrust to stay airborne.  User error caused pitot pressure to be applied during the shielding step, resulting in an incorrect pitot calibration.

## Comments (61)

### Pat Wells, 2024-12-12

@Ted Trowbridge @David Grosher have we determined if this was operator error or a fault on our end?
@Alexander Alan Arnold  FYSA

### Greg Fryer, 2024-12-12

@Ted Trowbridge AV 477 is still on the Engineering floor. Do you need it to support corrective actions, or can we recreate/verify on HIL or with an asset AV? If yes, we can return to RMA  and they can return to user.
@Rodney Linch @Pat Wells @Cody Smisek FYI.

### Ted Trowbridge, 2024-12-12

@Greg Fryer @Pat Wells @David Grosher @Eric Brewer 
Moving back to D4 - Investigating Root Cause due to LW calibration issue not fully explaining the issue.  I will pick the investigation back up today.

### Ted Trowbridge, 2024-12-12

After investigating, I do not believe the root cause was a GCS launch wizard calibration issue.  There are two calibrations seen in the XCOMM log that are consistent with expected behavior during preflight.
XCEVLOG.TXT Excerpt: 1st Calibration
```
[14:09:54.546 909.547] DebugMsg SEND CAL          <-- LW Calibrate Page Activated (RCS_CAL)
...
[14:10:04.956 919.956] DebugMsg SEND AIRDATA CAL  <-- LW Calibrate Button Pressed (COMMAND_AZ)
```
The XCL00223.CSV logs show airspeed dropping from ~5FPS prior to calibration to 0FPS after calibration, and a subsequent large increase during pitot test.  The pitot test did appear to have been a long press (30 seconds).  Following the pitot test, airspeed returned to 0FPS and the second calibration and launch occurred:
XCEVLOG.TXT Excerpt: 2nd Calibration, Launch, Crash
```
[14:11:36.955 1011.955] DebugMsg SEND CAL         <-- 2nd LW Calibrate Page Activated (RCS_CAL)
...
[14:11:45.297 1020.297] DebugMsg SEND AIRDATA CAL <-- 2nd LW Calibration Button Pressed (COMMAND_AZ)
...
[14:14:07.729 1162.729] ap dbg: arm command       <-- Launch commanded 2m22s after 2nd calibrate
[14:14:07.730 1162.730] ap dbg: Launch Armed
[14:14:07.734 1162.735] ap dbg: VTOL Launch Armed
...
[14:17:34.216 1369.216] ap dbg: airspeed fault detected <-- Vehicle crashes, airspeed fault and landing detected
[14:17:34.247 1369.247] sw 1 port link reset 2
[14:17:34.249 1369.251] sw 1 port link reset 4
[14:17:36.372 1371.373] sw 2 port rx reset 5
[14:17:36.373 1371.373] ave, flow 2784699  0
[14:17:37.145 1372.145] landing detected
```
With XCOMM log events only written at 0.1Hz during preflight, it’s not possible to completely rule out operator error (improper pitot shielding) during calibration due to airspeed readings being 10s apart and no data at the exact time of calibration.
I’ve been unable to reproduce the issue on the HIL by injecting airspeed faults during calibration, but I think we need to do additional testing on the speedgoat HIL to be confident.
If we confirm an operator shielding error can produce this issue in the HIL a GCS corrective action may be appropriate to detect and warn the operator.
@David Grosher @Eric Brewer

### Ted Trowbridge, 2024-12-12

It also appears that after crashing XCOMM continued running for almost 12 hours and had latched an airspeed value that caused it to spam the logs with “launch detected” and sometimes “landing detected”.  As a result, the XCL----.CSV ballooned up to 400MB (normally peaks at 4-5MB) and the FLTFILES.txt has 35,374 entries

### Eric Brewer, 2024-12-16

@Ted Trowbridge thanks for taking a look at this.  After reviewing your summary and the VTOL logs, I believe this was user error.  The most likely cause is the user pushing pitot during the ‘shield’ step.  See slide 7 of the investigation here.  
I was also able to run a HIL test and reproduce a similar crash.

### Pat Wells, 2025-01-03

@Eric Brewer & @Ted Trowbridge  can we confirm that this was user error and reflect accordingly in the investigation report?

@Rodney Linch @Alexander Alan Arnold FYSA

### Eric Brewer, 2025-01-03

@Pat Wells confirmed that’s our best guess.  I added a conclusion slide to the end of the investigation. @Ted Trowbridge @Alexander Alan Arnold

### Josh Burrell, 2025-01-07

@Dana Holley Can you please make sure we add a Caution to the OPS manual about ensuring the Piot test is completed correctly? I think that will satisfy the corrective action.

### Josh Burrell, 2025-01-08

This was taken care of in another ticket that @David Grosher assigned to review the manual. Dana added some verbiage to clarify the check. @Pat Wells can we close this ticket now?

### Alexander Alan Arnold, 2025-01-10

@Pat Wells Please recommend next step after reviewing information

### Pat Wells, 2025-01-10

@Alexander Alan Arnold we need to review the final report and release it to customer as operator error. 
Otherwise this looks like it’s ready to close since the CA has been implemented.
FYI there is also an opon RMA on this so we will need to address the issue of funding a repair with the customer.

### Alexander Alan Arnold, 2025-01-10

@Eric Brewer @Ted Trowbridge Can we clean up the final report so we can brief the customer on this item?

### Eric Brewer, 2025-01-10

@Alexander Alan Arnold done.
@Ted Trowbridge FYI.

### Alexander Alan Arnold, 2025-01-10

@Pat Wells Please review report

### Eric Brewer, 2025-02-03

@Josh Burrell given this was a training issue can you look into updating our training procedures to help educate operators on push vs. shield pitot?
@David Grosher @Jason Scherer FYI.

### Josh Burrell, 2025-02-04

@Eric Brewer we have the publications piece of the puzzle but don’t have much to do with the training. I’m going to tag @Gregory Nichols and @Grace Burgess as they’re the ones that would have to implement something for training and then push that change to us in Tech Pubs to incorporate into the OPS manual. @Dana Holley FYSA

### Pat Wells, 2025-02-04

@Eric Brewer @David Grosher @Jason Scherer @Gregory Nichols @Grace Burgess @Dana Holley @Josh Burrell 
This is a customer training issue.  We currently do not train Marines. 
Please clean up the final report in the proper format and we will pass along to the customer for their action.

@Alexander Alan Arnold  FYSA

### Eric Brewer, 2025-02-04

@Pat Wells updated report here.  AV477_crash.pptx  Let me know if you need anything else.
@David Grosher @Jason Scherer @Gregory Nichols @Grace Burgess @Dana Holley @Josh Burrell

### Pat Wells, 2025-02-21

Report sent to customer.
Corrective actions complete: Update training and ops manual.

### Artis Bertulis, 2024-04-18

Do we know what kind of payload they were running? Maybe it was overweight or CG was off having the VTOL system struggle.
As far as pre-flight air-data checks @Cameron Chapman we only do pitot calibration and pitot press, but the way the software is built it would allow to proceed with the launch even if there was an issue (if after calibration altitude isn’t close to 0, or if during pitot check there’s an air leak). That being said, I don’t think that has ever caused an issue. For SCO flights we manually confirm that the pitot calibration actually “zeros” the altitude, gyros, and IAS in the “Sensor Status” window, customers are not required to do so.
Also, note on the AS150 connectors, I’d say that’s how most of them look nowadays, I walked around and took some pictures of brand-new aircraft connectors in the SCO area, and here’s how they are looking like @Laszlo Juhasz @Connor Peebles :

[embedded image-20240418-144805.png]

[embedded image-20240418-144823.png]

[embedded image-20240418-144839.png]

### David Grosher, 2024-04-18

@Eric Brewer The event log on a new log startup will print date and time. I then use UTC/RTC time to identify the correct CSV file.

### Eric Brewer, 2024-04-18

@Artis Bertulis @Cameron Chapman there was no evidence in the logs that the climb was slow.  10fps is typical from other logs I’ve looked at, and the change in altitude is consistent with the 10fps.  It’s possible they were referring to the climb in the fixed-wing mode.  In this case it makes sense it would climb slow since it was overspeeding.

[embedded image-20240418-160458.png]

### Cameron Chapman, 2024-04-18

@Eric Brewer can you please start an investigation file and link it in the description? 
- Below you mentioned that airspeed looked normal, but then you said it was over speeding. Do all sensors indicate overspeeding, or was there a disagreement?
- Can we determine why it was over speeding? Ex: Commanded speed vs actual.
- Can you please update the fields above as each investigation proceeds?
- Ex: should one of the corrective actions be to RTB or land if speed sensors disagree (GPS, air data, etc)?

### Eric Brewer, 2024-04-18

@Cameron Chapman see link in “Issue Status” above, that should answer most of your questions.
- The airspeed sensor was not reading correctly, this does not impact VTOL flight since it is using GPS velocity at this time
- See above
- Fields are already updated with status.  Sensing a disagreement in airspeed/groundspeed is harder to do because they often disagree frequently during flight due to wind.  We could certainly write something to do this.  Do we know how often we see this type of issue?

### Eric Brewer, 2024-04-30

@Cameron Chapman @David Grosher @Jason Scherer @Kurt Burian FYI, I added a couple slides at the end of the ppt.  We saw a similar issue occur on VXE-523 (linked above).  In both cases, it looks like the pitot zero was run with pressure applied to the pitot system.  
The preflight procedure includes a step where we shield the pitot and zero its value, and then the next step pressure is applied.  I find it a little suspicious that these both occurred with the new software, so I’m wondering if perhaps there is a delay somewhere in the system with the new software where the calibration command is not being sent to the VTOL autopilot to execute until a bit after it is commanded.  It’s difficult to tell precisely in the logs (~10s log period), but at least within the log period it looks like the VTOL AP is applying the calibration when the command is sent from xcomm.  Could there be delays either in when the GCS command makes it to xcomm or when xcomm is sending the command to vtolap?

### Eric Brewer, 2024-04-30

@Cameron Chapman @David Grosher @Jason Scherer @Kurt Burian , if we have someone that can run a quick test I linked a quick procedure (no SW changes) that should work to determine if there is significant delay between calibration request and when it is applied.  If it turns out there is, we can repeat the test with an older version of the software to see if the change was inadvertently introduced with the latest release.

### Cameron Chapman, 2024-05-17

@Cody Smisek @Ruysser Gabler or @Artis Bertulis are you available to run this quick procedure if you have some spare time with an aircraft? See test procedure here.

### Artis Bertulis, 2024-05-17

@Cameron Chapman we don’t have an asset airplane to try this with. There might be availability to use vehicle 300 in engineering, we can either help using that or you can task someone from over there to try this - let me know.

### Cameron Chapman, 2024-05-17

@Gary Angelus this would be a good training exercise. Can you please coordinate finding someone available to train, setting up and performing this procedure?

### Gary Angelus, 2024-05-17

Sure, will do.

### Gary Angelus, 2024-05-20

Hi Eric, tried to read the AAR attached above but apparently the file format is not compatible with the Flight Data Analisys tool.  Liam tells me his tool works better with the original AAR format.  Can you supply a copy?

### Eric Brewer, 2024-05-20

@Gary Angelus Unfortunately I’m not aware that another format was provided by the customer.  I did try putting one of the raw vtol files into dash but that didn’t work either.
I was able to plot it with MATLAB.  If you need something specific let me know and I’m happy to make some plots with MATLAB, otherwise if you’re looking for a more long term solution we may need to update Liam’s tool to be able to read these logs.

### Gary Angelus, 2024-05-21

Pitot calibration test preformed on engineering asset v300 per Pitot Quick Test plan, Pitot calibration completed within one second.  Test log attached.
Test performed with Raj’s assistance.
 
[embedded file]

### Eric Brewer, 2024-05-23

Thanks @Gary Angelus ,
I got a hold of Ruysser and Artis yesterday afternoon and they were able to run a quick test on AV300.  I updated the results in the pitot quick test document.  Unfortunately the fast logging trigger was only set off once so I was only able to get one data point but it appeared within expected ranges.  I’ll ask the flight test team if they’re able to repeat the test today, if not we can try again Friday.
PitotQuickTest.docx (sharepoint.com)
If similar test results hold I think the right courses of action are:
Short term: issue operator caution to all VXE operators to ensure that operators wait 5 seconds between sending the calibration command and applying pressure
Long term: Add a wait to the GUI and/or change the order of when shield and pressure tests are done.

### Eric Brewer, 2024-05-23

@Gary Angelus @David Grosher @Pat Wells See additional test results in the quick test document.  It looks like the calibration is applied within 0.5-1s as far as we can tell.  This means that if an operator is quick, they could potentially have someone apply pressure just before the calibration takes.  I don’t see any evidence of obnoxious delays from the GCS, although I suppose they could certainly be possible if windows or any of the autopilot software happens to be busy.  
For now I’ll stick by my short term/long term recommendations below.

### Eric Brewer, 2024-08-27

@Pat Wells @David Grosher @Gary Angelus created https://jenaero.atlassian.net/browse/FS2-2204 .  
In the meantime if we need to get back to the customer we can let them know to make sure they are allowing extra time in between the pressure and shield steps to ensure proper airspeed calibration.  Let me know if you need anything else.

### Sean Odell, 2024-09-13

@David Grosher Aircraft went through induction and now in Engineering awaiting your next steps. 
@Pat Wells FYSA

### David Grosher, 2024-09-24

@Ted Trowbridge GCS CAs above.

### Alexander Alan Arnold, 2024-12-10

@Ted Trowbridge Is this still in D6 or can it be closed?

### Ted Trowbridge, 2024-12-10

@Alexander Alan Arnold Still in D6, the corrective action suggested would not resolve the issue.  Needs more investigation.

### Pat Wells, 2024-12-12

@Ted Trowbridge @David Grosher have we determined if this was operator error or a fault on our end?
@Alexander Alan Arnold  FYSA

### Greg Fryer, 2024-12-12

@Ted Trowbridge AV 477 is still on the Engineering floor. Do you need it to support corrective actions, or can we recreate/verify on HIL or with an asset AV? If yes, we can return to RMA  and they can return to user.
@Rodney Linch @Pat Wells @Cody Smisek FYI.

### Ted Trowbridge, 2024-12-12

@Greg Fryer @Pat Wells @David Grosher @Eric Brewer 
Moving back to D4 - Investigating Root Cause due to LW calibration issue not fully explaining the issue.  I will pick the investigation back up today.

### Ted Trowbridge, 2024-12-12

After investigating, I do not believe the root cause was a GCS launch wizard calibration issue.  There are two calibrations seen in the XCOMM log that are consistent with expected behavior during preflight.
XCEVLOG.TXT Excerpt: 1st Calibration
```
[14:09:54.546 909.547] DebugMsg SEND CAL          <-- LW Calibrate Page Activated (RCS_CAL)
...
[14:10:04.956 919.956] DebugMsg SEND AIRDATA CAL  <-- LW Calibrate Button Pressed (COMMAND_AZ)
```
The XCL00223.CSV logs show airspeed dropping from ~5FPS prior to calibration to 0FPS after calibration, and a subsequent large increase during pitot test.  The pitot test did appear to have been a long press (30 seconds).  Following the pitot test, airspeed returned to 0FPS and the second calibration and launch occurred:
XCEVLOG.TXT Excerpt: 2nd Calibration, Launch, Crash
```
[14:11:36.955 1011.955] DebugMsg SEND CAL         <-- 2nd LW Calibrate Page Activated (RCS_CAL)
...
[14:11:45.297 1020.297] DebugMsg SEND AIRDATA CAL <-- 2nd LW Calibration Button Pressed (COMMAND_AZ)
...
[14:14:07.729 1162.729] ap dbg: arm command       <-- Launch commanded 2m22s after 2nd calibrate
[14:14:07.730 1162.730] ap dbg: Launch Armed
[14:14:07.734 1162.735] ap dbg: VTOL Launch Armed
...
[14:17:34.216 1369.216] ap dbg: airspeed fault detected <-- Vehicle crashes, airspeed fault and landing detected
[14:17:34.247 1369.247] sw 1 port link reset 2
[14:17:34.249 1369.251] sw 1 port link reset 4
[14:17:36.372 1371.373] sw 2 port rx reset 5
[14:17:36.373 1371.373] ave, flow 2784699  0
[14:17:37.145 1372.145] landing detected
```
With XCOMM log events only written at 0.1Hz during preflight, it’s not possible to completely rule out operator error (improper pitot shielding) during calibration due to airspeed readings being 10s apart and no data at the exact time of calibration.
I’ve been unable to reproduce the issue on the HIL by injecting airspeed faults during calibration, but I think we need to do additional testing on the speedgoat HIL to be confident.
If we confirm an operator shielding error can produce this issue in the HIL a GCS corrective action may be appropriate to detect and warn the operator.
@David Grosher @Eric Brewer

### Ted Trowbridge, 2024-12-12

It also appears that after crashing XCOMM continued running for almost 12 hours and had latched an airspeed value that caused it to spam the logs with “launch detected” and sometimes “landing detected”.  As a result, the XCL----.CSV ballooned up to 400MB (normally peaks at 4-5MB) and the FLTFILES.txt has 35,374 entries

### Eric Brewer, 2024-12-16

@Ted Trowbridge thanks for taking a look at this.  After reviewing your summary and the VTOL logs, I believe this was user error.  The most likely cause is the user pushing pitot during the ‘shield’ step.  See slide 7 of the investigation here.  
I was also able to run a HIL test and reproduce a similar crash.

### Pat Wells, 2025-01-03

@Eric Brewer & @Ted Trowbridge  can we confirm that this was user error and reflect accordingly in the investigation report?

@Rodney Linch @Alexander Alan Arnold FYSA

### Eric Brewer, 2025-01-03

@Pat Wells confirmed that’s our best guess.  I added a conclusion slide to the end of the investigation. @Ted Trowbridge @Alexander Alan Arnold

### Josh Burrell, 2025-01-07

@Dana Holley Can you please make sure we add a Caution to the OPS manual about ensuring the Piot test is completed correctly? I think that will satisfy the corrective action.

### Josh Burrell, 2025-01-08

This was taken care of in another ticket that @David Grosher assigned to review the manual. Dana added some verbiage to clarify the check. @Pat Wells can we close this ticket now?

### Alexander Alan Arnold, 2025-01-10

@Pat Wells Please recommend next step after reviewing information

### Pat Wells, 2025-01-10

@Alexander Alan Arnold we need to review the final report and release it to customer as operator error. 
Otherwise this looks like it’s ready to close since the CA has been implemented.
FYI there is also an opon RMA on this so we will need to address the issue of funding a repair with the customer.

### Alexander Alan Arnold, 2025-01-10

@Eric Brewer @Ted Trowbridge Can we clean up the final report so we can brief the customer on this item?

### Eric Brewer, 2025-01-10

@Alexander Alan Arnold done.
@Ted Trowbridge FYI.

### Alexander Alan Arnold, 2025-01-10

@Pat Wells Please review report

### Eric Brewer, 2025-02-03

@Josh Burrell given this was a training issue can you look into updating our training procedures to help educate operators on push vs. shield pitot?
@David Grosher @Jason Scherer FYI.

### Josh Burrell, 2025-02-04

@Eric Brewer we have the publications piece of the puzzle but don’t have much to do with the training. I’m going to tag @Gregory Nichols and @Grace Burgess as they’re the ones that would have to implement something for training and then push that change to us in Tech Pubs to incorporate into the OPS manual. @Dana Holley FYSA

### Pat Wells, 2025-02-04

@Eric Brewer @David Grosher @Jason Scherer @Gregory Nichols @Grace Burgess @Dana Holley @Josh Burrell 
This is a customer training issue.  We currently do not train Marines. 
Please clean up the final report in the proper format and we will pass along to the customer for their action.

@Alexander Alan Arnold  FYSA

### Eric Brewer, 2025-02-04

@Pat Wells updated report here.  AV477_crash.pptx  Let me know if you need anything else.
@David Grosher @Jason Scherer @Gregory Nichols @Grace Burgess @Dana Holley @Josh Burrell

### Pat Wells, 2025-02-21

Report sent to customer.
Corrective actions complete: Update training and ops manual.

## Attachments (20)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 38CA8A62-77A0-4B3F-90D7-8B419CC04C4F.jpeg | image | 1166 | 2024-03-01 | listed only |
| 4031020D-16C5-4549-86C9-22B4FABB0F80.jpeg | image | 1432 | 2024-03-01 | listed only |
| 8408D3F1-6A83-4286-833B-0F8AA53D510A.jpeg | image | 1186 | 2024-03-01 | listed only |
| IMG_4064.JPG | image | 1337 | 2024-03-01 | listed only |
| IMG_4065.JPG | image | 1468 | 2024-03-01 | listed only |
| IMG_4066.JPG | image | 1311 | 2024-03-01 | listed only |
| IMG_4067.JPG | image | 494 | 2024-03-01 | listed only |
| IMG_4068.JPG | image | 583 | 2024-03-01 | listed only |
| IMG_4069.JPG | image | 892 | 2024-03-01 | listed only |
| IMG_4070.JPG | image | 1122 | 2024-03-01 | listed only |
| image-20240305-185946.png | image | 173 | 2024-03-05 | listed only |
| IMG_4353.jpeg | image | 1764 | 2024-03-29 | listed only |
| IMG_4354.jpeg | image | 2643 | 2024-03-29 | listed only |
| VTOL_VXE477.zip | archive | 59934 | 2024-03-29 | listed only |
| XCOMM_VXE 460.zip | archive | 62560 | 2024-03-29 | listed only |
| image-20240418-144805.png | image | 288 | 2024-04-18 | listed only |
| image-20240418-144823.png | image | 398 | 2024-04-18 | listed only |
| image-20240418-144839.png | image | 262 | 2024-04-18 | listed only |
| image-20240418-160458.png | image | 73 | 2024-04-18 | listed only |
| T95_V300_240520_160556_pack.zip | archive | 2549 | 2024-05-21 | listed only |
