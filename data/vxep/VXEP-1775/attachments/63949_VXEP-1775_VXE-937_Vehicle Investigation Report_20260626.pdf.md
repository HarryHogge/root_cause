# VXEP-1775_VXE-937_Vehicle Investigation Report_20260626.pdf

Attachment 63949, pdf, 637 KB, added 2026-08-07 by Drew Hildreth.

## Page 1

1
Title: VXEP 1775 Vehicle Investigation Report
Vehicle: VXE -937
26 June 2026

## Page 2

2
Proprietary
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
Send UFR 
Description
To Customer
Closed
User
Creates 
Incident 
Report (IR)
User Assembles After Action Report 
(AAR)
EA Assembles Incident Response Team (IRT)
User Secures Aircraft
User Packages Aircraft 
and Ships to EA Depot
EA Receives Aircraft
IRT reviews IR and AAR
IRT Inspects Aircraft
IRT requests additional info from customer
(phone, email, zoom, etc.)
IRT releases first-look report (FRP)
D1 – Form Team
D2 – Define The Problem
D3
Investigate Root 
Cause
D4 – Find Root Cause
D5
Verify Root Cause
RCIT Releases Root 
Cause Report (RCR)
EA Assembles Root 
Cause Investigation 
Team (RCIT)
Alert Users
IRT creates Airworthiness 
Safety Alert (ASA)
IRT publishes ASA
Affected customers are 
alerted to ASA
Is ASA 
Required?Yes
D3 – Interim Containment
D4
No
D4
Is Advisory 
Notice Req
uired?
IRT creates
Advisory Notice
IRT publishes 
Advisory Notice
Alert Users
Via ICR
IRT creates list of aircraft tail-
numbers affected by the 
incidents
IRT creates list of affected 
customers
IRT creates Interim 
Containment Report (ICR)
Yes
No
EA Assembles Corrective Action Team (CAT)
CAT Creates List of Corrective Actions
Funded
Fixes
Unfunded
Fixes
Add to Prioritized 
UFR List
Estimate Cost & 
Schedule
D6
D5 – Define Corrective Action
D8
Brief Customer on 
UFR
Are Fixes 
Required?
CAT Creates Corrective Action Plan and 
Releases Corrective Action Report (CAR)
Yes No
No
Yes
Alert Users
Funding 
Available 
to Fix 
Issue
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
Create 
Service 
Bulletin
Alert Users
Publish 
Service 
Bulletin & 
SW
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
Create 
Service 
Bulletin
Ship to 
Customers
Publish
Service
Bulletin
Production
Design
Production 
SCM Plan
Build
Kits
Identify 
Training 
Gap
Update 
Training 
Curriculum
Update 
User 
Manual
Alert Users
Identify 
MTBF Gaps
Update 
Sparing Plan
Update 
Mx
Manual
Create 
Service 
Bulletin
Release 
Updated
Mx
Manual
Publish
Service
Bulletin
Create 
Correction 
Action Plan 
(CAP) for 
SCM and 
Production
Implement 
CAP in SCM 
and 
Production
D6 – Implement and Verify Corrective Action
Alert Users
Create 
HIL/Flight 
Test Cards
Update Regression Tests for HIL and Flight Test
D7
Alert User of Preliminary Assessment
(known causes / mitigations)
Create
Operational 
Supplement
Publish 
Operational
Supplement
Alert Users
Version: Feb 2025

## Page 3

© 2026 Redwire. Proprietary, Not for Public Release.
Investigation Overview
XComm Processor 
Reset
Radio issue would 
cause comms loss but 
not crash
Dramatic pitch down and 
loss of altitude observed 
in VTOL logs
Investigated but inconclusive
Not the root cause or contributing factor
Root cause or contributing factor
Next Steps : 
1. C o n t i n u eX C O M M  P r o c e s s o r R e s e t  i n v e s t i g a t i o n
2. I m p l e m e n t  c o r r e c t i v e  a c t i o n  f o r  a i r s p e e d  t r a c k i n g  
w h e n  X C O M M  P r o c e s s o r e v e n t s  o c c u r .
Conclusion & Corrective Action :
1. C ra s h  d u e  t o  XCO M M  P ro c e s s o r r e s e t
2. I nve s t i ga t i o n  i n t o  r e s o l v i n g  XCO M M  P ro c e s s o r r e s e t s  
co n t i n u e s
3. I n  t h e  n e a r  t e r m ,  ro b u s t n e s s  t o  a i rs p e e d  co n t ro l  d u r i n g  
XCO M M  P ro c e s s o r e ve n t s  i s  b e i n g  i m p l e m e n t e d  a s  a  
co r r e c t i ve  a c t i o n
Evidence To 
Disprove
Evidence To 
Support
Evidence To 
Prove
Radio Issue
No Evidence of Radio 
Issue
Crash During Fixed -
Wing Flight

## Page 4

© 2026 Redwire. Proprietary, Not for Public Release.
Executive Summary
Problem Statement
Operators noticed no anomalies during the first hour of flight, after the first hour they lost link for approximately 15 to 20 seconds and 
after link was reestablished the aircraft icon did not update so the operators suspected the aircraft had crashed.
Sequence of Events 
The XCOMM firmware hit a critical exception it halted immediately and saved diagnostic data. It disabled interrupts and got stuck in an 
infinite loop with no ability to recover. After about 8 seconds, the XCOMM Processor Reset.
Root Cause 
Mishap due to XCOMM Processor Reset causing stale fixed wing data. The fixed wing autopilot was no longer receiving criticaldata 
such as airspeed and altitude resulting in the aircraft pitching down to gain airspeed but due to the reset the data did not refresh.
Ruled out Leading Causes
Silvus Radio issues as well as Lost Comm Logic were ruled out during this investigation 
Corrective Actions
In the near term, robustness to airspeed control during WDT events is being implemented as a corrective action

## Page 5

© 2026 Redwire. Proprietary, Not for Public Release.
Timeline
Reporter: 
Severity: Near Miss
09:14:29: launch
10:11:33: xcomm logs cease
10:11:40: xcomm shows crash 
restart dump
10:11:54: approximate time of 
impact
~57 minutes after launch which 
lines up with VTOL plots of takeoff 
and the incident.
