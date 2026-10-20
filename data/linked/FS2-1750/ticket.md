# FS2-1750: VXEP-363 Investigation (Landing Abort Issue)

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-04-17
- **Updated:** 2025-03-04
- **Resolved:** 2025-02-26
- **Reporter:** David Grosher
- **Assignee:** Jason Scherer
- **Creator:** David Grosher
- **Parent:** FS2-752 Vehicle Incident Investigation Support
- **Links:** relates to VXEP-363 (VXE 546 Loss of aircraft on landing)
- **Epic Link:** FS2-752
- **Sprint:** FS2 Sprint 18, FS2 Sprint 20, FS2 Sprint 27, FS2 Sprint 30, FS2 Sprint 22, FS2 Sprint 28, FS2 Sprint 17, FS2 Sprint 29

## Description

VTOL logs have been requested, but are not currently available for this investigation. 
Summary So Far: Although a VTOL land abort was logged and initiated due to an attitude fault, the abort was most likely not the cause of the crash. While log message timestamps are not precise due to internal system latency, the abort likely occurred after, or during, the impact. 
Review of the XComm logs indicates the vehicle consumed normal lift current with non-typical sustained throttle. VTOL GPS reported 32 satellites. Battery voltages remained above limits and the hybrid lift battery had a reported 60% State of Charge (SoC) at the conclusion of the landing. The forward motor also maintained high throttle longer than typical during transition to VTOL for landing. 
At the end of the XCOM data log the vehicle was in the state of waiting for proximity to the LZ. Neither the fixed wing autopilot nor the VTOL autopilot had advanced to the descension state. This means the vehicle should not have started descending.
**VTOL Land Abort**

[embedded: image-20240418-210420.png]
There is a VTOL land abort message in the XComm log, however, the abort was not the cause of the crash. This particular land abort code execution path has been shown to be successful in HIL testing on this firmware. This land abort was issued due to bad attitude data (likely a result of the already unstable aircraft). XComm data logs indicate the land abort occurred after the impact. This is backed up by FDR data that does not show a change of state from VTOL landing to VTOL land abort which would be evident in an active land abort.
VTOL Status 2376: The VTOL status value of 2376 indicates the VTOL autopilot is offline which matches XComm data indicating a power outage on the 12V bus which  powers the VTOL ap. During the impact the 12V bus current drops from ~0.4 Amps to 0.01 Amps at the same time the Ethernet connection between the XComm and VTOL AP processors drops. The AP IMU data in the XComm log shows the impact just before the 12V bus drops current and the Ethernet link drops out.
VTOL Landing Behavior: 
Below shows lift current and throttles during the landing. Along with the data from this incident is a comparison of data from a flight captured during SCO flights. This provides a comparison to a known good landing. Per Hayden, 160A, versus ~200A, is more typical for landing, so this current chart is not alarming.
[embedded: image-20240418-211334.png]
Low Lift Power: Comparing data from an NCR flight indicates that during this landing the lift system consumed ~20% less current during landing than some SCO flight data. The current level is also sustained as is the sustained high throttle value. 
Sustained High Lift Throttle: A typical VXE landing has a throttle pattern that goes up briefly at the start of transition then drops down for a very brief period before jumping back up to ~80%-90% throttle. 
VTOL Faults: The XComm data shows two short violations of the low power limit (<500W) at the start of the transition from fixed wing to VTOL flight. 
[embedded: image-20240418-211801.png]
VTOL State: The VTOL processor was in state 2 according to the XComm data. This state monitors battery charge state and GPS health while waiting for proximity to the 2D land position at altitude before descending. If the battery state of charge is low, the GPS drops out, or after reaching a timeout of 30 seconds, the VTOL AP proceeds to state 3 which stars the descent. Without VTOL logs/data it’s hard to determine for sure, but based on XComm log data the VTOL AP was not trying yet attempting to descend.
Rapid Altitude Loss: Vehicle 546 dropped ~350' in altitude over approximately 30 seconds before impacting with the ground. Comparing a typical VXE landing to this landing shows that the rapid altitude loss experienced by vehicle 546 is not typical in the first 30 seconds of a VTOL landing. 
[embedded: image-20240418-174537 (60924534-1b57-40d2-93b6-cae988ceba2e).png]
VTOL Offline: It is believed that the VTOL processor lost power on impact. The XComm data log shows the Ethernet link going down at the same time as a reduction in  current values on the 12V bus which power the VTOL processor. Additionally, the land abort status, in the XComm message log, indicates the VTOL is offline, and is the trigger for the land abort.
[embedded: image-20240417-190337.png]

## Comments (19)

### David Grosher, 2024-04-17

[11:17:19.447 9409.447] ap dbg: vt lnd abort, health fail during taxi to lz
[embedded: image-20240417-145155.png]

### David Grosher, 2024-04-17

The relevant datalog appears to be XCL00134.csv

### Jason Scherer, 2024-04-17

