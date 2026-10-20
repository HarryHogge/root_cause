# VXEP-1688: Limit In-Use HP Radios (2124664-01) Tx Power & Frequency. Update documentation and training until resolved.

- **Issue type:** Corrective Action
- **Status:** New
- **Priority:** Low
- **Created:** 2026-01-30
- **Updated:** 2026-06-02
- **Reporter:** Jacob Troyer
- **Assignee:** Josh Burrell
- **Creator:** Jacob Troyer
- **Parent:** VXEP-1671 HP Radio IPCOMM Component Ratings Exceeded

## Description

NOTE: Everything below is applicable only to the High Power (HP) Silvus Radio (10W), not the Standard Silvus Radio (4W). There are no additional transmit power or frequency range limitations required for the Standard Silvus Radio (4W).

An analysis was performed on the Silvus High Power Radio (2124664-01) and found that certain components on the IPCOMM board (1610P01-02) may be exceeded when the radio is at max transmit power and in the C-Band frequency range.
- Analysis JIRA: https://jenaero.atlassian.net/browse/AV-532
- Problem JIRA: https://jenaero.atlassian.net/browse/VXEP-1671

Corrective Action: For any HP Silvus radios in use, it is suggested to limit transmit output power to 4W and the frequency to the 2200-2500 MHz band (see https://jenaero.atlassian.net/wiki/spaces/EE/pages/859734046/Product+Radio+and+Antenna+Map).

## Issue Status

Until PCB is updated for the high power radios. Keep the transmit power at 4W and the frequency in <2500 MHz (S-Band). FYI @Cody Smisek @Josh Burrell  @Grace Burgess 
- @Drew Hildreth is anyone using high power radios with LEMB batteries? They may stop working <18V (LEMB voltage when nearly empty)

## Comments (8)

### Josh Burrell, 2026-02-09

@Jacob Troyer @Cameron Chapman Do we know if this is something that will be fixed for the first BLK 40 deliverers?

### Josh Burrell, 2026-02-09

@Mark Spence FYSA please take a look at adding something into the OPS manuals.

### Mark Spence, 2026-02-09

@Cameron Chapman @Jacob Troyer Do we know what aircraft or customers this will effect?

### Cameron Chapman, 2026-02-10

@Mark Spence All upcoming B40 aircraft. 35Y aircraft had high power radios, but they have been returned. @Erik Hanson  did any others? I don’t think so.

### Cameron Chapman, 2026-02-10

@Josh Burrellprobably not. Those aircraft have already been built with the existing radios and PCBs, and this project is not a high priority.

### Mark Spence, 2026-02-19

@Cameron Chapman @Jacob Troyer I’m working on the documentation for the 40 manual and would like to confirm one point. Is it correct that customers using the HP radios will NOT have access to the C- band frequency range (4400-4940)? Even if it’s set to 4W?

### Jacob Troyer, 2026-02-19

@Mark Spence Yes that’s correct. With the current IPCOMM boards, the radio should be limited to 4W and remain in S-Band (2200-2500).

4W limits the amount of continuous power only. The frequency range limits the amount of continuous and peak power. The peak power in C-band (4400-4940) exceeds the rating on the output inductor on the IPCOMM board.
I was out on leave for 2-weeks, so I’m not sure if any progress has been made towards updating the board (and/or testing it).

### Cameron Chapman, 2026-02-19

@Jacob Troyer@Mark Spence  Not much progress on the next board. Limitation should stay in effect until this is released and tested, then the limitation can be lifted on radios with these boards. https://jenaero.atlassian.net/browse/AV-564

## Attachments (0)
