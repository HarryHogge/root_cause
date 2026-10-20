# VXEP-640: IRAD: B40 Battery Charger

- **Issue type:** Initiative
- **Status:** New
- **Priority:** Medium
- **Created:** 2023-02-08
- **Updated:** 2026-07-30
- **Reporter:** Greg Fryer
- **Assignee:** Tom Westrich
- **Creator:** Greg Fryer
- **Links:** relates to ENG-232 (Certify battery cases/kits for shipping); relates to ENG-1070 (IRAD: Battery Study Next Gen Lift); relates to ENG-1369 (100-106835 Chargery Power Supply S600PLUS Potential New Version); relates to VXEP-232 (Overheating Battery/Cable (Fuel Cell Support Kit SCO Test Config) -); relates to VXEP-720 (VXE 490 main battery percentage reporting incorrectly during flight with MB's (S/N's 1967 and 1737)); relates to BAT-433 (Initial Delivery Battery Charger Development Tasks); relates to BAT-134 (2130966-02 Development); relates to BAT-498 (Battery Charger Round 1 Validation); relates to XKIT-5435 (B40 Prototype Main Battery Charger not charging due to connector failing out. )
- **Leadership Stakeholder:** Sam Miller
- **Job Number:** J100068 - Battery_NextGenCharger [2023 Code]?

## Description

Conceptual Design Review (CoDR) Universal Battery Charger.pptx
2025 US Battery Charger Requirements.xlsx
Project Working Folder:  Battery_NextGenCharger

## Plan

New charger delivery to SLO ETA 4/20 Tom Westrich: Here is the Charger schedule that I was working on this morning.  Ca... | Drew, Grace, Jessica, +6 | Microsoft Teams
Actions from 9/19/25 concept review. Need to update status of each
- Turn these actions into specific new or linked JIRA tasks
- Did you have a chance to review SLO design and review process? Thoughts of using it, or combining best aspects of each?
- Create design artifacts sheet with links. Link to presentation.
- Check LRR, TIQUILA, etc for requirements. charge rate, time, size, etc
- Add shipping, packing requirements. Need to think what is the best arrangement to limit packing space, optimize operator experience. How many per battery case/system.
- Trade study to see if it makes more sense to reduce batteries charged in parallel, combined discharger or separate, charge and discharge rates vs size and development cost and ROM.
- I think we probably want everything as small as possible for SOF users. Users who want more capacity can order more things.
- Adapt requirements to threshold and objective. Determine ROM for different feature sets.
- Threshold
- User method to update firmware.
- Objective
- GCS connection
- Add input power requirements. Expected 15A to work with standard outlet. Markings to indicate do not plug in parallel loads?
- Should we have FLOPs, PMs, BD, or customer service review the basic requirements and use cases? What requirements do customers want most. Ex: input voltage.
- Ask Sam and Josh. Business case. Seems like there would be a market for this product for other US drone manufacturers. Do we want to consider selling it standalone? Risk of helping our competitors, but commercial drones will likely want something like this.

## Comments (4)

### Cameron Chapman, 2023-03-06

Sent this email 
Hello Sam and Allen,
 
I am hoping to determine the scope of work for the “Battery Charger Upgrade Project”. I would like to answer the following questions before kicking it off. Would you prefer to answer in a call or email?
 
- The IRAD sheet just says "Consider FoxBMS. https://foxbms.org/ "  Are there any more details available for project definition?
- Sam mentioned that Ann Arbor may be a good candidate to lead this project under the "Energy Systems" domain. Do we want Ann Arbor or SLO to lead this project?

- The JIRA initiative is assigned to Cameron. The IRAD sheet lists Sam (Interim)

- Do we require a US made charger, NATO, or just not China?
- Does this effort also include the charger power supply (currently made in China), or just the charger? Guessing both.
- I think we should add the requirement to include a decent discharger (for shipping prep and potential capacity tests). This could either be included in the same device or separate.
- What is the ideal packaging?

- Charger can charge batteries in the case with input cables exiting the case?
- Bench top.

- Do we still want one charger per battery type or one for all that adjusts charge rate accordingly? We could likely accomplish this with a CAN connection to the current HLB.

- Do we still need to support XE25 hybrid batteries?

 
https://jenaero.atlassian.net/browse/ENG-371

### Cameron Chapman, 2023-04-19

On hold due to bandwidth/higher priority tasks. See https://jenaero.atlassian.net/browse/ENG-1474

### Christa Meck, 2025-03-04

@Greg Fryer  and/or @Tom Westrich Does this work from 2023 need to be completed?

### Cameron Chapman, 2025-11-20

Reopened, unless there is another Jira for the B40 charger. @Mike Gorski. If so, please link. Please also add this feature. https://jenaero.atlassian.net/browse/VXEP-1615

## Attachments (0)
