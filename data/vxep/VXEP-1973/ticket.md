# VXEP-1973: Do battery math, contact ConnectTech

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2026-07-30
- **Updated:** 2026-08-08
- **Resolved:** 2026-08-08
- **Reporter:** Connor Peebles
- **Assignee:** Connor Peebles
- **Creator:** Connor Peebles
- **Parent:** VXEP-1964 Nail down Hadron design incorporation
- **Epic Link:** VXEP-1964

## Description

ask CTI if rtc port on hadron supports rechargable battery
do math for CTI supplied battery harness CTIC-00477(0.02).cdr

## Comments (1)

### Connor Peebles, 2026-08-08

ConnectTech confirmed that the RTC connector on either Hadron does not support a rechargable battery.
RTC current on the OrinNX = 12 to 50μA = 0.012 to 0.050mA
CTI supplied battery harness = 225mAh
BattLifeMin = 225mAh / 0.050mA = 4500hrs = 1/2yrs
BattLifeMax = 225mAh / 0.012 = 18750hrs = 2.1yrs

## Attachments (0)
