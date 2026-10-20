# VXEP-326: AS150 pin connectors diagnosing the reason the parts are OOS when assembled (could be pin dimensions, threads too deep, etc).  Identify long term C/CAs and short term workarounds. Ex 107-102189 114-106508

- **Issue type:** Sub-task
- **Status:** In Process
- **Priority:** High
- **Created:** 2024-04-08
- **Updated:** 2025-12-31
- **Reporter:** Cameron Chapman
- **Assignee:** Nina Menon
- **Creator:** Cameron Chapman
- **Parent:** VXEP-553 AS150 Plug/Pin Connector Issue Systemic Collector
- **Links:** relates to VXEP-386 (Develop Replacement for AS150 Connections); relates to VXEP-540 (Recent AS150 Connectors causing intermittency and difficulty to connect and disconnect correctly and safely (AS150 Socket Issues)); is duplicated by ENG-2655 (107-102189 Pin Depth Tolerance Issue); relates to ENG-2734 (Update AS150 drawings ); relates to VXEP-761 (VXE 557 Smoking Smell from Fuselage after connecting main battery)

## Description

Ex: 107-102189, parent ticket

Related NCRs
- https://jenaero.sharepoint.com/sites/HuntsvilleQualityAssurance/Lists/NCR%20List/DispForm.aspx?ID=148&commentId=4&e=vGRmq3RxZUSJDVItcUPRsQ&at=15&xsdata=MDV8MDJ8Y2NoYXBtYW5AZWRnZWF1dG9ub215LmlvfGY4NGQxOGExOTA0MzRiM2JhMjc1MDhkY2MxMWQ4NzUwfDE4NzZmNjFhM2JkYjQ4NDNhZTcwNzVlZDBjY2I3NDA0fDB8MHw2Mzg1OTc1Nzk3ODI2NDQ1Mzl8VW5rbm93bnxUV0ZwYkdac2IzZDhleUpXSWpvaU1DNHdMakF3TURBaUxDSlFJam9pVjJsdU16SWlMQ0pCVGlJNklrMWhhV3dpTENKWFZDSTZNbjA9fDB8fHw%3D&sdata=bWI2a1R4cG41bzFWdkpHNm9JZVBpYXc0SjlDVnRqaWc3Z2tNSHZnMUQxST0%3D&CT=1724169422624&OR=OWA-NT-Mail&CID=d7e2458e-f178-d694-dbb6-ddaf67b9f2c0&clickParams=eyJYLUFwcE5hbWUiOiJNaWNyb3NvZnQgT3V0bG9vayBXZWIgQXBwIiwiWC1BcHBWZXJzaW9uIjoiMjAyNDA4MDkwMDYuMTEiLCJPUyI6IldpbmRvd3MgMTAifQ%3D%3D
- https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/NCR%20List/DispForm.aspx?ID=4072&e=iEKdjp

## Plan

- Nina and Luca to meet with Ben today to document all SLO workarounds and transfer that list to Huntsville. Once that is done, we can resume power harness production. Still some risk of this contributing to the mating issue, but initial indications are low. FYI @Desiray Johnston @Ryan Forcier 
- Please do this for all AS150 connectors (pins and sockets of both connector types)? Report what was previously done in SLO, but not yet transferred to HSV for recent batches. https://jenaero.atlassian.net/browse/VXEP-560
- Procedure/traveler changes. @Nina Menon 
- Ensure travelers inspect this dimension before potting - added to fuse power harness traveler 10/10.
- Approved workarounds. - both workarounds added to cables with round AS150: 107-102613, 107-102189-1, 96X-3-09-0011, 1803C03A, 114-106508
- Partially screwing in and potting if too long (Laszlo approved)
- tapping connector if too short (Matt approved)
- Document additional undocumented SLO processes in the procedure. Transfer to HSV. @Ben Norris can likely report most. See item 1. https://jenaero.atlassian.net/browse/VXEP-560 
- Install and pot with mated connector.
- Assign part number to jig and add to procedure. @Matt Weber
- Determine if implementing these reduces the difference between SLO and HSV parts.
- Matt to develop go/no go pin height gauge.
- Implement and document receiving inspection to verify. @Brad Crampton 
- Housing dimensions. Matt developed tools and shipped to HSV.@Matt Weber please link procedure and photos here.
- AS150 contacts. Need to make a specification. @Laszlo Juhasz  https://jenaero.atlassian.net/browse/VXEP-568
- Discuss with supplier why these are not being built to print and to ensure they are being built correctly. Wes reports inventory was sorted. @David Johantgen and Beth Barrett @Beth Barrett .  https://jenaero.atlassian.net/browse/VXEP-569 
- Evaluate updates of drawings and external parts. 
- See Ben’s recommendation in comments.
- Identify each assembly that uses these connectors. Round AS150’s: 107-102613, 107-102189-1, 96X-3-09-0011, 1803C03A, 114-106508 
- Create subtask to update drawings and inspections for each. @Nina Menon are you available to support this?
- See previous NCR conversations https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/NCR%20List/DispForm.aspx?ID=4072&e=iEKdjp

