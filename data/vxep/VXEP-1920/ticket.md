# VXEP-1920: VXE 940 has an internal clock mismatch and auto pilot will not connect to the VSM

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Known Error
- **Priority:** High
- **Created:** 2026-06-19
- **Updated:** 2026-07-07
- **Resolved:** 2026-07-07
- **Reporter:** Stephan Johnson
- **Assignee:** Stephan Johnson
- **Creator:** Stephan Johnson
- **Labels:** GS_Closed, RCCA, Redwire
- **Customer:** Sweden
- **Vehicle Tail Number:** VXE 940
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

VXE 940 has a date and time mismatch between the aircraft and the GCS where the aircraft is ~9 months behind the current date and time. When the aircraft is reset manually, the date and time do not keep when power is cycled on the aircraft. Once power is cycled on the aircrafts, the date and time revert to ~9 months behind.
On both aircraft the VSM will not connect to the autopilot. It’s suspected that the date and time mismatch between the aircraft and the GCS has something to do with the VSM’s inability to connect with the autopilot.
Users are using OGCS v1.3.3 and Block 30 Adv Nav aircraft.

## Comments (1)

### Stephan Johnson, 2026-07-07

OGCS issues with workaround.

## Attachments (0)
