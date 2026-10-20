# FS2-4351: Investigation: v881 not passing OGCS Sensor calibrate page

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2026-03-05
- **Updated:** 2026-03-24
- **Resolved:** 2026-03-24
- **Reporter:** Scott Whitney
- **Assignee:** Brandon Slater
- **Creator:** Scott Whitney
- **Links:** relates to VXEP-1608 (VXE 881 CW not detected but able to access .10 page and GPS Satellites displayed in SUAV)
- **Sprint:** FS2 Sprint 37

## Description

Reported:
OGCS fails to allow user to continue even though all green checks on Calibrate sensor page
Tests:
- Recreate the failure
- Recreate the failure using Legacy GCS
- If Legacy ‘passes’ and OGCS fails than we need to document the difference in Calibration Sensor validation

## Comments (1)

### Brandon Slater, 2026-03-05

Issue resolved: bad dted format

## Attachments (0)
