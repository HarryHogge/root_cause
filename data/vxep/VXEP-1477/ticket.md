# VXEP-1477: VXE-30 RTB to undesired and un-commanded location

- **Issue type:** Bug
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Highest
- **Created:** 2025-08-18
- **Updated:** 2026-08-12
- **Resolved:** 2026-08-12
- **Reporter:** Michael Mohr
- **Assignee:** David Grosher
- **Creator:** Michael Mohr
- **Labels:** TIQUILA, Weekly-incident-tracker
- **Links:** relates to VXEP-1479 (Loss of link RTB HIL SIM (VXE-765))
- **Asset type:** SGCS-1
- **Customer:** TIQUILA
- **Impacted Disciplines:** Software
- **Impacted Core Subsystems:** Aircraft, Ground Systems

## Description

During an initial training sortie (1 of 3 planned flights) in D201H the crew were advised by ATC to RTB due to an uncontactable aircraft intruding into the segregated airspace. To expedite the landing the Remote Pilot (RP) commanded the Uncrewed Aircraft (UA) to RTB via the ‘RTB’ button on the Ground Control Station (GCS); however, the GCS generated a simulation track (as if ‘synchronising' the mission with UA and generating an amendment to the loaded mission) instead of routing directly to the landing pattern. The simulation line drawn on the mapping did not plan to land the UA at either the Primary or Emergency landing point as per the RPs mission plan but headed Southeast out of the cleared airspace and out of view of the displayed map on the GCS. The RP cancelled the RTB command due to the simulation showing an undesired routing and commanded the UAV to ‘Go To’ IP1 of the landing pattern. The UAV entered the landing pattern without further incident, landing at the primary landing point. During the second sortie the RP tried to replicate the command by selecting the RTB function (‘RTB’ button); this time the UA performed as described in the OEM Operator Manual, heading directly towards IP1 of the landing pattern. During the third sortie the RP once again tried to replicate the RTB command failure by selecting the RTB function; once again the GCS generated a simulation line as if sync’ing to the UA (i.e. the same outcome seen in the initial flight). Upon further investigation, by means of conducting multiple RTB commands (plus cancelling the action before being sent to the UA and zooming out on the GCS mapping to understand the extent and routing of the simulation line being drawn) it was discovered that the simulation line initially tracked Southeast, then turned right to track South until the UA would run out of power and land at an undefined point.

## Comments (4)

### David Grosher, 2025-08-18

@Michael Mohr @Drew Hildreth @Pat Wells  @Ted Trowbridge This is a known issue and is the same as https://jenaero.atlassian.net/browse/VXEP-1474.  We don’t have the ability to fix this until we wholesale replace the simulation component of the GCS. This is a major effort and is something that we are working toward for OGCS. However, in the meantime I suspect we may get a lot of support requests, I think it may be prudent to issue an AN regarding this issue. Note: the aircraft will not actually fly the erroneous simulation, it will fly the expected route if allowed to continue. This has been shown in regression testing and HIL testing.

### Pat Wells, 2025-08-18

@Josh Burrell FYSA

### Pat Wells, 2025-08-19

@David Grosher is this something new that has recently occurred with an update?

### David Grosher, 2025-08-19

@Pat Wells I believe it started with v6.4, but I am not positive. It may be related to the new compiler toolchain that was introduced then. Ted is looking into it.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| TIQ RTB anomally.jpg | image | 504 | 2025-08-18 | listed only |
