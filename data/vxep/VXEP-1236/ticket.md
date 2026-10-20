# VXEP-1236: VXE 336 "0" dted to "---" dted, waypoint discrepancies between MSL and AGL

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Not Verifiable
- **Priority:** Low
- **Created:** 2025-05-08
- **Updated:** 2026-03-02
- **Resolved:** 2026-01-20
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** GS_Closed, SOCOM, Weekly-incident-tracker
- **Start date:** 2025-05-08
- **Customer:** SOCOM
- **Vehicle Tail Number:** 336
- **Vehicle Configuration:** VXE 30 Battery config, payload unknown
- **Problem Type:** Discovered Issue
- **Incident Type:** Mission Failure/Abort
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Operator Statement
I was flying VXE30 over the ocean the other day and noticed when I go from "0" dted to "---" dted, the way points seem to get messed up between MSL and AGL being the same. Instead, the waypoints would use a mixture of field elevation at the GCS location and MSL. For instance, 1400 ft MSL should equate to 1400 ft AGL as well, however it would change 1400 ft AGL to 2200 ish ft MSL. If I tried to correct it by placing the correct intended alt in either field, it would screw up the other. 
I was able to stop the unwanted climbs or descents by switching to udrive. I was flying from an island with a 800 ish ft drop off and didn't want the aircraft descending below my LOS. I also disabled auto AGL and auto LOS to see if that made a difference. It did not. I had to pull the logs from the .2 page after the flight. Please let me know if you have any questions. Thanks.

## Comments (5)

### Alexander Alan Arnold, 2025-05-08

@David Grosher Added data from the Precision team.
HIs statement confirms the uDrive workaround
I will ask him to ensure they do a normal AAR next time so we can have the full logs. 
Let me know if you need me to ask for anything else

### Drew Hildreth, 2025-08-26

@Jackson Riley Curvin @Michael Mohr What is going on with this? I assume nothing anymore. Can we get this closed up?

### Michael Mohr, 2025-08-26

@David Grosher @Ted Trowbridge Was this something that was fixed with 6.5.? Or was there not enough information to really nail down a cause?

### Ted Trowbridge, 2025-08-26

@Michael Mohr We haven’t done anything to address this with 6.5 – it would need more investigation.

### Alexander Alan Arnold, 2026-01-20

Issue not a priority

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 336 maritime.zip | archive | 766 | 2025-05-08 | listed only |
