# VXEP-637: VXE 401 loss of control, aircraft flying in loops

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-09-17
- **Updated:** 2026-09-14
- **Resolved:** 2024-12-10
- **Reporter:** Pat Wells
- **Assignee:** Eric Brewer
- **Creator:** Pat Wells
- **Labels:** FlightSystems, Hardware, INA, No_crash, PMA263
- **Links:** relates to RMA-356 (VXE-401  240923-3); relates to VXEP-414 (VXE 468 crash after transition to forward flight)
- **Customer:** PMA263
- **Vehicle Tail Number:** 401
- **Root Cause:** IMU data from FWAP is frozen, either due to hardware or software fault on the FWAP.  See report here.
- **Incident Type:** Near Miss
- **Severity:** 1 - Flight Critical

## Description

Relevant Files: https://jenaero.sharepoint.com/sites/FlightSafety/Shared%20Documents/Forms/AllItems.aspx?csf=1&web=1&e=dp79vR&CID=d8f1cb48%2D3366%2D403b%2Db278%2D98a1b6cdc45c&FolderCTID=0x012000D03119522A011A40817D7F0F59E3A7EF&id=%2Fsites%2FFlightSafety%2FShared%20Documents%2FIncident%20Reports%2FVXEP%2D637%2DVXE%20401%20loss%20of%20control%2C%20aircraft%20flying%20in%20loops&viewid=7181a7a2%2Dd286%2D47c9%2Dbdd3%2D9195ef18282c 
Statement from operator:
Flying out at CPEN today and about 35 minutes into flight the aircraft lost control and started doing loops, yes upside down. It did this uncontrollably for about 20 seconds and lost altitude to about 300 or so feet. We commanded a land immediately then aborted once we realized we were over water. We took manual control and were able to get it over the beach and restart the VTOL landing. No damage to the aircraft other than broken VTOL prop when it was upside down and land immediately was commanded.
Also wanted to add, 49.7 lbs.
Landing,climb,cruise speed set to 53,54,55
VTOL set to 6FPS on ascent.

AAR attached, missing VTOL data.  Working with customer to obtain VTOL data.

* 09/17/2024 Update. Customer stated that elevator servo started binding and was curious if servo current is logged anywhere.

## Corrective Action

While the VXE30 fixed-wing autopilot has seen many reliability improvements over its 20 years of service, the Group 2 system consists of several single-string system hardware elements that can fail. Because of this, there are limited corrective actions for this type of failure.  Per the manual emergency procedures for the departure of controlled fixed-wing flight, the operator may attempt a VTOL land immediately command and nudge or manually guide the vehicle to a clearing on the ground.  Additionally, Edge Autonomy will use mishap information like this to shape future technology refreshes and add redundancy and reliability where practical.

## Plan

Updated 10/17/24
- Ask Software to diagnose connection issue and pull any data that they can

## Issue Status

Updated 10/17/24
- FW AP has been removed and vehicle was sent back Sean to add a replacement.
- FW AP is currently with ENG

## Comments (37)

### Cameron Chapman, 2024-10-08

@Adrian Garcia please do not reconfigure any of those boards until approved. We do not want to wipe a configuration that could be useful. Please coordinate with a SW engineer to see if they can diagnose the connection issues or if they want to pull any information. @David Grosher who is the best person to help with this?

### Sean Odell, 2024-10-15

@David Grosher Recently found out, from the customer, that this aircraft is needed back for a demo in December. Does your team still need the physical aircraft or can I take from engineering and start repairs?
@Pat Wells FYI

### David Grosher, 2024-10-15

@Sean Odell Please replace the FW AP and leave the board with us. 
@Adrian Garcia @Cameron Chapman @Eric Brewer FYSA

### Pat Wells, 2024-11-07

@Sean Odell has the FW AP been delivered back to engineering as requested?

### Sean Odell, 2024-11-07

@Pat Wells I had engineering take the FW AP before I took the aircraft back. I believe @Adrian Garcia is the one who removed it before bringing 401 to RMA.

### Desiray Johnston, 2024-11-13

@Kyle England please remove FW AP and bring to me. @Sean Odell quote needs to be updated as it does not say to replace FW AP.

### Emalee Johnson, 2024-11-13

@Cameron Chapman @Adrian Garcia @David Grosher Is your team doing an investigation on a Red AP (107-101161) already? @Kyle England said this center wing is still sealed so I want to make sure you guys have the right material. @Sean Odell FYI

### Emalee Johnson, 2024-11-13

@Cameron Chapman @Adrian Garcia @David Grosher  Apologies for my confusion, we just pulled the VTOL AP (107-101161) out of the center wing for rework to get an industrial SD card. To confirm engineering has the Green AP (965-1-01-2004) from the avionics box for investigation and we are not to use any part of the current Avionics Box (107-111718), we are replacing the entire assembly? @Desiray Johnston @Kyle England @Sean Odell

### Adrian Garcia, 2024-11-13

@Emalee Johnson The green AP is at my workbench

### Adrian Garcia, 2024-11-13

@Emalee Johnson from my understanding the Green AP was just going to be replaced and the XCOMM was okay to use. Im not sure if that changed however.

### Cameron Chapman, 2024-11-14

Per@David Grosher request below, after quarantining the FWAP the rest of the Avbox should be ok to use. 
@David Grosher @Eric Brewer could anything on the XCOM or rest of the aircraft be causing the IMU to freeze up, or can we say it is very likely due to something on the FWAP? 
If the FWAP, the rest of the box should be ok to reuse. 
@Desiray Johnston @Kyle England @Sean Odell@Emalee Johnson

### Eric Brewer, 2024-11-14

