# VXEP-1622: PMA263 Master Systemic HLB Cell Failure

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** Highest
- **Created:** 2025-12-05
- **Updated:** 2026-08-13
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Stephen Peters
- **Creator:** Alexander Alan Arnold
- **Labels:** GS_Closed, HLB_bad_cell, RCCA, Weekly-incident-tracker, battery
- **Links:** Cannot finish until linked issue is finished. VXEP-1449 (Systemic Hybrid lift battery unexplained cell failures in flight); relates to VXEP-1974 (VXE 895 uncontrolled decent); relates to VXEP-1976 (VXE 617 HLB cell failure on landing)
- **Customer:** Air_PMO
- **Severity:** 1 - Flight Critical
- **Components (EA Aircraft):** Battery, HLB
- **Executive Summary:** Systemic issue tracked in HLB master. Master still investigating root cause.

## Description

We have reviewed the data from four incidents and determined all aircraft suffered from the HLB Cell dropout. 
The brief written statements from the Operators align with the symptoms of an HLB drop out.
This will be used as a master tracker for ALL PMA263 related battery issues and will be linked to the MASTER HLB problem ticket
VXE 865 HLB SB 2-3264
VXE 852 HLB SN 2-3264
(20OCT) VXE 639 HLB SN 2-2455
(22OCT) VXE 639 HLB SN 2-2443
These four flight/aircraft are all we have data for currently. There are additional flights and batteries we will enquire about based on comments we found in the GCS Logs. 

We will update with screenshots/information as we gather it.

## Comments (2)

### Alexander Alan Arnold, 2025-12-08

Added HLB Cell reading screenshots from Grafana.

### Eric Brewer, 2025-12-10

@Alexander Alan Arnold GPS fault was due to velocity uncertainty - I haven’t seen that much with ublox.  Have there been other gps-related aborts?

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V639_251020_212534_pack.zip | archive | 1221 | 2025-12-05 | listed only |
| T95_V639_251022_131449_pack.zip | archive | 3301 | 2025-12-05 | listed only |
| T95_V852_251119_080856_pack.zip | archive | 1809 | 2025-12-05 | listed only |
| T95_V865_251114_060527_pack.zip | archive | 1304 | 2025-12-05 | listed only |
| (20OCT)_VXE_639_HLB_SN_2-2455.png | image | 27 | 2025-12-08 | listed only |
| (22OCT)_VXE_639_HLB_SN_2-2443.png | image | 19 | 2025-12-08 | listed only |
| VXE_852_HLB_SN_2-3264.png | image | 29 | 2025-12-08 | listed only |
| VXE_865_HLB_SB_2_3264.png | image | 30 | 2025-12-08 | listed only |
