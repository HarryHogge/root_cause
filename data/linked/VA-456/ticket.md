# VA-456: HLB Connector Mate Indicator

- **Issue type:** Engineering Change
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2023-09-06
- **Updated:** 2025-09-15
- **Resolved:** 2025-05-28
- **Reporter:** Hans Hershberger
- **Assignee:** Desiray Johnston
- **Creator:** Hans Hershberger
- **Labels:** TIQUILA-Blocker
- **Links:** relates to VA-95 (8D #24 Update HLB Lift Connector to include some physical indication connection is fully seated. Evaluate adding to similar power connectors ); blocks VXEP-12 (TPTR-87 VXE 511 VTOL Connector Issues 516 CW. Contains Main connector/contact C/CAs)
- **Part Number(s):** 107-114271, 107-102264
- **Job Number:** J100078 - Sustainment: VXE-30
- **Link to Engineering Change Notice (ECN):** ECN #97 107-114271 HLB Mate Indicator.xlsx

## Comments (15)

### Matt Philley, 2023-09-06

This is tied to Customer Issue https://jenaero.atlassian.net/browse/VXEP-12 
The customer has requested some additional testing and will probably need to buy-off on this change. I think Sam and/or Greg would have the most info on what that testing will need to be, but based on what I have heard so far it was something like the following:
- Some form of physical durability testing (i.e. does it stand up to normal handling plus insertion and removals, any fraying, lack of adhesion, etc.)
- Heat resistance (does it turn into goopy mess when it gets hot)
- Cold resistance (any issue if it gets really cold/freezing)
- …?

### Matt Philley, 2023-09-06

@Hans Hershberger answering you question about where to call this out on the change ticket since this is the one more likely to be reviewed in CCB and that is a good CCB type question:
[embedded: image-20230906-223252.png]
I think this would need to go on the assembly level so Electronics applies the label during fabrication of the harness unless our vendor who makes the connector housing is able to apply it confidently… I would probably lean toward Production applying it in Electronics, which would be on drawing 107-102264 Dual Current Sense Assy.
Production and Supply Chain should weigh in on this decision (assuming this passes testing mentioned below).

### Matt Philley, 2023-09-11

@Greg Fryer @Hans Hershberger I see the 107-102264 Dual Current Sense drawing was pulled into CHANGE IN PROCESS with a note to add HLB label. We should really have a design review before pushing forward this change since there are so many stakeholders.

### Matt Philley, 2023-09-11

I dont think anyone from our own SCO or Flight Test team has gotten their hands on this label. We just had another internal occurrence of the connector not being mated fully. 
We should coordinate a test with them to review this solution.

### Matt Philley, 2023-09-14

@Hans Hershberger can you touch base with @Carson Buckley so he can take a look at the decal? Or can you let us know where we can take a look at it installed?

### Hans Hershberger, 2023-09-14

@Matt Philley @Carson Buckley There is an Avery label prototype on center wing 300.  I have a bunch of labels and a labeled connector on my workbench in the engineering bay

### Matt Philley, 2023-09-14

@Hans Hershberger thanks! I will try to look myself today, but Carson has said they look really good.

### Carson Buckley, 2023-09-14

@Hans Hershberger @Matt Philley  Tested the sample on CW 300 with an asset battery, pictures attached. With the connector pressed on until it meets the O-ring there is sufficient visible line to indicate no-go. Fully seated the indicator is obscured.
I like this solution, how soon until we can expect this to be rolled into production?

### Hans Hershberger, 2023-09-14

@Carson Buckley I have about 10 FA labels from Crisp Imaging Central Coast.  It has been decided that they are good enough to send out with an FSB for this issue.  I did find that the red no-go area has been shifted up some 15 thou meaning it isn’t as occluded as the Avery prototype on 300.  I am working on getting a new test run of those for production.  Once that happens and and this design goes through all the gates of this D4/6/8 control acceptance it will be on our stock center wings.
Label PN: 107-114271
Higher Level Assy (where it is attached w/ indexing instruction): 107-102264
The associated AD and FSB are Stalker Airworthiness Directive #2023-09-11 and VXE-SB-23-002 respectively

### Greg Fryer, 2023-09-14

@Hans Hershberger Isn’t 100-102570 the raw connector housing from Maglio? Don’t we need to put the label on in an assembly? Or are we changing the OTS part from Maglio to include the label?

### Hans Hershberger, 2023-09-14

Ah shoot I’m going too fast and I messed up.  @Greg Fryer yes 100-102570 is the Maglio part.  I will edit my earlier comment.

### Greg Fryer, 2023-09-14

@Hans Hershberger Move fast and break things. Ping me as soon as you have the assembly together, and I will corner Scott to review and release.

### Hans Hershberger, 2023-09-14

@Greg Fryer the assembly is ready to be judged/released.  It is 107-102264.  All is correct on ECN 97

### Hans Hershberger, 2023-09-14

There is a drawing of the current sense assembly (where the label goes) and the label file on the release table

### Greg Fryer, 2023-09-20

All content of ECN 97 released and approved by CCB. Catching up this workflow to Implementing, and assigned to @Desiray Johnston.  (Let me know if you track here, or track with a different task. I need to keep the link to https://jenaero.atlassian.net/browse/VXEP-12 for tracking the overall issue.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20230906-223252.png | image | 12 | 2023-09-06 | listed only |
| Side Not Seated.png | image | 239 | 2023-09-14 | listed only |
| Side Seated.png | image | 262 | 2023-09-14 | listed only |
| Top Not Seated.png | image | 237 | 2023-09-14 | listed only |
| Top Seated.png | image | 238 | 2023-09-14 | listed only |
