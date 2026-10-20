# VXEP-1779: Build Additional CAN Logger Setups

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2026-03-18
- **Updated:** 2026-04-02
- **Resolved:** 2026-03-30
- **Reporter:** Jeremy Kostel
- **Assignee:** Matthew Aguirre
- **Creator:** Jeremy Kostel
- **Labels:** EE-Intern
- **Parent:** VXEP-1667 New EE/Intern/Specialist Projects
- **Links:** relates to ENG-3733 (2130900- WIRE HARNESS, TAIL CAN DIAGNOSTIC, FDB VERSION); relates to XKIT-5362 (Order more CAN loggers for flight test. Prepare and install for engineering assets. )
- **Epic Status:** To Do
- **Epic Color:** ghx-label-2
- **Issue color:** dark_yellow

## Description

CAN logger setups need a few items
- CAN Logger itself
- Bring to me once ready to configure
- CAN Logger harness
- PN: 2134945 (See napkin sketch added to ticket)
- CAN Logger Battery
- 2200mAh Zeee 11.1V 24.42Wh Lipo battery
- Tail Diagnostic Breakout Harness
- PN 2130900
- No drawing yet but we should have enough made already for built vehicles

## Plan

- CAN Logger
- Get total count of loggers in house, order more if needed
- deliver to J Kostel to configure and document
- CAN Logger harness
- Add connector PNs to the napkin sketch
- hand off to drafters for PN and drawing
- Ben has built this before per that napkin sketch
- fill out inventory request for harness build parts
- fill out production request for Bens time
- CAN Logger Batteries
- Order batteries listed in description
- they will need an XT60 added
- include on Ben N’s production request
- We had a charger suitable for the batteries in SLO already, likely need to order one for HSV
- Tail Diagnostic harness
- J kostel to tally how many we have currently

## Comments (10)

### Jeremy Kostel, 2026-03-18

FYSA @Cameron Chapman @Ben Norris

### Matthew Aguirre, 2026-03-19

- Handed off 3 of the CAN loggers we have in stock this morning to Jeremy and sent rough sketch w/ part numbers to Will.
- Part number associated with CANEdge3 custom harness is 2134945.
- Made PR00763 for 3 11.1V 2200mAh 3S LiPo batteries and two new battery chargers, waiting for approval.
- Completed inventory and production request for 3 x custom harnesses to be made by Ben Norris. [embedded file] [embedded file]

### Cameron Chapman, 2026-03-19

@Jeremy Kostel @Matthew Aguirre we seem to have some duplication between https://jenaero.atlassian.net/browse/XKIT-5362 . I recommend either closing one, or separating into
- Order, build, and install
- Document how to build and use.

### Thomas McMillan, 2026-03-19

Initial CAN Logger Harness drawing for review.  @Matthew Aguirre @Jeremy Kostel @Ben Norris if y’all don’t mind double checking pinout and such.  There is a linked task to create each harness as well.

[embedded file]

### Matthew Aguirre, 2026-03-20

@Matthew Aguirre Batteries and Battery Charger set to arrive by Wednesday, 2026-03-25. Ordered through Amazon so hoping it comes in sooner than the promised delivery date. Tracking through PO-26-SLO-02079.

### Matthew Aguirre, 2026-03-24

original plan was to have Ben Norris construct the 3 CANEdge3 Harnesses, but Ben thought it would be a good idea for me to get some harness construction experience. Started making the three harnesses this morning. @Jeremy Kostel is there an expected delivery date for these harnesses? Would like to get an idea of priority in comparison of my other tasks.

### Matthew Aguirre, 2026-03-24

@Matthew Aguirre Putting construction on pause to assist with Sammy with ADP testing. Left off with the 3 harnesses being half-built, should be able to finish the 3 harnesses tomorrow. If construction needs to finish today and someone else can pick up where I left off, harnesses and materials will be on my workbench in a bin labeled “9D4B” on the front.

### Matthew Aguirre, 2026-03-26

Finished constructing the 3x CANEdge3 harnesses. Verified continuity with pinout diagrams after construction. Planning to switch over to documenting configuration of CANEdge3 and, if possible, test that CANEdge3 is properly logging CAN data with custom harnesses.

### Thomas McMillan, 2026-03-30

CAN logger harness updated to use rocker switch vs toggle switch (for better flight stability). Rev A02 of drawing added to child work ticket (xkit-5386).

### Thomas McMillan, 2026-04-02

Quick drawing to document assembly/pinot for 2130900 → modified tail harness (tail plug and two ODU connectors) for CAN logging.  PDF copy of A01 attached to ticket above (ENG-3733).  Not reviewed by anyone yet as I am writing this.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [CANEdge3 Harness (2).pdf](attachments/49192_CANEdge3%20Harness%20(2).pdf.md) | pdf | 240 | 2026-03-18 | converted |
| [2134945-BOM.xlsx](attachments/49329_2134945-BOM.xlsx.md) | xlsx | 35 | 2026-03-19 | converted |
| [2134945_A01 DRAFT FOR REVIEW 3.19.2026.pdf](attachments/49447_2134945_A01%20DRAFT%20FOR%20REVIEW%203.19.2026.pdf.md) | pdf | 2993 | 2026-03-19 | converted |
| [CANEdge3 Harness Rough Sketch.pdf](attachments/49328_CANEdge3%20Harness%20Rough%20Sketch.pdf.md) | pdf | 953 | 2026-03-19 | converted |
