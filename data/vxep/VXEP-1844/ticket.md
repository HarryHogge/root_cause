# VXEP-1844: VXE-102 (HIL SIM) anomalies

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2026-04-16
- **Updated:** 2026-07-07
- **Resolved:** 2026-07-07
- **Reporter:** Jackson Riley Curvin
- **Assignee:** Scott Lovett
- **Creator:** Jackson Riley Curvin
- **Labels:** RCCA, Weekly-incident-tracker
- **Customer:** TIQUILA
- **Vehicle Tail Number:** VXE-102
- **Vehicle Configuration:** VXE-30 Main Battery
- **Problem Type:** Discovered Issue
- **Incident Type:** Squawk
- **Severity:** 4 - Annoyance
- **Components (EA Aircraft):** Software, GCS

## Description

- During flight #1 a route named Flight was created, uploaded, and flown. A second route named Test Route was then created and uploaded to the aircraft. The aircraft departed Flight, orbit 2 and proceeded to Test Route orbit 2. Then Flight was reuploaded to the aircraft. After that, the display indicated that the aircraft was flying Flight while it was actually flying Test Route that was shown as not uploaded. The OGCS displayed the same.


The dashed line indicates the aircraft thinks it’s flying racetrack 3 of the uploaded mission but it’s flying the other racetrack 3
[embedded 23e3ee71-f5e5-434c-9436-a077878115a7.png]
The line from the aircraft shows it as flying a racetrack that is not the uploaded racetrack

## Comments (1)

### Jackson Riley Curvin, 2026-07-07

Closing due to end of support of product

## Attachments (9)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 23e3ee71-f5e5-434c-9436-a077878115a7.png | image | 595 | 2026-04-16 | listed only |
| AAR_V102_20260413T173333Z.zip | archive | 19971 | 2026-04-16 | listed only |
| [Contingency A.json](attachments/53770_Contingency%20A.json.md) | text | 1 | 2026-04-16 | converted |
| [Contingency A_2.json](attachments/53772_Contingency%20A_2.json.md) | text | 2 | 2026-04-16 | converted |
| [Flight.json](attachments/53771_Flight.json.md) | text | 3 | 2026-04-16 | converted |
| [PersistedLandingPatterns.json](attachments/53774_PersistedLandingPatterns.json.md) | text | 3 | 2026-04-16 | converted |
| [Test Route.json](attachments/53775_Test%20Route.json.md) | text | 3 | 2026-04-16 | converted |
| archive_20260413_181117.zip | archive | 25088 | 2026-04-16 | listed only |
| archive_20260413_181202.zip | archive | 3945 | 2026-04-16 | listed only |
