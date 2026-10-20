# GCSS-333: Land Immediately during VTOL landing - block command?

- **Issue type:** Bug
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2024-07-24
- **Updated:** 2026-09-23
- **Resolved:** 2026-09-23
- **Reporter:** Artis Bertulis
- **Assignee:** Michael Berger
- **Creator:** Artis Bertulis
- **Sprint:** GCSS Sprint 30, GCSS Sprint 25

## Description

If commanding “Land Immediately” during a VTOL landing, the vehicle (while still descending with VTOL motors on) drifts away into the wind direction with no user override options to nudge it back.
Problem description:
- Sent to IP1
- Aircraft tracked partial IP2 orbit and went to IP4
- IP5 and transitioned normally
- Let aircraft navigate to its decent point
- Active user control appeared (abort landing greyed out)
- Commanded LI and selected okay for land as quick as possible
- Aircraft continued decent seeming to be slower than normal and Activate user landing control greyed out
- Selected LI and okay again, as a user may if they were trying to land ASAP
- Activate user landing control still greyed out and aircraft was noticed to be drifting in a SE direction (not entirely with the wind of 5mh from the W)
- atempted to click Activate user control while still greyed out, still nothing
- Aircraft continued to descend slowly and drift SE
- At about 15-20ft AGL activate user landing control became clickable and was promptly selected to immediately nudge left to avoid crashing into a fence
- Landed after crossing the fence 5ish fe
et above and user cut and safe.
- Aircraft ended up 270m away to the SE

[embedded: Image (13).jpg]

## Comments (2)

### Michael Berger, 2024-08-26

Propose block of Land Immediately command if already in VTOL descent.

### Christa Meck, 2026-09-23

No work done in over a year.  Canceling.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Image (13).jpg | image | 317 | 2024-07-24 | listed only |
