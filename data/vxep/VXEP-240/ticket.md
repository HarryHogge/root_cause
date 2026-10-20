# VXEP-240: HIL Documentation needs to be released - Mechanical

- **Issue type:** Engineering Change
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2023-03-09
- **Updated:** 2025-09-15
- **Resolved:** 2025-04-29
- **Reporter:** Former user
- **Assignee:** Gerrit Sperling
- **Creator:** Former user
- **Labels:** SimBuild
- **Links:** relates to VXEP-563 (Consider providing HILs or other simulation to trainers, so that they could practice hovers and nudges without using an actual HIL); relates to FS2-1634 (HIL v1.1 - replace XPLANE as 6DOF); relates to ENG-240 (107-103343 VXE HIL Kit needs complete documentation package released)
- **Part Number(s):** 107-103343, 107-103344
- **Production Stakeholder:** Matt Philley
- **Engineering Change Level:** Level 0 - Scope of change is obvious to assigned engineer
- **Leadership Stakeholder:** Desiray Johnston
- **Link to Engineering Change Notice (ECN):** ECN #53 107-101050 HIL KIT Documentation Release, Mechanical.xlsx

## Description

This is currently not a formal product, though it has been sold. Not currently tracking as a Design Project, but will likely escalate as it gets defined.
>>>>>>>>>>>>>>>>>>>
Track and release of the HIL mechanical documentation which was missing. 
107-103343 - VXE30 Iron Bird and HIL Flight Simulator Package, BOM [DRAFT]  – calls out old laptop power adapter
107-103344 - VXE30 Iron Bird and HIL Flight Simulator Package, No Laptop, BOM [DRAFT]  
107-105822 - Transit Case, Empty [RELEASED] 
107-104414 - Transit Case, Assy [DRAFT] 
107-111227 - Transit Case Exterior Case Label [RELEASED]  (OUTDATED FORMAT)
107-100058- Transit Case Exterior Case Label, No Laptop (107-103344) [DRAFT]   (OUTDATED FORMAT)
107-111234 - Contents Placard [DRAFT]  (OUTDATED FORMAT - SHOULDNT HAVE PNS)
106-104454 - Silvus Enclosure Assy, No Radio [me-RELEASED]  
107-111015 - VXE30 HIL Flight Sim Laptop, Configured [DRAFT]  – needs further definition
- Check if the above includes x-plane license. - contains 100-111117 XPlane
- Some description of the purpose of each version would be useful.
- We should create one without a flight simulator, for ironbird, troubleshooting, etc.

## Comments (9)

### David R. Martin II, 2024-01-22

@Barry Mendez @Greg Fryer Both the reporter and assignee are no longer with the company. Who can this be assigned to?

### Greg Fryer, 2024-01-22

@David R. Martin II Since this will be a multi-step effort, I’m making it an improvement in the VXE Problem project. Will see if any of the designers can do this, but not sure who  would be knowledgeable.
@David Grosher Would @Wesley Reynolds or @Brandon Slater be able to walk one of the MEs what should be included? This is low priority, but would like to have the “how” defined. 
(For ref, it looks like Will Harris started the change, but did not finish it.)

### Cameron Chapman, 2024-09-05

@Desiray Johnston @Kyle DeBernardi here is the project tracking HIL documentation that is not released.

### Gerrit Sperling, 2024-09-09

@Wesley Reynolds @Brandon Slater Are either of you available to meet with me to help verify the accuracy of the ME documents listed above?

### Wesley Reynolds, 2024-09-09

@Gerrit Sperling I can meet with some time this week.

### Gerrit Sperling, 2024-09-10

@Wesley Reynolds I scheduled a meeting for Thursday, Sept 12

### Gerrit Sperling, 2024-09-12

After meeting with Wes, the highest level BOMs are accurate but need to call out the current laptop/charger configurations. The HIL laptops also need to be defined more completely. There is an Edge X-Plane Package that needs to be installed to the desktop of the HILs alongside the Xplane Software. I am going to generate a PN for this package (located on sharepoint but too large to download easily, see @Brandon Slater for USB drive with files). This will likely be defined similarly to 105-111426 Laptop Image Configuration. Note that HIL boxes will need to be shipped out and can only be used with the laptops they are configured with.
I am going to update the formatting of the files above, fixing outdated labels/placards to our current standard and create ECN’s to track the release of these items.

### Gerrit Sperling, 2024-09-12

@Greg Fryer Does the HIL kit have or need a catalog/sales PN assigned to it?

### Greg Fryer, 2024-09-12

@Gerrit Sperling We already sell the HIL, the catalog lists these numbers:
[embedded: image-20240912-233700.png]
Regarding the software config, please contact @Jo Brown We have just been establishing how we document the software config of a product, and it is slightly different than our history of adding an image/installer to the BOM.
We’ll need to decide if we should just revise the existing PN, or if now is the time to make catalog numbers. I believe the SW team is working on HIL 1.1 which will have significantly different software - so it might make sense to change to a Catalog PN when we do that, and just leave the number alone for the existing version. I am flexible.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240912-233700.png | image | 7 | 2024-09-12 | listed only |
