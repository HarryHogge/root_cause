# VA-1926: Replace Aluminum bolts with titanium for wing shift bracket

- **Issue type:** Engineering Change
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2024-09-05
- **Updated:** 2025-09-16
- **Resolved:** 2024-10-31
- **Reporter:** Jack Waeschle
- **Assignee:** Emalee Johnson
- **Creator:** Jack Waeschle
- **Parent:** VA-2035 Wing shift bracket Investigation and fixes
- **Links:** relates to VXEP-548 (VXE 300 CW not mounting securely and has some delamination)
- **Epic Link:** VA-2035
- **Sprint:** VXE Prod Dev & Sup 2024-08
- **Production Stakeholder:** Kyle England
- **Supply Chain Stakeholder:** Spenser Bracken
- **Engineering Change Level:** Level 1 - Scope of change is clear but there is a choice of approaches
- **Link to Engineering Change Notice (ECN):** ECN #146, 2119144 Wing Shift Bracket Mount Screws - Titanium DRAFT.xlsx

## Description

There are concerns about galling with the aluminum bolts used to secure the wing shift bracket to the fuselage. This ECN is to change these to titanium. New bolt P/N: 2119144-01
See Confluence for instructions and templates: https://jenaero.atlassian.net/l/cp/ztB58xvi.

## Comments (22)

### Jack Waeschle, 2024-09-05

@Greg Fryer @Kyle England @Greg Kalichak @Matt Philley FYSA

### Greg Fryer, 2024-09-05

@Jack Waeschle Thank you. Also kudos for filling things out including the ECN!

### Matt Philley, 2024-09-05

@Jack Waeschle are these 2119144 or 2119144-01 for the new PN? We are still not being consistent which makes things confusing.

### Jack Waeschle, 2024-09-06

@Matt Philley 2119144-01, thanks for asking for clarification. I updated the description of the ticket accordingly. Additionally, I added this new part to the inventory list and spooled @Spenser Bracken up on ordering some.

### Matt Philley, 2024-09-06

@Jack Waeschle are you tracking the incorporation of this change into the product somewhere else? It is called out in a variety of BOMs that will all need to be updated and I dont see them on your ECN yet. 
The Where-Used report shows the following:
[embedded: image-20240906-181347.png]

### Spenser Bracken, 2024-09-06

@Matt Philley I was planning to put this on the Outsourcing Status tracker once the order was placed, and then have them routed to Quality upon receipt; anything I’m missing?

### Jack Waeschle, 2024-09-06

@Matt Philley yes, I am working through that list today and will update the ECN accordingly. Yesterday I just used the Vault “where used” function and was disappointed in what it turned up as everything is in Excel BOMs in seems. Thank you for attaching that screenshot.
@Greg Fryer should I update the block 25 documentation as well with this change?

### Greg Fryer, 2024-09-06

@Jack Waeschle The production BOMs may be a better clue to where-used. And we are working on a system upgrade to better do BOM structure.
If it can be done quickly, yes update the block 25 documentation so any service we do will support. We are not selling more, finally.

### Matt Philley, 2024-09-06

@Spenser Bracken that sounds good just make sure they are marked FAI
@Catherine Wagner FYSA some new screws headed your way. I have mcmaster drawing in the vault already

### Jack Waeschle, 2024-09-06

@Greg Fryer oh my! No more block 25 sales?! I think that deserves an ice cream social of its own!

### Jack Waeschle, 2024-09-06

ECN updated, and all drawings/BOMs within that ECN have been updated. Let me know if there are more I am missing, however to the best of my knowledge this is a complete list of relevant assemblies with the FHMS 1/4-20 1.0L, Titanium screws.

### Trevor Gronner, 2024-09-12

@Emalee Johnson Do you mind helping with the last two implementation steps for this one? 
We are replacing all instances of 100-100792 with 2119144-01.
The following assemblies called out 100-100792 historically:
107-102461
127-118051-01
107-102564
JAI-XE25D-VEH
JAI-XE25D-FSKSPB
We’ll have to update any kit lists and procedures that already exist, but if any of the parts don’t have kit lists or procedures they can be skipped. Thanks for the help!

### Matt Philley, 2024-09-25

@Steve Stack @Catherine Wagner @Kevin Aban @Christopher Escobar 
FYSA not sure if yall were tracking this one, but its a change to the Fuselage Case Assy switching from Aluminum to Titanium screws for the wing shift bracket screws. This was supposed to be implemented 9/3/24 for all stuff moving forward, but doesnt look like its been cut in quite yet. 
We should be on the lookout for this.

### Emalee Johnson, 2024-09-25

@Matt Philley @Trevor Gronner @Greg Fryer 
Stockroom was told to use the remaining aluminum screws before switching over to titanium, is that the case? Brendan and I are coordinating with final this morning. 
@Kyle England @Sandra Lopez

### Trevor Gronner, 2024-09-25

@Emalee Johnson @Greg Fryer @Matt Philley We’ll follow the ECN guidance to scrap the parts in inventory and replace the items in WIP. Just for situational awareness, the placard is still called out incorrectly for the standard VXE30 Fuse Case as well so the part numbers don’t match.
@Kyle England @Sandra Lopez

### Greg Fryer, 2024-09-25

@Trevor Gronner@Tobi Ogunro Since I had to head home, is this the same placard we are trying to sort out based on not having a BOM/Drawing for it already? e.g. will the same fix resolve both issues?

### Greg Fryer, 2024-09-25

The following should be a new release, so it should go in a seperate Engineering Change to avoid delaying this one and/or cause confusion.
@Trevor Gronner @Tobi Ogunro @Jack Waeschle Just realized we neglected to do the spares check (need a better process!) on this. These are sold in a 5 pack in the catalog as a spare/replacement. Note that the PN for the 5 pack is  100-100792, the same as a single fastener:
[embedded: image-20240925-203508.png]
(This is a common error for spares in our catalog.)
So, we will need to also release a new Catalog BOM for a “Wing Shift Kit Bolt (5-Pack)”, as well as the internal drawing that identifies qty 5 of the new screw, and isntructs to bag them and label with the Catalog BOM #.
And also, figure out why it’s 5 and not 4 in the spare pack?

### Tobi Ogunro, 2024-09-25

@Greg Fryer Does the titanium “Wing Shift Kit Bolt (5-Pack)” require a new Catalog BOM #?

### Trevor Gronner, 2024-09-26

@Greg Fryer To answer your earlier question, the placard callout in the old work instruction has been corrected. Right now we have a placard for VXE30 standard and a placard for Pre-MAGNSS that both only include descriptions. The placards with part numbers for the Fuselage case have been obsoleted. If design engineering creates a BOM/drawing it can reference the released placard(s).

### Greg Fryer, 2024-10-02

@Trevor Gronner @Emalee Johnson @Brendan Palmer Just following up to see if this stalled out, or got done and just needs to be checked off? I know we’ve shuffled, just want to clean up the books!

### Emalee Johnson, 2024-10-02

@Greg Fryer  I will review remaining open actions with @Brendan Palmer  tomorrow and we will get it cleaned up. I think we should be close to buttoning this up.
@Trevor Gronner

### Brendan Palmer, 2024-10-03

@Trevor Gronner @Greg Fryer @Emalee Johnson all tasks moved to done. Moving this to done.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240906-181347.png | image | 49 | 2024-09-06 | listed only |
| image-20240925-203508.png | image | 3 | 2024-09-25 | listed only |
