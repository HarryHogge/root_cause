# GCSS-34: Implement user-focused messaging system between GCS and aircraft to indicate understood, causal behaviors

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Highest
- **Created:** 2023-07-14
- **Updated:** 2026-09-08
- **Resolved:** 2026-09-08
- **Reporter:** Craig Burton
- **Assignee:** Craig Burton
- **Creator:** Craig Burton
- **Links:** relates to GCS-843 (On launch abort, the reason for the abort is not provided to the user (in a pop up or report, or similar).); relates to GCS-841 (Implement user-focused messaging system between GCS and aircraft to indicate understood, causal behaviors); is blocked by FS2-1057 (Implement user-focused messaging system between GCS and aircraft to indicate understood, causal behaviors); relates to ENG-2998 (VXE 438 Launch Aborts, uncommanded motor spin after second abort, R Aft rotor broken likely from contact with the aircraft stand.)

## Description

For some expected aircraft behaviors (e.g. a launch abort due to degraded GPS positioning), there is no way for a customer to quickly understand the nature or root cause of the nominal behavior. This task will track enhancements to GCS and vehicle firmware to ensure that, for as many cases as practical, planned/expected causal vehicle behavior will be communicated simply and clearly to the user without the need for log file analysis or incident investigation.
Additionally, context would be valuable:
- Notify operator on no-launch due to GPS (no requirement to go look in the log, no vague “Sensor Fault: GPS” message)
- On launch abort due to GPS, show detected values or similar so that it is clear to the operator that GPS on the ground was fine, but airborne was below threshold. (e.g. jamming blocked by trees or terrain)

## Comments (2)

### Michael Berger, 2023-07-20

Waiting on support from Vehicle firmware. 
GCS can only display messages for data it gets from the vehicle.

### Christa Meck, 2026-09-08

No work done in over a year.  Canceling.

## Attachments (0)
