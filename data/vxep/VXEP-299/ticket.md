# VXEP-299: NCR 2583 - Wrong wire type used on Pegasus servos

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2024-03-11
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Cameron Chapman
- **Assignee:** Matt Philley
- **Creator:** Cameron Chapman
- **Issue color:** purple
- **Supply Chain Stakeholder:** Victor Vandor
- **Other Stakeholder (as required):** Matt Philley

## Description

The approved wire and alternate both have insulation diameter that should properly seal to the JST connector. 
Primary: 
| Nom. Insul. Thick. (in) | 0.010 |

Alt: 
| Jacket (Insulation) Diameter | 0.060" (1.52mm) |

JST requirement: .055-.067" insulation diameter. (1.39mm min)

Used 10900 Telemeter Outer Diameter: 1,17 mm (min); 1,42 mm (max)
[embedded file]

## Plan

The 10900 looks like acceptable performance other than the insulation diamter. I recommend one or a combination of the following, depending on production need dates. 
- RMA servos to pegasus to use the correct wire.
- Test build using the clear heat shrink we use on the 26AWG wire. Measure diameter after applying that. Insert into JST and inspect for issues. Report findings. We can review and approve for the remaining qty.

JST requirement: .055-.067" insulation diameter. (1.39mm min)
 Used 10900 Telemeter Outer Diameter: 1,17 mm (min); 1,42 mm (max)

## Comments (12)

### Matt Philley, 2024-03-11

@Cameron Chapman 
- Test build using the clear heat shrink we use on the 26AWG wire. Measure diameter after applying that. Insert into JST and inspect for issues. Report findings. We can review and approve for the remaining qty.

The purpose of this would be to build up the wire diameter to achieve a successful crimp for the JST contact is that correct? So we would need to clip off the contact, add heat shrink, re-crimp contact? 
If that is correct we can run a sample to see if that causes the length to be an issue.

### Matt Philley, 2024-03-11

Reference: 110-115192 JST Termination Specification
| Description | Internal PN | Vendor PN |
| HEAT SHRINK, NON-ADHESIVE, POLYOLEFIN, 2:1, CLEAR, 1/16" | 100-106697 | FP301-1/16-100'-CLEAR-SPOOL |

[embedded file]
[embedded file]

### Matt Philley, 2024-03-11

@Cameron Chapman 
OK here is the pitch for a proposed dispo:
There are 2 concerns with the “Type E” insulation wire and recommendations on how to resolve each one:

- Type E wire is under the minimum “Applicable Wire Insulation OD”
- Is: Type E is .051” +/- 0.005” (per Telemeter 10900 spec)
- Should be: .055” - .067” (per JST Spec)

Recommend we pull test to get a gut-check using same “Type E” spec wire such as 100-107261, which is Alpha Wire 5855. If those pass then we have a good indication that the servos are all acceptable for our application.
In addition we pull Qty 10 servos, de-pin all contacts, and perform a visual Crimp Inspection. If they all pass then we are satisfied.
[embedded external]
- The smaller diameter wire does not weather seal on the blue boot well.

Recommend we use RTV similar to 107-102095 Boom Signal Harness so seal boot around the wires. This way we dont need to de-pin every JST and the work can be done in Final Assy instead of Electronics. 
[embedded file]

### Matt Philley, 2024-03-12

@Cameron Chapman @Nina Menon 
RTV Proposal, Additional Details:
100-102206 DOW732, Black RTV
Application Method:
Goal is to add additional material between blue gasket and PTFE wires to promote a moisture barrier for the contacts. We will do this by applying a small amount of RTV in and around the wires and gasket. 
NOTE: The holes in the gasket are ~0.040” and the wires a minimum of 0.046” so there is some amount of interference already.
Open up a small gap by pulling wires “away” and apply a small amount of RTV in these gaps to promote RTV flowing a small amount into the gasket. Repeat this for the other side to promote a small amount of RTV flowing fully around each wire.
[embedded file]
After RTV has been applied clean off excess to reduce the amount of RTV visible. However, there should be a small amount visible around each wire to provide sealing.
[embedded file]

Verification:
To verify the RTV seal was successful wait until the RTV has cured. Then, mount the connector vertical so a small amount of alcohol can be added to the connector. If alcohol leaks through the seal then it was not successful. 
NOTE: The standard wire passes this test. The thin wire does not pass this test without RTV. 
[embedded file]

### Matt Philley, 2024-03-12

@Liam Limon FYSA

