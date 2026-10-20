# VXEP-1195: Decide if E140 requires a regulator to work with LEMB

- **Issue type:** Sub-task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-04-08
- **Updated:** 2025-04-09
- **Resolved:** 2025-04-09
- **Reporter:** Cameron Chapman
- **Assignee:** Mike DeJesus
- **Creator:** Cameron Chapman
- **Parent:** VXEP-1151 Test Epsilon 140 G2 input voltage down to 17.5V
- **Links:** relates to VXEP-1194 (Update E140 payload harness 101-106864 to include laser enable like in 2118386-01)

## Description

Greg’s request:
I talked to Mike, he is meeting with Riga first thing tomorrow (Guks, specifically, hopefully he is free) to try and get a clear answer on "if the gimbal powers up at a lower voltage, will it then perform (stabilize and such) as normal?" If yes, then per John's earlier comment on testing, that indicates it's fine w/o the regulator.
 
To be clear, the testing is insufficent w/o that answer from Guks. Sure it turns on, but can it stablize the image when zoomed to 2km (or whatever the high-magnification distance/zoom level is).
 
(I can make up a technical story either way on it working or not, if it powers up - hence needing Guks)

## Plan

I talked to Mike, he is meeting with Riga first thing tomorrow (Guks, specifically, hopefully he is free) to try and get a clear answer on "if the gimbal powers up at a lower voltage, will it then perform (stabilize and such) as normal?" If yes, then per John's earlier comment on testing, that indicates it's fine w/o the regulator.

## Issue Status

Testing performed on one gimbal at 17.5V. E140G2 Z Low Voltage Testing (17.5V).xlsx
DECISION

Move forward with the DCDC regulator.
- John G's testing is insufficient to confirm gimbal performance at low voltages
- The primary concern is around things we've already spoke about, performance in flight/vibration/wind resistance etc
- Guks does not have operators or other resources to conduct tests that fit our timeline

## Comments (1)

### Tobi Ogunro, 2025-04-09

@Cameron Chapman & @Mike DeJesus I’ve updated this ticket with the decision. Closing ticket.

## Attachments (0)
