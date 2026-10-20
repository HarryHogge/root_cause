# VXEP-1289: VXE 528 Not accepting 400 ft ALT command

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-05-16
- **Updated:** 2026-03-02
- **Resolved:** 2025-05-19
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** USASOC, Weekly-incident-tracker
- **Customer:** USASOC
- **Vehicle Tail Number:** VXE 528
- **Vehicle Configuration:** VXE 30 standard, battery, no payload
- **Issue Status:** General location per providing training .vmis file. https://maps.app.goo.gl/18qXDJVcSBch9p59A
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

During flight the Operator commanded a 400 ft AGL loiter and the commanded altitude carrot on the GCS Aircraft status panel would not move off of 600 ft AGL Operator commanded Orbit 2 and altitude would not drop below 600 ft AGL. Aircraft also drifted off of the commanded orbit point significantly prior to commanding RTB. During Recovery the aircraft entered IP4 at roughly 400 ft AGL and descended during the downwind leg. Once past IP5 the aircraft assumingly hit a thermal and was at roughly 500 ft AGL when it transitioned to VTOL.

## Comments (4)

### Cody Smisek, 2025-05-19

Looks like a case of glider doing glider things. Throttle zero, and still climbing. 
[embedded: image-20250519-165805.png]

### Cody Smisek, 2025-05-19

Local AWOS reporting wind shift w/ gusts of 18kt 1hr prior to launch. Suggesting winds extremely variable in the area. 
[embedded: image-20250519-171424.png]
Colorado springs (10nm away) reporting peak winds of 37kt in same time period
[embedded: image-20250519-171930.png]

### David Grosher, 2025-05-19

Closing per environmental conditions at time of incident.

### David Grosher, 2025-05-19

Environmental conditions resulted in incident.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V528_250516_134121_pack.zip | archive | 2520 | 2025-05-16 | listed only |
| Training flight.vmis | other | 4 | 2025-05-16 | listed only |
| image-20250519-165805.png | image | 125 | 2025-05-19 | listed only |
| image-20250519-171424.png | image | 20 | 2025-05-19 | listed only |
| image-20250519-171930.png | image | 16 | 2025-05-19 | listed only |
