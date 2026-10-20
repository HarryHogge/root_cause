# GCSS-359: Launch allowed after deleting W1 during Launch Wizard

- **Issue type:** Bug
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2024-09-17
- **Updated:** 2026-09-23
- **Resolved:** 2026-09-23
- **Reporter:** Ted Trowbridge
- **Creator:** Ted Trowbridge
- **Components:** GCS Application
- **Links:** causes VXEP-556 (VXE 600 W1 disappeared after passing Mission Check in Launch Wizard)

## Description

If the operator deletes W1 after completing the mission checkout page (intentionally or not) the launch wizard will still allow launching the vehicle.  If the vehicle is launched it appears to select an unpredictable departure heading as there is no W1 available to calculate a departure angle.
The mission simulation does not flag an error for only having 1 waypoint in the launch route, only the launch wizard mission checkout has that logic.
Ideally the launch wizard would catch this during mission simulation and prevent downloading it to the vehicle, or prevent launch (or both).

## Comments (1)

### Christa Meck, 2026-09-23

No work done in over a year.  Canceling.

## Attachments (0)
