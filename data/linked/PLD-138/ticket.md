# PLD-138: E95 EPS-8093 and EPS-8090 Customer Issues -camera would not connect to software. Camera would not power cycle or power off

- **Issue type:** Bug
- **Status:** Backlog
- **Priority:** Highest
- **Created:** 2025-12-12
- **Updated:** 2026-04-28
- **Reporter:** Cameron Chapman
- **Assignee:** Mike DeJesus
- **Creator:** Cameron Chapman
- **Links:** relates to RMA-861 (EPS8090 ); relates to RMA-862 (EPS8093); relates to PLD-139 (E95 SN 8098 and  8115 Vector nav not responding when tested with 987.); relates to VXEP-1641 (E140 MWIR VectorNav Not Communicating); relates to PLD-146 (US Epsilon questions for Latvia ); relates to PLD-97 (VXE30 AdvNav 886 - Payload Port Investigation)

## Description

Jira https://jenaero.atlassian.net/browse/XKIT-5244 
Sharepoint E95 Dec 2025 tilt encoder issues
Investigation Sheet: E95 Dec 2025 Investigation Sheet

Background: We did a system level test (ground and flight test) for this order using the E95s and did not observe the issue. When they were conducting the class the flight ops team reported persistent tilt encoder issues. 
Waiting for more detailed operator report. Was there an incident written/operator report of the E95 issues experienced (PNs, SNs, aircraft, location, conditions, other payloads, etc)?  Cameron Chapman: Main fix is hopefully for Latvia to include the FW fix in the E95... | E95 Issues | Microsoft Teams
From Linked RMAs:

Issues EPS-8093 and EPS-8090 going to HSV. ETA 12/15. 
Tested on 4 different aircraft. 920 was one (in SLO). 946 956 919 920 believed to be the involved issues.
| Product Serial Number | EPS8090, EPS8093 |
| Software Version | 3.5.12.14 |
| Firmware Version | 3.5.6.8 |
| Invoice Number |  |
| A brief description of the actions that were performed before the reported problem occurred. | camera would not connect to software. Camera would not power cycle or power off. Camera would make unusual spinning movements in flight. |

## Plan

- Inspect for excessive dust and debris.
- First on GSK, try to replicate issues. If unsuccessful, try to replicate on aircraft of the same configuration (or same aircraft if available).
- See if manually positioning the gimbal before power recreates or fixes issue.
- See if cleaning fixes the issue.
- Relay issues might be due to activating the wrong port, or SSR being activated by ground differences. Test if functional on vehicle and report differences. Test during flight as well.
- Confirm C/CA.

## Issue Status

Gimbals will arrive in HSV 2025-12-19
Suspected cause: 
- Operators report dusty conditions. Suspect gimbals was not stowed during forward motor test (sand visible on lenses in video). Looks like tile motor is jammed. Cannot reach position. Algorithm: When starting motor, needs to find 0 position. If it cannot find it. Looks upside down. Cannot move. Power off. Rotate by hand. Working on new error messaging system. Dirt or sand could cause this issue. Using air could work. Probably was not stowed for forward motor test. CA could be to ensure stowed. Improve sealing.
- Relay might not be powering off completely. Might be a few volts left when relay shuts off. Can measure.
- If missing motor index, it can spin. Best fix is to power cycle.

## Comments (0)

## Attachments (0)
