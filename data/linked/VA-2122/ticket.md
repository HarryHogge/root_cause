# VA-2122: Red AP replaced SD card and unable to access files after format

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-10-29
- **Updated:** 2025-08-05
- **Resolved:** 2025-08-05
- **Reporter:** Cameron Chapman
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-236 (Systemic SD card Investigation VXE-522 XCOM board failures at LM Source inspection); Linked issue cannot finish until this issue finishes. VA-2123 (VXE-592 Purple SD corruption observed)

## Description

NCR: Red AP replaced SD card and unable to access files after format
This AP came from inventory for an SD card swap. After replacing the SD card we verified that we could access the webpage and that it was showing accessing files off the SD card. However, when attempting to access the files in Drive status all memory options return a blank page. Further, the dates of the files in the log files show 1/1/2028 but the RTC and the date codes in the logs themselves show 1/1/1900. After reboot I can see that during the boot process the AP attempts to access the SD card files and is unable, and rebuilds them from flash. It is doing this each time the AP reboots. Battery measures 2.3 volts on the bench and was going up while connected to power.

## Plan

@Dave Grosher⁠ @Abel Markow⁠ @Kurt Burian⁠ @Connor Peebles⁠ should we preserve this SD card for investigation, or are we ok to attempt reformatting? How does this plan sound. 1. Replace SD card with another and attempt to process normally. Report results. 2. Place this SD card in another AP, see if it can be reprocessed normally?

## Comments (1)

### Christa Meck, 2025-08-05

Canceling as SD card issue ended up being A Big Deal (tm) and was handled in a separate incident.

## Attachments (0)
