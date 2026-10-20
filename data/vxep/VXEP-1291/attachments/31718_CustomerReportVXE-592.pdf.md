# CustomerReportVXE-592.pdf

Attachment 31718, pdf, 1324 KB, added 2025-08-25 by Jackson Riley Curvin.

## Page 1

1
Investigation Report
VXEP -1291
V592

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

3
Investigation Overview – Status: Implementing Corrective Actions
Edge Autonomy Proprietary Information
No indication of 
structural failure before 
crash
Sudden unexplained jump 
in fixed-wing attitude and 
rate bias estimate
Aircraft appears to 
respond to commands
Failed/Stuck 
control surface
Fixed-wing Attitude 
Estimate Erroneous
Aircraft Structural Failure
VTOL attitude estimate is 
consistent with flight 
behavior
Investigated but inconclusive
Not the root cause or contributing factor
Root cause or contributing factor
Next Steps : 
1. Investigate why fixed - wing attitude was erroneous
2. Implement corrective actions.
Conclusion & Corrective Action :
1. Fixed-wing attitude estimate is erroneous
2. Erroneous attitude estimate causes aircraft to dive and overspeed, resulting in a crash
3. Investigation inconclusive on true root cause
4. Missing XCOMM logs make pinning root cause difficult
5. CA: Implement clipping in software to avoid single erroneous measurement corrupting AHRS filter
6. CA: Implement buffering to avoid loss of xcomm logs in similar event
Evidence To 
prove
Evidence To 
Support
Evidence To 
Disprove
Loss Of Control
Autopilot 
Hardware Failure
Fixed-wing log shows 
autopilot still functioning 
at time of impact
Elevator Inspection 
Showed It To Be 
Functional
Fixed-wing attitude is 
inconsistent with flight 
behavior
Incorrect Fixed-Wing 
Attitude
Airspeed Sensor Failure
Airspeed measurement 
appears consistent with 
flight profile
GPS Spoofing
Position/Velocity 
consistent with 
baro and airspeed 
measurements
No indication of 
position or velocity 
jumps
Aircraft not in hostile EW 
environment
IMU/mag Sensor Failure
IMU measurement 
appears erroneous
Logged measurement 
includes IMU measurement 
+ bias estimate
IMU failure appears to 
manifest differently in 
simulation testing
Software Bug
Attitude estimate jumps 30+ 
degrees in a single time step
Measurements within 
expected software 
bounds cannot cause this 
jump
Issue can be recreated with 
out of bounds measurement

## Page 4

4
Timeline
Severity: Mishap
Timeline of events
Edge Autonomy Proprietary Information
All times Xcomm unless noted otherwise.
2570: PollMainLoop blocked ms=2032 logged in GCS
2574.58: Xcomm.csv logs drop out (flight profile is 
still normal)
2578.78: FWAP fast logging begins
2585: IAS reading reaches 100fps, fw autopilot 
believes vehicle is pitching up
2586.34: FWAP logs roll fault in xcomm event log
2592: impact
2593: ap logs airspeed fault and 'fixed wing ignoring 
vtol mag'

## Page 5

5
ANALYSIS: Fixed-wing and VTOL Attitude Disagreement
• VTOL and Fixed-wing attitude estimates disagree. VTOL attitude estimate is more consistent with vehicle behavior (i.e. pitch down, increase airspeed 
lose altitude).  Fixed-wing believes it is pitching up and only rolling slightly, which explains why the autopilot responds by pitching down hard.
Edge Autonomy Proprietary Information
Root cause or contributing factor

## Page 6

6
ANALYSIS: Fixed-wing and VTOL Rate Disagreement
• Analysis of rate data reveals a sudden step in the roll and yaw rate data logged on fixed-wing
• Roll rate data includes both raw measurement and AHRS bias estimate
o Means it is inconclusive as to whether the raw gyro measurement is incorrect or whether the AHRS had an incorrect bias
o XCOMM logs would have raw rate data, but they cut off before the time in question 
Edge Autonomy Proprietary Information
Root cause or contributing factor

## Page 7

7
Fixed Wing autopilot reduces throttle to correct for high air speed during fall
As the vehicle begins to descend, the airspeed increases quickly. As a result of high 
airspeed, the autopilot commands lower throttle.
Most likely a secondary effect of the root cause
• X-Axis on charts is fixed wing CPU seconds. Charts from FDR
• At 928 seconds, the vehicle begins to descend rapidly and impacts ~2 seconds later.
• After 928 the airspeed increases significantly.
• The autopilot compensates for high airspeed by reducing throttle.
• The bottom graph “Throttle and Throttle without airspeed correction” shows what the 
throttle would have been without the adjustment for air speed.
• As a result of lower throttle, the primary battery voltage increases due to less load.
Note: Altitude 
decreases rapidly
Note: Airspeed 
increases rapidly
Note: Throttle with and without 
airspeed compensation
Note: Primary battery 
voltage increases 
during decent

## Page 8

8
ANALYSIS: Sim recreation
• Attempted to create the bias and attitude changes we saw by injecting some erroneous data in the sim.  Accel and rate changes did not look all that similar, while mag data did.
• Note step changed in bias estimates (RRInt/PRInt/YRInt).  This indicates that the raw gyro measurements may be healthy while the filter output is erroneous
• Magnitude of injected error is outside the range of what should be possible given current software limit
Edge Autonomy Proprietary Information

## Page 9

9
Elevator Servo and boost board inspection
Performed 6/20/2025
• Inspection of elevator servo and boost board was performed to verify function.
• Boost board was tested using ‘VXE30 Servo Boost Boards Test Procedure’ 
– \\condor\production\Procedures\VXE30\Servo Boost Procedure\Servo Boost 
Procedure
– Tested normal
• Boost board and elevator servo were connected to electronics shop iron bird. Using RC, 
horizontal servo was actuated and moved commensurate with RC inputs
Servo Test Procedure example step
Test Data
Not the root cause or contributing factor

## Page 10

10
CONCLUSION DETAILS 
Severity: Mishap
Corrective Actions
Edge Autonomy Proprietary Information
1. CA: Implement clipping in software to avoid single erroneous measurement 
corrupting AHRS filter
2. CA: Implement buffering to avoid loss of xcomm logs in similar event to make 
troubleshooting and identification of root cause easier.
• The most likely assessment, based on available data, is that 
an out-of-range measurement resulted in corruption of the 
AHRS filter.
• The extensive flight hours accumulated without recurrence 
of this anomaly indicate that the failure mode is extremely 
rare.
• Planned corrective actions are expected to further reduce 
the likelihood of reoccurrence.

## Page 11

11
