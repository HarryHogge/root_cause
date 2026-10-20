# VXEP-274: VXE 438 Lift motor failure resulting in crash

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-02-14
- **Updated:** 2026-09-14
- **Resolved:** 2025-05-20
- **Reporter:** Pat Wells
- **Assignee:** Pat Wells
- **Creator:** Pat Wells
- **Labels:** Crash, PMA263, Software, Weekly-incident-tracker
- **Links:** relates to RMA-219 (VXE-438 240226); relates to VA-1311 (VXE-438 Lift motor failure resulting in crash); relates to FS2-3286 (Review and update max pause duration during descent. Coordinate with software to implement. ); relates to VA-93 (Record typical, max, and max tested lift current and voltage profiles. Save test data to confluence. Establish and implement limits and abort if exceeding.)
- **Impact:** Significant / Large
- **Customer:** PMA263
- **Vehicle Tail Number:** 438
- **Other Stakeholder (as required):** Rajesh Budhabhatti
- **Plan:** Investigation complete. Reports could be improved. Next step, implement corrective actions.
- **Severity:** 1 - Flight Critical

## Description

https://jenaero.sharepoint.com/sites/FlightSafety/Shared%20Documents/Forms/AllItems.aspx?newTargetListUrl=%2Fsites%2FFlightSafety%2FShared%20Documents&viewpath=%2Fsites%2FFlightSafety%2FShared%20Documents%2FForms%2FAllItems%2Easpx&isAscending=false&id=%2Fsites%2FFlightSafety%2FShared%20Documents%2FIncident%20Reports%2FVXE%2D438%20Lift%20motor%20failure%20resulting%20in%20crash&sortField=Modified&viewid=7181a7a2%2Dd286%2D47c9%2Dbdd3%2D9195ef18282c 
Investigation Summary: VXE-438-Lift Motor Failure-Investigation Summary.pptx
Investigation Report VXE-438 Lift Motor failure crash.docx'
Limited information as stated by customer:
A lift motor failed that resulted in significant damage to the AV
AAR files attached
Working with customer on potential return of ACFT for investigation

After a successful flight with no issues, the air vehicle (AV) was commanded to Return to Base (RTB). The last
portion of this event is to have the student use the Manual Nudge function of the AV, again with no issue. The AV
was placed back into Postion Nudge function and was 20 ft AGL and decending when it appeared that the front left
rotor stopped spinning causing the AV to violently pitch down and to the left, striking the ground. The were no
injuries to personnel however the AV appears to be a complete loss

## Corrective Action

- Landing and take-off should be limited to 45s and 30s respectively. If the operator issues extended pauses, the motors should run at PWM value of about 1300-1350. This PWM value translates to motor force needed to counter the gravitational force exerted on a 55lbs drone. Motors can be operated at 50% throttle for 100s max. Operating ESCs above 95% throttle (PWM=1812) for extended periods (20s+) should be avoided. VTOL PID control routine could use some damping.

https://jenaero.atlassian.net/browse/VA-1561 
- Consider providing HILs or other simulation to trainers, so that they could practice hovers and nudges without using an actual HIL.
- Update training documents to ensure pause/nudge duration is an emergency procedure only and is limited  See https://jenaero.sharepoint.com/:w:/r/sites/FlightSafety/Shared%20Documents/Incident%20Reports/VXE-438%20Lift%20motor%20failure%20resulting%20in%20crash/VXE-30%20Absolute%20maximum%20Pause%20duration.docx?d=w80e33a178fcc489495bd50d5da322b56&csf=1&web=1&e=0qZXg4. Could either set based on power level, or just list a conservative limit. 
- https://jenaero.atlassian.net/browse/VXEP-564
- Send out customer notification of the guidance to ensure pause/nudge duration is an emergency procedure only and is limited Done. Advisory Notice 24-003

## Issue Status

