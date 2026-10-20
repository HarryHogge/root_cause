# VXEP-523: Old. B40 Wing Utility Dropper Requirements/Scope

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-08-02
- **Updated:** 2026-02-07
- **Resolved:** 2025-12-09
- **Reporter:** Grant Goodman
- **Assignee:** Matt Philley
- **Creator:** Grant Goodman
- **Labels:** EndOfLife
- **Parent:** VXEP-337 Create, Test, and Release VXE30 Standard Config Wing Utility Drop
- **Links:** relates to VA-1572 (0716P01 Fuselage Drop Payload PCB Improvements); relates to ENG-2174 (Document EA portion of fuselage drop payload. Add to vault. ); relates to VA-1580 (Investigate Edge payload drop firmware, determine if we can modify to allow one drop at a time.); relates to VA-1722 (BMS & Hatchet integration to VXE30 Standard, including “High Payload (lower energy) battery”); relates to VA-1495 (Generate VXE30Std - Wing Utility Drop - Block Diagram (Concept))
- **Epic Status:** To Do
- **Epic Color:** ghx-label-10
- **Issue color:** blue
- **Leadership Stakeholder:** Greg Fryer
- **Product/Tech Owner:** Tom Westrich
- **Program (Marquee):** On-Board Heavy Fuel
- **Job Number:** J100130 - VXE Fuel Cell & Heavy Fuel Development

## Description

Concepts: https://jenaero.sharepoint.com/:u:/s/IRAD/ETDeR7eIsxVNtlj7YhPUI7sB9k7Cc32cPyy1FRLyuTgSSQ?email=ggoodman%40edgeautonomy.io&e=uoJ2Nb 
We need to update the drop payload boards to deal with obsolete parts. Greg recommended outsourcing to Treetown (design house AA uses) to limit our work. Seems like a good opportunity to add some easy improvements. 
The idea is to reproduce current functionality, but also set us up for future improvements like CAN commanding of dropper and servos, sensor inputs, better connectors, etc
 
- Define scope.
- Concept and requirements outline. 
- Features 3 positions to be commanded.  Current software has web interface with just a drop button. Automatically returns to load. 
- Safety: Slews servo to a point where it cannot be manually be released by hand. To exit safety, operator commands to load. (not currently an option). Ensure default/startup commanding defaults to safety.
- Load/Armed: Able to load dropped item or ready to mechanically drop. Currently 800PWM. This should be default position for this mode.
- Drop: Drops projectile. Returns to load after dropping. Currently 2200 PWM. This should be default position for this mode.
- Sensor integration: TBD. Need requirements. 
- Need WD. Send list of sensors to treetown. Have them scope the integration. Want to process on board. https://jenaero.atlassian.net/browse/VXEP-634 P/N: 100-117037-01
- @Scott Stuckey or @Geoffrey Smith to list sensor PNs and what we want them to do.
- GCS Software. Probably internal. 
- Automatically transition modes based on stage of flight.
- GCS Dropper board to the XCOMM @John Clark
- Board Firmware. TBD. 
- Handle all of the above.
- Board hardware
- CAN connection. Already HW on the board. Need to check if FW needs updates to use.
- May want to add ethernet connectivity at some point to take this off the flight critical bus. Could be next version.
- Connectors:
- @Scott Stuckey to define quick concepts of connector placement and angle.
- For now keep form as is.
- Board shape and features. 
- 4 mounting holes on the corners. Same board outline.
- Decide SOW for us and tree town.
- Plan and execute.

## Plan

- Asked @Gary Angelus to submit PR and PO to Tree town. @Perry Richardson
- Define need date. Need to update based on @Matt Philley's estimates in chat. 
- current forecast is Qty 30 sets in the first 3 months of production and we only have Qty 17 PCBs "in inventory", so if all goes to plan and we begin production next month we would ideally like to have more PCBs on hand at the beginning of January-ish.

## Issue Status

Sharepoint VXE Wing Drop (& Munitions)
Shared files with tree town: Drop payload
Tree town SOW draft Tree town dropper PCB SOW-new template.docx

## Comments (11)

### Grant Goodman, 2024-08-07

16x of 0716P01 PCBs in Engineering

### Cameron Chapman, 2024-09-14

@Grant Goodman @Jeremy White do you have any ICDs for BMS /Hatchet? I want to determine if this update of the wing drop board should have any features to enable BMS connection. 
https://jenaero.atlassian.net/browse/VA-1722

### Cameron Chapman, 2024-09-14

@Tom Westrich @Stephen Peters who is your contact at treetown? We would like to have them quote this project soon.

### Tom Westrich, 2024-09-14

@Cameron Chapman , Mike.Gorski@treetowntech.com

### Jeremy White, 2024-09-16

@Cameron Chapman  We don’t have the IMS for the BMS yet as they are finalizing it now. This is a new version of the BMS (SDP- Small Drone Platform). We have a meeting with them today at 2pm EST time and can ask for a status.

It is highly unlikely that we will get an ICD for the Hatchet since the aircraft won’t interact with the munition. All commands/communication with the hatchet and the backpack are through the BMS.

@Grant Goodman

### Matt Philley, 2024-09-16

@Grant Goodman @Cameron Chapman added this to our Utility Dropper action list since it will prevent us from completing Practice Builds and FAIs until it is resolved.
Will part of this project be to keep the same form factor and connectors on the board? If not, then this could also trigger redesigns of the126-117433-01 Drop Payload Board/Harness Assy (harnesses and enclosure). 
[embedded image-20240916-142143.png]

### Cameron Chapman, 2024-09-16

@Matt Philley yes, initial tree town ask will be for the same form factor. I hope to complete this RFQ this week.

### Cameron Chapman, 2024-11-06

@David Grosher our current plan for the drop payload board is: 
- Current: serial to the drop payload board
- Future: CAN, because the board already has CAN. Given that our plan has been CAN for flight critical items and ethernet for others, should this be an ethernet interface?

### Matt Philley, 2024-12-16

General update since status is mostly being tracked in the “Edge + Tree Town Chat” Teams chat
- Luke Paul from Tree Town has completed the initial design and doc package for the 2119594-01 replacement drop payload board PCB.
- This is being called a “Preliminary Release” for quoting and DFM feedback from board house (Sierra).
- Edge will send this out to Sierra for quote and feedback then initiate FAIs.
- Files kept in the sharepoint link above
- Still on track for roughly placing production orders for the replacement boards in Jan

### Matt Philley, 2025-01-30

General Update from “Edge + Tree Town Chat VXE Version” Teams chat
- “Final” (as of 1/23/25) release files are here 2119594-01 FINAL RELEASE 1-23-25.zip
- Files were sent to Sierra for quote/order and feedback has been incorporated twice(?)
- Open Order Link - EXPENSE Est. first week of Feb(?)

### Christa Meck, 2025-02-28

Due Date of 2025-01-01 removed per information in Mission Control spreadsheet.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240916-142143.png | image | 296 | 2024-09-16 | listed only |
