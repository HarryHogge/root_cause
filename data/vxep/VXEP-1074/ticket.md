# VXEP-1074: MOD-A Kit Cable, Connector and AHRS Issues

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-03-06
- **Updated:** 2025-11-14
- **Resolved:** 2025-11-14
- **Reporter:** Mike DeJesus
- **Assignee:** Tobi Ogunro
- **Creator:** Mike DeJesus
- **Links:** relates to VA-2455 (Mod Payload A-Kit "Gen 2" (originally "long term fixes")); relates to VXEP-891 (Create Mod Payload A-Kit for VXE30 Advanced Navigation aircraft (deliveries required for LRR by 23-03-2025))
- **Severity:** 2 - Degraded Performance - No Workaround
- **Product/Tech Owner:** Charles David Madewell

## Description

After delivering MOD-A Kit retrofit kits to the PMA-263 customer they reported some issues that persisted after the retrofit (Customer brief attached). 

During a follow-on visit @Alexander Alan Arnold and @Hannah Goelz provided a summary of the issues they observed, see below.

Issue 1: RF Cabling Misalignment https://jenaero.atlassian.net/browse/VA-2533 
- Reference: PN 111-105524
- Problem: The array antenna mount connectors are not extending far enough to properly seat and connect with the Bloodhound antenna array (MB and QB). This results in a dB drop rate and reduced RF signal strength.
- Supporting Evidence:
- Video 1: Shows the issue with the retrofit.
- Video 2: Demonstrates that pulling the Bloodhound connector plate further out does not resolve the problem.
- Potential Fixes:
- Extend the connector further outward.
- Use longer connectors.
- Use a thinner plate.
- This may require R&D collaboration with engineers.
- Responsibility & Recommendation:
- While this is not entirely EDGE’s responsibility, the fastest and simplest solution would be for EDGE to update PN 111-105524 rather than requesting CACI to manufacture entirely new antenna array mounts.

Issue 2: MAIM Connector Fasteners https://jenaero.atlassian.net/browse/VA-2521 
- Problem: The fasteners are not truly captive and fall out easily.
- Potential Fix:
- Use the CDIPT-recommended hardware to ensure a truly captive fastener.

Issue 3: AHRS GPS Timestamp Intermittency https://jenaero.atlassian.net/browse/VXEP-1138 
- Problem: The AHRS unit is intermittently failing to send GPS data in the required format (1PPS) for bloodhound to use the data. The SBG unit does not transmit in a 1 PPS format.
- Key Considerations:
- CDIPT reports that some SBG units work while others do not.
- Investigation is needed to determine whether the issue is related to configuration settings or a software/firmware version discrepancy.

Issue 4: DSUB Connector Screws Backing Out
- Reference: PN 111-105450 and 111-105451
- Problem:
- Screws from PN 111-105451 can back out from the retainer clip.
- The standoff peg is approximately 1/16 inch too long.
- Additional Note:
- This issue was not included in the CDIPT report but was brought to our attention by Kendel, the on-site representative for Synergy.

## Comments (6)

### Mike DeJesus, 2025-03-06

FYSA, @J Vo @Pat Wells @Charles David Madewell

### Charles David Madewell, 2025-03-06

@Tobi Ogunro

### Matt Weber, 2025-03-07

I looked at the array mount interface and found that the nominal contact interference is less than the SMPM connection should have.  This most likely contributes to the poor connection and dB drop we see.  The shims/new holder improves the contact but doesn’t fix the problem.  The contacts look to be spring loaded to absorb excess interference, so pushing the male contacts farther out from the holder should give us a reliable mate.  This would be a new PN for the contact holder and RF cable assembly, but only a revision to the wing tip assembly.
[embedded: image-20250307-191638.png]

### Tobi Ogunro, 2025-03-07

@Greg Fryer @J Vo @Desiray Johnston @Trevor Gronner @Charles David Madewell @Mike DeJesus Please see Matt comment below.

### Trevor Gronner, 2025-03-10

@Tobi Ogunro @Matt Weber We don’t currently have revision tracking for inventory. If we do not update the part number for the wing tip antenna array mount assembly we will not have clear data on when we moved over to the new contact holders. If they are not functionally interchangeable, I would recommend updating the part number for the wing tip antenna array mounts as well. Thanks!

### Greg Fryer, 2025-11-14

Multiple issues resolved and features updated in multiple tickets.

## Attachments (9)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Blound arrays.jpeg | image | 1151 | 2025-03-06 | listed only |
| Issue 1 video test Pulling CACI conector further.mov | video | 3003 | 2025-03-06 | listed only |
| Issue 1 video.mov | video | 3824 | 2025-03-06 | listed only |
| Issue 2 reference (2).jpeg | image | 377 | 2025-03-06 | listed only |
| [ModA_Issues_DamNeck 1 (1).pdf](attachments/26875_ModA_Issues_DamNeck%201%20(1).pdf.md) | pdf | 386 | 2025-03-06 | converted |
| [ModA_Issues_DamNeck.pdf](attachments/26905_ModA_Issues_DamNeck.pdf.md) | pdf | 386 | 2025-03-06 | converted |
| issue 4 (2).jpeg | image | 1843 | 2025-03-06 | listed only |
| issue 4.jpeg | image | 3031 | 2025-03-06 | listed only |
| image-20250307-191638.png | image | 406 | 2025-03-07 | listed only |