### Matt Philley, 2024-03-12

Update:
Use 100-106125, Adhesive Heat Shrink Tubing, 3/8" (0.375"), 3:1, Black (alt. vendor PN: 7861K54 - 4ft long)
Cut a short length (final length TBD, but approx. 0.5”) and position it with (final length TBD, but approx. 0.150”) off the back side of the JST
Shrink down and squeeze back side to seal the back of the connector
[embedded file]
This does reduce the bend off the back of the connector, however the tightest bend is on the Left Wing Tip and that should fit just fine as long as we control and inspect that. 
[embedded file]

### Matt Philley, 2024-03-13

Vendor has proposed the following: “We can add silicone sealant in the connector below the blue gasket to restore the sealing properties of the connector. “
I have asked for the following clarifying details:
- What sealant are you proposing to use?
- Is the sealant injected from the front of the connector or the rear?
- How are you making sure no sealant covers any of the mating surface of the contacts and does not effect continuity of the connector?


@Cameron Chapman  this looks like what you have been suggesting… I am curious to see how they did it to make sure it does not “leak” into the front of the connector. 
[embedded file]
[embedded file]

### Matt Philley, 2024-03-13

Vendor proposing to use the following material which is apparently very thick and does not leak down into connector. It also cures quickly. This is what they use to pot on the base of the servo already. 
I “potted” a JST with our black RTV and was able to verify it is possible to pot a thin layer and still get the gasket to fully seat… seems reasonable? 
https://eclecticproducts.com/product/amazing-goop-automotive/ 

[embedded file]

### Matt Philley, 2024-03-13

Qty 10 servos have been depinned and are pending Crimp Inspection. We are short on inspectors today so it might not be until tomorrow. 
3/14: Qty 10 servos passed crimp inspection and we are OK to move forward with rework.

Approval for rework has been passed to vendor as well

### Cameron Chapman, 2024-03-14

@Matt Philley since goop is already used on the servo and “AMAZING GOOP AUTOMOTIVE can also coat terminals on batteries.” this seems acceptable to use for potting as long as we ensure it stays out of the contact mating area. Approved.

### Matt Philley, 2024-03-18

Adding more info from Vendor on their troubleshooting and investigation of rework methods:
[embedded file][embedded file]

### Matt Philley, 2024-03-18

Production to start reworking today using “internal RTV” method per dispo in NCR:

If servos pass crimp inspection it is acceptable to seal back of connector using 100-102206 DOW732, Black RTV with the following method:
Using tweezers or another suitable tool carefully remove the blue seal from the back of the JST.
Apply a thin layer of RTV to the inside of the connector ensuring there is plenty of room left for the seal to fully seat. QA to visually inspect RTV seal is complete.
Allow the RTV to mostly or fully cure before moving seal back in position to avoid squeezing RTV deeper into the connector potentially in unwanted areas.
Replace blue seal and ensure it is flush with back of connector.
Visually inspect to make sure no RTV is present from the front side of connector and no excess RTV is present elsewhere on JST or servo.

## Attachments (14)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240311-170350.png | image | 300 | 2024-03-11 | listed only |
| image-20240311-183152.png | image | 191 | 2024-03-11 | listed only |
| image-20240311-183211.png | image | 285 | 2024-03-11 | listed only |
| image-20240311-210815.png | image | 142 | 2024-03-11 | listed only |
| image-20240312-182049.png | image | 185 | 2024-03-12 | listed only |
| image-20240312-182305.png | image | 225 | 2024-03-12 | listed only |
| image-20240312-182546.png | image | 627 | 2024-03-12 | listed only |
| image-20240312-221824.png | image | 344 | 2024-03-12 | listed only |
| image-20240312-221909.png | image | 470 | 2024-03-12 | listed only |
| image-20240313-142159.png | image | 321 | 2024-03-13 | listed only |
| image-20240313-142214.png | image | 575 | 2024-03-13 | listed only |
| [tds-amazing-goop-automotive-english.pdf](attachments/19338_tds-amazing-goop-automotive-english.pdf.md) | pdf | 373 | 2024-03-13 | converted |
| [PoC thin Wire Issue Method1.pdf](attachments/19584_PoC%20thin%20Wire%20Issue%20Method1.pdf.md) | pdf | 1603 | 2024-03-18 | converted |
| [Suggestion Method3.pdf](attachments/19585_Suggestion%20Method3.pdf.md) | pdf | 137 | 2024-03-18 | converted |
