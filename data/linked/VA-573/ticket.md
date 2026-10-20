# VA-573: Poor Quality/higher impedance plating on AS150 power contacts - Containment and Corrective Action

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-09-20
- **Updated:** 2025-08-12
- **Resolved:** 2025-05-28
- **Reporter:** Greg Fryer
- **Assignee:** Cameron Chapman
- **Creator:** Greg Fryer
- **Labels:** Production-Priority
- **Links:** blocks VXEP-12 (TPTR-87 VXE 511 VTOL Connector Issues 516 CW. Contains Main connector/contact C/CAs); relates to VXEP-385 (New Connectors and Contacts, Overall Requirements Review); relates to VA-774 (Poor quality power contacts seem to originate from the same source. Need to confirm.); relates to VA-553 (Review and improve receiving inspections for AS150 contacts); relates to VXEP-192 (107-102264 Dual Current Sense harness needs testing values defined); relates to VA-613 (Ensure all AMASS contacts and connectors are only ordered from authorized suppliers. Not amazon.); relates to VXEP-101 (VXE-487 488CW Damage to Center Wing power connector -Motors stopped at 90ft during VTOL landing); causes SP-206 (Improve Power Connector, Contacts, and Signal Connectors); causes VA-553 (Review and improve receiving inspections for AS150 contacts); relates to VXEP-386 (Develop Replacement for AS150 Connections); relates to VXEP-432 (Define Lifetime Fail Criteria for AS150 Anti spark connector resistance); relates to VXEP-639 (VXE 515- HLB Unexpected Voltage fluctuation. Aircraft flown multiple times after, leading to damage); relates to VXEP-646 (VXE 392 crash on VTOL launch); relates to VXEP-761 (VXE 557 Smoking Smell from Fuselage after connecting main battery)

## Description

Epic group of tasks related to containing one probable cause of VTOL connection incidents.
Files Anti-spark pin issue

Plan 6/21
Actions
- Schedule meeting with AA ASAP to coordinate efforts.
- Confirm plan.
- Get power switch and connectors happening ASAP
- Finalize plan details.
- Make subtasks, link, and track the following items.
- Organize and clean up duplication from previous tasks.
- Consider unlinking or hiding complete subtasks (ask Carl or another Jira expert)

Short term
- Per Pat W, he was expecting a lot of questions about contact cleaning when latest document was released, but received very little. This leads him to think not many read it. Less visible with rev update to previous document compared to a new document release.
- Release new document to make the importance of this more clear. -Pat to coordinate and lead?
- https://jenaero.atlassian.net/browse/VA-1983  Initial impressions seem like yes, but we need to collect more data and verify.  Quality or production may support.
- This could help prioritize actions below.

Soon After Options
Determine and implement long term fleet plan.
- Replace AS150 contacts. Similar connection method as current.
- Details: Need anti-spark or power switch (ideally in battery).
- Could activate via existing CAN connection or push button on the HLB. Don't want latch. Probably want disable button as well before demating.
- See connector replacement JIRA project. Want/Need features like rainproof, latching.
- Pros:
- Permanent fix (hopefully).
- Best option for customer after replacement.
- Cons:
- Requires replacing all HLBs and center wing power harness (EA rework).
- Large engineering project(s). Need to scope manpower and schedule.
- Not a lot of time to qualify long term use of replacement contacts. (Low risk if we select from a professional contact company, who may have such data).
- Good chance we will have to UN recertify battery assemblies. Small chance we might not (pack is certified, we are just adding disconnect switches)

- Improve resistance test procedure, deliver kits and training to all customers.
- Details: Improve test cables to ensure consistent results. Control measurement and pierce point.
- Pros: Probably quicker.
- Cons: Hard to get consistent results currently.
- Training will be difficult.
- Each test damages wire insulation
- Time spent on this will not be spent on the permanent solution.

- Adapter Harness to make new contacts primary disconnect. Keep AS150 contacts but never demate.

Pros: Do not have to scrap or change all center wing harnesses or batteries.
Cons:
- May not be able to fit extra connector bulk
- 2 more connectors will increase overall resistance. May create more heat.
- More weight.
- Frustrating (maybe impossible) for operators stuffing that much cable into the fuselage. May still have errors disconnecting and mating all connectors correctly?

- Others?

Recommendation
- Option 1 ASAP. Option 2 if timeline for option 1 is not acceptable and option 2 is. Avoid option 3. 
- Need to scope and prioritize. Timeline.

## Sprint

VXE-1 Electrical-8, VXE-2 Everything Else 2024-03, VXE-2 Greg's Team 9-17, VXE Product Dev & Sup 2024-07, VXE-2 Mechanical+Prod 09-Oct, VXE-2 Production, VXE Product Dev & Sup 2024-05, VXE-1 Electrical-7, VXE Prod Dev & Sup 2024-08

## Issue Status

Production test procedure and equipment ready.
Field test procedure and equipment ready.
Need guidance on service bulletin distribution. Asked.

## Comments (0)

## Attachments (0)
