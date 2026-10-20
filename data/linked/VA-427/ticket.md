# VA-427: Record pins with conformal coat intrusion. Install the VTOL+AP int board from this incident into a HIL

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-08-10
- **Updated:** 2023-11-09
- **Resolved:** 2023-08-14
- **Reporter:** Cameron Chapman
- **Assignee:** Mark Squillante
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-41 (TPTR-74 VXE 510: (VTOL AP WD) Consolidated Watch Dog tracking)
- **Sprint:** VXE-1 EE Team Sprint 8/28-9/17

## Description

Red AP Interface board has conformal coat intruding into contacts of J19 and J20 (contacts that mate with processor board). 
Need to identify which pins specifically.
Then install this AP interface board (SN API-1-1123) into HIL.

## Comments (5)

### Mark Squillante, 2023-08-10

Looks like J20 connector has conformal coat in all of the pins to some degree.
[embedded: J20 pins 41-80.jpg]
[embedded: J20 pins 1-40.jpg]
J19 connector also has conformal coat in most of the pins. 
[embedded: J19 pins 1-40.jpg]
[embedded: J19 pins 41-80 also.jpg]
[embedded: J19 pins 41-80.jpg]
I suspect insufficient masking prior to conformal coating the board.

### Mark Squillante, 2023-08-10

@John Clark do you have a specific HIL box in mind you would like this installed into?

### Mark Squillante, 2023-08-14

Red AP processor board (1409P01D; 107-107307) SN APB-1-1288 paired with interface board (1901P01B; 107-107306) SN VAPI-1-1123 will be going into HIL box SN S-S100044 (HIL PN: 107-111759). I have not had time to install this yet due to https://jenaero.atlassian.net/browse/ENG-2207 taking higher priority but will install it as soon as possible.

### Mark Squillante, 2023-08-14

I finished swapping out the red AP processor board on HIL box SN S-S100044 and put on @John Clark's desk.
@Cameron Chapman

### Greg Fryer, 2023-08-30

Admin note, I moved this to be a task in VA, but it’s still closed. So no action needed.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| J19 pins 1-40.jpg | image | 6034 | 2023-08-10 | listed only |
| J19 pins 41-80 also.jpg | image | 5926 | 2023-08-10 | listed only |
| J19 pins 41-80.jpg | image | 5638 | 2023-08-10 | listed only |
| J20 pins 1-40.jpg | image | 5842 | 2023-08-10 | listed only |
| J20 pins 41-80.jpg | image | 5691 | 2023-08-10 | listed only |
