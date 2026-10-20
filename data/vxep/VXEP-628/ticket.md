# VXEP-628: Systemic VXE30 VTOL ESC Reliability Issues

- **Issue type:** Incident (8D)
- **Status:** New
- **Priority:** High
- **Created:** 2024-09-11
- **Updated:** 2026-08-31
- **Reporter:** Cameron Chapman
- **Assignee:** Cameron Chapman
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-272 (VXE-425 Crash on VTOL landing-ESC Damage); relates to VA-444 (Evaluate replacing VXE30 ESCs); relates to ENG-3034 (Aircraft 450 VTOL Landing Crash-ESC Damage); relates to VXEP-811 (VXE-470 Crash on VTOL descent-flying overweight-HW not inspected?); relates to VXEP-231 (VXE-496 with 550 wing set-failure during VTOL transition-AS150 contact issues); relates to ENG-3121 (Main Lift Motor Issues Tracker-Undiagnosed Cause); relates to ENG-3090 (422 - Intermittent VTOL Lift Motor stopped during launch-No HW to investigate); relates to VXEP-1464 (VXE 829 LRR Asset mishap during VTOL landing-ESC corruption); relates to VXEP-1630 (VXE-920 Two separate incidents of near miss during fixed wing to Vtol recovery transition. Seemingly due to motor/ESC assembly-No investigation planned); relates to ENG-2973 (Aircraft 439 Launch Failure-No HW to investigate); relates to XKIT-760 (Main AS150 replacement issue-Develop new battery power connectors for Havoc Block 5); relates to VXEP-1802 (VXE 620 Suffered a VTOL Failure-unable to replicate); relates to VXEP-1881 (VXE 884 Mishap-Lift ESC Failure); relates to VXEP-1951 (VXE 996 RR Motor detached from boom)
- **Severity:** 1 - Flight Critical

## Description

Linking ESC failures and using this project to arrange improvement or replacement actions. Many due to soft start FETs which aren’t needed if using anti-spark contacts.

## Corrective Action

Main potential CAs
Future recommendations, not implemented yet:
- Replace B30 ESCs with B40 ESCs or a smaller variant. https://jenaero.atlassian.net/browse/VA-444
- Link to launch abort and other feature requests.  https://jenaero.atlassian.net/browse/VXEP-1519
- Pre-landing motor checks., fixed wing landing if not acceptable.  I think Dave mentioned that these were not very feasible and would not prevent many issues. Check if it comes up again.
- Pre-launch error detection and launch prevention https://jenaero.atlassian.net/browse/VXEP-1469
- Did we implement full power screening/functional test of B30 and B40 ESCs (including spares) @Daniel Ceja?
- B30 Motors get a quick spin (without a blade) after the motor leads are soldered to the ESC. As for B40 ESC there is still not screening/test. This could eventually be accomplished with the LMT once its up and running and modified for the B40 Motors or similarly to B30 we could make a jig that Spins a known good motor where the ESCs can be swapped in after they have been built up.
- 8/17/26. LMT almost done. Power supply on order. Plan to repurpose or make new

## Plan

- Could spend time better defining the operational limit of these ESCs, but I think the time would be better spent integrating and testing the Hargrave ESCs.
- Main CA is to remove them with B40. See linked issues for more info.
- @Laszlo Juhasz  can you find/send your previous analysis recommending not using the processor in ESC applications, and any other lift ESC design issues?
- Good example of analysis VXE 829 LRR Mishap Investigation Report-VXEP-1464.pptx
- B30 Open Systemic Issues (Also Applies to B35X, 35Y) - Product Design and Operation - Confluence


Typical investigation steps:
- Check logs for voltages. If issues, likely contact failure. https://jenaero.atlassian.net/browse/XKIT-760
- Compare commanded throttle to expected power (need to find link)  https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Electrical/Calculating%20Expected%20vs%20Actual%20Power%20for%20Lift%20Booms%20in%20terms%20of%20throttle?csf=1&web=1&e=eAe7n4
- Inspect what can be seen before removing from boom (wire damage, smell of burning, prop/hub issues, etc. 
- If all seems normal, remove props. Run ESC with no propeller load. See if it runs normally. Record normal vs abnormal RPM, motor signals, etc.
- open ESC. Inspect/smell for damage.
- Run on dyno under load.
- Run flight profile on dyno. https://jenaero.sharepoint.com/:p:/s/FlightSafety/EXQUfU9atqRNh2r13Q3--m0BlJCaJUcm5OPxeeOmJEmdAQ?e=VZ0ObR

## Root Cause

Common failure modes
- AS150 failures. See https://jenaero.atlassian.net/browse/XKIT-760
- Soft start FETs do not share current evenly. Overtemp and damage. Can be verified with inspection.
- @Laszlo Juhasz  can you find/send your previous analysis recommending not using the processor in ESC applications, and any other lift ESC design issues?
- Design is not well documented, limited test data available, operational limits not documented.

Sorting by incident https://redwireglobal.sharepoint.com/:x:/r/sites/FlightSafety/Shared%20Documents/Incident%20Reports/ESC%20Issue%20List.xlsx?d=w685c623d0d2a4f9391032cd056b37e33&csf=1&web=1&e=hnR4Ts
| Link | Description | Cause |
| - [VIT2-284] VXE 401 Failed VTOL Landing from 10ft (Crash) - Jira (atlassian.net) | AS150 contacts |
| - [VIT2-281] VXE 454 Center Wing Power Connector solder melted - Jira (atlassian.net) | AS150 contacts |
| VXEP-231 | VXE-496 with 550 wing set-failure dur... | AS150 contacts |
| ENG-3034 | Aircraft 450 VTOL Landing Crash-ESC D... | ESC damage |
| VXEP-272 | VXE-425 Crash on VTOL landing-ESC Damage | ESC damage |
| VXEP-1881 | VXE 884 Mishap-Lift ESC Failure | Investigating |
| ENG-2973 | Aircraft 439 Launch Failure-No HW to ... | No HW to investigate |
| VXEP-811 | VXE-470 Crash on VTOL descent-flying ... | No HW to investigate |
| ENG-3090 | 422 - Intermittent VTOL Lift Motor st... | No HW to investigate |
| VXEP-1630 | VXE-920 Two separate incidents of nea... | No investigation planned |
| VXEP-1464 | VXE 829 LRR Asset mishap during VTOL ... | Processor corruption |
| VXEP-1802 | VXE 620 Suffered a VTOL Failure-unabl... | Unable to replicate |

## Comments (2)

### Cameron Chapman, 2025-03-06

@Adrian Garcia @Hayden Jeanor here's an example system issue linker ticket like we discussed today. We could do something similar for AS150 contact issues, and a subset for the socket diameter issue.

### Cameron Chapman, 2026-07-09

Previous issues where the tickets may no longer exist:
- [ENG-1781] Record published limits and any guidance to exceed limits. Lower transition, slower climb rate, etc. - Jira (atlassian.net)
- [VIT2-284] VXE 401 Failed VTOL Landing from 10ft (Crash) - Jira (atlassian.net)
- [VIT2-281] VXE 454 Center Wing Power Connector solder melted - Jira (atlassian.net)
- [ENG-1710] Review VXE371 for overweight and above nominal current draw during AEWE - Jira (atlassian.net)
- [ENG-1711] Review VXE376 for overweight and above nominal current draw during AEWE - Jira (atlassian.net)

## Attachments (0)
