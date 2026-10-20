# VXEP-102: VXE-380 Launch abort

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-09-26
- **Updated:** 2026-03-02
- **Resolved:** 2023-10-06
- **Reporter:** Pat Wells
- **Assignee:** Greg Fryer
- **Creator:** Pat Wells
- **Labels:** FBI
- **Links:** relates to ENG-3071 (Aircraft 380 Launch Abort); is blocked by VA-609 (Review VXE-380 launch abort log, determine cause or if unknown); relates to FS2-754 (GNSS Multi-Constellation Support); relates to VXEP-1066 (VXE 448 Multiple Aborted takeoffs)
- **Customer:** FBI
- **Vehicle Tail Number:** 380
- **Problem Type:** Other (explain in description)
- **Plan:** Complete.
- **Root Cause:** Loss of GPS signal near transition altitude, system aborted launch per standard.
- **Incident Type:** Mission Failure/Abort
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

During FBI training the customer reported a launch abort.
Vehicle ascended to commanded launch altitude, then began to decend without any command from RPIC. RPIC then selected Abort Launch within the Override Launch Control menu, and had control of the aircraft during its remaining descent. RPIC nudged aircraft slightly left, before it landed safely. HLB landed with 57% battery life. Nominal winds, 73 degrees F, sunny, approx. 11:50 AM CST.
The HLB was swapped and the aircraft relaunched without issue.

AAR file attached

## Corrective Action

None required, notify customer on how to note this occurrence. Improvement already logged to better display reason for abort.

## Issue Status

File stored (please ignore attachments):
VXE-380 launch abort log, determine cause or if unknown

## Comments (2)

### Greg Fryer, 2023-09-28

@Pat Wells Formal short report to come from Jason, but this is a normal abort due to GPS loss prior to transition. Likely jamming or interference - similar to prior events on other aircraft, GPS signal is fine on ground but lost at altitude.

### Jason Scherer, 2023-09-29

@Pat Wells @Greg Fryer Report attached
[embedded file]

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V380_230921_115114_pack.zip | archive | 1650 | 2023-09-26 | listed only |
| [Vehicle Investigation Report VXEP-102 (a4ac957a-11e6-4f51-8ce6-645612679be6).pptx](attachments/16814_Vehicle%20Investigation%20Report%20VXEP-102%20(a4ac957a-11e6-4f51-8ce6-645612679be6).pptx.md) | pptx | 4145 | 2023-09-29 | converted |
