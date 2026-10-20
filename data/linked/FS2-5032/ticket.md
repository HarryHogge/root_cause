# FS2-5032: v882 (UAP) - CAN Launch abort investigation

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2026-08-19
- **Updated:** 2026-09-01
- **Resolved:** 2026-09-01
- **Reporter:** Scott Whitney
- **Assignee:** Jeremy Kostel
- **Creator:** Scott Whitney
- **Parent:** FS2-4628 B40 UAP Open Investigations
- **Links:** relates to FS2-5029 (8/18 Flight CAs); relates to AV-1370 (SB35/40 Lift Motor Phase Lead Wear Investigation); relates to VXEP-1933 (VXE 1038 VTOL motors failed to shut off after transition to fixed wing flight)
- **Epic Link:** FS2-4628
- **Sprint:** FS2 Sprint 38

## Description

Review of the CAN log (Flights 1 and 2 plus the first launch abort) indicates CAN errors correlate strongly with VTOL motor/ESC activity.
ALL TIME LISTED BELOW IS REFERENCED TO CAN LOGGER TIME ONLY
- Flight 1: No CAN errors observed.
- Ground Ops (5000-6000s): A small number of error spikes were recorded. These may be expected and associated with vehicle power cycles, AP/XCOM reboots, or CAN logger battery swaps.
- Flight 2 VTOL Takeoff (7040-7078s): CAN errors began at ~7074s and continued until ~7079s, coincident with VTOL motor operation. Errors subsided once in fixed-wing flight.
- Flight 2 VTOL Landing (7490-7561s): CAN errors reappeared from ~7490s to ~7560s during VTOL motor activity.
- This suggests a correlation between CAN bus degradation and active VTOL ESCs (CAN nodes) operating under high-current conditions.
- CAN Health Abort Behavior: Unified Autopilot includes a CAN health launch abort feature. It is currently unclear why Flight 2 did not trigger an abort despite the observed errors. Additional review of the abort logic is required to determine whether this behavior was expected.
- Ground Ops (9209-9664s): Another block of CAN errors was observed while on the ground. These may also be attributable to expected events such as power cycles or system reboots.
- Flight 3 Takeoff Attempt: Takeoff throttle commands began at ~10227s and ended at ~10233s. CAN errors started at ~10228.5s and persisted until ~10233s, resulting in a launch abort.

[embedded: image-20260820-150417.png]

Flight Data: https://jenaero.sharepoint.com/:f:/s/IRAD/IgBrb05EOPqhRrc5k2fXxWgVAbFkNcoIvHJEx5uhBmFaRLU?e=VWs685

## Plan

Final Assembly is currently kitting and building a replacement right boom assembly to replace the damaged hardware identified during teardown.
The left boom requires reassembly prior to return-to-flight activities. Ownership of this effort is still being determined between Engineering and Final Assembly.
As part of the corrective action, Sanjay will implement the boom composite modifications required for the ESC phase lead protection rework to prevent recurrence of the identified failure mode.
Once the replacement right boom is received, all boom assemblies are reworked as required, and aircraft reassembly is complete, the aircraft will undergo LW ground checks in SCO to verify system integrity and aircraft readiness prior to resuming flight operations.

## Issue Status

UPDATE 8/31:
V882 Booms were rebuilt and hovered with V997 (standard B40 code). Hover went through with 0 CAN error frames. Booms are approved to be sent back into the field 
[embedded: image-20260901-143428.png]


Aircraft was reassembled following centerwing harness repair and additional troubleshooting. On 8/21/26, flight operations resumed with the newly repaired V882 CW installed. A launch abort occurred again, and CAN bus errors were observed during the event, indicating that the previous centerwing connector hypothesis was not the sole root cause.
At engineering's direction, the V882 booms were removed and replaced with V997 booms. Following the swap, the team successfully performed a launch abort with no CAN bus errors present. Subsequent flight testing on 8/24/26 consisted of three successful flights with the CAN bus remaining completely healthy throughout all phases of operation. These results isolated the issue to the V882 boom assembly.
During teardown and detailed inspection of the V882 booms, a scorch mark was identified on the exterior of the right rear boom (see attached photos). After removal of the motor and ESC, it was discovered that an ESC phase lead contact had worn through its protective heat shrink insulation. The exposed conductor made contact with the boom composite structure on one side and the motor housing on the other, creating an unintended electrical path. Evidence of electrical arcing and thermal damage was present at the location.
This failure mode is consistent with an ongoing known issue currently being addressed through the linked corrective action ticket. These booms had not received the protective rework that is presently being incorporated into production hardware.
Due to the extent of the damage, the right boom and associated assemblies are not repairable and will be scrapped. Production has been notified and is building a replacement boom assembly. The left boom remains serviceable and requires reassembly prior to return-to-flight activities.
Historical Note:
Earlier troubleshooting identified a bent and recessed dummy pin in the centerwing connector, and while attempting removal of the damaged pin and clip, a CAN H conductor separated from its crimp and required harness repair. Although these findings warranted investigation, subsequent testing and hardware teardown indicate they were not the primary cause of the recurring CAN bus faults.

## Comments (3)

### Jeremy Kostel, 2026-08-20

Plots from Scott Hunter
Flight 3
[embedded: image-20260819-194144.png]

Flight 2:
[embedded: image-20260819-194150.png]

### Jeremy Kostel, 2026-08-20

[embedded: image-20260820-193200.png]
[embedded: image-20260820-193147.png]
[embedded: image-20260820-193215.png]

### Jeremy Kostel, 2026-09-01

V882 booms have passed checkouts (hover with V997) and are fit to return to service

## Attachments (12)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20260819-194144.png | image | 958 | 2026-08-19 | listed only |
| image-20260819-194150.png | image | 1080 | 2026-08-19 | listed only |
| image-20260819-194144 (9240aca4-e1ff-48e8-af0a-118a11f8a95a).png | image | 958 | 2026-08-20 | listed only |
| image-20260819-194150 (0782ad6d-3d5e-4440-a7df-feb285b9c1f4).png | image | 1080 | 2026-08-20 | listed only |
| image-20260820-150417 (d186c867-bb7a-43fe-a7cc-e782f7f2e5cc).png | image | 69 | 2026-08-20 | listed only |
| image-20260820-193147.png | image | 2407 | 2026-08-20 | listed only |
| image-20260820-193200.png | image | 2075 | 2026-08-20 | listed only |
| image-20260820-193215.png | image | 3316 | 2026-08-20 | listed only |
| Image (15).jpg | image | 619 | 2026-08-25 | listed only |
| Image (16).jpg | image | 585 | 2026-08-25 | listed only |
| Image (17).jpg | image | 939 | 2026-08-25 | listed only |
| image-20260901-143428.png | image | 147 | 2026-09-01 | listed only |
