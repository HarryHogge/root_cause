# VXEP-440: Add Loctite 262 to Drawings/BOMs with ODU Backshells - Deviation

- **Issue type:** Problem
- **Status:** New
- **Priority:** Low
- **Created:** 2024-02-09
- **Updated:** 2025-10-24
- **Reporter:** Matt Philley
- **Creator:** Matt Philley
- **Labels:** CCBstatus, Electronics_Drafting
- **Links:** relates to VXEP-258 (Potting concerns. DP100 may be too viscous or cure too fast to properly wick between ODU solder cups. ); relates to ENG-3339 (ECR - Add Loctite 262 to Drawings/BOMs with ODU Backshells - Deviation); relates to ENG-3366 (ECN - Add Loctite 262 to Drawings/BOMs with ODU Backshells - Deviation); relates to VA-905 (107-104993 Drawing Updates)
- **Sprint:** EE Drafting

## Description

Based on 8D #34 - ODU Connector Loose Backshell project we discovered that the ODU Installation Instructions includes direction to use loctite to secure the backshells on ODU connectors we use in the aircraft that used metal backshells.
8D Link: 8D #34 - ODU Connector Loose Backshell - WORKING FILE.pptx
Quality Alert Link: https://jenaero.sharepoint.com/:x:/r/sites/QualityTeam/Shared%20Documents/General/2%20-%20Quality%20Alerts/1%20-%20Quality%20Alert%20Storage/QA%20-%20007%20-%20ODU%20Backshell%20Potting%20Void%20Issue.xlsx?d=wcda9644dad694eb3ac1df40752db63fa&csf=1&web=1&e=EyWRlk 
This would help provide an extra feature to secure the backshell and prevent any chance of that coming loose and allowing wires inside the connector to move around (along with the potting).
ODU recommends Loctite 2701, but that is not easy to obtain and so we will use Loctite 262 (100-104074) which is readily available and already used on this program. 
Based on urgency from Production and QA to begin using this we will draft a deviation to accompany this change request to begin implementing it right away before Engineering is able to update drawings based on an agreement between Production, QA, and Electrical Engineering. 

ODU Connectors:
| Edge PN | ODU PN | Description | Backshell Size |
| 100-103070 | A10YAR-P04XFG0-0000 | ODU AMC Plug, Break Apart, Sz 0, 4p | (1B8C) 9mm |
| 100-106922 | K10YBR-P10WCD0-0000 | ODU AMC, Recept, In-Line, Sz 0, 10p (has duplicate in vault) | (1B8D) 9mm |
| 100-100877 | S10YCR-P10XCD0-0000 | ODU AMC Plug, Sty 1, Sz 0, 10p Blue | (1A10B) 7mm |
| 100-100801 | A12YAR-P26XCD0-0000 | ODU AMC Plug, Break Apart, Sz 2, 26p | (1A10A) 14mm |
| 100-100878 | S11YCR-P16XCD0-0000 | ODU AMC Plug, Sty 1, Sz 1, 16p, Blue | (1A9D) 9mm |
| 100-100798 | A10YBR-P10XCD0-0000 | ODU AMC Plug, Break Apart, Sz 0, 10p, Red | (1A5A) 9mm |
| 100-105682 | S10YBR-P04XFG0-0000 | ODU AMC Plug, Push-Pull, Sz 0, 4p, Red | (1A5D) 7mm |
| 100-109050 | G60WAM-P09WMM0-0000 | CONN, ODU AMC HD 9P FEM STD SZ0, STY 6, Brown | (6C1D) 10mm |
| 100-101417 | A10WAM-P09XMM0-0000 | ODU Plug, 9P | (1D8B) 10mm |
| 100-106471 | K12YAR-P26WCD0-0000 | AMC Recept, InLine, Sz 2, 26P, A Key | (1E7B) 14mm |
| 100-104976 | A11YAR-P16XCD0-0000 | ODU, AMC Plug, Sz 1, 16p, Brown | (1E7A) 11mm |
| 100-100797 | A10YAR-P10XCD0-0000 | ODU AMC Plug, Break Apart, Sz 0, 10p | (6B2G) 9mm |
| 100-105256 | A1AYAR-P19XCD0-0000 | ODU In Line Plug, Sz 1.5, 19p | (6B2F) 12mm |
| 100-107264 | A11YCR-P16XCD0-0000 | ODU AMC Plug, Sz 1, 16p, Blue | (6C3D) 11mm |


