# VXEP-297: (ITAR, no data in Jira) Integrate Aim-lock munition control system into VXE30 and conduct demo

- **Issue type:** Major Project
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2024-03-05
- **Updated:** 2025-03-11
- **Resolved:** 2024-10-02
- **Reporter:** Greg Fryer
- **Creator:** Greg Fryer
- **Parent:** VXEP-434 Wing Utility Drop & Integration of ESAD/Fires support
- **Product/Tech Owner:** Charles David Madewell
- **Program (Marquee):** ESAD/Fires & Drop Payloads
- **Job Number:** J100129 - VXE Gimbal & Payload Support & Sustainment

## Description

Create a wing drop-payload kit including the Aimlock system. Will require a new physical package, likely connector selection, new harness(es), and software updates to detect it’s presence and communicate with it. Unknown what activation system is, hopefully independent access via network.
Estimate (includes prototype and full release to production), by GF. No data.
200 hours Mechanical - 3-4 weeks
300 hours Electrical - 4-5 weeks (assumes signals do not match existing interfaces)
300 hours Software - 6 weeks (assumes no ground side SW, and we are just routing flight data to Aimlock)
150 hours Test - 1.5 weeks (assumes on-site Aimlock support, if on-call will be more & slower)



Aim-Lock POCs:
Lacey Hays - PM Director
Craig Elder - R&D DR
Kayla Kozlowski (KK) - Ent. Com Coordinator
Kalia Davis SW Eng Mgr

## Comments (3)

### Greg Fryer, 2024-03-14

Aim-Lock meeting on 3/14:
One CPM handles two drop payloads. 
1k-2k PWM (compare to existing).
>Can retaining be done without power. Document the positions and servo commands.
>Could load be mechanical only? Aim-Lock can probably adapt to what we have.
>Ethernet and application software on the GCS is good.
>Will need: position, altitude, wind speed est. (ICD to be forthcoming)
>Mission Compute will be needed. AL will send two waypoints (or could do a waypoint and heading).
>
Schedule:
CTM integration location (MS1). Mass of CTM is 510g, 330g housing, about 180g of electronics. 12-30w of power
MS2 - Provide detailed ICD. Environmental, cable, mechanical mounting. Deliver on the 22nd.

Flight test towards the last week of June as a target.

### Greg Fryer, 2024-10-02

No response after discussion on cost, assuming canceled. Can restore as needed.

### Automation for Jira, 2025-03-11

This item was removed from the Mission Control Dashboard.
LRR Priority was: 999.0
Company Priority was: 84.0
Current Sprint Priority was:

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [AimLock_SalesSheet_CORE_11 x 8.5_v2.pdf](attachments/19347_AimLock_SalesSheet_CORE_11%20x%208.5_v2.pdf.md) | pdf | 2919 | 2024-03-14 | converted |
