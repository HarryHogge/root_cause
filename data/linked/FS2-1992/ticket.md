# FS2-1992: VXEP-416 Investigation (v539) Failure to Launch

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-06-19
- **Updated:** 2024-10-21
- **Resolved:** 2024-10-21
- **Reporter:** Jason Scherer
- **Assignee:** Jason Scherer
- **Creator:** Jason Scherer
- **Parent:** FS2-1993 VXEP-416 Failure to Launch - Vehicle Investigation
- **Links:** relates to VXEP-416 (VXE 539 Failure to launch)
- **Epic Link:** FS2-1993
- **Sprint:** FS2 Sprint 19, FS2 Sprint 20, FS2 Sprint 24, FS2 Sprint 21, FS2 Sprint 22, FS2 Sprint 23, FS2 Sprint 25

## Description

Blocked: Waiting for input from hardware engineer on CAN timeouts.
First launch failed because VTOL was still in SAFE mode. The VTOL aborted launch with the error “mc launch trigger fail: safe”. After the first launch failure, the VTOL enters an RTL (Return To Land) loop where the RTL command is executed then landing is detected (since the vehicle is on the ground) then RTL executes again and so forth. Second launch attempt failed because VTOL was in an RTL loop.
Questions:
- Why was the VTOL still in SAFE mode when the launch command was given?
- If you compare the two launches on the XComm event logs it looks like the first launch didn’t send a “set mode 4” message. I believe this message could be what causes the safe mode to be disabled. Although, it could also just be that the message wasn’t logged because the mode was already 4 (guided) on the second attempt.
- Why did the VTOL start RTL loop? Possibly because avionics was reset per the observer description. But then why did RTL loop not stop after the avionics restarted?

Notes:
- VTOL chart (CSV) timestamps are ~6 seconds ahead of XComm timestamps.
- VTOL event log timestamps are about 8 hours off (VTOL is 13 hours versus XComm 21 hours) with the same ~6 seconds (VTOL ahead). I believe this is due to something like a time zone issue with the logging code.

[embedded: image-20240713-013757.png]

Launch attempt 1 sequence below:
[embedded: image-20240713-011607.png]
Prior to second launch attempt VTOL is stuck in an RTL loop. This code is part of the VTOL loss of signal code. This may be due to resetting the avionics.
[embedded: image-20240712-170915.png]
VTOL switches back to RTL after second launch commanded (“APVTOL_TAKEOFF”)
[embedded: image-20240712-171420.png]
Timeline for second launch attempt:
This time motors spin up since VTOL was not in a SAFE mode. However, it appears that RTL loop quickly aborts the launch. You can see below that SAFE mode goes to 0 before the ARM goes to 1. Once the launch is aborted the SAFE mode goes back to 1.
[embedded: image-20240713-013151.png]
Log coverage of second log with timeline and throttle data:
[embedded: image-20240713-013407.png]
Code that should have disabled SAFE mode the first launch
This is the code that updates the SAFE mode on the VTOL. This code is called when a MAVlink message (MAVLINK_MSG_ID_SET_MODE: MAV ID: 11) is received over the CAN bus. The message is passed to this code and, if the safety mode bit is different than the current state of the system, the handle_safe function is called with a value of '1' as the source. This is why we see the message in the log reflect “MC unsafe 1” in the second launch attempt. 
[embedded: image-20240713-015059.png]
[embedded: image-20240713-014730.png]
[embedded: image-20240713-015142.png]
[embedded: image-20240713-015213.png]
This is the XComm code that sends that CAN MAVlink message to the VTOL controller:
[embedded: image-20240713-020011.png]
I believe this (below code) is most likely the code that sends the unsafe command to VTOL during launch. I base this on the fact that the XComm log shows “Takeoff” and “LAUNCH” during the second launch attempt indicating that this code is indeed active at the time. After those messages are logged, the XComm sends messages to the VTOL processor setting the flight mode to Guided. This is reflected on the VTOL event log during the second launch right before the message “MC unsafe 1”.
[embedded: image-20240713-021125.png]
In the function below the variable ‘safelast’ should be declared as a static variable. Since it is not, the “SAFE OFF” debug message will never show up in the log. This makes it hard to determine if this function was called to send the safe off command.
[embedded: image-20240828-194647.png]

## Comments (1)

### Jason Scherer, 2024-07-12

@David Grosher The main issue with this incident is that the VTOL was in SAFE mode when the first launch was activated which caused the VTOL to enter an RTL loop which caused the second launch attempt to abort. They restarted everything except VTOL between launches, so the VTOL never got back to a good state. We should consider updating the launch wizard to restart the VTOL as well as the avionics like it currently does.
I was able to recreate the issues described in the incident by commenting out SendSafetySwitch(false) on lines 5312 & 5313. I’m not sure why this function didn’t seem to execute twice. I could see the message getting dropped maybe in a queue or on the CAN bus, but I would have expected to see the “SAFE OFF” message in the log for the first launch, but it is not there. Maybe XComm got into a weird state where it thought the safe mode was already off, so no message goes to logs. I think this is probably the most likely reason, but I haven’t looked further yet. If I get some time this weekend I may pull on that thread some more.
On another note. The HLB voltage seems higher than normal >30V. Also, the current is all over the place when the lift system is not on. Maybe this is because of the goofy state that the vehicle got into. However, it might be a good idea to have them to run a motor test and send us an AAR for evaluation before letting them fly.
[embedded: image-20240713-041343.png]

## Attachments (14)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240712-170915.png | image | 715 | 2024-07-12 | listed only |
| image-20240712-171420.png | image | 417 | 2024-07-12 | listed only |
| image-20240713-011607.png | image | 427 | 2024-07-12 | listed only |
| image-20240713-013151.png | image | 19 | 2024-07-12 | listed only |
| image-20240713-013407.png | image | 97 | 2024-07-12 | listed only |
| image-20240713-013757.png | image | 516 | 2024-07-12 | listed only |
| image-20240713-014730.png | image | 44 | 2024-07-12 | listed only |
| image-20240713-015059.png | image | 44 | 2024-07-12 | listed only |
| image-20240713-015142.png | image | 23 | 2024-07-12 | listed only |
| image-20240713-015213.png | image | 22 | 2024-07-12 | listed only |
| image-20240713-020011.png | image | 26 | 2024-07-12 | listed only |
| image-20240713-021125.png | image | 46 | 2024-07-12 | listed only |
| image-20240713-041343.png | image | 70 | 2024-07-12 | listed only |
| image-20240828-194647.png | image | 44 | 2024-08-28 | listed only |
