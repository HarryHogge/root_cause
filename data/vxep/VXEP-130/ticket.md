# VXEP-130: 8D #21 - VTOL AP Interface Board Conformal Coat Investigation

- **Issue type:** Improvement
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Lowest
- **Created:** 2023-08-09
- **Updated:** 2026-06-01
- **Resolved:** 2026-06-01
- **Reporter:** Matt Philley
- **Creator:** Matt Philley
- **Labels:** 8-28-Sprint, Electronics_Drafting, valid
- **Parent:** VA-642 VTOL AP Conformal Coat process investigation
- **Links:** relates to VXEP-41 (TPTR-74 VXE 510: (VTOL AP WD) Consolidated Watch Dog tracking); relates to VXEP-15 (TPTR-75 Conformal Coating Issues); is blocked by VA-642 (VTOL AP Conformal Coat process investigation)
- **Epic Link:** VA-642
- **Sprint:** VXE-2 Greg's Team 9-17
- **Estimated Finish Date:** 2023-08-29

## Description

Updating this Jira to make it more clear it is assocaited with the VTOL AP Conformal Coat Investigation and to begin linking Corrective Actions.
8D Link: 8D #21 VTOL AP Board Assy Conformal Coat Intrusion.pptx
Customer Complaint: TPTR-75
Original JIRA: https://jenaero.atlassian.net/browse/ENG-2183 
Background:
During investigation of AC 510 it was found we have been adding RTV(?) to seal the bottom of the VTOL AP Interface board in order to protect the connectors on the opposite side from conformal coat intrusion. That sealing step does not appear to be captured on any drawing, BOM, or procedure even though it is critical to getting a successful product.

## Comments (16)

### Matt Philley, 2023-08-09

@Greg Fryer @Cameron Chapman @Desiray Johnston @Kelly J Furlong @Trevor Gronner @Marc Richardson FYI one corrective action for our AC-510 investigation where we found conformal coating contaminating a connector. More details to come, but wanted to get this on the books.
@Sam Miller FYI

### Connor Peebles, 2023-08-21

[embedded: image-20230821-165044.png]
[embedded: image-20230821-165110.png]
This board Assy drawing & conformal coating information was updated mid July. I think this is sufficient information to cover this task. LMK what you think @Matt Philley @Cameron Chapman

### Cameron Chapman, 2023-08-21

Looks good. Has this change been released and CCBd. Please link eng change to this project either way.

### Connor Peebles, 2023-08-21

@Cameron Chapman Right that is a change that I’m working into my process right now. (we used to CCB after receiving first articles but will now CCB as soon as the documents are updated). 
I’ll get that done for this board: [ENG-1054] Establish ECN for 1901P01B w/ CC - Jira (atlassian.net)

### Cameron Chapman, 2023-08-21

@Connor Peebles thank you. Linking an issue means adding to linked issues field above. That way the link goes both ways, and doesn’t get buried in comments.  I have done that for this one.

### Matt Philley, 2023-08-23

@Connor Peebles @Cameron Chapman sorry if yall are getting blasted with a buncha notifications, but I am trying to clean this up with this being the parent Jira for the conformal coat investigation with sub-tasks for the corrective actions. 
Also adding reference to the Customer Complaint TPTR-75. This is also linked on the PTR Summary spreadsheet.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent

### Greg Fryer, 2023-10-05

@Cameron Chapman I moved this to VXEP, so it can have proper child tasks.

### Greg Fryer, 2023-10-05

@Cameron Chapman I also reassigned this to you, per our standard practice.

### Christa Meck, 2025-03-18

I was working on some data management when I came across this one.  
@Cameron Chapman and/or @Matt Philley Do we still need this one from 2023?  It’s due date was 8/29/2023.

### Cameron Chapman, 2025-03-19

@Christa Meck still valid.

### Christa Meck, 2025-03-20

@Josh Burrell Looks like this might need some help from your team.

### Camron Richardson, 2025-03-20

@Christa Meck @Matt Philley @Cameron Chapman Is it RTV or is it solder mask for protecting connectors when conformal coating? And doesnt the manufacture conformal coat the INT boards now?

### Cameron Chapman, 2025-03-20

@Camron Richardson please note lowest priority. Please do not work such issues without checking with drafting team (we have much higher priorities)

### Josh Burrell, 2025-03-20

@Christa Meck Not sure where or how we fit into this but we’ll be on standby for any updates we need to make.

### Christa Meck, 2026-06-01

1901P01B is VXE AP Interface board in Odoo.  It is purchased from SP MFG PTE.
The initial complaint in this work item is that the RTV over one component is not listed on any BOM, procedure, etc.  That still appears to be true.  However, it looks like there may have been a switch to have the manufacturer conformal coating the boards now.
There are no otner Jira work items for this part number except for new construction on new aircraft.  
No open NCRs for 1901P01B except for some missing items for SB40 which is a new aircraft at this time.
I am marking this one Done.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [AC 510 VTOL AP Board Investigation - MP 23.08.09.pptx](attachments/15767_AC%20510%20VTOL%20AP%20Board%20Investigation%20-%20MP%2023.08.09.pptx.md) | pptx | 7279 | 2023-08-09 | converted |
| image-20230821-165044.png | image | 288 | 2023-08-21 | listed only |
| image-20230821-165110.png | image | 21 | 2023-08-21 | listed only |
