# VXEP-1782: Was 2127251-01 XCOM Changes for B40 UAP config 1 “CW UAP”

- **Issue type:** Bug
- **Status:** New
- **Priority:** Low
- **Created:** 2026-03-20
- **Updated:** 2026-04-13
- **Reporter:** Cameron Chapman
- **Creator:** Cameron Chapman
- **Parent:** VXEP-1781 Hardware changes for B40 UAP config 1 “CW UAP”
- **Epic Link:** VXEP-1781

## Description

B40 version https://jennings-aeronautics-2.365.altium.com/designs/E876BB46-618F-4EEC-945C-B4389FEEB76F
See here https://jenaero.atlassian.net/wiki/spaces/VXEA/pages/1025867793/UAP+Cross+Functional+Roadmap#XCOM 
- Threshold: 
- retract needed without red board. Discussed here Cameron Chapman: wed need a replacement for payload retract (or not be compatible ... | Stalker UAP Architecture | Microsoft Teams
- Greg “ all B30 payloads* are to work on B40 as well, w/o modification. (we maintained the same physical interface, for example).
 
*Excludes officially discontinued ones like the old Jennings gimbals.
**e.g. no repeat of the AdvNav issue of mount plate interference
***All that said, an adapter cable could be included if we had to.”
- Objective: See list in https://jenaero.atlassian.net/wiki/spaces/VXEA/pages/1025867793/UAP+Cross+Functional+Roadmap#XCOM


Retract: 
I think the RP* pins are remappable peripheral pins, that can be used for output compare. Checking against the VTOL now
 RPB3 for example looks unused
The FW AP will no longer be used and the RX line is connected to RPB15
 output pin table
[embedded image-20260320-220737.png]

[embedded image-20260320-220534.png]

I think this means we can turn RPB15 into OC5 or OC8....glad we are testing this but I think it makes sense
The other half, input table
[embedded image-20260320-220542.png]

## Comments (3)

### Cameron Chapman, 2026-03-20

Dave and Kurt recommended using something like RPB15 above (U2RX) This would require
- Cut trace between processor and U15. Difficult and risky.
- Skywire processor pin (difficult) to Alden
- [embedded image-20260320-222123.png]

Would one of these be an option? Ex: RC2=RPC2. This would require 
- Pull R190, skywire from R190 pad to Alden. No cutting traces or small processor pins required. Longer skywire run for PWM line, which may cause issues. We can look for shorter options.

[embedded image-20260320-222217.png]
[embedded image-20260320-222549.png]

### Connor Peebles, 2026-03-30

@Cameron Chapman RC2 is currently used to control power switching to the MCM. All those GPIOs are in use currently

### Cameron Chapman, 2026-03-31

[embedded image-20260331-211726.png]

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20260320-220534.png | image | 587 | 2026-03-20 | listed only |
| image-20260320-220542.png | image | 163 | 2026-03-20 | listed only |
| image-20260320-222123.png | image | 65 | 2026-03-20 | listed only |
| image-20260320-222217.png | image | 104 | 2026-03-20 | listed only |
| image-20260320-222549.png | image | 714 | 2026-03-20 | listed only |
| image-20260320-220737.png | image | 14 | 2026-03-23 | listed only |
| image-20260331-211726.png | image | 272 | 2026-03-31 | listed only |
