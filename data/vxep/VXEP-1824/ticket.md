# VXEP-1824: Initial Release of Processed PCB Left/Right Configurations and Associated Wing Utility PCB Harnesses for Wing Utility Pylon (2123650)

- **Issue type:** Engineering Change
- **Status:** NOT Moved to Solidworks Manage
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2026-04-08
- **Updated:** 2026-09-26
- **Resolved:** 2026-08-15
- **Due:** 2026-06-19
- **Reporter:** Tobi Ogunro
- **Assignee:** Brendan Palmer
- **Creator:** Tobi Ogunro
- **Labels:** NotMovedToSWM, ReviewedAndReadyForCCB
- **Parent:** VXEP-1191 Mechanical - Wing Utility Pylon (FKA drop payload)
- **Links:** relates to ENG-3931 (VXE35/40 Wing Utility Pylon Board Firmware)
- **Epic Link:** VXEP-1191
- **Engineering Change Level:** Level 0 - Scope of change is obvious to assigned engineer
- **Key Stakeholder(s):** Brendan Palmer, Connor Peebles, Greg Fryer

## Description

Reason for Change: The Wing Utility Pylon now requires left and right configuration control due to location-agnostic software not being available for current builds.
The PCB (2123638) is currently common, but once processed and installed into the pylon assembly, it must support left/right identification to ensure correct installation and system behavior.

Description of Change: Define processed PCB configurations:
- 2135491-01 → Left PCB
- 2135491-02 → Right PCB

- No change to raw PCB design (2123638 base remains unchanged)

Release supporting PCB harness assemblies required for integration and validation of the processed PCB configurations:
2126526-01 → Payload Port to Wing Utility Payload Board
2126527-01 → Wing Utility Payload Board to Payload Servo
2126528-01 → Wing Utility Payload Board to Load Sensor
2126529-01 → Wing Utility Payload Board to Drop Sensor

Affected Item(s):  
- 2123650-01 - Wing Utility Pylon (Left)
- 2123650-02 - Wing Utility Pylon (Right)
- 2123638-01 - Wing Utility PCB (Base)
- 2135491-01 - Wing Utility PCB (Left, Processed)
- 2135491-02 - Wing Utility PCB (Right, Processed)
- 2126526-01 - Payload Port to Wing Utility Payload Board Harness
- 2126527-01 - Wing Utility Payload Board to Payload Servo Harness
- 2126528-01 - Wing Utility Payload Board to Load Sensor Harness
- 2126529-01 - Wing Utility Payload Board to Drop Sensor Harness

| BOM | Description | Release Status |
| 2135491-01 | Wing Utility PCB — Left (Processed) | Pending CCB |
| 2135491-02 | Wing Utility PCB — Right (Processed) | Pending CCB |
| 2126526-01 | PAYLOAD PORT TO WING UTILITY PAYLOAD BOARD | Pending CCB |
| 2126527-01 | WING UTILITY PAYLOAD BOARD TO PAYLOAD SERVO | Pending CCB |
| 2126529-01 | WING UTILITY PAYLOAD BOARD TO DROP SENSOR | Pending CCB |
| 2126528-01 | WING UTILITY PAYLOAD BOARD TO LOAD SENSOR | Pending CCB |

## Comments (12)

### Tobi Ogunro, 2026-04-14

@Sanjay Menon & @William Doupis This says EE released. Do we still need to push to CCB so it can go on EGG?

### Sanjay Menon, 2026-04-14

@Tobi Ogunro @Connor Peebles  Still need a processed PCB BOM for release

### Jeremy White, 2026-04-15

@Tobi Ogunro Are these the new pylons? If they haven’t been delivered to customers, any CCB determination would likely be made outside of the PMO.

### Tobi Ogunro, 2026-04-16

@Jeremy White Yes these are for the new pylons. This ticket is specifically for the PCB board.

### Tobi Ogunro, 2026-04-21

@Connor Peebles Let’s get this released this week. 🙂

### Tobi Ogunro, 2026-05-14

@Connor Peebles Did this get released?

### Connor Peebles, 2026-05-14

@Tobi Ogunro Not yet

### Connor Peebles, 2026-05-19

@Tobi Ogunro@Sanjay Menon  Released to:
"C:\JAI Vault 1\projects\129 - lrr\electrical design\pcb\2123638-01 Wing Utility Board\2135491-01.xlsx"
"C:\JAI Vault 1\projects\129 - lrr\electrical design\pcb\2123638-01 Wing Utility Board\2135491-02.xlsx"

### Jamie Davies, 2026-06-19

does not affect QTY’s

### Trevor Gronner, 2026-06-24

@Sloan Payne @Michael Cooper @Savannah Gilbert FYSA, utility pylon changes just got pushed to implementing. I think this will be relevant for HSV.

### Trevor Gronner, 2026-06-24

@Brendan Palmer @Michelle Greenwald FYSA, passing this utility pylon change ticket to you two. Sorry if you’ve already implemented these changes.

### Christa Meck, 2026-08-15

This Engineering Change was not actioned before the switch to Solidworks Manage.  If you wish to proceed with this change, open an ECR in Solidworks Manage.

## Attachments (0)
