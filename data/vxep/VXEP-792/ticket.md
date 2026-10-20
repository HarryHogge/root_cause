# VXEP-792: Visual Based Navigation (VBN)

- **Issue type:** Major Project
- **Status:** In Process
- **Priority:** Medium
- **Created:** 2024-11-25
- **Updated:** 2026-02-07
- **Due:** 2025-08-01
- **Reporter:** Scott Whitney
- **Assignee:** Scott Whitney
- **Creator:** Scott Whitney
- **Labels:** LRR, VBN
- **Parent:** SP-121 Visual Based Navigation (VBN) tech development
- **Links:** is a parent of VXEP-822 (Name for FWVBN Project); is a parent of VXEP-823 (Job Code for VBN); blocks LRRSUAS-454 (All-domain Persistent Experiment (APEX)); relates to VXEP-1444 (OGCS 1.3.1); relates to VXEP-1560 (LRR Software for April 2026 Final Delivery)
- **Start date:** 2025-03-10
- **Key Stakeholder(s):** David Grosher, Eric Brewer, Greg Fryer, J Vo
- **Project Tier:** Tier 2
- **Planned Milestone(s):** Concept Design Review (CoDR), Detailed Design/Critical Design Review (CDR)
- **Charter Link:** https://jenaero.atlassian.net/wiki/spaces/PE/pages/499187713/DRAFT+-+Visual+Based+Navigation+VBN
- **Current Sprint Priority:** 12.0
- **LRR Desired Delivery Date:** 2025-08-01
- **Contract/Customer First Need:** Not possible until May at earliest.  Aug only.
- **Product/Tech Owner:** David Grosher
- **Tech Lead:** Eric Brewer
- **Program (Marquee):** Visual Based Navigation
- **Job Number:** J100085 - GPS Denied Stalker

## Description

Project Name: (not VBN?)
| SharePoint | VBN_INTEGRATION |
| JIRA | https://jenaero.atlassian.net/browse/VXEP-792 |
| Confluence | Visual Based Navigation |
| Charter | Visual Based Navigation (VBN) |
| System Visio | VisnavDrawings (VBN).vsdx |
| John EE Visio | PCB Planning VBN Hub & Harnesses.vsd |
| System Requirements | VBNRequirements |
| PCB Requirements | 2123665-01 VBN Board - PCB RVTM and Trade Study.xlsx |
| PCB SharePoint | 2123665-01 VBN Board |
| BOM: | PAYLOAD BAY PROTOTYPE VBN BOM.xls |

## Milestones:

- Conceptual Design Review
- Integration
- Open Loop Integrated HIL Test
- Open Loop Flight Test
- Closed Loop Integrated HIL Test
- Test Flight - Closed Loop
- Critical Design Review
- 

## VBN Block 1 (On VXE40 and VXE35)

### Requirements: VBNRequirements.xlsx

- Ability to execute missions in GPS Denied environments
- Ability to fly using VBN (OKSI application)
- Closed loop navigation - images create coordinates which are used in INS
- VTOL can/should use GPS data
- Performance 
- <50m accuracy called out in SOW.
- Environmental concerns - see requirements spreadsheet.
- Min/Max Operational temp
- Max Distance?
- Min Distance = 200ft
- Optional kit for VXE MAGNSS
- Optional kit for Havoc
- Launch and landing in GPS-denied (fully GPS-denied mission)
- OKSI states we can use a camera marker to improve accuracy
- Investigate if we can have operators select a landing point on a map

### Nice to have:

- Image classification
- ACTION: Can this be done on GCS/laptop, or does it need to be onboard'
- Target Tracking

## Additional Information:

### Hardware

- IR and EO camera Trade study (in process - cameras below are likely candidates)
- Teledyne FLIR BOSON+ 640  (https://www.flircameras.com/22640AS95.htm?search=boson%2B%20640&description=true ) 
- 2x development cameras ordered
- 2x dev kits ordered
- Firefly S USB3 (https://www.teledynevisionsolutions.com/en-ca/products/firefly-s/?model=FFY-U3-04S2C-S&vertical=machine%20vision&segment=iis )
- 2x cameras for dev ordered
- USB Hub (for the 2-camera solution)

### Electrical:

- MAGNSS Avionics supports VBN
- USB hub? Or is this off the shelf?
- VBN Harness

### Mechanical:

- Needs to be integrated
- as a kit on MAGNSS
- fully integrated into Havoc
- Questions answered by OKSI
- Do you typically put the camera looking straight down or does it need to be angled forward some? Straight down is ideal.  It can be pointed off-nadir if it has to be.
- I assume any location that has a clear view down is acceptable, provided that the extrinsic cal with the IMU data can be managed within a degree or so.  Is this right? Clear view of the ground is optimal so the belly of the aircraft is the ideal mounting point.  Within a degree is sufficient for general use.
- Have you had any issues with the vibe on any of these cameras?  Our fixed-wing prop isn’t terrible from a vibe perspective but the VTOL props are.  We may want to use the cameras at lower altitudes to assist with takeoff and landing (I understand that will likely be separate algorithms from the map matching). Have not had vibration issues.
- The 4 EO options looked pretty similar in terms of price and size.  What is your top choice among those options?  Do you know if any of these options are NDAA compliant? I think most of these are Chinese made so these would just be for testing.  Top choice would just be the Arducam AR0234 since it hits the most ideal attributes.  For production modules you would need to work with an NDAA camera company such as FRAMOS.
- Additional Open Questions:
- See spreadsheet.

### Software:

- Architecture - Eric has this in progress
- Allow camera SW to be updated
- Needs to be upgradable
- ACTION: Determine whether through GCS or Partner installer
- GCS
- Map Management - Users can select an area of interest (size limit?)
- ACTION: Determine Map Size Limit
- Need an external hard drive that provides higher accuracy maps and DTED
- Higher accuracy than DTED and Maps on the SSD
- Status Page for VBN
- When it is on and being used

### Documentation

- Operational Manual

### Purchasing


### Production

- Camera Calibration
- Space
- Tooling
- 

## 
OPEN QUESTIONS:

- IR Camera is export controlled, how does this affect the team, project, product? Correction: After clarification from FLIR, IR camera is not ITAR controlled.
- IR Cameras are not ITAR controlled

Link to Project Overview: VBN- Engineering Kickoff.pptx

## Project Folder Link (Sharepoint)

https://jenaero.sharepoint.com/:f:/r/sites/EdgeUSOnlyMaterial/Shared%20Documents/General/Engineering%20Team%20-%2002%20Subsystems%20-%2002.02%20Navigation%20(US-Only%20Subset)/VBN_INTEGRATION?csf=1&web=1&e=eZOJpd

## Comments (1)

### Cameron Chapman, 2024-11-27

Asked via teams. @J Vo , I was told you would be there pm for vbn. Do any of you have information, order status, data,sheets, etc. for the initial implementation we are planning? It would be useful for this project and havoc architecture. No rush, it can wait till people are back from PTO, just messaging to get the request out.

## Attachments (0)
