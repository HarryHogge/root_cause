# VXEP-1007: Xcomm Board - Power & Thermal Test Plan and Execution

- **Issue type:** Task
- **Status:** New
- **Priority:** Low
- **Created:** 2025-02-12
- **Updated:** 2025-09-08
- **Reporter:** Jacob Troyer
- **Creator:** Jacob Troyer
- **Parent:** VXEP-1004 VXE30 LRR Avionics Box Test Plan and Execution
- **Links:** relates to VA-2434 (Trellis Radio LRR Architecture and Power Budget); relates to AV-74 (Perform Power Test on 12V Line to  Heated ADP and TW Radio)
- **Epic Link:** VXEP-1004

## Plan

Purpose: The purpose of this test is to ensure phase/gain stability and thermal performance of the Xcomm board over temperature when powering the ADP and TrellisWare Radio
- ADP: https://jenaero.atlassian.net/browse/VXEP-266
- TerllisWare Radio: https://jenaero.atlassian.net/browse/VA-2357

RVTM/Requirements: https://jenaero.sharepoint.com/:x:/r/sites/IRAD/Shared%20Documents/General/Projects/2024%20Air%20Data%20Pod%20Updates/2025%20ADP%20Requirements.xlsx?d=wd30b8fb658c54bedb6161b2868131a0f&csf=1&web=1&e=DGEVEx&xsdata=MDV8MDJ8anRyb3llckBlZGdlYXV0b25vbXkuaW98OGU5M2E3ZTEzNTczNDFiZTgwMWIwOGRkNGFmZDIyNzB8MTg3NmY2MWEzYmRiNDg0M2FlNzA3NWVkMGNjYjc0MDR8MHwwfDYzODc0OTE3MzIzNDMxMjg0N3xVbmtub3dufFRXRnBiR1pzYjNkOGV5SkZiWEIwZVUxaGNHa2lPblJ5ZFdVc0lsWWlPaUl3TGpBdU1EQXdNQ0lzSWxBaU9pSlhhVzR6TWlJc0lrRk9Jam9pVFdGcGJDSXNJbGRVSWpveWZRPT18MHx8fA%3d%3d&sdata=VDZzWVB1SkN5NFJLdmlaNDI1enI2RlJKbFprM1lsdVNXbkpxUTh0VEZlND0%3d  
- HP 0005: Do not exceed total available system power

| Device Under Test (DUT) | Part Number | Revision |
| Xcomm Board |  |  |

Test Setup: [Insert Visio Diagram]
(Optional?) Equipment List: 
Test Matrix/Procedure: https://jenaero.sharepoint.com/:x:/r/sites/IRAD/Shared%20Documents/General/Projects/VXE_TrellisWare_Radio_Payload/Electrical/Phase%20and%20margin%20testing.xlsx?d=w6087b5569c504191ba4ea7dd550ce707&csf=1&web=1&e=MZb88e 
Test Results:

## Comments (2)

### Jacob Troyer, 2025-02-17

Discuss the following once ADP picks back up:
| Cam Recommendations | Notes |
| Please do this process (https://jenaero.atlassian.net/wiki/spaces/EF/pages/612859909/EE+Test+Planning+to+verify+requirements.). Link to JIRA task for testing at top of this page | Complete |
| Please add a quick test summary to the plan field of the JIRA epic for testing | Complete |
| The JIRA task linked above is for making a power budget. It seems like it will be clearer to make a separate one for testing | Complete. Added https://jenaero.atlassian.net/browse/VXEP-1004 as a linked issue. |
| Is 37W TW sustained, pitot, new SA cam, etc? then 58W the pulsed load? | See Definitions on https://jenaero.sharepoint.com/:x:/r/sites/IRAD/Shared%20Documents/General/Projects/VXE_TrellisWare_Radio_Payload/Electrical/Phase%20and%20margin%20testing.xlsx?d=w6087b5569c504191ba4ea7dd550ce707&csf=1&web=1&e=MZb88e |
| What connections/regulators are you loading? A block diagram would be useful | In-Work |
| What does 69C represent? 50C plus solar load, or more extreme | (Worth discussing) Increased to 86C to represent 50C + solar loading + internal heat dissipation in Avionics Box |
| Clearly define measurement points, abort limits, etc. Linked document to this one | Measurement points in block diagram (Worth discussing) Currently no abort limits. May want some temperature based ones |
| What is DUT? Enclosed Avionics box | Only Xcomm board. All detail to be added to Plan |
| Are you taking MAGNSS loads into account? | (Need to discuss) |

 Other discussion points:
- Add TC to measure ambient temperature (to ensure chamber is at correct setting)
- Insure no airflow (put something over board) for hot conditions
- Instead of testing to loads, test until it power supply becomes unstable or until components get too hot. The idea here is to test to capability, so that we don't have to do this test again when we install the next thing.
- Vary the input voltage to the regulator to simulate battery voltage dropping during flight?
- 5V is also fed from U5 12.8V, do we need to account for that?
- See stepload response in time domain?

### Carl Graf, 2025-09-08

@Adrian Garcia this ticket is linked to the ticket for the 35X 12V line testing you are performing today. I am not sure how it relates and Jacob is out for a while. Can you please review the ticket and determine it’s criticality related to the testing you’re performing? Just want to make sure we’re not overlooking something. You may also want to review the other ticket linked here: https://jenaero.atlassian.net/browse/VA-2434 .

## Attachments (0)
