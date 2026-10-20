# VXEP-140: Sparking on boom connection of 565

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2023-10-10
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Greg Fryer
- **Assignee:** Cameron Chapman
- **Creator:** Greg Fryer
- **Links:** is blocked by VXEP-141 (VXEP-140   Sparking on boom connection of 565 Identify C/CA); causes VXEP-144 (VXEP-140 Sparking on boom connection of 565 CA: When creating SCO procedure, follow manual during boom installation)
- **Production Stakeholder:** Trevor Gronner
- **Other Stakeholder (as required):** Matt Philley
- **Problem Type:** Production Issue
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

The damaged ESC has been replaced, but the boom still sparks when hot swapped.
Normally I would push to just have SCO follow the manual, but since one ESC/Motor already torched itself in this boom assembly, and we had another ESC go bad, it feels like an investigation of the other ESC is warranted as well.
Do we have a set of defects occurring on the ESC boards? e.g. stray solder, bad board mfg, bad chips, etc.
AC 565 - Lift Boom Connector Scorch Marks
AC 565 - Lift Motor Stall and Overheat during SCO Ground Checkout
Rear left lift motor ESC fried

## Comments (10)

### Greg Fryer, 2023-10-10

LMK if you think i should handle this, but otherwise just assign some EE time since this is an interrupt. Happy to discuss. Production is already pulling both lift ESC/Motors and the wiring from the boom to deliver. To Connor notionally, but feel free to reassign.

### Cameron Chapman, 2023-10-10

@Connor Peebles mentioned he was working this. He mentioned the harnesses were replaced for cosmetic reasons (customer would question sparked contacts). @Connor Peebles can you please update current status?
@Connor Peebles Questions
- The booms are not supposed to be hot swapped per the manual. Should we update EA procedures to train and prevent this? Can you please create linked task and add details. 
- The ESCs are supposed to have soft start circuits, but do not seem to work as evidenced by sparking. This is true for all ESCs. They usually are not damaged by a few sparks, so that may indicate a unit specific issue.
- Please link to damaged ESC, suspect ESC, and harness issues/NCRs.
- Let me know if you have bandwidth for this.

### Connor Peebles, 2023-10-10

- There are no current procedure for SCO, it has so far all been tribal knowledge from Carson. Someone mentioned that they were starting to write these procedures down, @Matt Philley may know more. Artis mentioned that they follow the manual out in the field, but in SCO they have been hot-swapping the booms.
- done, in task description
- maybe, if it is production stoppage then we can put it high priority

### Connor Peebles, 2023-10-10

a note that I found, if you insert the connections fast and level enough, you don’t get any sparks

### Matt Philley, 2023-10-10

There is no procedure, however SCO checkout is performed and documented per 107-102560 Complete Aircraft, Standard Configuration, SCO Procedure (Doc# 103962) in the vault, which is the checklist that is printed and filled-out for every aircraft as it goes through SCO checkout. 
The excerpt below covers the order of operations for assembly which describes to connect centerwing to power first then install lift booms. It is worth a conversation with Carson if there is a desire to change the process.
Trevor G and his Production Engineering team currently have the ball to document SCO procedures since SCO is still under Operations. 
There has not been any communication about a production stoppage related to this, just the NCRs for AC 565 and replacing components now that they have scorch marks. All other aircraft will be assembled and tested the same way unless someone else steps in to say there is a large enough problem to stop and change.
Right now we just have a single NCR and SCO saying they have not changed they way they are doing things… so unless we have more NCR’s for damaged components or someone else raises a flag then QA does not have reason to put a hold on SCO. 
[embedded: image-20231010-183953.png]

### Connor Peebles, 2023-10-11

See linked ‘blocked by' task for identified C/CA and linked 'causes’ task for Corrective Action

### Carson Buckley, 2023-10-12

@Connor Peebles @Matt Philley If the vehicle SCO is completed as a single process, the booms will already be installed on the Center Wing. If the process is out of order, or done in non-standard flow, only then do we install booms on a powered vehicle. This has been normal practice since day 1, but we can easily switch our process to align with the manual.
My important question that needs to be answered however is; Why is this vehicle more sparky than any other vehicle we have done? An absolute minimal ‘spark’ has been considered normal, due to the weak soft start, but they do not ever create damaging arcing unless something is wrong. I highly urge for this vehicle to be investigated to ensure there are no other issues beyond a weak soft start which is causing this arcing damage.

### Connor Peebles, 2023-10-12

@Carson Buckley @Matt Philley I understand and from quick testing we could see that one of the lift ESCs were more likely to have arcing than compared to a standard sample I had on my bench. I will recommend engr holding these components for further investigation, but that would probably be put into a sprint and not looked at right away.
That being said, I’ve found that attempting this with any lift ESC and motor assy, you can always produce arcing if you try to poorly mate it. Even on the Ironbird in electronics and those are 2 years old.
Cameron and I are confident that this isn’t a systemic issue or reoccurring defect other than poor design.

### Matt Philley, 2023-10-12

(will copy to comment in NCR 1654 as well)
Based on comments below and chat with Connor we will recommend that Production replace the following components, so that Engineering can keep them until they are able to further investigate the cause of the difference in behavior.
Lift Motor & ESC, CW - SN: C-S100943
Lift Motor & ESC, CCW - SN: C-S101056
Lift Boom Harness: C-S101190

### Carson Buckley, 2023-10-12

@Connor Peebles @Matt Philley Sounds good, thank you. The SCO packet has already been updated to reflect the (minor) change in assembly procedure.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20231010-183953.png | image | 41 | 2023-10-10 | listed only |
