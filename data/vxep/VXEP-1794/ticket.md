# VXEP-1794: VXE 820 Fuel Cell not charging HLB in flight

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2026-03-24
- **Updated:** 2026-09-28
- **Resolved:** 2026-07-20
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Charles Sweet
- **Creator:** Alexander Alan Arnold
- **Labels:** Ann_Arbor, MOLSON, RCCA, Weekly-incident-tracker
- **Links:** relates to VXEP-1799 (B30 VXE 820 Forced to use ELZ due to HLB being to low to VTOL land safely); relates to VXEP-1586 ( VXE 593 smoking fuel cell)
- **Customer:** MOLSON
- **Vehicle Tail Number:** VXE 820
- **Vehicle Configuration:** ADV NAV, VXE SUAV, SOFC, 140G2
- **Severity:** 1 - Flight Critical

## Description

Fuel Cell failing unable to charge HLB on flight due to high power demand for sustained duration.
Sam M. Looked through the data last night and informed customer they were climbing higher than 500 ft at time which could cause their issue. We need verification that this was the root cause and that the fuel cell appears to be operating normally. Sam also was asking if an SB needs to be generated to allow him to increase the hybrid lift battery charge level that triggers the 500W turbo mode – maybe increase from 50% to 70% or even 90% for Adv Nav? 
@Sean Wendling  - Fuel Cell was operating normally, but this is only confirmed by the Fuel Cell Log file, Xcomm data was not available in the AAR. HLB was rebounding in state of charge, but comms is lost midflight.

## Plan

- XCOM data not present. Request from customer.
- Lost comms reported/indicated by fuel cell log gaps. Identify why and if this issue should be tracked in a separate issue.

## Issue Status

From 3/25 call: 400s or so, fuel cell lost comms. XCOM and VTOL log not in AAR.
Fuel cell was making 450W the entire time. HLB draw was fluctuating.

## Comments (10)

### Alexander Alan Arnold, 2026-03-24

@Sean Wendling Data is in here from the email I sent this morning, I will upload a description once i read through the signal chat where this was reported.

### Drew Hildreth, 2026-03-25

** Need FTP **

### Sean Wendling, 2026-03-25

Battery Performance as recorded by “FuelCellLog” on GCS. Battery was getting recharged.
[embedded: image-20260325-184424.png]

### Ronnie Baker, 2026-04-06

This AC has arrived in the RMA department.

### Scott Lovett, 2026-04-21

Unable to proceed without RMA paperwork.

### Michael Lindsay, 2026-04-21

Added AAR for last flight following belly landing.

### Michael Lindsay, 2026-04-21

Added AAR T115_V820_260326_163407_pack which is post belly landing AAR

### Drew Hildreth, 2026-06-22

@Sean Wendling is this good to close out since you said it was working as intended or are we continuing.

### Charles Sweet, 2026-07-20

@Drew Hildreth I discussed with Sean. This should be ready to close.

### Alexander Alan Arnold, 2026-07-20

SOFC operating as designed

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T115_V820_260323_183447_pack.zip | archive | 202 | 2026-03-24 | listed only |
| image-20260325-184424.png | image | 45 | 2026-03-25 | listed only |
| T115_V820_260326_163407_pack.zip | archive | 477 | 2026-04-21 | listed only |