@Cameron Chapman @David Grosher It is very likely due to the FWAP which contains the sensors and the boards that read the sensors.

### Emalee Johnson, 2024-11-14

@Cameron Chapman The way we received the avionics box back was deemed a risk by quality so we are issuing a full replacement. The XCOMM was not secured in the enclosure so we don’t know if there was any damage caused by the board bouncing around. Final Assembly flagged it because there was significant rattling in the enclosure. 
@Desiray Johnston @Kyle England @Sean Odell @David Grosher

### Eric Brewer, 2024-12-06

@Pat Wells is there anything remaining to investigate here or can this be closed?
@David Grosher FYI.

### Pat Wells, 2024-12-06

@Eric Brewer from my position I don’t have any remaining requirements. The aircraft has already been repaired and returned to the customer.
It looks like there are no suggested corrective actions that have came from the items that were investigated.

### Alexander Alan Arnold, 2024-12-10

@David Grosher Is this potentially ready to close out?

### David Grosher, 2024-12-10

@Alexander Alan Arnold  Yes, I believe so. We wouldn’t address this until we had the UAP completed in 2026. @Eric Brewer thoughts?

### Eric Brewer, 2024-12-10

@David Grosher @Alexander Alan Arnold agreed.  This is the first and only incident I’ve seen with this failure mode, so it seems reasonable to wait to address until UAP unless we see a significant uptick in this type of failure.

### Alexander Alan Arnold, 2024-12-10

I will move it to D8 and update the tracker unless there are any objections? @David Grosher @Pat Wells @Eric Brewer

### Eric Brewer, 2025-02-28

@David Grosher @Pat Wells created report here. VXE401_BarrelRolls.pptx

### Pat Wells, 2024-11-07

@Sean Odell has the FW AP been delivered back to engineering as requested?

### Sean Odell, 2024-11-07

@Pat Wells I had engineering take the FW AP before I took the aircraft back. I believe @Adrian Garcia is the one who removed it before bringing 401 to RMA.

### Desiray Johnston, 2024-11-13

@Kyle England please remove FW AP and bring to me. @Sean Odell quote needs to be updated as it does not say to replace FW AP.

### Emalee Johnson, 2024-11-13

@Cameron Chapman @Adrian Garcia @David Grosher Is your team doing an investigation on a Red AP (107-101161) already? @Kyle England said this center wing is still sealed so I want to make sure you guys have the right material. @Sean Odell FYI

### Emalee Johnson, 2024-11-13

@Cameron Chapman @Adrian Garcia @David Grosher  Apologies for my confusion, we just pulled the VTOL AP (107-101161) out of the center wing for rework to get an industrial SD card. To confirm engineering has the Green AP (965-1-01-2004) from the avionics box for investigation and we are not to use any part of the current Avionics Box (107-111718), we are replacing the entire assembly? @Desiray Johnston @Kyle England @Sean Odell

### Adrian Garcia, 2024-11-13

@Emalee Johnson The green AP is at my workbench

### Adrian Garcia, 2024-11-13

@Emalee Johnson from my understanding the Green AP was just going to be replaced and the XCOMM was okay to use. Im not sure if that changed however.

### Cameron Chapman, 2024-11-14

Per@David Grosher request below, after quarantining the FWAP the rest of the Avbox should be ok to use. 
@David Grosher @Eric Brewer could anything on the XCOM or rest of the aircraft be causing the IMU to freeze up, or can we say it is very likely due to something on the FWAP? 
If the FWAP, the rest of the box should be ok to reuse. 
@Desiray Johnston @Kyle England @Sean Odell@Emalee Johnson

### Eric Brewer, 2024-11-14

@Cameron Chapman @David Grosher It is very likely due to the FWAP which contains the sensors and the boards that read the sensors.

### Emalee Johnson, 2024-11-14

@Cameron Chapman The way we received the avionics box back was deemed a risk by quality so we are issuing a full replacement. The XCOMM was not secured in the enclosure so we don’t know if there was any damage caused by the board bouncing around. Final Assembly flagged it because there was significant rattling in the enclosure. 
@Desiray Johnston @Kyle England @Sean Odell @David Grosher

### Eric Brewer, 2024-12-06

@Pat Wells is there anything remaining to investigate here or can this be closed?
@David Grosher FYI.

### Pat Wells, 2024-12-06

@Eric Brewer from my position I don’t have any remaining requirements. The aircraft has already been repaired and returned to the customer.
It looks like there are no suggested corrective actions that have came from the items that were investigated.

### Alexander Alan Arnold, 2024-12-10

@David Grosher Is this potentially ready to close out?

### David Grosher, 2024-12-10

@Alexander Alan Arnold  Yes, I believe so. We wouldn’t address this until we had the UAP completed in 2026. @Eric Brewer thoughts?

### Eric Brewer, 2024-12-10

@David Grosher @Alexander Alan Arnold agreed.  This is the first and only incident I’ve seen with this failure mode, so it seems reasonable to wait to address until UAP unless we see a significant uptick in this type of failure.

### Alexander Alan Arnold, 2024-12-10

I will move it to D8 and update the tracker unless there are any objections? @David Grosher @Pat Wells @Eric Brewer

### Eric Brewer, 2025-02-28

@David Grosher @Pat Wells created report here. VXE401_BarrelRolls.pptx

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Log.png | image | 35 | 2024-09-17 | listed only |
| T95_V401_240916_141756_pack.zip | archive | 1115 | 2024-09-17 | listed only |
| image-20240917-160002.png | image | 71 | 2024-09-17 | listed only |
| VTOL_VXE401.zip | archive | 26729 | 2024-09-19 | listed only |
