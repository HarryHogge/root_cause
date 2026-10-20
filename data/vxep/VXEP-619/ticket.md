# VXEP-619: VXE 644 Loss of aircraft while in fixed wing flight.  Aircraft rolled over and crashed straight into ground.

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2024-09-06
- **Updated:** 2026-03-02
- **Resolved:** 2025-02-19
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** LM_asset, NAWCAD, Weekly-incident-tracker
- **Links:** relates to RMA-339 (VXE-644 240910-2 LM Incident ); relates to FS2-2319 (Investigate automatically engaging VTOL system when sensor failures are detected in the FWAP in order to prevent crashes.); relates to FS2-2381 (VXEP-619 Loss of Aircraft in FW flight)
- **Customer:** LM, LM_Asset, NAWCAD
- **Vehicle Tail Number:** 644
- **Root Cause:** Failure of y gyro reading. Currently unclear what caused the failure
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

Files: VXE644_BadPitchGyro
Summary ppt: here
Incident description: 644 and 643 history.docx
IMU Docs: MPU-9250 IMU Replacement

From LM FSR:
Unfortunately, we lost airframe 644 yesterday. About 2 hrs and 51 minutes into the flight, the airframe rolled over and went straight into the ground.  It is completely and utterly destroyed.  We were able to recover the FW autopilot and its data files.  We have the VTOL autopilot, but can’t get the files off of it.  We also have SA video. 
 AAR and SA camera attached
This is not a TIQ asset

## Corrective Action

Created backlog item below.  If a sensor has failed in the single-string autopilot there isn’t a ton we can do other than engage the VTOL system.
https://jenaero.atlassian.net/browse/FS2-2319
Held meeting with Quality dept. 2/24/25 and relayed finding of FWAP daughter card 1710p01a.  Quality will take action and perform a sampling plan to understand the impact or spread of the defects.

## Plan

- 1/28/25 Update from Dave and Sam: unlikely to recreate this failure and little value of doing so. Dave’s team will create a report for Pat to send to the customer. 
- Can the reported SD failure affect this issue?
- Evidence of sensor failure (based on flight data). Additional testing of IMU. Consider standard electronics checkout.
- Inspect IMU components for evidence of failure. Ensure components like the shield can are carefully removed if needed (so evidence  is not destroyed)
- Review data of subsequent power ups to see if the sensor kept reading anomalous, or if it recovered with a power cycle.  @Cameron Chapman the sensor appeared to recover in the bench testing to date, so if it were a hardware issue it would have been specific to the state at the time of the incident, i.e. temperature, vibe etc.
- Data questions:
- From ppt “Software limit on gyro appears to be disabled:” @Eric Brewer should this be reenabled? We should add to the ppt either way.  @Cameron Chapman the clip state could be used for reporting but the functionality it implements would not have helped in this case (just limits gyro bias estimation when clipping occurs).  I suspect it was disabled since the sensor limit is >> what we would see operationally.

## Issue Status

Avionics box was tested on the Iron Bird and showed a responsive IMU (MPU9250)  
The VTOL AP board has connectors that ripped off. Uncertain if this damage happened from impact or before, but since the issue was with the fixed wing IMU, not VTOL, damage to this board is likely from impact. 
Create powerpoint here with a few plots.

## Comments (56)

### Cameron Chapman, 2025-01-17

Responded on teams. Hi Pat Wells and Doug Baker. Responding to this comment. How urgent is this request? Worth working the holiday weekend troubleshooting? There is a very good chance we won't be able to replicate the issue with the small amount of evidence available.

### Pat Wells, 2025-01-21

@Cameron Chapman checking in for updates.  It looks like their is a bit of updated documentation since last Friday. Are we at a stopping point now or is the team still working on this?

### Cameron Chapman, 2025-01-21

@Pat Wells we are ready to work this again as soon as we can sort out this priority vs LRR projects. See plan field above for next steps.

### Steve Gonzales, 2025-01-21

General update, we have gathered a list of potential root causes and will be working on specific hardware tests.

### Pat Wells, 2025-01-23

Thanks @Steve Gonzales any updates or new info?

### Steve Gonzales, 2025-01-23

So far it looks like the capacitive pickoff within the MEMS itself.  An external resonance mode may have attributed to the failure but is still unknown and in process of further study.  Estimating less than 5 days for report out.

### Pat Wells, 2025-01-24