- See the results here: Investigation Report VXE-438 Lift Motor failure crash.docx
- VXE-438 underwent extended pauses. When replicating the throttle profiles from crash on working ESCs we observed similar failures of ESCs. ESC wires would overheat and make the solder melt. When the ESC cooled down, the solder made a substandard connection to the board again.
- The current report proves that this aircraft hovered at too high power for too long. Next steps are to determine why it was hovering at such high power, and to implement auto abort limits.

## Root Cause

- The current report seems to prove that this aircraft hovered at too high power for too long. Next steps are to determine why it was hovering at such high power, and to implement auto abort limits.
- 4/23/23: Flight log shows extended pause subjecting lift motors to remain at high power for about 240 seconds. Dyno tests of landing profile performed on stock lift motors caused the ESC to heat up to the level where the power conductors came unsoldered after ~50 seconds.. Tests were repeated on multiple ESCs and similar results observed. Details of investigation and tests can be found in the investigation report. 
- A typical VTOL landing is about 45 seconds at about 50% throttle depending on the wind condition. AAR data on this flight shows that the student was practicing the nudge function and had the aircraft in hoover condition for nearly 240 seconds or about 5-6 time the normal condition where the VTOL motor was operating at 70% the throttle. Flight log also indicated that it was moderately windy day (19 kts) and AV was trying to land against the wind (wind direction 234˚ while the AV was trying to land at 87˚). This may have caused the AV to operate at higher throttle setting to stabilize.

## Comments (53)

### Pat Wells, 2024-02-14

@David Grosher FYSA

### David Grosher, 2024-02-14

Initial insights, it looks like landing was paused continuously from the start of the descent to the moment the VTOL system failed. About 6 seconds before the VTOL AP stopped logging data the landing pauses were ignored due to low energy. Unfortunately, the datalog stopped about 10 senconds earlier, so I don’t know what the voltage was at that time. It had been at ~25V for a while during the pause. 
@Pat Wells @Cameron Chapman @Greg Fryer FYSA

### David Grosher, 2024-02-14

A bit more context from the XCOMM log, it appears the battery was down to 23.6V at one point. 
[embedded: image-20240214-204501.png]

### Cameron Chapman, 2024-02-14

@David Grosher do we have logic that aborts a pause if the battery gets too low? We should if not. I am out until Friday, but I recommend zooming into the pause timeframe and plotting current, throttles vs expected current, etc. Does it seem like the battery died or that a motor assembly gave out?

### Cameron Chapman, 2024-02-20

Log says it is ignoring the last couple pauses, then log ends. 6 seconds before impact. VTOL log Data log is ~10 seconds behind. XCOM log is all there.

### Cameron Chapman, 2024-02-23

@Rajesh BudhabhattiCan you work on this when you get a chance. I can give you an intro to the process 
See actions above. 
guide here Flight Data Processing and Review - Engineering Function - Confluence

### Rajesh Budhabhatti, 2024-02-23

