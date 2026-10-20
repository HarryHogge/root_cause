# GCSS-465: Update GCS software to force delay time in between pressure and shield steps, or change order of steps.

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Duplicate
- **Priority:** Low
- **Created:** 2024-08-27
- **Updated:** 2025-09-23
- **Resolved:** 2025-09-23
- **Reporter:** Eric Brewer
- **Assignee:** Ted Trowbridge
- **Creator:** Eric Brewer
- **Parent:** FS2-2390 VXEP-292 Crash on take off
- **Links:** relates to VXEP-292 (VXE-477 Crash on take off )
- **Epic Link:** FS2-2390
- **Sprint:** FS2 Sprint 33, FS2 Sprint 32

## Description

Update GCS software to force delay time in between pressure and shield steps, or change the order of the steps.  The goal is to reduce/eliminate issues such as AV477 (see VXEP-292) which crashed after takeoff due to bad airspeed cal.

## Comments (5)

### Scott Whitney, 2025-02-02

Moving out of the 6.4 release. We will look at implementing in 6.6

### Michael Berger, 2025-02-03

@Eric Brewer 
The current order is:
gpsfix
calibrate (shield)
pitot (pressure)
download mission
fuelcellhybridbattery - (if fuelcell)
calibrate again (shield)

The second calibrate step is a long way away from the pitot step.
Download mission takes while.
What do you propose?

### Eric Brewer, 2025-02-03

@Michael Berger as we dug into the investigation on 477 more it appeared to be user error (they pushed during both shield steps it looks like, see slide 6 here).  

Our only remaining suspicion was that somehow the user would jump the gun on applying pressure after the first shield step, but we were never able to reproduce this issue in simulation testing (the second shield step resets the calibration).  With the above updated understandings in mind I think it may not be necessary to perform this task.
@David Grosher @Ted Trowbridge thoughts?

### Scott Whitney, 2025-09-23

Moving to GCS backlog

### Scott Whitney, 2025-09-23

This duplicated https://jenaero.atlassian.net/browse/GCSS-368

## Attachments (0)
