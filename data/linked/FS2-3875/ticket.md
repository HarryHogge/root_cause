# FS2-3875: B40 Investigations

- **Issue type:** Epic
- **Status:** In Process
- **Priority:** High
- **Created:** 2025-10-30
- **Updated:** 2026-04-14
- **Reporter:** Scott Whitney
- **Creator:** Scott Whitney
- **Fix versions:** BLK 35/40
- **Parent:** VXEP-1512 SB40 Software (Release 6.7.0)
- **Links:** relates to XKIT-5208 (2025-11-22 SB40 Flight Test Issues); relates to XKIT-5172 (B40 CAN Issues Investigation); relates to XKIT-5217 (Legacy GCS displays fixed wing power 1/10. Determine if fixed in OGCS); relates to XKIT-5215 (Instrument panel airspeed is delayed ~5+ seconds when performing pitot test during launch wizard); relates to XKIT-5127 (9/17 Wobble during descent after fixing gains); relates to XKIT-5302 (B40 Slow descent during VTOL landing); relates to VXEP-1692 (B40/30 XCOM WDT resets ); relates to XKIT-5414 (B40 914 apVlife (XCOM FW) spikes during 4P flight. ); relates to XKIT-5424 (B40 914 4/7 Unable to climb in fuel cell flight. Slow climb rate otherwise. ); relates to XKIT-5425 (B40 914 4/7 during VTOL landing, seemed like it overshot the LZ by a good 100ft+. Taxied back fine.); relates to XKIT-5423 (914 VTOL sounds abnormal. At least one motor appears saturated during takeoff); relates to FS2-4436 (Short term deferred tasks for B40 and UAP)

## Description

Working notes for Everett B40
B40 Data Review.pptx

Findings from bank angle: If we dash above 105fps, bank angle limit will become the limiter in the gcs minimum radius turn not the turn rate limit.

## Plan

Using priority to clearly mark intended MVP:
- High/Highest=MVP
- Medium=Nice to have for MVP

## Comments (5)

### Scott Whitney, 2025-11-06

2025-11-05 during Flight test the CAN dropped out and the FW motor stopped providing thrust.
Action items:

- Validate if the updated ESC firmware with the Hargrave fix resolves the CAN dropout and slew rate issue, including ground checks and performance tests.
- Confirm that the new production ESC firmware supports the current CAN protocol.
- Ensure the throttle reset function can reach 0 to allow ESC fault recovery, independent of firmware fix.
- Investigate if lift ESCs are susceptible to the same CAN dropout issue as the forward ESC.
- Address the root CAN dropout issue to prevent recurring ESC shutdowns.

### Scott Whitney, 2025-11-19

2025-11-03 
[embedded: image-20251120-041424.png]

### David Grosher, 2025-11-20

@Scott Whitney I reviewed the epic and added comments to the issues. I also prioritized them. High being things that would prevent release, Medium being things that we should be addressed hopefully before a release. Low being backlog items. Highest would block flight test.

### Scott Whitney, 2025-11-20

@David Grosher Thanks! I will make sure we start working them in that order

### David Grosher, 2026-04-08

@Scott Whitney Can we try to update the tickets in this epic so that we have a clear picture of the current status on Blk40?

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20251120-041424.png | image | 111 | 2025-11-19 | listed only |