Yes, love to. I will review the crash data and guide and then reach out to you for an intro on the process.
Thanks Cameron,
Raj
From: Cameron Chapman (Jira) <jira@jenaero.atlassian.net>
Sent: Friday, February 23, 2024 9:41 AM
To: Raj Budhabhatti <rbudhabhatti@edgeautonomy.io>
Subject: [JIRA] Cameron Chapman mentioned you on https://jenaero.atlassian.net/browse/VXEP-274#icft=VXEP-274
You don't often get email from jira@jenaero.atlassian.net<jira@jenaero.atlassian.net>. Learn why this is important<https://aka.ms/LearnAboutSenderIdentification>
Cameron Chapman mentioned you on an issue
VXE Problems/https://jenaero.atlassian.net/browse/VXEP-274#icft=VXEP-274 VXE-438 Lift motor failure resulting in crash  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌
Cameron Chapman mentioned you on an issue
VXE Problems<https://jenaero.atlassian.net/browse/VXEP?atlOrigin=eyJpIjoiYWIwNDlkZjFmMjZhNDdjNDhhZWRkOTliM2Y3NGFlNDUiLCJwIjoiaiJ9>
/
VXEP-274<https://jenaero.atlassian.net/browse/VXEP-274?atlOrigin=eyJpIjoiYWIwNDlkZjFmMjZhNDdjNDhhZWRkOTliM2Y3NGFlNDUiLCJwIjoiaiJ9>
VXE-438 Lift motor failure resulting in crash <https://jenaero.atlassian.net/browse/VXEP-274?atlOrigin=eyJpIjoiYWIwNDlkZjFmMjZhNDdjNDhhZWRkOTliM2Y3NGFlNDUiLCJwIjoiaiJ9>
https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5dca22ba8365670de7e8a759/a707d30b-73bb-45f2-82ad-d614f7f8fce1/128
Cameron Chapman 9:40 AM PST
@Rajesh BudhabhattiCan you work on this when you get a chance. I can give you an intro to the process
See actions above.
guide here Flight Data Processing and Review - Engineering Function - Confluence<https://jenaero.atlassian.net/wiki/spaces/EF/pages/13467649/Flight+Data+Processing+and+Review>
[View issue]
Get Jira notifications on your phone! Download the Jira Cloud app for Android<https://play.google.com/store/apps/details?id=com.atlassian.android.jira.core&referrer=utm_source%3DNotificationLink%26utm_medium%3DEmail> or iOS<https://itunes.apple.com/app/apple-store/id1006972087?pt=696495&ct=EmailNotificationLink&mt=8>.
Manage notifications<https://jenaero.atlassian.net/jira/settings/personal/notifications?emailPreferences=true&atlOrigin=eyJpIjoiYWIwNDlkZjFmMjZhNDdjNDhhZWRkOTliM2Y3NGFlNDUiLCJwIjoiaiJ9#emailpreferences>  •  Give feedback<https://surveys.atlassian.com/jfe/form/SV_9X3zi1X4q1gKsqF>  •  Privacy policy<https://www.atlassian.com/legal/privacy-policy>
[cid:image002.png@01DA663D.21575260]
[cid:image002.png@01DA663D.21575260]
- - WARNING: This email originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe. **

### Rajesh Budhabhatti, 2024-02-26

Hi Cameron, I have compiled the VXE-438 data in a sharepoint folder and started editing the word/ppt templates. I can use some help figuring out how to use the flight data analysis tool. LMK if you have a moment to show me how to use it. Thank you. Sharepoint link here: Flight Safety - VXE-438 Lift motor failure resulting in crash - All Documents (sharepoint.com)

### Cameron Chapman, 2024-02-27

@Rajesh Budhabhatti this aircraft arrived today. @Sean Odell will perform receiving inspection and deliver to engineering. We can start by inspecting power connections and ESCs. 

Some indication of ESC2 failure (front right) Can you please post to the report altitude and current on the same plot with the same timeline below this?
[embedded: image-20240227-191956.png]

### Rajesh Budhabhatti, 2024-02-27

Excellent! Will do. Thanks.

### Rajesh Budhabhatti, 2024-03-06

I did some more analysis on power, current and throttle states, comparing the calculated and actual current. Two current peaks seems to match the observed and calculated peaks based on throttle states. Current peaks in as high as 200A+ were observed and matched the calculations. Between UTC 1959-2052, for about a minute and half (93 sec) VXE-438 experienced power draw in excess of 84Wh. (I will calculate exact power if further investigation is required). Also, between UTC 2068 & 2166 VXE-438’s throttle 2 remained at 0.76 while other three were considerably low. This could have flipped the craft and caused a crash. Excessive current could have caused the throttle 2 malfunction resulting in a crash. Here is my updated investigation report: Investigation template VXE-438 Lift Motor failure crash.docx

### Pat Wells, 2024-03-15

@Rajesh Budhabhatti @Cameron Chapman any updates on this ?
Thanks

