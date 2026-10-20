# VXEP-872: Updated Silvus Ground Control Station (SGCS1), increased performance and security

- **Issue type:** Major Project
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-01-06
- **Updated:** 2026-02-07
- **Resolved:** 2025-08-06
- **Reporter:** Greg Fryer
- **Assignee:** Carl Graf
- **Creator:** Greg Fryer
- **Labels:** LRR-March
- **Parent:** VXEP-902 LRR March Delivery
- **Links:** relates to VXEP-462 (Replace payload/nudge controller with non-Chinese part)
- **Project Tier:** Tier 2
- **Planned Milestone(s):** Preliminary Design Review (PDR), Production Readiness Review (PRR)
- **LRR Desired Delivery Date:** 2025-03-01
- **LRR Required Delivery Date:** 2025-03-01
- **Product/Tech Owner:** Greg Fryer
- **Tech Lead:** Jo Brown
- **Program (Marquee):** Ground Hardware Sustainment
- **Job Number:** J100082 - Sustainment: Ground Hardware
- **Estimated Finish Date:** 2025-07-31

## Description

This is a consolidation of several drafted projects, scope elements (represented as Epics below):
- Update kit contents based on various feedback, including NDAA controller from this project:https://jenaero.atlassian.net/browse/VXEP-462
- Update to https://jenaero.atlassian.net/wiki/x/AoCpH
- Update Laptop to new (non-obsolete) version from Dell, resolve MS Office licensing, protect for future map solution (if possible to define), apply cyber-hardening defaults (Edge general, not customer specific)
- Update radio configuration to include Spectrum Dominance.
- Update entire case/package to fit everything well. Also make the newer weather/wind device fit better (slightly larger opening, or new arrangement. Also ease the coil-requirement on the RF cables, if possible.
- Evaluate if any equipment can be removed (unlikely)

Resulting system will be ITAR controlled. It must have a unique PN (not just a configuration). Legal is evaluating if we need a note on the drawing for this.
The following scope is removed:
- Add Athena.AI Cortex computer and software (and cables), include ethernet switch. This will be delivered in it’s own case.

## Project Deliverables

New GCS data package, and prototypes for various contracts.
Transition to production (likely)

## Project Folder Link (Sharepoint)

https://jenaero.sharepoint.com/:f:/r/sites/IRAD/Shared%20Documents/General/Projects/LRR/March%202025%20Delivery%20Files/1%20-%20SGCS1?csf=1&web=1&e=uRwR9x

## Project Schedule

https://jenaero.sharepoint.com/:f:/r/sites/IRAD/Shared%20Documents/General/Projects/LRR/March%202025%20Delivery%20Files/1%20-%20SGCS1/101%20-%20Schedule?csf=1&web=1&e=YgI6Ja

## Comments (4)

### Carl Graf, 2025-02-04

I just received word that the controller needs Glenair to USB-A cable harness. Need to add an EE to this effort. 

@Ryan Babigian are you tracking an effort to support this harness?

### Carl Graf, 2025-02-04

TNT Concord action (from NG) to get contact info, at NG, to supply chain, Allen Peek, to acquire the SW. It is ITAR controlled. 

MDJ sent over info on 2/3. @Jo Brown to follow up with Allen Peek.

### Jo Brown, 2025-02-04

@Carl Graf Allen and I had a short conversation earlier today. He’s getting in touch with Northrop Grumman right now to figure out next steps.

@Greg Fryer I also got in touch with Sam Jones. We’ll be using our encrypted server, Sphinx, to store TNT Concoord. This server requires ZPA (Zscaler) to access. To move this installer onto the LRR GCS laptops, we will use the same encrypted external drive that we include in the SGCS1, and, once we have the ITAR stickers, mark those drives as ITAR controlled.

### Carl Graf, 2025-08-05

@Greg Fryer, unless you have issue with it or would like a review, I can close out this ticket. 

FYSA, @Addison Osborn @Jessica Meyers @Matt Weber @Matt Philley

## Attachments (0)
