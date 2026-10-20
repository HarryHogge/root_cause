# VXEP-1446: VXE-519 Power Fluctuations

- **Issue type:** Incident (8D)
- **Status:** D6 - Implementing Corrective Actions
- **Priority:** Low
- **Created:** 2025-07-23
- **Updated:** 2026-10-15
- **Reporter:** Jackson Riley Curvin
- **Assignee:** Samuel Lopez
- **Creator:** Jackson Riley Curvin
- **Labels:** GS_Closed, Hardware, TIQUILA, Weekly-incident-tracker
- **Links:** relates to RMA-722 (VXE-519 RMA 250701-1)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** VXE-519
- **Vehicle Configuration:** VXE-30 Battery Configuration
- **Issue Status:** Report reviewed with team and sending to customer
- **Root Cause:** FWAP Failure.  Unable to diagnose what caused FWAP failure due to losing evidence.
- **Incident Type:** Mission Failure/Abort
- **Severity:** 3 - Degraded Performance - With Workaround
- **Components (EA Aircraft):** Aircraft, full assembly
- **Executive Summary:** Updates requested on CA tasks. Probable cause Hardware.

## Description

•VXE-519 exhibited fluctuations in reported power, voltage, endurance, and altitude while on the ground.
•Initial customer troubleshooting did not resolve the issue, and the aircraft was returned for further investigation.

## Corrective Action

https://jenaero.atlassian.net/browse/VXEP-1658 
- Update aircraft intake procedures to maintain accurate records of replaced parts and establish clear criteria requiring approval for when part replacement is allowed and appropriate.
- Implement a standardized post-failure checklist to ensure complete data collection after any aircraft issue, enabling thorough analysis and root cause identification.

https://jenaero.atlassian.net/browse/VXEP-1659 
- Generate a glossary of terms for the GCS log like the VTOL and XCOMM ones shown below. These should be added to SharePoint here: VXE Documentation 
- VTOL Log Glossary: VXE-FCD-VTOL Log Glossary.docx
- XCOMM Log Glossary: VXE-FCD-XCOMM Log Glossary.docx

## Plan

See below links for full details
Presentation Report: VXE-519 Investigation Report - Power Fluctuations.pptx
SharePoint: VXEP-1446 VXE-519 Power Fluctuations

## Comments (20)

### Rodney Linch, 2025-07-23

@Jackson Riley Curvin – AAR zip file attached.

### Drew Hildreth, 2025-08-12

@David Grosher has this moved at all? Should we move to Cameron since it seems to be something electrical?

### David Grosher, 2025-08-12

@Drew Hildreth This should be an electrical air systems issue. Assign it to Greg and he can disposition it, Cameron has taken a new position in SEIT and is no longer responsible for this, although he has been backfilling the work.  @Greg Fryer FYI.

### Drew Hildreth, 2025-08-12

@David Grosher Thanks Dave. @Greg Fryer when you a couple seconds can you push this to somebody for a review?

### Cameron Chapman, 2025-08-12

Assigned to Steve

### Drew Hildreth, 2025-09-30

@Steve Gonzales Can you provide an update on this one? Have you had a chance to look at it at all? It came in for power fluctuations and then an AP was changed. I am trying to wrap my head around it all.

### Steve Gonzales, 2025-09-30

@Drew Hildreth Hi, I should be able to look at this towards the end of the week and provide an update then.

### Drew Hildreth, 2025-09-30

@Steve Gonzales Cool thanks.

### Drew Hildreth, 2025-10-14

@Steve Gonzales could we have an update on this one this afternoon during the incident meeting?

### Steve Gonzales, 2025-10-14

@Drew Hildreth I have had a lot of feedback on my other reports/investigations.  I have been working on those items first.  This is next on the list.

### Cameron Chapman, 2025-11-11

@Samuel Lopez can you please work this when available?

### Samuel Lopez, 2025-12-09

Issue regarding Power Fluctuations.

- As of 11/15, the aircraft no longer shows power fluctuations when tested either on iron bird bench, or with MB/HLB.

- Almost certainly, the issue was fixed when the green AP was replaced.
- No travelers exist regarding this fix.  However, it’s unlikely that replacing the XCOMM SD card addressed the power fluctuations.

### Jacob Troyer, 2025-12-11

Adding videos showing power fluctuations and mismatch between measured battery voltage and reported battery voltage in “stalker-519-gcs-fluctuations.zip”

### Cameron Chapman, 2025-12-30

@Jacob Troyer  @Samuel Lopez please update status, C/CA fields. CA should be linked Jira tasks.

### Jacob Troyer, 2025-12-30

@Cameron Chapman added as child work items and included in corrective action field.

### Cameron Chapman, 2025-12-31

@Jacob Troyer Updated cause field “FWAP Failure.  Unable to diagnose what caused FWAP failure due to losing evidence.”

### Pat Wells, 2026-08-11

Updates requested on CA tasks 8/11/2026

### Alexander Alan Arnold, 2026-10-13

@Samuel Lopez @Jacob Troyer Is this ticket able to be closed or do we need to keep it in D6?

### Samuel Lopez, 2026-10-13

@Alexander Alan Arnold Let me check with Drew.  If he gives the sign off, we can close.

### Drew Hildreth, 2026-10-15

@Samuel Lopez We can’t close until there is a Disposition provided about. I think the CA is good but the Dispo has to be filled out before this can be closed.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V519_250714_084622_pack.zip | archive | 716 | 2025-07-23 | listed only |
| [VXE519_maintenance.txt](attachments/30897_VXE519_maintenance.txt.md) | text | 27 | 2025-07-23 | converted |
| stalker-519-gcs-fluctuations.zip | archive | 66986 | 2025-12-11 | listed only |