## Comments (15)

### Cameron Chapman, 2024-08-19

@Emalee Johnson are you able to collect feedback on why these connectors cannot be assembled to meet this spec when assembled correctly? It also seems like we could make some changes to inspect this dimension before potting.

### Emalee Johnson, 2024-08-19

@Cameron Chapman I provided significant details in this ticket in April: https://jenaero.atlassian.net/browse/VXEP-301 
It looked like you and Ben N. thought you came up with a workaround but we are still seeing NCRs despite the work around.

### Emalee Johnson, 2024-08-19

@Cameron Chapman I have shared the status of this with @Luca Lauritzen  and @Nina Menon , please direct any other support with them, they are the production engineers supporting electronics now.

### Cameron Chapman, 2024-08-19

Pasting NCR comments https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/NCR%20List/DispForm.aspx?ID=4072&commentId=10&e=lMeE__gYhUSPg8rFyZfw4A&at=15&xsdata=MDV8MDJ8Y2NoYXBtYW5AZWRnZWF1dG9ub215LmlvfDE4Mzg3MzMzY2Q4ZTRiZmI0Mjg5MDhkY2MwOTI3ODMxfDE4NzZmNjFhM2JkYjQ4NDNhZTcwNzVlZDBjY2I3NDA0fDB8MHw2Mzg1OTY5ODI1Mjk4NTAwMTZ8VW5rbm93bnxUV0ZwYkdac2IzZDhleUpXSWpvaU1DNHdMakF3TURBaUxDSlFJam9pVjJsdU16SWlMQ0pCVGlJNklrMWhhV3dpTENKWFZDSTZNbjA9fDB8fHw%3d&sdata=cEhtNGZVOFgveVVKYkFkLy9SRDl5K21WbU5TcmdDd0lLak5ML1JtT3F0Yz0%3d 
ou commented
@Nina Menon this is more of a mechanical task since they are CAD masters and control the design of the housing. Adding @Matt Weber. From the electrical perspective, we want to ensure the pins are fully inserted. Please follow up in the JIRA task, as they are generally much easier to track towards a document update.  
Just now
NM
Nina Menon commented
@Garrett O'Neill Yes, they were threaded all the way down. @Cameron Chapman Can your team look into adjusting the tolerance for the distance between the connector face and the top of the pin? It seems that the current process (threading the pins all the way down) is preventing us from hitting the current tolerance  
2h ago
GO
Garrett O'Neill commented
@Nina Menon @Luca Lauritzen Do you know if the AS150 contacts were installed properly? (threaded all the way down)
I don't think these are usable as-is.
2h ago
CC
You commented
@Emalee Johnson The most related JIRA issue is this subtask https://jenaero.atlassian.net/browse/VXEP-326.  These parts are OOS. They are not approved. We could use the JIRA issu...
4h ago
GF
Greg Fryer commented
@Cameron Chapman Need a EE to follow up on this. I'll come find you and help coordinate.
5h ago
GF
Greg Fryer commented
@Emalee Johnson I'll get someone on it, sorry I was OOO Friday afternoon.
5h ago
Last week
EJ
Emalee Johnson commented
@Ben Hansen FYI, this is a hot NCR, trying to get a dispo ASAP.
Fri at 4:08 PM
EJ
Emalee Johnson commented
@Greg Fryer We need a dispo on the -1 parts, hoping it can be UAI. The jira referenced shows the historical issue which we thought we resolved. This is preventing us from finishing Pre-MAGNSS fuselages.  
Fri at 4:05 PM
LJ
Luis Jacinto commented
@Emalee Johnson @Catherine Wagner @Garrett O'Neill @Brad Crampton
Fri at 2:27 PM
EJ
Emalee Johnson commented
@Garrett O'Neill These are hot if you can support that would be great. I think the potting issue we can dispo rework but the pin depth if that can be UAI. I thought we had resolved this with this ticket: https://jenaero.atlassian.net/browse/VXEP-301  but we are still seeing NCRs related to the pin depth.  
Fri at 2:27 PM