### Rajesh Budhabhatti, 2024-03-15

@Pat Wells Hello Patrick, We thoroughly checked this aircraft and did not find anything wrong with the circuitry. All motors were operational and we could connect to fusulage and center wing (Center wing had a different tail number indicating it was swapped) It also appered that customer had done some unauthorized work on the craft. Nose cone was smashed and jammed, both front lift booms were badly damaged. The best guess I have is that the aircraft was stalled for several minutes and caused high current (210A) for extended period of time, This may have caused a failure such that when the operator tried to land the craft, front right lift motor throttle remained high, causing the craft to loose control. It then seemed to topple and crash-land upside down.  We can use some more data from the eye witness to figure out what could have happened.  See the investigation report and flight data analysis here: Investigation template VXE-438 Lift Motor failure crash.docx

### Pat Wells, 2024-03-15

@Rajesh Budhabhatti I have sent a request to the customer for witness statements. 

I see that it was submitted on RMA with center wing serial number: 4031  This would be a “spare” center wing.  Is the wing shown in the data not the same? (4031)

### Rajesh Budhabhatti, 2024-03-15

@Pat Wells Thank you, witness statement will help. Correct. The data shown is for wing serial number 4031.

### Cameron Chapman, 2024-03-19

Hi @Rajesh Budhabhatti , when you have time to work on this again (after MAGNSS and heated pitot), please do the following. 
- Your current plot where it reaches 200A has no duration. Duration is very important to heating and failures. Please add a time axis and compare to this https://jenaero.atlassian.net/wiki/spaces/EE/pages/11272193/Power+and+Temperature+Profiles?search_id=ad7224dc-272b-447e-adc7-acdd497e6158. Summarize current and duration for each current level.
- If the sustained 200A did cause the circuit to fail, it would not heal itself after. The next step may be to run the same current profile on the dyno on a normal ESC, then this ESC to see if either/both survives it without issue.
- Before the abusive profile, we should run a normal take off and landing with the front right ESC to see if it produces normal thrust and efficiency. Is the front right prop functional or damaged?
- Please add findings for these to the report when complete.

### Rajesh Budhabhatti, 2024-03-19

Good Idea. Will do. Both front motor housings are damaged and front right prop destroyed.

### Pat Wells, 2024-03-20

@Rajesh Budhabhatti @Cameron Chapman Added MISHAP report file from operator with statement.

### Rajesh Budhabhatti, 2024-04-02

Adding investigation report: Investigation template VXE-438 Lift Motor failure crash.docx

### Rajesh Budhabhatti, 2024-04-09

Updated Investigation report and added timeline plots, potential causes, fishbone per review actions list. Creating scripts from crash log data files for Dyno system.

### Cameron Chapman, 2024-04-12

Summary of testing Raj performed and we discussed today. 
- Initial inspection Solder joints looked normal.
- Confluence profile on standard and incident motor. Both passed, looked normal
- Raj ran 50A for 60 seconds on right front (suspect one) 438. Passed. Motors got to 85C. Cooled down for 5 min
- Ran profile again. 50 seconds into it, motor stopped running. Died after 50 seconds.
- 2 wires desoldered.
- Repeated for right rear motor, ran same test as 3-4. Same issue. Indicates that this profile is too extreme, heats up solder joints, increases resistance of joints, causes them fail.

 
Next steps.
- Take unrelated motor+ESC pair. Instrument solder joints and motor fets.
- Define abort criteria (temp 10% lower than FET max or solder melt point)
- Run 25A for 100 seconds or until abort limit. Record results.
- Discuss results with Cam.
- Repair and repeat for 438 right front motor.

### Rajesh Budhabhatti, 2024-04-23

@Cameron Chapman Completed the investigation steps listed below. See the results in the invstigation report here: Investigation template VXE-438 Lift Motor failure crash.docx

### Cameron Chapman, 2024-04-23

