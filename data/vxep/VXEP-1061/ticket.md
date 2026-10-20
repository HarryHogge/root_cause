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

### Jason Scherer, 2025-03-06

In the GCS log (_171620_log.csv) There is a 51 second gap in log records right before the incident. The GCS is running a simulation of the flight during this time starting at 17:26:42. @Michael Berger Do you think this data indicates that the mission simulation blocks GCS updates such as logging and potentially uplink servicing? If so, that could be a contributing factor to what we are seeing. Maybe this mission is long and takes a lot of GCS time to simulate. Uplink data queues up while waiting causing XComm to think the link is lost? The XComm reports aplink fault (GCS->FW) starting at 17:26:42 which is when the mission simulation starts. I don’t see a huge increase in network traffic to the vehicle after the simulation completes. But after the sim completes and the link is “restored” the syscmds fail.
[embedded image-20250306-233927.png]

### Jason Scherer, 2025-03-06

@Alexander Alan Arnold What do you think about having the customer retest with a default mission loaded to see if that resolves the issue. If my theory about long mission simulation time causing link instability, then that might work.

### Jason Scherer, 2025-03-06

I was able to recreate the link outage, with a long mission sim time, but not the failed system commands.
This is the recreation of link outage logged in the event log. Fault Status 0x0005C000 means ap link fault which occurs when the fixed wing doesn’t get messages from the GCS for more than 5 seconds.
[embedded image-20250307-004622.png]
Additionally, the GCS log shows a 55 second outage of data
[embedded image-20250307-004750.png]
We were hard wired to the vehicle for this test. I will try again tomorrow on a radio link to see if I get different results.

### Alexander Alan Arnold, 2025-03-07

I can have them do it I’m just curious how it affects the launch wizard process because flight surface checks is also before the mission sim as well. @Jason Scherer

### Jason Scherer, 2025-03-07

@Alexander Alan Arnold The GCS runs a mission sim in the mission checkout page of the LW. This page occurs before surface checks.
Mission Checkout->Maint Checkout->Battery Voltages Check->Surface Checks
This is the page I’m talking about, that can take quite a while to run the sim test. In this case with a large mission from a previous customer the GCS froze for ~40-50 seconds.
[embedded image-20250307-165332.png]
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
