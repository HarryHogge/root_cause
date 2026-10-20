# ENG-346: 1607P01A Improvements. XCOM / XE240 PWR COMMS BD

- **Issue type:** Minor Project
- **Status:** On Hold
- **Priority:** Medium
- **Created:** 2023-02-06
- **Updated:** 2026-10-01
- **Reporter:** Cameron Chapman
- **Assignee:** Connor Peebles
- **Creator:** Cameron Chapman
- **Parent:** XKIT-2150 Hardware & PCB Improvement Collector
- **Links:** relates to ENGPRJA-144 (1607P01A Documentation update); relates to VXEP-367 (12.8V Bus Current Limiting Issue (U5 X COM)); relates to XKIT-2046 (Integrate Mod Payload interfaces into aircraft on connector (e.g. eliminate need for MAIM)); relates to ENG-2650 (Document XCOM failure in linked JIRA issue. Record other instances or frequency of that failure type in the issue); relates to XKIT-2503 (Test 5V Enable Solutions on Xkit nose cone with production Hargrave ESC (p/n: 100-114708)); relates to XKIT-2934 (Complete Xcomm hardware modifications for 5v ESC change); relates to XKIT-2899 (Avionics box+XCOM changes for Havoc and/or Xkit); relates to VXEP-612 (SD Card Reliability Corrective Actions); relates to ENG-615 (Delete - 1607P01A Improvements); relates to VXEP-944 (VXE 614 Erratic behavior and propulsion failure led to crash ); relates to VXEP-1695 (Add JTAG debugging to future boards like XCOM with processors. ); relates to VXEP-229 (Avionics box improvement ideas); relates to AV-716 (2135413-01 - XCOMM UAP - REV A); relates to VXEP-1692 (B40/30 XCOM WDT resets ); relates to XKIT-5551 (1607P01A Improvement Ideas); relates to AV-717 (2135413-01 - XCOMM UAP - REV A01)
- **Epic Link:** XKIT-2150

## Description

Need to update this list to identify what is included in https://jenaero.atlassian.net/browse/AV-717 
Please link production improvements here.
UAP MVP Tracking here https://jenaero.atlassian.net/browse/AV-717 
This list is things not included in that. 
Documentation
- 1607P01A on vault is poorly formatted and cuts off

Harness Changes
- check the XCOM pinout for any open ports that could connect a temp sensor (with the appropriate HW and SW updates). Ex: a IO ports that could read temperature from a thermistors. This could be an easy and useful addition either for testing and/or production. Moved to https://jenaero.atlassian.net/browse/AV-717

Component changes-Could order 2 variants. One without one with changes. 
- Set servo voltage so that boost boards are no longer required. 
- If 28V servos are available this could eliminate the need for 3 DC-DC converters currently on XCOM as well (U18, U19, U25). https://jenaero.atlassian.net/browse/VA-1684
- Replace all SK56B Schottky diodes with CDBB545LR-HF, lower forward voltage drop and better thermal impedance, runs ~10-15C cooler at higher load currents https://jenaero.atlassian.net/browse/ENG-2608 Was this done for B40? UAP   https://jenaero.atlassian.net/browse/AV-717  Moved to https://jenaero.atlassian.net/browse/AV-717
- Ensure critical power supplies cannot be disabled https://jenaero.atlassian.net/browse/VXEP-944 . Review staging of converters. Timing capacitor? UAP? No.  Would need to do testing to ensure this is ok. Out of scope.
- Specify all components in industrial temperature range. Some components are rated at 85C. Having them at 125C would help carry greater payload. (Applies for both XCOMM and AP). 
- Did easier ones here https://jenaero.atlassian.net/browse/AV-717. Need to check how many are left and make subtask to track those.

Layout changes   
- Faster ethernet switch and better magnetics. 1Gps. Evaluate single pair? Abel Markow: It’s an interesting idea.  The following things are gotchas with it. ... | EE Chat | Microsoft Teams
- PPS to center wing and mod payload locations (can be split if needed). Done, but could be improved integrity.
- WD related improvements (Mainly redo power converters or move off board)
- Move to glenair payload board list PN
- Consider including Schmidt trigger circuit
- Relay to switch payload power.
- Isolated CAN tranceiver. See 28V converter board in battery.

Layout+FW Changes
- Switch from SD cards to something more reliable. Same for VTOL AP. Avbay?
- Consider RS-485 or a similar bus rather than 232 (parallel, more EMI resistant). (Likely move FC to CAN. No more need for serial?)
- Separate CAN bus for payload and flight critical? Payload stick to eth?

Layout+Harness Changes
- Incorporate branch cable features so that branch cable extra Alden is no longer required. Combine with avbay concept. Don’t want to rework fuses for UAP.
- Change blinker supplies so that they work in parallel rather than serial (requires harness changes, increases redundancy). Make CAN so they don’t need dedicated wiring? Avbay?
- Ribbon cables/flex PCBs rather than harnesses. Link to that project. Avbay?
- Evaluate Combining MAGNSS boards, especially SLA breakout, but maybe parts of GNSS board as well. UAP? Start with SLA breakout?
- Rearrange connectors to make the harnesses 1:1 (or as simple as feasible) with destinations? UAP? Probably not. Avbay?
- Less connectors in harness, move to boards.

Layout+Mech Changes
- Ensure all hot components/converters have adequate heat sinking.
- PCB mount power input connector (payload vbatt) UAP to simplify harnessing? Probably not, but would save a lot of harnessing. Does it still save harnessing with MCM on critical? 
- Add VBN schmidtt trigger circuit. https://jenaero.atlassian.net/browse/VXEP-1773
- Move payload efuse to glenair interface board to save a lot of harnessing.
- Incorporate heatsinks for power tree components, especially inductors (L1, L3 etc.).

## Comments (7)

### Greg Fryer, 2023-02-22

Needs an epic crated by @Former user for 1607P01A, and this would be a child of it.

### Cameron Chapman, 2023-12-14

| If the Green AP is replaced with a red AP, revise the X-comm to include the two headers to plug the autopilot into it.  This will remove the ribbon cable from the box which has caused more than a few major NCRs. | R. Ferguson | Electrical Mechanical Software | XCOMM will defintely take a spin for 2024 to accomodate MCM and AGNSS, but the current plan for the Unified Auto Pilot is to use an adapter board that sits exactly where the current Green AP is and that will have the 2 headers, leaving a ribbon cable. This could definetly be re-evaluated but the next XCOMM will probably be even more crowded than the current one. Cam C: Given the scope of VXE2024, there is a good change we will need to update the XCOM. In that case, removing the ribbon cable and adding headers to the XCOM would likely make the most sense. [embedded: image-20231214-195954.png] |

### Christa Meck, 2025-04-15

@Cameron Chapman Does this work from 2023 still need to be completed?

### Christa Meck, 2026-07-13

We’re past Block 25 now.

### Connor Peebles, 2026-07-15

@Christa Meck same board is currently used in B30, B35, B40

### Christa Meck, 2026-07-15

@Connor Peebles See https://jenaero.atlassian.net/browse/XKIT-5551

### Cameron Chapman, 2026-09-17

@Christa Meck Reopening. B25 was in the title of the board. These issues are still relevant to the latest one.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20231214-195954.png | image | 35 | 2023-12-14 | listed only |
