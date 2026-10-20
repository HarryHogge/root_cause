# FS2-2604: Aircraft departed plan unintentionally

- **Issue type:** Bug
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-12-06
- **Updated:** 2025-10-14
- **Resolved:** 2025-10-14
- **Reporter:** Ruysser Gabler
- **Assignee:** David Grosher
- **Creator:** Ruysser Gabler
- **Environment:** Takeoff: ~5 mph ground winds, 5°F, cloudy skies. Winds aloft 20-25 mph @ 92
Landing: ~6 mph ground winds, 5°F, cloudy skies
- **Links:** relates to FS2-2605 (Aircraft indication flying opposite tracked direction); relates to FS2-2408 (External Mag data on CAN); relates to FS2-2606 (Crazy landing plan behavior ); relates to VXEP-813 (E140 Octopus/VXE30 Isolation Issues: Arcing to Fuselage, mag interference suspected)

## Description

At Alaska demo During flight, multiple orbits were commanded. one orbit in particular the aircraft entered and then about half way departed the orbit and flew away then turning extremely tight to get back to the orbit, I can not recall if a go to was sent to send it back to the plan or nothing was sent and it did it itself. AAR would have the be checked but it departed without operator telling it to 
 E140 G2 payload Fuel cell config

## Comments (4)

### David Grosher, 2024-12-06

This is most likely related to the magnetometer interference with the E140 that is currently being investigated and will most likely be resolved with the two fixes currently being worked. 

- Use the Center wing Mag on the FW AP. Will be released with v6.4
- Resolve ground loop between E140 and the Aircraft.


@Eric Brewer @Scott Whitney FYSA

### Eric Brewer, 2024-12-08

@David Grosher thanks for the heads up.  Confirmed the logs show huge heading and roll/pitch errors on the fixed-wing ap.

### Scott Whitney, 2025-10-14

@David Grosher  @Ruysser Gabler - can this be closed since we use ext mag as the primary now?

### Ruysser Gabler, 2025-10-14

@Scott Whitney yes, I believe we can close this

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Departure of orbit 1.PNG | image | 2573 | 2024-12-06 | listed only |
| Departure of orbit 2.PNG | image | 2568 | 2024-12-06 | listed only |
| T95_V499_241115_205354_pack (1).zip | archive | 4527 | 2024-12-06 | listed only |
