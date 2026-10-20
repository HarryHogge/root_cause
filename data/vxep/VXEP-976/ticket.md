# VXEP-976: VXE 500 Reports large negative AGL after landing

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2025-02-05
- **Updated:** 2025-09-22
- **Resolved:** 2025-09-22
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Ben Triplett
- **Creator:** Alexander Alan Arnold
- **Labels:** Edge_Asset, Weekly-incident-tracker
- **Links:** relates to VXEP-978 (VXE 500 Freezing fog caused issues with ADP LRF); is fixed by VXEP-266 (VXE (all) ADP: Heated Pitot/New SA CAM/Remove other obsolete components)
- **Vehicle Tail Number:** VXE 500
- **Vehicle Configuration:** Fuel cell config, heated pitot prototype
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

EDGE ASSET
Ruysser: On landing for all 3 days the AGL altitude displayed on the VTOL control panel indicated a large negative altitude once on the ground. The AGL altitude should be close to 0 but the indicated each time was below -100:  2/2 landing ~ (-107), 2/3 landing ~ (-108), 2/4 landing ~ (-116). This could be an issue if it becomes a larger discrepancy as it may make the aircraft have more than the desired altitude to descend in VTOL (if transition altitude is set to 400 it may transition at 500 instead). I am not sure what logic it uses to determine its altitude of transition (VTOL or Xcom). But the VTOL should probably think that the ground is really 0AGL. 
Take off and landing location were the same

## Corrective Action

OAT measurement: use a sensor that is not influenced by heated pitot air to measure OAT. https://jenaero.atlassian.net/browse/VXEP-266 
LRF: software fix to exclude unreasonable LRF range measurements. Tracked here https://jenaero.atlassian.net/browse/VXEP-978

## Issue Status

We have identified two sources of altitude error: erroneous LRF range measurements likely due to environmental conditions, and OAT measurements that measure the temperature of heated air inside the pitot system instead of true OAT.

## Root Cause

The reported issue is the result of two other issues: Heated pitot and erroneous LRF measurements. The OAT estimate that is used in turn to estimate baro altitude is corrupted by the temperature of the heated air in the pitot tube. The ground temperature being reported around 25 degrees F while the OAT from the ADB is reported over 60 deg F. This issue should be resolved by measuring OAT independently from the air that is heated in the pitot system. 
 The LRF occasionally measures false ranges in certain conditions. The freezing fog environment is apparently one of those conditions, causing the LRF to measure ranges on the order of a 5 ft when its height above ground was around 500 ft. This problem can be solved in software by filtering LRF ranges that are very small while no reasonable LRF measurements have yet been made.

## Comments (9)

### Greg Fryer, 2025-02-05

@Eric Brewer Can you look at this? It is an asset, so no customer (you can ping Ruysser directly as needed). Don’t forget to change the state of the ticket once you start. 🙂 
@David Grosher @Scott Whitney FYSA, I guessed at a first look. Please interrupt if you want to divert or decide it’s less critical.

### Eric Brewer, 2025-02-05

@Ben Triplett can you take a look at this?

### Ruysser Gabler, 2025-02-14

@Ben Triplett Im not sure that this is an issue with the LRF, the last flight attached (250204) had the same issue it seemed with no freezing fog present

### Ben Triplett, 2025-02-14

@Ruysser Gabler The data I was originally provided definitely showed an issue with the LRF. That was part of the problem, but the heated pitot was also responsible in part for the bad altitude estimate. I assume the latest data is for a heated pitot system?

### Ruysser Gabler, 2025-02-14

@Ben Triplett All these flights are with the heated pitot, yes

### David Grosher, 2025-04-22

@Ben Triplett @Eric Brewer Is this investigation complete?

### Ben Triplett, 2025-04-22

@David Grosher Yes in that the problem is understood and I think the heated pitot / ADB was improved so that we don’t measure OAT at the heater, but I don’t know the actual status of this. For the LRF we proposed a software fix and created a task to implement but have taken no further action.

### Jackson Riley Curvin, 2025-09-16

@David Grosher @Ben Triplett @Eric Brewer do you all still need this ticket open? I am going to close this on our tracker.

### David Grosher, 2025-09-16

@Jackson Riley Curvin Yes, please close this out.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Mishap Reporting VTOL Altitude.docx](attachments/25974_Mishap%20Reporting%20VTOL%20Altitude.docx.md) | docx | 186 | 2025-02-05 | converted |
| T95_V500_250202_121303_pack.zip | archive | 6457 | 2025-02-05 | listed only |
| T95_V500_250203_111706_pack.zip | archive | 7508 | 2025-02-05 | listed only |
| T95_V500_250204_111241_pack.zip | archive | 4195 | 2025-02-05 | listed only |
