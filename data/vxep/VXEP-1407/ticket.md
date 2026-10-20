# VXEP-1407: VXE 801 Hard landings after Aborts

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-07-15
- **Updated:** 2026-08-14
- **Resolved:** 2026-08-07
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Stephen Peters
- **Creator:** Alexander Alan Arnold
- **Labels:** HLB_bad_cell, PMA263, Weekly-incident-tracker, battery
- **Links:** relates to VXEP-1418 (674 Hard Landing); relates to VXEP-1398 (VXE-808 Aborted launch cell balance ); relates to VXEP-1435 (VXE-674 Second Hard Landing); relates to VXEP-1485 (VXE-499 Hard Landing/ HLB Cell Drop Out)
- **Customer:** PMA263
- **Vehicle Tail Number:** VXE 801
- **Vehicle Configuration:** Assumed battery, MOD A kit(with Bkit) and HD40
- **Root Cause:** HLB Cell failure
- **Severity:** 1 - Flight Critical
- **Executive Summary:** HLB Cell failure, told customer to qaurantine battery

## Description

Operator Statement
I am at a MC training event and we have had two hard landings now on the same aircraft. One landing broke an antenna array mount and the other chipped a vtol prop that we have swapped out. The aircraft goes up 50-100 feet, aborts, and then comes down pretty fast. I was wondering if you could take a look at the logs for any smoking gun.
The weight of the system is probably 49lbs so a little on the heavy side. The winds arnt too bad: ~ 5mph gusting 10mph.

## Comments (8)

### Alexander Alan Arnold, 2025-07-15

[embedded: image-20250715-140459.png]

This is from the flight on the 14th. There is a massive drop in cell 5 of the HLB, if I am reading this correctly

### Alexander Alan Arnold, 2025-07-15

[embedded: image-20250715-140642.png]
The flight on the 9th displays the low climb rate message

### Greg Fryer, 2025-07-15

@David Grosher @Scott Whitney See incident.
@Alexander Alan Arnold Unless you can tell immediately it’s a hardware issue, likely fastest to contact Dave G. (and Scott W as backup) directly.

### David Grosher, 2025-07-15

@Alexander Alan Arnold Quarantine that battery. This is almost certainly the cause of the issue. I’m going to kick this over to AnnArbor. @Tom Westrich @Stephen Peters , see the battery balance plot below.  @Greg Fryer @Scott Whitney FYSA

### Alexander Alan Arnold, 2025-07-15

Will do. 

Please let me know what you find on the other incident, I'm not sure if it was same battery different day, but I know they were at 49 lbs, but the DA reading in grafana from the aircraft looked like they were within lims.

### Jackson Riley Curvin, 2025-07-15

flight from july 9th 
[embedded: image-20250715-181153.png]

### Scott Lovett, 2026-02-02

Tied this to overall HLB investigations

### Alexander Alan Arnold, 2026-08-07

tracked by HLB investigation

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V801_250709_163631_pack.changetozip.zip | archive | 1078 | 2025-07-15 | listed only |
| T95_V801_250714_152209_pack.changetozip.zip | archive | 1155 | 2025-07-15 | listed only |
| image-20250715-140459.png | image | 36 | 2025-07-15 | listed only |
| image-20250715-140642.png | image | 57 | 2025-07-15 | listed only |
| image-20250715-181153.png | image | 36 | 2025-07-15 | listed only |
