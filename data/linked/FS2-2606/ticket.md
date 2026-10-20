# FS2-2606: Crazy landing plan behavior

- **Issue type:** Bug
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-12-06
- **Updated:** 2025-10-14
- **Resolved:** 2025-10-14
- **Reporter:** Ruysser Gabler
- **Assignee:** David Grosher
- **Creator:** Ruysser Gabler
- **Environment:** Takeoff: ~5 mph ground winds, 5°F, cloudy skies. Winds aloft 20-25 mph @ 92
Landing: ~6 mph ground winds, 5°F, cloudy skies
- **Links:** relates to FS2-2605 (Aircraft indication flying opposite tracked direction); relates to FS2-2604 (Aircraft departed plan unintentionally); relates to FS2-2408 (External Mag data on CAN); relates to VXEP-813 (E140 Octopus/VXE30 Isolation Issues: Arcing to Fuselage, mag interference suspected)

## Description

Alaska demo flights 
▪ Very erratic flight behavior from fixed-wing autopilot upon sending to landing pattern required us to abort first landing attempt. After sending it back to the primary orbits the aircraft was not tracking waypoints at all with very high bank angles. Considered landing immediately in U-drive but decided against it due to no SA camera in the dark, the forest of tall trees with a tower close by. Aircraft could not track orbits at all after multiple attempts, descending extreemly low. After several retasks and orbit changes, the aircraft stabilized and reached the LZ. 

AAR is attached 

E140 G2 payload Fuel cell config

## Comments (3)

### David Grosher, 2024-12-06

Same here, linked to other issues likely driven by Mag interference. @Eric Brewer @Scott Whitney FYSA

### Scott Whitney, 2025-10-14

@David Grosher  @Ruysser Gabler - can this be closed since we use ext mag as the primary now?

### Ruysser Gabler, 2025-10-14

@Scott Whitney yes, I believe we can close this

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AC not tracking orbit at all.PNG | image | 3232 | 2024-12-06 | listed only |
| T95_V499_241115_205354_pack (1).zip | archive | 4527 | 2024-12-06 | listed only |
