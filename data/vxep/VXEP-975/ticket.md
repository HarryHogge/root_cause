# VXEP-975: VXE 500 reports wrong temperature in flight

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2025-02-05
- **Updated:** 2025-04-15
- **Resolved:** 2025-04-15
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Ben Triplett
- **Creator:** Alexander Alan Arnold
- **Labels:** Edge_Asset, Weekly-incident-tracker
- **Vehicle Tail Number:** VXE 500
- **Vehicle Configuration:** Fuel cell config, heated pitot protoype
- **Corrective Action:** Revise design to ensure the temperature measurement is thermally isolated from heater.
- **Issue Status:** Investigation Complete
- **Root Cause:** Defective design of the unreleased heated Pitot.
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

EDGE ASSET
-Ruysser: The aircraft reports a temperature of 45 Deg F plus in flight. This temperature is very likely incorrect due to the ground temp being 22-25 deg F. Based on standard laps rate the temp should drop 3.5 F for every thousand ft AGL. Even if there was a temp inversion the temperature would likely not climb 20+ degrees in 2500 ft. I am not 100% sure that the temp sensor is in the ADP but if it is, the heated pitot prototype is likely the cause of this issue but should be considered when operating with a heated pitot prototype and when designing the new version.

## Comments (3)

### Greg Fryer, 2025-02-05

@Eric Brewer Just realized these are both tickets for 500, not sure if it’s the same flights. I could see an interaction of temperature mis read and the altitude calc? I will stop pretending to do your job now.

### Cameron Chapman, 2025-02-05

Added to ADP requirements. 2024 ADP Requirements.xlsx
| Ensure HP does not interfere with ADB measurements, especially OAT |

### David Grosher, 2025-02-14

@Pat Wells I propose we close this issue. It is regarding an unreleased heated Pitot design that is being tracked independently by the Engineering team 
@Greg Fryer FYSA

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Mishap Reporting AV Temp.docx](attachments/25973_Mishap%20Reporting%20AV%20Temp.docx.md) | docx | 53 | 2025-02-05 | converted |
| T95_V500_250202_121303_pack.zip | archive | 6457 | 2025-02-05 | listed only |
| T95_V500_250203_111706_pack.zip | archive | 7508 | 2025-02-05 | listed only |
| T95_V500_250204_111241_pack.zip | archive | 4195 | 2025-02-05 | listed only |
