# VXEP-1224: 2121756-01 Updated ADP Document Release for Production

- **Issue type:** Engineering Change
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2025-04-24
- **Updated:** 2026-06-17
- **Resolved:** 2026-03-09
- **Reporter:** Cameron Chapman
- **Assignee:** Eric Rinell
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-1157 (2121756-01 Updated ADP Document Release for Production); relates to VA-2794 (2122858-01 Heated Pitot Cable Production Redlines); relates to VXEP-1395 (2121366-01 AIR DATA POD V3 HARNESS ASSEMBLY redline from Jira VXEP-1049 implemented incorrectly. SB: ODU to ADB P6 6.35". IS: C1 to ADB P6 as 6.35" on Rev B); duplicates XKIT-5086 (Add RF protection to Heated ADP 2121756-01); relates to VXEP-1918 (2121823-01 REV B - RTV callout)
- **Engineering Change Level:** Level 0 - Scope of change is obvious to assigned engineer

## Description

See Confluence for instructions and templates: https://jenaero.atlassian.net/l/cp/ztB58xvi 
ECN: https://jenaero.sharepoint.com/:x:/s/JAI_Operations/EU_O6EVw901Osx-jqJSYq8wBH8NVen64x2BpkcxnnzLBPg?e=SbaLxn

## Issue Status

@Eric Rinell @Camron Richardson there should be an ECN linked to this eng change. Please link and update for the linked releases that will be CCBd with this assembly.

## Comments (31)

### Daniel Herrera, 2025-04-24

@Grant Goodman @Rajesh Budhabhatti Drawing 2121366-01: AIR DATA POD V3 HARNESS ASSEMBLY is ready for review. Pdf in Vault.

### Rajesh Budhabhatti, 2025-04-24

@Cameron Chapman @Daniel Herrera Hi Cameron, this harness is ready for release. Thank you.

### Cameron Chapman, 2025-04-25

@Rajesh Budhabhatti it is a mech drawing checked out by Eric. Please check if you meant a different drawing.

### Rajesh Budhabhatti, 2025-04-25

Hi Cameron,
Sorry. I meant the 2121366-01 is ready for release. I will check with Eric to see if he has checked out the mechanical drawing.
Regards
Raj

### Eric Rinell, 2025-05-27

Part drawing revvING to C level 0 change. CHANGED 6-32 COUNTERSUNK TO SLOTTED,
ADDED RELEIF FOR WING PLUG, ADDED GORE
VENT HOLE AND LOCATING FEATURE
changes performed in-house for first 10 units and functionality tested. other 50 units in inventory can be modified to rev C at any time in-house.

### Eric Rinell, 2025-06-13

Revised 2121002-51 to REV E to include black anodize
Revised 2122371-03 to REV B to include black anodize
Revised 2122738-01 to REV B to include black anodize
Revised 2122738-02 to REV B to include black anodize

NO GEOMETRY CHANGES
PERMISSIBLE TO ORDER PARTS FROM SAME VENDOR EVEN IF THEY CANNOT PROVIDE ANODIZE. WE ARE SENDING EXISTING INVENTORY TO ANO-TECH FOR ANODIZING AND CAN DO SO IN THE FUTURE.

### Eric Rinell, 2025-07-03

Revising 2122481-01 from A to B to incorporate redlines from practice build. Some item # callouts are incorrect

### Eric Rinell, 2025-07-14

Released 2121923-01 to rev B. Scott approve changes i made to implement red-lines from VXEP-1327

### Eric Rinell, 2025-07-21

Released 2121002-01 (static probe gore bonding) to ref F to replace the old fuel sealand with NEW 1 part adhesive 2124912-01 (AA 3494 - loctite pn) and added masking callout to anodize to eliminate future sanding operations.

### Eric Rinell, 2025-07-28

RE-RELEASED TO REV B: 2122623-01; HEATED PITOT-STATIC, SUB-ASSY
INCORPORATED REDLINES FROM PRACTICE BUILD, ADDED TORQUE CALL-OUT FOR FITTING, REMOVED DUPLICATE FITTING, SPECIFIED THERMAL PASTE APPLICATION IN MORE DETAIL

### Eric Rinell, 2025-07-28

RELEASED 2121756-01 AIR DATA POD; TOP LEVEL; TO REV B
INCORPORATED REDLINES FROM PRACTICE BUILD SUCH AS 
ADD LOCTITE CALLOUT TO MICRO-D SCREWS
ADD RTV TO LIDAR CONNECTOR EXIT

### Eric Rinell, 2025-07-28

RELEASED 2121823-01, HARNESS ASSEMBLY, HEATER CONTROL BOARD TO REV B
ADDED OPTION TO FILL SMALL VOIDS WITH RTV

### Eric Rinell, 2025-07-28

RELEASED 2121923-01; SA CAM SUBASSY TO REV C
ADDED CA GLUE TO BOM AND ADDED NOTE WITH CALLOUT

### Eric Rinell, 2025-08-12

2122481-01 (AIR DATA BOARD ASSEMBLY) CHANGED THE TYGON TUBING LENGTH FROM 1.1 TO 1.2 BETWEEN TEE AND STATIC PROBE FITTING. REV-C RELEASED. REV-B ASSEMBLIES STILL GOOD AND CROSS COMPATIBLE.

### Eric Rinell, 2025-08-25

UPDATED 2122623 TO REV C TO CHANGE ADHESIVE USED TO BOND HEATER INTO PITOT FROM E-20 TO AA3494 FOR ASSEMBLY CONVENIENCE AND SPEED. LEVEL 0 CHANGE

### Eric Rinell, 2025-08-27

