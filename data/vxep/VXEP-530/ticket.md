# VXEP-530: VXE 490 GCS displaying erractic aircraft icon position data and not maintaining size of commanded loiter

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-08-09
- **Updated:** 2025-04-22
- **Resolved:** 2025-04-22
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** Edge_Asset
- **Links:** relates to VXEP-529 (VXE 674 Erractic landing behavior, not accepting operator commands)
- **Vehicle Tail Number:** 490
- **Corrective Action:** Upgrade to v6.4 and utilize mitigations for E140 ground loop.
- **Root Cause:** Magnetometer interference stemming from E140 Ground loop (most likely - not conclusive)
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Edge asset currently at Operation Northern Strike demo / exercise

Statement from operator:
: During this flight we saw another issue regarding the software aircraft icon displaying erroneous behavior that did not match the actual flight path of the aircraft. During this, the icon displayed the aircraft flying any where from a 90 degree to180 degree difference from the actual flight path. It was also not maintaining the accurate size of the commanded loiter. The aircraft yaw and SA camera confirmed the orientation of the vehicle were different than the displayed icon orientation.

E140 camera installed.
 AAR attached

## Comments (9)

### David Grosher, 2024-09-05

@Eric Brewer This looks like another Mag related issue with the E140 at Northern Strike. I thought we had looked at all the data but there are no comments on this ticket.

### Eric Brewer, 2024-09-05

@David Grosher confirmed looks like mag issue.  FW and VTOL heading disagree by ~100 degrees shortly after transition.  It looks better the rest of the flight so wondering what would have changed? Maybe the payload was stowed?

[embedded image-20240905-173137.png]

### David Grosher, 2024-09-05

@Pat Wells @Sam Miller Does the E140 have a log? It would be good to correlate these errors to a position or event.

### Pat Wells, 2024-09-05

@David Grosher Edited and added correct information. 

It does keep an error log if there are errors.
It has the ability to log telemetry, BUT the operator has to specifically turn that on.  It's not by default.

### Pat Wells, 2024-09-06

@David Grosher added E140 telemetry and AAR from today’s flight that you requested.

### Alexander Alan Arnold, 2025-01-10

@Pat Wells @David Grosher Is this linked to the ground loop issue we believe the octopus gimbals to have? If so, should this be closed since there is another investigation for that? We could move the data from this over to that investigation as well.

### David Grosher, 2025-01-10

@Alexander Alan Arnold Yes, we believe the ground loop is driving the majority of the E140 EMI noise. We should link the issues but not close them yet.

### Alexander Alan Arnold, 2025-04-15

@David Grosher Is there a path forward on this investigation?

### David Grosher, 2025-04-15

@Alexander Alan Arnold I think this investigation is complete. With v6.4 and mitigations in place to address the E140 ground loop this should no longer be an issue.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V490_240809_133628_pack.zip | archive | 2676 | 2024-08-09 | listed only |
| image-20240905-173137.png | image | 94 | 2024-09-05 | listed only |
| [9_6_2024 12_24_55 PM_telemetry_log.txt](attachments/23008_9_6_2024%2012_24_55%20PM_telemetry_log.txt.md) | text | 1858 | 2024-09-06 | converted |
| T95_V490_240906_125151_pack.zip | archive | 1898 | 2024-09-06 | listed only |
