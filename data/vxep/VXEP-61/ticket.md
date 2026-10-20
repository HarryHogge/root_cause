# VXEP-61: More mounting holes than needed on SGCS-3 dishes.

- **Issue type:** Sub-task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-02-21
- **Updated:** 2025-02-28
- **Resolved:** 2023-08-15
- **Reporter:** Kurt Burian
- **Assignee:** Gerrit Sperling
- **Creator:** Kurt Burian
- **Parent:** VXEP-55 Alternate (or replacement) long range SGCS-3 dish vendor (MicroAnt)
- **Links:** causes ENG-1058 (96X-3-14-5326-1 Antenna Mount Arm Hole Pattern Change (From 8 holes to 4))
- **Sprint:** VXE-2 ME Sprint Team 8-28
- **Job Number:** J100082 - Sustainment: Ground Hardware

## Description

We need the new dish to have 4 holes.instead of 8 for mounting the quick release. Epsilon dish drawing doesn't have them but the epsilon dishes do for whatever reason. 
We don't need the extra or the 4 holes on the larger outer radius, but the larger radius holes aren't hurting anything.
Explanation of issue:
The issue that we’ve noticed is that while the mount is 4-prong and 4 bolts, the dish and mounting arm are 8 bolts. There is no indication (currently) during assembly that the mounting ring needs to be installed in a particular orientation. Operators won’t figure this out until they have secured the dishes and moved on to installing the feed, only to find they are 45 deg clocked￼

## Comments (12)

### Former user, 2023-02-21

Before we move forward with this, we should confirm that there is not operational reason to have 8 mounting holes. The LM folks may be able to help answer this. @Dustin Gamble @matthew.curran @Daniel Lloyd 

If we move forward, 96X-3-14-5326 (SGCS-3 Antenna Mount Arm) will also need to change to resolve alignment issue unless.
Changing the number of holes will only help for new parts. Since all of the stocked and fielded SGCS-3 hardware was built with 8 holes, the fix needs to extend labeling and documentation.

### Daniel Lloyd, 2023-02-21

I’ve never seen a need for the extra holes

### Cameron Chapman, 2023-03-31

Microant to remove these holes on the upcoming dishes if they pass prototype testing. See https://jenaero.atlassian.net/browse/ENGPRJ-37

### Former user, 2023-04-03

@Cameron Chapman @Kurt Burian Is there a drawing/document we need to update to communicate the removal of 4 holes from the dish? Or do they maintain the design and we just need to notify them?

### Kurt Burian, 2023-04-03

@Former user I would reach out to them and ask for drawings or step files if it’s in question. We provided the documents on https://jenaero.atlassian.net/browse/VIT2-41 , but have had a few calls since this projects inception. We should make sure what they are building makes sense.

### Cameron Chapman, 2023-04-04

@Former user , maybe obvious, but we should save the files they send us to the vault and assign a PN for them.

### Former user, 2023-04-05

I have removed the 4 holes from the dish to match the 4 hole mounting pattern on the arm. this is just for a proper visual representation on our drawing 105-107149, as we do not own the CAD design. The information has been handed off to Micro-ant so that the hole pattern can be implemented into production. This change will not make it into the prototypes (see email attachment for details).

### Cameron Chapman, 2023-04-14

@Former user do we have drawings from micro ant for the updated design? We should request them if not. I think We will need them for quality inspection and to ensure they deliver to the agreed design specs. Reopening this task until that is resolved.

### Former user, 2023-04-21

@Cameron Chapman I am not sure what has been used in the past, and what was supplied to MicroAnt by Enoch to manufacture the dish. @Gerrit Sperling Can you please look into this and see if we have any existing documentation, of if we can get a drawing from MicroAnt?
If not, we can create a COTS inspection drawing to define the physical characteristics for QA.

### Gerrit Sperling, 2023-04-21

The drawing 105-107149 was sent to microant for them to produce the part. The drawing specifies mounting requirements and fitment requirements for the foam case.

### Cameron Chapman, 2023-04-21

I was mostly thinking of a drawing and documentation from microant to list things like size, weight, tolerances, performance, etc for quality and functional verification. It looks like we have a design review planned. We can ask Microant then. https://jenaero.atlassian.net/browse/ENGPRJ-38 
FYI @Maxime Jeanneau

### Gerrit Sperling, 2023-08-15

Closing this ticket, the hole quantity change is captured in the released 96X-3-14-5326 drawing.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| PXL_20230221_201921872.jpg | image | 2514 | 2023-02-21 | listed only |
| PXL_20230221_201927706.jpg | image | 1321 | 2023-02-21 | listed only |
| [RE_ JEN-003_ Status Update.msg](attachments/13453_RE_%20JEN-003_%20Status%20Update.msg.md) | msg | 612 | 2023-04-05 | converted |
