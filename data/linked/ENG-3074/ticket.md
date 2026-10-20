# ENG-3074: 539 Failure to Launch

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-05-21
- **Updated:** 2025-06-02
- **Resolved:** 2025-02-18
- **Reporter:** Daniel Lloyd
- **Assignee:** Pat Wells
- **Creator:** Daniel Lloyd
- **Labels:** TIQUILA
- **Links:** relates to VXEP-416 (VXE 539 Failure to launch); relates to RMA-358 (VXE-539 TIQ 240924)

## Description

During a training flight the aircraft was armed, and launch was selected. The aircraft did not respond. Three attempts were made. During one attempt the VTOL message “Launch abort, lift power fault” was displayed. 
@Pat Wells @Garret Moose @matthew.curran

## Comments (10)

### Pat Wells, 2024-05-22

@Daniel Lloyd received and investigation underway.
Who is the customer?

### Daniel Lloyd, 2024-05-22

Tiquila

### Daniel Lloyd, 2024-05-22

More information from the trainer.
“Yesterday, V539 flew its first flight of the day with no issues.  During Launch Wizard for its second flight, it failed the first Sensor Calibration, then passes a few seconds later, and passed the second Sensor Calibration the first attempt.  When commanded to Launch, the screen said “Waiting to detect launch” for about a minute, the window to “Enable User Launch Control / Abort“ was open.  I noticed the VTOL status window on the right of the screen said Entering RTL mode (RTL = Return To Launch point).  The plane had aborted the launch before engaging the lift rotors.  The “Waiting to detect launch” and “Enable User Launch Control / Abort” windows remained open.  We enable user launch control and commanded “Cut motors and safe vehicle”.  Instead of closing, the window changed back to “Enable User Launch Control / Abort” window.  We disconnected from the plane and closed and restarted the CGS software.  The “Cut motors and safe vehicle” was still open.  Resetting the autopilot (in the launch wizard) did not result in the window closing. 
On the second launch attempt, all four lift rotors engaged at a low power setting.  The plane did not come close to lifting out of the stand.  The “Enable user launch control” button was open, but grayed out and we were not able to enable user launch control or command Cut motors and safe vehicle (from that window).  The autopilot aborted the launch.  VTOL status window said “Landed”.
 We produced a second AAR w/ FDR. 
We disconnected from the plane, closed the GCS software, and restarted the GCS laptop.  We disconnected the aircraft main power cable from the main battery, waited 10 seconds, and reconnected it to fully reset the plane.  Third launch attempt was like the first: the screen continued to say Waiting to detect launch and the VTOL status said Entering RTL mode.  A third AAR w/ FDR was produced and the plane was put away.”
@Pat Wells

### Daniel Lloyd, 2024-05-30

Is there any update on this investigation?
@Pat Wells

### Pat Wells, 2024-06-03

@Daniel Lloyd no updates as of today.  I’ve reached out to the engineering team to see if we can get some movement.

### Pat Wells, 2024-09-13

@Daniel Lloyd @Garret Moose @matthew.curran  The engineering team would like to have this aircraft returned on an RMA so they can further investigate the hardware in order to determine the root cause.
@Sean Odell FYSA please process the RMA.

### Pat Wells, 2024-09-17

@Sean Odell have you followed up on this ?

### Sean Odell, 2024-09-17

@Pat Wells Currently Jeff is estimating it will be delivered to him this coming Thursday. Then he does his processing before asking me for an RMA. So no ticket generated until I get the official request (likely this Thursday or Friday).

### Daniel Lloyd, 2024-09-23

Aircraft was received in SLO on 20 Sept. @Pat Wells

### Pat Wells, 2024-09-23

@Sean Odell  FYSA aircraft is in SLO

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V539_240521_105943_01_pack.zip | archive | 2271 | 2024-05-21 | listed only |
| T95_V539_240521_105943_pack.zip | archive | 1078 | 2024-05-21 | listed only |
| T95_V539_240521_142311_pack.zip | archive | 1423 | 2024-05-21 | listed only |
| T95_V539_240521_143419_pack.zip | archive | 875 | 2024-05-21 | listed only |
| [Vehicle Investigation 539.pdf](attachments/26310_Vehicle%20Investigation%20539.pdf.md) | pdf | 2214 | 2025-02-18 | converted |
