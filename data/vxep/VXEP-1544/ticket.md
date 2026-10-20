# VXEP-1544: BOM Validation and Release for B35/B40 WUP

- **Issue type:** Engineering Change
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-10-07
- **Updated:** 2026-04-16
- **Resolved:** 2026-04-16
- **Reporter:** Tobi Ogunro
- **Assignee:** Brendan Palmer
- **Creator:** Tobi Ogunro
- **Parent:** VXEP-1191 Mechanical - Wing Utility Pylon (FKA drop payload)
- **Links:** relates to ENG-3793 (Catalog BOM Number Initial Release: Block 35/40 Wing Utility Pylon )
- **Epic Link:** VXEP-1191
- **Other Stakeholder (as required):** Scott Stuckey

## Description

Drive full release of the Block 40 Wing Utility Pylon assembly (PN: 2123650-01) and all associated subcomponents required for production and delivery.
This effort expands beyond ME-RELEASED status and ensures all required components are fully released (ENG/ME/QA as applicable) and aligned with the latest drawing line items prior to CCB approval.
**Scope**

- Top Level Assembly:
2123650-01 - STALKER BLK40 CONFIG, WING UTILITY DROP SYSTEM
- Includes:
- All line items defined in the Block 40 WUP drawing (Sheet 1 & 2)
- All mechanical, electrical (non-EE owned), and hardware components required for a complete build


| Part Number | Description | Current State | Released |
| 2123650.SLDASM | STALKER BLK40 CONFIG, WING UTILITY DROP SYSTEM | ME-RELEASED |  |
| 2123652.SLDASM | DROP PAYLOAD, BLK 40, WITH INSERTS | ME-RELEASED |  |
| 2123652.SLDPRT (-03) | DROP PAYLOAD, 1/4 TURN, HOUSING | ME-RELEASED |  |
| 2123652.SLDPRT (-05) | DROP PAYLOAD, 1/4 TURN, HOUSING | ME-RELEASED |  |
| 2123652.SLDPRT (-54) | DROP PAYLOAD, 1/4 TURN, HOUSING | ME-RELEASED |  |
| 2127085.SLDASM | DROP SERVO MOUNT | ME-RELEASED |  |
| 2127085.SLDPRT (-51) | DROP SERVO MOUNT | ME-RELEASED |  |
| 101-115883_Maker.sldprt | WING CANISTER DROP | ME-RELEASED |  |
| 101-118067.SLDPRT | DROPPER ODU BLOCK | ME-RELEASED |  |

## Plan

Deliverables / Action Items:
Cross-check carryover PNs vs new parts.Validate all new PN entries in procurement tracker.Coordinate QA audit and release preparation.Submit CCB documentation for approval.

## Issue Status

The following items are intentionally excluded from this release scope:
- Harness Assemblies:
- 2126526-01 - Payload Port to Wing Utility Payload Board
- 2126527-01 - Payload Board to Servo
- 2126528-01 - Payload Board to Load Sensor
- 2126529-01 - Payload Board to Drop Sensor
- PCB Assembly:
- 2123638-01 - Wing Utility Board

These items will be tracked and released by the EE team.

## Comments (3)

### Tobi Ogunro, 2026-03-31

@Alfredo Macias I’ll like to push these files specified in the table to EGG.

### Alfredo Macias, 2026-04-01

Received, thanks. Could we convert this task into an engineering change (can still be structured under the parent Epic) so that it can be reviewed at CCB tomorrow? Thanks!

### Trevor Gronner, 2026-04-03

@Brendan Palmer Would you please coordinate with the tech writers to update any travelers/procedures to Revision A (or the new correct assembly revision)? If necessary, please do a sweep of the BOM in Odoo to verify it matches the rev A release from engineering. Thank you!

## Attachments (0)
