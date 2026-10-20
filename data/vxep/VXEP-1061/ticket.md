# VXEP-1061: VXE 548 Command AUX SERVO fail

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-03-03
- **Updated:** 2026-07-13
- **Resolved:** 2026-07-13
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Greg Fryer
- **Creator:** Alexander Alan Arnold
- **Labels:** USASOC, Weekly-incident-tracker
- **Links:** relates to VXEP-600 (VXE 600 Communication errors); relates to FS2-3085 (Investigate VXEP-1061)
- **Customer:** USASOC
- **Vehicle Tail Number:** VXE 548
- **Vehicle Configuration:** VXE standard battery config trillium gimbal
- **Issue Status:** Vehicle has no issues with a default mission. Issue seems to be resolved.
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Investigation Report: Vehicle Investigation VXEP-1061.pptx
SharePoint Folder: VXEP-1061
5th Group OCONUS
Operator states that on two different GCS they receive the same warning {COMMAND_AUXSERVO} failed
Operator states that during trim check is when the warning pops up 

attached is data and a screenshot provided by the customer

## Corrective Action

Fixed wing is running old firmware and should be updated to match the 6.3.4 release.
The effect of long mission simulations should be investigated further.

## Plan

Have customer update fixed wing firmware to match the 6.3.4 release.
Continue investigating the effects on long mission simulation time.

## Root Cause

Issue appears to be caused by long mission simulations which lead to uplink outage and instability. With a default mission the issue did not occur, however, no further tests were completed to attempt recreating the issue.

## Comments (31)

### Alexander Alan Arnold, 2025-03-06

T95_V548_250303_174800_event
Time: 030:28.047  SysCmd Failed (cmd, priority): : 31  1
Time: 030:28.062  SysCmd Failed (cmd, priority): : 32  1   
I believe this is associated with the warning the operator is seeing. they describe it as popping up every time they get to the surface checks in the launch wizard.  I am not sure what it means though. I am trying to match it to the documents provided in the team's chat yesterday. 

I currently have them not flying the aircraft until I can determine if it is safe to fly or not. @David Grosher

### David Grosher, 2025-03-06

@Jason Scherer I thought this was related to the Trillium retract mechanism?

### Jason Scherer, 2025-03-06

@David Grosher Yes Aux0 is payload retract. Which doesn’t make sense, since the two commands being sent are servo center and disarm.
The SysCmd IDs can be found in an enumeration in the source file updown.h. The Fixed Wing, XComm, and GCS all use this enumeration for system commands. 
[embedded: image-20250306-171155.png]
The two command IDs that are failing are:
COMMAND_SERVOCENTER = 31
COMMAND_DISARM = 32
[embedded: image-20250306-171033.png]
Both commands are simply forwarded to FW meaning the XComm isn’t doing anything extra when forwarding these commands. So we have to look at the fixed wing code to determine what could be failing.

### Jason Scherer, 2025-03-06

This is interesting, I don’t see an FDR (which comes from the fixed wing ap) in any of the AAR packages.
The XComm log shows data being transmitted between fixed wing and xcomm, but this doesn’t necessarily mean it’s working. However, given the fact that only those commands are failing I’m inclined to think the serial link connecting those two processors is working.

### Jason Scherer, 2025-03-06

The error message in the event log for (_171620_event.txt) shows an error code right before the command fails which has a bit set that indicates losing link to the fixed wing ap.
[embedded: image-20250306-180444.png]
Fault value of 0x0005C000 with bit mask of #define VT_FAULT_LINK_APRX 0x00040000 is 1 indicating a fault with the aprx link. AP always refers to the fixed wing ap versus apm always refers to the vtol ap.
Since the aprx link fault occured ~7 seconds before the failed commands I think this data from XComm is recording that same event. 

This log of XComm data (_171620_xcl00144.csv) shows that the XComm did not receive data from the uplink for ~50 seconds (362-412). That number 50 seconds is very special. It just happens to be the timeout for the xcomm gcs connection. After the 50 seconds timeout the XComm will release the gcs connection and become available to new GCS connections. I’ll bet it we look in the XComm event log, we will see a gcs connection attempt around 412 seconds.
[embedded: image-20250306-180803.png]
Ok I don’t see a GCS connection timeout with a new link, but I do see this [14:26:42.718 418.718] ap link restored.

### Alexander Alan Arnold, 2025-03-06

Would the GCS being connected to the internet for an extended amount of time potentially cause an issue like this? @Jason Scherer

### Jason Scherer, 2025-03-06

