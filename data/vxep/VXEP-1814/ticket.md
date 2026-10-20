# VXEP-1814: Add Left/Right Configurations for B40 Wing Utility Pylon (2123650) and Update Kit (2123717)

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
- **Links:** relates to VXEP-1817 (Create B35/B40 Kit Configurations (2123717-01 / -02) and Define Left/Right Pylon Usage)
- **Epic Link:** VXEP-1191
- **Engineering Change Level:** Level 2 - Scope of change is not immediately clear
- **Key Stakeholder(s):** Addison Osborn, Greg Fryer, J Vo

## Description

This ECN introduces Left (-01) and Right (-02) configurations for the B40 Wing Utility Pylon to support current production builds.
The existing pylon PN 2123650-01 will be designated as the Left Pylon, and a new configuration 2123650-02 will be created for the Right Pylon.
Additionally, the top-level kit 2123717-01 and 2123717-02 will be updated to explicitly call out and support these new left/right configurations to ensure proper configuration control, traceability, and correct installation.
This approach is required due to location-agnostic software not being ready for current builds.

| BOM / Item | Description | Status |
| 2123650-01 | Wing Utility Pylon — Left | Released |
| 2123650-02 | Wing Utility Pylon — Right | Released |

## Link to Engineering Change Notice (ECN)

https://jenaero.sharepoint.com/:x:/r/sites/JAI_Operations/Shared%20Documents/CCB%20Engineering%20Changes/ECN%20%23273%20-%20Add%20left%20and%20right%20configuration%20to%20B40%20utility%20pylon.xlsx?d=wc8d91dc877274221a7e1dc28e57b8043&csf=1&web=1&e=WK8il9

## Comments (8)

### Sanjay Menon, 2026-04-09

@Trevor Gronner

### Trevor Gronner, 2026-04-09

Sanjay and I talked briefly on this change. The original planned version of 2123650-01 was never sold to customers to our knowledge. Production Engineering is comfortable with repurposing the configuration to only relate to the left pylon.

### Trevor Gronner, 2026-04-09

@Steve Stack @Noah Chavez @Catherine Wagner @Brendan Palmer @Kyle England @Greg Kalichak @Sandra Lopez FYSA, wing utility pylon is being split into two configurations (one for left and one for right). The plan is to modify 2126350-01 to only be for the left pylon (as opposed to both as was planned with the original design). To our knowledge this has never been given to customers and it goes with an aircraft that is not fully production released, so I don’t see an issue with this.

### Tobi Ogunro, 2026-04-14

@Sanjay Menon Did you end up making the update so we can release this?

### Sanjay Menon, 2026-04-14

@Tobi Ogunro Pushed to pending CCB

### Christa Meck, 2026-04-15

Teams sent to @Sanjay Menon re:
Part number on drawing for 2123650 says 101-115866
Part number on drawing for 2123717 says 101-117342
The Part number field in question is a Solidworks Expression.  Logged an item with GoEngineer for our next sync up.

### Christa Meck, 2026-04-15

This Engineering Change has been reviewed using the checklist and is ready for CCB.
Notes:
- 2123650-01 - onhand 0
- 2123650-02 - not in Odoo as expected
- 2123717-01 - onhand 0
- 2123717-02 - not in Odoo as expected
- Part number on drawing for 2123650 says 101-115866.  Logged item on GoEngineer meeting for this since it is a generated field.
- Part number on drawing for 2123717 says 101-117342.  Logged item on GoEngineer meeting for this since it is a generated field.
- Disposition is rework but doesn't matter cause 0 on hand.
- 2123650 is used in 2123717
- 2123717 used in [500-2124086] Stalker Block 40 Wing Utility Pylon Kit   AND   [500-2123975-01] Stalker Block 35 Wing Utility Pylon Kit
- This item is one in a series of items involving L/R pylon configurations and separating B35 from B40.  This Engineering Change is unique to the parts involved.
- No open NCRs

[embedded: EC Checklist VXEP-1814.docx]

### Trevor Gronner, 2026-04-17

@Brendan Palmer This feels very similar to the other pylon left/right change tickets. Please make subtasks as needed and mark as Done when complete. Thanks!

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [EC Checklist VXEP-1814.docx](attachments/53712_EC%20Checklist%20VXEP-1814.docx.md) | docx | 36 | 2026-04-15 | converted |
