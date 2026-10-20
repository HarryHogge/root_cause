# VXEP-1997: Remove calibration value from VTOL Checksum?

- **Issue type:** Epic
- **Status:** New
- **Priority:** Low
- **Created:** 2026-09-11
- **Updated:** 2026-09-11
- **Reporter:** Jeremy Kostel
- **Assignee:** Scott Whitney
- **Creator:** Jeremy Kostel
- **Parent:** VXEP-1785 B30 Multiple HLB Voltage Measurements Outside of Voltage Limits. Suspect VTOL AP or voltage sense circuit (harness, ground iso, etc)
- **Epic Status:** To Do
- **Epic Color:** ghx-label-3
- **Issue color:** yellow

## Description

Carson B mentioned we calibrate the voltage reading for the FWAP and this is ok to do since those calibration values arent factored into the checksum (FWAP gains)
We could change the SW to not factor in VTOL voltage cal values into VTOL checksums so this calibration could be done in SCO

## Comments (0)

## Attachments (0)
