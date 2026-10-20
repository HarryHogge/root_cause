# VXEP-1083: Advanced Navigation HIL as "VXE30 Advanced Navigation Simulator"

- **Issue type:** Major Project
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2025-03-10
- **Updated:** 2026-07-06
- **Resolved:** 2026-07-06
- **Reporter:** Tobi Ogunro
- **Assignee:** Tobi Ogunro
- **Creator:** Tobi Ogunro
- **Labels:** LRR-March
- **Parent:** XKIT-4172 Link to VXE30 Advanced Navigation (MAGNSS)
- **Links:** is cloned by VXEP-1254 (Advanced Navigation HIL – “VXE30 Advanced Navigation Simulator” (LM Configuration))
- **Is this ticket a Design Project?:** Yes
- **Key Stakeholder(s):** Greg Fryer
- **Project Tier:** Tier 2
- **Planned Milestone(s):** Preliminary Design Review (PDR), Detailed Design/Critical Design Review (CDR), Production Readiness Review (PRR)
- **Project Deliverables:** QTY: 3 Hils Stalker Block 35X Advanced Navigation Simulator
- **Current Sprint Priority:** 18.0
- **Program (Marquee):** VXE30 Advanced Navigation
- **Job Number:** J100132 - VXE Advanced GPS Follow On

## Description

This project focuses on the design, integration, and delivery of three HIL systems for LRR training. The HIL enclosures must be user-friendly, professional in appearance, and functionally accessible. The final package will include hardware and software, ensuring that packaging, assembly, and testing are fully validated before shipment.
### Deliverables:


QTY: 3 Hils VXE30 Advanced Navigation SimulatorFinalized BOM (Hardware & Software)HIL Enclosure DesignIntegrated Software SetupPackaging Solution for Customer DeliveryManual needed on setting up the HIL- Clarifications on Open Questions
- VTOL BOM - Needed to identify hardware (PN?)
- HIL assembly - Mark S, Electronics, Engineering
- MCM Hardware- Liam and Brandon
- Fix Wing BOM
- Due Date?
- Checkout Procedure Needed (standard MCM checkout?)

## Project Folder Link (Sharepoint)

https://jenaero.sharepoint.com/:f:/r/sites/IRAD/Shared%20Documents/General/Projects/Advanced%20Navigation%20HIL?csf=1&web=1&e=6v9tUQ

## Project Schedule

https://jenaero.sharepoint.com/:u:/r/sites/IRAD/Shared%20Documents/General/Projects/Advanced%20Navigation%20HIL/Progress%20Tracker/Schedule%20-%20Advanced%20Navigation%20HIL%20as%20VXE30%20Advanced%20Navigation%20Simulator.mpp?csf=1&web=1&e=2liBLR

## Comments (5)

### Matt Philley, 2025-03-11

Helpful PNs
| FIXED WING HIL BOX ASSY | 107-104055 |
| XE VTOL HIL BOX ASSY | 107-104091 |
| VXE30 HIL TRANSIT CASE ASSY | 107-104414 |

### Brendan Palmer, 2025-03-11

@Tobi Ogunro @Scott Whitney @Ben Norris Is there any reason we have the SLA Breakout Board Rev B called out for this when we have a released BoM for Rev C? Looks like they use the same components, just in different quantities. They are located under the same PN: 128-117156-01.
C:\JAI Vault 1\projects\128 - vxe2024\electical design\pcb\128-117156-01 sla breakout v2\128-117156-01-SLA Breakout V2, BOM.xlsx
C:\JAI Vault 1\projects\128 - vxe2024\electical design\pcb\128-117156-01 sla breakout v2 rev c\128-117156-01 Revision C, BOM.xlsx

### Ben Norris, 2025-03-11

@Brendan Palmer should be rev C if the bom was pulled from premagnss it would list rev B but rev C has a power filtering improvement that would be important for this application.

### Scott Whitney, 2025-03-11

@Brendan Palmer @Ben Norris  - I called out Rev B because they would still work for HILs. The power filtering is unnecessary for this application based on my conversation with @Connor Peebles. We can verify with him or decide to trash the Rev Bs and move to Rev C.

### Christa Meck, 2026-07-06

No work done in over a year.  Canceling.

## Attachments (0)
