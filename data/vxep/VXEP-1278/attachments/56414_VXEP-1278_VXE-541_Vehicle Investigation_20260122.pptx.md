# VXEP-1278_VXE-541_Vehicle Investigation_20260122.pptx

Attachment 56414, pptx, 139082 KB, added 2026-05-12 by Drew Hildreth.

## Slide 1

Title: VXEP 1278 Investigation Report
Vehicle: VXE-541
22 January 2026
[picture]
[picture]

## Slide 2

VXE30 - Issue Resolution Process
D7 – Prevention
D8 - Done
Yes
Add to Lessons
Learned
Document
Debrief Customers
Closed
With
UFRs
UFR
Added?
No
Send UFR Description
To Customer
Closed
User
Creates Incident Report (IR)
User Assembles After Action Report (AAR)
EA Assembles Incident Response Team (IRT)
User Secures Aircraft
User Packages Aircraft and Ships to EA Depot
EA Receives Aircraft
IRT reviews IR and AAR
IRT Inspects Aircraft
IRT requests additional info from customer
(phone, email, zoom, etc.)
IRT releases first-look report (FRP)
D1 – Form Team
D2 – Define The Problem
D3
Investigate Root Cause
D4 – Find Root Cause
D5
Verify Root Cause
RCIT Releases Root Cause Report (RCR)
EA Assembles Root Cause Investigation Team (RCIT)
Alert Users
IRT creates Airworthiness Safety Alert (ASA)
IRT publishes ASA
Affected customers are alerted to ASA
Is ASA Required?
Yes
D3 – Interim Containment
D4
No
D4
Is Advisory Notice Required?
IRT creates
Advisory Notice
IRT publishes Advisory Notice
Alert Users
Via ICR
IRT creates list of aircraft tail-numbers affected by the incidents
IRT creates list of affected customers
IRT creates Interim Containment Report (ICR)
Yes
No
EA Assembles Corrective Action Team (CAT)
CAT Creates List of Corrective Actions
Funded
Fixes
Unfunded
Fixes
Add to Prioritized UFR List
Estimate Cost & Schedule
D6
D5 – Define Corrective Action
D8
Brief Customer on UFR
Are Fixes Required?
CAT Creates Corrective Action Plan and Releases Corrective Action Report (CAR)
Yes
No
No
Yes
Alert Users
Funding Available to Fix Issue
Software
Issue
Hardware
Issue
Training
Issue
Maint
Issue
QA
Issue
Fix Code
Bench
Test
HIL Test
Flight
Test
Release
Software
Upgrade
Create Service Bulletin
Alert Users
Publish Service Bulletin & SW
Prelim
Design
Final
Design
Build
Prototype
Bench Test
Prototype
Flight Test
Prototype
Create Service Bulletin
Ship to Customers
Publish
Service
Bulletin
Production
Design
Production SCM Plan
Build
Kits
Identify Training Gap
Update Training Curriculum
Update User Manual
Alert Users
Identify MTBF Gaps
Update Sparing Plan
Update 
Mx
Manual
Create Service Bulletin
Release 
Updated
Mx
Manual
Publish
Service
Bulletin
Create Correction Action Plan (CAP) for SCM and Production
Implement CAP in SCM and Production
D6 – Implement and Verify Corrective Action
Alert Users
Create HIL/Flight Test Cards
Update Regression Tests for HIL and Flight Test
D7
Alert User of Preliminary Assessment
(known causes / mitigations)
Create
Operational Supplement
Publish Operational
Supplement
Alert Users
Version: Feb 2025

Speaker notes:
Current updated version as of 8/2024

## Slide 3

