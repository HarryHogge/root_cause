# VXEP-320: VXE-522 / VXE-529 Corrective Action: Add code to automatically timeout upon SD Card read and automatically reformat SD Card

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

To have this error fix itself, low level driver would need a rewrite to timeout and upper layer code would need to be modified to trigger a reformat
- a significant amount of SW work.

Note* This ticket can act as an evaluation of the possibility of adding this feature*

## Comments (4)

### David Grosher, 2024-04-05

@Connor Peebles Were you able to reformat the SD card via APBL?

### Connor Peebles, 2024-04-05

@David Grosher on 529 XCOMM, we pulled the SD Card out which allowed it to boot, re-installed the SD Card while powered, and went to the XCOMM webpage and re-formatted the SD Card.
On 522 XCOMM, Kurt was not able to reformat the SD Card at all, neither through the webpage or through standard WindowsPC reformatting of the SD Card

### David Grosher, 2024-04-05

@Kurt Burian Is the bootloader trying to boot from the SDcard and then booting from the flash when it is removed? I’m thinking this code feature would be a change to the bootloader.

### Matt Philley, 2024-12-10

@Scott Whitney @Jason Scherer this is a lingering action tied up to SD Card stuff. Can you check and see if there is a duplicate in the Flight Science project and if we can close this one? 
https://jenaero.atlassian.net/browse/FS2-310

## Attachments (0)
