# VXEP-651: VXE 594 Operator commanded RTB, AV went directly to IP5

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-09-26
- **Updated:** 2026-09-09
- **Resolved:** 2025-05-19
- **Reporter:** Pat Wells
- **Assignee:** Jason Scherer
- **Creator:** Pat Wells
- **Labels:** Crash, PMA263, Training, Weekly-incident-tracker
- **Links:** relates to RMA-363 (VXE-594 240926-2); relates to FS2-2321 (Create a consolidated report on mismatched SW/FW versions for VXE-572/573/574/628/688/594); relates to GCSS-362 (Implement lockouts or significant warnings to prevent operators starting VTOL landing at too high of an altitude. )
- **Customer:** PMA263
- **Vehicle Tail Number:** 594
- **Issue Status:** Aircraft returned to RMA
- **Root Cause:** Operator Error: Commanded transition to VTOL at Altitude via goto to IP4.
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

Note, this is not new. Creating now as previously we didn’t receive data and now the aircraft is enroute to SLO so that the investigation can begin.  Incident is from the grouping with mis-matched software at 29 Palms. 8/26/24
Statement from operator
Operator commanded RTB, AV went straight to IP5 and entered VTOL landing. HLB depleted and operator glide landed AV. 

Files downloaded on 11/12/2024 by C. Smisek. Stored here VXEP-651 VXE594 RTB to IP5
Report Included in Consolidated Report from incidents at 29 Palms.

## Corrective Action

This is covered by existing corrective action delivered in v6.4 to provide an interlock in the GCS asking the operator if they are sure they want to perform the dangerous action.

## Comments (15)

### Sean Odell, 2024-10-30

@David Grosher Aircraft has been though RMA intake and will be moved to engineering in the next hour. 
@Pat Wells FYSA

### David Grosher, 2024-10-30

@Jason Scherer FYI see below, this is part of the consolidated report.

### Cody Smisek, 2024-11-07

@Jason Scherer @David Grosher aircraft is in Engineering awaiting next steps.

### David Grosher, 2024-11-08

@Cameron Chapman Can you pull the data off of this aircraft and then return to RMA.

### Cameron Chapman, 2024-11-12

@Giovanni Gonzalez or @Cody Smisek are you available to pull data from this aircraft?

### Cody Smisek, 2024-11-12

@Cameron Chapman I will download logs then return to RMA.

### Cody Smisek, 2024-11-12

Removed avionics from fuselage due nose harness condition. Utilized engineering iron bird for power/connection to download xcomm logs. 
Utilized engineering iron bird to connect to center wing (VTOL) to pull logs.

### Cody Smisek, 2024-11-12

@David Grosher @Cameron Chapman Data downloaded. Returning to RMA. Ticket reassigned to Dave.

### David Grosher, 2024-12-04

@Pat Wells Despite this vehicle incident happening with the others with mismatched software it appears that this vehicle did NOT have that issue. However, the operator did not command a RTB but a GOTO to IP5, which led to their issue. @Jason Scherer FYSA

[17:56:11.098 10974.098] GoTo m,w 1  3

### Alexander Alan Arnold, 2024-12-10

@David Grosher Based on the comment below are we considering this operator error or is there still work that needs to be done?
@Pat Wells

### David Grosher, 2024-12-10

@Alexander Alan Arnold I would like to have @Jason Scherer review my findings and create a report.

### Alexander Alan Arnold, 2025-01-10

@Jason Scherer How is the final report looking?

### David Grosher, 2025-02-14

CA is the https://jenaero.atlassian.net/browse/GCSS-362, which will be delivered in v6.4

### Jason Scherer, 2025-03-22

Report is included in the 29 Palms software miss match report.

### David Grosher, 2025-05-19

Closed with release of v6.4

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Screenshot 2024-11-12 094601.png | image | 167 | 2024-11-12 | listed only |
| Screenshot 2024-11-12 095126.png | image | 183 | 2024-11-12 | listed only |
| Screenshot 2024-11-12 095526.png | image | 568 | 2024-11-12 | listed only |
| Screenshot 2024-11-12 095539.png | image | 586 | 2024-11-12 | listed only |
| vtol.zip | archive | 4843 | 2024-11-12 | listed only |
| xcomm.zip | archive | 1684 | 2024-11-12 | listed only |
