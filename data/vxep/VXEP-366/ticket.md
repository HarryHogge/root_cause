# VXEP-366: VXE 439 Three minutes after launch and transition the AV went into an automated RTB that could not be corrected

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-04-17
- **Updated:** 2026-10-08
- **Resolved:** 2026-10-08
- **Reporter:** Pat Wells
- **Assignee:** Josh Burrell
- **Creator:** Pat Wells
- **Labels:** No_crash, PMA263, Weekly-incident-tracker
- **Links:** Cannot finish until linked issue is finished. VXEP-306 (VXE 439 Fuel cell not reaching adequate power in flight); relates to RMA-247 (VXE-439 240515); Linked issue cannot finish until this issue finishes. FS2-2183 (Investigate Customer Incident VXEP-366 (Low Battery RTB after launch)); relates to FS2-2184 (Document VXEP-366 (Low Battery RTB after launch)); duplicates SMUP-27 (The Operations Manual needs an update that instructs operator to restart the launch wizard after cycling the vehicle power.); relates to SMUP-70 (The Operations Manual needs an update that instructs operator to restart the launch wizard after cycling the vehicle power.); relates to FS2-3048 (VXEP-366 (V439) Put report in correct format.)
- **Customer:** PMA263
- **Vehicle Tail Number:** 439
- **Problem Type:** Other (explain in description)
- **Plan:** Update Operations Manual
- **Issue Status:** Investigation complete.
- **Root Cause:** Launch wizard was not restarted after resetting the vehicle.
- **Incident Type:** Mission Failure/Abort
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Investigation files: VXEP-366 VXE 439 Three minutes after launch and transition the AV went into an automated RTB that could not be corrected
Report: Vehicle Investigation VXEP-366.pptx
Information reported from customer:
AV 439.  3 minutes after launch and transition the AV went into an automated RTB that could not be corrected.  The GCS was reporting 75% charge on the Main Battery and 70% charge on the HLB.  Upon transition to VTOL, the AV would not allow the operator to pause as if the HLB was drained below override levels. This is the same AV that we had errors with some recent, at the time thought to be fuel cell, later thought to be the HLBs.  We quarantined those HLBs.  I am hoping we get some resolution on this quickly as between this issue and the VTOL sensor error, are flight operations are drawing to a close.   
Previous incident: https://jenaero.atlassian.net/browse/VXEP-306 
AAR attached

## Corrective Action

The Operations Manual needs an update that instructs operator to restart the launch wizard after cycling the vehicle power.https://jenaero.atlassian.net/browse/SMU-134

## Comments (35)

### David Grosher, 2024-04-17

@Pat Wells I thought we asked them to ground this vehicle while the investigations were ongoing. Something is clearly wrong with the vehicle. I think @Cameron Chapman requested this yesterday.

### Pat Wells, 2024-04-17

@David Grosher ,  yes @Cameron Chapman  made that recommendation yesterday.  This flight and AAR is from 15 Apr.

### David Grosher, 2024-04-17

@Greg Fryer @Pat Wells I see that RTB popup on the GCS for low power came up.  I also see no overlapping data from the XCOMM datalog, however the XCOMM event log contains data for the incident.  I suspect that there is an issue with the XCOMM or one of its peripherals resulting in this behavior.  This will need further investigation.

### Sean Odell, 2024-05-20

Aircraft has arrived, inventory taken, and photos uploaded to RMA ticket.    Aircraft has been dropped off in Engineering.
@David Grosher @Cameron Chapman @Greg Fryer  @Pat Wells FYSA

### Greg Fryer, 2024-05-24

Aircraft has been stored on the aircraft case shelf.

### Cameron Chapman, 2024-05-29

Data attached does not seem to contain flight data in the flight data tool. @Liam Limon can the tool handle an AAR with multiple xcom logs? If not, can you please add this to the feature addition list as higher pri? 
[embedded: image-20240529-223540.png]

### Cameron Chapman, 2024-05-29

Flight data is in T95_VT439_240415_103147_vtl0051. No Xcom data for some reason. We could pull that from the aircraft likely.

### Cameron Chapman, 2024-05-29

