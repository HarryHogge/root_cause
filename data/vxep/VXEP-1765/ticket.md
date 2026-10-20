# VXEP-1765: Fuselage Fuse Distribution Board AVBP2 Test Harness (2130896)

- **Issue type:** Minor Project
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2026-03-03
- **Updated:** 2026-07-14
- **Resolved:** 2026-07-14
- **Due:** 2026-04-30
- **Reporter:** Matthew Aguirre
- **Assignee:** Matthew Aguirre
- **Creator:** Matthew Aguirre
- **Parent:** VXEP-1762 B40 ENG Iron Bird Test Boards
- **Links:** is cloned by VXEP-1805 (Fuselage Fuse Distribution Board AVBP1 Test Harness (2135313))
- **Approvers:** Jeremy Kostel
- **Epic Link:** VXEP-1762
- **Issue color:** teal
- **Target start:** 2026-02-26
- **Target end:** 2026-03-31
- **Issue Status:** Currently at step 6 of plan. Waiting on confirmation that harness is functional.

## Description

This project is meant to design and build a test connector for AVBP2 on the Iron Bird that exits the fuse distribution board. Due to the high current that is passing through these power signal lines, this test connector will need to be a harness rather than a PCB.

## Plan

- Scope out the different signal lines feeding from the connector and the connectors PNs being used.
- Create a wire harness design on Altium.
- Touch base with William and Daniel for up-to-date standards and requirements for test harness drawings.
- Validate design with Jeremy. 
- Resolve comments left by Jeremy before construction.
- Once validated, place inventory request with BOM.
- Test the harness for the following:
- Matches pinout (continuity testing)
- Abnormally large impedances (resistance testing)
- Pass on built and verified harness to Jeremy for second review.
- Install in Iron Bird:
- Ask Jeremy, or someone familiar with Iron Bird, to show how to “turn on”.
- When Iron Bird is on, test the signal lines using the test harness and verify functionality.
- Make note of any heat, or warm spots, giving off the test harness during operation.

## Comments (6)

### Matthew Aguirre, 2026-03-09

Jeremy’s Comments:
- add net names to wires in wiring schematic.

### Matthew Aguirre, 2026-03-13

Finished rough draft of wire harness design, and put in a request for the kit to construct harness this morning.

### Matthew Aguirre, 2026-03-20

Working on higher priority tasks, harness construction is put on hold for time being.

### Matthew Aguirre, 2026-03-26

Beginning construction of test harness today. Still need to go through entire design review process, once harness is constructed.

### Matthew Aguirre, 2026-03-30

Finished constructing harness today. Performed continuity and resistance test across all pins. Verified that pinout was correct, and all connections had a resistance of ~0.3 ohms. Passed off to Jeremy to double check pinout before moving toward testing on Iron Bird B40.

### Matthew Aguirre, 2026-04-02

part number for test harness is 2130896

## Attachments (0)
