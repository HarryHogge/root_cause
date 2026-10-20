# VA-2533: Resolve and Release Mod Payload Standard antenna interface issue.

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-03-10
- **Updated:** 2025-09-26
- **Resolved:** 2025-04-02
- **Due:** 2025-03-13
- **Reporter:** Greg Fryer
- **Assignee:** Tobi Ogunro
- **Creator:** Greg Fryer
- **Parent:** VXEP-1008 Mod Payload A-Kit Gen 2 design/release/test (Long term issue resolution)
- **Links:** blocks VA-2455 (Mod Payload A-Kit "Gen 2" (originally "long term fixes")); blocks VXEP-891 (Create Mod Payload A-Kit for VXE30 Advanced Navigation aircraft (deliveries required for LRR by 23-03-2025))
- **Production Stakeholder:** Trevor Gronner
- **Other Stakeholder (as required):** Desiray Johnston
- **Leadership Stakeholder:** Charles David Madewell
- **Product/Tech Owner:** Charles David Madewell
- **Program (Marquee):** Mod Payload A-Kit
- **Job Number:** J100078 - Sustainment: VXE-30

## Description

There is a misalignment issue with the RF cabling in the Array Antenna Mount (PN 111-105524), causing insufficient connector extension to properly seat with the Bloodhound Antenna Array (MB and QB). This results in dB drop rate and reduced RF signal strength.
Analysis of the array mount interface revealed that the nominal contact interference is lower than the required SMPM connection, contributing to the poor connection. While shims and new holders improve contact, they do not fully resolve the issue. The spring-loaded contacts suggest that pushing the male contacts further out from the holder would ensure a reliable connection.
A new part number is required for the contact holder and RF cable assembly, and because the wing tip assembly is not functionally interchangeable, it also requires a new part number rather than a revision.
**Action Items:**

- Redesign Contact Holder & RF Cable Assembly:
- Modify the design to extend the male contacts outward for improved connection reliability.
- Assign a new part number for the contact holder and RF cable assembly to reflect this update.
- Assign New Part Number for Wing Tip Antenna Array Mount Assembly:
- Since the updated version is not interchangeable with the existing assembly, create a new part number for proper inventory differentiation.
- Ensure clear documentation of the transition between old and new assemblies.
- Inventory & Revision Tracking:
- Establish a tracking system for production and inventory to ensure correct usage of the new assemblies.
- Label and update BOMs and work instructions accordingly.

**Deliverables:**


Updated design for the contact holder and RF cable assemblyNew part number for the RF cable assemblyNew part number for the wing tip antenna array mount assemblyUpdated BOMs and inventory tracking documentation

## Comments (4)

### Trevor Gronner, 2025-03-12

@Brendan Palmer @Nina Menon @Kyle England@Sandra Lopez For your situational awareness, the wing tip antenna array mount is being redesigned again by design engineering based on customer feedback. This will impact the Mod Payload A Kit Gen 2 and the Mod Payload A Kit Advanced Nav builds we are currently working on in Final Assembly.

### Brendan Palmer, 2025-03-13

@Trevor Gronner @Tobi Ogunro @Greg Fryer Does this impending redesign put the HSV FLOPS Asset build on hold?
https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/Engineering%20Request%20for%20Prod%20Resources/DispForm.aspx?ID=459&e=4d6bZT 
https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/Engineering%20Request%20for%20Prod%20Resources/DispForm.aspx?ID=458&e=FipHrd

### Tobi Ogunro, 2025-03-20

@Brendan Palmer Did you get the answer you need to your question below?

### Brendan Palmer, 2025-03-20

@Tobi Ogunro Yes, we shipped the current design since they are for asset use.

## Attachments (0)
