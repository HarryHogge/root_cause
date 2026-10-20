# VXEP-1639: E95 S/N E8093 experienced multiple issues during NSW IQT

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
- **Problem Type:** Discovered Issue
- **Severity:** 2 - Degraded Performance - No Workaround
- **Components (EA Aircraft):** Payload, E95

## Description

Gimbal would not connect in VXESUAV software, would not power off through custom payload controls, and would make random un-commanded movements.

## Vehicle Configuration

Battery
VXESUAV
AdvNav
E95

## Comments (6)

### Mike DeJesus, 2025-12-22

@John Gober please report E95 findings on this Jira ticket.

### John Gober, 2025-12-22

Tested E95’s EPS 8090 and EPS8093 after they were returned.
Test Conditions:
Gimbal: EPS8093
Gimbal installed in T/N: 758 (Standard VXE30)
Power Source: VXE Main Battery
Connection:  Connected at Hood Payload - No Silvus
Test Locaton: HSV Eng Lab (Inside under repeater)

EPS8093 Results:
Video is very jerky. Mike thinks it may be configuration problem with the video encoder 
Motors operate smoothly and did what they were told 
This unit did get a GPS fix
Errors: None

EPS8090 Results on VXEP-1637
[embedded image-20251222-181509.png]
[embedded IMG_2720.MOV]

### Jackson Riley Curvin, 2026-01-14

Tested EPS 8093 
Test conditions
Power source: E95 quick connect bench cable
Connection: Serial and Ethernet
video was still jerky, still had GPS fix motors worked as expected.
[embedded MicrosoftTeams-video (4).mp4]

### Cody Smisek, 2026-01-22

@Jackson Riley Curvin would you be able to screenshot network, video, video player & common settings? Just curious what is set.

Is that the latest greatest windows 11? Does that have the fixes for windows 11 to support Epsilon?

### Jackson Riley Curvin, 2026-01-23

@Cody Smisek  this gimbal is already on its way back to Riga this was tested on my FSR GCS that was on windows 11 with a driver version that was previous to 2025. it was tested in multiple resolutions. The issue still remained.

### Alexander Alan Arnold, 2026-08-07

RMA complete gimbals repaired

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T115_V946_251208_091832_pack.zip | archive | 2467 | 2025-12-12 | listed only |
| T115_V946_251208_142019_pack.zip | archive | 2437 | 2025-12-12 | listed only |
| T115_V946_251208_153804_pack.zip | archive | 2188 | 2025-12-12 | listed only |
| IMG_2720.MOV | video | 19118 | 2025-12-22 | listed only |
| image-20251222-181509.png | image | 2322 | 2025-12-22 | listed only |
| MicrosoftTeams-video (4).mp4 | video | 7570 | 2026-01-14 | listed only |
