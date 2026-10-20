# VXEP-55: Alternate (or replacement) long range SGCS-3 dish vendor (MicroAnt)

- **Issue type:** Major Project
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2022-11-01
- **Updated:** 2025-03-11
- **Resolved:** 2025-02-04
- **Due:** 2023-10-31
- **Reporter:** Greg Fryer
- **Assignee:** Cameron Chapman
- **Creator:** Greg Fryer
- **Parent:** VXEP-667 Sustainment: Ground Hardware
- **Links:** duplicates ENG-3142 (Alternate Long Range Antenna Vendor); relates to VA-109 (Microant conduct development design review (and kick off prototype fabrication)); relates to VA-108 ((Microant conduct electrical design review); is blocked by VA-107 ((Micro Ant) Determine Drop Dead Date for Cut-in - Nov 2023); is blocked by VA-617 (Complete new vendor of antenna feeds); is blocked by VA-809 (Characterize and Validate SGCS3 Antenna Performance in Anechoic Chamber)
- **Sprint:** VXE-2 ME Sprint Team 8-28
- **Production Stakeholder:** Desiray Johnston
- **Supply Chain Stakeholder:** Victor Vandor
- **Other Stakeholder (as required):** Matt Philley
- **Product/Tech Owner:** Greg Fryer
- **Program (Marquee):** Ground Hardware Sustainment
- **Job Number:** J100082 - Sustainment: Ground Hardware

## Description

Existing vendor Epsilon is unreliable. New vendor Microant.
Delivery is first article, which sets due date.
Current Plan 8/2: We have (13) SGCS 3 due by end of 2023 and an additional (9) due in 2024. To support these, we would need QTY 44. Drop dead date to be safe should be November 2023 to give time for cut in. Please let me know if there is more information needed from production in order to close this action.
Lead time for next order: “8 weeks works for us for QTY 3 systems = 6 feeds and 6 aluminum reflectors. Please send us a PO as that will kick the fabrication process internally.” -Ashram at Microant. Need to quote (13) SGCS 3 due by end of 2023 and an additional (9) due in 2024. 8 weeks from 8/2 is 9/27
Next steps:
- Contact micro-ant for their latest models, drawings, etc.
- Verify that they have made all of the improvements listed above.
- Check with @Matt Philley and production if they agree or recommend any more.
- Tag up with Victor, and ask him to approve them shipping the remaining 2 we ordered with these changes.
- If schedule allows, receive and inspect these 2 units, if not skip to next step.
- Complete approval, document changes, CCB, etc. and approve for production orders.


Complete these improvements before next orders if possible. All changes should be reviewed with all stakeholders (quality and production as well) released and CCBd before approving for customer orders. 
Notes for mechanical improvements:
- aluminum dish not carbon
- paint dish same color as feeds
- 4 mounting holes not 8 on dish
- better marking of up on feed, not scratched off paint and laser etched
- anodizing of parts that contact between spring mount, dish and feed to prevent paint from peeling

- keep sma connectors on feed from spinning when torqued
- verify stainless steel sma connectors on feed, brass have lower torque spec (need to ensure mating connectors are steel as well, or check compatibility and torque spec of steel to brass. Koaxis cables will be steel.) Verify kit has the correct torque wrench. 
- Cables on current NHA are brass, replacement Koaxis cables will be stainless steel. Microant claims they cannot source stainless steel connectors for their feeds.

## Comments (56)

### Cameron Chapman, 2022-11-01

Attached email chains I received

### Kurt Burian, 2022-11-14

PO kicked off. Vendor had few mechanical questions I relayed to @Former user . Pasted below from email 11/11:
Couple requests from the dish people:
On drawing 105-107149, the diameter of the circle the 8x32 Helicoils lie on isn’t defined.
Can you verify the 4 outer holes on the dish are not used. I’m 99% sure we decided they are not and just running in past you incase my memory is faulty.
FYI, they promised a solidworks model in December.
 
-Kurt

### Former user, 2022-11-14

Replying here so others can track:
On drawing 105-107149, the diameter of the circle the 8x32 Helicoils lie on isn’t defined.
That is an important one… Added to drawing and submitted for approval.
Can you verify the 4 outer holes on the dish are not used. I’m 99% sure we decided they are not and just running in past you incase my memory is faulty.
Confirmed

### Cameron Chapman, 2023-03-08

From @Victor Vandor email
We need this one elevated since the vendor is in the middle of making the part….
 
Victor Vandor
Supply Chain Manager
Edge Autonomy
Previously Jennings Aeronautics
P: +1-805-544-0932
Email: vvandor@edgeautonomy.io

### Cameron Chapman, 2023-03-08

Another email.
Kurt – Is this https://jenaero.atlassian.net/browse/ENGPRJ-37 ?
 
Given the tight timeline, let’s see if we can get Enoch and Will or Gerrit into a room to itemize the changes out. I can see in Jira the discussion, but I’m getting stuck trying to determine which actual drawings have the issue. E.g. the mount drawing, the new dish drawing, the old dish drawing, or “all”.
 
~Greg
 
From: Kurt Burian <kburian@edgeautonomy.io> 
Sent: Tuesday, March 7, 2023 2:20 PM
To: Cameron Chapman <cchapman@edgeautonomy.io>; Greg Fryer <gfryer@edgeautonomy.io>
Cc: Victor Vandor <vvandor@edgeautonomy.io>; Enoch Nicholson <enicholson@edgeautonomy.io>
Subject: Fwd: JEN-003 New dish
 
Hey,
We need to follow up with removing the extra holes from the dish as well as addressing these questions. AP has me swamped. Is anyone available to help since Enoch is leaving? Prototype shows up end of month.
 
Thanks,
Kurt
 
From: Ashram <ashram@micro-ant.com>
Sent: Tuesday, March 7, 2023, 2:07 PM
To: Victor Vandor <vvandor@edgeautonomy.io>; Kurt Burian <kburian@edgeautonomy.io>
Subject: JEN-003
 
Hi Victor and Kurt,
 
Hope you are doing well. Our team had a couple of questions which I need your input in:
 
- Does the hub have any specific orientation?

- Are the polarization band Decals acceptable?

 
Thanks

### Kurt Burian, 2023-03-08

The subtask about the holes, 370, and addressing the questions about part orientations and stickers copied below. 
Hi Victor and Kurt,
 
Hope you are doing well. Our team had a couple of questions which I need your input in:
 
- Does the hub have any specific orientation?

- Are the polarization band Decals acceptable?

 
Thanks

### Greg Fryer, 2023-03-20

@Kurt Burian @John Clark I know you have been swamped, but we do need to meet on this and get actions assigned out. (and maybe status the things that are already listed as subtasks). Please schedule something, including Will or one of his folks.
- Our discussion about the need for both the feed and the mount of the feed: Is this coming as a set from Microant for this, or are we making a new part somehow? (Probably a call to them, maybe a design review if the one in plan hasn’t already happened).
- Also, see NCR 776 SGCS3 Spring Ring Not Plated - Since this is a COTS part we may not know what spring material should be used (or we are not controlling it). Need to figure out how to resolve when we get the new part.

@Former user @Gerrit Sperling I think we need some mechanical help here, maybe @Nadia Brown could help too. This jumps ahead of the regular BOM queue as well. Open to thoughts.
~Greg

### Kurt Burian, 2023-03-20

If I remember correctly, they are making the quick release mount per the phone call. Will or Gerrit should be able to verify Im not crazy. I think they needed a drawing with modified holes. @Former user Do you need me to dig into this or are you guys squared away?

### Former user, 2023-03-20

@Kurt Burian is correct. We had a call and they are designing and supplying the coupler. We will need to update the arm to omit the unused holes. The vendor is going to include some part marking to help with assembly orientation. Stickers with arrows or something similar. FYI @Gerrit Sperling @Victor Vandor @Greg Fryer

### Greg Fryer, 2023-03-20

@Former user @Kurt Burian @Victor Vandor @Kurt Burian Don’t forget how lousy those stickers were on the paint used. Might already be solved, but a template/paint would be WAY better. I’m open to other options too.

### Cameron Chapman, 2023-03-31

Here are the meeting notes from a 3/31 call with MicroAnt. I am not very familiar with this project, so please feel free to add or change any details.
 
Actions for MicroAnt
Ship 1st article 3rd week of April.
1 reflectors in hand need to confirm 2nd. 1 feed each.
- Shipping composite reflectors. Production units will be Aluminum due to cost.
- No difference in RF performance vs Aluminum. Lighter, more rugged, more expensive.

Want to have data review of chamber measurements. Hoping to meet early next week. Will send data in advance.
Prototype ones will have 8 holes. Will change hole pattern to 4 for following ones. Will to send CAD.
Anodize base parts. Want as close to production as possible.
Will get reflectors painted. Paint specified. Desert Tan.
Sending update model. Rerouting cables. Will be on prototypes.
Change all labels to etched.
 
Actions for EA
- Send updated CAD.
- MicroAnt wants to join for testing. EA to coordinate.

FYI @Maxime Jeanneau @Sam Miller

### Cameron Chapman, 2023-04-21

@Kurt Burian , I know you are slammed with AP work. Could you let us know a good time to meet with me, @Maxime Jeanneau, and @Former user for a handoff of this project? We can then complete remaining actions, documents, CCB, etc.  
Did Micro-Ant complete any of these actions from what you know, or should we ask them to complete?
[embedded: image-20230421-215510.png]
FYI @Matt Philley @Greg Fryer @Victor Vandor

### Kurt Burian, 2023-04-24

@Cameron Chapman I already met with @Former user and @Gerrit Sperling a few weeks back prior to the last call to unload the project. The actions for you guys are to test the dishes and make sure they work just as well as the last ones and make sure the assembly is clear mechanically so things line up. I provided a test procedure. Who will be executing it? I have provided the vendor with requirements, they should be associated with this project for you to reference. Which part is hanging you up? Im happy to answer questions, just tell me what they are.

### Maxime Jeanneau, 2023-04-25

@Kurt Burian happy to take on this task from here. As far as I understand it the remaining task is to test the new antenna.

Can you, or someone else please point me to the: 
- Previous dishes that we are replacing
- Vendor requirements
- Test procedure (Found in email chain)

### Matt Philley, 2023-04-25

FYI I added a new child issue (subtask) for Production and Supply Chain to align on a clear need date
https://jenaero.atlassian.net/browse/ENGPRJ-405

### Cameron Chapman, 2023-04-25

@Maxime Jeanneau see the following. 
SGCS3 Dish Antenna, Product Requirements.docx
96X-3-14-5430 Silvus Long Range Extension Kit (SGCS-3), Case 3, BOM.xlsx. We will need to update this BOM and the item below. 
105-108632 DISH, 24IN, DESERT TAN, BOM.xlsx

### Kurt Burian, 2023-04-25

@Maxime Jeanneau https://jenaero.atlassian.net/browse/VIT2-41 Attached the requirements there. Should also have the latest on the Vault, Enoch was handing and the mechanical and foam stuff, but should be a drop in replacement to the existing case. They were going to provide solidworks exports to check, but we can just drop it in the foam if that didnt happen and see if it fits. The requirement is that it works the same as before with dual band on a single feed. I wrote up a gain spec, but we arent going to measure it. We are going to do a qualitative side by side comparison. If video/bandwidth is as good or better, its a win. Part number should be on the drawings.

### Maxime Jeanneau, 2023-04-26

Dishes and feeds are in the QA area getting processed as first articles, will run a spectrum analyzer sweep once released, and coordinate with the @Former user to check the mechanical design items.

### Maxime Jeanneau, 2023-04-27

Photos of mechanical check with first article:
[embedded: IMG_5680.jpg]
[embedded: IMG_5681.jpg]
[embedded: IMG_5682.jpg]

### Jack Waeschle, 2023-04-27

@Former user @Gerrit Sperling @Maxime Jeanneau and I, along with the help of @Carson Buckley assembled the first articles from Microant. The quick attach clamps contained both a 25 lb and 50 lb wave spring. The 50 lb wave spring proved far more secure, although required a firm hand when installing and removing feeds.
The feeds appear to be well made and do not feature excessive chips in the paint or other build quality issues that we commonly found with our previous vendor. The arrows at the bottom that indicate installation orientation could be both brighter (white or black paint instead of an etching in silver paint), and feature lines or other markings that extend beyond the base and up the sides of the shaft of the feeds. This would make them far more noticeable. Additionally, the quick attach clamps could use white paint marking the orientation arrows, instead of dark red, once again to make the markings more obvious/provide users with more signifiers for correct installation. Lastly, the feeds fit in the existing foam well, meaning cases/foam will require no modification.
The dishes are unpainted carbon fiber. In production they will have to be painted. They are slightly smaller than the old dishes, so they easily fit in the same foam in the case. As mentioned in the subtasks of this ticket, they feature 8 holes while only 4 are required for installation.
See Maxime’s photos below.

### Matt Philley, 2023-04-27

@Jack Waeschle is it any concern if the dish is too lose and could move around too much in the case? It seems like most things were design to be pretty snug. If the lid is closed is that “compartment” is not fully closed is there any risk of the dish moving around inside the case and coming out of its pocket?

### Former user, 2023-04-27

@Matt Philley I am not concerned about the fit check that we performed today.

### Matt Philley, 2023-04-27

@Former user dig it. thanks!

### Maxime Jeanneau, 2023-04-28

As we move into testing: 
- Carbon dishes are not painted, we’re planning on having the production units painted, is it worth testing without paint given it’s not fully representative?
- We’re planning on using aluminum as the production units to reduce cost. Is it worth testing the carbon dishes given the production units will be different? Maybe we’re considering carbon dishes for production?

### Cameron Chapman, 2023-04-28

@Maxime Jeanneau according to Ant-com, the aluminum painted units should be equivalent performance to the carbon ones. I think we can do detailed tests for the carbon ones, then less complex tests of the aluminum ones to confirm equivalence. We can also review Ant-com data for both versions when available. We may not have time to wait for the aluminum units.

### Maxime Jeanneau, 2023-04-28

Ran spectrum analyzer sweep test following 110-109257 results passed on both feeds, photo captures of the results posted below: 
Feed 23160001 SBand: 

[embedded: IMG_5693.HEIC][embedded: IMG_5694.HEIC]
Feed 23160001 CBand: 
[embedded: IMG_5692.HEIC][embedded: IMG_5691.HEIC]
Feed 23160002 SBand: 
[embedded: IMG_5689.HEIC][embedded: IMG_5686.HEIC]
Feed 23160002 CBand: 
[embedded: IMG_5689 (d900b9a4-a2c0-4fa0-9d2a-3c4584b82007).HEIC][embedded: IMG_5688.HEIC]

### Artis Bertulis, 2023-05-09

@Maxime Jeanneau 
We performed a comms check with an actual aircraft and Carson said that he sees the same performance as he usually does during the other SGCS3 checkouts, so they seem to be good to go. 
To be specific, when the antenna is close to the aircraft and pointing the it at the aircraft he’s used to seeing Received signal power in between -5 to -15 dbm
[embedded: image-20230509-221208.png]
When pointing it away from the aircraft in between -20 to -30
[embedded: image-20230509-221351.png]

### Artis Bertulis, 2023-05-09

@Maxime Jeanneau While performing the test few observations were made:
- 50lb spring works the best for the antenna base (see below), one of them had what I assume was a ~10lb spring, and we also tried the 25lb spring, but it seems like the 50lb one works the best (both antenna bases now has 50lbs one) so order that for the future.

[embedded: image-20230509-221658.png]
- The SMA connector at the bottom of the antenna was loose - when we connected the cable and tried to tighten it using a torque wrench we noticed that the SMA connector started spinning. That’s very bad, if it spins too much it might damage the cable inside the antenna and the user would never know that there’s damage, but the signal quality will be significantly reduced.
It seems that the problem is the star washer under the connector locking nut, it’s very soft, so even though it was tightened by the manufacturer, because the washer is soft it could bend its teeth and start spinning. We had to tighten the nut until the point where the washer is flattened and oval (see below), and only then the connector wasn’t moving when torquing the cable.

[embedded: image-20230509-222217.png]
 
[embedded: image-20230509-222411.png]
- The arrow indications need to be marked more clearly, for first-time users it’s hard to locate the correct orientation of the parts, they would need to be bright white, or highlighted some other way. Currently, their color is not different enough from the part, they don’t stand out, and the arrow location is not intuitive, you can’t see them by quickly looking at the antenna.
The same applies for the C-band and S-band markings on the bottom of the antenna, just scraped-off color is not enough, and does not look professional.

[embedded: image-20230509-222854.png]
[embedded: image-20230509-223258.png]
- As far as I know, these parts have been assembled only 2 times, but there is an awful lot of small color damage on the parts. Firstly, if the color chips that easily, we might not be able to ship “fresh” parts to the customer, and secondly, even if we do, the regular use of the product will make it look bad real quick. Damages are visible in all the pictures in this comment.

[embedded: image-20230509-223122.png]

### Former user, 2023-05-18

@Artis Bertulis MicroAnt is asking for feedback on the first articles. I will forward them the comments you had for mechanical.

### Former user, 2023-05-18

Sent mechanical feedback to Micro-Ant.

### Former user, 2023-05-18

Below are some notes from Micro-Ant about the feedback, and what they plan to do about it moving forward:
Will,
 
Connectors rotating
                The connectors in the future will have a D Hole that prevents them from rotating. The D hole on these units had to be drilled out because I was having assembly issues. Our new design accounts for this assembly issue.
 
Labeling/Markings
                The laser etching arrows and the S/V labels on the feed were supposed to be milled pockets like the hub. This will be a pocket filled with colored epoxy as well. We can make the epoxy white or use more red pigment to make the color more prominent on the next feeds.
 
Springs
                I liked the 50 lb spring as well. I just sent the 25lb springs for your evaluation.
 
Paint chipping/Anodizing
                Due to Timing the unit was not anodized, and the paint was applied in house with sub par equipment. The Hub pieces will have hard black anodizing.  Where the feed is inserted into the hub will always have metal to metal interaction that will chip even the best applied paint.  I think we should anodize the base of the feed black as well, to keep the finish fresh.
 
With the In house painting there was a lot of texture as well. The texture will be very light on future feeds.
 
 
Josh

### Maxime Jeanneau, 2023-06-22

Functional test in Bend has been conducted. See results attached. Based off of the results are satisfied to approve purchases of Micro Ant antennas. Arranging meeting with vendor to discuss changes we’d like to see and eventually procure. 
[embedded: May2023BendLongRangeTestingAntennaReport.docx]

### Maxime Jeanneau, 2023-06-26

Discussed results with Micro-Ant over google meets 6/26, have decided to move forward with procuring the next round of antennas: 
We discussed: 
- Moving forward with painted Aluminum dishes
- Mechanical improvements as outlined below by Will


Leaving ticket open until we receive the next batch. We should hear back about the mechanical improvements soon.

### Matt Philley, 2023-06-27

@Maxime Jeanneau is there a reason for choosing paint instead of anodize? If a production batch of parts came in the way the samples did they would be rejected and sent back to the supplier…
Is the next batch intended to be representative of the Production product?

### Maxime Jeanneau, 2023-06-27

Did not consider moving to anodized for the entire dish/feed. Anodized seems off to me due to the shininess. It seems silly painting it camo but also having it be reflective. 
The manufacturer did respond to Will on the subject with: 
“Paint chipping/Anodizing
                Due to Timing the unit was not anodized, and the paint was applied in house with sub par equipment. The Hub pieces will have hard black anodizing.  Where the feed is inserted into the hub will always have metal to metal interaction that will chip even the best applied paint.  I think we should anodize the base of the feed black as well, to keep the finish fresh.
 
With the In house painting there was a lot of texture as well. The texture will be very light on future feeds.”
I interpreted this as the part that contacts between the dish and feed can be anodized, and sounds like a good idea. We will have a mechanical review soon of all the improvements, MicroAnt said they would schedule it soon, I’ll be sure your a part of the discussion. @Matt Philley

### Matt Philley, 2023-06-27

@Maxime Jeanneau thanks! I will be out on PTO soon, so if I am not around please ping @Marc Richardson for QA representation.

### Cameron Chapman, 2023-08-01

Maxime is leading this project, but is out until 8/20. I’ll send him a teams message.
 
It looks like he approved the next order, but some additional work was recommended. Has anyone else been working on this since Will left?
 
I recommend moving all responses to JIRA and will paste this one there. https://jenaero.atlassian.net/browse/ENGPRJ-37 
 

Maxime Jeanneau 
June 26, 2023 at 4:07 PM
 
Discussed results with Micro-Ant over google meets 6/26, have decided to move forward with procuring the next round of antennas:
We discussed:
- Moving forward with painted Aluminum dishes
- Mechanical improvements as outlined below by Will

 
Leaving ticket open until we receive the next batch. We should hear back about the mechanical improvements soon
 
 
Thank you,
|  | Cameron Chapman Electrical Engineering Supervisor Edge Autonomy – SLO (formerly Jennings Aeronautics) Email: cchapman@edgeautonomy.io Phone: (970)389-5904 |

 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Victor Vandor <vvandor@edgeautonomy.io> 
Sent: Tuesday, August 1, 2023 8:54 AM
To: Ashram <ashram@micro-ant.com>; Cameron Chapman <cchapman@edgeautonomy.io>
Cc: James Messink <jmessink@micro-ant.com>
Subject: RE: Update on MicroAnt Feeds and Dishes
Importance: High
 
Ashram,
 
I am about to send a Purchase Order for additional units.
 
I will be ordering in systems where each system consists of :  2 dishes +  2 feeds per system
 
If our Purchase order says qty 3, it means we need 3 systems
 
Please confirm everyone is on the same page
 
Also what is the lead time?  Can delivery 2-3 systems in 8 weeks?
 
Victor Vandor
Supply Chain Manager
Edge Autonomy
Previously Jennings Aeronautics
P: +1-805-544-0932
Email: vvandor@edgeautonomy.io

### Cameron Chapman, 2023-08-01

We should also point to what parts are approved and to order, even if it is just a temporary excel BOM/

### Matt Philley, 2023-08-01

Also is the purpose of the next order for Engineering Testing or is this meant to be representative of Production. We really need to make sure we understand which components are getting hard anodized versus painted and that all the require indications are permanent and visible. 
This should make it onto the FAI spreadsheet if this is something we want other groups outside of Engineering to review.

### Cameron Chapman, 2023-08-02

@Matt Philley see updated description. You are welcome to add details, questions, or comments to the improvements list above.
Current Plan 8/2: Hold on any orders, we do not have customer demand for these.

### Matt Philley, 2023-08-02

@Cameron Chapman looks good to me thanks! I will add notes if anything else comes up.

### Matt Philley, 2023-08-02

Updating due date to Oct 31,2023 based on reported Production Drop-Dead date of Nov 2023  from https://jenaero.atlassian.net/browse/ENGPRJ-405

### Cameron Chapman, 2023-08-02

@Scott Stuckey the new due date makes this higher priority. Is someone available to review the latest design from Microant and verify those changes have been implemented. @Victor Vandor says they still owe us 2 more antennas, so it would be good to verify the changes get into those shipments, review with @Matt Philley and any other parties, then have them ship that order for final confirmation and production approval. 
@Gerrit Sperling worked on this previously. Are you available. 
If not, maybe @Nadia Brown  Maxime is out until ~8/20,.

### Cameron Chapman, 2023-08-02

Talked to @Jack Waeschle , he worked on the previously and will pick it up. 
Next steps: 
- Contact micro-ant for their latest models, drawings, etc.
- Verify that they have made all of the improvements listed above.
- Check with @Matt Philley and production if they agree or recommend any more.
- Tag up with Victor, and ask him to approve them shipping the remaining 2 we ordered with these changes.
- If schedule allows, receive and inspect these 2 units, if not skip to next step.
- Complete approval, document changes, CCB, etc. and approve for production orders.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent

### Cameron Chapman, 2023-09-15

@Maxime Jeanneau , can you please update the status of the linked tasks, and create linked tasks or subtasks for the remaining steps of this project?

### Maxime Jeanneau, 2023-09-15

Handing off to Wes: 
- 2nd round of feeds have been procured, they will arrive in house and we will have to evaluate them and provide feedback
- Mechanical feedback of improvements
- Validate performance is as good as before
- Follow up with testing as described in follow up ticket [VA-116] (Micro Ant) Define test criteria for production units (aluminum) to ensure equivalent to prototype units. Test and approve for production. - Jira (atlassian.net)

### Wesley Lilienthal, 2023-10-03

@Greg Fryer @Cameron Chapman @Maxime Jeanneau Do we have an ETA on the Micro-Ant second articles? When are these due to arrive? 
Updated VA-116 with a proposal on the optimal means to characterize and evaluate antenna production sample radiated performance.

### Cameron Chapman, 2023-10-03

Maxime or @Victor Vandor would know best.

### Victor Vandor, 2023-10-03

Vendor to ship by the end of this week with painted dishes

### Greg Fryer, 2023-10-05

@Cameron Chapman moved to you from @Wesley Lilienthal . Wes has the Epic to manage all the tasks with, but should be in your sprint. Tag back if you disagree.

### Matt Philley, 2023-11-16

@Greg Fryer @Barry Mendez @Marc Richardson I dont yet see any sub-task for Customer Notification related to this change to SGCS3s, but we should probably sneak that in one of these. For most customers it sounds like it would just be a heads-up on the visual change unless there are any functional differences? 
I still dont see any on order for TIQUILA so we should be in the clear on that side of things.

### Greg Fryer, 2024-11-08

@Wesley Lilienthal Did this project finally close? Or do we have tings open? I see blocked epics, but think this is fully in production. Not urgent, but clean up helps.

### Christa Meck, 2024-12-05

Pinged @Wesley Lilienthal about this one today.

### Christa Meck, 2025-02-04

Marking this one done as all its child tickets are done.

### Automation for Jira, 2025-03-11

This item was removed from the Mission Control Dashboard.
LRR Priority was: 999.0
Company Priority was: 85.0
Current Sprint Priority was:

## Attachments (24)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [FW_ Dish Antenna - FW_ Edge Meeting.msg](attachments/11210_FW_%20Dish%20Antenna%20-%20FW_%20Edge%20Meeting.msg.md) | msg | 169 | 2022-11-01 | converted |
| [RE_ Dish Antenna.msg](attachments/11211_RE_%20Dish%20Antenna.msg.md) | msg | 143 | 2022-11-01 | converted |
| [RE_ QUOTE 80608  (EPSILON REPLACEMENT)   IMPORTANT   IMPORTANT   IMPORTANT.msg](attachments/11209_RE_%20QUOTE%2080608%20%20(EPSILON%20REPLACEMENT)%20%20%20IMPORTANT%20%20%20IMPORTANT%20%20%20IMPORTANT.msg.md) | msg | 154 | 2022-11-01 | converted |
| image-20230421-215510.png | image | 40 | 2023-04-21 | listed only |
| IMG_5680.jpg | image | 134 | 2023-04-27 | listed only |
| IMG_5681.jpg | image | 170 | 2023-04-27 | listed only |
| IMG_5682.jpg | image | 140 | 2023-04-27 | listed only |
| IMG_5686.HEIC | image | 145 | 2023-04-28 | listed only |
| IMG_5688.HEIC | image | 155 | 2023-04-28 | listed only |
| IMG_5689 (d900b9a4-a2c0-4fa0-9d2a-3c4584b82007).HEIC | image | 135 | 2023-04-28 | listed only |
| IMG_5689.HEIC | image | 135 | 2023-04-28 | listed only |
| IMG_5691.HEIC | image | 127 | 2023-04-28 | listed only |
| IMG_5692.HEIC | image | 173 | 2023-04-28 | listed only |
| IMG_5693.HEIC | image | 122 | 2023-04-28 | listed only |
| IMG_5694.HEIC | image | 128 | 2023-04-28 | listed only |
| image-20230509-221208.png | image | 755 | 2023-05-09 | listed only |
| image-20230509-221351.png | image | 990 | 2023-05-09 | listed only |
| image-20230509-221658.png | image | 222 | 2023-05-09 | listed only |
| image-20230509-222217.png | image | 235 | 2023-05-09 | listed only |
| image-20230509-222411.png | image | 240 | 2023-05-09 | listed only |
| image-20230509-222854.png | image | 335 | 2023-05-09 | listed only |
| image-20230509-223122.png | image | 658 | 2023-05-09 | listed only |
| image-20230509-223258.png | image | 589 | 2023-05-09 | listed only |
| [May2023BendLongRangeTestingAntennaReport.docx](attachments/15161_May2023BendLongRangeTestingAntennaReport.docx.md) | docx | 4480 | 2023-06-22 | converted |
