# VXEP-286: VXE 603 HLB Data Connector Shorted. Evaluate equipment.

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-02-23
- **Updated:** 2025-06-10
- **Resolved:** 2025-06-10
- **Reporter:** Cameron Chapman
- **Assignee:** Rajesh Budhabhatti
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-258 (Potting concerns. DP100 may be too viscous or cure too fast to properly wick between ODU solder cups. )
- **Production Stakeholder:** Kyle DeBernardi
- **Other Stakeholder (as required):** Matt Philley
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Links for reference AC 603 - SCO - Branch ODU Loose and Caused Short
https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/NCR%20List/DispForm.aspx?ID=2459&commentId=9&e=eolIiQEWWU-Bu8qHyExs_Q&at=15&CT=1708732262853&OR=OWA-NT&CID=f2ac072a-9ed7-0ba0-17df-ba564b63c3e2&WSL=1&xsdata=MDV8MDJ8fGRjZGFmZDMxMDQ3MDQ4MjU2NzZmMDhkYzM0Y2E2MzhjfDE4NzZmNjFhM2JkYjQ4NDNhZTcwNzVlZDBjY2I3NDA0fDB8MHw2Mzg0NDMyOTEwMzc5NTE4NTV8VW5rbm93bnxWR1ZoYlhOVFpXTjFjbWwwZVZObGNuWnBZMlY4ZXlKV0lqb2lNQzR3TGpBd01EQWlMQ0pRSWpvaVYybHVNeklpTENKQlRpSTZJazkwYUdWeUlpd2lWMVFpT2pFeGZRPT18MXxMMk5vWVhSekx6RTVPakZpWmpobE9HVmlNVFUyWXpRNE9EazRZMk5rT1dKa1pHRTNPR0k1TURnMFFIUm9jbVZoWkM1Mk1pOXRaWE56WVdkbGN5OHhOekE0TnpNeU16QXlPVFUyfDI1ZmNlNTczN2YwYTQ2NGM2NzZmMDhkYzM0Y2E2MzhjfDM1ODE1ZmVmYzg4ZDRmMWZiNjM0MzU5M2NjZGMyNjM3&sdata=b0paTlNieVNiOHB0cFhIVDQ0OXF1dnJidjllVmFOZmwyakQxUXlDUitMcz0%3D&ovuser=1876f61a-3bdb-4843-ae70-75ed0ccb7404%2Cchapman%40edgeautonomy.io 
The FWAP in the dropped box was also involved in the shorting incident of AC 603 - SCO - Branch ODU Loose and Caused Short. This FWAP should also be evaluated for potential damage from that incident before reusing.

## Plan

@Laszlo Juhasz can you please inspect this XCOM board with @Rajesh Budhabhatti on Monday? I think it is on @Katherine Duberg's desk. We want to determine which pins shorted to explain the behavior notes (blinker lights came on) and if there is any damage that could have propagated to any other components in the avionics box. We can look for damaged components or conductors as well.
As a lower priority, we could see if replacing the damaged component (Iikely CAN transceiver) gets it operational for a ground asset
@Carson Buckley do you know if the shorted branch cable or connector are still available? They could contain some evidence.
603 board is fried.

## Comments (10)

### Cameron Chapman, 2024-02-23

Chat thread so far. [3:33 PM] Cameron Chapman
What is the status of 604? I have some questions on the electronics that should be answered before they are cleared for flight
[3:33 PM] Cameron Chapman
Reviewing NCR 2304, I think the UAI disposition for the remaining hardware needs some additional review. @Ryan Ferguson did you account for any other CAN devices that were connected at the time (HLB, was the CW connected?). Did you inspect the CAN transceiver to see if that damage could have propagated to any other connections (ex gnd)? Do we have evidence from PCB or connector inspection indicating which pins shorted? Carson reported the blinker lights turned on, which sound more like power on the ground line rather than CAN. I think all equipment involved should be held until these questions are answered.
[3:34 PM] Cameron Chapman
See NCR 2304
2459
 
[3:42 PM]
Cameron Chapman added Connor Peebles to the chat and shared all chat history.
[3:42 PM] Ryan Ferguson
Carson commented in that NCR - "IIRC this was during intial SCO checkout, so no other surfaces were connected yet."  
 