@Alexander Alan Arnold Got pulled into some meetings, but after reviewing the data again I believe the failed system commands actually occurred around XComm clock of 436 in the plot below. After the big outage, but still a low point for receiving data.
As for the question about the internet. I wouldn’t initially think that would be the cause, but I won’t say it can’t be. If it was a firewall or something like that I don’t think any of the system commands would be successful. Also, since this occurred on two sperate system, I’d lean away from GCS hardware issues. 
The thing that strikes me as very odd is that it seems to be isolated to these specific commands at a specific part of the pre-flight process. I’m wondering if the motor tests right before the errors could indicate that we have a loose or intermittent connection that is vulnerable to vibration. 
My next thoughts are to spend more time reviewing datalogs. See if we can show that the uplink to xcomm always drops/has issues at the same time. Or if the link between xcomm and fixed wing is struggling. 
Additionally, we have another vehicle incident with failed system commands (V600). I’m wondering if there is a correlation. I was thinking about putting its avionics on a shake table and send repeated system commands to see if we can stimulate a failure with vibration. If so, that could point to a manufacturing defect.
The other thing that is odd is that the GCS shows the COMMAND_AUXSERVO is the failed command, but the event log shows servo center and disarm as the failed commands which makes more sense.

### Alexander Alan Arnold, 2025-03-06

Copy on the internet piece thank you 
So the operator is reporting that these warnings are first popping up during surface checks which are before the motor checks in the launch wizard

### Jason Scherer, 2025-03-06

You are right. I had the order wrong. Motor tests are after surface checks.
I’m also still wondering why we did not get FDRs in the AAR. The FDR data comes from the fixed wing. XComm should have pulled the FDR when the AAR was generated.

### Jason Scherer, 2025-03-06

The XComm fault VT_FAULT_LINK_APRX contained in the value 0x0005C00 right before the failed syscmds, indicates that the fixed wing has not received GCS messages in 5 seconds. The fact that the GCS is reporting this indicates that the downlink is working. So, the uplink is where the problem is. Somewhere along the GCS->XComm->FW path the messages are not making it.
[embedded: image-20250306-180444.png]
The error code does not contain a fault for the GCS->XComm link (VT_FAULT_LINK) or the FW->XComm link (VT_FAULT_LINK_AP). This Means that the GCS->XComm link might be working as expected. This would leave the XComm->FW link as the potential location of the dropped messages.

### Jason Scherer, 2025-03-06

Here is what XComm logs. At XComm clock 372, the fixed wing reports a 5 second timeout on GCS message. At 382, XComm reports a 1 second timeout on GCS messages. At 422 both faults are cleared.
[embedded: image-20250306-222654.png]

### Jason Scherer, 2025-03-06

In the GCS log (_171620_log.csv) There is a 51 second gap in log records right before the incident. The GCS is running a simulation of the flight during this time starting at 17:26:42. @Michael Berger Do you think this data indicates that the mission simulation blocks GCS updates such as logging and potentially uplink servicing? If so, that could be a contributing factor to what we are seeing. Maybe this mission is long and takes a lot of GCS time to simulate. Uplink data queues up while waiting causing XComm to think the link is lost? The XComm reports aplink fault (GCS->FW) starting at 17:26:42 which is when the mission simulation starts. I don’t see a huge increase in network traffic to the vehicle after the simulation completes. But after the sim completes and the link is “restored” the syscmds fail.
[embedded: image-20250306-233927.png]

### Jason Scherer, 2025-03-06

@Alexander Alan Arnold What do you think about having the customer retest with a default mission loaded to see if that resolves the issue. If my theory about long mission simulation time causing link instability, then that might work.

### Jason Scherer, 2025-03-06

I was able to recreate the link outage, with a long mission sim time, but not the failed system commands.
This is the recreation of link outage logged in the event log. Fault Status 0x0005C000 means ap link fault which occurs when the fixed wing doesn’t get messages from the GCS for more than 5 seconds.
[embedded: image-20250307-004622.png]
Additionally, the GCS log shows a 55 second outage of data
[embedded: image-20250307-004750.png]
We were hard wired to the vehicle for this test. I will try again tomorrow on a radio link to see if I get different results.

### Alexander Alan Arnold, 2025-03-07

I can have them do it I’m just curious how it affects the launch wizard process because flight surface checks is also before the mission sim as well. @Jason Scherer

### Jason Scherer, 2025-03-07

@Alexander Alan Arnold The GCS runs a mission sim in the mission checkout page of the LW. This page occurs before surface checks.
Mission Checkout->Maint Checkout->Battery Voltages Check->Surface Checks
This is the page I’m talking about, that can take quite a while to run the sim test. In this case with a large mission from a previous customer the GCS froze for ~40-50 seconds.
[embedded: image-20250307-165332.png]
I’m planning to run some more tests today to ensure that this is a contributing factor. If you want to hold off on the customer ask until I know more than that is ok. I just thought it would be a potentially easy test, but since they are OCONUS maybe it’s not so quick.

### Jason Scherer, 2025-03-07

