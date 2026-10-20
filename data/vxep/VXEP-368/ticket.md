# VXEP-368: VXE 523 multiple faults with HLB discharging while in fuel cell configuration

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-04-18
- **Updated:** 2026-03-02
- **Resolved:** 2025-05-19
- **Reporter:** Pat Wells
- **Assignee:** Josh Burrell
- **Creator:** Pat Wells
- **Labels:** Airspeed-Cal, GCS, USASOC, Weekly-incident-tracker
- **Links:** relates to FS2-1758 (v523 Investigation Fuel Cell and HLB issue seems to be Faulty Air Speed Data); is cloned by FS2-1759 (Fuel cell and HLB state of charge); relates to VXEP-292 (VXE-477 Crash on take off ); relates to FS2-2390 (VXEP-292 Crash on take off); relates to SMUP-43 (Evaluate Manuals for accurate pitot calibration procedure)
- **Customer:** USASOC
- **Vehicle Tail Number:** 523
- **Problem Type:** Other (explain in description)
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Information received from customer:
Over the last 72 hours we have had several faults we believe relate to the fuel cell configuration. Upon launching the aircraft, the HLB will continue discharging. The fuel cell operation window was also reporting a battery current of "-10". We chose to immediately start the landing sequence 10 minutes after launch. At IP1 the HLB was reporting a 40% state of charge while still continuously discharging. The aircraft was reporting failure to maintain altitude.

AAR file attached

**
Added additional information received from customer below:
We have not isolated an individual fuel cell or component yet. After the issue occurred the first time, we swapped to a new fuel cell, fuel filter, and HLB while using the same aircraft. The two separate flights have had the faults populate within the same timeframe of each other. We reviewed the latest software update to be published and found nothing correlating to fuel cell operations, however after installing the update, our first two flights since have had the same issue with the fuel cell configuration. We have paused flight operations until the problem is resolved.

Files: https://jenaero.sharepoint.com/sites/FlightSafety/Shared%20Documents/Forms/AllItems.aspx?RootFolder=%2Fsites%2FFlightSafety%2FShared%20Documents%2FIncident%20Reports%2FVXEP%2D368

## Corrective Action

https://jenaero.atlassian.net/browse/VXEP-377 
For determining if there is a software issue, run test procedure describe din vxep-292.
For this particular bird, an updated air data calibration can be performed.  This will likely resolve the issue.  After the airdata cal is completed, pressure can be applied and the airspeed reading observed.  The sensor is expected to read above 60 knots for a good cal.  Both 477 and 523 read below 40 knots with pressure applied.
- Update Training
- Delay in the launch wizard before moving to pitot pressure test.

@Josh Burrell This is another airspeed-cal issue.  There is discussion on our team that fuel cell operation training needs to be reviewed to ensure operators monitor the state of charge of the battery to ensure it is neutral or charging the HLB the vast majority of the time.

## Plan

Per plots on slide 11 here, this looks like the same issue experienced by AV477.  Recommend performing testing described in [VXEP-292] VXE-477 Crash on take off - Jira (atlassian.net) in order to understand if new software is causing delays in when pitot calibration is applied.  Since the step where pressure is applied immediately follows the step where the pitot is shielded, we suspect there could be a software delay causing the software to latch a pressured-applied value as the new zero for airspeed.
@Pat Wells can you see if we can get VTOL logs from the flight in question?  If not I can scrub through the logs to see if we have any other estimates we can use to double-check TAS.

Seems like SW group is working here. https://jenaero.atlassian.net/browse/FS2-1759 We can still use this incident to summarize overall status. 
- @Eric Brewer discussing with @David Grosher , can you please look into the new AAR and my questions below? We are trying to determine what variables caused the throttle to be higher than normal, and if the replacement nose cone resolved the issue (which would isolate it to the nose cone). @Pat Wells mentioned it was very high priority, as the customer is unable to perform important missions without this aircraft.
- I am thinking they could run a ground test of this nosecone, then swap it and compare the result. If the power is much higher for the same throttle, that should prove it is a problem in the nose. (Hopefully not damage caused by something in the vehicle). Given their remote location, I think this is worth the low risk.
- @Michael Berger @Jason Scherer is there a motor test page like there is in VTOL? If so, they could use that. I am thinking launch wizard might be too quick and high throttle for a good comparison.
- 4/23/23: I charted the Throttle Vs Power curves from XCL00050 (original cruise motor) and XCL00052 (Spare cruise motor). The power draw is nearly the same. This tells us that the issue is not with the motor. I also charted throttle vs power curves from another vehicle. This standard vehicle is drawing nearly half the power as VXE-523 for the same throttle value. See slide number 8 and 9 here:  Vehicle Investigation VXEP-368 v523 Data for charts here: VXE-523 investigation data XCL00050.CSV
- See questions from Cam below.
- @Jason Scherer is there any logic to stop climbing, alert operator, and/or RTB if the HLB is too low and not charging during fuel cell operations? I’ll look into this. I believe there is some logic that pertains to that. I do know that the XComm will command the “emergency” level of output (500W) from the fuel cell based on SoC and range to waypoint. The data shows this occurred during the flight. Tracking here https://jenaero.atlassian.net/browse/VXEP-377
- @Pat Wells  there are still some actions and questions for @Jason Scherer below, but I think sending a replacement nose cone to test is a good idea. We should try to verify this fixes the issue before clearing it for flight.

