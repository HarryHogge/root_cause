# VXEP-1556: VXE 881 Erroneous servo and forward prop behavior with Orbital Drop kit attached

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2025-10-17
- **Updated:** 2026-03-02
- **Resolved:** 2026-02-02
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Alexander Alan Arnold
- **Creator:** Alexander Alan Arnold
- **Labels:** LRR_Internal_Asset, Weekly-incident-tracker
- **Customer:** LRR
- **Vehicle Configuration:** 35X, battery, no gimbal
- **Severity:** 1 - Flight Critical

## Description

ISSUES WITH ORBITAL DROP CONFIGURATION
Complete configuration: aircraft weight was 47.6.   pounds, without gimbal.
VXE B35X SN 881
HPMB 8-003
Aux payload cover
Orbital PMM
2x Orbital PRM
2x Orbital DGM
 
With aircraft powered on the aircraft lost power to the forward motor and the servos upon connecting the PMM. 
PRMs were disconnected with no result. 
Aircraft power was cycled with no result. 
PMM was disconnected via securing Aux payload port 2 power. 
Aircraft resumed normal functionality. 
PRMs were re-connected, no loss of function. 
PMM was re-connected and no loss of function.
After about 10 minutes, Launch Wizard was started and the aircraft had lost power to the front prop again, noticed upon front prop test in Launch Wizard. 
Aircraft power was cycled to the plane and front prop and servos are working again.
 
Orbital equipment was disconnected and launch wizard was conducted to the point of Arm/ Launch with no abnormalities.

## Plan

- @Alexander Alan Arnold the aircraft might have been damaged, so it should be grounded until some investigation happens. Please red tag the aircraft.
- Data Review. @Alexander Alan Arnold are you guys available to do some data review? If not, I recommend asking Dave if his group is available to support that
- @John Gober  is investigating on site. Please report plan and findings here.

## Comments (1)

### Scott Lovett, 2026-02-02

Aircraft has flown since this incident.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| VTOL 881 FTP.zip | archive | 59766 | 2025-10-17 | listed only |
| XCOMM 881 FTP.zip | archive | 24601 | 2025-10-17 | listed only |
