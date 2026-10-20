# Vehicle Investigation V450.pptx

Attachment 15569, pptx, 3453 KB, added 2023-07-26 by John Clark.

## Slide 1

Investigation Report
https://jenaero.atlassian.net/browse/VIT2-327
V450
Author: John Clark
July, 24 2023
[picture]
[picture]

## Slide 2

VXE30 - Issue Resolution Process
User
Creates Incidence Report (IR)
User Assembles After Action Report (AAR)
EA Assembles Incidence Response Team (IRT)
User Secures Aircraft
User Packages Aircraft and Ships to EA Depot
EA Receives Aircraft
IRT reviews IR and AAR
IRT Inspects Aircraft
IRT requests additional info from customer
(phone, email, zoom, etc.)
IRT releases first-look report (FRP)
IRT creates list of aircraft tail-numbers affected by the incidents
IRT creates list of affected customers
IRT creates Interim Containment Report (ICR)
IRT creates Airworthiness Directive (AWD)
IRT publishes AWD
Affected customers are alerted to AWD
Is AWD Required
Yes
EA Assembles Root Cause Investigation Team (RCIT)
Investigate Root Cause
RCIT Releases Root Cause Report (RCR)
EA Assembles Corrective Action Team (CAT)
CAT Creates List of Corrective Actions
Funded
Fixes
Unfunded
Fixes
Software
Issue
Add to Prioritized UFR List
Estimate Cost & Schedule
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
Publish Service Bulletin and SW
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
Create
Operational Supplement
Update Training Curriculum
Update User Manual
Alert Users
Identify MTBF Gaps
Update Sparing Plan
Update Maint
Manual
Create Service Bulletin
Release 
Updated
Maint
Manual
Publish
Service
Bulletin
D6
D7
Create Correction Action Plan (CAP) for SCM and Production
Implement CAP in SCM and Production
Add to Lessons
Learned
Document
D1 – Form Team
D3 – Interim Containment
D4 – Find Root Cause
D5 – Define Corrective Action
D6 – Implement and Verify Corrective Action
D7 – Prevention
D8 - Done
D2 – Define The Problem
D5
D3
D8
D4
Debrief Customers
Closed
With
UFRs
UFR
Added?
No
Yes
Send UFR Description
To Customer
Closed
Alert Users
Create and Release Airworthiness Directive (AWR) If Required
Publish Operational
Supplement
Verify Root Cause
Brief Customer on UFR
Create HIL/Flight Test Cards
Update Regression Tests for HIL and Flight Test
Are Fixes Required?
CAT Creates Corrective Action Plan and Releases Corrective Action Report (CAR)
Yes
No
D4
Is Safety Alert Required
IRT creates
Safety Alert
IRT publishes Safety Alert
Funding Available to Fix Issue
No
No
Yes
Note: This Process does not have a way to handle issues with inconclusive results from an investigation

## Slide 3

Investigation Overview
Edge Autonomy Proprietary Information
Right Front Motor Did not Start on transition to VTOL Mode in Landing

v450
Configuration Issue
Details
Details
Details
Cause 1
Cause 4
Cause 5
ESC 2 (Right Front) Failed
On Landing
Details
Details
Details
Details
Details
Details
Details
Details
[picture]
[picture]
[picture]
Investigated but inconclusive
Not the root cause or contributing factor
Root cause or contributing factor
Next Steps:
[picture]

## Slide 4

Summary
Reporter: Daniel Loyd
Severity: Aircraft Destroyed
Motor sounds like it was damaged before this flight. “During the LW the ground crew indicated that the right front lift motor sounded different during the spin-up checks.”
In the video, it looks like the front right motor does not activate during attempted transition to descent. 
ESC feedback could have prevented this. Planned for next ESC generation. Linked to that project. 
Data review findings.
Investigation Plan
Investigation Status
Edge Autonomy Proprietary Information
Aircraft was participating in operator training at Camp Lejeune NC. It was in the fuel cell configuration with a Trillium HD55 payload. This was the second flight on this day. During the LW the ground crew indicated that the right front lift motor sounded different during the spin-up checks. The check was repeated several times and determined to be fine. The launch was uneventful. Per the flight profile, at around twenty minutes into flight the aircraft was commanded to RTB. The aircraft transitioned to vertical flight and then continued to drift past the programmed LZ toward the south. Attempts to nudge the aircraft back to the LZ produced no effect. The aircraft was placed in manual nudge which also produced no effect. At some point the aircraft dropped suddenly to the ground.
Inspect AP for damage. 
Perform input resistance, and PWM channels compare to normal. 
Open ESC lid, inspect for damage/burning smell. 
Perform input resistance, motor resistance, etc. measurement and compare to normal. 
Inspect all hardware, connections
Test ESC assy, trace signals compare
Plug AP in and see if PWM signals are generated using motor tester. 
Compare expected vs recorded boom power

## Slide 5

VTOL Throttles Normal at Launch
Data from the VTOL Log shows normal Throttle at Launch
Review VTOL data log throttles.
Investigation Plan
Results
Edge Autonomy Proprietary Information
[picture]

Speaker notes:
SW release workflow, simulated flight hours prior to flight test, phased implementation, GNSS denied testing, regression testing refinement.

## Slide 6

VTOL Throttles Abnormal at Landing (Throttle at Full on Failed Motor all Others Attenuated)
Data from the VTOL Log shows abnormal Throttle at Landing
Review VTOL data log throttles.
Investigation Plan
Results
Edge Autonomy Proprietary Information
[picture]
Front Right (Failed) Motor at 
Maximum Throttle in VTOL
Low or no Throttle on Remaining Motors to compensate for Front Right
[picture]

Speaker notes:
SW release workflow, simulated flight hours prior to flight test, phased implementation, GNSS denied testing, regression testing refinement.

## Slide 7

VTOL Currents Normal at Launch
Data from the VTOL Log shows normal Current at Launch
Review VTOL data log current.
Investigation Plan
Results
Edge Autonomy Proprietary Information
[picture]

Speaker notes:
SW release workflow, simulated flight hours prior to flight test, phased implementation, GNSS denied testing, regression testing refinement.

## Slide 8

VTOL Currents Critically Low at Landing
Data from the VTOL Log shows Current critically low in Landing
Review VTOL data log current.
Investigation Plan
Results
Edge Autonomy Proprietary Information
[picture]
Critically Low Current

Speaker notes:
SW release workflow, simulated flight hours prior to flight test, phased implementation, GNSS denied testing, regression testing refinement.

## Slide 9

BACKUP
[picture]
[picture]
