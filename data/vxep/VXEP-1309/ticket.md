# VXEP-1309: SB40X VXE376 Xcomm SD Issue

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2025-06-14
- **Updated:** 2025-06-18
- **Resolved:** 2025-06-18
- **Reporter:** Cody Smisek
- **Assignee:** Cody Smisek
- **Creator:** Cody Smisek
- **Parent:** XKIT-752 Design SB40 Propulsion & Flight Controls (PFC)
- **Links:** Cannot finish until linked issue is finished. VXEP-1307 (SB40x - N376VX: Network Issue); relates to VXEP-1310 (VXE689 - Network Issues); blocks XKIT-4730 (SB40x - N376VX: Network Issue); is duplicated by XKIT-4741 (SB40x N376VX XCOMM SD Issue)
- **Vehicle Tail Number:** 376
- **Vehicle Configuration:** Havoc / SB40X / D750
- **Issue Status:** Canceled and move to https://jenaero.atlassian.net/browse/XKIT-4741
- **Incident Type:** Mission Failure/Abort
- **Severity:** 1 - Flight Critical

## Description

On 5/29/2025, VXE376 with 376 avionics was powered on after ~1-2mo of storage. Forward motor/esc audible sequence indicated PWM signal was not present and continued for 5-10mins with this indication until ceasing (with no changes in configuration by user).
After reviewing xcomm event log, data appeared to be corrupted. SD card was replaced from older style to updated industrial SD. 
After reforming the updated SD card. Numerous attempts to download the xcomm config (through AAR) were performed, but the config was never present. While attempting to troubleshoot, some webpage navigation was slow and/or pages intermittently blank. 
A soft reset was performed and ~1min later aircraft reset uncommanded. Due to this, avionics was swapped for alternate set and 376 avionics red tagged. 
The uncommanded reset was later explained to be a known issue (by SCO), where a reset occasionally is not acknowledged, so it automatically gets sent again some time later.

## Plan

Due to discovery on 695 avionics (VXEP-1307), this avionics should be inspected for any power issues, consistent with any findings from https://jenaero.atlassian.net/browse/XKIT-4730  investigation.

## Comments (0)

## Attachments (0)