Just tagging in a reminder here based on teams chat with @David Grosher 

@Steve Gonzales FYSA

### Liam Limon, 2025-01-27

@Steve Gonzales Just a quick update on this AP. I ran it through programming this morning and it’s currently in Burn-in. Tomorrow we should be able to go through Calibration with it and see if anything stands out. My one finding from this morning is that the AP is constantly outputting “short stat msg: 0031 short stat parm1: 0000 short stat parm2: 00000000”. I’ve only seen this on one other autopilot in the past. The reference NCR is in the NCR Archives NCR-230828 - 1430. That AP had passed all of it’s checkouts and then failed the final servo test in electronics. It was pulled from the box and found to be giving the short stat parm message. I don’t believe any further investigation was done to determine what that message means and what causes it, but ultimately that AP was scraped. Perhaps software can provide more insight on what that is and what causes it?

### Pat Wells, 2025-01-27

@Liam Limon @Steve Gonzales I had a Teams chat with Dave G last Friday about producing a properly formatted customer report for this.  The request was to have a completed document by close of business today (27Jan)

### Liam Limon, 2025-01-27

@Pat Wells The burn in takes a little over 5 hours, I may be able to get to it this evening. @David Grosher I would like to know more about the short stat parm error though. It’s not a common error and as I said below, the other AP that I’ve seen that error on had a failed servo output and was scraped. It would be good to know what drives that message and if it relates at all to the locked up sensor values in this AP and the servo output failure on the other one. Speculating on Gordon’s naming conventions, that could be calling some kind of statistic parameter that isn’t outputting correctly.

### Steve Gonzales, 2025-01-27

@Eric Brewer FYI on below comments from Liam regarding the FWAP pcb I had run through electronics cal and burn in.

### Liam Limon, 2025-01-27

@Steve Gonzales I talked through what was going on with Eric and we were able to determine that the ‘short stat msg’ and ‘short stat parm' messages in the debug log are a symptom of using an autopilot that is on the newer 6.05 firmware with our old GCS that is on GCS version 2.3. The handling of those messages is different on the old GCS and that’s why it continually displays them every 10 seconds. It seems like this is expected behavior and we can discard it as being a problem for this investigation. I’ll give you an update once the burn-in is complete and I do calibration.

### Steve Gonzales, 2025-01-27

@Eric Brewer FYI, per Brandon the SD on the Xcomm failed upon startup on 1/24. Here are the logs pulled off that card by Jason.  [embedded file]

### Cameron Chapman, 2025-01-28

@Steve Gonzales per 1/28 meeting. Ok to hold on this investigation.

### David Grosher, 2025-01-28

@Pat Wells I cleaned up the report.

### Steve Gonzales, 2025-01-29

Added calibration file from burn in testing.  Abnormality in that it has stored FDR data after cal without header files.

### Steve Gonzales, 2025-01-29

Adding soft version of previously performed on paper fishbone.

### Steve Gonzales, 2025-01-29

About 10 out of spec workmanship issues found after removing the can on the FWAP daughter card 1710p01a.  No shorts detected with DMM.  Passing calibration confirms no opens, respectively.

### David Grosher, 2025-02-18

@Pat Wells It is unclear to me what the next required step is here. If the customer is satisfied then it may make sense to close this to the Bermuda triangle as there are still a few open “whys?” that weren’t answered.

### Pat Wells, 2025-02-19

@David Grosher I concur.  Customer was provided the report summary almost a month ago and didn’t provide any additional feedback.

### Adrian Garcia, 2024-09-30

@David Grosher Do you want me to still pull the all the logs, I added some of the logs to the zip folder called 644 logs when I was first assigned this issue?

### David Grosher, 2024-09-30

@Adrian Garcia Yes, still pull the data. We can include it in the report. @Eric Brewer FYSA

### Adrian Garcia, 2024-09-30

@David Grosher @Eric Brewer @Cameron Chapman here is the VTOL logs [embedded file]

### Eric Brewer, 2024-10-01

@Adrian Garcia thanks.  It’s a bit odd - the VTOL log cuts out just before the rate excursion happens, although we can see in the xcomm log that the VTOL attitude is still updating.  @Jason Scherer do you know if there would be of any link between fixed-wing IMU and VTOL logging? I can’t think of any and don’t see any clues in the log. @David Grosher @Cameron Chapman FYI.  The VTOL log is VTL00061.CSV.  I added plots and updated the powerpoint linked above, I believe it is ready to send to the customer if Dave agrees.

