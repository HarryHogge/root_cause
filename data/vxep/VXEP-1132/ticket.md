# VXEP-1132: Confirm Voltage Range for payload

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2025-03-12
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Scott Whitney
- **Assignee:** John Gober
- **Creator:** Scott Whitney
- **Parent:** VXEP-1131 CDR Action Items
- **Epic Link:** VXEP-1131

## Description

We will need to compare the range of what we will deliver in march to the range of the battery, and possibly add a regulator if those are not compatible.
17.5V pack cutoff and we're using 18V" -
Latest email: 
- The voltage range is 20 to 30 V

## Issue Status

Testing conducted on E140Z G2 at 17.5 Volts on 3-21-2025
https://jenaero.atlassian.net/browse/VXEP-1151 
On Thursday, March 13, I requested by email from Guks an analysis of whether the EA Latvia gimbals listed in the spreadsheet "VXE Payload List.xlsx" were compatible with the full voltage range of the new LEMB. Cameron Chapman was copied. We have not received a response.

## Comments (4)

### Cameron Chapman, 2025-03-19

@Tobi Ogunro @Scott Whitney @Matt Philley can you please add this as a blocker to your project schedules?

### John Gober, 2025-03-19

Sent to Aleksandrs Guks on 03-13-25 @ 15:46; Cameron Chapman and Charles Madewell copied

Hi Aleks,
 As you may be aware, SLO and Ann Arbor are developing a new Long Endurance Main Battery (LEMB) module.
 They are utilizing newer Silicon Anode battery cells which have slightly different voltages than we’re all used to working with.
 Our existing Main Battery has maximum voltage of 31.0V and the cutoff is 21.0V.
 The new LEMB will have maximum voltage of 29.4V and the cutoff is 18.0V.
 We are concerned about LEMB compatibility with the gimbal products at the lower end of the pack life – around the 18.0V level.
 Can you have someone verify operation from 18.0V to 29.4V for all released and shipped versions of these products?
 
| Model | Mfr | Power (typ) (W) | Voltage | VXE Status | VXE Interface | Schematic | Flight History |
| E140 G2 MWIR expanded voltage range | EA Latvia | 51 | 24V was default. 20-32VDC option. Need to verify version. Custom harness regulator used was 9-36V. | Prototype documented and flown? | BRANCH/GRY ALDEN | 101-109751 | Since ~2023? |
| E140 G2 MWIR | EA Latvia | ? | 24V was default. 20-32VDC option. Need to verify version. Custom harness regulator used was 9-36V. | Prototype documented and flown? | BRANCH/GRY ALDEN | 107-106488 | Since ~2023? |
| E180 | EA Latvia | 40 | 24V was default. 20-32VDC option. Need to verify version. Custom harness regulator used was 9-36V. | Not integrated, Havoc need to have list | N/A YET |  | None |
| E140Z G2 | EA Latvia | 36 | 24V was default. 20-32VDC option. Need to verify version. Custom harness regulator used was 9-36V. | Prototype documented and flown | BRANCH/GRY ALDEN | Old- 101-109034 Epsilon 140Z G2, WD.PDF 101-106864 Input Power Assembly, Epsilon 14oz G2_P1.pdf | Since ~2023? |
| E175 | EA Latvia | 35 | 24V was default. 20-32VDC option. Need to verify version. Custom harness regulator used was 9-36V. | Not integrated | N/A YET |  | None |
| E140 | EA Latvia | 20 | 24V was default. 20-32VDC option. Need to verify version. Custom harness regulator used was 9-36V. | Active, but close to obsolete, likely will not be purchased | BRANCH/GRY ALDEN | SLO does not have/has not tested | Since ~2023? Obsolete? |
| E140Z | EA Latvia | 20 | 24V was default. 20-32VDC option. Need to verify version. Custom harness regulator used was 9-36V. | Obsolete? | BRANCH/GRY ALDEN | SLO does not have/has not tested | Since ~2023? |
| E140LC | EA Latvia | 17 | 24V was default. 20-32VDC option. Need to verify version. Custom harness regulator used was 9-36V. | Active, but close to obsolete, likely will not be purchased | BRANCH/GRY ALDEN | SLO does not have/has not tested | Since ~2023? |
| E95 | EA Latvia | 12 | 24V was default. 20-32VDC option. Need to verify version. Custom harness regulator used was 9-36V. | Prototype documented and flown | BRANCH, BOOM MOUNTS (PROTOTYPE) | Search epsilon on vault. Populate here when you do | Since ~2023? |

 Please note this is tied to LRR and thus a high priority for the company. 
Thanks,
John Gober
Senior Electrical Engineer
Phone: +1-256-810-0219
Email: jgober@edgeautonomy.io

### John Gober, 2025-03-20

Aleks responded 3-20-25
We have never tested such low voltage. This might impact on motor performance. All our payloads are tested in the range of 20 - 30V. I believe we need to conduct some additional tests. Give me some time, I will discuss with the team if we have any 140G2 for tests. I think you can also perform testing on your units. I don't see any issue applying 18V. In the worst case the gimbal will not initialize.

### Tobi Ogunro, 2025-03-26

@Erik Hanson This ticket may provide some additional details regarding your question on Payload voltage.

## Attachments (0)