VTOL voltage and current do not look abnormal (high takeoff current, but not abnormal at first glance). @David Grosher do you have anyone available to look into the recorded abort reasons. Do you know why XCOM data was not included in the AAR?
I can see if any EEs are available to pull the XCOM log. 
[embedded: image-20240529-225401.png]

### Cameron Chapman, 2024-05-29

@Rajesh Budhabhatti will pull logs.

### David Grosher, 2024-05-29

@Cameron Chapman I see XCOMM data in the log. But I don’t see any abort. It looks like it flew to the landing pattern.

### David Grosher, 2024-05-29

Note:  the XCOMM data in the event log covers the period of time when the event occurred, but the datalog does not.
From the GCS
[10:33:26.831] Show Caution(): Low Energy RTB
[10:33:26.831] MessageBoxTop(): Warning
[10:33:30.518] Show Caution(): Vehicle has entered landing pattern
[10:33:30.519] MessageBoxTop():
[10:33:34.091] roll fault: 4052
From XCOMM: 
[14:35:02.238 329.239] ap dbg: roll fault: 4052

Note the time offset XCOMM is in UTC. GCS is in local time. VTOL is in PST.

### Cameron Chapman, 2024-05-30

@David Grosher how do these sound for next steps? 
- pull the correct xcom data log @Rajesh Budhabhatti
- Check for what caused the low energy fault
- Check for potential roll fault causes
- Do you see anything that would indicate why the pause was auto aborted as in the descirption?

### David Grosher, 2024-05-30

@Cameron Chapman 
- The roll fault indication in the log happens on just about every transition to vtol flight. There is no need to investigate that. If anything the threshold needs to be opened up.
- I see no indication of a pause received by the AP systems. But there are a few joystick messages in the GCS debuglog. That will be a GCS activity to see if the correct message was sent and if so why it was rejected. 
[10:38:40.493] m_JoystickID 1: pan 33780, tilt 36529, turn 33780, lchovr
[10:38:40.494]     33036, alta 32819

### Rajesh Budhabhatti, 2024-06-03

I downloaded the flight logs as well as looked at the debug log. I see the low power but the battery seems to be fine. Tomorrow I will try to run the AV with power supply and see if it still gives me the low power indication. I will also replace the xcomm board and see if the problem persists. Power connector looks ok. We don’t have the battery here to see if it is weak.

### Cameron Chapman, 2024-06-03

@Rajesh Budhabhatti can you please upload those logs here and start an investigation report.  https://jenaero.sharepoint.com/:f:/r/sites/FlightSafety/Shared Documents/Incident Reports/VXEP-366 VXE 439 Three minutes after launch and transition the AV went into an automated RTB that could not be corrected?csf=1&web=1&e=HvhJGh
- What do you mean by “I see the low power” can you add a screenshot to the report?
- Please do not replace XCOM board.


@Ted Trowbridge or @Michael Berger is one of you available to investigate if the correct message was sent and if so why it was rejected.

### Rajesh Budhabhatti, 2024-06-03

HI Cameron,
Will do. I have started an investigation report and added the screenshots. I will include the link to the report in Jira ticket once I have some more information in it.
Raj

### Michael Berger, 2024-06-04

@Cameron Chapman “if the correct message was sent and if so why it was rejected.“ What message are you referring to? Are you talking about the pause? This is not really a GCS problem, it is a vehicle XComm, VTOL Controller, FW AP problem.

Also it says XCOM data missing from AAR. The XComm generates the list of files which the GCS downloads (this list is in fltfiles.txt)

### Cameron Chapman, 2024-06-04

@Michael Berger see @David Grosher's comment below. Can you please coordinate with him?

### Pat Wells, 2024-07-24

@Cameron Chapman any updates on this?  The aircraft physically has no damage so we’d like to expedite it’s return to the customer if possible.  @Sean Odell FYSA

### Cameron Chapman, 2024-07-24

@Pat Wells I had some hardware questions about the data, but it seems like most actions are with the SW team to review the data, provide an incident summary, and sort out message rejection questions. 
“This is the same AV that we had errors with some recent, at the time thought to be fuel cell, later thought to be the HLBs.  We quarantined those HLBs. “ Where is this documented? Can you link the incident? The cause of https://jenaero.atlassian.net/browse/VXEP-306  was the fuel cell.

