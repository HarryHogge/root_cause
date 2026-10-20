# VA-2521: Revised BOM for 111-105025 to new PN: 2122628-01

- **Issue type:** Engineering Change
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-03-06
- **Updated:** 2025-11-26
- **Resolved:** 2025-11-26
- **Reporter:** Tobi Ogunro
- **Assignee:** Trevor Gronner
- **Creator:** Tobi Ogunro
- **Parent:** VA-2455 Mod Payload A-Kit "Gen 2" (originally "long term fixes")
- **Epic Link:** VA-2455
- **Production Stakeholder:** Trevor Gronner
- **Engineering Change Level:** Level 1 - Scope of change is clear but there is a choice of approaches
- **Link to Engineering Change Notice (ECN):** ECN #242 2122628-01 GEN 2 MOD PAYLOAD.xlsx

## Description

Reason for Change:  Screws often would fall out of connector in the field when operators were uninstalling harness, making them easy to lose.
Description of Change:  Replace screws with alternatives that have retention clip so screws are kept captive in connector/cannot be lost. New part number for this harness so it is exceedingly clear whether a customer has an old REV or new REV harness, and an update to the NHA to call out the new part number.
Affected Item(s):   
Top level Payload Mount Assy: 111-105201
Harness with hardware change: 111-105025-D which is being replaced with 2122628-B (REV A was released back in March, found a few typos that I rolled into REV B today).
Revisioning --  See screenshot below:
[embedded: image-20251124-221214.png]


Part number 111-105025 is being replaced with new harness 2122628-01. Additionally, BOM (NHA) 111-105201 should be updated to call out new harness part number 2122628-01.
**Action Items:**

- Update/create new Part Number:

Replace 111-105025 with a new part number (2122628-01) to reflect the required changes.- Revise Note #7 in 2122628-01:

Update the note to state:
"USE ITEMS 21 AND 22 INSTEAD OF HARDWARE INCLUDED WITH CONNECTOR. INVERT ORIENTATION OF INCLUDED RETAINING CLIPS BEFORE INSTALLING BOLTS AND WASHERS. THE CIRCULAR HOLE MUST BE ON THE PLUG SIDE OF THE CONNECTOR WITH THE SQUARE HOLE ON THE CABLE SIDE."- Update BOM 111-105201 (NHA):

Modify item #3 so that it references the new part number instead of 111-105025. **Deliverables:**

Updated Note #7Modified BOM 111-105201 referencing the new part number [ME-REVIEW] [embedded: image-20250311-192517.png]

## Issue Status

CCB REVIEW

