# VXEP-467: Red AP board 1409P01D in avionics box

- **Issue type:** Sub-task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2023-04-20
- **Updated:** 2025-05-05
- **Resolved:** 2025-05-05
- **Reporter:** Cameron Chapman
- **Assignee:** Maxime Jeanneau
- **Creator:** Cameron Chapman
- **Parent:** VXEP-466 IRAD: Unified Autopilot
- **Links:** relates to ENG-1525 (Avionics Graphic for XCOM Board)

## Description

@Maxime Jeanneau, can you please create a multiboard schematic of the following boards connected together? To do so, you will likley need to rebuild the projects in the vault, then change the part type of the connectors to “connector”.
Mount 1409P01D PIC32MZ Autopilot
to this board: 1809P01A-AP Adapter Board
Which then connects via ribbon cable to this board 1607P01A, XE240 Block 25 Power Comms
See 965-1-01-3100 XE25 Avionics Enclosure, WD.SchDoc.
Essentially, The top two boards replace the 000 AP. 
Save to here (I already started some files) https://jenaero.sharepoint.com/:f:/r/sites/IRAD/Shared%20Documents/General/Projects/Autopilot_Unified?csf=1&web=1&e=bnf3u0 
You can work will @Mark Squillante/teach multiboard schematics if you don’t have enough bandwidth to complete this.
Once the schematic is complete, we want to document cables to connect the the transponder connector CAN and etherenet lines to the red AP, then splice CAN and connect another AP ethernet port to the transponder port on the avionics box.

## Comments (9)

### Maxime Jeanneau, 2023-04-20

So far have the Multi Board Schematic up and connected, note doted lines are b2b connections, solid ribbon cable. File is saved to One Drive.
[embedded file]
Awaiting extra information for the transponder/ethernet additions.

### Maxime Jeanneau, 2023-04-20

Ribbon cable to access “Sightline” Ethernet port on XCOM board: HLCD-20-01.72-TR-TR-1 Samtec Inc. | Cable Assemblies | DigiKey

### Cameron Chapman, 2023-04-21

0.02” 38AWG coax cable, ouch. Any creative ideas to connect that to a 4 pin DF13? Adapter PCB/flex PCB?
@Kurt Burian , would you rather use an easier to connect port like the bulgin or transponder for initial testing, then have us develop another solution to keep the original ports for the future solution?
The best longer term option may be to update the carrier board to add a switch and additional ethernet connectors (like the CW interface board). Created https://jenaero.atlassian.net/browse/ENG-1509

### Kurt Burian, 2023-04-24

@Cameron Chapman Is this my unified AP project? Please come talk to me, I know what I want done and we have not started this work yet. We were scheduling when I asked you for a time estimate to do the work. That has been submitted.

### Maxime Jeanneau, 2023-04-25

@Kurt Burian I started gathering all the connector pinout information on one sheet as an interconnect drawing, I still have a bit of work to do. Plan is to validate that all necessary connections can be achieved and start planning out what wiring harnesses or board modifications are needed. 
Would like to collaborate with you on this project, maybe we can tag up and discuss where we’re at.

### Kurt Burian, 2023-04-25

@Maxime Jeanneau we aren't starting the electrical work on this for a few months. I can tell you where and what I want connected next time we chat, but this has not started so I can focus on the software that's needed for this project first. There already is a Jira for it.

### Kurt Burian, 2023-04-25

@Maxime Jeanneau Antenna rollout is what I need now, not this

### Kurt Burian, 2023-04-25

@John Clark can you please close the loop on this miscommunication with Cameron.

### John Clark, 2023-04-25

@Kurt Burian no problem. @Cameron Chapman I’ll take SWE point on this one. Kurt is involved in Unified AP. Right now we are just trying to scope time.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| step1.PNG | image | 368 | 2023-04-20 | listed only |
