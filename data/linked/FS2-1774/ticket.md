# FS2-1774: Crash after transition (v540)

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-04-22
- **Updated:** 2024-05-02
- **Resolved:** 2024-05-02
- **Reporter:** Scott Whitney
- **Assignee:** David Grosher
- **Creator:** Scott Whitney
- **Labels:** USASOC, Weekly-incident-tracker
- **Components:** Vehicle Incident Support 
- **Fix versions:** Release 6.3.4
- **Links:** clones VXEP-284 (VXE-540 Crash after transition at training event); relates to RMA-220 (VXE-540 240223); relates to FS2-1579 (Implement CAs from v540 investigation)
- **Vehicle Tail Number:** 540
- **Vehicle Configuration:** Battery only, no fuel cell
- **Issue Status:** Suspect potential cross talk from 547.
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

VXE-540 Crash during transition at Fort Moore, GA customer training event. 
Customer owned aircraft. 
Scott Shilvock's witness statement: About 5 seconds after launching the aircraft and with it already climbing, we received a "Launch Error" dialog box that indicated we should not launch the aircraft despite it already being in the air (attached).  Afraid that it may put the aircraft into a non-airborne state we hesitated to click OK as the vehicle was climbing normally.  I called Dana Holley over to take a look and the aircraft turned to a 090 heading and visually appeared to transition to normal fixed wing flight as was confirmed in the VTOL Messages section despite the flight plan to initiate the transition in a roughly 315 heading. The aircraft transited out of sight due to the close proximity of trees blocking our visibility.  No other commands could be given until the "OK" button was pressed in the dialog box and shortly after we lost communication.  Despite taking antennas up to the roof and going mobile with another antenna in a truck that drove to the east we were unable to regain communication and the aircraft never appeared in its lost communication orbit.  Airspace controllers were notified, and we sent a team out to the last reported location.  They were able to locate the aircraft approximately 350 meters east of that last known track location.  The wing structure was roughly 100 feet up in the top of the trees with the rest of the fuselage below it on the ground.
 
Saving files here. VXE540 Mishap After Transition-2024-02-22 1

Report

## Corrective Action

- Need to link or open Jira issues for each of these.
- Review Training
- Handling Sensor Errors
- Handling error warnings on launch / Launch abort
- Prevent VTOL ARM if FW fails to ARM
- Warn User sooner before launch as the error state was detected

## Plan

1.Determine how a operator can unintentionally erase the mission. Mission was on GCS in pictures.
2.Determine if Launch Wizard Logic can be bypassed prior to receiving a response from AP regarding the sensor health
- Need to link or open Jira issues for each of the C/CAs.
- Planning to pull data to inspect for cross talk. Flight ops said they would pull GCS log

## Root Cause

- The aircraft crashed because the FW AP was in idle state and never tried to fly the plane after VTOL AP transitioned to FW flight.
- The FW AP rejected the ARM command multiple times because there was no mission loaded.
- A mission had been loaded but it was erased.
- Despite this, it is unclear if the aircraft should have passed through the launch wizard, in response to a COMMAND_SENSORHEALTH, an IMU error was detected and logged in the XCOMM log. This was seen multiple times, perhaps it was tried until it passed? We still need to document the exact Launch Wizard behavior here.

I see two problems here:
- potential operator error
- Yet another mode logic RACE condition, as the VTOL AP should not have transitioned to ARMED if the FW AP failed pre-condition checks.

## Comments (0)

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Incident-Mishap Ft. Moore..docx](attachments/20193_Incident-Mishap%20Ft.%20Moore..docx.md) | docx | 1179 | 2024-04-22 | converted |
| Last Screenshot.jpg | image | 2567 | 2024-04-22 | listed only |
| Screenshot of Error.jpeg | image | 502 | 2024-04-22 | listed only |
| T95_V547_240228_103325_pack.zip | archive | 3704 | 2024-04-22 | listed only |
| VXE540 Mishap After Transition-2024-02-22 1.zip | archive | 20942 | 2024-04-22 | listed only |
| image-20240223-000039.png | image | 30 | 2024-04-22 | listed only |
