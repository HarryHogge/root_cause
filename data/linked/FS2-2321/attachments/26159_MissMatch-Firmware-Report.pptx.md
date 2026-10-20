# MissMatch-Firmware-Report.pptx

Attachment 26159, pptx, 1161 KB, added 2025-02-10 by Jason Scherer.

## Slide 1

Investigation Report
VXE-629(501), VXE-572, VXE-573, VXE-574, VXE-594, VXE-688
Mismatched Firmware

February 2025
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
IRT creates Airworthiness Directive (AWD)
IRT publishes AWD
Affected customers are alerted to AWD
Is AWD Required?
Yes
D3 – Interim Containment
D4
No
D4
Is Safety Alert Required?
IRT creates
Safety Alert
IRT publishes Safety Alert
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

Summary
Edge Autonomy Proprietary Information
Edge Autonomy has received multiple vehicle incidents resulting from miss-matched and outdated firmware versions. 
Operating old or miss-matched software is not safe and not supported.

Three vehicles are missing firmware from last three releases. All vehicles are missing firmware from the last two releases. Every vehicle that has GCS logs shows miss-matched software. VXE-688 has miss-matched firmware as well.
6.1.2 – Sept 2023
Fixed Wing v6.05m, Xcomm v4.67, VTOL v1.53
6.2.9 – April 2024 (Airworthiness Directive (AD)_ Software Update_2024-03-18_A 1.pdf)
Fixed Wing v6.05o, Xcomm v4.68, VTOL v1.54
6.3.4 – Aug 2024 (Airworthiness Directive (AD) Software Update 2024-08-08_A.pdf)
Fixed Wing v6.05p, Xcomm v4.69V, VTOL v1.55

## Slide 4

Vehicle Incidents Summary
Summary of reported vehicle incidents
VXEP-732 (VXE-628 reconfigured to 501) - Crash on VTOL descent “AV made hard right turn in VTOL descent and crashed into ground.”
Not investigated due to outdated firmware

VXEP-605 (VXE-572) - Multiple un-commanded aborted launches
Issue addressed in firmware updates (6.2.9 & 6.3.4) 

VXEP-652 (VXE-573) – Cruise motor stopped during RTB, aircraft crashed
Aircraft descended (as commanded) while returning to PLZ resulting in controlled flight into terrain (CFIT).

VXEP-598 (VXE-574) – Aircraft made hard right turn from PLZ during VTOL landing
Not investigated due to outdated firmware

VXEP-651 (VXE-594) – Operator commanded go-to IP5 (incorrect landing sequence)
Operator commanded VTOL transition beyond vehicle VTOL landing capability
Issue prevention included in upcoming release

VXEP-611 (VXE-688) – On landing transitioned to VTOL, aircraft continues forward flight and crashes into a mountain
Not investigated due to outdated firmware

## Slide 5

Airworthiness Directive (AD)_ Software Update_2024-03-18_A 1
Edge Autonomy Proprietary Information
[picture]

## Slide 6

Airworthiness Directive (AD)_ Software Update_2024-03-18_A 1 - Changes
Edge Autonomy Proprietary Information
[picture]

## Slide 7

Airworthiness Directive (AD) Software Update 2024-08-08_A
Edge Autonomy Proprietary Information
[picture]

## Slide 8

Airworthiness Directive (AD) Software Update 2024-08-08_A - Changes
Edge Autonomy Proprietary Information
[picture]
[picture]

## Slide 9

BACKUP
[picture]
[picture]
