# VXEP-45: 371 mis-configured (ready for flight then DTED loaded)

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2023-08-31
- **Updated:** 2025-06-09
- **Resolved:** 2025-06-09
- **Reporter:** Greg Fryer
- **Assignee:** Cameron Chapman
- **Creator:** Greg Fryer
- **Links:** relates to VA-445 (371 mis-configured -Record procedure used to land aircraft flying with wrong DTED. ); relates to VA-446 (371 mis-configured-Provide more details. Identify C/CAs.); is blocked by VA-439 (Record 371 YPG near miss incident, the procedure you used to fix it, and any recommended corrective actions to prevent it in the future? ); is blocked by GCSS-99 (Force Restart of GCS Following Load of DTED)
- **Customer:** LM_Palmdale
- **Vehicle Tail Number:** 371
- **Issue Status:** Done
- **Incident Type:** Near Miss
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Verbal report only, so far:
371 was supporting JHU VBN demo. DTED was loaded after launch prep completed. Aircraft launched. Resulted in inability to land normally (aircraft was 800' hire than it’s assessment, insufficient energy to VTOL land). 
New/unknown procedure executed to resolve, aircraft landed safely.

## Corrective Action

Immediate fix documented here:https://jenaero.atlassian.net/browse/VA-439 
Long term fix: https://jenaero.atlassian.net/browse/GCSS-99

## Root Cause

Problem description:
- Launch wizard (at least the pitot calibration) happened without DTED loaded (aircraft thinks it’s at 0ft MSL)
- At some point after calibration, DTED was loaded
- The aircraft flew ~1000 - 1500ft higher than it was supposed to because it didn’t have ground elevation reference during calibration, but after GCS got the DTED (elevation) data it commanded to climb to maintain the same altitude, but above the newly obtained elevation data
- A concern/assumption was made that during the landing aircraft could start the transition to VTOL at a very high altitude and run out of HLB power. And there wasn’t a known safe way to command aircraft to fly lower than the GCS elevation.

## Comments (0)

## Attachments (0)