Effected Cables:
| PN | Description | Location |
| 115-105407 | Branch Cable Assy | Traveler Updated |
| 107-103806 | Fuselage Cable Assembly (Main System Harness) | Traveler Updated |
| 107-104993 | Fuselage Payload Harness | Traveler Updated |
| 107-102227 | ESC Signal Harness, FWD Propulsion | Nose Power Harness (107-109521) Traveler Updated |
| 107-102291 | Nose Signal Harness | Nose Power Harness (107-109521) Traveler Updated |
| 107-102238 | Servo Boost Assy, Wing Tip | Traveler Updated |
| 107-102257 | Servo Boost Assy, Horizontal | Traveler Updated |
| 107-102547-L/R | Center Wing to Boom Data Cable, Left/Right | Traveler Updated |
| 111-104977 | MAIM Harness | Traveler Updated |
| 112-105827-z | VXE30 Main Battery Checker Harness | Main Battery Checker (112-105827)  Traveler Updated |
| 112-105829-z | VXE30 Hybrid Battery Checker Harness | Hybrid Battery Checker (112-105829) Traveler Updated |
| 116-106156 | Hybrid Battery Charge Cable | Traveler Updated |
| 116-106155 | Main Battery Charge Cable | Traveler Updated |


Deviation Disposition/Instructions:
Application Instruction: 
Apply a small amount (2-3 drops) of 100-107074 Loctite 262 to the threads of the connector. Install backshell and make sure the backshell fully seats to the back of the connector. Clean any excess loctite before proceeding with the next steps.
- “Break-away” plug style ODU connector: Apply a small amount of loctite to the threads of the connector

[embedded file]
- “Push-pull” plug style ODU connector: Apply a small amount of loctite to the BACKSHELL. Applying to the connector runs the risk of loctite seeping into the push-pull collar which can cause the collar to get stuck and not function properly.

[embedded file]
 
[embedded file]

Production Instruction: 
Apply 100-104074 Loctite 262 to the backshell per the Application Instruction above. Write in “Loctite 262 on Backshell, NCR: XXXX, Lot:____ Exp:_____ ” in notes section of traveler. 

Inspection Instruction: 
- Verify “Loctite 262 on Backshell, NCR: 2478, Lot:____ Exp:_____ “ has been added to traveler with filled in traceability information
- For push-pull style connectors verify the plastic collar moves freely and loctite did not flow into the collar.

[embedded file]
- Verify the backshell is secure by attempting to unscrew the connector from the backshell in the following manner. It is recommended to use gloves available in the vending machines when performing this to reduce hand fatigue. This should be impossible to do by hand if loctite and potting were successful, so only use as much force as seems reasonable without hurting your fingers or risking damage to the connector.


[embedded file]
Acceptable:
[embedded file]

Not Acceptable:
[embedded file]

## Part Number(s)

115-105407 107-103806 107-104993 107-102227 107-102291 107-102238 107-102257 107-102547-L/R 111-104977 112-105827-z 112-105829-z 116-106156 116-106155

## Comments (21)

### Matt Philley, 2024-02-12

@Emalee Johnson do all those ODU’s have backshells?

### Emalee Johnson, 2024-02-12

@Matt Philley Yes!

### Matt Philley, 2024-02-14

@Catherine Wagner @Emalee Johnson @Brad Crampton @Cameron Chapman @Marc Richardson 
Deviation is ready for rollout. I will discuss with QA (hopefully) today. 
Deviation NCR 2478 is linked here and includes relevant info linked to this ticket
Quality Alert has been updated with another tab for “Deviation Instructions” to provide a 1-page printable summary for folks on the floor as well.

### Matt Philley, 2024-02-15

@Sloan Payne let me know when you have a few so we can go over this. 
This deviation will apply to HSV for some of the battery charger/checker cables to add loctite to the backshells.

### Sloan Payne, 2024-02-15

@Matt Philley I am available now for a call.

### Sloan Payne, 2024-02-15

@Paul Parker @Joshua McGuire and @Randall Eric Baldwin FYI.

### Matt Philley, 2024-02-21

@Emalee Johnson please review updated notes for Production and Inspection for the push-pull style connector. If you agree I will update the deviation summary page and reprint those, then train inspection.

### Emalee Johnson, 2024-02-21

@Matt Philley The updates look great, thank you for getting that completed.

### Emalee Johnson, 2024-03-04

@Matt Philley All travelers have been updated to include Loctite 262 in the operations and the material tracking table.

### Matt Philley, 2024-03-05

@Emalee Johnson awesome job! 🙂

### Matt Philley, 2024-03-06

@Brad Crampton FYSA

### Emalee Johnson, 2024-06-06

@Matt Philley Do we have a separate ticket for tracking the engineering update for all of the drawings/BOMs?

### Matt Philley, 2024-06-10

@Emalee Johnson not that I am aware of. I lost track of this one and had assumed drawings were being updated the 8D just targeted getting the deviation approved with this Jira ticket. 
Are the drawings not being updated?

### Emalee Johnson, 2024-06-10

@Matt Philley I checked the branch cable drawing and that has not been updated yet. I checked the new branch cable drawing 128-117437 and these changes have not been rolled in yet. 
Fuselage signal harness 965-1-01-1150 has not been updated
112-105829 was updated April and this change was not rolled into that drawing either. 
I checked all other PNs and none have been updated recently so I don’t think a single drawing has been updated to include this change.
Additionally the ODU termination standard 110-115262 does not have any details on loctite for the backshell.

### Catherine Wagner, 2024-06-28

