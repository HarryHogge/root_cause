# VXEP-1465: VXE 827 LRR Asset LRF and GPS error on VTOL launch

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-08-11
- **Updated:** 2025-08-11
- **Resolved:** 2025-08-11
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Corrective Action:** None, system operating as expected.
- **Plan:** Complete
- **Issue Status:** Closed
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

During our first launch with aircraft 827, the vehicle aborted due to an emergency panel warning stating " Sensor: laser range finder fault". Once the aircraft was paused on the GCS, another alert message popped up stating a GPS error, "GPS fault: Prepare to manual nudge".
After this alert, the aircraft went into manual nudge and started drifting. The PIC (instructor) grabbed the joystick and attempted pause/nudge commands. These commands were not taken by the aircraft because the joystick was unplugged. 
The aircraft continued to drift and descend and safely landed on its own. There was no damage to the aircraft.  
Other:
During the preflight of this aircraft, there was a failed calibration. After this failed calibration, the aircraft was power cycled.

## Root Cause

System operating as expected. Uncertainty in GPS resulted in abort of the launch (this is normal). Due to the altitude at which the abort occurred, the LRF return was unstable which resulted in the additional error message.

## Comments (2)

### Greg Fryer, 2025-08-11

@Eric Brewer @David Grosher log is attached to the ticket.

### David Grosher, 2025-08-11

[embedded image-20250811-191136.png]
@Greg Fryer FYI

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V827_20250811T152025Z.zip | archive | 11449 | 2025-08-11 | listed only |
| IMG_2500.jpeg | image | 2693 | 2025-08-11 | listed only |
| IMG_8072.jpeg | image | 1586 | 2025-08-11 | listed only |
| Screenshot 2025-08-11 111818.png | image | 101 | 2025-08-11 | listed only |
| Screenshot 2025-08-11 112321.png | image | 41 | 2025-08-11 | listed only |
| image-20250811-191136.png | image | 60 | 2025-08-11 | listed only |
