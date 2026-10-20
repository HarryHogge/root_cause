# VXEP-1485: VXE-499 Hard Landing/ HLB Cell Drop Out

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-08-22
- **Updated:** 2026-06-30
- **Resolved:** 2026-06-30
- **Reporter:** Jackson Riley Curvin
- **Assignee:** Stephen Peters
- **Creator:** Jackson Riley Curvin
- **Labels:** Edge_Asset, GS_Closed, HLB_bad_cell, Weekly-incident-tracker
- **Links:** relates to VXEP-1413 (HLB Issues 4139, 3908, and 3867); relates to VXEP-1412 (VXE 401 Aborted launch ); relates to VXEP-1407 (VXE 801 Hard landings after Aborts); relates to VXEP-1435 (VXE-674 Second Hard Landing)
- **Customer:** Redwire
- **Vehicle Tail Number:** VXE-499
- **Vehicle Configuration:** VXE-30 Battery Config.
- **Problem Type:** Other (explain in description)
- **Root Cause:** HLB cell drop out
- **Incident Type:** Near Miss
- **Severity:** 3 - Degraded Performance - With Workaround
- **Components (EA Aircraft):** Aircraft, full assembly

## Description

Launch wizard and initial launch nominal. Approximately 5-10 seconds into launch, launch was abort (messages populated in VTOL control window - see screenshot in folder above). I did not see if the battery imbalance turned red in the VTOL control window due to student manipulating VTOL Control Window since it was overlapping with Active User Landing Control. Once groundcrew said aircraft was on ground, cut and safed motor.
HLB SN:2-2628
DOM:240214
Cycle Count:4

## Plan

1: FSRs will try and collect previous AARs with battery serial number
2: Try and determine how long battery was in storage

## Comments (6)

### Jackson Riley Curvin, 2025-08-22

[embedded image-20250822-141332.png]

### Jackson Riley Curvin, 2025-08-22

FYSA @David Grosher @Cameron Chapman just received word this morning that the FLOPs team in Riga had a hard landing. I reviewed the data and found that cell 2 on the HLB dropped to Zero. I told them to quarantine the battery and that they are good to keep flying the aircraft.

### Pat Wells, 2025-08-22

@Sean Wendling @Tom Westrich

### Cameron Chapman, 2025-08-22

@Jackson Riley Curvin how do the cells look during launch wizard motor tests? I am wondering  if bad cells like this could be caught then. Could you post plots of that time?

### Jackson Riley Curvin, 2025-08-23

@Cameron Chapman I had the same thought as well but that screen shot is the whole AAR but I do wonder if we bumped up the motor test up to 100% if we could see it then?

### Jackson Riley Curvin, 2026-06-30

Closing battery was quarantined, added to master ticket.

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| HLB Battery-vxe-499.jpg | image | 1912 | 2025-08-22 | listed only |
| MISB-08222025-123056-0.mpg | video | 3038 | 2025-08-22 | listed only |
| MicrosoftTeams-video (1).mp4 | video | 2745 | 2025-08-22 | listed only |
| T95_V499_250822_123044_pack.zip | archive | 1260 | 2025-08-22 | listed only |
| [VXE499 22Aug2025 Mishap Reporting Procedure Form.pdf](attachments/31696_VXE499%2022Aug2025%20Mishap%20Reporting%20Procedure%20Form.pdf.md) | pdf | 428 | 2025-08-22 | converted |
| image-20250822-141332.png | image | 28 | 2025-08-22 | listed only |
| vxe49922Aug1.trl | other | 1 | 2025-08-22 | listed only |
| vxe49922Aug1.vmis | other | 4 | 2025-08-22 | listed only |