Summary of discussion with Raj:
- Please list SNs and source for each ESC tested. Ex: 
- Took EOL ESC from field return. Tested profile from the incident
- Need to confirm this with data (list section of report)
- Took EOL ESC from field return. Tested profile from the incident. Raj reports that it failed due motor wires desoldering. Please plot throttle, and power for this test and reference section of the report.
- May want to repeat with a new ESC.
- Look at worst case landing profile. Determine worst case pause load (heaviest aircraft, highest altitude, worst conditions) https://jenaero.atlassian.net/wiki/spaces/EE/pages/11272193/Power+and+Temperature+Profiles, determine max pause duration. Everett can help with this. Determine max pause duration. Open up corrective action task for FW to implement.

### Cameron Chapman, 2024-04-23

@Pat Wells Raj is going to update the investigation and perform a few more steps, but we seem to be closing in on an C/CA for this one. As predicted, it seems like the pause was too long, which caused ESCs to overheat. See fields above. FYI @David Grosher

### Rajesh Budhabhatti, 2024-04-24

@Cameron Chapman Updated the investigation report with ESC serial numbers. See table 2 for serial numbers, figure 22-24 for power and throttle plots in the investigation report here: Investigation template VXE-438 Lift Motor failure crash.docx.
I will repeat the 25A, 100 seconds test with new ESCs and chart Power, current, throttle and temperature data in the report.

### Cameron Chapman, 2024-04-24

Thanks @Rajesh Budhabhatti please monitor and log temps if possible during that test, and abort if any hit your limits established before the test. 
We should not need a brand new ESC, but can likely find one that is red tagged for an NCR/crash that is functional for these purposes.

### Rajesh Budhabhatti, 2024-04-24

Yes, will find a way to be able to log and chart temps.
I have found a cache of red tagged ESCs in the lab. I will also get some input from Everett on worst case scenarios and extrapolate ambient temperature.
Thank you for yesterday’s OJT.
Raj

### Cameron Chapman, 2024-04-24

@Rajesh Budhabhatti the tests in figures 22-24 should be compared to flight profiles. Ex: 94% throttle for 30 seconds seems high. What is the worst case takeoff profile throttle setting and duraton? 
Is the profile in figure 24 the same as the ESCs experienced during this incident? If so, you should state that in that section/figure.
Given that the 438 EScs were ran to failure at a high current before this test, I do not think this is enough to prove that there was an issue with those ESCs that caused the incident. This does seem to prove that normal ESCs should survive a 100s 25A run. 
@Sean Odell I take back what I said earlier. I do not think we are ready to finish this investigation. Do we have other cases we could use if you need these, or could we issue new cases to the customer?
[embedded: image-20240424-174056.png]

### Cameron Chapman, 2024-04-24

@Rajesh Budhabhatti can you please add details to the investigation of all of the tests run on each of the 438 motors after we received them? Especially the tests that were ran at 2x the intended current.

### Rajesh Budhabhatti, 2024-04-24

@Cameron Chapman Hi Cameron, once we realized that first 60 seconds of 240s landing profile was the cause of damaging the ESCs, the intent was to 
- See how far we can push EOL ESCs ie. 90% of absolute limits. Do you want me to run the landing profile on EOL ESCs and see how far/long they last? The landing profile is full of peaks and valleys and I don’t see how we can quantize that to determine the ESC limits. Steps 1-, 2. Let me know if you want me to run the crash profiles to determine the ESC limits.
- Step 3-4 to see what would be a safe operating range for ESC. We selected 25A at 100s.
- Yes, As we hoped, a normal ESC will survive a 100s run at 25A. Since the ambient temperature in Dyno room was about 23C, a temperature rise of 75.5c would place the ESC at 98.5c in 50c ambient.

Great idea. Yes, I will list out all the tests run on each of the 438 motors. I have this info in my notes.

### Cameron Chapman, 2024-04-26