### Cameron Chapman, 2024-08-19

@Emalee Johnson it looks like that workaround was updated for the 96X-3-09-0011 inspection sheet, but it was not applied to other assemblies using this connector. @Nina Menon are you or another production engineer able to identify and update each of these applications? 

From https://jenaero.atlassian.net/browse/VXEP-301 
brad crampton
April 11, 2024 at 1:45 PM
@Cameron Chapman  @Ben Norris Attached is the proposed inspection sheet for 96X-3-09-0011. It shows the proposed pin depth requirements for the AS150 terminals. @Sam Omiotek The procedure and traveler will need to be modified and I have left some notes on your desk we may need to discuss. 
Cameron Chapman
April 11, 2024 at 10:19 AM
Edited
Thank you @Ben Norris great analysis. Are you or production engineering able to mark up a drawing with the recommended changes? That would expedite our availability to review and update the drawings. 
Edit
Delete
Ben Norris
April 10, 2024 at 4:41 PM
From looking into this I think I have found a workaround until proper Design Engineering Drawings can be drafted up. It seems like the two critical dimensions for placement inside the housing are the closest distance from the face of the connector housing and the face of the pins (because if the pins are too close or even worse proud to the connector face then they could potentially short to the female terminals in the wrong orientation.) The second measurement being the difference between the faces of the two pins (because if the negative pin is lower than .1in from the top of the positive pin then the antispark feature will be negated.) So we just need to add to the procedure and inspection sheets for all GCS assemblies with this housing, a callout for more than 0.085 in gap from the face of the housing and no more than .100 in difference in height between the pins. And we can leave the 0.115 in measurement in as reference if desired. This would be implemented by production engineering and quality with approval from design engineering until design engineering has sufficient bandwidth to draft proper drawings which can apply this deviation from the callout for the Fuse Power Harness which has different power requirements compared to the adapters included in the GCS into the GCS adapters. @Emalee Johnson @Cameron Chapman @Catherine Wagner @Matthew Philley @brad crampton

### Nina Menon, 2024-08-19

@Cameron Chapman it looks like the procedures for the applicable PNs listed on https://jenaero.atlassian.net/browse/VXEP-301 were all updated. I can update the traveler/procedure to have the workaround for 107-102189, and @Brad Crampton can update the inspection sheet. Just to confirm, is there an impact from an electrical standpoint if the pins sit lower? 
From a mechanical perspective for @Matt Weber 's reference: I measured 20 pins in inventory and they all measure between .892” and .895” in length, with 12 of them at .893”. The longest the hole could be is 1.025” (.755+ .27). With the pins coming in at .893”, we are seeing the dimension between the face of the connector and the tip of the pin (fully screwed in) at about .132, which is outside the current tolerance of .100 +/- .015. 
[embedded: image-20240409-163447.png]
[embedded: image-20240409-164138.png]

### Cameron Chapman, 2024-08-19