## Issue Status

Latest investigation report uploaded to SharePoint here: Vehicle Investigation VXEP-368 v523.pptx. Data for charts here: VXE-523 investigation data XCL00050.CSV
Looking at the original logs and test investigation logs from customer after changing the cruise motors and comparing these numbers with other cases, it seems that the cruise motor and power systems (Battery Fuel Cell) are fine.
Issue appears to be caused by pitot calibration errors.

## Root Cause

Pitot calibration errors caused the air vehicle to fly too fast, resulting in more thrust usage than typical.
Root cause of calibration errors is unclear.  Leading theory is operator error, software issue causing delay in calibration, or some combination of both.

## Comments (43)

### Pat Wells, 2024-05-08

@Cameron Chapman @Jason Scherer 
Any updates?  The customer reached out this morning inquiring.

### David Grosher, 2024-05-10

@Cameron Chapman FYI, this issue has new data on the FWD propulsion that was pulling too much power.

### Cameron Chapman, 2024-05-14

@Eric Brewer discussing with @David Grosher , can you please look into the new AAR and my questions below? We are trying to determine what variables caused the throttle to be higher than normal, and if the replacement nose cone resolved the issue (which would isolate it to the nose cone). @Pat Wells mentioned it was very high priority, as the customer is unable to perform important missions without this aircraft. 
Thank you.

### Eric Brewer, 2024-05-14

@Cameron Chapman apologies I had shared some IM’s with @Jason Scherer on the side but did not update this issue.  This looked to me like a bad airdata calibration.  The groundspeed is consistently well above the airspeed.  We saw something similar happen on AV477 (I linked that issue above also).  Unfortunately I don’t have TAS in the xcomm log and I don’t see a VTOL log with this, but unless it was an extremely hot day I suspect a bad airdata cal.

[embedded image-20240514-183851.png]

### Cameron Chapman, 2024-05-14

Thanks @Eric Brewer 
- Can you please update the fields above and the incident report with your findings and what you recommend next.
- Do you know why we do not have a VTOL log? AAR run after CW was removed? Should we request it from the customer to confirm?
- Can the operators in the field recalibrate the air data, or does that need to be done here? Is that the shield pitot, push pitot step in the pre-flight?

### Eric Brewer, 2024-05-14

@Cameron Chapman 
- will do
- I do not, probably worth confirming if the logs are available.
- Yes the calibration is the shield/push step.  If you take a look at https://jenaero.atlassian.net/browse/VXEP-292 I had suggested some procedures to test if the software is inducing more delay than normal.  I find it suspicious that both incidents were with the new software.

### Pat Wells, 2024-05-15

@Eric Brewer @Cameron Chapman 
Here’s my proposed path forward. 
I will notify the operator informing them that there were no issues discovered with their fuel cell or forward propulsion system.
The cause of the anomaly was a bad air data calibration.
Instruct the operator to perform a new air data calibration.  Informing them that a reading above 60 knots on the pitot check is a “GO” and they are clear to fly.

Is this ok?

### Eric Brewer, 2024-05-15

@Pat Wells I took a quick look at some data and depending how they are doing the air data calibration there are some that look “successful” but only go to 54 knots or so.  Let me do a little more digging and get you a more concrete answer this afternoon if that’s OK.

### Pat Wells, 2024-05-15

@Eric Brewer got it.
Standing by.

### Eric Brewer, 2024-05-15

@Pat Wells per our discussion find summary slides at the end of the ppt (slides 13-18). Let me know if the slides are clear.  If everyone is OK with the content we can export those slides specifically to .pdf and send. 
I did mention in the slides that we’ve seen this on another aircraft, that will likely be news to the customer and could potentially raise more questions.  If we can I’d recommend we expedite trying to run the in-house testing I mentioned below.
@David Grosher @Cameron Chapman FYI.

