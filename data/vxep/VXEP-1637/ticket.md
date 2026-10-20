# VXEP-1637: E95 S/N E8090 experienced multiple issues during NSW IQT

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-12-12
- **Updated:** 2026-08-07
- **Resolved:** 2026-08-07
- **Reporter:** Michael Mohr
- **Assignee:** Mike DeJesus
- **Creator:** Michael Mohr
- **Labels:** NSW, Weekly-incident-tracker
- **Links:** relates to VXEP-1635 (During NSW IQT, both customer E95 gimbals had multiple issues connecting to three different Advanced Nav aircraft used during training. Also, the gimbals would not power off when cycling power in the custom payload control in VXE-SUAV.)
- **Customer:** NSW
- **Vehicle Tail Number:** VXE-956
- **Severity:** 2 - Degraded Performance - No Workaround
- **Components (EA Aircraft):** Payload, E95

## Description

Gimbal would not connect in VXESUAV software, would not power off through custom payload controls, and would make random un-commanded movements.

## Vehicle Configuration

Battery
VXESUAV
AdvNav
E95

## Comments (4)

### Mike DeJesus, 2025-12-22

@John Gober please report E95 findings on this Jira ticket.

### John Gober, 2025-12-22

Tested E95’s EPS 8090 and EPS8093 after they were returned.
Test Conditions:
Gimbal: EPS8090
Gimbal installed in T/N: 758 (Standard VXE30)
Power Source: VXE Main Battery
Connection:  Connected at Hood Payload - No Silvus
Test Locaton: HSV Eng Lab (Inside under repeater)
 
EPS8090 Results:
Video seems good
No GPS fix
Errors: GPS No Communications, GPS Init Failed. 
Gimbal makes strange noise when stowed. Changed Stow location – still makes noise. 
The noise was captured in the video – make sure your volume is turned up. 
 
EPS8093 Results on https://jenaero.atlassian.net/browse/VXEP-1639
[embedded: image-20251222-181307.png]
[embedded: IMG_2733.MOV]

### John Gober, 2026-01-14

@Jackson Riley Curvin

### Alexander Alan Arnold, 2026-08-07

closing since cable modification solved issue

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Spinning E95.mp4 | video | 6183 | 2025-12-12 | listed only |
| T115_V956_251208_093736_pack.zip | archive | 2161 | 2025-12-12 | listed only |
| T115_V956_251208_102645_pack.zip | archive | 1959 | 2025-12-12 | listed only |
| T115_V956_251208_114515_pack.zip | archive | 1923 | 2025-12-12 | listed only |
| E8090.mov | video | 8400 | 2025-12-15 | listed only |
| Error list.jpg | image | 21 | 2025-12-15 | listed only |
| IMG_2733.MOV | video | 59850 | 2025-12-22 | listed only |
| image-20251222-181307.png | image | 1132 | 2025-12-22 | listed only |