Operator Report
Who:	SORD, ATOC, 4BN, 10SFG(A)
What:	Stalker VXE30 (Tail #541) failed to perform proper landing sequence actions, resulting in the aircraft crashing into the 	ground.
Where:	Agony North, Fort Carson, CO 80911
When:	06 December 2024 at 1200L
Why:	During landing sequence, tail #541 failed to transition to the Vertical Take Off and Landing (VTOL) motors. The aircraft 	instead, continued to reduce its airspeed causing it to glide until it struck the ground. 
Note: 	Customer did not report incident until beginning of May 2025

## Slide 4

Executive Summary
Problem Statement​
Upon transition to VTOL landing the vehicle did not function properly and crash landed.  Post landing transition what part of the vehicle’s operation failed to perform and why?
​
Probable Sequence of Events 
The HLB (hybrid lift battery) connector from the center-wing to HLB was not fully seated pre-flight.  Upon transitioning to landing the logs show signs of a marginal connection throughout, with the VTOL motors responding briefly for about 30 sec.(2130-2160) then unable to respond for the remainder of the flight less a brief 3sec.(3893-3896) period right before crashing. 

Root Cause ​
The HLB battery connection was not fully connected due to a previously identified dimensional tolerance issue or not enough force was applied when seating the connector by the operator.

Ruled out Leading Causes​
GPS and related sensor data were verified as within specification. 
​
Corrective Actions​
Rely on existing corrective actions implemented through pre-sorting quality inspections at the sub-assembly level.  Provide a revision to Advisory Notice -25-006 (main battery connection notice), adding HLB to the context.

## Slide 5

Investigation Overview
Edge Autonomy Proprietary Information
Failed to perform proper landing
2.1 HLB(hybrid lift battery) Connection not Fully Mated
[picture]
[picture]
[picture]
Investigated but inconclusive
Not the root cause or contributing factor
Root cause or contributing factor
[picture]
1.1 GPS
Failure
[picture]
Legend

## Slide 6

1.1 GPS Failure - Attitude, Airspeed, and GPS Quality - Good
X-Axis is VTOL CPU seconds for all.
Baro AGL (bottom plot) for reference again, descent starts at ~3,863 seconds on CPU time axis

Euler angles are relatively smooth, suggesting normal controllability up until the transition
GPS satellite count stays between 20-22 during the entire landing process (which is sufficient)
GPS link quality, described by a parameter CNo, stays above 40 throughout the entire landing process as well reaffirming our thought that GPS is likely not related
Airspeed appears consistent with the altitude and throttle plots
[picture]
Edge Autonomy Proprietary Information

## Slide 7

2.1 HLB Not Fully Mated – Low Power Consumed by the Lift System
Lift System consumes very little power during transition to VTOL
Edge Autonomy Proprietary Information
During landing sequence, CW 541 failed to transition to the Vertical Take Off and Landing (VTOL). Vehicle continued reducing airspeed until it struck the ground.  VTOL flight data records very little power consumed by the lift system during transition until impact.
[picture]

## Slide 8

2.1 HLB Not Fully Mated – Low Power Consumed by the Lift System
X-Axis is VTOL CPU seconds
Lift Throttles start at ~200’ AGL for landing.
Throttles are heavily divergent suggesting the autopilot is attempting to correct for instability
Power consumption is very low indicating motors are not consuming power
Several HLB voltage dips suggest battery connectivity issues
[picture]
Note: Low Current levels ~5 Amps vs typical ~180 Amps
Note: Voltage frequently dips to ~10V
Note: Divergent throttles suggest instability
Edge Autonomy Proprietary Information

## Slide 9

[picture]
2.1 HLB Not Fully Mated – Voltage Drops Out
Connection appears marginal 2x
[picture]
[picture]
[picture]
[picture]
Voltage Dips to 1.26 VDC
Edge Autonomy Proprietary Information

## Slide 10

2.1 HLB Not Fully Mated – Logic Drops Out
State Machine Logic Drops to Zero
[chart: No Load HLB Voltage vs Fused State of Charge & State Machine Logic]
State Machine Logic Erratic (2128-3000)
No Load Voltage Drops to 8VDC approximately
Edge Autonomy Proprietary Information

## Slide 11

[chart: Linear Acceleration vs HLB Voltage]
2.1 HLB Not Fully Mated – Minor Acceleration May Move Contact Slightly
Some vehicle movement occurs before connection worsens
Some correlation with acceleration to connection instability
Vehicle to ground impact

## Slide 12

2.1 HLB Not Fully Mated – Motors Start Intermittently
Responded to throttle for about 30 sec.
VTOL motors unable to respond (current limited)
[chart: Throttle vs  Current]
Brief final start
Edge Autonomy Proprietary Information

## Slide 13

[chart: HLB Current vs Voltage]
[chart: Throttle vs HLB Current]
2.1 HLB Not Fully Mated – Motors are Unable to Start
Connection improves slightly motors start
Voltage drop possible reflecting anti-spark(5.6ohms):
25.459-20.976VDC =4.483V∆
1.18 -.76 = .42A∆*2
= 5.34 ohms
Motors are current limited which limits torque = no start across (3864-3892)
ESC trying to start sawtooth ramps
Current
Current
[picture]

## Slide 14

[picture]
3.1 Female Contacts out of Specification – HLB is at Customer Site, can’t be Tested
No solder seen above here
[picture]
Contact resistance measured 5.7 ohms approximately
Tested male side pins solid and hollow to HLB from center-wing.  Both had an external diameter of approximately 0.256 with variance in the angle, force and location measured.  While the connecting females on a spare HLB measured 0.275 to 0.276 with the same variation.  

Overall, it shows about 20 mils of positive displacement needed on the HLB side with its featured slotted finger female sockets.  This displacement is part of the manufacturer’s design and is not stated on the specification sheet.
[picture]
Advisory Notice 25-006 (excerpt)
Edge Autonomy Proprietary Information

## Slide 15

Corrective Actions – Currently Implemented
09/2024 Pull testing implemented. Post assembly check.
Assembly dates are before quality implemented dimensional sorting activities
[picture]
[picture]
[picture]
[picture]
Correction actions implemented 10/03/2024
Web Manuals - Reader
Perform revision to existing advisory notice -25-006
Edge Autonomy Proprietary Information
