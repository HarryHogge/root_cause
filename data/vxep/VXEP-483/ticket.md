# VXEP-483: Remove LM Stickers from all VXE30-system Transit Cases

- **Issue type:** Major Project
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2023-04-21
- **Updated:** 2025-05-05
- **Resolved:** 2025-05-05
- **Due:** 2023-03-31
- **Reporter:** Scott Stuckey
- **Assignee:** Greg Fryer
- **Creator:** Scott Stuckey
- **Labels:** 8-28-Sprint, Misc.
- **Links:** relates to ENG-1006 (FSK Transit Case is missing LM sticker on BOM /Drawing); is blocked by VA-559 (Review all cases in vault to verify all LM labels or p/n lines are removed.); is blocked by VA-560 (Review all production work instructions to verify all released changes are in place to eliminate LM/Stalker labels)
- **Production Stakeholder:** Matt Philley
- **Supply Chain Stakeholder:** Victor Vandor
- **Other Stakeholder (as required):** Kyle England

## Description

Task 1 - LM Label Remove/Replace
 Steps: 
- Remove item 100-105960 (LM TRANSIT CASE LABEL) and 100-106853 (LM BUISNESS CARD).
- Replace with  Edge Autonomy label PN: 107-111697
- Get label layout approval from Joshua Stinson then release Edge Autonomy label PN: 107-111697.
- Release each of the updated transit case BOMs
- CCB to push into production

BOMs Effected: 
- SGCS1: 965-3-14-6000 - updated,  Needs Release
- SGCS2: 96X-3-14-5200 - updated,  Needs Release
- SGCS3-1: 96X-3-14-5410 - updated,  Needs Release
- SGCS3-2: 96X-3-14-5420 - updated,  Needs Release
- SGCS3-3: 96X-3-14-5430 - updated,  Needs Release
- FSK: 107-102845 - updated,  Needs Release
- Main Batt Kit: 107-102850 - updated,  Needs Release
- Hybrid Batt Kit: 114-107055 - updated,  Needs Release
- MOD Payload: 111-105328 - updated,  Needs Release
- Hill Box Kit:
- VXE30 Spares Kit:
- VXE30 TCI Spares Kit:

Task 2 - Update Edge Case Label - remove “Stalker”
 Steps: 
- Update released Edge Case labels from “Stalker VXE30” to just have “VXE30”
- Release updated label file
- CCB to push change to production floor

Label PN to update: 
- MOD Payload: 111-105572 - updated, Needs Release
- VXE30 CASE 1of 2: 107-103436 - updated, Needs Release
- VXE30 CASE 2 of 2: 107-103438 - updated, Needs Release

## Comments (14)

### Cameron Chapman, 2023-04-27

@Former user to support

### Matt Philley, 2023-04-27

@Desiray Johnston @Kyle England @Nina Menon FYI

### Nina Menon, 2023-04-28

@Jeremy Roberson FYI

### Former user, 2023-04-28

Reviewed and updated Task 1 list. Cross checked with the Vault where used list for the sticker.

### Matt Philley, 2023-05-01

For awareness there are some orders running through the shop right now that are NOT going to LM, so those stickers will need to be removed. The direction to Production and QA is to follow the BOMs that are currently released and John Tucker will remove LM labels as-needed during or after SCO. 
This will hopefully help keep the cut-in for this change from getting too complicated while Engineering is working on this project.

### Scott Stuckey, 2023-05-22

@Sam Miller  Please assign this ticket back to me when you put a 1(800)-XXX-XXXX for the Edge Transit Case Label in the comments. Thanks

### Matt Philley, 2023-05-23

@Scott Stuckey once we are ready to release all these updates can you ping me so I can work with Final Assy to tag cases with all these new labels and I can get pictures for QA in preparation for the rollout to Production?

### Matt Philley, 2023-06-05

@Scott Stuckey are we supposed to be using the new transit case labels without “STALKER” on them yet? it looks like the label templates are changed in the vault, but still not released yet.
Fuse labels - 107-103436
Wing labels - 107-103438

### Matt Philley, 2023-06-27

@Scott Stuckey checking up on this. Are we supposed to be using the “Non-Stalker” stickers…?

### Sam Miller, 2023-07-02

Hi all, @Sean Odell , @Pat Wells have created a new support number for Edge: 1-855-334-3457 (1-855-EDGE-HLP).  Going forward, we will want this contact number on all cases that are delivered from Edge directly to end customers, but NOT on LM deliverables - they’ll want the LM support number for their deliverables.  To keep consistency from production, maybe we add them at the time of delivery/shipment?  For simplicity, I suggest that we remove the laminated business card from SGCS1 and just go with the simple vinyl support stickers on the outside of the case.

### Matt Philley, 2023-07-21

@Scott Stuckey @Greg Fryer following-up on this one again. Are we supposed to be using stickers without the “Stalker” branding now? 
- 107-103438 - VXE30 Wing Case Stickers. Doc is in Change in Process. STALKER removed, but LM part number is still present
- 107-103460 - VXE30 Fuselage Case Stickers. Doc is in Change in Process. STALKER removed, but LM part number is still present

I dont think this change ever went thru CCB (since docs are still not released).
@Marc Richardson  @Desiray Johnston  FYSA Production appears to be using the new Wing case stickers, but not the Fuse case stickers… so trying to get clarity on what the direction is, so we know what to inspect to. These are TIQUILA aircraft and USASOC aircraft in the shop now if that matters one way or another. 

[embedded: IMG_9938.JPG]

### Matt Philley, 2023-08-03

I notified Final Assy last week to at least make sure they are pulling the latest template, so now vehicle cases as of last week were using all labels WITHOUT Stalker, however they all still have the Lockheed PN on the label, which seems like something we would not want on the cases going to USASOC.
Production and QA will continue as-is until further direction.

### Sam Miller, 2023-08-03

For consistency on ALL future deliveries, I recommend updating all case labels to list Edge part numbers only as the MFG part number.  LM can then add a second LM part number label for stuff that they are reselling to their customers.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IMG_9938.JPG | image | 3144 | 2023-07-21 | listed only |
