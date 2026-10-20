# Vehicle Investigation Report VXEP-102 (a4ac957a-11e6-4f51-8ce6-645612679be6).pptx

Attachment 16814, pptx, 4145 KB, added 2023-09-29 by Jason Scherer.

## Slide 1

Investigation Report
VXEP-102
V380
Author: Jason Scherer
Sep 29, 2023
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

Investigation Overview – Status: Resolved - [Updated 2023-9-29]
Edge Autonomy Proprietary Information
Launch abort VXEP-102
v380
VTOL AP Log 
Analysis
Bad GPS?
Bad LRF?
[picture]
[picture]
[picture]
Investigated but inconclusive
Not the root cause or contributing factor
Root cause or contributing factor
LRF data is
Not useable at altitude.
This is normal and expected
Next Steps: 
Review Investigation Report
Conclusion & Corrective Action:
The VTOL launch was successful. During the ascent to the commanded altitude, the AC experienced both LRF and GPS outages. The LRF outage is normal and will not cause an RTL. Once the GPS SNR value dropped below 40 the AC initiated automatic RTL and began descending.
GPS improvements are currently in development
JScherer
Log indicates
RTL Due to
LRF/GPS sensors
JScherer
JScherer
[picture]
[picture]
JScherer
[picture]
GPS Signal Drops at time of RTL
GPS Status Byte (0x2E) indicates bad SNR. SNR at RTL is 36. RTL threshold is 40, so this caused the RTL
JScherer

## Slide 4

Summary [Updated 2023-09-29 JScherer]
Reporter: Jason Scherer
Severity: 3 – Degraded Performance – With Workaround
AC logs indicate GPS and LRF faults
Edge Autonomy Proprietary Information
Aircraft 380 aborted first launch approximately 30 seconds after liftoff and switched to RTL mode. This occurred due to degradation in GPS signal quality. RPIC aborted launch and safely landed the AC. Edge Autonomy is currently working on GPS improvements which will reduce likelihood of GPS failure launch aborts like this.
GPS signal drops below 40 causing auto RTL
[picture]
[picture]

## Slide 5

BACKUP
[picture]
[picture]
