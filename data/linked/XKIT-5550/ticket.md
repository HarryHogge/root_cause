# XKIT-5550: SLO EE Troubleshooting Plan

- **Issue type:** Sub-task
- **Status:** New
- **Priority:** Low
- **Created:** 2026-07-10
- **Updated:** 2026-07-27
- **Reporter:** Jeremy Kostel
- **Assignee:** Jeremy Kostel
- **Creator:** Jeremy Kostel
- **Parent:** XKIT-5529 V1038 Troubleshooting Steps
- **Links:** relates to XKIT-5529 (V1038 Troubleshooting Steps); relates to VXEP-1933 (VXE 1038 VTOL motors failed to shut off after transition to fixed wing flight)

## Description

V1038 experienced a near-incident during FLOPs training in which the VTOL motors remained active during fixed-wing flight. Refer to the parent ticket for additional event details.
Post-flight analysis of CAN health messages indicates an unhealthy CAN bus was present during the event. Logs also suggest the autopilot handoff message between the VTOL autopilot and FWAP was lost, resulting in both autopilots simultaneously maintaining control authority ("both had a hand on the wheel").
An attempt was made to isolate and reproduce the issue through the test activities documented in the associated HSV test-plan ticket; however, the behavior could not be replicated during ground testing. The inability to reproduce the issue on the ground may indicate that the failure condition requires a loaded system state (e.g., spinning motors and/or higher bus utilization during flight) to manifest.

## Plan

@Alexander Alan Arnold  to coordinate returning to SLO for troubleshooting. Please add tracking info when availalble.   Tracking addded UPS 1ZK6A5960302058407

Because the issue could not be replicated during HSV ground testing, I do not recommend repeating the same test plan documented in the associated HSV ticket. Instead, testing should progress directly to higher-load operating conditions that more closely match the environment present during the original event.
- Tie-down Testing
- Secure the aircraft and use RC control to command significant throttle on the VTOL motors.
- Monitor CAN bus health and record any bus errors, unhealthy bus indications, or autopilot handoff anomalies.
- Repeat the test with significant throttle applied to the forward motor while continuing to monitor CAN health and messaging.
- Hover Testing
- If tie-down testing does not reproduce the issue, proceed to a controlled hover test.
- Monitor CAN bus health, autopilot handoff messaging, and overall system behavior throughout the test.
- FLOPs Test Flight
- If the issue remains unreproducible during hover testing, conduct a FLOPs test flight representative of the conditions present during the original event.
- Continue monitoring for CAN errors, unhealthy bus conditions, and loss of autopilot handoff messages.
- Battery Quarantine
- If the issue cannot be reproduced after the above testing, quarantine the flight batteries used during the original event to eliminate battery-related effects as a contributing factor.
- Failure Isolation
- If the issue is successfully reproduced at any point during the above testing, stop progression testing and execute the HSV test plan documented in the associated ticket to systematically isolate the root cause.

## Issue Status

Open – Awaiting aircraft availability. Ground-based HSV testing has been completed and did not reproduce the issue. The next phase of investigation requires access to the aircraft to perform tie-down, hover, and potentially FLOPs testing under higher-load operating conditions. No further troubleshooting is planned until the aircraft is available for testing.

## Comments (6)

### Matt Philley, 2026-07-15

@Greg Fryer @Nigel Goodison @William Dresser do we have anyone who could answer HSV questions about this while Jeremy is out? 
Support is being requested by @Alexander Alan Arnold

### William Dresser, 2026-07-15

@Matt Philley Please copy/include me and I will help as much as I am able.

### Matt Philley, 2026-07-15

@Alexander Alan Arnold please connect with @William Dresser for support while Jeremy is out. He will support where possible or help direct traffic where he is able.

### Alexander Alan Arnold, 2026-07-21

Tracking added UPS 1ZK6A5960302058407

### Alexander Alan Arnold, 2026-07-27

@Jeremy Kostel This aircraft should be delivered today in SLO. When you're ready to test ping @Lauren Velasquez since it will be in the RMA area.

### Lauren Velasquez, 2026-07-27

@Alexander Alan Arnold@Jeremy Kostel  INTAKE UNDERWAY IN RMA

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T135_V1038_260720_092201_pack.zip | archive | 9760 | 2026-07-20 | listed only |
| VTOL_VXE1038.zip | archive | 58610 | 2026-07-20 | listed only |
| XCOMM_VXE1038.zip | archive | 20973 | 2026-07-20 | listed only |
