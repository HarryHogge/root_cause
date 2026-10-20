# VXEP-417: Review and provide overall shielding requirements, goals, location and technique of shield terminations, etc. wrt our upcoming MAGNSS builds

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-05-22
- **Updated:** 2025-02-17
- **Resolved:** 2025-02-17
- **Reporter:** Cameron Chapman
- **Assignee:** Connor Peebles
- **Creator:** Cameron Chapman
- **Labels:** EE-Active
- **Parent:** VXEP-183 Establish aircraft grounding, bonding, shielding, etc. status and roadmap.
- **Epic Status:** To Do
- **Epic Color:** ghx-label-3
- **Issue color:** yellow
- **Other Stakeholder (as required):** Garrett O'Neill

## Issue Status

I think we could benefit from reviewing and summarizing the overall shielding requirements, goals, location and technique of shield terminations, etc. wrt our upcoming builds. First focus on what is the best we can do with our short timeframe and current vehicle architecture, or things that can be applied and tested to the vehicle architecture in the same timeframe (deliveries in July, need to be tested and validated earlier. Schedule here:https://jenaero.atlassian.net/wiki/spaces/PDAO/pages/83165185/Advanced+GNSS+VXE+2024). Then we can work on how do we optimize this assembly and our vehicle architecture going forward.

## Comments (4)

### Cameron Chapman, 2024-05-23

@Abel J. Markow could we make this your top EA priority?

### Cameron Chapman, 2024-06-13

@Garrett O'Neill 
Garrett bonding review[embedded file] 
Comments:
- We should create a similar diagram for low side signal and power connections (in addition to shields). Color code on the same diagram?
- Does the 19P ODU fit mated in MB config?
- If we are already making a branch cable V2, wouldn't it be easier to connect reference point to avionics box via the existing branch cable to HLB cable, but adding a shield connection? This would just require a branch cable mod (already needed for MAGNSS), and not another cable.
- We would still need a new connection between HLB and Main battery. The ground isolation one is likely too high resistance (too long of a loop)

### Cameron Chapman, 2024-06-20

6/20 Discussion @Abel J. Markow and @Garrett O'Neill 
Need list of issues from Abel.
- Implementation order and scope.
- Prioritized
- MAGNSS plan
- Bond  batteries together and to avionics box? Need to test.
- Fix CSB isolation? Need to open center wing and replace PCB. Probably needs more software changes. MANGSS reworks may be the best opportunity
- Not yet prioritized and scoped
- Ethernet magnetics
- Bond aircraft structure.
- Review BMS/requirements. -Tag up with Ann Arbor. Abel Already on the chat.

### Connor Peebles, 2025-02-17

Review of shielding and return architecture completed as part of overall system of Advanced Navigation.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [VXE30 + MAGNSS Shield Architecture 1.pdf](attachments/20979_VXE30%20+%20MAGNSS%20Shield%20Architecture%201.pdf.md) | pdf | 2422 | 2024-06-13 | converted |
