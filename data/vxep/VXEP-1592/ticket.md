# VXEP-1592: VXE-881 Would not accept Land immediately Commands

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-11-10
- **Updated:** 2026-06-30
- **Resolved:** 2026-06-30
- **Reporter:** Jackson Riley Curvin
- **Assignee:** Josh Burrell
- **Creator:** Jackson Riley Curvin
- **Labels:** 25thID, GS_Closed, LRR, Weekly-incident-tracker
- **Links:** relates to FS2-3923 (Land Immediately Command from VSM to XCOMM not receieved)
- **Customer:** 25thID, LRR
- **Vehicle Tail Number:** VXE-881
- **Vehicle Configuration:** BLOCK 35X LEMB
- **Problem Type:** Discovered Issue
- **Root Cause:** None. Vehicle behaved as expected.
- **Severity:** 1 - Flight Critical

## Description

Summary as follows: 
Unit called saying there was a “VTOL GPS Fault” and it wouldn’t transition in the PLZ
We looked in the Stalker 35X Manual for the message they were seeing, and the recommended action was U drive and land immediately. We relayed this to the operator and gave tips for a full manual nudge landing 
The operator then tried approximately 4 times at a u drive and land immediately and the aircraft still failed to transition. 
After forcing the plane down to 200 feet in u drive, and clicking land immediately it still did not land immediately 
We then had them to turn off the gimbal, add another Silvus node to the network, and send it back in the PLZ. During this PLZ attempt the aircraft landed as intended without the VTOL GPS fault. 
There are questions as to whether L1 jamming was present at the time of the flight as 3MBDE also experienced an inflight E140 GPS fail during their operations and are still waiting to see if they receive a similar VTOL fault during landing. 
After the aircraft was safely on the ground the unit relayed they were having everyone turn in for the night so we will be on site at approximately 8am local to retrieve data and I have asked them to quarantine 881 and the LEMB used until we can review the data.

## Corrective Action

Potentially update manual to describe LI behavior more comprehensively. In this case document that LI while the ELZ is selected will result in glide landing on the current flight path.

## Comments (2)

### David Grosher, 2026-01-14

@Josh Burrell The only outstanding task here is a decision on whether this requires a manual update. I’ll assign this to you, and defer to you on whether the current documentation is adequate. The report is in the linked FS2 ticket.  FYSA @Jackson Riley Curvin, @Drew Hildreth

### Jackson Riley Curvin, 2026-01-21

Closed on GS side.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V881_20251110T101020Z 1.zip | archive | 38382 | 2025-11-10 | listed only |
