# XKIT-5523: OGCS Allows Landing transitions of 0ft

- **Issue type:** Improvement
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2026-06-22
- **Updated:** 2026-10-05
- **Resolved:** 2026-10-05
- **Reporter:** Cody Smisek
- **Assignee:** Cody Smisek
- **Creator:** Cody Smisek
- **Labels:** NoCUI
- **Parent:** XKIT-5113 B40 Non Flight-blocker flight test issue collector/Squawk List
- **Links:** is fixed by OGCS-605 (No Landing Transition Altitude Limits); relates to VXEP-1928 (VXE 1006 would not maintain altitude during descent in landing pattern leading to mishap)
- **Epic Link:** XKIT-5113
- **Issue Status:** In progress, will be in 1.4.3 release (July). See linked issues.

## Description

It appears OGCS allows setting landing transitions as low a 0ft. 
If this is confirmed, recommend either not permitting an automatic PLZ to be this low, add some limit or at minimum a pop up that asks users to confirm they wanted something set below ~100ft (continue to allow U-drive to Land Immediately at any altitude).

## Plan

See status and linked investigation here [VXEP-1928] VXE 1006 would not maintain altitude during descent in landing pattern leading to mishap - Jira

## Comments (2)

### Cody Smisek, 2026-06-22

@Scott Whitney @Anthony Hansen

### Ted Trowbridge, 2026-06-22

Linked https://jenaero.atlassian.net/browse/OGCS-605

## Attachments (0)
