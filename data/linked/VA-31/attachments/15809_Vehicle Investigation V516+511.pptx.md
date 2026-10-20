# Vehicle Investigation V516+511.pptx

Attachment 15809, pptx, 22024 KB, added 2023-08-10 by Cameron Chapman.

## Slide 1

Investigation Report
https://jenaero.atlassian.net/browse/VIT2-322
V511/516
Author: John Clark
Aug 3 2023
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

## Slide 4

Summary
Reporter: Daniel Loyd
Severity:
Investigation Plan
Investigation Status
Edge Autonomy Proprietary Information
Engineering was requested to review flights and to provide Lift Ibatt data to Laszlo Juhasz.
Review flight data for 511 fuselage and 511+516 center wings for the last flight and ones before that. Inspect for overcurrent conditions. -John reviewed plots. No obvious anomalies. Will link ppt in description.

## Slide 5

Center Wing
Data from the VTOL Log
Review VTOL data log throttles.
Investigation Plan
Results
Edge Autonomy Proprietary Information
[chart: VTOL00016]

Speaker notes:
SW release workflow, simulated flight hours prior to flight test, phased implementation, GNSS denied testing, regression testing refinement.

## Slide 6

Center Wing
Data from the VTOL Log
Review VTOL data log throttles.
Investigation Plan
Results
Edge Autonomy Proprietary Information
[chart: VTOL0018]

Speaker notes:
SW release workflow, simulated flight hours prior to flight test, phased implementation, GNSS denied testing, regression testing refinement.

## Slide 7

[chart: VTOL00026]
516 Center Wing
Data from the VTOL Log
Edge Autonomy Proprietary Information
[chart: VTOL00026]

Speaker notes:
SW release workflow, simulated flight hours prior to flight test, phased implementation, GNSS denied testing, regression testing refinement.

## Slide 8

516 Center Wing
Data from the VTOL Log
Edge Autonomy Proprietary Information
[chart: VTOL00029]
[chart: VTOL00029]

Speaker notes:
SW release workflow, simulated flight hours prior to flight test, phased implementation, GNSS denied testing, regression testing refinement.

## Slide 9

BACKUP
[picture]
[picture]