@Rajesh Budhabhatti the intent was not to match the exact profile, just the average current, which is where 25A/100s came from. Since normal ESCs survive this profile, and one of these did not (seeks like front right, Thr2), we need to try and figure out why that one was different with that ESC that caused it to fail. This may be more difficult, since they were run on a more extreme profile to failure after, so it will be hard to tell when damage occurred. 
Can you please plot ibatt 1-2 if we have those plots and post to comments here? That will show the difference in current between left 1 and right 2.
There should be OAT data if we want to record temperature at the time of the incident.

### Rajesh Budhabhatti, 2024-04-26

Good morning Cameron,
Will do.
Raj

### Rajesh Budhabhatti, 2024-04-26

@Cameron Chapman Current draw discrepancy observed. Lift system on right side was drawing considerable more power than the left side. See figures 26 and 27 in the investigation report.

### Cameron Chapman, 2024-04-30

@Rajesh Budhabhatti the timelines for the XCOM log and VTOL log don’t always line up. You should compare the vtibatt on the xcom log to the ibatt and ibatt 1-2 on the VTOL log to line up the profiles. In this case, the plots you listed correspond to no current, not landing current.
@Liam Shaw  or another FW engineer may be able to point to conversion, or explain why the UTC is not for the same time period (it should be). We should log and link  any useful information or conversions in the data review documents. 
[embedded: image-20240430-182040.png]

### Rajesh Budhabhatti, 2024-04-30

Table 2 in the investigation report lists serial numbers and other details about the ESCs under test.

### Rajesh Budhabhatti, 2024-04-30

Updated the fishbone diagram and scaled the XCOM-VTOL charts time axis.

### Cameron Chapman, 2024-05-07

Assigning back to @Rajesh Budhabhatti please ensure all Jira fields and sections of the report are updated to the latest status.

### Rajesh Budhabhatti, 2024-05-07

- Took EOL ESC from field return. Tested profile from the incident. They failed due motor wires desoldering. Plotted throttle, and power for this test. See fig. 20 in the report.

### Pat Wells, 2024-06-14

@Cameron Chapman @Rajesh Budhabhatti Any more progress made on determining root cause?

### Rajesh Budhabhatti, 2024-06-14

@Pat Wells @Cameron Chapman  Hello Patrick, We replicated the failure mode by running the ESCs under AAR conditions. It looks like the failure was caused by subjecting the AV to extended pauses. We ran further tests using field return ESCs to replicate ESC failure pattern. Based on these experiments, we developed a thermal model and set of guidelines on maximum pause under various conditions such as ambient temperature, heat build-up during take-offs, heat dissipation during cruising, pause and thermal budget for landing. Please see the report here:  VXE-30 Absolute maximum Pause duration.docx

### Cameron Chapman, 2024-06-17

@Rajesh Budhabhatti  please update all fields in this incident, the report, and the subtask and let me know when ready to review.
FYI @Pat Wells

### Rajesh Budhabhatti, 2024-06-17

Done

### Cameron Chapman, 2024-06-18

@Rajesh Budhabhatti the report is becoming more clear. Thank you for the detailed testing and reports. Some remaining questions, errors, or unclear items: Please correct. 
Investigation report: 
- Fishbone says cause 6 is confirmed. List says cause 5.
- Unclear how cause 5 and 6 are different.
- The throttle profile in figure doesn't seem to match the flight profile (flight profile throttles go up to 90%, dyno max is 60).
- Table 2 ESCs under test: wasn’t there a test before this where the ESCs were tested above the flight profile? That should be added for full transparency.
- It seems like your investigation indicates that a normal aircraft should hover around 50% throttle, but this one averaged around 70%. You should update the applicable parts of the report accordingly. So the next steps of the investigation should be:
- to confirm those estimates with Everett.
- identify why this one hovered at a higher throttle (flying over weight limits, extreme conditions, etc).
- Confirm that the heating profile of a fluctuating throttle and load is similar to a flat profile with a throttle based on the first profiles aveage (via integral). Need to verify that to ensure we establish a good limit.
- List what the maximum limit should have been for this throttle average (based on your evaluation)

