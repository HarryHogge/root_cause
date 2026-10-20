# VXEP-723: VXE 724 MCM reset when changing HLB, other potential issues

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-10-15
- **Updated:** 2026-09-23
- **Resolved:** 2025-08-05
- **Reporter:** Cameron Chapman
- **Assignee:** Connor Peebles
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-729 (128-117156-01 SLA Breakout improvements for next revision (Rev C to Rev D)); causes VXEP-730 (128-117156-01 Rev B SLA Breakout Board - Increment to Rev C); relates to VXEP-844 (VXE724 VTOL Climb Abort Lift System Fault); relates to VXEP-1315 (B30 Systemic MCM Resets due to payload power)
- **Vehicle Tail Number:** 724
- **Corrective Action:** - https://jenaero.atlassian.net/browse/VXEP-730
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Copying from NCR NCR List - AC 724 - Flight Test - MCM reset abnormal
“Brought 724 out for flight test another time and ran into more issues.
When changing the HLB the power or something for the MCM is cycling causing the VSM to reset and loose all data (this was noticed because the mission had already been done and uploaded and then it cleared after changing the HLB)
This behavior is believed to not be observed in other PreMAG AC and seems to be isolated to AC 724.  
After checking the VSM up time and the XCOMM up time they were not the same and it seemed to only be cycling the MCM. “


Craig Burton commented
@Cameron Chapman While it would have been possible to re-load the mission, we did not want to risk an MCM power reset in flight, which would trigger a Lost Comms scenario. This same vehicle had a prior electrical (harness) issue, so we opted for an abundance of caution. @Dave Grosher @Ted Trowbridge less

Investigation Data collected here: 128-117156-01 Rev B SLA Breakout Board - Increment to Rev C (VXEP 730)
PPT for investigation & resolution here: VXEP 730 - 128-117156-01 Rev B SLA Breakout Board - Increment to Rev C.pptx

## Plan

- Investigate C/CA.
- Potential solutions
- Specific order of connection
- Connecting HLB Data before or after HLB power does not prevent transients any more or less
- Accept MCM reset when HLB is swapped and reconfigure.
- Update SLA board to increase:
- Transient filtering, Overvoltage shutoff limit, Undervoltage lockout limit: https://jenaero.atlassian.net/browse/VXEP-730

## Root Cause

SLA Breakout 128-117156-01 Rev B has the Over Voltage Protection pin of both E-Fuses set to ~35V. When plugging in the HLB data cable, transients can occur that may briefly trip the E-Fuse protecting the MCM, which then has the possibility to drop power below the 9V minimum of the MCM.

## Comments (16)

### Ruysser Gabler, 2024-10-16

Hey @Cameron Chapman this AC is a Pre MAGNSS AC 

Here are the NCR’s for AC 724 since it has come to flight test 
AC 724 - Flight Test - MCM reset abnormal
AC 724 - Flight Test - Stiff Vertical stabilizer
AC 724 - Flight Test - VTOL GPS Fail
AC 724 - Flight Test - VTOL Land odd decent
AC 724 - Flight Test - Failed to reset
AC 724 - Flight Test - ADP cant see Fwd Prop
(SCO) Intermittent Connection Between XCOMM and SLA
I understand that some may not be associated with this but wanted to get all info here for the investigation 

Here

### Craig Burton, 2024-10-16

Vehicle 724 is preMAGNSS and has had several associated NCRs (thank you for capturing all of them in the above comment, Ruysser!).

This latest issue was reported because the MCM’s power was interrupted in the process of swapping an HLB during preflight.  FLOPS ssh’d into the MCM and ran the “uptime” unix command which reported that the MCM had only been running a few minutes, indicating that a power cycle had occurred.  This is not simply that the VSM process was stopped and restarted, but rather the entire MCM had been rebooted.  By using the vehicle web pages, FLOPS was able to determine that the AP had been up ~20 minutes longer than the MCM, indicating a power cycle on MCM.

FLOPS has replaced HLBs without rebooting the MCM in other vehicles.  Out of an abundance of caution with this specific vehicle (due to the long and growing list of NCRs), and wanting to avoid an unplanned LOS situation, we decided not to fly and create another NCR for further analysis.
@Scott Whitney FYSA

### Connor Peebles, 2024-10-16

Initial thought is that there was a transient that exceeded the electronic fuse Over Voltage Protection that is set to 34.9V on the SLA Breakout Board V2.

[embedded image-20241016-164406.png]
Going to make a breakout pigtail for the Glenair payload to scope the behavior on the payload E-fuse, which has the same over-voltage protection value set. If I am right, we should have the potential for a similar dropout there when swapping HLB’s.

### Ruysser Gabler, 2024-10-17

@Cameron Chapman @Connor Peebles  I was able to test this again with another PreMAG vehicle. It actually showed the same behavior of resetting. So the other vehicles that we have done it on and not seen it may very well be outliers.  I still think that there is a problem here in general but not sure of the importance of it. Also very well may be that the vehicle I tested it on  has an issue just like 724 and they are the only 2 or something

### Cameron Chapman, 2024-10-17

@Ruysser Gabler @Connor Peebles agreed. We definitely have some grounding/low side issues. For one, the HLB BMS bypasses the ground isolation circuit developed as a fix for a similar issue. Potential solutions
- Specific order of connection
- Accept MCM reset when HLB is swapped and reconfigure.
- Update SLA board to increase transient current limit.
- Possibly others.

### Connor Peebles, 2024-10-17

@Ruysser Gabler @Cameron Chapman I agree, the conclusion that I was coming to is that you will probably see this on more planes, but you beat me to it.

Cameron, on point 3., I’ll add:
- Update SLA board to increase:
- Transient filtering
- Overvoltage shutoff limit

### Liam Limon, 2024-10-17

@Connor Peebles if you need Glenair breakout cables we have 3 sets of all the harnesses now and you could borrow one.

### Connor Peebles, 2024-10-18

D5 - Impacts would be the possibly of MCM reset upon HLB data plug in for all aircraft with 128-117156-01 Rev B installed

### Connor Peebles, 2024-10-18

D5 - Determine CA: Changing values of some of the components of 128-117156-01 so that the E-Fuse is not tripping Over Voltage Protection upon common voltage transient, Adding more filtering. Will require a board spin.

### Connor Peebles, 2024-11-25

D6 - Implementing Corrective Actions: see [VXEP-730] 128-117156-01 Rev B SLA Breakout Board - Increment to Rev C - Jira

### Cody Smisek, 2024-12-23

This Jira issue contained a confusing title and was also missing the vehicle number in the details. I have updated from 723 to 724. 
@Cameron Chapman @Connor Peebles

### Connor Peebles, 2025-04-30

moving this investigation to CCB

### Lauren Velasquez, 2025-06-05

724 has moved from RMA to FLOPS

### Lauren Velasquez, 2025-06-10

FLOPS returned 724 to RMA area

### Christa Meck, 2025-08-05

@Connor Peebles Where are we at on this investigation?

### Connor Peebles, 2025-08-05

@Christa Meck Change was implemented, has been in production

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20241016-164406.png | image | 183 | 2024-10-16 | listed only |
