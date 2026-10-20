# VA-95: 8D #24 Update HLB Lift Connector to include some physical indication connection is fully seated. Evaluate adding to similar power connectors

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-08-21
- **Updated:** 2023-11-09
- **Resolved:** 2023-09-14
- **Reporter:** Cameron Chapman
- **Assignee:** Hans Hershberger
- **Creator:** Cameron Chapman
- **Labels:** 8-28-Sprint
- **Links:** relates to VXEP-481 (8D #24 – CW to HLB AS150 Connection Issues​ Corrective Actions); relates to ENG-2181 (EA Internal: VXE511 Aborted Launch at 2ft, VTOL ESCs stuck in initialization loop); relates to VA-456 (HLB Connector Mate Indicator); relates to SMUP-77 (CW to HLB AS150 Connection Issues-airworthiness directive (AD)); relates to VA-469 (TPTR-87 VXE 511 VTOL Connector Issues-Create, procure, and document kit for SB/AD application. ); blocks VXEP-12 (TPTR-87 VXE 511 VTOL Connector Issues 516 CW. Contains Main connector/contact C/CAs)
- **Sprint:** VXE-1 EE Team Sprint 8/28-9/17
- **Production Stakeholder:** Ryan Ferguson
- **Supply Chain Stakeholder:** Victor Vandor
- **Other Stakeholder (as required):** Matt Philley

## Description

Need an immediate service bulletin option, and a long term solution. 
Immediate ideas:
- Qualify tape Matt selected or similar. Ensure it will stay adhered in all all environmental conditions (by rating and/or test). 
- Link to Tape Used for testing: https://www.mcmaster.com/7779A22/ (3M 471)

Long term ideas:
- Paint connectors.

## Comments (32)

### Cameron Chapman, 2023-08-21

Please report estimated completion date for service bulletin technique.

### Cameron Chapman, 2023-08-21

Attaching email chain with Maglio for long term improvement. 
Hi Ted,
 
We are trying to visibly mark when the connector is fully mated or not. The red should not be blocked by the battery and not visible when mated. A high visibility color was selected to help make it obvious in a hard to see, access, dim area.
What do you recommend for this goal?
 
Thank you,
|  | Cameron Chapman Electrical Engineering Supervisor Edge Autonomy – SLO (formerly Jennings Aeronautics) Email: cchapman@edgeautonomy.io Phone: (970)389-5904 |

 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Ted Thayer <tthayer@maglio-inc.com> 
Sent: Friday, August 18, 2023 2:06 PM
To: Hans Hershberger <hhershberger@edgeautonomy.io>
Cc: Cameron Chapman <cchapman@edgeautonomy.io>
Subject: RE: Connector Question
 
Howdy Hans,
 
Anything is doable over here, my concern would be applying paint to the part would be too time consuming & costly for EA.
 
I assume you’ve evaluated light etching/engraving (if thickness allows) which we could add as a milling op, but I’m not sure if that would solve your issue?
 
Feel free to elaborate on what you’re needing to accomplish & I’ll run this by folks here for other ideas.
 
Regards,
 
Ted Thayer
 
President
MAGLIO INC.
141 Suburban Road, B1
San Luis Obispo, CA 93401
 
tel: 805.788.0820 x111
cel: 805.878.9199
fax: 805.788.0825
 
tthayer@maglio-inc.com
www.maglio-inc.com
 
PRIVILEGED AND CONFIDENTIAL
This electronic transmission, and any documents attached hereto, may contain confidential and/or legally privileged information.  The information is intended only for use by the recipient named above. If you have received this electronic message in error, please notify the sender and delete the electronic message. Any disclosure, copying, distribution, or use of the contents of information received in error is strictly prohibited.
 
From: Hans Hershberger [mailto:hhershberger@edgeautonomy.io] 
Sent: Friday, August 18, 2023 12:14 PM
To: Ted Thayer
Cc: Cameron Chapman
Subject: Connector Question
 
Hey Ted!
 
There has been an internal request here to add a visual mating indication to 100-102570 (VC0123).  I was wondering how doable it might be to add a line of red paint at the tip of the connector as mocked up by one of our personnel.  We are also totally open to alternative ideas.
 
See photos below for more details and dimensions.  
 
Thank you!
 

 
|  | Hans Hershberger Mechanical Engineer Edge Autonomy Mobile: +1 805-592-1179 Email: hhershberger@edgeautonomy.io |

 
 
** WARNING: This email originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe. **

### Hans Hershberger, 2023-08-21

My concern with the tape is not so much with how it is affected by higher temperatures (though that is important) but how quickly tape warps and degrades with minimal use.  I am considering for the short term solution making a jig stencil and using a paint pen to make the red line on the connector.

### Cameron Chapman, 2023-08-21

Paint+jig sounds much better. Are you able to estimate time to develop and approve that? Ryan is asking.

### Hans Hershberger, 2023-08-21

I have a first pass at a prototype jig that I am testing right now and have placed a purchase request for a paint pen that hopefully will be get ordered within the next few days.  Until that paint pen comes, I can’t move forward.  So probably around a week.  Assuming the paint pen method works as assumed

### Cameron Chapman, 2023-08-21

Thanks Hans. For urgent orders like this, you can contact purchasing directly to expedite the purchase.

### Hans Hershberger, 2023-08-22

Paint pens have been ordered.  Working on improvements to jig.

### Hans Hershberger, 2023-08-22

@Jeremy Roberson here is the associated HLB connector fix ticket

### Cameron Chapman, 2023-08-24

Linking subtasks to parent

### Matt Philley, 2023-08-24

@Hans Hershberger fyi we have “waxy” paint pens in the electronics vending machines and we have actual paint touch-up pens we use in Final Assy if you wanna try those for a proof of concept.

### Hans Hershberger, 2023-08-24

Tested with paint pens and there was capillary that pulled the paint into the space between the connector and the jig.  Jig redesign needed to remediate this issue.

### Hans Hershberger, 2023-08-24

Long term solution has not been determined yet but likely paint in booth

### Hans Hershberger, 2023-08-25

New painting jig has been designed and is being printed.  A wider paint pen has also been ordered.

### Hans Hershberger, 2023-08-28

New painting jig works but there are some concerns over durability of paint to rubbing off with time.  Pursuing a sticker/label option.  Creating a sticker option similar to that used on our x-box controllers.  Will hand over to @Gerrit Sperling for his expertise when the sticker is sized/profiled.

### Hans Hershberger, 2023-08-28

A sticker/label file has been created.  It needs some data filled out in its data card, but the number is 107-114271.

### Gerrit Sperling, 2023-08-28

A PDF of the 107-114271 has been posted to the vault as an output file for getting stickers made. Need to test cut on the Avery and then order these from the same vendor as the XBOX controller stickers (Vendor: Coastal Reprographic Services, MATERIAL: 3.5 MIL DPM ADHESIVE FLEXCON VINYL WITH 3 MIL PS UV VINYL LAMINATE) .

### Matt Philley, 2023-08-28

@Gerrit Sperling @Hans Hershberger have yall tested to see if that material sticks to the connectors? Do we need to look at using an adhesion promoter?
Also… those stickers look like they will have extremely specific indexing. Is there any mark on them to assist with that? I really recommend yall do some testing with one of the Production Engineers.
There was also a request that a sticker like this covers the entire bottom portion of the connector and not be just the stripe. Was that discussed or considered?

### Hans Hershberger, 2023-08-28

A sticker has been made that covers the entirety of the bottom of the connector.  Indexing is not difficult and has been done many times by my hand in the process of iterating this design.  There will have to be some instruction in the FSB and in house production documents, but I would say it is totally doable.  We chose the indexing of the sticker based off of where it will be out of sight of most operation but in the middle of a flat plane.  It is hard to say on adhesion without experience.  I think we could do a test run from the vendor and see how that goes.   The Avery waterproof labels stuck very well interestingly.  I don’t have much more time to spend on these labels in this new sprint system engineering finds ourselves in so this is about the best I can do with the time I have been given.

### Gerrit Sperling, 2023-08-29

PO placed for first articles from Coastal Reprographic Services.

### Hans Hershberger, 2023-09-05

we got in some labels today.  I believe they are goon enough and we are ready to roll these out to FSB and into our manufacturing process.  Creating a drawing for the labels.  Will have to add to an assembly level as well.

### Matt Philley, 2023-09-05

@Hans Hershberger I would recommend a review with @Greg Fryer and probably @Sam Miller and maybe PM @Former user…? This should be transitioned over to an Engineering Change Jira so it goes through CCB for those types of discussions before moving further with the change implementation. 
Since this is related to a big customer complaint we need our Customer facing friends on board for the solution and I think there were prior concerns about the use of tape and/or a label that we need to address.

### Hans Hershberger, 2023-09-06

drawing made for label 107-114271-01 HLB Mate Indicator Label.
https://jenaero.atlassian.net/browse/VA-456 created for engineering change

### Hans Hershberger, 2023-09-06

Should the label (if that is what we decide to go with) be added at the assembly level of 107-102264 or should we make a separate subassembly of the connector housing 100-102570 with the label put on it that would then go into the higher level assembly aforementioned?  I think I would vote for the former, but just thought I would ask.

### Hans Hershberger, 2023-09-06

working on making a drawing for 107-102264 because we don’t have a mechanical drawing of it and if we are going to include the label it will be useful

### Hans Hershberger, 2023-09-07

Creating test plan for labels

### Hans Hershberger, 2023-09-08

Put in the freezer for several hours.  The result was that the label seemed to have even better adhesion and the label would chip off before peeling if an attempt was made at removal.
Hit it with a heat gun for several minutes until hot to the touch.  Managed to peel off the gloss laminate from the label without much difficulty.  Peeled off the colored label with a bit more effort leaving behind a bit of adhesive residue.
From the hot test, I was curious if it was possible to remove the laminate from the label at normal temperatures.  It is possible, but not something one is likely do to without trying to.  And if it happens, the colored label below appears to be plenty sturdy enough to still be useful for operation.

### Dana Holley, 2023-09-08

@Hans Hershberger Need to clarify short term procedural guidance for fully seated connection for AD scheduled release for 9/15/23. Are we still planning on using 0.5” painters tape around the collar of the connector for interim guidance?

### Hans Hershberger, 2023-09-13

dirty water soak is no match for the connector mate label patch

### Greg Fryer, 2023-09-14

@Hans Hershberger Great update, seems like this task is complete. Please clsoe and focus on the release. (Which I’m going to go look at now because I think it’s done.)

### Hans Hershberger, 2023-09-14

I’m having @Gerrit Sperling recess the red area by 10 thou to better match what the performance of the Avery label prototype.  I’m confident that it is a good change.  If it is decided in release not to be so, we will revert it back to version 7 on the vault.  I have spoken.  Closing this ticket.

### Greg Fryer, 2023-09-14

@Hans Hershberger Boom. I am also trying to clean up all the extra tickets and such. Is there one already extant to create a BOM for the “Service Kit” that has the pick and labels in it?

### Hans Hershberger, 2023-09-14

There is https://jenaero.atlassian.net/browse/VA-469 which I think is close to what you are describing.  I will link it above

## Attachments (15)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20230826-033414.png | image | 3 | 2023-08-25 | listed only |
| processed-2F107E9A-8821-4FFF-A71C-8CA2B2343FB8-E75568C7-1A87-4D66-98BD-E8914B269356.jpeg | image | 2945 | 2023-08-28 | listed only |
| processed-489FC5C8-3D6C-4B36-9019-0808BCD1EEFB-D52BE0B1-732E-4E3A-BD6D-E5F805AEE416.jpeg | image | 2538 | 2023-08-28 | listed only |
| processed-4FD30744-E18E-4526-BD90-71EE6A4DB091-7C4B092D-9F86-4C3D-83C4-4647FB1FC01D.jpeg | image | 2945 | 2023-08-28 | listed only |
| processed-BF2E5908-6E51-48C8-86C0-7C0B9CF3C6BC-046C4C2E-47B5-440B-BBD9-C36A49DEE55C.jpeg | image | 2944 | 2023-08-28 | listed only |
| processed-C644A63C-7BCF-4D31-A43A-783118965A4F-635A812C-52E7-4519-8285-0B5EC08D8C64.jpeg | image | 3058 | 2023-08-28 | listed only |
| processed-F553B0C5-CCC9-4D1C-8B94-79E5E2184741-CED4B2DB-9AFB-4701-A270-69A8B88D90D4.jpeg | image | 582 | 2023-08-28 | listed only |
| IMG_3477.JPG | image | 2940 | 2023-09-05 | listed only |
| IMG_3478.JPG | image | 2302 | 2023-09-08 | listed only |
| IMG_3479.JPG | image | 3480 | 2023-09-08 | listed only |
| IMG_3480.JPG | image | 2493 | 2023-09-08 | listed only |
| IMG_3481.JPG | image | 3026 | 2023-09-08 | listed only |
| IMG_3483.JPG | image | 2993 | 2023-09-13 | listed only |
| IMG_3484.JPG | image | 3161 | 2023-09-13 | listed only |
| IMG_3485.JPG | image | 3158 | 2023-09-13 | listed only |