I don't believe we have any reason to believe the center wing was suspect in this incident.  The only CAN devices in the fuselage are the X-comm and the HLB heater controller board.  
[3:43 PM] Cameron Chapman
that is good for the CW. There is still possible damage in the HLB and other fuse electronics if the short propagated or shorted to a different pin
[3:43 PM] Carson Buckley
Blinkers came on during the initial prep for firmware and calibration, so the center wing would not have yet been connected, but very shorltly after would have been.
[3:44 PM] Cameron Chapman
Carson Buckley
Blinkers came on during the initial prep for firmware and calibration, so the center wing would not have yet been connected, but very shorltly after would have been.

Was the CW connected at any time to this fuselage? Damage possible if so. The blinkers aren't a 100% indicator of issue or not in this case
[3:45 PM] Ryan Ferguson
Also if we are bringing this back into question, Matt Philley should we reopen this NCR for another round of investigations?
[3:45 PM] Cameron Chapman
I think yes
[3:45 PM] Carson Buckley
Can't say for 100% certain that it wasn't at any point while it was shorted, but it absolutely was / has been after the XComm was reworked.
[3:46 PM] Cameron Chapman
Carson Buckley
Can't say for 100% certain that it wasn't at any point while it was shorted, but it absolutely was / has been after the XComm was reworked.

the main before/after we should focus on is before/after the shorting connector was removed. Damage is more likely from that vs with an already damaged xcom with the main short removed
[3:47 PM] Carson Buckley
You can probably pull the log files and check when each was powered on, go back to the earliest on that day that the XComm was powered and check if the VTEV has a boot around that same time.
[3:47 PM] Carson Buckley
Probably the only way to be sure, since we don't know otherwise.
[3:49 PM] Cameron Chapman
Ok. In that case, I think the CW and fuselage should be red tagged at least until we have done more connector/PCB inspection
[3:51 PM] Cameron Chapman
Links for reference AC 603 - SCO - Branch ODU Loose and Caused Short
https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/NCR%20List/DispForm.aspx?ID=2459&commentId=9&e=eolIiQEWWU-Bu8qHyExs_Q&at=15&CT=1708732262853&OR=OWA-NT&CID=f2ac072a-9ed7-0ba0-17df-ba564b63c3e2&WSL=1 
[3:55 PM] Cameron Chapman
Will track engineering evaluation here https://jenaero.atlassian.net/browse/VXEP-286 
VXEP-286: VXE 603 HLB Data Connector Shorted. Evaluate equipment.
[3:56 PM] Ryan Ferguson
It is worth noting that functional checks will be about all we can do for the HLB battery.  It's sealed inside the housing where we can't access in a non-destructive method.  If Engineering doesn't like it, we will have to scrap the battery.
[3:56 PM] Cameron Chapman
Understood. I think we can start by looking more closely at the connector, harness (if we still have them), and the PCB for any visible damage, might also be able to find more info with a DMM
[3:57 PM] Cameron Chapman
There is a good chance the damage is only on the XCOM, but until we have evaluated more, I think we should red tag the involved equipment.

### Cameron Chapman, 2024-02-23

@Laszlo Juhasz can you please inspect this XCOM board with @Rajesh Budhabhatti on Monday? I think it is on @Katherine Duberg's desk. We want to determine which pins shorted to explain the behavior notes (blinker lights came on) and if there is any damage that could have propagated to any other components in the avionics box. We can look for damaged components or conductors as well.
As a lower priority, we could see if replacing the damaged component (Iikely CAN transceiver) gets it operational for a ground asset
@Carson Buckley do you know if the shorted branch cable or connector are still available? They could contain some evidence.

### Matt Philley, 2024-02-26

@Cameron Chapman @Laszlo Juhasz Branch Cable SN F-S100540 was the cable installed in AC603 when the shorting incident occurred. The cable is still in the Final Assy NCR cage. If someone would like to grab it to investigate let me know and I can hand it off. 
Carson is out this week in PTO, so @Kyle England and @Dominic Garcia are the points of contact for SCO this week.

### Matt Philley, 2024-02-26

@Cameron Chapman @Laszlo Juhasz Dropped Avionics Box from 603 is in the Electronics NCR cage. Let me know or one of the Inspectors around there and we can unlock the cage to hand it off

### Rajesh Budhabhatti, 2024-02-26

@Carson Buckley Hi Carson, I received this board from Katherine. Preliminary examination of connector going to blinking LED did not reveal any shorts so I would like to get my hands on cable to see if it is shorted. Do you have the cable?

