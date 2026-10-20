# VXEP-1628: 757 RC Pitch Trim Crash

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-12-08
- **Updated:** 2025-12-11
- **Resolved:** 2025-12-11
- **Reporter:** Cody Smisek
- **Assignee:** Scott Whitney
- **Creator:** Cody Smisek
- **Vehicle Tail Number:** 757
- **Vehicle Configuration:** Advanced Nav
- **Plan:** @Scott Whitney to fill in root cause (multiple controllers causing RC wind pitch trim issue) and then close ticket.
- **Severity:** 1 - Flight Critical

## Description

During 6.6 SW testing, 757 crashed after VTOL to fixed wing transition. Aircraft pitched down abruptly following VTOL to fixed wing transition.

## Corrective Action

- Added RC test points to safety of flight tests.
- Fixed the trim handling in the joystick management code.

## Issue Status

Fixed wing avionics, VTOL avionics and fuselage avionics harness removed and placed on rack in SWQA area. Not for flight, can be used for ground test hardware. 
Vertical stab composite okay. removed and placed under stairwell SWQA area. 
All other components disposed of. 

Data / photos located below. 
VXEP-1628 VXE 757 RC Pitch Trim Crash

## Root Cause

New Joystick handling code set trim value to zero even though no trim was present on the Joystick. The trim value was saved into the ini file and loaded for the following flights. This issue was present only in RC mode operations.

## Comments (5)

### Cody Smisek, 2025-12-08

@Artis Bertulis can you link or add video & AAR to this ticket?

### Cody Smisek, 2025-12-08

@Scott Whitney not sure if there was another ticket floating around for this, if so just link and close this one. Feel free to close this one if corrective action is already in place. Just wanted to create to document location of hardware and reason hardware was removed for future reference.

### Artis Bertulis, 2025-12-09

@Cody Smisek Misshap report, videos, pictures, “.ini” file and AAR is in this link 757 Crash

### Cody Smisek, 2025-12-09

@Artis Bertulis thanks

### David Grosher, 2025-12-11

Note: This issue is not related to released code and will be closed. It has also been resolved for the v6.6 release.

## Attachments (0)