| Item | Old Part Number | New Part Number | Description | Reason for Change |
| 1 | 111-105025 | 2122628-01 | Revised MOD Payload Hardware Assembly | Replace incorrect BOM references with updated configuration |
| 2 | Items 21 & 22 | 2119692-01 | Spare Bolt Kit, MOD Payload Harness Connector | Replace individual hardware with retrofit bolt kit |
| 3 | 111-105025 (Note #7) | — | Updated Installation Instruction (within BOM) | Clarifies use of retrofit bolt kit instead of default HW |
| 4 | 111-105201 (Item #3) | 2122628-01 | Reference Update in Parent Assembly | Reflects new part number replacing 111-105025 |

## Comments (19)

### Trevor Gronner, 2025-03-06

@Nina Menon @Luca Lauritzen FYSA the Mod Payload harness is being updated to capture a change that was an issue with the old Gen 1 Mod Payload A Kit. It is a minor change in hardware and reorienting the retaining clips on the side of the backshell.

### Nina Menon, 2025-03-11

@Brendan Palmer @Matt Philley changes to the mod payload harness which affects payload mount assy 111-105201

### Matt Philley, 2025-03-11

@Nina Menon is this reflected on the Cartoon and will this need a new practice build/FAI?

### Tobi Ogunro, 2025-03-11

@Matt Philley I already updated the Cartoon.

### Brendan Palmer, 2025-03-12

@Gerrit Sperling the note on the 2122628 drawing has the orientation of the retaining clips backwards. It should read:
”INVERT ORIENTATION OF INCLUDED RETAINING CLIPS BEFORE INSTALLING BOLTS AND WASHERS. THE CIRCULAR HOLE MUST BE ON THE PLUG SIDE OF THE CONNECTOR WITH THE SQUARE HOLE ON THE CABLE SIDE.”
Orienting the square hole on the cable side is what will reduce the likelihood of the fasteners falling out of the connector.
@Tobi Ogunro @Trevor Gronner FYSA

### Tobi Ogunro, 2025-03-13

@Gerrit Sperling Please don’t forget to copy and paste @Brendan Palmer note into the drawing.

### Gerrit Sperling, 2025-03-13

@Tobi Ogunro @Brendan Palmer 
[embedded: image-20250313-225643.png]
NOTE 7 Updated

### Tobi Ogunro, 2025-03-24

@Matt Weber Can we get these 2 tasks pushed to release.

### Greg Fryer, 2025-04-10

@Tobi Ogunro @Matt Weber Please fix drawing meta data (PN field is wrong). Please move to actual release state, then send ticket back.

### Tobi Ogunro, 2025-04-10

@Greg Fryer This is the PN that needs to be fixed? 
[embedded: image-20250410-183656.png]

### Greg Fryer, 2025-06-04

@Tobi Ogunro Let’s discuss when you have a sec. Part of the issue is also that the change is not defined here, e.g. “PN X from Rev B to Rev C”

### Trevor Gronner, 2025-11-07

@Tobi Ogunro The drawing for 111-105201 received a BOM update to call out the new harness but it is still in Edit. It was never reviewed and pushed to Release. Do you mind helping to get this through the Release process?

### Thomas McMillan, 2025-11-07

@Trevor Gronner I also noticed that the BOM for 111-105025/2122628 was never updated to change items 21 and 22 into new part number 2119692-01 (Spare Bolt Kit, MOD PAYLOAD Harness Connector).  Not critical, and right now its not a non-conformity (we still use items 21 and 22), just an observation.

### Trevor Gronner, 2025-11-07

@Thomas McMillan That was a correction I had them make. That bolt kit includes 4 bolts and 8 washers which is too many for this assembly. We also don’t want to kit them just to break them back apart in production. Good catch, but we want to stick with the bolts/washers individually called out.

### Jack Waeschle, 2025-11-24

@Trevor Gronner looking for clarification on pending actions for this ticket.

### Jack Waeschle, 2025-11-24

Revised wording on this ticket so it is easy to follow changes that occurred. Additionally, created an ECN: ECN #242 2122628-01 GEN 2 MOD PAYLOAD.xlsx

### Jack Waeschle, 2025-11-24

Drawings revised and in pending CCB state, @Matt Weber please release when you can. Otherwise @Alfredo Macias will see this at CCB this week. Moving ticket to retro CCB

### Greg Fryer, 2025-11-24

@Alfredo Macias Given the need to sort out the NCR and that it’s L1, I have gone ahead and done the CCB transition to full release of both 2122628 and 111-105201
@Jack Waeschle Thank you.
@Mike DeJesus FYI, should be good to close NCR if not already.

### Trevor Gronner, 2025-11-26

@Thomas McMillan @Noah Chavez @Brendan Palmer FYSA engineering updated the drawing for 111-105201 (Mod Payload Mount to call out the correct harness - 2122628 instead of 111-105025). Hopefully this will allow us to handle the open NCRs/inspection calls that flagged this issue. Thanks!

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20250311-192517.png | image | 300 | 2025-03-11 | listed only |
| image-20250313-225643.png | image | 4 | 2025-03-13 | listed only |
| image-20250410-183656.png | image | 11 | 2025-04-10 | listed only |
| image-20251124-221214.png | image | 40 | 2025-11-24 | listed only |
