# VXEP-1292: VXE 376 Xcomm Issues

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-06-02
- **Updated:** 2025-06-16
- **Resolved:** 2025-06-16
- **Reporter:** Cody Smisek
- **Assignee:** Cody Smisek
- **Creator:** Cody Smisek
- **Issue Status:** duplicated VXEP-1309

## Description

When attempting to access 376 for the first time since its previous flight (~2months between), aircraft exhibited symptoms of xcomm resets during power up. This was noted by PWM motor tone sequence when power was applied. 
After ~10-15mins of the PWM tone, the issue seemingly cleared and subsequently access to xcomm page was available. Checking xcomm event log led to discovery of what appeared to be corrupted data within the log. 
xcomm had older style SD card, so the SD card was removed and replaced with the latest version of the industrial SD card. Instructions within 965-1-01-4008 were followed for replacement. 
[embedded: image-20250603-154610.png]
After replacement, it was discovered that the xcomm event log and xcomm config was no longer being included as part of the FDR/AAR. Additional attempts of reformatting and various other troubleshooting was performed, but problem continued. 
Avionics was removed and red tagged for further investigation. Unknown cause at this time.

## Comments (0)

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20250603-154610.png | image | 3767 | 2025-06-03 | listed only |
