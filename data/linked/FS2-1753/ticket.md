# FS2-1753: v426 Investigation (Slow descent, land on fence)

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-04-17
- **Updated:** 2024-05-22
- **Resolved:** 2024-05-17
- **Reporter:** David Grosher
- **Assignee:** Ben Triplett
- **Creator:** David Grosher
- **Parent:** FS2-1768 VXEP-365 Slow descent in VTOL landing
- **Links:** relates to VXEP-365 (VXE 426 Slow descent on VTOL landing, crash landing into a fence); relates to VXEP-412 (VXE 426 Overshoot on landing, becoming progressively worse)
- **Epic Link:** FS2-1768
- **Sprint:** FS2 Sprint 18, FS2 Sprint 17

## Description

Slow descent was a bug fixed in 1.53. It was due to a drop in barometric pressure during flight that resulted in a mismatch in the baroAGL and LRF AGL readings. The delta caused a continue change in state during landing that kept changing the commanded Vd, resulting in a very slow descent that caused a number of crashes.  This bug behavior changed based on how far the landing was away from launch. Because if landing was at launch, the ground altitude was assumed to be known. 
This incident had the latest code 1.54.02. But perhaps there is another failure mechanism in related code. Scott Hunter and Kurt worked on the previous fix. 
Vehicle Investigation VXE426 Slow Descent.pptx

## Comments (2)

### Ben Triplett, 2024-04-22

Powerpoint analysis uplinked. 
Summary:
- Position overshoot on transition - apparently due to winds - resulted in additional time before descent started
- 200 ft offset error resulted in transition to 3 ft/s descent rate 200 ft higher above ground than intenede (compared to 7.5 ft/s before reaching ground level)
- Apparently degraded VTOL main battery put operators under additional pressure as AV neared the ground
- Nudge command moves the position setpoint - not intuitive - AV landed on fence. AV tracked position setpoints well but final setpoints put AV over the fence

### Gabriel Staples, 2024-04-22

note to self: Vd = “velocity down”

## Attachments (0)
