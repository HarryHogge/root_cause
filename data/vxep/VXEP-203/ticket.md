# VXEP-203: 497 - Poor GPS Signal Issue Solved with GPS Board Replacement, Investigate Removed Board

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-11-29
- **Updated:** 2025-06-10
- **Resolved:** 2025-06-10
- **Reporter:** Matt Philley
- **Assignee:** Connor Peebles
- **Creator:** Matt Philley
- **Links:** relates to RMA-181 (AITB VXE-497 231027-6  Center wing ODU connector issue)
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

AC 497 came back to SLO as an RMA for an unrelated issue, but during Flight Test AC was unable to fly due to poor GPS signal.
NCR 1889 was generated to investigate where we found questionnable ribbon cables inside Avionics Boax and corrosion on the Green AP GPS Header. That was all replaced but issue remained.
NCR 1928 was generated and we replaced GPS board SN GPS-1-1249. After GPS Board replacement the issue appears to be resolved.
Desire to investigate this board to see if we can find definitively what might be causing the GPS signal issue. Suspicion is that perhaps there might be solder balls or corrosion under RF Shield like was found with MAGACC board.
RMA JIRA:
https://jenaero.atlassian.net/browse/RMA-181

## Comments (4)

### Matt Philley, 2023-11-29

@Connor Peebles @Cameron Chapman I created this VIT2 and linked to AC497 RMA ticket to investigate the GPS Board. I will drop off the GPS Board (with Orange and Red Tags) to Connor’s workstation.

### Connor Peebles, 2023-11-29

@Cameron Chapman @Matt Philley I moved this to a VXE Problems - VXEP ticket. VIT2 is reserved for tickets that customers can see.

### Connor Peebles, 2023-12-07

No evident corrosion underneath shield. BT1 (the coincell battery) is low at 1.745V when it should be at ~3V. 
[embedded file]

### Connor Peebles, 2023-12-07

If the coincell batt drops below the min voltage, which is about 1.4V, it would cause the timing reference for the receiver to go out of whack and may require reflashing as the RAM data is lost. I am not an RF receiver expert though.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| MicrosoftTeams-image (13).png | image | 537 | 2023-11-29 | listed only |
| MicrosoftTeams-image (14).png | image | 478 | 2023-11-29 | listed only |
| MicrosoftTeams-image (15).png | image | 415 | 2023-11-29 | listed only |
| MicrosoftTeams-image (17).png | image | 513 | 2023-11-29 | listed only |
| IMG_0577.jpg | image | 6751 | 2023-12-07 | listed only |
