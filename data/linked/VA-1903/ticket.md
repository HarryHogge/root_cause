# VA-1903: VXE695 - Main Battery Harness Connector Sparking when Main Battery Mate

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-08-26
- **Updated:** 2026-03-02
- **Resolved:** 2025-08-05
- **Due:** 2024-08-27
- **Reporter:** Cody Smisek
- **Assignee:** Cameron Chapman
- **Creator:** Cody Smisek
- **Labels:** Havoc, XKIT
- **Links:** relates to VXEP-540 (Recent AS150 Connectors causing intermittency and difficulty to connect and disconnect correctly and safely (AS150 Socket Issues))
- **Start date:** 2024-08-26
- **Sprint:** XKIT 8/21-9/10
- **Customer:** XKIT
- **Vehicle Tail Number:** 695
- **Problem Type:** Discovered Issue
- **Incident Type:** Aircraft Damage
- **Severity:** 4 - Annoyance
- **Components (EA Aircraft):** Aircraft, full assembly, Airframe, Fuselage, Battery, Main
- **Job Number:** J100115 - VXE Havoc Development

## Description

When main battery is connected to VXE695 main battery harness/connector, there is a spark.  (Occurred on 8/26/2024)
No other hardware was connected during spark observations. Only fuselage was involved. 
The following Main Batteries were used and sparks were seen during connection. 1678, 1310, 2040, 2028
Suspect anti-spark is ‘dead’. 
Reported by @Artis Bertulis & @Ruysser Gabler

## Issue Status

harness removed and red tagged. 
measured 66 ohms across anti-spark

## Comments (6)

### Cody Smisek, 2024-08-26

@Carl Graf FYI

### Cameron Chapman, 2024-08-26

@Cody Smisek Please red tag, remove, and replace fuse power harness. EEs can then test it. These harnesses are currently holding up production due to AS150 issues. 

The most feasible path to a Wednesday flight is to use one from the ironbird. We will inspect the harness and check with @Adrian Garcia to determine why that harness is on the iron bird/where it came from. FYI @Carl Graf

### Carl Graf, 2024-08-26

@Cameron Chapman does this harness get replaced by a different design when converting from Standard to Havoc config? We need to be very careful that this situation does not harm the D750 Fuel Cells.

### Cameron Chapman, 2024-08-26

@Carl Graf no, it is the same harness. It is a very simple harness of a few power wires, so if it works on the iron bird and can handle standard current, it will have no higher risk of damaging a fuel cell.

### Cody Smisek, 2024-08-26

this harness is for a separate effort than this weeks flights (different aircraft). harness has been removed and red tagged. harness will be replaced with one that has been checked out from the iron bird.

### Christa Meck, 2025-08-05

Closing this incident as it’s from Aug 2024 and any investigation is likely done at this point.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Media (3).jfif | image | 232 | 2024-08-26 | listed only |
