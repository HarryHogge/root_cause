# VXE 401 Centerwing failing to report proper VTOL battery state.pptx

Attachment 35079, pptx, 3325 KB, added 2025-12-01 by Jackson Riley Curvin.

## Slide 1

Investigation Report
VXEP - 946
V401
Author: A. Garcia 
February 28, 2025
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

Investigation Overview – Status: INVESTIGATING – D4 [Updated 2025-02-28 A Garcia]
Edge Autonomy Proprietary Information
CW failing to report proper VTOL battery state 
VXEP - 946
V401
HLB Quality
Discontinuity across power harness
Grounding Issues
AS150 measurement specifications
Vref suggests that something within the ground line is broken
[picture]
[picture]
[picture]
Investigated but inconclusive
Not the root cause or contributing factor
Root cause or contributing factor
Next Steps: 
Replace Dual Current Sense Board and test full functionality 
Return to RMA once replacement has been done
Conclusion & Corrective Action:
Replace the Dual Current Sense Assembly (PN: 107-102264) on V401
2. Move where the wire is spliced on from the main AS150 connector to the Lift Boom ground banana connector (on the same harness)
This would put significantly less strain on the wire and is located closer to the CSB
3. Connor mentioned there is a process in the E shop currently for the branch cable where the wires are done in a method to provide more strain protection
Evidence To Disprove
Evidence To Support
Evidence To Prove
[picture]
[picture]
[picture]

## Slide 4

Incident Summary [Updated 2025-02-28 A Garcia]
Reporter: 
Severity:
Edge Autonomy Proprietary Information
Operator is unable to get through pre-flight check because the VTOL battery shows low. The center wing also does not give a proper voltage of the battery

## Slide 5

CONCLUSION DETAILS [Updated 2025-02-28 A Garcia]
Reporter: 
Severity: Near Miss
Corrective Actions
Edge Autonomy Proprietary Information
The 26 AWG wire in the current sensor harness was disconnected at an unspecified point along the line. Wire strain caused the ground wire in the Dual Current Sense Assembly (PN: 107-102264) to break. As a result, if the HLB was connected without the data cable, the battery was not properly grounded.
Replace the Dual Current Sense Assembly (PN: 107-102264) on V401
2. Move where the wire is spliced on from the main AS150 connector to the Lift Boom ground banana connector (on the same harness)
This would put significantly less strain on the wire and is located closer to the CSB
3. Connor mentioned there is a process in the E shop currently for the branch cable where the wires are done in a method to provide more strain protection

## Slide 6

ANALYSIS: Grounding Issue [Updated 2025-02-28 A Garcia]
Review VTOL logs 
Plot Vref against Vbatt – Vref should be the inverse of Vbatt and within in the negative range
Vref is used to calculate the value of Vbatt 
If Vref looks abnormal there may be an issue within the wiring 
Continuity test current sensing circuitry
Investigation Plan
Results
Edge Autonomy Proprietary Information
The oscillations in the Vref (blue trace) appear to be high-frequency, intermittent disturbances. This behavior suggests that the signal is experiencing:
Grounding Issues – The sharp transitions and erratic nature of Vref could be due to poor grounding, a noisy power supply, or switching transients from nearby circuits.
The ground line highlighted in red shows no continuity explaining the intermittent disturbance
[picture]
[picture]
V401 Vref Profile
Typical Vref Profile
[picture]

## Slide 7

ANALYSIS: Unmated HLB Connector [Updated 2025-02-28 A Garcia]
Measure the AS150 dimensions and compare them against accepted criteria 
Measure the resistance of the anti-spark 
If the anti-spark measures more than 6 ohm it may have been damaged by overheating which is a symptom of a bad matting
Intentionally make a bad connection on the CW power harness and check on the webpage is battery voltage is read
Investigation Plan
Results
Edge Autonomy Proprietary Information
| Contact ​ | Accepted Measurement (in)​ | Actual Measurment (in) ​ | Measurement Delta (in)​ |
| Anti-Spark AS150​ | 0.275​ | 0.275 | 0 |
| Non-Anti-Spark AS150​ | 0.28​ | 0.2755 | 0.0045 |
Anti-spark measured at 6.2ohm which is within the accepted criteria 
AS150 measurements are within accepted measurements 
Unlikely the root cause is due to out of specification AS150 measurements

## Slide 8

BACKUP
[picture]
[picture]
