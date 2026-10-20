# FS2-2605: Aircraft indication flying opposite tracked direction

- **Issue type:** Bug
- **Status:** To Do
- **Priority:** Medium
- **Created:** 2024-12-06
- **Updated:** 2025-10-14
- **Reporter:** Ruysser Gabler
- **Assignee:** David Grosher
- **Creator:** Ruysser Gabler
- **Environment:** Takeoff: ~5 mph ground winds, 5°F, cloudy skies. Winds aloft 20-25 mph @ 92
Landing: ~6 mph ground winds, 5°F, cloudy skies
- **Links:** relates to FS2-2604 (Aircraft departed plan unintentionally); relates to FS2-2408 (External Mag data on CAN); relates to FS2-2606 (Crazy landing plan behavior ); relates to VXEP-813 (E140 Octopus/VXE30 Isolation Issues: Arcing to Fuselage, mag interference suspected)

## Description

During Alaska demo several flights had the aircraft flying completely backwards on the map versus the actual heading of the aircraft. This seems to be a magnetometer issue attached is the AAR from one of the flights, can get more if needed. 

E140 G2 payload Fuel cell config

## Comments (3)

### David Grosher, 2024-12-06

Same here, linked to other issues likely driven by Mag interference. @Eric Brewer @Scott Whitney FYSA

### Scott Whitney, 2025-10-14

@David Grosher  @Ruysser Gabler - can this be closed since we use ext mag as the primary now?

### Ruysser Gabler, 2025-10-14

@Scott Whitney yes, I believe we can close this now

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V499_241115_205354_pack (1).zip | archive | 4527 | 2024-12-06 | listed only |
| backwards!.PNG | image | 3323 | 2024-12-06 | listed only |
