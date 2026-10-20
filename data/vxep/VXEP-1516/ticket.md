# VXEP-1516: Audible or visual Operator aircraft is powered on

- **Issue type:** Task
- **Status:** In Process
- **Priority:** Low
- **Created:** 2025-09-19
- **Updated:** 2026-07-10
- **Reporter:** Cameron Chapman
- **Assignee:** Cameron Chapman
- **Creator:** Cameron Chapman
- **Parent:** VXEP-1549 BLK 40 OPEN REQUESTS (Need to be prioritized)
- **Links:** relates to BAT-420 (There is no indication of HLB being in 'ON' state when removed from charger or aircraft (can be closed when all batteries shut off reliably)); relates to VXEP-1577 (56V on command); relates to XKIT-5125 (Power Button Issues and improvements.); relates to BAT-779 (Battery System Squawk List 2026 + AA support request priority from SLO perspective); relates to XKIT-5456 (Ranked B40 firmware electrical requests)
- **Epic Link:** VXEP-1549

## Description

CBP noted desire for some power on indication: https://jenaero.sharepoint.com/:w:/s/GlobalSupport2/IQAhDSqUEJ2xS4hcktakU1d4AbN1x1zql6SUr68TM_0E198?e=JCEc7n
FLOPS as well
I think Sam said multiple customers would not want lights to stay discrete, If using lights, they should be able to be enabled or disabled by operator selection and remember last setting. 

Ex: using blinker lights, especially when battery is critically low. If some customers don't want this for austere reasons, we could have it user configurable and discuss which should be defect. Multiple batteries killed during test could have been prevented with this. B30 had the CW light
Indicators for the following
- 28V on
- commanded 28V off
- Commanded 56V off, could use motor beep before powering off.

Options
- use the ailerons as “state identifiers”.  Example: First button press and the flaps rotate up.  Second press and they flap low and then return to normal.  Off and they return to normal, error and one goes high and one goes low.  Meets requirements of a visual indicator that does not involve unwanted noises or lights.
- During testing and for most customers, I think we should use nav lights to indicate power status, especially when low SOC on ground test, but we would need an option to default these off when customers desired that. (add to ini file or similar?)
- Use AP Int beeper. This would need a beeper attached to J23
- [embedded: image-20250919-164345.png]
Gets signal from VTOL AP.
- Ben Norris or Jeremy Kostel do you know if pegasus servos can be configured to do anything like beep or move on power up? that might be one of the easier to do items since it would just require a servo config change vs RW FW change

## Plan

- Look into options like servos to indicate 28V power up. @Ben Norris
- Look into if any GPIO could be set earlier in the process (ex: Fan on, blinker lights, etc.)
- Shorten button press times may help. See linked issue.

## Comments (0)

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20250919-164345.png | image | 72 | 2025-09-19 | listed only |
