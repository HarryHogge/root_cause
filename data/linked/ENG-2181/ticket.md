# ENG-2181: EA Internal: VXE511 Aborted Launch at 2ft, VTOL ESCs stuck in initialization loop

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Highest
- **Created:** 2023-08-09
- **Updated:** 2023-09-05
- **Resolved:** 2023-08-10
- **Reporter:** Cameron Chapman
- **Assignee:** Carson Buckley
- **Creator:** Cameron Chapman
- **Links:** relates to VA-31 (EA Internal: 516 center wing damaged. 511 fuselage+516CW LW motor test failed. ); duplicates VA-33 (VXE511 Aborted Launch at 2ft, VTOL ESCs stuck in initialization loop); relates to VA-35 (511 CW Input power connector damaged); is caused by VXEP-28 (TPTR-94 HLB reading incorrect percentage compared to measurement with checker); relates to VXEP-481 (8D #24 – CW to HLB AS150 Connection Issues​ Corrective Actions); relates to VA-95 (8D #24 Update HLB Lift Connector to include some physical indication connection is fully seated. Evaluate adding to similar power connectors )
- **Part Number(s):** VXE30
- **Other Stakeholder (as required):** Matt Philley
- **Problem Type:** Other (explain in description)

## Description

See external issue https://jenaero.atlassian.net/browse/VIT2-340 
 CA-07-23 Defective part delivered to customer
During TIQUILA FAT, UK MOD Asset VXE511 experienced an abrupt aborted takeoff with all four motors cutting at ~6” above the stand. The vehicle fell back onto the stand, knocking the stand over and causing minor damage to the fuselage composites around the payload bay opening. IIn the video below (IMG_1722.mov), the motors can be heard repeatedly resetting in a loop until the GCS operator issued a cut and safe command. Subsequently, the operator was unable to download the data from the aircraft via the AAR window. It appeared to have been stuck on the file FLTFILES.txt, and would eventually time out itself or the operator would cancel the download. Attempting to skip that file in the pop up window would not work. So all files were downloaded manually and married up with the AAR data that did download. The event appears to have been recorded in VTOL0087 and XCL00081. Preliminary review of the files shows an abnormal voltage drop when the lift motors activated for launch.
Post flight, the ground crew cycled the main battery and VTOL battery power. Using the launch wizard motor check, the operator conducted multiple tests with all of motors running at the same time, with the same hybrid lift battery, resulting in around 400W of total power. The XCOMM hybrid lift battery page was open showing all cell voltages while all four lift motors were activated. Cell voltages remained nominal through the motor tests and the lift motors returned to home position multiple times without issue. We were unable to replicate the initialization loop. It is a theory that the low voltage may have caused the lift ESCs to get stuck in an initialization loop (sorta what happens to your cars systems when you try to start the engine with a low/dead battery).
After completing the launch wizard tests, the vehicle was disassembled for inspection. The connector did not smell and showed no signs of overheating, however a solder ball was noted on one of the VTOL male connector pins. The female of this pin showed signs of it rubbing off on the mating side. We do not know if this solder ball was present before the test. If it was a manufacturing defect present before the test, it may have prevented the connector from being fully mated, resulting in a poor connection and subsequent voltage drop under load. This needs to be investigated in the shop.
The battery is being returned to the shop and needs to undergo a simulated launch discharge profile to certify that the cells perform properly under full load. Recommend a couple of cycles.
The customer requests us to advise them ASAP whether this vehicle is safe to return to flight on Wednesday.
Post FAT, the customer requests repair to the payload bay opening under warranty.

## Corrective Action

CAR CA-07-23 Defective part delivered to customer
-Ensure all cases in investigation and parts when removed from the case are red tagged.
-RMA tickets should be complete and signed off before vehicles are returned to flight/customers. 
- After RMA, vehicles should get SCO flight before delivery to customers
-Damage missed during original intake and discovered during investigations should then be added to RMA, to ensure resolved before returning parts. 
-Recommend not modifying parts involved in investigation until all stakeholders agree on next steps. "removed the solder blob and hover-tested the center panel at 75% power for 60 seconds without issue"
-Asset planning and tracking should ensure that all issues have been resolved and aircraft is approved for flight before it is needed for an event.

## Plan

Investigate cause of initial issue: https://jenaero.atlassian.net/browse/ENG-2182
Verify that cause above also would have caused this incident.

## Issue Status

1. 511 wing was damaged, in engineering for troubleshooting, and should not have been flown or delivered to the customer. See https://jenaero.atlassian.net/browse/ENG-2181. The findings were reported in JIRA, but wing was not red tagged. 511 RMA was not updated to indicate connector damage.
-HLB 2-1803 had a low voltage issue reporting from GCS SW when this HLB was installed during earlier attempted flight. Battery checker showed appropriate voltage. This battery was set aside as not to be used, but was not marked as NFF (schedule pressure reported). This battery was then used on this flight. The battery shows a missing retention ring, and small amounts solder of the end of the socket (probably from the overheating pin mating to it).  This is the contact that mates to the anti-spark contact on the wing.

## Root Cause

1. 511 wing was damaged, in engineering for troubleshooting, and should not have been flown or delivered to the customer. See https://jenaero.atlassian.net/browse/ENG-2181. The findings were reported in JIRA, but wing was not red tagged. 511 RMA was not updated to indicate connector damage.

## Comments (4)

### Cameron Chapman, 2023-08-09

Email chain:
Sam – In the course of investigating 511, we did find connector damage and were working on root cause (probably similar to 516, but not certain). It’s in the ticket (which is not super-helpful or immediately obvious) – we’ve opened a CAR with Marc to analyze and resolve, since that will be part of the formal response to TIQUILA.
 
In the immediate term, we’re red-tagging everything that’s an investigation/issue item so that it’s obvious to anyone who sees a part if it is down-checked. Working with Sean to ensure everything that comes in the door is red-tagged too. Also working on getting another color (orange or something cautionary) to use instead, so we aren’t mixing factory NCRs and customer/test/investigation issues.
 
~G
 
From: Sam Miller <smiller@edgeautonomy.io> 
Sent: Wednesday, August 9, 2023 9:36 AM
To: Greg Fryer <gfryer@edgeautonomy.io>; Cody Smisek <csmisek@edgeautonomy.io>; John Clark <jclark@edgeautonomy.io>; Dave Grosher <Dgrosher@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Cc: Allen Gardner <agardner@edgeautonomy.io>
Subject: RE: VXE511 Aborted Launch at 2ft, VTOL ESCs stuck in initialization loop
 
Greg,
 
I do not believe that the statement: “Center Wing 511 was known-bad and not released for flight” is true.  It was my impression that 516’s center panel had the issue, not 511’s center panel.  511 had a chunk of glue floating around, which was removed. 
 
-Sam
 
 
 
 
From: Greg Fryer <gfryer@edgeautonomy.io> 
Sent: Wednesday, August 9, 2023 9:23 AM
To: Sam Miller <smiller@edgeautonomy.io>; Cody Smisek <csmisek@edgeautonomy.io>; John Clark <jclark@edgeautonomy.io>; Dave Grosher <Dgrosher@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Cc: Allen Gardner <agardner@edgeautonomy.io>
Subject: RE: VXE511 Aborted Launch at 2ft, VTOL ESCs stuck in initialization loop
 
I’ve spoken to Carson. Unfortunately since he already cleaned out the solder blob and tested, we can’t re-measure to get full details, but short answer to the current incident:
 
Center Wing 511 was known-bad and not released for flight, it was the wing in play on the ticket I linked below, and was actively being investigated. So root cause of the latest incident was using a known bad wing.
 
From Carson: The root of the original incident could be the bent pins, resulting in only partial mating, generating far more heat than normal, which both melted solder and resulted in the voltage drop and non-flight.
 
We’ll do what we can to isolate out the original root cause, and then corrective action to go with it – but we can stop chasing the data on yesterday’s incident. (John, Dave)

~Greg
 
From: Sam Miller <smiller@edgeautonomy.io> 
Sent: Wednesday, August 9, 2023 9:10 AM
To: Greg Fryer <gfryer@edgeautonomy.io>; Cody Smisek <csmisek@edgeautonomy.io>; John Clark <jclark@edgeautonomy.io>; Dave Grosher <Dgrosher@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Cc: Allen Gardner <agardner@edgeautonomy.io>
Subject: RE: VXE511 Aborted Launch at 2ft, VTOL ESCs stuck in initialization loop
 
This battery is currently under full load discharge test with Ben Norris. 
 
Carson removed the solder blob and hover-tested the center panel at 75% power for 60 seconds without issue. He noted that the pins are slightly canted, not parallel, which could result in a lower contact area when engaged.  After this PMA-263 meeting, I’d like to meet with Cameron and Desiray to discuss if we should replace the center panel power harness as a precaution. 
 
Thanks,
Sam
 
From: Greg Fryer <gfryer@edgeautonomy.io> 
Sent: Wednesday, August 9, 2023 8:57 AM
To: Cody Smisek <csmisek@edgeautonomy.io>; John Clark <jclark@edgeautonomy.io>; Dave Grosher <Dgrosher@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Cc: Allen Gardner <agardner@edgeautonomy.io>
Subject: RE: VXE511 Aborted Launch at 2ft, VTOL ESCs stuck in initialization loop
 
I’ll pull us together this AM.
 
Could we potentially have an HLB issue, or an HLB data-reading issue (in the battery or in the SW)? Tail 516 incident (https://jenaero.atlassian.net/browse/VIT2-322) includes:
 
“VTOL Control Window indicated VTOL launch not OK and the HLB voltage was fluctuating 7-27”
 
~Greg
 
 
 
From: Cody Smisek <csmisek@edgeautonomy.io> 
Sent: Wednesday, August 9, 2023 8:21 AM
To: John Clark <jclark@edgeautonomy.io>; Dave Grosher <Dgrosher@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Cc: Greg Fryer <gfryer@edgeautonomy.io>; Allen Gardner <agardner@edgeautonomy.io>
Subject: Re: VXE511 Aborted Launch at 2ft, VTOL ESCs stuck in initialization loop
 
All
 
Just providing data. HLB 2-1803, which I assume is the one currently sitting in the building, should have been set aside earlier in the day. Can't recall if this CW was the one used in an initial problem or not. But we had a low voltage issue reporting from GCS SW when this HLB was installed during earlier attempted flight. Battery checker showed appropriate voltage.
 
Cody 
From: John Clark <jclark@edgeautonomy.io>
Sent: Wednesday, August 9, 2023 7:51 AM
To: Dave Grosher <Dgrosher@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Cc: Cody Smisek <csmisek@edgeautonomy.io>; Greg Fryer <gfryer@edgeautonomy.io>; Allen Gardner <agardner@edgeautonomy.io>
Subject: RE: VXE511 Aborted Launch at 2ft, VTOL ESCs stuck in initialization loop
 
Dave, messages are originating from here in ApmParser.cpp line 2924 I’ll review the VTOL data now.
 
if(m_ttakeoff)
{
                m_expalt = vtolclimb * (float) (GetTime() - m_ttakeoff) * 0.001f;
                               
                if((m_expalt - (float)gApmState.RelAlt) > vtolalterr)
                {
                                if(gApVtolStatus.ApVtolState <= APVTOL_CLIMB)              // in climb phase
                                {
                                                if(rtlcount)
                                                {
                                                                AddMessage("climb fault, RTL");
                                                                if(rtlcount == 1)
                                                                                g_XCommControl.DebugMsg("Climb abort, low climb rate", 4);
                                                                CommandReturnToLaunch();                    
                                                                rtlcount--;
                                                }
                                }
                                else
                                {
                                                m_ttakeoff = 0;
                                }
                }
}
 
From: John Clark <jclark@edgeautonomy.io> 
Sent: Wednesday, August 9, 2023 7:45 AM
To: Dave Grosher <Dgrosher@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Cc: Cody Smisek <csmisek@edgeautonomy.io>; Greg Fryer <gfryer@edgeautonomy.io>; Allen Gardner <agardner@edgeautonomy.io>
Subject: RE: VXE511 Aborted Launch at 2ft, VTOL ESCs stuck in initialization loop
 
These messages are from the log and seem to back a lift system fault. I think the highlight is the fist indication of failure. I’ll follow up on that.
--jc
 
[00:06:44.576 3423.576] climb fault, RTL
[00:06:44.577 3423.577] DebugMsg RTL
[00:06:44.578 3423.578] aux servo cycle start
[00:06:44.579 3423.580] trillium park cmd sent
[00:06:44.678 3423.678] climb fault, RTL
[00:06:44.679 3423.680] DebugMsg RTL
[00:06:44.751 3423.751] ap dbg: lch timeout: 4
[00:06:44.781 3423.781] climb fault, RTL
[00:06:44.782 3423.782] DebugMsg RTL
[00:06:44.883 3423.883] climb fault, RTL
[00:06:44.891 3423.891] DebugMsg RTL
[00:06:44.993 3423.993] climb fault, RTL
[00:06:45.000 3424.000] DebugMsg Climb abort, low climb rate
[00:06:45.001 3424.002] DebugMsg RTL
 
[00:06:50.679 3429.679] MESSAGE_VTOL 2  6
[00:06:50.720 3429.721] DebugMsg Climb abort, lift system fault
[00:06:50.723 3429.724] VT pwr fault: min pwr  0x21
[00:06:50.799 3429.799] MESSAGE_VTOL 2  6
[00:06:50.875 3429.875] MESSAGE_VTOL 1  1
[00:06:50.878 3429.878] MESSAGE_VTOL 2  6
[00:06:50.974 3429.974] MESSAGE_VTOL 1  1
[00:06:50.977 3429.977] MESSAGE_VTOL 2  6
[00:06:51.075 3430.075] MESSAGE_VTOL 1  1
[00:06:51.076 3430.076] MESSAGE_VTOL 2  6
[00:06:51.148 3430.148] DebugMsg Climb abort, lift system fault
[00:06:51.149 3430.149] VT pwr fault: min pwr diff thr  0x31
[00:06:51.174 3430.174] MESSAGE_VTOL 1  1
[00:06:51.175 3430.175] MESSAGE_VTOL 2  6
[00:06:51.276 3430.276] MESSAGE_VTOL 1  1
[00:06:51.277 3430.277] MESSAGE_VTOL 2  6
[00:06:51.375 3430.375] MESSAGE_VTOL 1  1
[00:06:51.378 3430.378] MESSAGE_VTOL 2  6
[00:06:51.475 3430.475] MESSAGE_VTOL 1  1
[00:06:51.476 3430.476] MESSAGE_VTOL 2  6
[00:06:51.552 3430.552] DebugMsg Climb abort, lift system fault
[00:06:51.553 3430.554] VT pwr fault: min pwr  0x21
[00:06:51.576 3430.576] MESSAGE_VTOL 1  1
[00:06:51.577 3430.577] MESSAGE_VTOL 2  6
 
From: Dave Grosher <Dgrosher@edgeautonomy.io> 
Sent: Wednesday, August 9, 2023 7:36 AM
To: Sam Miller <smiller@edgeautonomy.io>; John Clark <jclark@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Cc: Cody Smisek <csmisek@edgeautonomy.io>; Greg Fryer <gfryer@edgeautonomy.io>; Allen Gardner <agardner@edgeautonomy.io>
Subject: Re: VXE511 Aborted Launch at 2ft, VTOL ESCs stuck in initialization loop
 
 
 
Hi All, 
 
Some notes from looking at the data. I can produce some plots to support these notes when I get a bit of time.  I'm responding via email given the customer has access to the vehicle incident in Jira. 
 
Files:
VTL00087.csv - incident is at  ~3405 CPU Time
XCL00081.csv - incident is at ~3400 CPU Time
 
Observations in XCOMM data:
- APAGL is corrected preflight

 
Observations in VTOL Event Log:
- Landing Jerk (16.06.41.664) was detected prior to Launch abort (16.06.51).

 
Observations in VTOL Data:
- IDLE > TAKEOFF (3405) > DESCENT (3428)

- It took 23 seconds to abort per the vtol host state, very different from the movie but in line with the event log.

- Throttle cmds (FL CW, FR CCW, RR CW, RL CCW) ramp up just after 3414. At 3416.36 throttle commands all start oscillating between very high values and zero. Oscillations become less frequent after 3418 but occur less frequently until 3432.

- The throttle commands are from the fastServo.c. Perhaps there is logic setting it to zero given the battery voltage?

- The boom currents ramp up at 3414.5 and then start to decline at 3416.25. There is no indication of the abrubt drops in current tracking the throttle commands. Perhaps there is some protection logic in the ESC?
- Drop in lift battery voltage to < 18V, steepest drop starts at 3416.3
- At 3416.3 there is a switch to GPS AGL and Baro AGL is invalid
- At 3416.1 the IMU qual bits start to toggle (bit positions versus documented positions don't seem to align.  Need to verify bit positions)
- There is a large jump in ltp position at 3410, about 250 ft.
- Roll seems to have moved about -5 degrees prior to throttle commands spinning up. Pitch appears to shift abrubtly from 3415.5 - 3417. The crash appears to be at 3417.
- The Az control loop looks well behaved. mxAz doesn't have any throttle spikes to zero.
- mxM1-4 show a steep decrease in throttle at 3416.7 but it does not go to zero.

 
 
Hypothesis:
- Zero throttle commands are possibly causing the ESC logic to enter safe mode. Need to understand the difference between the MxM* signals and FL/R RL/R throttle commands as the command dropping to 0 is only in the latter. Is there logic to set the throttle to 0 when the battery voltage drops? Note: the voltage drop is steady it is not oscillatory.

 
 Let me know if you have any questions. 
 
Dave
From: Sam Miller <smiller@edgeautonomy.io>
Sent: Tuesday, August 8, 2023 10:05 PM
To: Dave Grosher <Dgrosher@edgeautonomy.io>; John Clark <jclark@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Cc: Cody Smisek <csmisek@edgeautonomy.io>; Greg Fryer <gfryer@edgeautonomy.io>; Allen Gardner <agardner@edgeautonomy.io>
Subject: VXE511 Aborted Launch at 2ft, VTOL ESCs stuck in initialization loop
 
All,
During TIQUILA FAT at 5pm today, UK MOD Asset VXE511 experienced an abrupt aborted takeoff with all four motors cutting at ~6” above the stand. The vehicle fell back onto the stand, knocking it over and causing minor damage to the fuselage composites around the payload bay opening. In the video (IMG_1722.mov), the motors can be heard repeatedly resetting in a loop until the GCS operator issued a cut and safe command.  I’ve never heard the vehicle do this.  Please see the Jira ticket here for full synopsis and associated files: https://jenaero.atlassian.net/browse/VIT2-340?atlOrigin=eyJpIjoiZDkzOTBmY2I4NDI0NDQ3M2JmNTljOWZhNjFhNjdkNTkiLCJwIjoiaiJ9
I returned the center panel and hybrid lift battery to SLO for inspection and testing this evening. We need these inspected first thing in the morning, and the customer needs to know whether this aircraft is safe to return to flight ASAP.
Please let me know if you have any questions or need additional information. I know everyone is extremely busy hunting down 509 and 516’s issues as well, but I would appreciate you taking a look at this soonest. We must have at least two flying vehicles to complete FAT this week. 
Thank you in advance for your help!
-Sam

### Cameron Chapman, 2023-08-09

[embedded: Photo 2023-08-09 11_25_53.jpg]
HLB used in this flight was 2-1803.  The positive terminal looks like it is missing the ring around the socket, which could lead to higher contact resistance. The terminal also shows some solder near the top of the contact, which could be from the mating contact overheating. @Laszlo Juhasz

### Cameron Chapman, 2023-08-09

Current sense assembly was replaced on 511. It passed SCO flights according to @Carson Buckley he will upload FDR to Condor/FlightOps when they return from the field today.

### Cameron Chapman, 2023-08-10

I moved https://jenaero.atlassian.net/browse/ENG-2193 to an internal issue, so this issue is now a duplicate. Closing.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Photo 2023-08-09 11_25_53.jpg | image | 1407 | 2023-08-09 | listed only |
