# VXE-530 Anomalies.pdf

Attachment 30002, pdf, 524 KB, added 2025-06-18 by Pat Wells.

## Page 1

1
Investigation Report
VXEP-555
V530
March 31, 2025

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
Investigation Overview – Status: INVESTIGATING – D4 [Updated 2025-03-31]
Edge Autonomy Proprietary Information
VXE 530 Anomalies on 
Launch and in flight
A recent bug has been discovered in the GCS that can cause 
the vehicle to lose connection during mission simulations. If 
the vehicle released the GCS connection due to timeout, 
then the GCS would have to reconnect.
If the vehicle is in flight during a long mission simulation, the 
vehicle could execute a lost comms mission due to the lost 
connection with GCS.
Long Mission Sim leads to Mission Upload 
Timeout and uncommand LOS mission (1&4)
Investigated but inconclusive
Not the root cause or contributing factor
Root cause or contributing factor
Conclusion & Corrective Action :
1. Resolve GCS simulation bug
2. Advise operators to not switch GCS Ethernet ports 
during flight
3. Update vehicle firmware
Evidence To 
Disprove
Evidence To 
Support
Evidence To 
ProveEthernet Issue (3)
The GCS logs show that the Ethernet connection was 
moved from one port to another. Each port has a 
unique IP address. The new port would not be able to 
connect to the vehicle until a 50 second timeout on the 
previous connection is complete.
GCS Mission Sim Bug
Swapped Ethernet Ports
GCS Telemetry Lag (5)
Brief Throttle Pause on Launch (2)
Vehicle firmware version has a known software 
behavior that can cause a throttle delay if the 
VTOL controller is not restarted between flights.
This issue has been resolved in newer firmware
Known Firmware Bug
Suspect LOS causes GCS to 
spam ELZ commands on re-
connect. Need to attempt 
HIL recreation.

## Page 4

4
Mission sync issue
Edge Autonomy Proprietary Information
During V530 1st flight of the day, 4th flight of the T&E, during a mission sync, the sim took a LONG time, then the 
mission upload failed and timed out. This happened a few times before the mission was successfully sync’d. Mission 
was fairly large/long, but still took an unexpectedly long time (and multiple failures) to sync. Comms indicator was 
green and comms (per the Silvus GUI) were excellent (SNR=34, Airtime <60%).
Response:
A software bug in the GCS, can cause the vehicle to disconnect link during long mission simulations which leads to 
execution of loss of link behavior as observed.

## Page 5

5
VTOL throttle delay
Edge Autonomy Proprietary Information
On the 2nd flight of the day, the aircraft paused briefly (throttle reduced) before lifting out of the stand, then paused 
for ~5 seconds at 10 feet before continuing to climb. See attached video with sound up to hear throttle pause in stand.
Response:
VTOL Controller was not restarted between flights causing known throttle delay issue in previous firmware versions. 
This has been corrected in new firmware.

## Page 6

6
Ethernet Issue
Edge Autonomy Proprietary Information
During flight, radio Ethernet cable was moved from one Ethernet port to the other to eliminate multiple SA camera 
video feeds in the downlink. Cable was reconnected within 2-3 seconds. GCS software took 60+ seconds to reconnect to 
aircraft. Comms (per Silvus GUI) were great.
Response:
Each ethernet port has a unique IP address. Suppose the IP for port 1 is 10.10.10.1 and port 2 is 10.10.10.2.
When the cable was disconnected, the vehicle detected that it lost link with the GCS at IP address 10.10.10.1. It then 
started waiting for the GCS at IP address 10.10.10.1 to reconnect. During this time the vehicle would not allow 
connections from other GCSs (specifically the one at IP address 10.10.10.2).When the vehicle eventually. timed out on the connection, it then allow the GCS at IP address 10.10.10.2 to connect.,
The vehicle could not tell that it was the same GCS trying to reconnect. It thought it was another GCS trying to take 
control.
In a handoff, which is what this was, the GCS must manually disconnect from the vehicle, and then reconnect.,
Switching Ethernet ports while connected to a vehicle is not a supported operation.

## Page 7

7
RTB lost comms issue
Edge Autonomy Proprietary Information
When RTB was commanded, GCS screen froze with hourglass for 90+ seconds. When the sim (or whatever it was doing) 
finished, a window popped up for 1 or 2 seconds stating that the aircraft was executing the Lost Comms Mission. when 
the window closed, the aircraft entered the active landing pattern with no user input. Comms indicator remained green 
throughout and comms (per Silvus GUI) were great.
Response:
Data was not in provided logs. Unable to investigate.

## Page 8

8
GCS telemetry delay
Edge Autonomy Proprietary Information
During the landing pattern, it was observed that the aircraft position and telemetry on the GCS was 20-30 seconds 
behind the actual aircraft position. This could have been an issue if the gap had been longer and the aircraft had landed 
before the operator was given the option to Enable User Landing Control. See attached video of GCS showing aircraft on 
approach to landing while the aircraft was already on the ground. 
Response:
Investigation ongoing
