# ENG-1344: Top Cutout Battery Area Enlargement Investigation

- **Issue type:** Sub-task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-04-12
- **Updated:** 2023-11-09
- **Resolved:** 2023-08-29
- **Reporter:** Hans Hershberger
- **Assignee:** Hans Hershberger
- **Creator:** Hans Hershberger
- **Parent:** ENG-904 Epsilon E140Z G2 VXE Vehicle Productionize
- **Links:** blocks ENG-913 (Make 107-110926 Fuselage Skin DWG); blocks ENG-907 (Update fuselage cutout trim paths); is blocked by ENG-1500 (Battery Connection Angle between Lift Battery and Centerwing); relates to VXEP-39 (TPTR-54 minor cut/graze caused during the removal of a HLB); relates to ENG-918 (Release changes to fuselage for Epsilon payload modification)

## Description

Investigate fuselage assemblies and edge chipping to determine how the top cutout battery area should be enlarged.

## Comments (17)

### Hans Hershberger, 2023-04-17

@Jeremy Roberson Jeremy!  See attached image for the area that can be enlarged for the battery.  The back section has already been appropriately enlarged for Epsilon payloads.  Also, while we currently are using the 965-1-01-7001-1 Fuselage Skin in our builds, we will are making changes to the 107-110926 Fuselage Skin, as this will replace the prior part upon its release.

### Jeremy Roberson, 2023-04-17

@Hans Hershberger Thanks!

### Artis Bertulis, 2023-04-18

I agree with removing the material, I don't with using a tool to disconnect the cable.
This comes from experience with product that took many tools to assemble - it's a pain in the ass, and customers will complain. Especially if we introduce an extra tool to a solution that didn't need any. We should look into redesigning the connector, or having the battery connector facing up, and not into the fuselage wall, or having something to grab on right next to the connector/cable.

### Hans Hershberger, 2023-04-18

@Jeremy Roberson please break the cutout enlargement and battery connection issues into two separate Jira tickets.  I.E make a new Jira ticket for the connector issues/concerns.

### Jeremy Roberson, 2023-04-20

@Hans Hershberger  https://jenaero.atlassian.net/browse/ENG-1500

### Hans Hershberger, 2023-04-20

@Jeremy Roberson How is progress going on this?  Have you changed the CAD yet or would you like me to do that?  Thanks!
I.E. has the CAD been updated for CAM and drawing purposes.

### Jeremy Roberson, 2023-04-21

@Hans Hershberger I can update the CAD. I’ll get with you to sort it out.

### Jeremy Roberson, 2023-04-25

[embedded: image-20230425-231716.png]
@Hans Hershberger

### Hans Hershberger, 2023-04-26

@Jeremy Roberson Thank you so much buddy.  I will take a look at those edits in a bit and make sure the respective drawing updates appropriately.  I look forward to getting this buttoned up.

### Hans Hershberger, 2023-04-26

CAD looks good.  I will move on to making any necessary drawing updates/making sure changes propagated.

### Hans Hershberger, 2023-04-26

@Jeremy Roberson Looking at the drawing, it appears that shortening the fore dimension of the cutout has slid the whole cutout forward by the subtracted amount.  Consider bringing that dimension back to original value, making its associated line a construction line, creating a new cutout line to the dimension desired, and connecting everything with associated fillets etc.  There are also many alternate ways to do this, but that is the first that comes to my brain.  If you have questions on it or are unsure how to do it, let me know.  I can also totally dive in there and make the changes pretty quickly as well.  Thanks again!

### Jeremy Roberson, 2023-04-26

@Hans Hershberger Contact me on Teams when you are available and I will swing by

### Jeremy Roberson, 2023-04-27

@Hans Hershberger Check 
[embedded: image-20230427-220007.png]
shoutout to @Luca Lauritzen for his CAD expertise!

### Hans Hershberger, 2023-04-28

CAD and drawings look good.  Marking as done

### Cameron Chapman, 2023-08-29

This issue seems prematurely closed. The change should go through ccb. Was that done? If so, please link to this one.

### Hans Hershberger, 2023-08-29

Has already been enlarged, rev’d and accepted by CCB months ago.  @Jeremy Roberson was in charge of making the top larger.  This issue has been already fixed in the new fuselage skins.  @Cameron Chapman please check with someone before making assumptions and opening old tickets

### Cameron Chapman, 2023-09-02

Opening an old ticket is and asking to link the engineering change is checking with someone and correctly closing the task.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 9c382f2a-3a59-419d-b442-0e6b0e9f4499.png | image | 118 | 2023-04-17 | listed only |
| [ENG-1344NEW.pptx](attachments/13961_ENG-1344NEW.pptx.md) | pptx | 97986 | 2023-04-18 | converted |
| image-20230425-231716.png | image | 25 | 2023-04-25 | listed only |
| image-20230427-220007.png | image | 15 | 2023-04-27 | listed only |