### Pat Wells, 2024-05-15

@Eric Brewer great report and summary!  Thank you!
I will adjust slightly and send over to the operators today.

### Cameron Chapman, 2024-05-17

I asked flight team if they could perform the test in the linked incident.

### Eric Brewer, 2024-05-21

@David Grosher @Cameron Chapman I ran a query in the database:
SELECT M.flight_id, M.tail_number, M.date, M.time
FROM missions AS M
INNER JOIN xcomm_data as X on (X.flight_id = M.flight_id )
WHERE X."apgpsGs">100 AND X."apIas" < 50
Group by M.flight_id, M.tail_number, M.date, M.time
This returned 5 flights total.  One was incident 523, 3 were windy days (no indications of bad airdata cal), and one was consistent with a bad airdata cal (T95_V465_220804_111608_pack)
Based upon that result it looks the bad airdata cal is pretty rare event (at least for the log sets we have) which makes it more suspicious we’ve had a few more recently with the latest software.

### David Grosher, 2024-09-24

@Ted Trowbridge Another Airspeed Cal related issue. See the CAs, they are probably duplicate.

### Alexander Alan Arnold, 2024-12-10

@Ted Trowbridge Can this item be closed out?

### Josh Burrell, 2025-01-07

New verbiage has been added to the OPS manual to clarify what a correct Pitot test should look like.

### Alexander Alan Arnold, 2025-01-10

@Josh Burrell Since the verbage has been added can we close this out @Ted Trowbridge

### Alexander Alan Arnold, 2025-01-10

@Pat Wells review final report please.

### Pat Wells, 2025-01-10

@Alexander Alan Arnold we sent a report to the customer on this shortly after it happened in Apr 24.  If the corrective action has been implemented then we should move to close this out.

### Jason Scherer, 2025-03-22

Completed subtask https://jenaero.atlassian.net/browse/VXEP-377. Low Energy RTB would also apply to fuel cell configurations. So, if the HLB s low during fixed wing flight, the fixed wing processor would stop climbing, RTB, and alert the operator.

### Cameron Chapman, 2024-04-30

@Pat Wells  there are still some actions and questions for @Jason Scherer below, but I think sending a replacement nose cone to test is a good idea. We should try to verify this fixes the issue before clearing it for flight.

### Pat Wells, 2024-04-30

@Cameron Chapman  I’ll ask them to run ground tests and provide data for your team first.

### Pat Wells, 2024-05-05

@Cameron Chapman @Jason Scherer OCONUS operators ran a forward propulsion ground test with “known good” nose cone assembly.
New AAR attached, dated 4/24

### Pat Wells, 2024-05-08

@Cameron Chapman @Jason Scherer 
Any updates?  The customer reached out this morning inquiring.

### David Grosher, 2024-05-10

@Cameron Chapman FYI, this issue has new data on the FWD propulsion that was pulling too much power.

### Cameron Chapman, 2024-05-14

@Eric Brewer discussing with @David Grosher , can you please look into the new AAR and my questions below? We are trying to determine what variables caused the throttle to be higher than normal, and if the replacement nose cone resolved the issue (which would isolate it to the nose cone). @Pat Wells mentioned it was very high priority, as the customer is unable to perform important missions without this aircraft. 
Thank you.

### Eric Brewer, 2024-05-14

@Cameron Chapman apologies I had shared some IM’s with @Jason Scherer on the side but did not update this issue.  This looked to me like a bad airdata calibration.  The groundspeed is consistently well above the airspeed.  We saw something similar happen on AV477 (I linked that issue above also).  Unfortunately I don’t have TAS in the xcomm log and I don’t see a VTOL log with this, but unless it was an extremely hot day I suspect a bad airdata cal.

[embedded image-20240514-183851.png]

### Cameron Chapman, 2024-05-14

Thanks @Eric Brewer 
- Can you please update the fields above and the incident report with your findings and what you recommend next.
- Do you know why we do not have a VTOL log? AAR run after CW was removed? Should we request it from the customer to confirm?
- Can the operators in the field recalibrate the air data, or does that need to be done here? Is that the shield pitot, push pitot step in the pre-flight?

### Eric Brewer, 2024-05-14

@Cameron Chapman 
- will do
- I do not, probably worth confirming if the logs are available.
- Yes the calibration is the shield/push step.  If you take a look at https://jenaero.atlassian.net/browse/VXEP-292 I had suggested some procedures to test if the software is inducing more delay than normal.  I find it suspicious that both incidents were with the new software.

### Pat Wells, 2024-05-15

