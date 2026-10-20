# XKIT-4777: 2123714-01 SLA Breakout V3 - Rev B

- **Issue type:** Engineering Change
- **Status:** NOT Moved to Solidworks Manage
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2025-06-27
- **Updated:** 2026-09-26
- **Resolved:** 2026-08-15
- **Reporter:** Connor Peebles
- **Assignee:** Connor Peebles
- **Creator:** Connor Peebles
- **Labels:** NotMovedToSWM
- **Links:** relates to VXEP-1315 (B30 Systemic MCM Resets due to payload power)
- **Engineering Change Level:** Level 1 - Scope of change is clear but there is a choice of approaches
- **Project Tier:** Tier 1
- **Project Folder Link (Sharepoint):** https://jenaero.sharepoint.com/:f:/s/EngineeringTeam/Eix6d9-UGAtNgwWexqIXPUgB-VTSD5x74rpmkUB7zOFZuw?e=ORScWy

## Description

A365 Link: 2123714-01 SLA Breakout V3 - Rev B
Vault Location: C:\JAI Vault 1\Projects\128 - VXE2024\Electical Design\PCB\2123714-01 SLA Breakout V3\2123714-01 SLA Breakout V3 Rev B
Sharepoint Location: Engineering Team - 2123714-01 SLA Breakout V3 - All Documents
ECN: ECN #205 2123714-01 SLA Breakout V3 - Rev B.xlsx

## Project Deliverables

2123714-01 SLA Breakout V3 - Rev B, next iteration of SLA Breakout Board that includes opto-isolator for the GPIO lines that protect them from "Ground-Bounce".

## Link to Engineering Change Notice (ECN)

Not happening. Functions moving to XCOM in this task. Targeting UAP avionics. https://jenaero.atlassian.net/browse/AV-717 
@Connor Peebles  should we mark in A365 that this release is not happening (obsolete state, delete file, etc). The PN in A365 is already used by a VBN harness. 

https://jenaero.sharepoint.com/:x:/r/sites/JAI_Operations/Shared%20Documents/Engineering%20Changes/ECN%20%23205%202123714-01%20SLA%20Breakout%20V3%20-%20Rev%20B.xlsx?d=w5e2c7b748ac548b8882959ce126f51f9&csf=1&web=1&e=CqiI7F

## Comments (4)

### Christa Meck, 2026-02-10

@Connor Peebles What happened with this one?  It’s marked Highest priority and also related to a flight issue.

### Cameron Chapman, 2026-05-29

- LA Breakout Board 2123714-01 Rev A significantly reduced the likelyhood of such an event, but was not found to be a definite solution.
- Root Cause found to be:
- inrush current on theNON_CRITICAL bus
- Resulting back-fed inrushcurrent tripping the fast-tripcomparator on the TPS16630Efuse (max 45A)
- I suggest finding a new fuse/switching solution or simply removing the Efuse since the MCM is now a critical application.
- This analysis and work was de-prioritized from my plate
- Here is where that work would be done to roll out a new version of the SLA Breakout Board, still pending permanent solution
[XKIT-4777] 2123714-01 SLA Breakout V3 - Rev B - Jira
- I know of no way to analyze fleet wide aspect of if there have been any resets since Rev A was rolled out other than what is manually reported.
- Containment plan was ‘do not power cycle payloads during flight’

### Christa Meck, 2026-08-15

This Engineering Change was not actioned before the switch to Solidworks Manage.  If you wish to proceed with this change, open an ECR in Solidworks Manage.

### Christa Meck, 2026-08-15

This Engineering Change was not actioned before the switch to Solidworks Manage.  If you wish to proceed with this change, open an ECR in Solidworks Manage.

## Attachments (0)
