# VXEP-1681: 111-115715 production request to make qty. 3 more of those harnesses for our IBs.

- **Issue type:** Sub-task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-09-20
- **Updated:** 2026-01-29
- **Resolved:** 2026-01-29
- **Reporter:** Hayden Jeanor
- **Assignee:** Giovanni Gonzalez
- **Creator:** Hayden Jeanor
- **Parent:** VXEP-1673 Build and document EE ironbirds
- **Links:** relates to VA-222 (2119518-01 AUX HOOD CONN TO RJ-45 PLUG Cable for SCO)

## Description

create a test harness to ‘breakout’ the bulgin payload port of the avionics box. Harness to replicate from production Iron Bird:
[embedded: image-20240920-172343.png]

[embedded: image-20240920-172405.png]

## Plan

- borrow cable to replicate from electronics IB
- ensure test cable allows IB to connect to vehicle over ethernet
- create a drawing for the test harness
- Effectively, breakout the 12V and ethernet lines from the bulgin connector of the payload connector board (P/N: 965-0-01-2008)
- a good reference cable is the HD payload interface cable (P/N: 106-104299) that uses the same connector your cable will
- do design in altium
- use https://jenaero.atlassian.net/wiki/spaces/EE/pages/169214153/Schematic+and+PCB+Style+Guide , https://jenaero.sharepoint.com/:x:/r/sites/EngineeringTeam/_layouts/15/Doc.aspx?sourcedoc=%7BD9683083-DE28-455A-9ABE-AD7432BF942C%7D&file=Harness%20Design%20Checklists.xlsx&wdLOR=cF341A190-F6E1-43E2-9A7C-267FC501FC1B&action=default&mobileredirect=true , https://jenaero.atlassian.net/wiki/spaces/EE/pages/357335127/Altium+Harness+Designer+Style+Guide+Procedure , and https://jenaero.atlassian.net/wiki/spaces/EF/pages/15597578/File+Naming+and+Part+Numbering  (sorry for the link overload)
- send to hayden for peer review
- submit production request for first article build 
- implement feedback from production into drawing
- release drawing
- final peer review
- submit for approval

## Comments (9)

### Hayden Jeanor, 2024-09-20

@Giovanni Gonzalez feel free to ask me or gary any questions when you run into them. FYI @Gary Angelus

### Cameron Chapman, 2024-09-20

@Hayden Jeanor and @Giovanni Gonzalez a few ideas.
- This cable or similar is already documented in some ways. [embedded: 107-111892 Bulgin Checkout Harness Pinout.xlsx]
- Unless you need to test avboxes without the rest of the IB, I'd prefer to build more 111-115715, which does the same thing, is already designed, and is much easier to connect to vehicles. also the bulgin connector is replaced with MAGNSS.
- We may have some of these in inventory we never plan to use, in which case, you could reterminate to RJ45[embedded: 111-105263 BULGIN PAYLOAD CABLE, JUMPER, PINOUT.xlsx]

### Hayden Jeanor, 2024-09-23

@Cameron Chapman thanks for stopping us. @Giovanni Gonzalez  yes, the 111-115715 should serve the same purpose we need, so lets just put in a production request to make qty. 3 more of those harnesses for our IBs. Canceling this ticket.

### Cameron Chapman, 2024-09-23

@Hayden Jeanor @Giovanni Gonzalez reopening this ticket and renaming to track that task.

### Cameron Chapman, 2024-09-23

We should resolve the items in this task in parallel https://jenaero.atlassian.net/browse/VA-222

### Giovanni Gonzalez, 2024-09-23

Production request has been submitted.

### Giovanni Gonzalez, 2024-09-23

Harnesses are expected to be completed mid-November due to production and electronics main focus being on the practice builds.

### Gary Angelus, 2024-09-24

@Giovanni Gonzalez When you have a tentative parts list give me a copy and I’ll update the Altium library, so they are available for you to use.
@Hayden Jeanor

### Giovanni Gonzalez, 2024-09-25

@Gary Angelus We are straying away from replicating the harness from electronics and making a drawing for it. Instead, we are requesting harness [embedded: 111-115715 Mod Payload Port Diagnostic Harness, BOM.xlsx] which serves the same purpose and is already documented.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [107-111892 Bulgin Checkout Harness Pinout.xlsx](attachments/23337_107-111892%20Bulgin%20Checkout%20Harness%20Pinout.xlsx.md) | xlsx | 41 | 2024-09-20 | converted |
| [111-105263 BULGIN PAYLOAD CABLE, JUMPER, PINOUT.xlsx](attachments/23338_111-105263%20BULGIN%20PAYLOAD%20CABLE,%20JUMPER,%20PINOUT.xlsx.md) | xlsx | 54 | 2024-09-20 | converted |
| image-20240920-172343.png | image | 12504 | 2024-09-20 | listed only |
| image-20240920-172405.png | image | 20530 | 2024-09-20 | listed only |
| [111-115715 Mod Payload Port Diagnostic Harness, BOM.xlsx](attachments/23364_111-115715%20Mod%20Payload%20Port%20Diagnostic%20Harness,%20BOM.xlsx.md) | xlsx | 12 | 2024-09-25 | converted |
