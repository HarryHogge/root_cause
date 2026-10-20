# PLD-139: E95 SN 8098 and  8115 Vector nav not responding when tested with 987.

- **Issue type:** Bug
- **Status:** Backlog
- **Priority:** Highest
- **Created:** 2025-12-12
- **Updated:** 2026-04-28
- **Reporter:** Cameron Chapman
- **Assignee:** Mike DeJesus
- **Creator:** Cameron Chapman
- **Links:** relates to PLD-138 (E95 EPS-8093 and EPS-8090 Customer Issues -camera would not connect to software. Camera would not power cycle or power off); relates to VXEP-1635 (During NSW IQT, both customer E95 gimbals had multiple issues connecting to three different Advanced Nav aircraft used during training. Also, the gimbals would not power off when cycling power in the custom payload control in VXE-SUAV.); relates to VXEP-1641 (E140 MWIR VectorNav Not Communicating); relates to PLD-142 (Grant edge US access to Octopus design files and problem tracking system to better enable troubleshooting and collaboration ); relates to PLD-144 (Release Architecture and interconnect diagrams for E95 then E140); is a child of PLD-131 (SLO+Riga Epsilon Cross-Site Project and Issue Collector); relates to PLD-97 (VXE30 AdvNav 886 - Payload Port Investigation)
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Cody testing in SLO on 987 1520 2025-12-12
"Vector nav not talking to gimbal. Doc 2126889 OPTIONS BASED FUNCTIONS. Steps 4-7 were all ran in simulation mode. Seems acceptable. Should add another section to test actual GNSS  to vecor nav. 
In error list of epsilon. Secondary error: GPS no communication. GPS init failed.
In diagnositic. GPS INS module. Firmware tab. Reading firmware.. sending command again. "

SLO testing was first done in a advanced nav aircraft. Gimbal function was not checked on bench prior to installing into an aircraft. 

https://jenaero.sharepoint.com/:f:/s/IRAD/IgDMuCJ8f6cBS4p6-bMOpO-eAYUuvQSB48FrQahNjSSz94c?e=9hocjQ

## Corrective Action

Containment
- https://jenaero.atlassian.net/browse/VXEP-1648
- https://jenaero.atlassian.net/browse/VXEP-1655

CA 
- https://jenaero.atlassian.net/browse/VXEP-1640
- https://jenaero.atlassian.net/browse/VXEP-1660
- https://jenaero.atlassian.net/browse/VXEP-1656
- https://jenaero.atlassian.net/browse/VXEP-1646

## Plan

Primary Plan for Customer Assets
- Locate an internal asset we can test the fix on. John G will ship 8077 from HSV 12/19. It has a damaged micro-d connector. Will need to replace it if we need serial to PC connection. Can use connector from damaged unit.
- Cut and stow the wires we did not intend to connect. (PPS, VNRX).
- Double check E95 cables are built to print otherwise.
- Ground test internal asset of advanced nav aircraft. Verify VN remains functional and perform other gimbal checkouts.
- Test VN on stand, B30 aircraft, advanced nav other than 987.
- Remove 987 branch cable. Check on cable tester. Ensure pinned out correctly at Alden connector.
- HSV has 4 E95s on loan from Lativa. Mike to call Rihards to see if we can transfer those for customer deliveries.
- Tracking for the 4x E95s: UPS# 1ZK6A5960120495897
- Ship 3 customer E95s with the vehicles to customer.

 
Other Supporting Activities
- Connor to continue testing vector nav. See if it is misconfigured or damaged.
- John in HSV and Mark/Laszlo in SLO to test the following ports on the working and not working gimbals.

both sides of level shifter. Guessing VN has to be configured before it starts to transmit.  All measured to gnd.
- U4 13 and 12
- 8 and 9
- 7 and 10
- Check voltage U3 in. 5V. We think done.

- Schedule call with Latvia. See linked question list.
- Determine plan for switched rtn vs power. Test.  
- when opening gnd, maybe lifting chassis to power. Likely ok if no other return paths.
- SSR not turning off likely due to ground differences keeping FET open. @Abel J. Markow  to evaluate harness rework options with @Cliff Gerhard
- PPS is supposed to be 50 ohm load. Very fast signal. Supposed to be differential pair to 50ohm load. 1 or 10Mohm load currently. G2 board should isolate and work. Include in MANI project.
- Return damaged E95 and MWIR units to Latvia for repair.

## Issue Status

Gimbal Tracking
NCR List - EPS.95 Functional Discrepancies for SN 8094, 8095, 8096, 8097
NCR List - E95 Gimbal Paperwork & Configuration Issues
 Edge Autonomy Operations - NCR List - All Items EPS8106 / EPS8110 / EPS8112 / EPS8105 / EPS8107 / EPS8108 / EPS8111

## Root Cause

- Harnesses (add PN) built in Riga were delivered with wires that were not supposed to be connected, were not peer reviewed, approved, etc. While these caused no issues on B30 assets, and potentially some advanced nav aircraft, connecting them to advanced nav aircraft in SLO caused the vector nav chips on the E95s to be damaged. No anomalies were found on the SLO aircraft.

## Comments (3)

### Cody Smisek, 2025-12-15

@Drew Hildreth these are the two.

### Jackson Riley Curvin, 2026-01-21

@Cameron Chapman who does this camera belong to?

### Cameron Chapman, 2026-01-23

@Jackson Riley Curvin Not sure. Both are not on the tracker. I think they were destined for a customer, but then we sent 2 others to replace them. They may need to go back to Latvia to replace the bailment ones. Check with @Mike DeJesus 
Save this link 
| HSV asset Tracker | EA Huntsville Operations - Gimbal Status - All Items |

## Attachments (0)
