# VXEP-41: TPTR-74 VXE 510: (VTOL AP WD) Consolidated Watch Dog tracking

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-08-09
- **Updated:** 2024-08-23
- **Resolved:** 2024-08-23
- **Reporter:** Cody Smisek
- **Assignee:** David Grosher
- **Creator:** Cody Smisek
- **Labels:** 8-28-Sprint, TIQUILA-Blocker, VTOL-AP-WD, Weekly-incident-tracker
- **Links:** relates to VXEP-130 (8D #21 - VTOL AP Interface Board Conformal Coat Investigation); relates to VXEP-466 (IRAD: Unified Autopilot); blocks FS2-8 (Unified Autopilot Flight Test); relates to RMA-132 (VXE-510 230810 - Center Wing Tequila); relates to ENG-2978 (VXE 515 XComm Watchdog Triggering); relates to VA-427 (Record pins with conformal coat intrusion. Install the VTOL+AP int board from this incident into a HIL ); is blocked by FS2-806 (Embedded SW Evaluation of VTOL AP); is blocked by FS2-603 (Trace support); is duplicated by VXEP-9 ((Duplicate) TPTR-74 VXE 510 Watchdog Software Fault); is duplicated by VXEP-161 ((VTOL AP WD)VXE-499 uncommanded lift system shutdown during landing SCO flight ); relates to VXEP-11 (TPTR-5 VXE 407: (VTOL-AP-WD) Unexpected Behavior Seen During Vertical Landing); relates to VXEP-230 (Tail 499 crash during VTOL landing from 10-15', system disarm/re-arm and launch post-crash. NCR 1787)
- **Sprint:** VXE-1 EE Team Sprint 8/28-9/17
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 510
- **Incident Type:** Mission Failure/Abort
- **Severity:** 1 - Flight Critical
- **Impacted Disciplines:** Software
- **Impacted Core Subsystems:** Flight Systems

## Description

Description updated to be general WD issue. Linking other WD issues here as duplicates and canceling those. Ensure each of those gets a response once issue is addressed (or status report as needed).
Specific Incident:
510 was in fuel cell configuration with 510 centerwing.  When performing a launch wizard lift rotor check, the rear left rotor initially began to spin but stopped and system automatically disarmed. After subsequent checks, lift rotor appeared normal. Swapping centerwing to other aircraft (511 in battery configuration), lift rotor check was okay. 
Centerwing is set aside and not being flown until data analysis. 
Attached is FDR from launch wizard checks. 
>>>>>>>
Added description from duplicating issue:
During TO1 STALKER FAT, an aborted launch was caused by a software watchdog creating a failure in the autopilot. This occurred whilst the aircraft was launching off the stand, and was approximately 6inches of the ground. The aircraft fell back onto the ground and sustained minor cosmetic damage   [THIS IS WHAT THE CUSTOMER REPORTED BUT IS NOT TRUE, THE ABOVE INCIDENT WAS THE RESULT OF A BAD HLB]
During TO1 STALKER FAT, VXE 510 was performing a launch wizard lift rotor check.  When checking the rear left rotor, it initially began to spin but stopped and system automatically disarmed. After subsequent checks, the lift motor functioned normally. Preliminary analysis showed that a watchdog reset occurred.
Desired Behavior: Software Watchdog triggers are identified through root cause analysis and do not cause critical failures
>>>>>>>

## Plan

Cause 1: Continued review of driver, determine if data rate, driver structure, or prioritization are an issue.
Cause 2: Add functionality to identify when blocking occurs and what is blocked.
Cause 3: (Multiple)
- Data review to try to determine potential causes of WD.
- Embedded SW robustness review
- Build Trace Support into software
- Bring HIL online that uses (normal HIL bypasses) interface drivers.

## Issue Status

- Preliminary analysis shows a watchdog reset occurred.
- Identified SW issues (https://jenaero.sharepoint.com/:p:/r/sites/EngineeringTeam/Shared%20Documents/General/Vehicle%20Incidents/VIT2-189/WDT%20Investigation%20VIT2-189.pptx?d=w34c21ded9c1f47109895c16b0641f6f9&csf=1&web=1&e=Mqt7Mn )
- VTOL AP firmware 1.53 was the TIQUILA release candidate, so it was expected on this processor. The only change from released FW was the fix for the slow descent rate according to John.
- VTOL AP is now installed on HIL 105 and pending Test

Excluded causes:
- Conformal coat intrusion discovered on 107-107306 Interface board connector.

## Root Cause

In investigation, possibilities identified:
- Issue in sensor polling (seen in 6 of 6 watchdog cases, unclear if this is symptom or cause)
- Lower priority tasks being promoted and blocking higher priority tasks. (Function of FreeRTOS to provide determinism.)
- Other software architectural issues.

## Comments (29)

### Matt Philley, 2023-08-09

@Sam Miller @Sean Odell @Marc Richardson 
Interface board removed from AC 510 has been delivered to @John Clark (left on your keyboard) per request from @David Grosher

### Matt Philley, 2023-08-09

Ben N replaced Interface board and re-used AC510 VTOL AP board. Kyle E is re-installing it into AC 510 Centerwing. It has an updated traveler packet indicating the QA inspection points for conformal coat inspection. 
NOTE: Ben N noted the AP Firmware version installed is a later version than what he installs in the shop, so @Carson Buckley will need to verify that when it gets back to SCO

### Matt Philley, 2023-08-09

Avionics Board Assy with replaced Interface board installed in AC510 centerwing.
Chris E performed the pre-close inspection documented in the inspection call
Sam M gave it a look as well before taping the cover shut.
Sam M took possession to drive the wing out to SMR to complete Qty 3 test flights with the rest of the AC510 aircraft.
@Sean Odell @Marc Richardson FYI

### Cameron Chapman, 2023-08-09

@Matt Philley did anyone record which pins were suspected contaminated on those connectors? If not, we can inspect and report. @Former user is this something you could help with?

### Matt Philley, 2023-08-09

@Cameron Chapman we did not record specific pins. Board is with John Clark if we want to track that down.

### Cameron Chapman, 2023-08-09

Dave G said we don't know that WDs can't be caused by hardware, so we may want to hold the 510 flight and quarantine the AP board. He is calling Sam now.

### John Clark, 2023-08-09

@Cameron Chapman I will need some of @Mark Squillante 's time to install AC 510 Interface Board in HIL 101. Copying @David Grosher

### David Grosher, 2023-08-09

@Cameron Chapman My understanding is that the offending VTOL board will also be swapped. I would like to have it installed in the same HIL as well.  The goal is to recreate WD events if possible. Thanks.

### Matt Philley, 2023-08-10

510 centerwing was returned to SLO Final Assy last night
The full Avionics Board Assy (SN APB-1-1288) was removed by Sam M working with Ben N
Ben N assigned a brand new Avionics Board Assy (New AP and Interface Board, SN APC-1-1374) which was temporarily installed last night
The installation was completed this morning by Kyle E and inspected by Chris E. The paperwork for the new Avionics Board Assy was added to the AC510 vehicle packet.
AC 510 centerwing handed off to Artis with plan to flight test at SMR today.

The removed Avionics Board Assy SN APB-1-1288 has been given an RMA tag and will br dropped off to @Sean Odell for a moment until we can make sure we are all coordinated.

### Cameron Chapman, 2023-08-10

Sounds good to both. I agree, the ap and int boards should be paired in the Hil and a new set installed in the aircraft. 
@Mark Squillante can you please ask @Former user if he’s available to inspect these boards, record which pins have conformal coat intrusion, then you can help install them in a Hil? We can save the current Hil boards for a future Hil.

### Matt Philley, 2023-08-10

(For lack of a better location for notes) 
AC 509 and AC 511 centerwings were also brought back to SLO Final Assy and found to have conformal coat in the same connectors on the interface board.
They were removed from the centerwing
New avionics board assemblies have been prepared. We are working on installing those. 
@Marc Richardson @Desiray Johnston @Sam Miller

### Matt Philley, 2023-08-10

“Original” Avionics Board Assy from 510 was handed off to @Cameron Chapman in our meeting this morning.
The Replacement Avionics Board Assy SN APC-1-1375 (Corrected 8/10/23) did NOT PASS SCO checkout and Carson reported he could not connect to the autopilot. 
Decision was made to swap Avionics Board Assy again. SN APC-1-1378 was installed and AC 510 has been inspected and handed back to SCO for checkout.

### Matt Philley, 2023-08-11

For recordkeeping… based on the conformal coat investigation the Avionics Board Assy was swapped once more in AC 510. The current SN of Avionics Board Assy is as follows:
APB-1-1365
The aircraft is currently undergoing SCO config and checkout with plan to drive it to SMR ASAP for test flight and I believe Customer handoff.

### Cameron Chapman, 2023-08-13

The avionics board assembly from this incident was installed in one of @John ClarkHILs and the board was marked with this incident number. They are trying to determine the cause and recreate the WD reset. @Mark Squillante, can you please confirm the board was labeled and record which HIL sn it was installed into?

### Mark Squillante, 2023-08-14

Red AP processor board (1409P01D; 107-107307) SN APB-1-1288 paired with interface board (1901P01B; 107-107306) SN VAPI-1-1123 will be going into HIL box SN S-S100044 (HIL PN: 107-111759). I have not had time to install this yet due to https://jenaero.atlassian.net/browse/ENG-2207 taking higher priority but will install it as soon as possible.

### Mark Squillante, 2023-08-14

I finished swapping out the red AP processor board on HIL box SN S-S100044 and put on @John Clark's desk. 
@Cameron Chapman

### Cameron Chapman, 2023-08-24

Linking subtasks to parent

### Cameron Chapman, 2023-08-24

@John Clark @David Grosher What is the main WD troubleshooting issue? Can you please link it to this one?

### Greg Fryer, 2023-08-30

All - I have moved this over to VXEP where it should be, and I am canceling VXEP9 which duplicates it. This had more info and links, so kept it.
@David Grosher I also added the blocking links to your Epics as discussed.

### Greg Fryer, 2023-09-11

@Scott Hunter @John Clark @David Grosher @Kurt Burian 
Please review the root cause related fields of this issue, I am using it as the “master summary” of the WD issue(s) and status. I will point other known/suspected WD issues here, to avoid duplication.

### Matt Philley, 2023-08-10

“Original” Avionics Board Assy from 510 was handed off to @Cameron Chapman in our meeting this morning.
The Replacement Avionics Board Assy SN APC-1-1375 (Corrected 8/10/23) did NOT PASS SCO checkout and Carson reported he could not connect to the autopilot. 
Decision was made to swap Avionics Board Assy again. SN APC-1-1378 was installed and AC 510 has been inspected and handed back to SCO for checkout.

### Matt Philley, 2023-08-11

For recordkeeping… based on the conformal coat investigation the Avionics Board Assy was swapped once more in AC 510. The current SN of Avionics Board Assy is as follows:
APB-1-1365
The aircraft is currently undergoing SCO config and checkout with plan to drive it to SMR ASAP for test flight and I believe Customer handoff.

### Cameron Chapman, 2023-08-13

The avionics board assembly from this incident was installed in one of @John ClarkHILs and the board was marked with this incident number. They are trying to determine the cause and recreate the WD reset. @Mark Squillante, can you please confirm the board was labeled and record which HIL sn it was installed into?

### Mark Squillante, 2023-08-14

Red AP processor board (1409P01D; 107-107307) SN APB-1-1288 paired with interface board (1901P01B; 107-107306) SN VAPI-1-1123 will be going into HIL box SN S-S100044 (HIL PN: 107-111759). I have not had time to install this yet due to https://jenaero.atlassian.net/browse/ENG-2207 taking higher priority but will install it as soon as possible.

### Mark Squillante, 2023-08-14

I finished swapping out the red AP processor board on HIL box SN S-S100044 and put on @John Clark's desk. 
@Cameron Chapman

### Cameron Chapman, 2023-08-24

Linking subtasks to parent

### Cameron Chapman, 2023-08-24

@John Clark @David Grosher What is the main WD troubleshooting issue? Can you please link it to this one?

### Greg Fryer, 2023-08-30

All - I have moved this over to VXEP where it should be, and I am canceling VXEP9 which duplicates it. This had more info and links, so kept it.
@David Grosher I also added the blocking links to your Epics as discussed.

### Greg Fryer, 2023-09-11

@Scott Hunter @John Clark @David Grosher @Kurt Burian 
Please review the root cause related fields of this issue, I am using it as the “master summary” of the WD issue(s) and status. I will point other known/suspected WD issues here, to avoid duplication.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [AC 510 VTOL AP Board Investigation - MP 23.08.09.pptx](attachments/15766_AC%20510%20VTOL%20AP%20Board%20Investigation%20-%20MP%2023.08.09.pptx.md) | pptx | 7279 | 2023-08-09 | converted |
| IMG_1346.mov | video | 19598 | 2023-08-09 | listed only |
| T95_V510_230809_092808_pack.zip | archive | 669 | 2023-08-09 | listed only |
