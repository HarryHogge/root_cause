# BAT-84: LRR charger repair prior to release to customer - march LRR delivery (2025)

- **Issue type:** Major Project
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-08-07
- **Updated:** 2026-04-20
- **Resolved:** 2025-10-30
- **Reporter:** Tom Westrich
- **Assignee:** Tom Westrich
- **Creator:** Tom Westrich
- **Fix versions:** 03/02/2026
- **Links:** relates to VXEP-1472 (LRR LEMB Chargers (Stalker 28V Battery Charger) smoking); Linked issue cannot finish until this issue finishes. BAT-117 (Charger software 1.2.35 Engineering testing); Linked issue cannot finish until this issue finishes. BAT-118 (Charger software 1.2.35 LEMB disengage charge bug); relates to BAT-148 (Apply 1.2.38 to Charger SN0024); relates to BAT-149 (Apply 1.2.38 to Charger SN0013 and test); relates to BAT-150 (Apply 1.2.38 to Charger SN0007 and Test)

## Description

Major project to track the development of 28V Battery Charger continued development.
Initial Delivery ~ 5/20/2025 from AA to SLO of 12 Chargers, Power Supplies, and Dischargers.
Feedback:
- Charge harness quality low
- Plugging in LEMB sometimes resulted in chip failure in charger
- User button interaction not functioning as anticipated
- Plugging in Main FCR resulted in damage to charger and Main FCR battery

Corrective actions:
- All harnesses fixed in HSV
- LEMB caused a voltage overshoot and ringing on the main bus of PCA0120 when installed.  The addition of 330uF capacitance reduced the overshoot from ~5-15V to less than 2V.  Additionally, a TVS diode (P4SMA33A) was added to the main bus to catch any voltage transients higher than 45V, in an attempt to further reduce any potential chip damage.
- Updated charger software per https://jenaero.atlassian.net/browse/BAT-54
- SLO labeled chargers with a Use for 35X label

Army Training Activity ~8/18/25 in HSV
Feedback:
- https://jenaero.atlassian.net/browse/VXEP-1472

Corrective actions:
- https://jenaero.atlassian.net/browse/BAT-101

Additional Engineering Testing 9/4-9/20
- Required tests
- total input power loss on power supply
- Power loss event (passing with 1.2.35)
- battery disconnection (passing with 1.2.35)
- power on event (sometimes failing with 1.2.35)
- Failure of TVS diode upon reconnection of power!https://jenaero.atlassian.net/browse/BAT-117
- battery reconnection (passing with 1.2.35 with exception)
- partial/fast power loss and recovery to power supply (untested with 1.2.35)
- Power loss event
- battery disconnection
- power on event
- battery reconnection
- disconnection of battery during charge (NOTE: this condition has not been protected)
- battery disconnection
- Some user / state machine interlock
- battery reconnection
- elevated temperature testing (untested with 1.2.35)
- charger in 40C hot/humid environment

## Comments (0)

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| SFT0065_CHARGER_1p2p38.bin | other | 240 | 2025-09-29 | listed only |
