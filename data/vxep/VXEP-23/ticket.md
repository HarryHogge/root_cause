# VXEP-23: TPTR-101 Battery Charging Failure with 12V DC

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2023-08-23
- **Updated:** 2025-08-05
- **Resolved:** 2025-08-05
- **Reporter:** Allen Gardner
- **Assignee:** Cameron Chapman
- **Creator:** Allen Gardner
- **Links:** relates to VA-398 (TPTR-101 Battery Charging Failure with 12V DC-Identify C/CA); relates to VA-935 (TPTR-101 Battery Charging Failure with 12V DC - Investigate, Report, and Close)
- **Customer:** TIQUILA
- **Corrective Action:** Use an inverter from the FSK kits with the power supply to reach 12V.
- **Issue Status:** - Demonstrated 12V to GCS inverter to power supply  to charge both battery types.
- **Root Cause:** Manufacturer “Lowest input Voltage” is set to 12.6V and therefore the power supply cannot go lower.
- **Incident Type:** Mission Failure/Abort
- **Severity:** 3 - Degraded Performance - With Workaround
- **Impacted Core Subsystems:** Aircraft

## Description

During TO1 STALKER FAT, a test was conducted to charge the main and hybrid lift batteries with 12V DC power supplies. The test failed due to to the following error observed on the battery chargers:  "input voltage lower than 12.6V"

SRD-186
Requirement Text: Any batteries within the [System] shall be able to be charged by 
MoP: 12/24/110/240 volts supply e.g., DC or AC from a vehicle battery, generator or mains power supply. 
Remarks/Supporting Information: This requirement does not apply if no batteries are used within the [System].  
To be able to take advantage of as wide a range of power sources as possible. 
Acceptance Criteria
Demonstrate for the system that the system batteries can be charged from 12/24/110/240 volts supply e.g. DC or AC from a vehicle battery, generator or mains power supply.

## Plan

- @Former user what is the closure process? Should we collect that information in a report? Do you recommend a template?
- The setup demonstrated does meet the requirement, but would be rather frustrating in the field. The better fix would be to lower the charger minimum voltage. Do we want to spend time and money doing that? (pay ISDT to update the firmware).

## Comments (4)

### Allen Gardner, 2023-08-24

@Cameron Chapman Please add a task to VA for someone to  determine the root cause of this problem.

### Cameron Chapman, 2023-09-12

- Demonstrated 12V to GCS inverter to power supply to HLB charger. Need to repeat for main battery and determine reporting requirements.

### Christa Meck, 2025-04-17

Removed parent to prep for Incident hierarchy change.  Parent is linked as Linked issue.

### Christa Meck, 2025-08-05

Closing this incident as it’s from August 2023 and any investigation is likely done at this point.

## Attachments (0)