### David Grosher, 2024-10-01

@Eric Brewer @Jason Scherer The VTOL and XCOMM will buffer data for a number of seconds before writing to the SD card. So it is common to see lost data at the end of the file in the event of an incident. I don’t think this is due to any dependency, it is expected behavior.

### David Grosher, 2024-10-01

@Eric Brewer I think there are a few more questions that need to be answered before the report is sent out. Why would the sensor report a value at the max value of its range? Is it an error state being reported by the sensor itself? Is clipping it appropriate in this case? If it isn’t an error state, did the hardware fail? Hardware data should be included in the report. What could explain the hardware working now but failing previously? Can we collect more data to test the hypothesis? 
Also for the report, we need the conclusion up front. I would suggest adding it to the same slide with the summary.

### Eric Brewer, 2024-10-01

@Connor Peebles , are you able to help test out the autopilot hardware a bit?  The initial bench logs looked normal.  I think we’d want to do some shaking tests and then apply heat and see if the gyro output becomes corrupted like we saw in flight.  Let me know if you want to discuss details. @David Grosher FYI.

### Pat Wells, 2024-10-28

@David Grosher wanted to re-visit this.  LM has been inquiring on an estimated date that we’re about to provide a conclusive report for their customer.

### David Grosher, 2024-10-28

@Pat Wells We can see that the IMU failed, but we don’t have any indication why.  Bench tests have also shown it to be working following the incident. We need the EE team to support further investigation but resources are tied up on other investigations.

### Pat Wells, 2024-11-26

@David Grosher @Cameron Chapman 
Are we at a point where we can make a call on this in regards to warranty determination. Was this an Edge related component failure?

### David Grosher, 2024-11-26

@Pat Wells Yes, I believe this was a hardware failure even though we can’t conclusively demonstrate it.

### Cameron Chapman, 2024-11-27

@Laszlo Juhasz can you please look into if this IMU is still malfunctioning, and what may have caused this behavior?

### Alexander Alan Arnold, 2024-12-10

@Laszlo Juhasz Is D4 still accurate for this issue or can it be updated to D5/D6?

### Alexander Alan Arnold, 2025-01-10

@Laszlo Juhasz Are we good to move this to D5/6? @Cameron Chapman

### Cameron Chapman, 2025-01-10

@Alexander Alan Arnold no. We do not have any evidence of why the IMU may have failed, or explanation of if it is not possible to determine that at this time. Assigning to @Steve Gonzales to help further investigate or wrap this one up.

### Pat Wells, 2025-01-17

@David Grosher @Cameron Chapman LM’s end user customer is requesting an immediate finalized report with all possible information on the root cause of the failure. They are deeply concerned that their other aircraft, 643, could be affected by the same issue. The aircraft involved in the crash is one of only two owned by the customer, and with a high-profile event coming up for their last remaining aircraft, they need urgent assurance that this is not a fleetwide problem. They are also seeking an assessment of the likelihood of recurrence.
Could we please prioritize this request and provide as much detailed information as possible without delay.

### Cameron Chapman, 2025-01-17

Responded on teams. Hi Pat Wells and Doug Baker. Responding to this comment. How urgent is this request? Worth working the holiday weekend troubleshooting? There is a very good chance we won't be able to replicate the issue with the small amount of evidence available.

### Pat Wells, 2025-01-21

@Cameron Chapman checking in for updates.  It looks like their is a bit of updated documentation since last Friday. Are we at a stopping point now or is the team still working on this?

### Cameron Chapman, 2025-01-21

@Pat Wells we are ready to work this again as soon as we can sort out this priority vs LRR projects. See plan field above for next steps.

### Steve Gonzales, 2025-01-21

General update, we have gathered a list of potential root causes and will be working on specific hardware tests.

### Pat Wells, 2025-01-23

Thanks @Steve Gonzales any updates or new info?

### Steve Gonzales, 2025-01-23

So far it looks like the capacitive pickoff within the MEMS itself.  An external resonance mode may have attributed to the failure but is still unknown and in process of further study.  Estimating less than 5 days for report out.

### Pat Wells, 2025-01-24

Just tagging in a reminder here based on teams chat with @David Grosher 

@Steve Gonzales FYSA

### Liam Limon, 2025-01-27

