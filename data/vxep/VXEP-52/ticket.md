# VXEP-52: 107-102262 LED Button Design Improvement Request 26g Wire

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2022-10-14
- **Updated:** 2025-04-28
- **Resolved:** 2025-03-11
- **Due:** 2022-11-25
- **Reporter:** Matt Philley
- **Assignee:** Cameron Chapman
- **Creator:** Matt Philley
- **Links:** is blocked by VA-504 (NCR-230913 - 1515  Incorrect Gauge Wire Used in LED Button Assy -Determine plan to address. ); is blocked by VA-513 (Find most-finished discrepant assy and deliver to engineering (for mechanical eval)); is blocked by VA-514 (Inspect assembly provided by production, determine if wires are impacted or if vibration of board will be limited/increased.)
- **Part Number(s):** 107-102262
- **Production Stakeholder:** Emalee Johnson
- **Incident Type:** Squawk
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Next Steps:
- Engineering to determine via CAD and/or fit check if there will be bend radius issues using 26AWG instead of 28AWG in the small area between the lift AP and avionics cover. -Matt P has a sample available for fit check.
- If bend radius is acceptable, open up subtasks to consider switching to 26AWG for all connections on the top of the LIFT AP (CW harness, magnetometer,  GPS, etc.). Consider weight impacts for each.
- Decide effectivity and priority if change is warranted.
- Update and release documents.

Due to repeated NCRs the Production team is requesting the following change to improve the manufacturability and reliability for this assembly:
Is: 28g wire for 3 wire leads
Proposed: 26g wire for 3 wire leads (assembly weight 5g)
A sample part was made and is available for Engineering to review. Electronics and SCO agree this would be a great improvement for a more robust assembly. The existing 28g wire is extremely thin for crimping and assembly. There is concern damage is being caused by pull testing with such small connections, so the extra thickness will help provide a lot of confidence.
NCRs:
247 - Fail Pull Test
266 - Pins not Seated
426 - Not operational in SCO
1515 - Used in LED Button Assy
NOTE: The traveler is also being revised and we are planning to implement a functional check in Electronics as well.

## Comments (13)

### Matt Philley, 2022-10-14

@Cameron Chapman @Connor Peebles  FYI
@Greg Fryer  FYI this is the type of request I am not sure how to communicate priority to the Engineering team

### Greg Fryer, 2022-10-14

@Matt Philley I am planning to update are Jira setup in a couple ways. One of which is to make a “Product Improvement” issue/workflow. This sort of thing (even when small like this) would land there, and Engineering would be regularly allocating time to implement them. So, your hardware issue would work just like it is currently (and you could close it once you’ve done what you can without a design change), but you’d be able to create a new issue that we would tackle. (“Based on available people and priorities” - hate saying it, but true right now.)
Plan to start updating Jira next week.
@Kyle DeBernardi @Ryan Ferguson This is also where things like the Band-It clamp would end up. Who is doing the work is just a matter of assignee.
Let me know if that seems like it will work, and once we have something, let me know if you see any issues. (Working on a way to record that too.)

### Matt Philley, 2022-10-14

Sounds good to me. Thanks @Greg Fryer 
Once there is a process or framework I think it would be great to sit down and run through it.

### Cameron Chapman, 2022-11-15

Next Steps:
- Engineering to determine via CAD and/or fit check if there will be bend radius issues using 26AWG instead of 28AWG in the small area between the lift AP and avionics cover.
- If bend radius is acceptable, open up subtasks to consider switching to 26AWG for all connections on the top of the LIFT AP (CW harness, magnetometer,  GPS, etc.). Consider weight impacts for each.
- Decide effectivity and priority if change is warranted.
- Update and release documents.

### Matt Philley, 2022-11-15

@Cameron Chapman I still have the sample part here at my desk if anyone would like it for that fit test action.

### Matt Philley, 2023-09-13

@Cameron Chapman @Greg Fryer it looks like Production incorrectly made a Lot of Qty 30 of these using 26g instead of 28g (the same as this change request from long ago).
I am working on the NCR right now to understand the scope, but looks like we have already shipped several aircraft this way.
Can you weigh as an initial gut-check if you think this is a high risk and Engineering will need to do some testing (or we will need to think about sending aircraft back) or lower risk but annoying and the function should be OK? It looks like the evaluation you outlined lower was mostly fit check related. 
I will work on a more formal NCR soon.

### Cameron Chapman, 2023-09-13

@Matt Philley The risk is that the 26 AWG will be too stiff relative to the 28AWG, which could cause the AP boards to push against the lid and ruin the critical vibration isolation. Here is what we could do. I am guessing @Greg Fryer as the product owner would be the one to decide which option, after discussing with other stakeholders. 
- Mechanical Engineer to determine via CAD and/or fit check if there will be bend radius issues using 26AWG instead of 28AWG in the small area between the lift AP and avionics cover. -Matt P has a sample available for fit check. @Matt Weber @Scott Stuckey 
- Maybe inspect via borescope?
- Rework all of the ones in our custody. This shouldn’t be a crazy rework, as they are just secured with solder and adhesive heat sink.
- Need to determine risk and plan for shipped aircraft. See item 1. 
- @Matt Philley are you able to create a list of what aircraft and customers got these parts?

### Greg Fryer, 2023-09-13

@Matt Philley @Cameron Chapman FYI I moved the old XE item to current VXEP board, and made the task Cameron created a proper blocker.
@Trevor Gronner or @Kelly J Furlong can I get a quick estimate on the pain (hours of work) required to rework? Want to weigh that against the time delay to have Eng screw around with it do analysis and test, and the remaining risk that we don’t know what will happen for sure.

### Cameron Chapman, 2023-09-13

@Greg Fryer that sounds like a good plan, I think we will need engineering to look into it either way, due to the vehicles shipped with these parts.

### Greg Fryer, 2023-11-08

@Cameron Chapman This one stalled out after Scott took a look and it looked fine, mechanically. I just shifted it over to you, we should either close or update the drawing to 26g. Maybe as part of the larger harness drawing effort?

### Cameron Chapman, 2023-11-08

@Greg Fryer I didn't see any analysis or summaries saying that 26AWG wire would not cause any clearance issues to the CW cover. It is very important to not affect the vibration isolation of the AP board. 
If that was done and approved, then there should be no issues modifying these harnesses to use 26AWG. Was that done? 
Do we want to borescope during an install? 
We should weigh the difference, but it is likely only a few grams. 
If approved, we can create linked tasks to update each affected harness. 
FYI @Emalee Johnson

### Christa Meck, 2025-03-11

@Cameron Chapman and/or @Matt Philley Does this work from 2022 still need to be completed?

### Cameron Chapman, 2025-03-11

Cancelling. We will likely remove this button in B40 before we spend time evaluating this change request.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 26g wire.JPG | image | 3811 | 2022-10-14 | listed only |
| 28g wire pic 1.JPG | image | 3838 | 2022-10-14 | listed only |
| 28g wire pic 2.JPG | image | 3893 | 2022-10-14 | listed only |
