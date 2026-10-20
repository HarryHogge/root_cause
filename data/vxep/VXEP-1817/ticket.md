# VXEP-1817: Create B35/B40 Kit Configurations (2123717-01 / -02) and Define Left/Right Pylon Usage

- **Issue type:** Engineering Change
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2026-04-08
- **Updated:** 2026-06-04
- **Resolved:** 2026-06-04
- **Reporter:** Tobi Ogunro
- **Assignee:** Brendan Palmer
- **Creator:** Tobi Ogunro
- **Labels:** ReviewedAndReadyForCCB
- **Parent:** VXEP-1191 Mechanical - Wing Utility Pylon (FKA drop payload)
- **Links:** relates to VXEP-1814 (Add Left/Right Configurations for B40 Wing Utility Pylon (2123650) and Update Kit (2123717))
- **Epic Link:** VXEP-1191
- **Engineering Change Level:** Level 0 - Scope of change is obvious to assigned engineer
- **Key Stakeholder(s):** Addison Osborn, Greg Fryer, J Vo

## Description

Reason for Change: Current Wing Utility Pylon Kit configuration does not differentiate between B35 and B40 platforms and does not explicitly define left and right pylon usage.

Description of Change: Create separate kit configurations:
- 2123717-01 → B40 Wing Utility Pylon Kit
- 2123717-02 → B35 Wing Utility Pylon Kit (LRR-specific)

- Update both kit definitions to explicitly include:
- 1x 2123650-01 (Left Pylon)
- 1x 2123650-02 (Right Pylon)

Affected Item(s):  
- 2123717-01 — Wing Utility Pylon Kit (B40)
- 2123717-02 — Wing Utility Pylon Kit (B35)
- 2123650-01 — Wing Utility Pylon (Left)
- 2123650-02 — Wing Utility Pylon (Right)
- 500-2124086-01 — B40 Catalog BOM
- 500-2123975-01 — B35 Catalog BOM

Where Used:  

- B40 Aircraft — Wing Utility Pylon Kit
- B35 Aircraft (LRR) — Wing Utility Pylon Kit

What Product Line(s) is this for?  

Revisioning -- 
Current Rev: 
Proposed Rev:

| BOM | Description | Status |
| 2123717-01 | Wing Utility Pylon Kit — B40 | Released |
| 2123717-02 | Wing Utility Pylon Kit — B35 (LRR) | Released |

[embedded: image-20260414-203714.png]
[embedded: image-20260416-173240.png]

## Comments (5)

### Trevor Gronner, 2026-04-08

@Brendan Palmer @Kyle England @Greg Kalichak@Sandra Lopez @Steve Stack @Catherine Wagner @Noah Chavez FYSA, this ticket is to track different configurations of the wing utility pylon.

### Tobi Ogunro, 2026-04-14

@Sanjay Menon Let me know when we can push this to release.

### Sanjay Menon, 2026-04-14

@Tobi Ogunro Pushed to pending CCB

### Christa Meck, 2026-04-16

This Engineering Change has been reviewed using the checklist and is ready for CCB.
- 2123717 - initial production release of drawing.
- 2123650 - ECN referenced is for related Engineering Change https://jenaero.atlassian.net/browse/VXEP-1814
- 2123650-01 - onhand 0
- 2123650-02 - not in Odoo
- 2123717-01 - onhand 0
- 2123717-02 - not in Odoo
- Part number on drawing for 2123650 says 101-115866
- Part number on drawing for 2123717 says 101-117342
- Logged item on GoEngineer meeting for this since it is a generated field.
- Disposition is rework but doesn't matter cause 0 on hand.
- 2123650 is used in 2123717
- 2123717 used in [500-2124086] Stalker Block 40 Wing Utility Pylon Kit   AND   [500-2123975-01] Stalker Block 35 Wing Utility Pylon Kit
- This item is one in a series of items involving L/R pylon configurations and separating B35 from B40.  This Engineering Change is unique to the parts involved.
- No open NCRs
- No CR/CCN required.
- 500-2124086-01 - Stalker Block 40 Wing Utility Pylon Kit BOM
- 500-2123975 - Stalker Block 35 Wing Utility Pylon Kit BOM

@Tobi Ogunro has some stuff he wants to discuss

### Trevor Gronner, 2026-04-17

@Brendan Palmer I believe this is a very similar change to https://jenaero.atlassian.net/browse/VXEP-1814. Please add any implementation tasks needed that aren’t covered in that other ticket. Please move this ticket to Done when it’s fully implemented. Thanks!

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20260414-203714.png | image | 21 | 2026-04-14 | listed only |
| image-20260416-173240.png | image | 9 | 2026-04-16 | listed only |
