# VXEP-470: Unified AP for Block 40

- **Issue type:** Major Project
- **Status:** In Process
- **Priority:** Highest
- **Created:** 2023-04-10
- **Updated:** 2026-09-17
- **Due:** 2026-08-31
- **Reporter:** Kurt Burian
- **Assignee:** David Grosher
- **Creator:** Kurt Burian
- **Labels:** valid
- **Parent:** VXEP-466 IRAD: Unified Autopilot
- **Links:** relates to ENG-1752 (1409P01D VTOL AP improvements); relates to ENG-1774 (Replace obsolete MPU-9250 accelerometer (FW AP and ADP). ); relates to FS2-252 (Unified Autopilot non-MVP features); relates to FS2-3831 (ADP to support UAP); relates to VXEP-466 (IRAD: Unified Autopilot)
- **Project Tier:** Tier 3
- **Planned Milestone(s):** Preliminary Design Review (PDR), Detailed Design/Critical Design Review (CDR)
- **Project Folder Link (Sharepoint):** https://jenaero.sharepoint.com/:f:/s/IRAD/EtG227nEnnhPsusNICXhIy4BLj7incPZB4-Ij9mjfdJVlA?e=3uaPae
- **Design Plan Link:** https://jenaero.sharepoint.com/:x:/s/IRAD/IQBrEBAf_FWeTZXts1rTiRbgAUuFxDzr8mtWxQUs2tfcexg?e=NJl5qD
- **Charter Link:** https://jenaero.atlassian.net/wiki/x/FYCmMg
- **Program (Marquee):** Unified Auto Pilot
- **Job Number:** J100065 - Autopilot Unified

## Description

Project Pages
| B41 Charter | https://jenaero.atlassian.net/wiki/spaces/SEIT/pages/849772565/Project+Charter+-+Unified+Autopilot+UAP+Phase+1+Block+40 |
| Project Charter - ADP Upgrade for UAP | https://jenaero.atlassian.net/wiki/spaces/SEIT/pages/886210689/Project+Charter+-+ADP+Upgrade+for+UAP |
| B41 JIRA | https://jenaero.atlassian.net/browse/VXEP-470 |
| FW confluence page | Blk 40 UAP Dev (Internal Release Only) - VXE Aircraft - Confluence |

Design Pages
| Architecture Diagram | System Architecture Diagram, UAP.vsdx |
| Project Files Sharepoint: | Autopilot_Unified |
| Altium 365 | TBD |


(Seems Old) Critical Task List: UAP Critical Tasks.xlsx

Deliverables:
- Software Release version 7.0.0
- What Vehicle configuration will be supported in 7.0.0??
- FWAP and VTOL AP running together on the VTOL AP board,
- communicating over a virtual Ethernet local host
- Vehicle configurations supported?
- Backward compatibility?
- 

Resources:
- GNC/Flight Science - validate tuning
- flight data review and analysis
- Speedgoat support (Everett? and electrical)
- Electrical development setup? (may not be needed)
- build up X-Plane HIL for UAP
- Inventory of VTOL and FWAP I/O (IMPORTANT - need asap)
- BLK 45 Vehicles
- Avionics:
- Mechanical
- Electrical
- CenterWing
- Flight Data Analysis
- GNC
- Electrical
- Mechanical

Avionics Software Milestones:
- Start Date 8/18
- Target Date for Dev Complete 12/31
- Vehicle Configuration
- Vehicle type - 145 (UAP)?
- Rebasing to 6.5.0
- XCOMM - 2 weeks (move from Serial Port to CAN port)
- VTOL - 3 weeks
- FWAP - 6 weeks
- Currently 6.2.1
- HIL Flight Verification after rebasing 6.5.0
- Speedgoat buildup time (2-months)
- XPlane (will work after rebase)
- Rebase to 6.6
- XCOMM - 1 week
- FWAP - 2 weeks
- VTOL - 1.5 weeks
- First Flight 1/21
- Production Handoff starts 4/1
- Production Ready 6/1


RISKS:
- MEDIUM: UNKNOWNS
- LOW: What if we cannot fit all AP into one processor?
- Schedule risk
- Hardware
- 

Future Optimizations:
- Unified Architecture
- Replace obsolete parts on VTOL AP
- Training SIL?


Discussion Points:
- How will the UAP impact NovAtel integration?
- Does UAP need to support training SIL?
- Payload directly connected to FWAP?

## Comments (3)

### Greg Fryer, 2023-05-03

@David Grosher Did you already make your own project, and is this a duplicate?

### Cameron Chapman, 2023-06-26

Emailed for the meeting today.
For discussion, here is our work so far and other links.
- HW deltas required for UAP: https://jenaero.atlassian.net/browse/ENG-230?search_id=2c34ed2e-a62c-4476-9ffb-42037ce40097 
- Red board as Not-An-AP breakout & Eventually redundant AP  https://jenaero.atlassian.net/browse/ENG-1488 
- We should have a separate discussion with Will/Scott to discuss mechanical integration of this equipment. I do not think it has started.
- C:\JAI Vault 1\Projects\107 - Stalker XE, VTOL Gen 2\Electrical Design\PCB\1809P01A-AP Adapter Board
- CAN connection to Not-An-AP
- The current VXE30 config has CAN connect to the XCOM, then talks RS232 to the FWAP. The block diagram below says CAN is needed to the not AP red board. If that is correct and connectors don’t change, the best place to connect would likely be a splice to the CAN wires on the internal transponder cable to the top of the red board J8.
- Ethernet connection to Not-An-AP
- Short term, would be easiest to steal from the transponder internal cable. If that is not acceptable, we would have to add a switch inside the avionics box. Longer term, adding a switch to the adapter board or red AP board if it changes may be best.
- Transponder connection
- Need to determine if this is still required with the same pins. Latest transponders have used the mod payload port.
- MCM connection to XCOMM 
- https://jenaero.atlassian.net/browse/ENG-572
- Discussed below with Dave
- Need to downselect adapter board
- 1 Ethernet and power connection to vehicle. Same connection method as discussed above? XCOM Transponder port to MCM port 1, MCM port 2 to red AP?
- For the remaining signals,
- list all connections available from carrier board and processor.
- Determine how many pins required each. Determine connector size required.
- Review and discuss which ones are not needed if we want to downsize.

 
 VXE Unified AP Blockdiagram JC-CC.pptx
 WIRELIST-VXE30+XE25.xlsx

### Scott Whitney, 2025-12-01

Notes 2025-12-01 
- Hardware Blockers from testing SW
- None at this point - B40s CAN-based design allows us to
- turn off FWAP in SW
- Shortcomings/Risks:
- Not final config
- EMI protection
- Required in final config (hardware)
- VTOL in Avionics
- Re-spin of ADB
- Harness to mag
- CW pocket will have network board and SSR board and be shielded
- 8 wire ethernet (will come with additional software work)
- Coin battery(ies) on outside of avionics box

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| epic.svg | other | 1 | 2026-07-06 | listed only |