@Matt Philley @Steve Stack This is a good candidate for configuration management since we’re using Loctite that is not called out and the design drawings are not updated to reflect the change. FYA @Jingle Pina

### Matt Philley, 2024-07-01

@Catherine Wagner @Steve Stack I did try to bring this up at CCB already a few weeks ago to get CM and Engineering engaged, but doesn't seem like it got any traction. 
This was intended to be a deviation to last until drawings were released though, so I think the direction still stands for Production and Inspection that Loctite is required per the evidence in this Jira and associated 8D #34

### Matt Philley, 2024-07-03

@Trevor Gronner Engineering sprint request

### Camron Richardson, 2025-02-21

@Matt Philley  Currently working on this, need states changed from ECR to EDIT to complete this ticket

### Michelle Greenwald, 2025-04-23

@Camron Richardson I just updated the procedure and traveler for 107-102065 as it was not on this list but uses the affected ODUs. Same with 2122465-01

### Christa Meck, 2025-10-24

@Camron Richardson I know you are not currently assigned to this ticket, but I saw you had asked for the drawings to be moved from [ECR]  so you can update them.  I’ve checked every part number referenced in this ticket and put information below.  Whatever drawings need to be updated and released, please make a NEW Engineering Change ticket for them so we don’t get lost in the mess of ancient linked tickets.  Lastly: If you need help getting any other items into an editable state, please reach out.
100-103070 - COTS part [shared] 
100-106922 - COTS part [shared]  
100-100877 - COTS part [shared]  
100-100801 - COTS part [shared]  
100-100878 - COTS part [shared]  
100-100798 - COTS part [shared]  
100-105682 - COTS part [shared]  
100-109050 - COTS part [shared]  
100-101417 - COTS part [shared]  
100-106471 - COTS part [shared]  
100-104976 - COTS part [shared]  
100-100797 - COTS part [shared]  
100-105256 - COTS part [shared]  
100-107264 - COTS part [shared]  
115-105407 - Moved Drawing and Assembly documents to [ME - Edit]  
107-104993 - Drawing and Assembly documents are already [released] 
107-102227 - Moved Part document to [ME - Edit] 
107-102291 - Part document already in [ME - Edit]  
107-109521 - Drawing and Assembly documents are already [released]  
107-102238 - Assembly document currently in [ME - released]  
107-102257 - Assembly document already [released]  
107-102547 - Assembly document already in [ME - Edit]  
111-104977 - Drawing and Assembly documents are already [released]  
112-105827 - Part document currently in [ME - released]  
112-105829 - Part document currently in [ME - released]  
116-106156 - Assembly document already in [ME - Edit]  
116-106155 - Assembly document currently in [ME - released]

### Christa Meck, 2025-10-24

@Camron Richardson I know you are not currently assigned to this ticket, but I saw you had asked for the drawings to be moved from [ECR]  so you can update them.  I’ve checked every part number referenced in this ticket and put information below.  Whatever drawings need to be updated and released, please make a NEW Engineering Change ticket for them so we don’t get lost in the mess of ancient linked tickets.  Lastly: If you need help getting any other items into an editable state, please reach out.
100-103070 - COTS part [shared] 
100-106922 - COTS part [shared]  
100-100877 - COTS part [shared]  
100-100801 - COTS part [shared]  
100-100878 - COTS part [shared]  
100-100798 - COTS part [shared]  
100-105682 - COTS part [shared]  
100-109050 - COTS part [shared]  
100-101417 - COTS part [shared]  
100-106471 - COTS part [shared]  
100-104976 - COTS part [shared]  
100-100797 - COTS part [shared]  
100-105256 - COTS part [shared]  
100-107264 - COTS part [shared]  
115-105407 - Moved Drawing and Assembly documents to [ME - Edit]  
107-104993 - Drawing and Assembly documents are already [released] 
107-102227 - Moved Part document to [ME - Edit] 
107-102291 - Part document already in [ME - Edit]  
107-109521 - Drawing and Assembly documents are already [released]  
107-102238 - Assembly document currently in [ME - released]  
107-102257 - Assembly document already [released]  
107-102547 - Assembly document already in [ME - Edit]  
111-104977 - Drawing and Assembly documents are already [released]  
112-105827 - Part document currently in [ME - released]  
112-105829 - Part document currently in [ME - released]  
116-106156 - Assembly document already in [ME - Edit]  
116-106155 - Assembly document currently in [ME - released]

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Connector Twist Check - Acceptable.mp4 | video | 509 | 2024-02-13 | listed only |
| Connector Twist Check - Not Acceptable.mp4 | video | 616 | 2024-02-13 | listed only |
| image-20240213-184217.png | image | 432 | 2024-02-13 | listed only |
| image-20240213-191315.png | image | 286 | 2024-02-13 | listed only |
| image-20240221-184421.png | image | 209 | 2024-02-21 | listed only |
| image-20240221-184441.png | image | 491 | 2024-02-21 | listed only |
| image-20240221-184811.png | image | 207 | 2024-02-21 | listed only |
