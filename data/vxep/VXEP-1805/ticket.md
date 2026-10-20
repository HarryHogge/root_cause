# VXEP-1805: Fuselage Fuse Distribution Board AVBP1 Test Harness (2135313)

- **Issue type:** Minor Project
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2026-04-02
- **Updated:** 2026-07-14
- **Resolved:** 2026-07-14
- **Due:** 2026-04-30
- **Reporter:** Matthew Aguirre
- **Assignee:** Matthew Aguirre
- **Creator:** Matthew Aguirre
- **Parent:** VXEP-1762 B40 ENG Iron Bird Test Boards
- **Links:** clones VXEP-1765 (Fuselage Fuse Distribution Board AVBP2 Test Harness (2130896))
- **Approvers:** Jeremy Kostel
- **Epic Link:** VXEP-1762

## Description

This project is meant to design and build a test connector for AVBP1 on the Iron Bird that exits the fuse distribution board. For simplicity sake, this will be constructed as a harness rather than PCB as originally discussed.

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

## Comments (2)

### Matthew Aguirre, 2026-04-02

starting work on harness today

### Matthew Aguirre, 2026-06-04

Finished construction, handed off to @Ben Norris for pinout check yesterday around 3pm.

## Attachments (0)
