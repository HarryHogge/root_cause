# VXEP-466: IRAD: Unified Autopilot

- **Issue type:** Initiative
- **Status:** In Process
- **Priority:** Medium
- **Created:** 2023-01-17
- **Updated:** 2026-03-25
- **Reporter:** Greg Fryer
- **Assignee:** David Grosher
- **Creator:** Greg Fryer
- **Labels:** valid
- **Parent:** SP-77 Unified Auto Pilot (Tech Development)
- **Links:** relates to ENG-2921 (Replace 0002P01G Autopilot-processor ST10F168SQ6 obsolete.); relates to ENG-123 (PCB Redesign 1710P01A; 1409P01D; 1502P01D Required (by ~12/2023)); relates to VXEP-484 (0002P01G Green Autopilot Reliability Issues/Fallout Study); relates to ENG-1539 (Build 107-111666 AUTOPILOT HILS to support engineering); relates to FS2-106 (Implementation+Test JAI CommandSensorHealth); relates to VA-30 (Edge internal troubleshooting-VXE 407 -VTOL AP Froze-Error during transition for landing, VTOL AP WD); relates to VXEP-41 (TPTR-74 VXE 510: (VTOL AP WD) Consolidated Watch Dog tracking); relates to VXEP-606 ( improve data logging so data is logged closer to incidents/crashes. Would saving more data to the GCS help?); relates to VXEP-470 (Unified AP for Block 40)
- **Supply Chain Stakeholder:** Perry Richardson
- **Leadership Stakeholder:** Allen Gardner
- **Product/Tech Owner:** David Grosher
- **Program (Marquee):** Unified Auto Pilot
- **Job Number:** J100065 - Autopilot Unified

## Description

Project to: 
Combine VTOL and FW Autopilots on VXE30
Eliminate current obsolescence of ST10F168SQ6
Update electrical architecture to support updated software.

We need to resolve the VTOL AP WD issue before implementing this project. 

ST10F168SQ6 inventory 10/9 1156
0002P01G 128
Rate calculation sheet. Rate Forecasts.xlsx
| temp rating goes up to 125 on the Q3 |  |  |  |  |
| Date | Rate/mo | ST10F168SQ6 or Q3 Inventory | Fallout rate | Months left |
| 10/9/2024 | 20 | 800 | 0.25 | 30 |

Some of those are Magacc board failures, which can be replaced and retested (difficult process). May be able to reduce fallout rate if electronics needed to/had time to rework.

## Comments (3)

### Cameron Chapman, 2023-03-22

Attaching presentation Gordon sent to Kurt.

### Cameron Chapman, 2023-03-30

Actions from 3/30 meeting.
- Need list of all changes that need to be made in the code to use daughterboard. John C to assign someone.
- Shaheen needs HIL to run the code. Go to Kyle to request.
- Cam to provide HIL WD and BOM.
- Talk to Sam about using in Penguin idea

### John Clark, 2023-04-21

@Cody Smisek this is where the bug in the FW AP should be directed I think. It needs to be linked into this project somehow. @Greg Fryer @Cameron Chapman I will explain.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [unified_ap.pdf](attachments/13199_unified_ap.pdf.md) | pdf | 528 | 2023-03-22 | converted |
| [Autopilot Source Code Analysis ST10 Family Port.docx](attachments/14357_Autopilot%20Source%20Code%20Analysis%20ST10%20Family%20Port.docx.md) | docx | 46 | 2023-05-03 | converted |
| [VXE Blockdiagram JC 5.1.23.pptx](attachments/14358_VXE%20Blockdiagram%20JC%205.1.23.pptx.md) | pptx | 54 | 2023-05-03 | converted |
| [1409P01D Schematic.PDF](attachments/15185_1409P01D%20Schematic.PDF.md) | pdf | 798 | 2023-06-26 | converted |
| [1809P01A-AP Adapter Board.PDF](attachments/15186_1809P01A-AP%20Adapter%20Board.PDF.md) | pdf | 3306 | 2023-06-26 | converted |
