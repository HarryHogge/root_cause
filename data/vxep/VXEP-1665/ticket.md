# VXEP-1665: 2123638-01 Rev A05

- **Issue type:** Sub-task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2026-01-23
- **Updated:** 2026-03-31
- **Resolved:** 2026-03-30
- **Reporter:** Connor Peebles
- **Assignee:** Connor Peebles
- **Creator:** Connor Peebles
- **Parent:** VXEP-1192 PCB - Wing Utility Pylon (FKA drop payload) - 2123638-01 Rev A

## Description

2123638-01 Rev A05 should get the following improvements;
ALL PARTS PULLED FROM EDGE AUTONOMY SLO PARTS LIBRARYRelated to above, ensure correct values, descriptions on all partsreplace CGA3E1X7R1V334K080AD with CGA3E1X7R1V334K080ACFor R3, R8- add CPF0603B34KE1 as primaryadd TNPU060349K9BZEN00 as primary to R10Fix footprints for C20, C23, C29 (LINE ITEM8) [MPN: GRM21BR61H106KE43L]C37 (LINE ITEM11) [MPN: C0402C103K3RALTU]Remove R28 and Q1, replace with a 10K resistor between 5V_EN and SERVO_ENInstall a 0 Ohm resistor between U3-RST_ENC and the D14,R13,C23 reset circuit?

## Comments (2)

### Connor Peebles, 2026-03-30

replaced all parts to pull from company library
removed Q1 NPN transistor, connected servo_en to MCU since it has internal pull up, worked in proto
several other small fixes

### Connor Peebles, 2026-03-30

Eng released on vault, sending out to vendor

## Attachments (0)
