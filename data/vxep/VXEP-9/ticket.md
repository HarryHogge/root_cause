# VXEP-9: (Duplicate) TPTR-74 VXE 510 Watchdog Software Fault

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2023-08-23
- **Updated:** 2023-09-13
- **Resolved:** 2023-08-30
- **Reporter:** Allen Gardner
- **Assignee:** David Grosher
- **Creator:** Allen Gardner
- **Links:** is blocked by FS2-603 (Trace support); is blocked by FS2-751 (Speedgoat Test Capability Development); is blocked by FS2-749 (Embedded SW Robustness Initiative); is blocked by FS2-806 (Embedded SW Evaluation of VTOL AP); duplicates VXEP-41 (TPTR-74 VXE 510: (VTOL AP WD) Consolidated Watch Dog tracking)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** VXE 510
- **Incident Type:** Mission Failure/Abort
- **Severity:** 1 - Flight Critical
- **Impacted Disciplines:** Software
- **Impacted Core Subsystems:** Flight Systems

## Description

See linked issue for content, this was logged as a duplicate.
During TO1 STALKER FAT, an aborted launch was caused by a software watchdog creating a failure in the autopilot. This occurred whilst the aircraft was launching off the stand, and was approximately 6inches of the ground. The aircraft fell back onto the ground and sustained minor cosmetic damage   [THIS IS WHAT THE CUSTOMER REPORTED BUT IS NOT TRUE, THE ABOVE INCIDENT WAS THE RESULT OF A BAD HLB]
During TO1 STALKER FAT, VXE 510 was performing a launch wizard lift rotor check.  When checking the rear left rotor, it initially began to spin but stopped and system automatically disarmed. After subsequent checks, the lift motor functioned normally. Preliminary analysis showed that a watchdog reset occurred.
Desired Behavior: Software Watchdog triggers are identified through root cause analysis and do not cause critical failures

## Corrective Action

Related to PTR-5. 
LMUK: Correct problem description
Engineering: 
- Hardware inspection revealed conformal coat quality issue, but initial assessments indicate that it is not related  to the watchdog timer event.
- Watchdog timer investigation underway.  Initial investigation suggests that
- Additional diagnostic, fixing crash dump for in-flight detection
- Additional logging of task usage
- Improving embedded software robustness

## Comments (0)

## Attachments (0)
