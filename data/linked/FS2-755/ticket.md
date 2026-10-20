# FS2-755: ESC Check prior to VTOL transition

- **Issue type:** Epic
- **Status:** To Do
- **Priority:** Low
- **Created:** 2023-08-22
- **Updated:** 2025-05-06
- **Reporter:** David Grosher
- **Creator:** David Grosher
- **Links:** relates to VXEP-51 (Internal - Aircraft 450 VTOL Landing Crash - ESC soft start); relates to ENG-3034 (Aircraft 450 VTOL Landing Crash-ESC Damage); relates to ENG-3052 (CLONE - Aircraft 450 VTOL Landing Crash); is duplicated by FS2-573 (Perform Pre-VTOL transition check on VTOL lift system)

## Description

NOTE: Started and put on hold. This needs to be designed out and reviewed, there is good chance it could cause RACE conditions and instabilities during flight.

## Comments (2)

### Scott Whitney, 2024-02-21

Merging https://jenaero.atlassian.net/browse/FS2-573 and https://jenaero.atlassian.net/browse/FS2-755 into 755

### Scott Whitney, 2024-02-21

Description from 573:
See incident: https://jenaero.atlassian.net/browse/VIT2-272 
Implement a current check on the lift motors individually (or possibly two at a time, with opposite motors) prior to transitioning to VTOL mode to determine that the lift system is OK. If the system is NOK then perform a glide landing.

## Attachments (0)