@Steve Gonzales Just a quick update on this AP. I ran it through programming this morning and it’s currently in Burn-in. Tomorrow we should be able to go through Calibration with it and see if anything stands out. My one finding from this morning is that the AP is constantly outputting “short stat msg: 0031 short stat parm1: 0000 short stat parm2: 00000000”. I’ve only seen this on one other autopilot in the past. The reference NCR is in the NCR Archives NCR-230828 - 1430. That AP had passed all of it’s checkouts and then failed the final servo test in electronics. It was pulled from the box and found to be giving the short stat parm message. I don’t believe any further investigation was done to determine what that message means and what causes it, but ultimately that AP was scraped. Perhaps software can provide more insight on what that is and what causes it?

### Pat Wells, 2025-01-27

@Liam Limon @Steve Gonzales I had a Teams chat with Dave G last Friday about producing a properly formatted customer report for this.  The request was to have a completed document by close of business today (27Jan)

### Liam Limon, 2025-01-27

@Pat Wells The burn in takes a little over 5 hours, I may be able to get to it this evening. @David Grosher I would like to know more about the short stat parm error though. It’s not a common error and as I said below, the other AP that I’ve seen that error on had a failed servo output and was scraped. It would be good to know what drives that message and if it relates at all to the locked up sensor values in this AP and the servo output failure on the other one. Speculating on Gordon’s naming conventions, that could be calling some kind of statistic parameter that isn’t outputting correctly.

### Steve Gonzales, 2025-01-27

@Eric Brewer FYI on below comments from Liam regarding the FWAP pcb I had run through electronics cal and burn in.

### Liam Limon, 2025-01-27

@Steve Gonzales I talked through what was going on with Eric and we were able to determine that the ‘short stat msg’ and ‘short stat parm' messages in the debug log are a symptom of using an autopilot that is on the newer 6.05 firmware with our old GCS that is on GCS version 2.3. The handling of those messages is different on the old GCS and that’s why it continually displays them every 10 seconds. It seems like this is expected behavior and we can discard it as being a problem for this investigation. I’ll give you an update once the burn-in is complete and I do calibration.

### Steve Gonzales, 2025-01-27

@Eric Brewer FYI, per Brandon the SD on the Xcomm failed upon startup on 1/24. Here are the logs pulled off that card by Jason.  [embedded file]

### Cameron Chapman, 2025-01-28

@Steve Gonzales per 1/28 meeting. Ok to hold on this investigation.

### David Grosher, 2025-01-28

@Pat Wells I cleaned up the report.

### Steve Gonzales, 2025-01-29

Added calibration file from burn in testing.  Abnormality in that it has stored FDR data after cal without header files.

### Steve Gonzales, 2025-01-29

Adding soft version of previously performed on paper fishbone.

### Steve Gonzales, 2025-01-29

About 10 out of spec workmanship issues found after removing the can on the FWAP daughter card 1710p01a.  No shorts detected with DMM.  Passing calibration confirms no opens, respectively.

### David Grosher, 2025-02-18

@Pat Wells It is unclear to me what the next required step is here. If the customer is satisfied then it may make sense to close this to the Bermuda triangle as there are still a few open “whys?” that weren’t answered.

### Pat Wells, 2025-02-19

@David Grosher I concur.  Customer was provided the report summary almost a month ago and didn’t provide any additional feedback.

## Attachments (9)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 644 SA Camera of incident.mpg | video | 1626 | 2024-09-06 | listed only |
| [644 and 643 history.docx](attachments/23012_644%20and%20643%20history.docx.md) | docx | 902 | 2024-09-06 | converted |
| T95_V644_240905_104705_01_pack.zip | archive | 2077 | 2024-09-06 | listed only |
| 644 logs.zip | archive | 6098 | 2024-09-11 | listed only |
| DATALOG (1).zip | archive | 25961 | 2024-09-30 | listed only |
| VXE-644-SDCard-Data.zip | archive | 9468 | 2025-01-27 | listed only |
| [644 fishbone.xlsx](attachments/25765_644%20fishbone.xlsx.md) | xlsx | 16 | 2025-01-29 | converted |
| 9dof pcb pics.zip | archive | 66225 | 2025-01-29 | listed only |
| [acal10674-250129.csv](attachments/25756_acal10674-250129.csv.md) | csv | 308 | 2025-01-29 | converted |