### Sean Wendling, 2024-08-13

@Cameron Chapman I was referring to this new incident: https://jenaero.atlassian.net/browse/VXEP-532?atlOrigin=eyJpIjoiNDMyZDhjZWMwOGI2NDBhZWEzNGE5YjNhNGExZGYxZWMiLCJwIjoiaiJ9 . I will plan to update today. Just got back from the support trip

### Cameron Chapman, 2024-08-13

@Sean Wendling thanks for the correction. I will move my comment there.

### Pat Wells, 2024-08-15

@David Grosher @Cameron Chapman FYSA
This case was put into the plan to be worked to closure during the Sprint planning meeting held on 8/14.  8/19-8/23

### David Grosher, 2024-08-19

@Jason Scherer Can you start with this incident? Thanks.

### Jason Scherer, 2024-08-19

Coming up to speed on the issue. Will report here when I have an update.

### Jason Scherer, 2024-08-19

I have tracked the low battery RTB message from the GCS logs to the variables that drive it on the fixed wing ap code. It’s based on how long it takes to RTB versus battery endurance. So, for some reason the vehicle decided it didn’t have enough endurance to RTB which triggered the low battery RTB sequence of code.
I’m digging into how RTB time and battery endurance are calculated now.

### Jason Scherer, 2024-08-19

Ok after some analysis of the logs and code, I was able to replicate the issue on the HIL.
This is what happened in the incident. 
On the last flight, during the pre-flight phase, the vehicle was restarted in the middle of the launch wizard. I believe this was probably to resolve a sensor calibration error. Once the vehicle reconnected the launch wizard was not restarted. Instead, the operator proceeded from the same page of the launch wizard. 
This sequence results in the vehicle using an incorrect (default) battery model. The battery model is what the vehicle uses to calculate endurance. The battery model used by default has a severely reduced endurance. I’m guessing it’s a model of a really old battery that used to be used on a predecessor to the current VXE-30. This is the reason the vehicle activated a low battery RTB ~ 3 minutes into the flight. 
I was able to recreate this issue in our HIL by following the same steps.
Next steps: I will put some charts together with supporting data.

### Jason Scherer, 2024-08-20

Here is the XComm log with annotations that show the vehicle was reset during the launch wizard without restarting the launch wizard.


[embedded: image-20240820-154817.png]
[embedded: image-20240820-154843.png]

### Jason Scherer, 2024-08-22

I have updated the investigation document with a flight timeline. At this point I believe the root cause has been identified and documented. If there is any more information that should be added to the report let me know.

### David Grosher, 2024-09-05

@Dana Holley The CA from this investigation is an update to the Operators Manual. @Pat Wells FYSA

### Dana Holley, 2024-09-05

@Dave Grosher Copy that.

### Alexander Alan Arnold, 2024-12-10

@David Grosher Since the CA has been determined is D5 still the correct status?

### David Grosher, 2024-12-10

@Alexander Alan Arnold Linked a new CA for a manual update and changed the status.

### Jason Scherer, 2025-02-28

@David Grosher @Pat Wells I put the investigation report into the correct format as requested. The report is linked from the description. Let me know if you would like any changes.

### Stephan Johnson, 2026-10-08

Reclosing after test

## Attachments (9)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V439_240415_103147_pack.zip | archive | 2260 | 2024-04-17 | listed only |
| image-20240529-223540.png | image | 51 | 2024-05-29 | listed only |
| image-20240529-225401.png | image | 44 | 2024-05-29 | listed only |
| image002.png | image | 0 | 2024-06-03 | listed only |
| image003.png | image | 4 | 2024-06-03 | listed only |
| image004.png | image | 1 | 2024-06-03 | listed only |
| ~WRD0000.jpg | image | 1 | 2024-06-03 | listed only |
| image-20240820-154817.png | image | 837 | 2024-08-20 | listed only |
| image-20240820-154843.png | image | 293 | 2024-08-20 | listed only |