@David Grosher FYSA. My current theory is that long complex missions are leading to uplink instability when the mission sim runs. At the very least I have proven that the vehicle stops receiving GCS messages during the sim which gets flagged as a GCS->FW timeout.
I have not yet proven that this is causing the syscmd failures, but at the very least we should consider looking into making the GCS Mission Sim a non-blocking function as it will freeze the GCS. Cody said that flight operators are disabling some mission sims on mission sync while flying to prevent the GCS lockup and temp loss of connection/control. His example was if an operator is simply moving a waypoint slightly, they don’t want the GCS to freeze on them and have accepted the risk of not running a mission sim.
This seems mainly to be a problem with longer missions.

### David Grosher, 2025-03-07

@Ted Trowbridge FYSA, see Jason’s comment below.

### Jason Scherer, 2025-03-07

Cody ran the long mission sim test on V600 again this morning using a radio connection. The AAR does not contain any syscmd failures, so that part is still a mystery.

### Alexander Alan Arnold, 2025-03-08

I had them remove the mission and create a new short mission and they said the errors did not populate so either that fixed it or letting the equipment sit for a couple days with no use somehow got the gremlins outs @Jason Scherer

### Jason Scherer, 2025-03-10

@Alexander Alan Arnold That’s very interesting. Are you/they considering this resolved? If not, I would like to get AAR from the new result with default mission. I would then like to have them put the old mission back on the GCS and attempt to recreate the issue to confirm if it is the cause. AAR for that would be great as well.

### Alexander Alan Arnold, 2025-03-10

@Jason Scherer I can ask them for the AAR. It is their only asset they have that is flyable, so I do not believe they will want to actively try and create errors on it. From a customer facing side I would consider this resolved.

### Alexander Alan Arnold, 2025-03-10

@Jason Scherer Added most recent AAR from customer

### Jason Scherer, 2025-03-10

@Alexander Alan Arnold That sounds reasonable. I have https://jenaero.atlassian.net/browse/VXEP-600 here which seems to have the same issue. I can experiment on that vehicle. I’ll write up a quick report to close out the investigation.

@David Grosher @Cody Smisek @Ted Trowbridge @Michael Berger 
FYSA. The customer tried a default mission, and the syscmd failures did not occur. In my opinion, this is not definitive, but it does provide additional data to suggest that this (complex missions causing long sim time, blocking uplink) is the cause. I will continue testing on V600 which had the same issue, to attempt to identify the root cause more definitively.

### Cody Smisek, 2025-03-10

@Alexander Alan Arnold @Jason Scherer Can they provide the problematic mission? or provide a written description of each mission element?

### Jason Scherer, 2025-03-10

@Alexander Alan Arnold I just realized that they have outdated firmware on the fixed wing ap. They are running 6.05o (6.2 release) and the rest of the software (GCS, XComm, VTOL) is from release 6.3. Can you have them update the fixed wing ap before they fly?

### Jason Scherer, 2025-03-10

@Alexander Alan Arnold @David Grosher Report created and linked in description. Please review.

### Pat Wells, 2025-03-17

@Alexander Alan Arnold did you advise the customer on their outdated firmware issue.

### Alexander Alan Arnold, 2025-03-17

They sent me a screen shot of the SW Page with the appropriate versions on the AV 
@Pat Wells

### Alexander Alan Arnold, 2025-04-15

@Pat Wells Having the customer update fw and create smaller missions alleviated this issue, recommend closing this out on customer side @Drew Hildreth

### Jackson Riley Curvin, 2026-07-13

Issue Resolved in Later versions of software with no customer complaints since.

## Attachments (16)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V548_250221_193027_pack.zip | archive | 903 | 2025-03-03 | listed only |
| T95_V548_250303_122148_pack.zip | archive | 1018 | 2025-03-03 | listed only |
| T95_V548_250303_171620_pack.zip | archive | 475 | 2025-03-03 | listed only |
| T95_V548_250303_174800_pack.zip | archive | 354 | 2025-03-03 | listed only |
| warning.jpg | image | 206 | 2025-03-03 | listed only |
| image-20250306-171033.png | image | 6 | 2025-03-06 | listed only |
| image-20250306-171155.png | image | 42 | 2025-03-06 | listed only |
| image-20250306-180444 (e3f50da4-a3bb-4ca1-8500-484155a34b7e).png | image | 6 | 2025-03-06 | listed only |
| image-20250306-180444.png | image | 6 | 2025-03-06 | listed only |
| image-20250306-180803.png | image | 25 | 2025-03-06 | listed only |
| image-20250306-222654.png | image | 9 | 2025-03-06 | listed only |
| image-20250306-233927.png | image | 97 | 2025-03-06 | listed only |
| image-20250307-004622.png | image | 11 | 2025-03-06 | listed only |
| image-20250307-004750.png | image | 10 | 2025-03-06 | listed only |
| image-20250307-165332.png | image | 362 | 2025-03-07 | listed only |
| T95_V548_250308_131416_pack.zip | archive | 246 | 2025-03-10 | listed only |