### Carson Buckley, 2024-03-04

@Rajesh Budhabhatti If I recall, this short was caused by FOD that was bridging pins on the main Alden connector, solder side. The FOD was removed and the box was verified funcaitonal, then returned to Electronics for closeout. It was damaged (dropped) after this point and a replacement was used for the vehicle.

### Rajesh Budhabhatti, 2024-03-04

Thank you Carson,
Laszlo and I plan to check out this board this afternoon. I will get back to you with our finding.
Raj
From: Carson Buckley (Jira) <jira@jenaero.atlassian.net>
Sent: Monday, March 4, 2024 7:53 AM
To: Raj Budhabhatti <rbudhabhatti@edgeautonomy.io>
Subject: [JIRA] Carson Buckley mentioned you on https://jenaero.atlassian.net/browse/VXEP-286#icft=VXEP-286
You don't often get email from jira@jenaero.atlassian.net. Learn why this is important<https://aka.ms/LearnAboutSenderIdentification>
Carson Buckley mentioned you on an issue
VXE Problems/https://jenaero.atlassian.net/browse/VXEP-286#icft=VXEP-286 VXE 603 HLB Data Connector Shorted. Evaluate equipment.  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌
Carson Buckley mentioned you on an issue
VXE Problems<https://jenaero.atlassian.net/browse/VXEP?atlOrigin=eyJpIjoiOWYxMDE1NjhhZjkwNDFiNjk1MzBmZWYxNzdhZjMyNTUiLCJwIjoiaiJ9>
/
VXEP-286<https://jenaero.atlassian.net/browse/VXEP-286?atlOrigin=eyJpIjoiOWYxMDE1NjhhZjkwNDFiNjk1MzBmZWYxNzdhZjMyNTUiLCJwIjoiaiJ9>
VXE 603 HLB Data Connector Shorted. Evaluate equipment. <https://jenaero.atlassian.net/browse/VXEP-286?atlOrigin=eyJpIjoiOWYxMDE1NjhhZjkwNDFiNjk1MzBmZWYxNzdhZjMyNTUiLCJwIjoiaiJ9>
[Image removed by sender.]
Carson Buckley 7:53 AM PST
@Rajesh Budhabhatti If I recall, this short was caused by FOD that was bridging pins on the main Alden connector, solder side. The FOD was removed and the box was verified funcaitonal, then returned to Electronics for closeout. It was damaged (dropped) after this point and a replacement was used for the vehicle.
[View issue]
Get Jira notifications on your phone! Download the Jira Cloud app for Android<https://play.google.com/store/apps/details?id=com.atlassian.android.jira.core&referrer=utm_source%3DNotificationLink%26utm_medium%3DEmail> or iOS<https://itunes.apple.com/app/apple-store/id1006972087?pt=696495&ct=EmailNotificationLink&mt=8>.
Manage notifications<https://jenaero.atlassian.net/jira/settings/personal/notifications?emailPreferences=true&atlOrigin=eyJpIjoiOWYxMDE1NjhhZjkwNDFiNjk1MzBmZWYxNzdhZjMyNTUiLCJwIjoiaiJ9#emailpreferences>  •  Give feedback<https://surveys.atlassian.com/jfe/form/SV_9X3zi1X4q1gKsqF>  •  Privacy policy<https://www.atlassian.com/legal/privacy-policy>
[cid:image002.png@01DA6E0A.3FE19E50]
[cid:image002.png@01DA6E0A.3FE19E50]
- - WARNING: This email originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe. **

### Matt Philley, 2024-03-05

Branch Cable SN F-S100540 dropped off to Raj

### Laszlo Juhasz, 2024-05-13

Just finished a basic function test (Connor and me) and the XCOM board is defective.  While it shows no significant power demand the servo power and other power and the indication LEDs are not lighting or blinking. My suggestion is to scram this board while the cable could be used after careful re-testing.

### Rajesh Budhabhatti, 2024-05-20

603 board was involved in unrelated testing and got further damaged. It could not be booted up. See the investigation report here: 
C:\JAI Vault 1\Shared\Sandbox\Raj B\Investigation Reoirt VXE-603 Connector short.docx

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image002.png | image | 4 | 2024-03-04 | listed only |
| image003.png | image | 1 | 2024-03-04 | listed only |
| ~WRD0001.jpg | image | 1 | 2024-03-04 | listed only |
