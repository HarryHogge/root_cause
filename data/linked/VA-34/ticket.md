# VA-34: VXE 509 - Connection to vehicle lost while idle on the ground

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-08-07
- **Updated:** 2026-03-02
- **Resolved:** 2024-03-21
- **Reporter:** Connor Peebles
- **Assignee:** Connor Peebles
- **Creator:** Connor Peebles
- **Labels:** 8-28-Sprint, TIQUILA, TIQUILA-Blocker
- **Links:** relates to RMA-131 (VXE-509 230808 Tequila POST Delivery); relates to VA-40 (VXE 509 - NCR 1022 Investigation (Board #1 - SN APB-10424)); relates to VA-37 (VXE 509 - NCR 1165 Investigation (Board #2 - SN APB-10432)); relates to VXEP-10 (TPTR-85 VXE 509 Fixed Wing Autopilot Failed on First Flight); relates to VA-64 (VXE509 CA - Add conformal coating to inside of magacc2 board before can is installed); relates to VA-63 (VXE509 CA - Customer risks assessment. Statistical analysis of left over magacc2 boards.); relates to VA-62 (Quarantine old, un-labeled magacc2 assemblies that are in E-shop/ assemblies w/ no travelers); relates to VA-61 (VXE509 CA - Implement humidity check, Bake out MAGACC2 board before shield - Test the best route forward); relates to VA-59 (VXE509 CA - Implement checks on traveler for solder balls, F.O.D., and undried moisture before soldering the shield on.); relates to VA-60 (VXE509 CA - Require gloves for all avionics/ clean before CC/ bake out boards before CC & shield installation); relates to VA-54 (VXE509 Review C/CA TPTR-74 VXE 509 Fixed Wing Autopilot Failed on First Flight); relates to VA-53 (VXE509 Hands on trobleshooting. Identify cause and corrective actions.); relates to VA-51 (Create summary ppt slides for customer); relates to VA-50 (NCR 1349 Investiagtion); relates to VA-52 (VXE509 Determine parts for investigation, ok to rework or replace); relates to VXEP-480 (Create Master Document for Quality: IPC-A-610, IPC-A-620 Conformances and Engineering Deferrals/ Deviations); relates to VA-481 (VXE509 CA - Implement procedure updates to Magacc2 Assembly Procedure); relates to VA-503 (VXE509 CA - FixedWing AP Firmware Question: Relating to Magacc2 assembly (MPU-9250)); relates to ENG-2350 (Determine and document electronics IPC and other requirements we will use for assembly and inspection.  ); causes VA-597 (VXE 509 CA - Evaluiate: Swap to VTOL mag+acc if FixedWing Magacc2 isn’t working during flight)
- **Customer:** TIQUILA
- **Production Stakeholder:** Desiray Johnston
- **Other Stakeholder (as required):** Matt Philley

## Description

8D Link: 8D flight 509.pptx
Flight Safety Report Link: Vehicle Investigation V509.pptx (sharepoint.com)
NCR AC509 - RMA - AP (Green) Failure during Pre-Launch
APB-10460
From Carson “509 had an AP (FW AP) failure (on the ground) at SMR. Early diagnosis is the mag board (MagAcc) failed, so the AP shut down. Liam has pulled that AP and is putting in a new one.”
”I'm not sure what the exact message was, but there was a string of failure in the debug. The outward indication was that connection to the vehicle was lost while idle on the ground. Connecting to the XComm showed no serial or traffic from the AP on the Throughput page.”

Logs from Dexter while trying to connect: 
[embedded: MicrosoftTeams-image (1).png]
The non-conformance has already been resolved: Complete AP was replaced in the 509 Avionics Box, see NCR 1349 for those details
The purpose of this Jira is to determine the cause of the Vehicle Incident.

## Corrective Action

- [VA-59] VXE509 CA - Implement checks on traveler for solder balls, F.O.D., and undried moisture before soldering the shield on. - Jira (atlassian.net)
- [VA-481] VXE509 CA - Implement procedure updates to Magacc2 Assembly Procedure - Jira (atlassian.net)
- [VA-60] VXE509 CA - Require gloves for all avionics/ clean before CC/ bake out boards before CC & shield installation - Jira (atlassian.net)
- [VA-61] VXE509 CA - Implement humidity check, Bake out MAGACC2 board before shield - Test the best route forward - Jira (atlassian.net) (setting aside longer term experiment)
- [VA-62] Quarantine old, un-labeled magacc2 assemblies that are in E-shop/ assemblies w/ no travelers - Jira (atlassian.net)
- [VA-63] VXE509 CA - Customer risks assessment. Statistical analysis of left over magacc2 boards. - Jira (atlassian.net)
- [VA-64] VXE509 CA - Add conformal coating to inside of magacc2 board before can is installed - Jira (atlassian.net)
- [ENG-2017] Create Master Document for Quality: IPC-A-610, IPC-A-620 Conformance - Add Standard solder temps and techniques.

## Plan

Per coordination with LM, this TPTR has been closed
JSMT 230918.pptx

## Issue Status

8/8: The incident maggacc board 3.3V test point is showing 2.7V. The 5.0V test point is showing 2.5V. This suggests some failure around the voltage regulators on the maggacc board. I would like to take the shielding can off to get a look at the components
After probing inside this while powered to attempt to narrow down where the voltage was dropping, there was a small spark around R1. After powercycling the board it was noted that the 5V and 3.3V test points were back to their correct values. The board was then able to successfully connect to the GCS.

8/9: I suspect that there was F.O.D. bridging to the RF shield can (GND in this circuit), potentially making a voltage divider.
I suspect the F.O.D. made enough contact to induce a spark which may have separated the bridge, allowing normal operation. 3.3V TP = 3.3V and 5.0V TP = 5.0V 

There is no indication that the previous NCRs (1022, 1165, and 1349) are caused by an adjacent or reoccuring problem in AC509

## Root Cause

Excessive solder balls, F.O.D. and potential corrosion was found on the component side of the magacc2 board (1710P01A), potentially as a result of missed quality check. This caused a short that inhibited functionality of the board.

## Comments (34)

### Matt Philley, 2023-08-08

Added link to NCR
Updated details, dispo, SN info, etc. to NCR
@Sean Odell FYI AC 509 VIT2 ticket

### Matt Philley, 2023-08-08

Need to locate the removed AP board from Liam. Expected to be SN APB-10460

### Matt Philley, 2023-08-08

AC 509 had a lot of NCRs… it looks like we replaced the Green AP board a couple of times:
5/18/23 - NCR 1022 - Flight Test NCR for DO NOT LAUNCH suspect Magnetometer and dispo remove and replace Green AP
6/19/23 - NCR 1165 - Flight Test NCR for GPS Signal found corrosion on AP Board and removed and replaced Green AP

### Matt Philley, 2023-08-08

@Marc Richardson 
At this time my recommendation from Quality is that we do not deliver this AC back to the Customer until we can investigate at least AP Board #1 (SN 10424) and AP Board #3 (SN 10460) to see if it was the same failure which may indicate something else in the aircraft is causing the boards to fail. 
(Duplicated in RMA Jira Ticket)

### Sam Miller, 2023-08-08

@Matt Philley Agreed

### Matt Philley, 2023-08-08

All relevant boards handed off to @Connor Peebles about an hour ago to facilitate this investigation with relevant NCR tags, RMA tag, and paperwork (mostly).

### Connor Peebles, 2023-08-08

Made child issues for the separate NCRs, will also keep the NCRs up to date from engineering as investigation progresses

### Matt Philley, 2023-08-08

[10:26 AM] Carson Buckley
Vehicle has been flown, passed all 3 checks without issue.
[10:27 AM] Carson Buckley
Transponder cable [106-103720 inside the Avi Box] was found to be inop during ironbird checkout, so that would be a possible investigation lead. That cable was removed and retained, check with Liam.
@Connor Peebles in case that is helpful

### Connor Peebles, 2023-08-08

The transponder cable is pinned out correctly and was beeped out. Was the transponder cable tested independently of 509’s avi box? Because if not that might narrow the problem down to 509’s xcomm

### Matt Philley, 2023-08-08

@Connor Peebles worth a follow-up with Carson, Liam, and/or Ben N
Carson: “The cable was tested multiple ways while installed and failed each one. It was replaced and the box re-tested, which then passed. Ben Norris had the cable last, he was going to put it on the cable tester to verify. Manually beeping it out wouldn't reveal a cross-short unless you're specifically looking for it, so could be FOD in the ODU.”

### Connor Peebles, 2023-08-08

I was specifically looking for a cross short (didn’t find one)

### Connor Peebles, 2023-08-08

On NCR 1349: The maggacc board 3.3V test point is showing 2.7V
the 5.0V test point is showing 2.5V. This suggests some failure around the voltage regulators on the maggacc board. I would like to take the shielding can off to get a look at the components.
This is actually in an acceptable range for most components on the board (but it is not normal for the board), so it may be that it is messing with the SPI bus and that is why there is no connection.

### Cameron Chapman, 2023-08-08

Good finding.
Sent the following to ask for clearance to proceed. 
Hello Sam, (copy of a message I sent in case email is easier to track)
For the TIQUILA AP issue on 509, are we ok to modify the PCBs to troubleshoot? I thought we should ask given the visibility
From https://jenaero.atlassian.net/browse/VIT2-336 
The maggacc board 3.3V test point is showing 2.7V
the 5.0V test point is showing 2.5V. This suggests some failure around the voltage regulators on the maggacc board. I would like to take the shielding can off to get a look at the components.
This is actually in an acceptable range for most components on the board (but it is not normal for the board), so it may be that it is messing with the SPI bus and that is why there is no connection.
For future troubleshooting, we may want to remove the magacc board, which would require cutting pins.

### Connor Peebles, 2023-08-08

Referring to the previous comment, we got approval to do so.

### Connor Peebles, 2023-08-09

From the child issue for NCR1349: “Opening up the Maggacc board rf shield allowed examination of the boards components. A great amount of F.O.D. and corrosion was found, including large solder balls (not suspended in dried flux).
[embedded: IMG_0261.jpg]
[embedded: IMG_0264.jpg]
[embedded: IMG_0263.jpg]
[embedded: IMG_0262.jpg]
[embedded: IMG_0266.jpg]
[embedded: IMG_0260.jpg]
[embedded: IMG_0265.jpg]
“

### Connor Peebles, 2023-08-09

Also from child issue for NCR 1349 (most recent issue): “After probing inside this while powered to attempt to narrow down where the voltage was dropping, there was a small spark around R1. After powercycling the board it was noted that the 5V and 3.3V test points were back to their correct values. The board was then able to successfully connect to the GCS.
[embedded: IMG_5529.JPG]

I suspect that there was F.O.D. bridging to the RF shield can (GND in this circuit), potentially making a voltage divider.
[embedded: image-20230809-234310.png]
I suspect the F.O.D. made enough contact to induce a spark which may have separated the bridge, allowing normal operation.
To confirm, we can try to replicate the outcome.”


[embedded: IMG_0261 edited.jpg]
Noticeably, there is the most corrosion along the shield - which is connected to GND - and the 12V rail. This is indicative of voltage gradient corrosion.

### Cameron Chapman, 2023-08-10

Converted this to an EA internal incident. All future incidents should be filed in the ENG project. VIT2 may turn into the customer filed incidents project.

### Matt Philley, 2023-08-11

@Connor Peebles what happened to the summary table of SN’s per Incident?
I see you found the cause to the most recent NCR, AP #3 (SN APB-10460), which is great, but did we get an answer about AP#1 (SN APB-10424)? The aircraft issues seemed similar so we wanted to make sure the causes were different before breaking this aircraft loose with the new AP#4 (SN 10512)
I think the most definitive would be to open up the RF Shield to see if it shows the same solder balls and corrosion, however would that impact your ability to troubleshoot the board if that is NOT the cause?

### Connor Peebles, 2023-08-11

@Matt Philley Converting to an EA internal incident wiped all the fields besides description. Then I was requested to separate the NCR Jira tickets into their own issues, so see “relates to” linked issues.
To summarize NCR 1022 it had a pitch rate of 0.2 calibrated on it, which basically means it thinks it is pitching up constantly. I haven’t gotten an answer as to whether this will cause a “Do not launch” error.
I’ll happily open up the can on #1 though just to be sure.

### Connor Peebles, 2023-08-11

@Greg Fryer @Cameron Chapman Moving this Jira into working corrective actions, let us know if there are more corrective actions we can pursue. @Matt Philley

### Connor Peebles, 2023-08-11

FYI @Liam Limon

### Matt Philley, 2023-08-11

@Desiray Johnston @Trevor Gronner we will need some Production Engineering support on some of these CA’s I think in Electronics. We can circle up on Monday to go over the investigation findings and recommended CA’s.

### Cameron Chapman, 2023-08-21

@Connor Peebles @Matt Philley what is the risk to our current fleet for this or related issues? Do we need a containment? Considering that this made it to a customer, I think this needs more consideration.

### Connor Peebles, 2023-08-21

@Cameron Chapman @Matt Philley I think this problem was caused by rushed execution of a fixed NCR (Lawton era). The Magacc2 board did not have a serial number/lot number sticker on it. I think the risk is low for the current fleet. More thorough risk assessment underway.
As far as containment, @Liam Limon and @Brad Crampton were planning on quarantining the un-labeled overstock of the Magacc2 assembly left over from (Lawton Era).

### Connor Peebles, 2023-08-21

Here is a picture of a random other magacc2 board that was peeled open: It is perfectly clean, lacking corrosion or solder balls.
[embedded: IMG_0268.jpg]

### Connor Peebles, 2023-08-22

@Matt Philley Asked about my method of opening up these shield cans, and I can summarize it as the dustiness seen on the original postings of the 509 magacc board is from opening it. That said, I still believe my analysis to be correct…
I opened the first 2 shield cans using a small Dremel on the corner until I could peel open the can. This can account for the dustiness you see in the original image that I left out of my analysis. Below is a different magacc2 board cut open in the same exact method:
[embedded: IMG_0284.jpg]
You can probably identify the dustiness I mentioned, but also the lack of solder balls and voltage gradient corrosion.
See below for an updated image of 509’s magacc2 board, with attempted cleaning of the dustiness of opening it up:
[embedded: IMG_0283.jpg]
Corrosion and solder balls still evident, with attempted dustiness removal

### Matt Philley, 2023-08-22

@Cameron Chapman Customer Impact should be evaluated as part of the 8D process. @Brad Crampton is the QE assigned to this investigation, so Brad should be aligning with the rest of the team and then communicating with Marc and the Management team to assess the risk and coordinate engagement with the Customer.
@Brad Crampton has that happened yet? I lost track of this investigation.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent

### Connor Peebles, 2023-09-18

@Cameron Chapman If possible, could you review the investigation report for this incident: Vehicle Investigation V509.pptx (sharepoint.com)

### Cameron Chapman, 2023-09-19

Great report @Connor Peebles , please do the following:
- Remove things that are done from inv plan.
- Should we open a corrective action to document and train standard soldering iron temps and techniques?
- Copy the slide info into each linked CA.
- The software corrective action is not clear. Can you please restate it in terms understandable to the average reader? What specifically are you recommending? Swap to VTOL mag+acc if FW isn’t working? Notify user in this condition and command a RTB or immediate landing? Can you link to the software tasks already existing in CA?

### Connor Peebles, 2023-09-19

Thanks @Cameron Chapman 
2. We could create a master document such like will be made for this [ENG-2017] Create Master Document for Quality: IPC-A-610, IPC-A-620 Conformances with engineering specified solder temps
4. Yes I suggested a corrective action that instead of having the FW AP continually try to re-connect to the Magacc2 board, it should instead swap to the VTOL mag+acc. Kurt told me in person that this would be taken care of in the Unified Autopilot (UAP), but obviously that is a long term solution and I cannot find a specific Jira ticket for that.

### Cameron Chapman, 2023-09-19

“I cannot find a specific Jira ticket for that.” Can you please create a FS task for that and assign to Dave G, then linkit in the CA? They can always link it and close if its a duplicate of another. 
After that, it seems like this should be ready to review for closure. Can you please update https://jenaero.atlassian.net/browse/VXEP-10  then ask Glenn and Greg if ready to move to closure? 
Great work.

### Connor Peebles, 2023-09-22

@Cameron Chapman Task for FS to evaluate created and linked: [VA-597] VXE 509 CA - Evaluiate: Swap to VTOL mag+acc if FixedWing Magacc2 isn’t working - Jira (atlassian.net)
https://jenaero.atlassian.net/browse/VXEP-10 was closed without me intervening.
Assigning to you Cameron for official investigation review stage

### Cameron Chapman, 2023-09-22

Per coordination with LM, this TPTR has been closed. Great work Connor!
JSMT 230918.pptx

## Attachments (15)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| MicrosoftTeams-image (1).png | image | 1236 | 2023-08-07 | listed only |
| AC 509 Updated Avionics Enclosure Traveler.JPG | image | 3922 | 2023-08-08 | listed only |
| IMG_0260.jpg | image | 6205 | 2023-08-09 | listed only |
| IMG_0261.jpg | image | 6139 | 2023-08-09 | listed only |
| IMG_0262.jpg | image | 5834 | 2023-08-09 | listed only |
| IMG_0263.jpg | image | 5904 | 2023-08-09 | listed only |
| IMG_0264.jpg | image | 6052 | 2023-08-09 | listed only |
| IMG_0265.jpg | image | 5767 | 2023-08-09 | listed only |
| IMG_0266.jpg | image | 5816 | 2023-08-09 | listed only |
| IMG_5529.JPG | image | 9525 | 2023-08-09 | listed only |
| image-20230809-234310.png | image | 112 | 2023-08-09 | listed only |
| IMG_0261 edited.jpg | image | 317 | 2023-08-11 | listed only |
| IMG_0268.jpg | image | 6082 | 2023-08-21 | listed only |
| IMG_0283.jpg | image | 5458 | 2023-08-22 | listed only |
| IMG_0284.jpg | image | 5101 | 2023-08-22 | listed only |
