# VXEP-1503: VVE-538/VXE-553 Sim limitations

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-09-08
- **Updated:** 2026-03-02
- **Resolved:** 2026-01-23
- **Reporter:** Jackson Riley Curvin
- **Assignee:** Jackson Riley Curvin
- **Creator:** Jackson Riley Curvin
- **Labels:** TIQUILA, Weekly-incident-tracker
- **Customer:** TIQUILA
- **Plan:** Known issues with current sim. Customer is notified of known issues. CA to replace with new sim.
- **Incident Type:** Squawk
- **Severity:** 4 - Annoyance
- **Components (EA Aircraft):** Aircraft, full assembly

## Description

The detachment deployed on the 05 SEP 25 to soak and collect anything of interest. During the flight, the detachment witnessed numerous abnormalities on the system which lead to swapping the current aircraft and GCS to a new one of each and conducted a second flight at the same location. Whilst conducting the second flight, the same issues occurred which led to recovering the aircraft and end flying activity for the day. The decision was made to conduct an additional flight on the 06 SEP 25 at a different location to see if the same issues would occur with a different aircraft being operated
 
The faults we experienced are as follows:
 
The Eagle system simulator exhibited significant limitations. It was unable to replicate the full mission profile instead only simulating mission elements directly ahead in the aircraft’s current flight path. This constraint reduced the effectiveness of mission rehearsal as it prevented comprehensive testing of the entire mission sequence. Furthermore, the simulator failed to simulate the Emergency Landing Zone (ELZ) and lost communications orbit functions when selected during setup creating a critical gap in training and pre-mission validation. The system would only simulate the full mission including ELZ and lost comms orbits while the aircraft was on the ground. This restriction prevented in-flight verification of essential mission elements. When simulation was applied during flight the system incorrectly reported insufficient endurance to complete the mission despite adequate battery power being available. This discrepancy raised concerns about the accuracy of the system’s endurance calculations.
 
Analysis revealed that as the aircraft was flown for longer durations and at greater distances the number of system faults increased. Simulation functions became less dependable the further the aircraft was from the Ground Control Station. This pattern suggested potential issues with data processing endurance calculations or bandwidth limitations over extended ranges.

## Comments (2)

### Jackson Riley Curvin, 2025-09-08

Waiting on AARs

### Michael Mohr, 2025-09-15

New AARs uploaded

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V538_250905_030032_pack.zip | archive | 995 | 2025-09-09 | listed only |
| T95_V538_250905_152716_pack.zip | archive | 248 | 2025-09-09 | listed only |
| T95_V553_250906_023736_pack.zip | archive | 856 | 2025-09-09 | listed only |
| FDL.zip | archive | 15 | 2025-09-10 | listed only |
| FDR.zip | archive | 13056 | 2025-09-10 | listed only |
| XCOMM_VXE553.zip | archive | 4304 | 2025-09-10 | listed only |
