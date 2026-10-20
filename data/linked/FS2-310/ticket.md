# FS2-310: VXEP - SD Card file corruption (VXEP-236,237,414)

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-05-16
- **Updated:** 2025-04-18
- **Resolved:** 2025-04-18
- **Reporter:** David Grosher
- **Assignee:** Michael Berger
- **Creator:** David Grosher
- **Components:** Vehicle Incident Support 
- **Links:** relates to VXEP-236 (Systemic SD card Investigation VXE-522 XCOM board failures at LM Source inspection); relates to VXEP-237 (VXE-529 XCOM board failures at LM Source inspection); relates to VXEP-414 (VXE 468 crash after transition to forward flight); relates to FS2-2550 (SD Card CAs for 6.4 release); split to FS2-2824 (SD Card Improvements)
- **Job Number:** J100084 - VXE Incident Investigation
- **SQA Assignee:** Gabby Fajardo

## Description

Ongoing issue for SCO and Flight Test, description taken from NCR 653:
“With the latest batch of spare Center Wings, all 5 had SD card corruption after flight tests. When connecting to update firmware it was found that the config would fail, and it was realized that SD corruption was the cause. This has been an issue in the past, usually related to a poor quality SD or occasional faulty card. Reformat was able to fix all 5.”

## Comments (2)

### Greg Fryer, 2025-02-05

@Scott Whitney @Jason Scherer There’s a big outstanding list of tasks here, are they tied to resolving the SD Card issue, or are they tied to further improvements. I am trying to square that up with Dave’s comments that this is already wrapped up, so maybe it’s just reorganizing the tickets?

### Scott Whitney, 2025-02-05

@Greg Fryer  - This is an open investigation. The CAs that are going into 6.4 are part of https://jenaero.atlassian.net/browse/FS2-2550

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| NCR 653 - CW 474 SD Corruption.png | image | 17 | 2023-07-19 | listed only |