@Eric Brewer @Cameron Chapman 
Here’s my proposed path forward. 
I will notify the operator informing them that there were no issues discovered with their fuel cell or forward propulsion system.
The cause of the anomaly was a bad air data calibration.
Instruct the operator to perform a new air data calibration.  Informing them that a reading above 60 knots on the pitot check is a “GO” and they are clear to fly.

Is this ok?

### Eric Brewer, 2024-05-15

@Pat Wells I took a quick look at some data and depending how they are doing the air data calibration there are some that look “successful” but only go to 54 knots or so.  Let me do a little more digging and get you a more concrete answer this afternoon if that’s OK.

### Pat Wells, 2024-05-15

@Eric Brewer got it.
Standing by.

### Eric Brewer, 2024-05-15

@Pat Wells per our discussion find summary slides at the end of the ppt (slides 13-18). Let me know if the slides are clear.  If everyone is OK with the content we can export those slides specifically to .pdf and send. 
I did mention in the slides that we’ve seen this on another aircraft, that will likely be news to the customer and could potentially raise more questions.  If we can I’d recommend we expedite trying to run the in-house testing I mentioned below.
@David Grosher @Cameron Chapman FYI.

### Pat Wells, 2024-05-15

@Eric Brewer great report and summary!  Thank you!
I will adjust slightly and send over to the operators today.

### Cameron Chapman, 2024-05-17

I asked flight team if they could perform the test in the linked incident.

### Eric Brewer, 2024-05-21

@David Grosher @Cameron Chapman I ran a query in the database:
SELECT M.flight_id, M.tail_number, M.date, M.time
FROM missions AS M
INNER JOIN xcomm_data as X on (X.flight_id = M.flight_id )
WHERE X."apgpsGs">100 AND X."apIas" < 50
Group by M.flight_id, M.tail_number, M.date, M.time
This returned 5 flights total.  One was incident 523, 3 were windy days (no indications of bad airdata cal), and one was consistent with a bad airdata cal (T95_V465_220804_111608_pack)
Based upon that result it looks the bad airdata cal is pretty rare event (at least for the log sets we have) which makes it more suspicious we’ve had a few more recently with the latest software.

### David Grosher, 2024-09-24

@Ted Trowbridge Another Airspeed Cal related issue. See the CAs, they are probably duplicate.

### Alexander Alan Arnold, 2024-12-10

@Ted Trowbridge Can this item be closed out?

### Josh Burrell, 2025-01-07

New verbiage has been added to the OPS manual to clarify what a correct Pitot test should look like.

### Alexander Alan Arnold, 2025-01-10

@Josh Burrell Since the verbage has been added can we close this out @Ted Trowbridge

### Alexander Alan Arnold, 2025-01-10

@Pat Wells review final report please.

### Pat Wells, 2025-01-10

@Alexander Alan Arnold we sent a report to the customer on this shortly after it happened in Apr 24.  If the corrective action has been implemented then we should move to close this out.

### Jason Scherer, 2025-03-22

Completed subtask https://jenaero.atlassian.net/browse/VXEP-377. Low Energy RTB would also apply to fuel cell configurations. So, if the HLB s low during fixed wing flight, the fixed wing processor would stop climbing, RTB, and alert the operator.

## Attachments (15)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V523_240418_174902_pack.zip | archive | 2997 | 2024-04-18 | listed only |
| image-20240419-114014.png | image | 34 | 2024-04-19 | listed only |
| image-20240419-114026.png | image | 27 | 2024-04-19 | listed only |
| image-20240419-114047.png | image | 26 | 2024-04-19 | listed only |
| [XCL00050.CSV](attachments/20153_XCL00050.CSV.md) | csv | 584 | 2024-04-20 | converted |
| [XCL00052.CSV](attachments/20152_XCL00052.CSV.md) | csv | 798 | 2024-04-20 | converted |
| image-20240422-200645.png | image | 24 | 2024-04-22 | listed only |
| image-20240422-200853.png | image | 47 | 2024-04-22 | listed only |
| image002.png | image | 4 | 2024-04-22 | listed only |
| image003.png | image | 1 | 2024-04-22 | listed only |
| ~WRD0001.jpg | image | 1 | 2024-04-22 | listed only |
| image-20240423-182909.png | image | 5 | 2024-04-23 | listed only |
| image-20240423-183448.png | image | 164 | 2024-04-23 | listed only |
| T95_V523_240424_174046_pack.zip | archive | 795 | 2024-05-05 | listed only |
| image-20240514-183851.png | image | 21 | 2024-05-14 | listed only |
