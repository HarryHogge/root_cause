# FS2-2335: VXEP-555 Anomalies on Launch and in flight

- **Issue type:** Epic
- **Status:** Canceled
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2024-09-30
- **Updated:** 2025-09-24
- **Resolved:** 2025-09-24
- **Reporter:** Scott Whitney
- **Creator:** Scott Whitney
- **Components:** Vehicle Incident Support 

## Description

Received from LM:
Multiple anomalies were observed during the third and fourth flights of V530 during the Reiver Look 2 T&E in the UK. On 22 August 2024:
- During V530 1st flight of the day, 4th flight of the T&E, during a mission sync, the sim took a LONG time, then the mission upload failed and timed out. This happened a few times before the mission was successfully sync’d. Mission was fairly large/long, but still took an unexpectedly long time (and multiple failures) to sync. Comms indicator was green and comms (per the Silvus GUI) were excellent (SNR=34, Airtime <60%).
- On the 2nd flight of the day, the aircraft paused briefly (throttle reduced) before lifting out of the stand, then paused for ~5 seconds at 10 feet before continuing to climb. See attached video with sound up to hear throttle pause in stand.
- During flight, radio Ethernet cable was moved from one Ethernet port to the other to eliminate multiple SA camera video feeds in the downlink. Cable was reconnected within 2-3 seconds. GCS software took 60+ seconds to reconnect to aircraft. Comms (per Silvus GUI) were great.
- When RTB was commanded, GCS screen froze with hourglass for 90+ seconds. When the sim (or whatever it was doing) finished, a window popped up for 1 or 2 seconds stating that the aircraft was executing the Lost Comms Mission. when the window closed, the aircraft entered the active landing pattern with no user input. Comms indicator remained green throughout and comms (per Silvus GUI) were great.
- During the landing pattern, it was observed that the aircraft position and telemetry on the GCS was 20-30 seconds behind the actual aircraft position. This could have been an issue if the gap had been longer and the aircraft had landed before the operator was given the option to Enable User Landing Control. See attached video of GCS showing aircraft on approach to landing while the aircraft was already on the ground.

AAR data has to go through formal MOD channels which will take a few days.
For consistency, the MOD plans to fly the same aircraft with the same GCS tomorrow. Please advise Garret Moose asap if the recommendation is to NOT fly V530 until the fight data is reviewed.

## Comments (1)

### Scott Whitney, 2025-09-24

Closing this epic. The original investigation has been closed and moved to cannot be reproduced

## Attachments (0)
