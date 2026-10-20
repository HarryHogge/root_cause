# VXEP-462: Replace payload/nudge controller with non-Chinese part

- **Issue type:** Major Project
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-07-08
- **Updated:** 2026-08-04
- **Resolved:** 2026-08-04
- **Reporter:** Greg Fryer
- **Assignee:** Matt Weber
- **Creator:** Greg Fryer
- **Parent:** VXEP-444 Sustainment: VXE-30 (inc'l minor issues and improvements)
- **Links:** relates to VXEP-926 (Make VXE30 and Havoc NDAA Compliant); relates to VXEP-872 (Updated Silvus Ground Control Station (SGCS1), increased performance and security); blocks ENG-3251 (Vendor PN RZ06-0356, IPN 100-112998 is obsolete. We have material to cover current loaded demand until Nov 2025. )
- **Issue color:** purple
- **Is this ticket a Design Project?:** Yes
- **Current Sprint Priority:** 10.0
- **LRR Desired Delivery Date:** 2025-03-01
- **LRR Required Delivery Date:** 2025-03-01
- **Product/Tech Owner:** Greg Fryer
- **Tech Lead:** Ted Trowbridge
- **Program (Marquee):** Ground Hardware Sustainment
- **Job Number:** J100082 - Sustainment: Ground Hardware

## Description

From Sam:
After more research and thought, I take back what I said about NDAA controller options from Taiwan and Vietnam.  It’s unlikely that COTS gamepads will be stable long-term NDAA-compliant solutions.  We’re well overdue to bite the bullet and go with a configuration-managed military controller from either of these companies:
 Ultra Electronics FMCU (already used by the Marine Corps and Army, probably the winner):
https://inkom.se/wp-content/uploads/2021/03/ULTRA_FMCU_LCD_2020.pdf
https://www.alamy.com/the-controller-used-on-the-hunter-and-killer-vehicles-are-similar-to-that-of-a-video-game-controller-and-was-experimented-with-during-the-maneuver-fires-implementation-exersice-mfix-april-3-at-fort-sill-image228581793.html
 SCIP:
https://www.scip-engineering.com/portfolio/pcu-l-series/
 Greg, can you please have someone in engineering contact these companies to see if they have two bailment units immediately available? They must include a USB cable and be Windows 10 compliant. Ideally, they would have a button layout as close as possible to our Wolverine V2. While integrating these controllers is typically very easy, and they’ll probably use higher-quality gimbals, I don’t know if we’d be able to integrate them and be comfortable using them in time for the fly-off.  I think having them at least available for show-n’-tell would be valuable, though. 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>
For context for the vendor, we make 10 a month or so (Kyle D will estimate better, but that’s a good enough number to roughly set qty).

## Project Deliverables

New defined, procurable controller, NDAA compliant. Released in Vault (likely with new PN and Catalog Number)
Release updated SGCS1 Catalog BOM (which will require displacing the existing BOM down one level, likely)
Release new "Spare" Catalog Number for just the controller

## Project Folder Link (Sharepoint)

https://jenaero.sharepoint.com/:f:/r/sites/IRAD/Shared%20Documents/General/Projects/Payload%20Controller%20Replacement?csf=1&web=1&e=UPTrEk

## Project Schedule

https://jenaero.sharepoint.com/:f:/r/sites/IRAD/Shared%20Documents/General/Projects/Payload%20Controller%20Replacement/Schedule?csf=1&web=1&e=7TDHAf

## Comments (7)

### Scott Whitney, 2024-11-21

@Ryan Babigian - I added the software plan to https://jenaero.atlassian.net/browse/GCSS-380. Ted and Jo Brown are going to review.

Still need to think about:
- Controller button mapping configurations?
- Do we know if the controllers are used for anything else?
- more

### Christa Meck, 2025-06-03

@Greg Fryer @Ryan Babigian  See linked ticket https://jenaero.atlassian.net/browse/ECM-295 this part is going obsolete!  Bringing to CCB on 2025-06-05

### Greg Fryer, 2025-06-03

@Matt Weber This has the various tickets on the controller. @Ryan Babigian moving this to Matt, as it should be straightforward.
@Christa Meck thank you!

### Carl Graf, 2025-08-04

@Matt Weber is this effort completed yet?

### Matt Weber, 2025-08-05

@Carl Graf Not closed out, still ongoing.

### Christa Meck, 2025-10-15

@Matt Weber The linked Engineering Change suggests we have until Nov to sort this.  Nov is getting closer.  How we looking?

### Christopher Maddaloni, 2026-08-04

Going to use SCIP controller, it’ll probably be fine

## Attachments (0)
