# VXEP-1651: New GSC alden harnesses are not compatible with old connectors. They are supposed to be. Complete interconnects and figure out why, and what to do.

- **Issue type:** Epic
- **Status:** New
- **Priority:** Low
- **Created:** 2025-12-17
- **Updated:** 2026-09-23
- **Reporter:** Cameron Chapman
- **Creator:** Cameron Chapman
- **Labels:** Electronics_Drafting
- **Parent:** PLD-144 Release Architecture and interconnect diagrams for E95 then E140

## Description

Plan: I think we can/should make a universal GSC to be compatible with both E95 and 140. Daniel Herrera William Dresser can you please work on that? I think you could provide splice relay power to alden 52 and 34, and the same for rtns. If we want the cable to be able to activate the relay (switch the SSR or DCDC, then adding a basic switch or connector on those lines for the GSC seems like it would work. Connor Peebles John Gober thoughts?
 Until then, we could mark cables as E95 or E140 only


Gimbal harness
[embedded: image-20251217-205814.png]
Branch cable 
[embedded: image-20251217-205832.png]


Teams message John Gober: Here is the LV Ground Support Cable revised for use with the new regul... | Octopus Tagup | Microsoft Teams
Here is the LV Ground Support Cable revised for use with the new regulator/PCB/mount.  Also on the vault.  Two first articles have been made. David was using one for his stand testing. Sending the second to Connor as soon as I can check with Mike. 
Rework EH-003-012-00 REV - to 2129334-01 REV A1 (Draft-NFP).pdf
 
[embedded: image-20251217-203139.png]
[embedded: image-20251217-203130.png]
Here is the analysis 

 
Here are the steps to fix it.  Note when I went to do the schematic, I noticed you had the shield on pin 40 so I left ground there on the first articles.  

 
Thank you John. Can you please capture such issues in JIRA in the future? Info and tasks are easier to track and not lose there vs chat
 
depending on the details, this could drive a quarantine

## Plan

- @William Dresser @John Gober quarantine all GSCs built incorrectly.
- Update documents for correct pinout.
- C/CA. ensure that such drawings are reviewed and cables tested before building and releasing. https://jenaero.atlassian.net/browse/VXEP-1606

## Comments (0)

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20251217-203130.png | image | 14 | 2025-12-17 | listed only |
| image-20251217-203139.png | image | 280 | 2025-12-17 | listed only |
| image-20251217-205814.png | image | 187 | 2025-12-17 | listed only |
| image-20251217-205832.png | image | 353 | 2025-12-17 | listed only |
