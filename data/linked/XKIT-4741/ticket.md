# XKIT-4741: SB40x N376VX XCOMM SD Issue

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2025-06-18
- **Updated:** 2025-09-01
- **Resolved:** 2025-09-01
- **Reporter:** Carl Graf
- **Assignee:** Cody Smisek
- **Creator:** Carl Graf
- **Parent:** XKIT-4517 Test & Down-Select New Motors for SB35/40
- **Links:** is blocked by XKIT-4730 (SB40x - N376VX: Network Issue); duplicates VXEP-1309 (SB40X VXE376 Xcomm SD Issue)
- **Epic Link:** XKIT-4517
- **Plan:** Pending 4730 findings to complete the plan above.

## Description

On 5/29/2025, VXE376 with 376 avionics was powered on after ~1-2mo of storage. Forward motor/esc audible sequence indicated PWM signal was not present and continued for 5-10mins with this indication until ceasing (with no changes in configuration by user).
After reviewing xcomm event log, data appeared to be corrupted. SD card was replaced from older style to updated industrial SD. 
After reforming the updated SD card. Numerous attempts to download the xcomm config (through AAR) were performed, but the config was never present. While attempting to troubleshoot, some webpage navigation was slow and/or pages intermittently blank. 
A soft reset was performed and ~1min later aircraft reset uncommanded. Due to this, avionics was swapped for alternate set and 376 avionics red tagged. 
The uncommanded reset was later explained to be a known issue (by SCO), where a reset occasionally is not acknowledged, so it automatically gets sent again some time later.

## Comments (0)

## Attachments (0)
