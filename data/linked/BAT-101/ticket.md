# BAT-101: Battery Charger software update, correcting input DCDC failure when power supply drops

- **Issue type:** Bug
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-09-01
- **Updated:** 2026-03-02
- **Resolved:** 2025-09-18
- **Reporter:** Tom Westrich
- **Assignee:** Tom Westrich
- **Creator:** Tom Westrich
- **Fix versions:** 03/02/2026
- **Parent:** BAT-83 NCR-250626 - 6536
- **Links:** relates to VXEP-1472 (LRR LEMB Chargers (Stalker 28V Battery Charger) smoking)
- **Epic Link:** BAT-83

## Comments (7)

### Tom Westrich, 2025-09-01

Power supply startup shows no significant overshoot in voltage (<4V), as well as a slow turn on from a 0V state (~150ms).  Also observed no ringing in input voltage, suggesting that power supply stability during a turn on event is not likely an issue.
[embedded: IMG_2993.jpg]

### Tom Westrich, 2025-09-01

Power supply shutdown shows no significant voltage ripple, and a substantial turn off period (45V to 30V in 460ms).  Clean shutdown is likely not an issue.
[embedded: IMG_3041.jpg]

### Tom Westrich, 2025-09-01

The slow power supply testing shows that it may be possible to have a faster software loop responding to changes in the input power supply voltage

### Tom Westrich, 2025-09-01

Action 1: Updated the Maximum Output Voltage variable in the model to be 35V, rather than tied to the battery voltage setpoint (100%, 60%, 25% charge, etc.).  This will force the output voltage control variable to cap the DCDC output voltage response to 35V when the battery is disconnected during a charge cycle, limiting damage to the charger circuitry.  This also allows the DCDC converter to operate with a high voltage control point to prevent backfeeding battery power.

### Tom Westrich, 2025-09-18

Action 2: Updated charger software to detect a fluctuation in input voltage (presumably due to noisy/bad input power supply), and then simultaneously force the charger to operate in “Burst Mode” AND reduce the DCDC power target at a rate of 800W/s.
In the event of a brownout, the input voltage would fall below a pre-determined threshold (35V = Max Output Voltage) - whi.ch is still above the battery voltage (max of 30.1), and toggle the Burst Mode on the DCDC to prevent any backfed power to the DCDC chips.  An additional change to increase the power ramp down rate was implemented to allow the DCDC PID loops to spool down and force the DCDC converter to turn off

### Tom Westrich, 2025-09-18

Testing protocol:
- Install and charge an LEMB at full rate (18.6A)
- Unplug 110VAC input power from Charger Power supply
- Verify that no damage occurred.


Testing passed on all three chargers with version 1.2.35 of the charger software.  Released to chargers in HSV, and updated on 9/4/25

### Tom Westrich, 2025-09-18

Action 4 (missed in earlier documentation):
Add DCDC temperature control logic to prevent overheating of the DCDC converter during LEMB charging.  Temperature control point of 100C currently installed.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IMG_2993.jpg | image | 2380 | 2025-09-01 | listed only |
| IMG_3041.jpg | image | 2680 | 2025-09-01 | listed only |
| SFT0065_CHARGER_1p2p35.bin | other | 239 | 2025-09-18 | listed only |
