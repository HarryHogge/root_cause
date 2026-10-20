# VXEP-1035: Inspect V598 Hardware

- **Issue type:** Sub-task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2025-02-18
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Jeremy Kostel
- **Assignee:** Adrian Garcia
- **Creator:** Jeremy Kostel
- **Parent:** VXEP-999 VXE 598 with VXE 596 Center Wing. Lost connection to VTOL AP and ADB and crashed. 

## Issue Status

Copied from main ticket: 
The main battery cell voltage readings indicate an abnormal condition. The total voltage is measured at 12.97V, but Cell 0 is not being detected, and the remaining cells are all operating below their nominal voltage levels of 3.6V. It is unclear whether this issue happened during flight or resulted from the crash.
Additionally, the vehicle was not located until several hours after the crash. During this time, it remained powered on, gradually depleting its battery voltage. Just before the vehicle shut down, the main battery registered a voltage of 25.2V.
Moreover, analysis of the most recent XCOM log reveals that the battery voltage initially measured 29.3V and steadily declined to 27.6V over a span of 2.2 hours. This suggests a slow discharge process leading up to the final recorded values.

Hardware: 
Avionics and VTOL were powered separately to prevent potential power failures from affecting both systems. When powering the Avionics, the Fuselage Power Harness was unusually difficult to fully mate, requiring more force than usual (though the exact force required is subjective, it felt noticeably harder to connect). Despite this, the Avionics powered on normally, drawing an average current of 0.4A. The 12V output from the fuse measured 12.8V, which was expected. Similarly, the VTOL AP board powered on as expected and measured 12V. All connectors appeared intact and undamaged. Images are in the comment.

## Comments (3)

### Jeremy Kostel, 2025-02-18

Inital findings:
As expected aircraft sustained damage during the crash
- airframe
- Nose cone has caved in from impact
- several chips and cracks in the airframe
- When removing nose, all connectors were still mated and appear unaltered
- all still had solid mating connection
- Fuse power harness
- AS150 antispark on the Fuse Power harness measuring ~27 ohms (6 ohms expected)
- No visible damage or sparking on any of the fuse power harness connectors
- something to note: potting on AS150 antispark connector leaked through the housing and covers the soldering hole on the side of the contact

### Adrian Garcia, 2025-02-19

[embedded: image-20250219-185630.png]
[embedded: image-20250219-185642.png]
[embedded: image-20250219-185713.png]

### Adrian Garcia, 2025-02-21

copy from main ticket: I inspected the Main Battery and did not observe any visible damage. I also tested the cell voltages on the harness connected to the cell taps, and the readings aligned with those from the charger. @Hayden Jeanor suggested that a minor short may have occurred after the crash, potentially causing a slow discharge over time, which could explain the current cell voltage levels. @Cody Smisek and @Hayden Jeanor suggested to measure the resistance from the black alden to the fuse power harness so that will be my next steps. However, as highlighted in the root cause section, I believe the root cause is due to bad mating on the main battery. This would explain the brown out at the higher altitude and the voltage drop seen in the logs.
[embedded: image-20250221-211831.png]
[embedded: image-20250221-211840.png]
[embedded: image-20250221-211846.png]
[embedded: image-20250221-211853.png]

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20250219-185630.png | image | 12334 | 2025-02-19 | listed only |
| image-20250219-185642.png | image | 13379 | 2025-02-19 | listed only |
| image-20250219-185713.png | image | 21529 | 2025-02-19 | listed only |
| image-20250221-211831.png | image | 952 | 2025-02-21 | listed only |
| image-20250221-211840.png | image | 11896 | 2025-02-21 | listed only |
| image-20250221-211846.png | image | 10453 | 2025-02-21 | listed only |
| image-20250221-211853.png | image | 11321 | 2025-02-21 | listed only |
