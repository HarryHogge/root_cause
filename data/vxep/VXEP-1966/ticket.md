# VXEP-1966: VXE 742 multiple launch aborts

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** Highest
- **Created:** 2026-07-21
- **Updated:** 2026-09-09
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Eric Brewer
- **Creator:** Alexander Alan Arnold
- **Labels:** Hardware, Investigating, No_crash, RCCA, Weekly-incident-tracker
- **Customer:** Air_PMO
- **Vehicle Tail Number:** VXE 742
- **Vehicle Configuration:** Standard VXE
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

VXE 742 experiencing multiple launch aborts

## Executive Summary

Have customer try with another battery, awaiting operator statement. recomend RMA for further testing. Probable cause; Battery Failure

## Comments (5)

### Alexander Alan Arnold, 2026-07-21

@David Grosher I believe this aircraft is at Lejune where alot of the AIR PMO issues are happening, this one seemed to have two aborts during launch. I was wondering if you would be able to find anyhting usefule in here. @Eric Brewer this one may be easier to use based on our teams converation earlier

### David Grosher, 2026-07-29

@Eric Brewer Can you look into this?

### Eric Brewer, 2026-07-29

@Alexander Alan Arnold it’s reporting a bus fault and the reported voltage is quite low.  Have they attempted a launch with a different battery?



[embedded image-20260729-175331.png]
[embedded image-20260729-175258.png]

### Alexander Alan Arnold, 2026-08-10

@Eric Brewer Was this for all flights or just one?

### Eric Brewer, 2026-08-10

@Alexander Alan Arnold I see the RF motor pegged in this log T95_V742_260709_125115_pack_unzipped\T95_VT742_260709_125115_vtl00652.csv
[embedded image-20260810-184621.png]
While this log shows the low voltage (T95_V742_260709_081426_pack_unzipped\T95_VT742_260709_081426_vtl00645.csv) and different motors pegged throughout:

[embedded image-20260810-184843.png]

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| DOD SAFE-Euwn1DU77r8Rwc9d.zip | archive | 5203 | 2026-07-21 | listed only |
| T95_V742_260709_125115_pack.zip | archive | 1993 | 2026-07-29 | listed only |
| image-20260729-175258.png | image | 35 | 2026-07-29 | listed only |
| image-20260729-175331.png | image | 76 | 2026-07-29 | listed only |
| image-20260810-184621.png | image | 176 | 2026-08-10 | listed only |
| image-20260810-184843.png | image | 162 | 2026-08-10 | listed only |
