# MS-1684: VSM: Accommodate MCM Restarts in Flight

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2026-07-09
- **Updated:** 2026-10-05
- **Resolved:** 2026-10-05
- **Reporter:** Craig Burton
- **Assignee:** Craig Burton
- **Creator:** Craig Burton
- **Links:** relates to VXEP-1956 (VXE 880 MCM Reset inflight after gimbal power cycle); relates to VXEP-1890 (VXE 902 - user power cycled aux 1&2 simultaneously, and lost comms with the A/C for ~2 minutes. CHAOS payload); relates to VXEP-2005 (VXE 966 MCM reset led to uncommanded climb ); relates to VXEP-1315 (B30 Systemic MCM Resets due to payload power)
- **Sprint:** MS Sprint 34

## Description

This feature enables operators to upload routes following an in-flight reboot of the MCM. The Launch Wizard-calibrated altitude is stored in the VSM’s database at calibration/launch. Under normal circumstances, i.e. if the MCM is not rebooted in flight, the stored value will not be utilized.
However, the periodic mission operation in the database now looks for a case in which the vehicle is in flight and the calibrated altitude has not been set. If this case is encountered, the calibrated altitude value is retrieved from the database and utilized, allowing the operator to upload new routes or command Loiter. An alert is also broadcast for awareness, since the UI will not display any routes after the reboot.
The database had to be used to cover the case in which flight operations are performed in an area without DTED coverage. In areas with DTED coverage, the VSM’s reference altitude matches the value commanded to the AP. Without DTED, the AP must be commanded with a reference altitude of 0, but the VSM still needs to have the actual MSL elevation in order to process waypoints it receives from GCSs that are not in the AGL reference frame.

## Plan

Mitigation assumes VTED has already been loaded.  For flights in areas with no DTED, additional functions required.  Will scope as effort proceeds.

## Issue Status

Handle base case of allowing routes to be uploaded.Ensure FixedWingAPHasBeenReset() conditions are satisfied for in-flight init.Prevent Loiter from being commanded by an operator until calibrated altitude is set.Test transitions from Route, Loiter and U-Drive.

## Comments (3)

### Craig Burton, 2026-09-23

The PR is in review.  Testing notes:
- On test MCM, move DTED so that it can’t be found at runtime.
- cd /opt/maps/
- sudo mv dted dted-not-available
- Install OGCS/VSM
- It is important to install after the DTED has been moved, so that OGCS hasn’t cached anything.
- Launch as usual, noting to look for calibration warnings that DTED is not available.
- Wait until the vehicle is flying in its Primary route and then disconnect power to the MCM.
- Count to 5, then reconnect the MCM to power.
- Observe the OGCS web UI displaying stale telemetry warnings.
- After about 1.5 minutes, observe the resumption of telemetry and two specific alerts:
- “No one is in control”
- “MCM restarted in flight”
- Take control.
- Command Loiter and observe stable altitude.
- Upload stored routes.
- Command Go Tos.
- Observe safe landing.
- Cycle the test.
- Stop OGCS and VSM temporarily.
- Move the DTED back to where it can be found.
- Remove the EMPTY dted directory created by OGCS mounts.
- sudo rmdir dted
- Move DTED back into position.
- sudo mv dted-not-available dted
- Start OGCS and VSM.
- Perform the same tests as above.

### Craig Burton, 2026-09-23

Sample event log messages from testing (unrelated messages removed).
Startup without DTED:
12:00:47.573363:  oper            Vehicle reporting reference altitude of 0 ft MSL.
12:00:59.514466:  oper            Sending reference LLA commands to AP
12:00:59.514504:  oper            Vehicle reference altitude has been commanded to 779 ft MSL.
12:00:59.514518:  oper            Vehicle reference altitude adjusted to 0 ft AGL (no DTED).
12:00:59.652521:  db_update       Commanded reference altitude persisted
Flight, then plug is pulled:
12:05:35.652802:  oper            MCM restarted in flight
12:05:35.653153:  oper            Updated calibrated reference altitude to 779 ft MSL
12:05:40.803584:  oper            Vehicle reporting reference altitude of 0 ft MSL.
Loiters, Go Tos, then safe landing.
Test cycled and DTED added:
12:17:39.395465:  oper            Sending reference LLA commands to AP
12:17:39.395512:  oper            Vehicle reference altitude has been commanded to 751 ft MSL.
12:17:39.768482:  db_update       Commanded reference altitude persisted
12:17:46.584106:  oper            Vehicle reporting reference altitude of 751 ft MSL.
Flight, then pull the plug again:
12:22:08.076156:  oper            MCM restarted in flight
12:22:08.076553:  oper            Updated calibrated reference altitude to 751 ft MSL
12:22:10.396456:  oper            Vehicle reporting reference altitude of 751 ft MSL.
Loiters, Go Tos, then safe landing.

### Craig Burton, 2026-10-05

Merged.

## Attachments (0)
