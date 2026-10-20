# VXEP-403: Firmware update through webpages is currently nonfunctional

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2024-05-01
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Ryan Ferguson
- **Assignee:** David Grosher
- **Creator:** Ryan Ferguson
- **Links:** relates to FS2-1808 (Production software cannot flash from webpage)
- **Issue color:** purple
- **Part Number(s):** 1409P01D
- **Production Stakeholder:** Ryan Ferguson
- **Impacted Disciplines:** Software

## Description

Programming VTOL autopilots through the webpage seems to be broken in the newest VTOL firmware release.  This is a major impact to production as many processes require the ability to program a VTOL autopilot without the GCS as that would require a full vehicle worth of electronics.  In the field, if a customer has an issue programming through the GCS, they will no longer be able to push a firmware update through the webpages and will need to ship back to SLO to be updated.

This issue has been recreated in two separate vehicles.  One was produced less than a month ago and the other is asset 491 which has an autopilot that is at least 6 months old.  Effectivity appears to be the whole fleet operating on firmware 1.54.  Testing has not been performed to determine if the X-comm is affected too.

Steps to recreate:
Navigate to the program page of the VTOL autopilot.  Upload the current released firmware (1.54) and attempt to update.

Result:
The VTEV log will throw an error for the hex file, saying “Bad hex file address range”
[embedded image-20240501-222254.png]
Navigating to the index page after this error will also show the autopilot has dismounted the SD card and is now in ROM mode.
[embedded image-20240501-222341.png]
The error can also be recreated by navigating to Utilities and clicking the Program from vtol.hex button.  This is supposed to reinstall the firmware from the hex file on the SD card but will also throw a corrupt pop-up message and dismount the SD card, kicking it back to ROM mode.
[embedded image-20240501-222458.png]

## Comments (0)

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240501-222254.png | image | 24 | 2024-05-01 | listed only |
| image-20240501-222341.png | image | 85 | 2024-05-01 | listed only |
| image-20240501-222458.png | image | 103 | 2024-05-01 | listed only |