Max Pause Duration Report
- Table 4 should read “Max hover time after X minute cruise”. The tables are not clear to a first time reader and could use some captions or descriptions.
- We should add a table for 0 cruise time (hover immediately after climb)

Notes 
- Average current during the pause was ~30A with large fluctuations, throttle around 60%.

### Cameron Chapman, 2024-06-18

@Pat Wells I think the current report proves that this aircraft hovered at too high power for too long. Next steps are to determine why it was hovering at such high power, and to implement auto abort limits.

### Pat Wells, 2024-07-16

@Cameron Chapman @Rajesh Budhabhatti sent a note to the customer today.  Asked if there were any special payloads installed or configurations that may have caused the vehicle to be heavier than normal.

### Pat Wells, 2024-07-16

@Cameron Chapman @Rajesh Budhabhatti received feedback from customer.  No additional payloads or weight on the aircraft.  Standard battery configuration with Trillium HD45 payload.

### Pat Wells, 2024-08-15

@Cameron Chapman FYSA
This case was put into the plan to be worked to closure during the Sprint planning meeting held on 8/14.  8/19-8/23.

### Cameron Chapman, 2024-08-15

@Rajesh Budhabhatti please work this issue if you do not have any critical MAGNSS work. See plan above.

### Alexander Alan Arnold, 2024-12-10

@Rajesh Budhabhatti Is D5 the appropriate status for this issue?

### Rajesh Budhabhatti, 2024-12-10

@Alexander Alan Arnold Yes, the root cause for this incident was excessive pause and high current. We have been able to replicate this failure on dyno tests.

### Alexander Alan Arnold, 2024-12-10

@Rajesh Budhabhatti Since we have a corrective action identified shouldn't it be moved to D6 since we are working to implement that CA?

### David Grosher, 2025-05-19

@Pat Wells This task is assigned to you, are you tracking it? Is there a customer request pending?

### Pat Wells, 2025-05-20

@David Grosher CA is complete. Moving to Done.

## Attachments (11)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V438_240209_111159_pack.zip | archive | 2694 | 2024-02-14 | listed only |
| image-20240214-204501.png | image | 77 | 2024-02-14 | listed only |
| image-20240227-191956.png | image | 97 | 2024-02-27 | listed only |
| [09 Feb 24 438 Rotor Fail SUAS Incident Mishap Report.xlsx](attachments/19608_09%20Feb%2024%20438%20Rotor%20Fail%20SUAS%20Incident%20Mishap%20Report.xlsx.md) | xlsx | 1654 | 2024-03-20 | converted |
| [Investigation template VXE-438 Lift Motor failure crash (0776e3e6-6e7e-4c9a-8de1-a4df1cc3e379).docx](attachments/19740_Investigation%20template%20VXE-438%20Lift%20Motor%20failure%20crash%20(0776e3e6-6e7e-4c9a-8de1-a4df1cc3e379).docx.md) | docx | 1686 | 2024-03-28 | converted |
| image-20240424-174056.png | image | 21 | 2024-04-24 | listed only |
| ~WRD0000.jpg | image | 1 | 2024-04-24 | listed only |
| ~WRD0001.jpg | image | 1 | 2024-04-26 | listed only |
| image-20240430-182040.png | image | 60 | 2024-04-30 | listed only |
| [Advisory Notice-24-003 Use of Pause and Nudge Commands.pdf](attachments/26808_Advisory%20Notice-24-003%20Use%20of%20Pause%20and%20Nudge%20Commands.pdf.md) | pdf | 208 | 2025-03-04 | converted |
| [pause Nudge Advisory notice.pdf](attachments/26799_pause%20Nudge%20Advisory%20notice.pdf.md) | pdf | 319 | 2025-03-04 | converted |
