# ENG-3065: AC 482 Crash

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-09-17
- **Updated:** 2025-06-02
- **Resolved:** 2023-12-12
- **Reporter:** Daniel Lloyd
- **Assignee:** Pat Wells
- **Creator:** Daniel Lloyd
- **Labels:** MARSOC
- **Links:** relates to VXEP-99 (VXE-482 loss of altitude and crash); relates to FS2-986 (VIT2-448 AC 482 Crash); relates to FS2-1152 (Evaluate transferring flight logs during flight, in the case of lost vehicle/logs. )

## Description

As reported from the deployed customer:
Aircraft experienced loss of altitude control over target objective in orbit 4.  Operator recommanded orbit 4 however the aircraft was unable to maintain altitude.  Orbit 3 was commanded to fly the aircraft away from objective.  Aircraft was still unable to maintain altitude and U-drive was commanded to attempt to regain altitude control and manually steer the aircraft away.  Link was lost at 367 feet before the U-drive command could be sent.  MSOC declined to recover aircraft due to partner force protection and operational concerns.

## Comments (9)

### matthew.curran, 2023-09-21

The preflight power was 42.7W, the power during and after the altitude loss was 50 W.  The added 7W is likely due to servos.  Commanded throttle was 100% during descent with what look like ESC throttle resets.  
If the no load power on the nose motor is greater than 7 W, then the cause might be the spinner coming off.
If the no load power is less than 7 W, then the ESC may have stopped driving the motor.
What is the no load power from the motor at 100% throttle?
Is the AP limiting the power on the climb because the HLB is low?

### Pat Wells, 2023-10-02

@Daniel Lloyd could you please request SA CAM and payload video from the customer? 
If they are unable to release it, ask them to review it for
- any signs of incoming fire
- sudden jolts to the aircraft
- If the forward propeller is present.
- If so, is it spinning at commanded speed, windmilling, or still/folded back?

### matthew.curran, 2023-10-05

will do

### Connor Peebles, 2023-10-11

status set to waiting for customer to provide data/video

### Pat Wells, 2023-10-20

@Daniel Lloyd @matthew.curran 
Any feedback from the customer on the request to review video?

### Daniel Lloyd, 2023-10-23

@Pat Wells A request was sent to the customer but no files have been received.

### Pat Wells, 2023-11-03

@Daniel Lloyd  just following up on customer request to provide or review video with feedback. Any updates?

### Daniel Lloyd, 2023-11-08

@Pat Wells I haven’t heard anything and I don’t expect we ever will.

### Pat Wells, 2023-12-12

Investigation complete.  Forward propulsion ESC failure.  Report attached. 
Replacement ACFT being provided under warranty.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [VIT2-448_VXE-482_Investigation (71253279-82b9-42c2-88ad-54fef7685b65).pdf](attachments/17811_VIT2-448_VXE-482_Investigation%20(71253279-82b9-42c2-88ad-54fef7685b65).pdf.md) | pdf | 641 | 2023-12-12 | converted |
