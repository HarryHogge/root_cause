# VXEP-161: (VTOL AP WD)VXE-499 uncommanded lift system shutdown during landing SCO flight

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-10-31
- **Updated:** 2026-01-15
- **Resolved:** 2023-11-08
- **Reporter:** Pat Wells
- **Assignee:** Greg Fryer
- **Creator:** Pat Wells
- **Labels:** Edge_Asset, VTOL-AP-WD, Weekly-incident-tracker
- **Links:** duplicates VXEP-41 (TPTR-74 VXE 510: (VTOL AP WD) Consolidated Watch Dog tracking)
- **Severity:** 1 - Flight Critical

## Description

During landing, after otherwise normal flight, vehicle was commanded to pause at approximately 10 - 15 feet high. The lift system subsequently shut down and the vehicle fell to the ground and disarmed. Shortly after, uncommanded, the vehicle rearmed and took off sideways, folded the wingtip, and drifted approximately 100 feet before crashing down.
Note: Prior to SCO flight the XCOM board was identified as faulty and replaced. 
Obvious Damage:
Right & Left Wing Tip
Fuse - Mount holes for Avi Box
Fuse - FCR Battery Mount (Check)
FDR was acquired and data shows a possible LRF failure which may have caused early shut down of lift system. Impact of the drop seemed to reset the VT AP, which may have contributed to the re-arm and loss of control.

## Comments (3)

### Pat Wells, 2023-11-01

@Sean Odell  FYSA

### Greg Fryer, 2023-11-07

@John Clark reports that this is indeed a Watch Dog event, essentially the worst case. So will tie it to that and close off, need to determine vehicle-specific corrective actions (if any).

### Greg Fryer, 2023-11-08

The FS team has proven from the log that this is a WD event. Closing as a duplicate, and linking to consolidated WD incident.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Landing Power_Motors.png | image | 233 | 2023-10-31 | listed only |
| Landing Rate Of Climb.png | image | 150 | 2023-10-31 | listed only |
| Landing Vibe Roll Pitch Yaw.png | image | 129 | 2023-10-31 | listed only |
| T95_V499_231031_094142_01_pack.zip | archive | 2502 | 2023-10-31 | listed only |
