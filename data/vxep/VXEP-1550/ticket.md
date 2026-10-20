# VXEP-1550: Not MVP: Load shedding in emergency conditions

- **Issue type:** Story
- **Status:** To Do
- **Priority:** Medium
- **Created:** 2025-09-19
- **Updated:** 2026-10-06
- **Reporter:** Cameron Chapman
- **Assignee:** Madeleine Moir
- **Creator:** Cameron Chapman
- **Parent:** VXEP-1549 BLK 40 OPEN REQUESTS (Need to be prioritized)
- **Links:** relates to XKIT-5456 (Ranked B40 firmware electrical requests); relates to FS2-2522 (B30+40: Implement 12V load shedding when vbatt gets too low or overcurrent detected. ); relates to FS2-3976 (Automatic load shedding or shutoff recommendations in certain flight phases to optimize endurance); relates to BAT-402 (MPQ600 28V Converter Thermal Shutdown); relates to BAT-1143 (Quantify the contribution of 56V load on heating up the 28V converter/reducing its capacity)
- **Epic Link:** VXEP-1549
- **Issue color:** orange
- **Issue Status:** B40 Load Shedding Trade.pptx

## Description

I have a greater goal (not sure how realistic)of having one location to document existing and planned cautions, warnings, automatic actions. I started this sheet for that. Stalker CAWs and Automations.xlsx
I am listing load shedding outlines that can be filtered in the type column "28V load shedding" additions, comments, updates welcome

Triggers
- Low battery pack or cell voltages.
- Current higher than limits on any bus

Load shedding.
- Turn off non-critical 28V bus
- ADo we want a similar functionality where we shutoff Fwd motor when an extreme battery condition exists? Ex: cell failing, would catch on fire with additional motor use, but could still power avionics to glide land. Longer term, having a shared bus for both batteries would make this much less likely

## Plan

- Available to test in latest DCDC FW


Old
- Teams chat has latest Cameron Chapman: Erik Hanson did you bring these projects to SLT yet? We think we...
- Outline, review, approve recommended load shedding conditions. @Cameron Chapman
- Coordinate FW updates to battery to implement.
- Coordinate/plan future aircraft FW updates.,

I have a greater goal (not sure how realistic)of having one location to document existing and planned cautions, warnings, automatic actions. I started this sheet for that. Stalker CAWs and Automations.xlsx
I am listing load shedding outlines that can be filtered in the type column "28V load shedding" additions, comments, updates welcome

## Comments (4)

### Scott Whitney, 2025-09-26

@Cameron Chapman  - do we have more details around this requirement? We need to understand the intent of this before it can be implemented in the avionics software. 

For example: 
- The BMS reports current at ~1Hz (instantaneous current). Is that sufficient, or do we need a flag from the BMS that says we had an over-sense fault since the last current report?
- Will the three 28V non-critical be prioritized? Do we turn one at a time off or all 3?

### Cameron Chapman, 2025-09-30

@Scott Whitney 1Hz is acceptable. Anything faster could be limited internally to the BMS. Let me know if any other requirement questions. 
- Are we currently monitoring total 28V current or individual?
- MVP: if monitoring just 28V, shut off all non-critical.
- Ideal: monitor each bus and shut off the highest/most over the limit bus. This would require changes on the aircraft side and possibly the battery. @Mike Gorski what current monitoring options does the battery HW and FW have?

### Mike Gorski, 2025-09-30

@Cameron Chapman the non-critical load switches have internal current monitoring that can be used to report the current of each channel.

### Cameron Chapman, 2025-09-30

@Mike Gorski Thank you. Apologies if sent before. Do you have a shared location of current CAN messages, and future planned/potential ones?

## Attachments (0)
