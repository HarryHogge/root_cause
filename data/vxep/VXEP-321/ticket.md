# VXEP-321: VXE-522 / VXE-529 Corrective Action: Add power down recognition, refrain from writing or reading to SD Card during power down

- **Issue type:** Sub-task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2024-04-04
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Connor Peebles
- **Assignee:** David Grosher
- **Creator:** Connor Peebles
- **Parent:** VXEP-236 Systemic SD card Investigation VXE-522 XCOM board failures at LM Source inspection
- **Links:** relates to RMA-230 (VXE 508 240325-2)
- **Job Number:** J100084 - VXE Incident Investigation

## Description

To attempt to prevent SD Card corruption: add a super-cap to power the XCOMM while the last write operations are completed after power has been disconnected
- XCOMM will need to understand that it has lost main power and is booting down
- During this, tell PIC32 to not read or write from SD Card

## Comments (1)

### Matt Philley, 2024-12-10

@Scott Whitney @Jason Scherer 
more lingering SD card stuff for SW. Can yall take a look and see if we can close this one if its already being tracked with 6.4 or otherwise?

## Attachments (0)
