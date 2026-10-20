# FS2-2319: Investigate automatically engaging VTOL system when sensor failures are detected in the FWAP in order to prevent crashes.

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2024-09-24
- **Updated:** 2025-09-23
- **Resolved:** 2025-09-23
- **Reporter:** Eric Brewer
- **Assignee:** Eric Brewer
- **Creator:** Eric Brewer
- **Components:** Emb SW Robustness
- **Parent:** FS2-2381 VXEP-619 Loss of Aircraft in FW flight
- **Links:** relates to VXEP-619 (VXE 644 Loss of aircraft while in fixed wing flight.  Aircraft rolled over and crashed straight into ground.)
- **Epic Link:** FS2-2381

## Description

Consider adding error checking to the fwap code to detect out of range or likely out of range measurements from the IMU.  IN the case where the IMU is determined to be failed, engage the VTOL system with land immediately in order to potentially save the vehicle.

## Sprint

FS2 Sprint 33, FS2 Sprint 34, FS2 Sprint 27, FS2 Sprint 30, FS2 Sprint 28, FS2 Sprint 31, FS2 Sprint 26, FS2 Sprint 32, FS2 Sprint 29

## Comments (4)

### David Grosher, 2024-10-01

@Eric Brewer I think it would easier from a mode control perspective if instead of engage the VTOL system we send IMU data or INS data from the VTOL to the FWAP if an error on the IMU is detected. We could also inform the user so that they can issue a LI once in a safe location if latency results in the system being marginally stable.

### Eric Brewer, 2024-11-07

Browsing the fixed-wing code, the code implementation is somewhat nontrivial since we’d need updates within the fast task to stop reading existing sensors and plumb in values from xcomm/vtol link.  I can run a quick feasibility test once SG is available to determine how much latency we can tolerate on the fixed-wing loops before they become unstable.

### Scott Whitney, 2025-09-23

@Eric Brewer  @David Grosher - I am going to cancel this task (and epic) based on the VXEP being closed. If the investigation is reopened. We can reopen or create a new set of tasks

### Scott Whitney, 2025-09-23

No further information or data from customer. https://jenaero.atlassian.net/browse/VXEP-619 has been closed.

## Attachments (0)
