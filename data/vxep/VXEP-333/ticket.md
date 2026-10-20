# VXEP-333: VXE-522 / VXE-529 / VXE-508 Follow up testing: Investigate SD Card new and old PN's. Investigate how speed difference could affect XCOMM.

- **Issue type:** Sub-task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-04-08
- **Updated:** 2025-02-28
- **Resolved:** 2024-10-11
- **Reporter:** Connor Peebles
- **Assignee:** Connor Peebles
- **Creator:** Connor Peebles
- **Parent:** VXEP-236 Systemic SD card Investigation VXE-522 XCOM board failures at LM Source inspection
- **Links:** relates to RMA-230 (VXE 508 240325-2)
- **Plan:** - Sort out current and former part numbers first. https://jenaero.atlassian.net/browse/VXEP-235
- **Job Number:** J100084 - VXE Incident Investigation

## Description

U1/U2/U3 SD cards support their namesake data rates. The new SD cards are U3 compared to the older U1 SD cards. On the U3 cards, the caching mechanism is going faster using DDR3. We are not utilizing the full DDR3 lines, but the card is processing the one line we use faster. This results in “snappier” webpage loading.

## Comments (2)

### Connor Peebles, 2024-09-16

we’ll verify with @Abel J. Markow , but from his previous investigation it seems that we have plenty of open space left for extra speed on the SPI bus

### Connor Peebles, 2024-10-07

U1/U2/U3 SD cards support their namesake data rates. The new SD cards are U3 compared to the older U1 SD cards. On the U3 cards, the caching mechanism is going faster using DDR3. We are not utilizing the full DDR3 lines, but the card is processing the one line we use faster. This results in “snappier” webpage loading.

## Attachments (0)
