# ENG-2946: Investigate where the harness failure occured and why

- **Issue type:** Sub-task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2024-08-21
- **Updated:** 2026-03-27
- **Resolved:** 2026-03-27
- **Reporter:** Jeremy Kostel
- **Assignee:** Adrian Garcia
- **Creator:** Jeremy Kostel
- **Parent:** ENG-2944 [REMOVE from VXEP] VXE 689 - VTOL battery voltage sensor stopped working after power cycling. 
- **Links:** relates to VXEP-946 (VXE 401 Centerwing failing to report proper VTOL battery state)

## Description

- The dual current sense harness (pn: 107-102264) had a broken connection to ground (DP1).
- See red highlighted path in the drawing
- The ground line is 26 AWG and potted with three other wires (11 AWG 2x, 8 AWG 1x)
- There is no ground line stuck out in the potting where the break occurred, so it could have happened while the potting was still wet
- See attached images

## Plan

When time permits, investigate changing the potting material
Alert QA to the potting not reaching the bottom of the connector

## Issue Status

- Harness thoroughly investigated
- Corrective actions proposed

## Comments (4)

### Jeremy Kostel, 2024-08-21

[embedded: 107-102264_d dual current sense, assembly 1 (1).pdf]
[embedded: Image (1).jpg]

[embedded: IMG_0025.jpg]


[embedded: IMG_0022.jpg]

### Jeremy Kostel, 2024-08-21

Full set of images can be seen here
Findings:
- The ground line (26 AWG) was found severed directly on top of the AS150 connector. This line was soldered to the two 11 AWG ground lines inside the connector.
- Check highlighted path on the drawing to see broken path
- The harness contains three other wires: two 11 AWG wires and one 8 AWG wire.
- The severed ground line showed visible damage beyond the break, including a circular cut around the wire, suggesting it was initially cut to be stripped off. Additional damage, likely caused by strain, was also observed.
- this damage occurred before any tampering during the inspection
- The inspection itself only involved cutting through the nylon, far above the location of the damaged wire
- The top of the AS150 connector was not potted as outlined in procedure document 107-102264 even though there are gaps present (still plenty of solder to have continuity)
- [embedded: image-20240821-201633.png]
- The 26 AWG wire was the correct length according to the drawing
- The potting inside the custom AS150 plug did not fully reach the base of the connector
- 26 AWG wire was found severed outside the potting, indicating that the severing occurred before the potting had dried.

### Jeremy Kostel, 2024-08-21

Potential Solutions
- We may need to change the potting compound use in this assembly
- 26AWG wire is actually able to “slide” through and back in this part of the assembly:
- [embedded: image-20240821-204314.png]
- It is possible when tech connected the ground connector, they pulled the 26AWG wire through and it caused so much strain the wire broke.
- Need a potting compound that does not allow wires to slide
- Making sure the potting goes all the way to the bottom of the cable should also provide much more strain protection

Potential Longer Term Changes
- We could relocate the ground connection to one of the EC5 ground wires in the same harness
- this would alleviate stress on the 26AWG wire
- The connection in the CW would then have an origin much closer to its mating connector
- These connectors currently mate with the booms, which require much less force to disconnect and connect
- Connor mentioned we have a process in production currently when making the branch cable to give the wires more strain protection
- As it might be easier to make this adjustment than relocating the origin of the line - I could follow up with connor to learn more

### Jeremy Kostel, 2024-08-21

FYSA @Cameron Chapman

## Attachments (9)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [107-102264_d dual current sense, assembly 1 (1).pdf](attachments/22539_107-102264_d%20dual%20current%20sense,%20assembly%201%20(1).pdf.md) | pdf | 714 | 2024-08-21 | converted |
| 212ae690-56ac-4093-92e9-f9d6eb6e058d.jpg | image | 71 | 2024-08-21 | listed only |
| 302b7ad1-305d-457e-8922-23ff97504607.jpg | image | 70 | 2024-08-21 | listed only |
| 67e69af7-dee4-45d4-95e2-1a27bfa26a46.jpg | image | 53 | 2024-08-21 | listed only |
| IMG_0022.jpg | image | 6533 | 2024-08-21 | listed only |
| IMG_0025.jpg | image | 6649 | 2024-08-21 | listed only |
| Image (1).jpg | image | 240 | 2024-08-21 | listed only |
| image-20240821-201633.png | image | 464 | 2024-08-21 | listed only |
| image-20240821-204314.png | image | 170 | 2024-08-21 | listed only |
