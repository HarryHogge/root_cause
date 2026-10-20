# FS2-4282: NCR: No GPS Lock, No Sats

- **Issue type:** Story
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2026-02-12
- **Updated:** 2026-02-26
- **Resolved:** 2026-02-26
- **Reporter:** Scott Whitney
- **Assignee:** Brandon Slater
- **Creator:** Scott Whitney
- **Links:** relates to VXEP-1608 (VXE 881 CW not detected but able to access .10 page and GPS Satellites displayed in SUAV)
- **Sprint:** FS2 Sprint 37

## Description

v881 No GPS Lock, No Sats

## Comments (5)

### Scott Whitney, 2026-02-12

@Brandon Slater  @Logan Wright  - could either of you take a look at this NCR and support Carson in SCO.

### Brandon Slater, 2026-02-12

@Scott Whitney  I’ll head over to SCO

### Brandon Slater, 2026-02-12

data on hardened laptop need encrypted drive to pull it

### Brandon Slater, 2026-02-12

Steps so far:
- Confirmed correct firmware & configs for 6.6.1 BLK35X were on aircraft
- Checked GPS on VTOL webpage, No Sats shown only C/No value
- checked GPS on GCS, No Sats shown only C/No value
- Repushed firmware for 6.6.1
- Same results as above
- Checked GPS data from Putty and Novatel Application Suite, saw GPS data so data is getting to OEM7700

### Brandon Slater, 2026-02-13

Reviewed data from AAR, some GPS data seen on fixed wing ap and no GPS data seen on vtol, likely CAN due to fixed wing ap data is off serial while vtol ap data is off CAN for GPS

## Attachments (0)