@David Grosher @Scott Whitney This type of land abort was successful in HIL testing on this release (Test Case: LA-02-010-01: LAND_WAITLZ (APM_ATT)). During HIL testing, after triggering an attitude fault and getting this message, the vehicle executes a glide landing. Because of previous successful testing (in the HIL) I believe the land abort was merely a symptom of a bigger problem. The vtstatus value of 2376, displayed during the land abort, indicates the VTOL was offline, and the IMU data was bad compared to the AP. I’m just getting into this investigation. I’ll share more when I have more to share. Getting VTOL logs in this case will be really helpful.

### Jason Scherer, 2024-04-17

It is weird though that it doesn’t look like the vehicle is trying to fly to the ELZ.

### David Grosher, 2024-04-17

@Jason Scherer Is there wind? Look for deltas in IAS and ground speed. That could result in course deviations.

### Jason Scherer, 2024-04-17

VTOL status during landing abort indicates VTOL processor offline. XComm datalog confirms the Ethernet link between XComm and VTOL AP drop at the same time as we see a 12V current drop from ~.4A to .01A

[embedded: image-20240417-190337.png]

### Jason Scherer, 2024-04-17

XComm log data during landing 
[embedded: image-20240417-205418.png]

### Jason Scherer, 2024-04-17

FWAP FDR Data during landing
[embedded: image-20240417-232829.png]

### Jason Scherer, 2024-04-18

Lift current during landing with comparison to similar timeframe during an NCR landing. V546 consumed ~20% less power during transition than typical VXE.
[embedded: image-20240418-173744.png]

### Jason Scherer, 2024-04-18

Altitude descent during landing with comparison to similar timeframe during an NCR landing. V546 dropped ~420' in the first 30 seconds of landing versus typical VXE drop of ~79' in the same amount of time.
[embedded: image-20240418-174537.png]

### Jason Scherer, 2024-04-18

Forward Motor & Lift Motors throttle during landing.
[embedded: image-20240418-180710.png]

### Jason Scherer, 2024-04-18

Comparison of Forward and Lift throttles during initial landing with NCR data for reference.
[embedded: image-20240418-181718.png]

### Jason Scherer, 2024-04-18

VTOL AP was in land state 2.
[embedded: image-20240418-182632.png]

Unlikely that VTOL started descent due to not advancing passed land state 2.
VTOL will start descent if:
- Low Energy.
- Unlikely: Battery State of Charge was 60%
- Bad GPS.
- Unlikely: VTOL has 32 sats during landing
- 2D position reached.
- Hard to tell based on available data (missing VTOL).
- Timeout of 30 seconds.
- Crash occurred ~30 seconds into landing.

### Jason Scherer, 2024-04-18

VTOL Faults during landing as recorded by XComm.
[embedded: image-20240418-193817.png]

### Jason Scherer, 2024-04-18

Fixed Wing Wind data during landing as reported by XComm.

[embedded: image-20240418-194643.png]

### Scott Whitney, 2024-04-19

blocked - waiting on vtol log

### Cameron Chapman, 2024-04-23

@Jason Scherer can you please use one of the standard investigation templates as you work on investigations and save files to a shared location? https://jenaero.atlassian.net/wiki/spaces/EF/pages/23363854/Incident+Troubleshooting+and+Resolution+Tracking.

### Scott Whitney, 2024-05-29

https://jenaero.atlassian.net/browse/VXEP-363?focusedCommentId=35741

### Jason Scherer, 2025-02-26

Closing this ticket as the investigation has been closed.

## Attachments (16)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240417-145155.png | image | 83 | 2024-04-17 | listed only |
| image-20240417-190337.png | image | 40 | 2024-04-17 | listed only |
| image-20240417-205418.png | image | 264 | 2024-04-17 | listed only |
| image-20240417-232829.png | image | 141 | 2024-04-17 | listed only |
| image-20240417-190337 (0755223b-b83c-47bb-95b7-2563d39f370d).png | image | 40 | 2024-04-18 | listed only |
| image-20240418-173744.png | image | 56 | 2024-04-18 | listed only |
| image-20240418-174537 (60924534-1b57-40d2-93b6-cae988ceba2e).png | image | 90 | 2024-04-18 | listed only |
| image-20240418-174537.png | image | 90 | 2024-04-18 | listed only |
| image-20240418-180710.png | image | 106 | 2024-04-18 | listed only |
| image-20240418-181718.png | image | 180 | 2024-04-18 | listed only |
| image-20240418-182632.png | image | 105 | 2024-04-18 | listed only |
| image-20240418-193817.png | image | 208 | 2024-04-18 | listed only |
| image-20240418-194643.png | image | 8 | 2024-04-18 | listed only |
| image-20240418-210420.png | image | 23 | 2024-04-18 | listed only |
| image-20240418-211334.png | image | 180 | 2024-04-18 | listed only |
| image-20240418-211801.png | image | 208 | 2024-04-18 | listed only |