@Nina Menonthe pins are designed to fully mate to the sockets. There is an electrical impact if they do not fully mate. A small deviation is likely ok for any connector other than the HLB one. @Laszlo Juhasz did you ever do any testing for pin insertion vs current capacity? Can you please link it if so? 
[embedded: image-20240819-230729.png]

### Matt Weber, 2024-08-22

The pin in the male connector bottoms out on a step and is a repeatable operation.  The pins in the female connector, however, rely solely on the cut depth of the thread and is a less reliable feature.  We have seen connector housings in which the thread depth varies more than the +/- 0.015” that the assembly drawing calls out.  
@Laszlo Juhasz , the pins that we see have a minimum insert of .53” if you want to include that in your power testing.

Why don’t we use off the shelf AS150 waterproof connectors?  Potentially avoid these fitment issues and 1/3 the price of our custom Ultem parts.

[embedded: image-20240822-163603.png]

### Cameron Chapman, 2024-08-22

@Matt Weber I do not think those existed when the Ultem connectors were designed, but I agree, they look like they may have been a better part. For the next connector, AS150 contacts have many issues, so we will be using a different contact entirely. See linked task.

### Cameron Chapman, 2024-08-22

Thanks Matt. @Nina Menon and @Luca Lauritzen are you available to coordinate implementing this tool into the traveler or a receiving inspection to cut down on the frequency of this issue? That plus measuring before potting should reduce it a lot. 
Laszlo should be dispositioning the NCR soon. You are welcome to check with him in person if you would like to expedite.  
Thank you,
Cameron Chapman
 
From: Matt Weber <mweber@edgeautonomy.io>
Sent: Thursday, August 22, 2024 11:47 AM
To: Desiray Johnston <djohnston@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>; Laszlo Juhasz <ljuhasz@edgeautonomy.io>; Luca Lauritzen <llauritzen@edgeautonomy.io>; Nina Menon <nmenon@edgeautonomy.io>
Cc: Kelly Furlong <kfurlong@edgeautonomy.io>; Spenser Bracken <sbracken@edgeautonomy.io>
Subject: RE: Fuselage Power Harness Issue
 
I’ve looked at the drawing for these parts.  The issue isn’t tolerance stack-up, it’s that the connectors I’ve seen are out of spec.  The thread depth seems to be a difficult feature to machine consistently and hard to inspect, so a lot of non-compliant housings end up in production.  I just made a tool, PN 2118888, to validate that the connector housings have adequate thread depth, but we would probably need to redesign the part (or buy off the shelf components) if we wanted this issue to go away completely.
 
Thank you,
 
-Matt

### Cameron Chapman, 2024-10-08

@Matt Weber Moving this out of done. All items in the plan are not done. Reassgning to @Nina Menon. FY @Sloan Payne

### Nina Menon, 2024-10-10

@Cameron Chapman workarounds added to procedures and pin depth verification added to travelers (107-102613, 107-102189-1, 96X-3-09-0011, 1803C03A, 114-106508, 114-106509). We cannot update the Dual Current Sense (107-102264) docs until the pin depth/tolerance in this ticket is approved: https://jenaero.atlassian.net/browse/ECM-266 
I created a ticket to update all AS150 drawings (ENG-2734) but i wasn't able to add this one as a parent. Not sure if that’s because of the issue type or if I don’t have access to create a sub-task.
The inspection sheets for the parts listed above have a check for the pin depth, is there something else Brad should add?

### Christa Meck, 2025-12-31

@Nina Menon and/or @Cameron Chapman This has been in progress for over a year now.  We done yet?

### Cameron Chapman, 2025-12-31

no

### Cameron Chapman, 2025-12-31

@Christa Meck no

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240409-163447.png | image | 52 | 2024-08-19 | listed only |
| image-20240409-164138.png | image | 22 | 2024-08-19 | listed only |
| image-20240819-230729.png | image | 167 | 2024-08-19 | listed only |
| image-20240822-163603.png | image | 2156 | 2024-08-22 | listed only |
