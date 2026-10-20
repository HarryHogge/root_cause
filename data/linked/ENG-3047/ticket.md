# ENG-3047: 530 Anomalies on Launch and In Flight

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-08-22
- **Updated:** 2026-06-16
- **Resolved:** 2026-06-16
- **Reporter:** Garret Moose
- **Assignee:** Pat Wells
- **Creator:** Garret Moose
- **Links:** relates to VXEP-555 (VXE 530 Anomalies on Launch and in flight)

## Description

Multiple anomalies were observed during the third and fourth flights of V530 during the Reiver Look 2 T&E in the UK.  On 22 August 2024:
- During V530 1st flight of the day, 4th flight of the T&E, during a mission sync, the sim took a LONG time, then the mission upload failed and timed out.  This happened a few times before the mission was successfully sync’d.  Mission was fairly large/long, but still took an unexpectedly long time (and multiple failures) to sync.  Comms indicator was green and comms (per the Silvus GUI) were excellent (SNR=34, Airtime <60%).
- On the 2nd flight of the day, the aircraft paused briefly (throttle reduced) before lifting out of the stand, then paused for ~5 seconds at 10 feet before continuing to climb.  See attached video with sound up to hear throttle pause in stand.
- During flight, radio Ethernet cable was moved from one Ethernet port to the other to eliminate multiple SA camera video feeds in the downlink.  Cable was reconnected within 2-3 seconds.  GCS software took 60+ seconds to reconnect to aircraft.  Comms (per Silvus GUI) were great.
- When RTB was commanded, GCS screen froze with hourglass for 90+ seconds.  When the sim (or whatever it was doing) finished, a window popped up for 1 or 2 seconds stating that the aircraft was executing the Lost Comms Mission.  when the window closed, the aircraft entered the active landing pattern with no user input.  Comms indicator remained green throughout and comms (per Silvus GUI) were great.
- During the landing pattern, it was observed that the aircraft position and telemetry on the GCS was 20-30 seconds behind the actual aircraft position.  This could have been an issue if the gap had been longer and the aircraft had landed before the operator was given the option to Enable User Landing Control.  See attached video of GCS showing aircraft on approach to landing while the aircraft was already on the ground.

AAR data has to go through formal MOD channels which will take a few days.
For consistency, the MOD plans to fly the same aircraft with the same GCS tomorrow.  Please advise Garret Moose asap if the recommendation is to NOT fly V530 until the fight data is reviewed.
garret.moose@lmco.com  661-264-7130

## Comments (9)

### Garret Moose, 2024-08-22

Item 1) 1st flight of the day, THIRD flight of the T&E.

### Pat Wells, 2024-08-22

@Garret Moose received and passed to engineering team.  Awaiting guidance

### Garret Moose, 2024-08-23

AAR attached.

### Pat Wells, 2024-11-18

@Garret Moose Would it be possible to get the previous AAR T95_V530_240822_133603_pack.zip. I’We don’t see any mission upload/download timeouts in the debug of the AAR currently attached (T95_V530_240822_151625_pack) to this ticket. However, we do see timeouts in the event log for the previous AAR, which should be for the same day according to the event log we do have.

### Garret Moose, 2024-11-18

Hi Pat,
I have requested that our UK office request all AAR from V530 from 22 August 2024 from the MOD.  I’m not sure how long it will take, but shouldn’t be a problem to get them.
Cheers,
Garret Moose
Stalker sUAS, Lead Instructor
Lockheed Martin Aeronautics Company
661-264-7130

### Pat Wells, 2024-12-03

@Garret Moose just checking in to see if there’s any movement on obtaining the AAR

### Pat Wells, 2024-12-10

Aircraft being returned to SLO for updates. 
Will evaluate upon return.

### Pat Wells, 2025-01-16

Aircraft in SLO being investigated.

### Christa Meck, 2026-06-16

Related incident closed.  Closing this as well.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| V530 Landing While On the Ground.MOV | video | 23094 | 2024-08-22 | listed only |
| V530 Pauses on Launch.mp4 | video | 10911 | 2024-08-22 | listed only |
| V530 RTB Commanded.MOV | video | 66276 | 2024-08-22 | listed only |
| T95_V530_240822_151625_pack.zip | archive | 1849 | 2024-08-23 | listed only |
