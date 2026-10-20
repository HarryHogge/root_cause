# VXEP-12: TPTR-87 VXE 511 VTOL Connector Issues 516 CW. Contains Main connector/contact C/CAs

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-08-23
- **Updated:** 2025-05-28
- **Resolved:** 2025-05-28
- **Reporter:** Allen Gardner
- **Assignee:** Cameron Chapman
- **Creator:** Allen Gardner
- **Labels:** Weekly-incident-tracker
- **Links:** relates to ENG-2983 (511 LW motor test failed. 511 and 516 center wings damaged. ); relates to VXEP-481 (8D #24 – CW to HLB AS150 Connection Issues​ Corrective Actions); relates to VA-35 (511 CW Input power connector damaged); relates to VA-31 (EA Internal: 516 center wing damaged. 511 fuselage+516CW LW motor test failed. ); relates to VA-474 (TPTR-87 VXE 511 VTOL Connector Issues - Identify short and long term connector improvements. ); is blocked by VA-475 (Place an order for a qty (UNK 10-20?) of dual sense current boards.); relates to FS2-952 (Do any of the flight logs list what equipment was connected? If not, could we add this feature?); is blocked by VA-468 (TPTR-87 VXE 511 VTOL Connector Issues-Create and implement SB and/or AD); is blocked by VA-469 (TPTR-87 VXE 511 VTOL Connector Issues-Create, procure, and document kit for SB/AD application. ); is blocked by VA-164 (Check manual for guidance on reapplying grease to power connector o-rings. Add if not present. ); is blocked by VA-501 (TPTR-87 VXE 511 VTOL Connector Issues - Prepare and submit data package for customer. ); is blocked by VA-95 (8D #24 Update HLB Lift Connector to include some physical indication connection is fully seated. Evaluate adding to similar power connectors ); is blocked by VA-456 (HLB Connector Mate Indicator); relates to VA-553 (Review and improve receiving inspections for AS150 contacts); relates to RMA-128 (VXE 511 070523); is blocked by VA-573 (Poor Quality/higher impedance plating on AS150 power contacts - Containment and Corrective Action); relates to VXEP-101 (VXE-487 488CW Damage to Center Wing power connector -Motors stopped at 90ft during VTOL landing); is caused by VA-93 (Record typical, max, and max tested lift current and voltage profiles. Save test data to confluence. Establish and implement limits and abort if exceeding.); relates to RMA-129 (VXE 516 230705 TIQ); relates to VXEP-272 (VXE-425 Crash on VTOL landing-ESC Damage); relates to VXEP-231 (VXE-496 with 550 wing set-failure during VTOL transition-AS150 contact issues); relates to VXEP-315 (VXE 459 Overshoot of LZ Mishap on landing, operator unable to nudge); relates to VXEP-415 (VXE 538 Altitude Drop During Landing); relates to VA-1374 (Add power contact and inspection cleaning to appropriate training documents/manuals. (Check first if not already there))
- **Customer:** TIQUILA
- **Vehicle Tail Number:** VXE 511
- **Production Stakeholder:** Trevor Gronner
- **Supply Chain Stakeholder:** Former user
- **Other Stakeholder (as required):** Matt Philley
- **Severity:** 3 - Degraded Performance - With Workaround
- **Impacted Disciplines:** Hardware, Quality Assurance

## Description

File location: https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Investigations/Old%20Docs-use%20flight%20safety%20Incident%20Reports%20-%20Shortcut%20now/VIT2-322,%20Tail%20516-Fuse%20511%20and%20516-Wing?csf=1&web=1&e=esK7Td 

During TO1 STALKER FAT, VXE 511 (with VXE 516 Center Wing) experienced an abruptly aborted takeoff with all four motors cutting at ~6” above the stand. The vehicle fell back onto the stand, knocking the stand over and causing minor cosmetic damage to the fuselage composites around the payload bay opening. In subsequent inspection, it was noted that the VTOL power connector would not fully engage due to a solder blob on the pins.  

8D #24 - CW to HLB AS150 Connection Issues.pptx

## Corrective Action

- Incomplete connector mate
- https://jenaero.atlassian.net/browse/VA-82
- https://jenaero.atlassian.net/browse/VA-365
- https://jenaero.atlassian.net/browse/VA-163
- https://jenaero.atlassian.net/browse/VA-162
- https://jenaero.atlassian.net/browse/ENG-2226
- https://jenaero.atlassian.net/browse/VA-468
- https://jenaero.atlassian.net/browse/VA-164
- https://jenaero.atlassian.net/browse/VA-469
- https://jenaero.atlassian.net/browse/VA-95
- https://jenaero.atlassian.net/browse/VA-456
- High resistance contacts
- https://jenaero.atlassian.net/browse/VA-553
- https://jenaero.atlassian.net/browse/VA-573 https://jenaero.atlassian.net/browse/VXEP-386
- https://jenaero.atlassian.net/browse/VA-93
- https://jenaero.atlassian.net/browse/SMU-70

## Plan

https://jenaero.atlassian.net/browse/VA-1983 
Need to assign: https://jenaero.atlassian.net/browse/VA-501  (Reporting)

## Issue Status

Complete on 2 of 3 outstanding causes.
Working CA (see below) on remaining 2.

## Root Cause

511+516-investigation report.pptx
8D #24 - CW to HLB AS150 Connection Issues.pptx
Multiple potential causes:
- Incomplete mate of connector
- Quality issue.  Excess glue from sealing of battery prevents full engagement of the VTOL power connector, leading to increased internal resistance under high power load.  As a result, the connector pins overheat, potentially leading to solder flow and failure.
- Lack of latching connector, and fully mated indicator.
- If the connector O-ring not lubricated, the connector can seem fully mated without being so.
- High resistance contacts. 
- Over-current on flight prior to incident due to poor quality plating in commercial contact resulted in solder-ball in connector which prevented full mating in the incident flight. Contact measured 178uohms. Which is very close to the maximum acceptable limit of 180 uohms. A high resistance contact like this combined with an incomplete mate would lead to even higher resistance, which would then heat the contact up enough to melt the solder and disconnect the connection.

## Comments (9)

### Allen Gardner, 2023-08-25

@Sam Miller Who is the best person to itemize all the corrective actions tasks?

### Matt Philley, 2023-08-28

https://jenaero.atlassian.net/browse/VA-82 
was the ticket created to track all the associated Corrective Actions for this topic.

### Cameron Chapman, 2023-09-07

I think this issue will require a high priority SB and/or AD (the definitions seem to overlap). FYI @Dana Holley .
We still need to finalize specifics, but the the actions are summarized in slide 3 of this ppt. https://jenaero.sharepoint.com/:p:/s/ContinuousImprovement/EUP5VvyBE09Mte_5wSGWcHUBXCvOKny6UYF6mzoYLSLRWw?e=s3wCj5 . I will create a task to create these documents. 

Latest EA definitions from Dana 
[embedded file]

### Matt Philley, 2023-09-07

Some misc notes from our meeting…
SB/AD make sure they include:
- Batteries: check for squeeze out and lubrication. Rework as needed.
- Aircraft: check for solder reflow and apply decal. If solder reflow… (need to determine, but probably RMA centerwing)
- Also, should place production order for 10? 20? extra dual current sense harnesses NOW so we build up some extra anticipating this.

### Cameron Chapman, 2023-09-07

New finding. One of the 511 flights does seem to have much higher current and power than normal. More analysis needed, but this may indicate the cause was more environmental than the connector not being plugged in far enough (both could still contribute). 
[embedded file]

### Matt Philley, 2023-09-11

Added link to https://jenaero.atlassian.net/browse/VA-456 which is the Engineering Change related to the label for the AS150 connector on the Dual Current Sense Assy

### Cameron Chapman, 2023-11-09

@Greg Fryer @Former user the 516 CW seems ready to return to repair and RMA. Do we need customer approval and/or TPTR closure before performing those actions?  FYI @Sean Odell

### Greg Fryer, 2023-11-10

@Cameron Chapman I think we’ll need to reach out to Steve A. to ask for direction on shipment. I would go ahead and send the CW back into the RMA flow, they just won’t authorize us to ship it and @Sean Odell may have to sit on it. But that’s better than it sitting loose in Engineering.

### Sean Odell, 2023-11-13

@Greg Fryer @Cameron Chapman I can store the wing in the RMA area. No problem with me.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20230907-150453.png | image | 392 | 2023-09-07 | listed only |
| image-20230907-221852.png | image | 98 | 2023-09-07 | listed only |