CAN TERMINATION RESISTOR REMOVED FOR ADP -02 CONFIG FOR BLK 35/40
TBD: WILL ADB WITHOUT RESISTOR ALSO WORK ON VXE30?   
- UPDATED 2122481(ADB POTTED ASSEMBLY) TO REV D TO ADD -02 CONFIG
- UPDATED 2121756(ADP TOP LEVEL ASSEMBLY) TO REV C TO ADD -02 CONFIG
- UPDATED 2122839(ADB) TO ADD -02 CONFIG (FILE IS IN SHARED STATE)

### Sloan Payne, 2025-10-01

@Eric Rinell  I am the Quality Manager in HSV. This is marked as high, so I am sure it is being worked but wanted to let you know that I am holding the 2121756-01, part number implementation due to the drawing not being released and no revision in revision block. @Emalee Johnson @Justin Evans @Spenser Bracken @Maggie Morris FYI

### Eric Rinell, 2025-10-01

@Sloan Payne The drawing for 2121756-01 was updated and released to rev B to correct that revision block issue. If you look in egg you can find that latest drawing. Shouldn't need to hold part number implementation for any reason. This issue tracker can probably be closed out.

### Sloan Payne, 2025-10-08

@Greg Fryer My understanding was that the Egg and Vault were linked so if the Revision B drawing was released in Egg why is it not populating in the vault. @Eric Rinell I can move these parts forward once the above is resolved.

### Sloan Payne, 2025-10-08

@Sloan Payne @Steve Stack I wanted to make you aware of this disconnect that may require action.

### Greg Fryer, 2025-10-08

@Sloan Payne @Steve Stack I see you scheduled a discussion, which might be a better way to explain. But in case it helps un-block work/close out:
The vault and egg ARE linked, however the vault maintains every iteration (check in/out), Eng release (B01, B02, B03, etc.), and production release (B, C, etc.). I believe what is happening here is simply that the next revision to the ADP has started (it’s on it’s way to Rev C, but not released yet so no notice/ticket). By default the Vault will always show you the latest. On egg, the prod folder will always and only have the latest CCB released version of a given part or drawing. This difference is why we created egg.
Using the vault history function, it is possible to pull the specific iteration that matches the released PDF if an audit is needed.
Our current standard (because we are still migrating things to egg) is “Egg is the authority, if a part/drawing/etc. is not there, then the vault should be used”. We’re working on tools that will let us ensure all production parts/files get published to egg.

### Greg Fryer, 2025-10-08

@Nicole Hess Note the above comment, we might need some clearer documentation (which of course will need update when Manage kicks in…)

### Sloan Payne, 2025-10-08

@Greg Fryer @Steve Stack @Nicole Hess @Ryan Forcier We can discuss this in next week's meeting, but will there be training/announcement that the Egg is the authority as HSV is not aware of that. Also, as far as sifting through vault history this is not a function operators can do so that will not pass in an audit as they need to be able to pull the current released drawing and they do not have access to all historical revisions.

### Sloan Payne, 2025-10-08

@Greg Fryer @Steve Stack @Nicole Hess @Ryan Forcier Is the standard to have the released pdf drawing in the vault? If the released revision B was in the vault, then there would be no need to search history in SolidWorks file while its being updated in Egg.

### Greg Fryer, 2025-10-08

@Sloan Payne Our prior standard (pre egg) was to keep the PDFs on the vault. As we grew, this resulted in MANY errors as the wrong version would be referenced (B01, B02, B03, and B would all be visible, along With C01, C02, C, etc.). The interface is also slow and… unintuitive. 
Even worse, the vault cannot make the PDFs appear as a single item and only show “the production version” to some folks and “the engineering version' to others. (e.g. right now, a notional PDF in the vault for this part would ALSO show C02, not the CCB released Rev B, because that is the latest PDF that has been generated on the way to the next revision)
As such, we created egg. Generally, formal actions should ONLY occur from egg, and the Vault is only used to either audit egg, or for “Advanced operations” (whatever that ends up meaning). And as the backup for legacy data not yet published to egg.

### Sloan Payne, 2025-10-08

@Greg Fryer Understood, I think there will just need to be a process written for their interactions until the vault is gone. Also needs to be a formal announcement about this as like I said the HSV site is not functioning out of Egg.

### Eric Rinell, 2025-10-08

@Sloan Payne Egg and Vault are not linked in that way. The vault will always show the in-process or ‘working’ version. Egg will show last released version (which is currently b). Because we have engineered revision C of the air data pod assembly, the version in the vault reflects that it is in ‘Production readiness review' (PRR) state, but production will continue building to rev B until that review is complete and the assembly is released in the vault. Revision C will not be populated on the drawing until it is approved in the PRR. The PRR gives production the chance to schedule and implement changes to their procedures and understand the impact of change to existing vehicles in build and in the field. For your purposes, I suggest referencing Egg first, resorting to the vault if you need to understand what step of the release process a given component or assembly is in.

### Sloan Payne, 2025-10-08

@Eric Rinell @Nicole Hess @Ryan Forcier Okay thank you Eric. I appreciate this explanation. We will move forward with this, but more conversation may be had about this on a meeting that is set. I appreciate the support.

### Eric Rinell, 2025-10-08

@Sloan Payne My comment a few moments ago was made before I noticed this thread. Greg provided a lot of great context. I agree that training HSV on the release process is necessary.

### Eric Rinell, 2025-10-08

@Sloan Payne Sounds good. feel free to include me in the meeting if you think I can add value.

### Christa Meck, 2026-03-09

The drawing was released on 10/10/2026 as a part of https://jenaero.atlassian.net/browse/XKIT-5086.  I believe this is a duplicate.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [2121366-01.pdf](attachments/28489_2121366-01.pdf.md) | pdf | 2698 | 2025-04-25 | converted |
