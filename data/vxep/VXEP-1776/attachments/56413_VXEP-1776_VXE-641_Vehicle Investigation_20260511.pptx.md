# VXEP-1776_VXE-641_Vehicle Investigation_20260511.pptx

Attachment 56413, pptx, 829 KB, added 2026-05-12 by Drew Hildreth.

## Slide 1

Title: VXEP-1776 Investigation Report
Vehicle: VXE-641
11 May 2026
[picture]
[picture]
Investigation Report

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
Who:     TIQUILA
What:    Aircraft crash during fixed-wing flight
Where:  Undisclosed
When:   March 15, 2026
Why:      Aircraft departed controlled flight and crashed into the ground during fixed-wing orbits.
Note:     Root cause and contributing factors on next page.

## Slide 4

Executive Summary
Problem Statement​
At 16:30, the detachment deployed. The mission was planned with a maximum operating height of 800ft AGL. The detachment was fully briefed, and all personnel were alert, well-rested. The aircraft, EAGLE VXE30 tail number 641, launched successfully and entered its designated orbit. At the time of the incident, the aircraft had been in flight for 1 hour and 7 minutes, with 2 hours and 30 minutes endurance remaining to complete the task. Weather conditions were within operational limits, with a steady wind speed of 22.2 knots from 118° SE, below the maximum allowable limit of 26 knots. The temperature was recorded at 21°C. 
At 19:02, while the aircraft was in its orbit at 800ft AGL, it was observed to bank excessively to the left. The aircraft then looked as if it rolled over, and it appeared to lose stability. The payload footage showed the aircraft rolling over completely, with the camera momentarily pointing upwards towards the sky. The footage then displayed the aircraft continuing to roll multiple times, indicating a loss of controlled flight. Simultaneously, the Ground Control Station (GCS) populated a GPS warning, which cleared after a few seconds. The pilot immediately issued a positive command to return the aircraft to its current orbit in an attempt to stabilize it. However, this action was unsuccessful, and the aircraft continued to lose altitude. Shortly after, the GCS displayed a red "loss of link" warning, indicating that communication with the aircraft had been lost. The detachment continued to monitor the situation closely. At approximately 300ft AGL, all telemetry and video feed from the aircraft had paused, and the detachment were unable to regain control. The aircrafts last known position was recorded, and the incident was promptly reported through the appropriate channels, including the chain of command and relevant authorities. 
Following the loss of the aircraft, the detachment initiated a search and recovery operation. The team proceeded to the aircrafts last known position and located the aircraft. Upon arrival, the team documented the scene by taking photographs of the aircraft and its surroundings. The area was immediately cordoned off to ensure safety, preserve evidence, and prevent unauthorized access. The detachment then moved back 400m from the site to maintain a safe distance while awaiting further instructions. 
Root Cause ​
Fixed-wing autopilot roll gyro suddenly developed a bias of approximately 20 deg/s.  This bias is too great for the estimator to converge out.
Ruled out Leading Causes​
Surface failure, structural failure, FWAP processor failure
Corrective Actions​
None.  The  FWAP gyro is a single point of failure. Injection of a bias this large is unrecoverable.

## Slide 5

Investigation Overview – Status: Closed – D8
Crash During Fixed-Wing Flight
FWAP Processor Failure
Surface Failure
No Evidence of Surface Failure
No evidence to support
Large gyro bias observed
FWAP Gyro Failure
Structural Failure
Autopilot appeared to be running/commanding surfaces
Attitude disagreement with VTOL autopilot
Task Lock
Roll fault message logged
[picture]
[picture]
[picture]
Investigated but inconclusive
Not the root cause or contributing factor
Root cause or contributing factor
FWAP Logs continued updating
Next Steps: 
None
Conclusion & Corrective Action:
FWAP Gyro Bias Increased Unexpectedly 
Failure of a flight critical sensor in a single-string system is unrecoverable
Evidence To Disprove
Evidence To Support
Evidence To Prove
[picture]
[picture]
[picture]
[picture]

## Slide 6

ANALYSIS: Logs consistent with unexpected fwap gyro bias
Comparison of VTOL and Fixed-wing data is consistent with fixed-wing gyro failure
FWAP log shows roll right
[picture]
[picture]
VTOL attitude estimate shows vehicle roll left which  matches operator reports
Large gyro bias observed in roll gyro.  FWAP gyro reads roll right
In lab testing, Attitude Heading Reference System (AHRS) can converge out about 5 deg/s of gyro bias.  In flight bias of ~20 deg/s was too large for AHRS estimate to remain accurate.

Speaker notes:
SW release workflow, simulated flight hours prior to flight test, phased implementation, GNSS denied testing, regression testing refinement.

## Slide 7

ANALYSIS: Fixed-wing and VTOL gyros appear to match at vehicle launch
Comparison of VTOL and Fixed-wing roll rate data during takeoff
[picture]
FWAP and VTOL gyros are synced during takeoff, indicating issue was not present when preflight and takeoff checks were performed.

Speaker notes:
SW release workflow, simulated flight hours prior to flight test, phased implementation, GNSS denied testing, regression testing refinement.

## Slide 8

Notes: Some other notes on AHRS performance
AHRS solutions are compared during various phases of flight
Question: Do the VTOL and FW IMU do comparative analysis in real time or was the mismatch/discrepancy highlighted from data in the log files?
Answer: The fixed-wing and VTOL solutions are compared only during preflight and the initial climb-out.  Disagreements during this phase block launch or in the case of climb-out would cause a launch abort.
Question: There are some alerts highlighted in the manuals, and where you mention “warn the operator” – Would those alerts (as detailed as examples in my previous email) have been observed? Or on the flipside, were any alerts expected? I fully appreciate that it all happened pretty quickly, but it reads like the AV didn’t have enough time to compute what was happening to be able to do anything apart from spiral down?
Question: Do we know why no alert was provided to the operator for the failure? And/Or were these seen on the logs?  Answer to both: There is very limited action that any operator could have taken. The only potential action is a Land Immediately, but that is only advisable below a certain AGL. The system would have had to recognize the error, warn the operator and the operator take action is a very short span of time, which isn't a feasible process.

Speaker notes:
SW release workflow, simulated flight hours prior to flight test, phased implementation, GNSS denied testing, regression testing refinement.
