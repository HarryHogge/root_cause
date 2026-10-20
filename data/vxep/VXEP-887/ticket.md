# VXEP-887: Create, Test, and Release B40 Wing Utility Pylon (FKA drop payload) PN: 2123650-01

- **Issue type:** Major Project
- **Status:** In Process
- **Priority:** Medium
- **Created:** 2025-01-08
- **Updated:** 2026-05-27
- **Reporter:** Cameron Chapman
- **Assignee:** Tobi Ogunro
- **Creator:** Cameron Chapman
- **Parent:** VXEP-434 Wing Utility Drop & Integration of ESAD/Fires support
- **Links:** relates to XKIT-3487 (Design SB40 Center Wing Distribution Board (Ethernet plus power switching)); relates to XKIT-3266 (Should Drop Payload controller use ethernet or CAN? ); relates to FS2-655 (VXE30 X-Kit - Drop Payload); relates to FS2-2799 (Utility Pylons (Previously Payload Droppers))

## Description

Sharepoint IRAD - B35 Wing Utility Pylon - All Documents
Requirements: B35 Wing Utility Pylon, Compliance Matrix.xlsx
### Requirement Summary


- see requirements Compliance Matrix above


Wing Pylon Part Comparison – No Munition vs Blindmate

| Component | No Munition PN | Blindmate PN | Comparison |
| Electronic Board | 2119594-01 | 2119594-01 | Same |
| Housing | 2119649-01 | 2119649-01 | Same |
| Lever Cap | 2119649-05 | 101-117759-05 | PN update (same part - keep 2119649) |
| Lever Arm | 2119649-04 | 101-117759-04 | PN update (same part - keep 2119649) |
| Servo Assy | 2119719-01 | TBD (carryover) | Same (PN TBD in Blindmate) |
| Bag of Latches | 2118761-01 | 2118761-01 | Same |
| Consumable Spares | 101-117687-01 | 101-117687-01 | Same |
| Transit Case | 2117820-01 | 2121932-01 | Different PN, same function |
| System Assembly | 101-115866-01 | 101-117757-01 | Different assembly |
| Drop Kit | 2118737-01 (500-117326) | 2121930-01 (500-2121525-01) | Different kit version |
| Harnesses/PCB | 126-116212-02 / 101-118005-01/02 / 126-117433-01 / 101-118007-01/02 / 2122094-01 | 212512-01 / 2122437-01 / 2122438-01 / 2122439-01 | Different harness sets |
| Control Unit | — | 2122640-01 | New in Blindmate |
| Enclosures | — | 2122646-01 / 2122646-02 | New in Blindmate |

Summary of Part Comparison (No Munition vs Blindmate):
Most core components remain unchanged (housing, lever cap/arm, servo, bag of latches, consumables, electronic board). Some parts have PN updates but are functionally the same. Key differences are in the harness/PCB sets, system assembly, and drop kit (STND vs Havoc/LRR). Blindmate also introduces new parts (control unit and enclosures). See table above for full mapping.

## Project Deliverables

An independent Wing Utility Pylon that does not need external commands from the old XE25 dropper box and payload dropper PCB. This pylon will interface with the new B35/ B40 inboard and outboard wing utility locations.
Independent Wing Utility Pylon (PN: 2123650) compatible with B35/B40 inboard + outboard wing stations.
Full CAN/Ethernet control (remove legacy XE25 PCB dependency).
Payload dropper integration with latch wiring.
Meet compliance matrix requirements (capacity, accuracy, electrical/software/GCS interface, MTBF, safety/lockouts).
Deliver 2 units to Sweden by 12/31/25.

## Comments (7)

### Scott Whitney, 2025-01-10

@Cameron Chapman  - I do not believe John C has any work for Havoc Utility Drop. If he does, it would be new news for me

### Cameron Chapman, 2025-01-10

@Scott Whitney Here is what he and Dave described. 
Havoc wing drop controller(FKA version 3) desired feature additions.
- EA (John ClarK):
- Get current firmware working and rebuilt in modern IDE @John Clark
- Ability to update firmware.
- Ability to update parameters. Ask Dave.
- TBD is EA or TT adds these features.
- Features 3 positions to be commanded. 
- i.     Safety: Slews servo to a point where it cannot be manually be released by hand. To exit safety, operator commands to load. (not currently an option). Ensure default/startup commanding defaults to safety.
Load/Armed: Able to load dropped item or ready to mechanically drop. Currently 800PWM. This should be default position for this mode.
Drop: Drops projectile. Returns to load after dropping. Currently 2200 PWM. This should be default position for this mode.
- Process dropper sensor data on board. Display status on GUI.
- Eventually add more detailed algorithms for wind, different masses of payloads (parachutes, inert rounds, etc).

### Connor Peebles, 2025-04-07

@John Clark Let me know when you have your parts selected, then we'll make a block diagram and a statement of work for our outsourcing PCB

### John Clark, 2025-04-07

@Connor Peebles currently we have Doc Number 0716P01 Drop Payload Board and my provided Ethernet PICtail Plus schemo 03-01898. That needs to be combined per design into a single board. I can provide a mark-up schematic for the routing. Let me know?

### Connor Peebles, 2025-04-08

@John Clark Please do, I’ll schedule a meeting to talk the broader picture as well

### Tobi Ogunro, 2026-02-27

@Alfredo Macias Can you drop the Catalog number here?

### Connor Peebles, 2026-03-12

moved any requirements from this Jira into B40 Wing Utility Pylon, Compliance Matrix.xlsx

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20260227-203739.png | image | 1 | 2026-02-27 | listed only |
