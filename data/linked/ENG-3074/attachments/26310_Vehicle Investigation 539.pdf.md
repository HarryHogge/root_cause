# Vehicle Investigation 539.pdf

Attachment 26310, pdf, 2214 KB, added 2025-02-18 by Pat Wells.

## Page 1

1
Investigation  Report
VXEP ‐416
V539
Author:  Jason  Scherer
February 4, 2024

## Page 2

2
Proprietary
VXE30 - Issue Resolution Process
D7 – Prevention
D8 ‐Done
Yes
Add to Lessons
Learned
Document
Debrief Customers
Closed
With
UFRs
UFR
Added?
No
Send UFR 
Description
To Customer
Closed
User
Creates 
Incident 
Report (IR)
User Assembles After Action Report 
(AAR)
EA Assembles Incident Response Team (IRT)
User Secures Aircraft
User Packages Aircraft 
and Ships to EA Depot
EA Receives Aircraft
IRT reviews IR and AAR
IRT Inspects Aircraft
IRT requests additional info from customer
(phone, email, zoom, etc.)
IRT releases first‐look report (FRP)
D1 –F o r m Team
D2 –D e f i n e The Problem
D3
Investigate Root 
Cause
D4 –F i n d Root Cause
D5
Verify Root Cause
RCIT Releases Root 
Cause Report (RCR)
EA Assembles Root 
Cause Investigation 
Team (RCIT)
Alert Users
IRT creates Airworthiness 
Directive (AWD)
IRT publishes AWD
Affected customers are 
alerted to AWD
Is AWD 
Required?Yes
D3 – Interim Containment
D4
No
D4
Is Safety 
Alert 
Required?
IRT creates
Safety Alert
IRT publishes 
Safety Alert
Alert Users
Via ICR
IRT creates list of aircraft tail‐
numbers affected by the 
incidents
IRT creates list of affected 
customers
IRT creates Interim 
Containment Report (ICR)
Yes
No
EA Assembles Corrective Action Team (CAT)
CAT Creates List of Corrective Actions
Funded
Fixes
Unfunded
Fixes
Add to Prioritized 
UFR List
Estimate Cost & 
Schedule
D6
D5 –D e f i n e Corrective Action
D8
Brief Customer on 
UFR
Are Fixes 
Required?
CAT Creates Corrective Action Plan and 
Releases Corrective Action Report (CAR)
Yes No
No
Yes
Alert Users
Funding 
Available 
to Fix 
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
Fix Code
Bench
Test
HIL Test
Flight
Test
Release
Software
Upgrade
Create 
Service 
Bulletin
Alert Users
Publish 
Service 
Bulletin & 
SW
Prelim
Design
Final
Design
Build
Prototype
Bench Test
Prototype
Flight Test
Prototype
Create 
Service 
Bulletin
Ship to 
Customers
Publish
Service
Bulletin
Production
Design
Production 
SCM Plan
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
Alert Users
Identify 
MTBF Gaps
Update 
Sparing Plan
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
Action Plan 
(CAP) for 
SCM and 
Production
Implement 
CAP in SCM 
and 
Production
D6 – Implement and Verify Corrective Action
Alert Users
Create 
HIL/Flight 
Test Cards
Update Regression Tests for HIL and Flight Test
D7
Alert User of Preliminary Assessment
(known causes / mitigations)
Create
Operational 
Supplement
Publish 
Operational
Supplement
Alert Users
Version: Feb 2025

## Page 3

3
Investigation Overview – Status: INVESTIGATING – D6 [Updated 2024-09-11 jscherer]
Edge Autonomy Proprietary Information
Failure  to  launch
VXEP ‐416
V539
SAFE Mode Active
During the first launch 
the vehicle did not 
disable SAFE mode 
after motor testing and 
prior to launch
Investigated but inconclusive
Not the root cause or contributing factor
Root cause or contributing factor
Next  Steps :
1. Implement  corrective  actions Conclusion  & Corrective  Action :
1. Update  software  to  ensure  delivery  of  SAFE  ON/OFF  
commands  between  XComm and  VTOL.
2. Fix  logging  software  to  positively  confirm  transmission  
of  the  SAFE  OFF  message.
3. Update  software  to  reset  VTOL  autopilot  during  
software  resets.
~JScherer
Uplink Dropout
SAFE off 
commands are 
sent directly 
from XComm.
~JScherer
CAN Bus Dropouts
Software has a bug that prevents logging 
of SAFE off commands, however, there is 
evidence that XComm ran the code that 
should have sent the SAFE off command. 
There is also evidence that some timeouts 
occurred on the CAN bus, but not at the 
time of the missing SAFE off message. 
~JScherer
VTOL State
VTOL autopilot was in a 
weird state after the first 
launch which activated an 
RTL loop. While the 
operator issued a reset, the 
VTOL AP was not reset. 
Second launch immediately 
landed due to RTL loop on 
VTOL AP.
~JScherer
Additionally, there is missing 
motor tests reported on XC for 
both launch attempts.

## Page 4

4
Summary [Updated 2024‐09‐10 jscherer]
Reporter: Patrick Wells
Severity: Degraded Performance‐No Workaround
Missing SAFE OFF Command During First Launch
Edge Autonomy Proprietary Information
VXE 539 failed to disable SAFE mode during the first launch attempt which prevented launch, and activated 
“RTL” (Return To Land) mode on the VTOL autopilot. After the first attempt the operator issued a software reset 
through the GCS launch wizard. This unfortunately does not reset the VTOL autopilot which was still in an RTL 
loop. During the second launch attempt, the vehicle successfully disabled SAFE mode and began launching 
before immediately landing due to the active RTL loop.
Customer Statement: During a training flight the aircraft was armed, and launch was selected. The 
aircraft did not respond. Three attempts were made. During one attempt the VTOL message “Launch 
abort, lift power fault” was displayed.
Additional information received from Lockheed FSR on 5/22
“Yesterday, V539 flew its first flight of the day with no issues. During Launch Wizard for its second 
flight, it failed the first Sensor Calibration, then passes a few seconds later, and passed the second 
Sensor Calibration the first attempt. When commanded to Launch, the screen said “Waiting to detect 
launch” for about a minute, the window to “Enable User Launch Control / Abort“ was open. I noticed 
the VTOL status window on the right of the screen said Entering RTL mode (RTL = Return To Launch 
point). The plane had aborted the launch before engaging the lift rotors. The “Waiting to detect 
launch” and “Enable User Launch Control / Abort” windows remained open. We enable user launch 
control and commanded “Cut motors and safe vehicle”. Instead of closing, the window changed back 
to “Enable User Launch Control / Abort” window. We disconnected from the plane and closed and 
restarted the CGS software. The “Cut motors and safe vehicle” was still open. Resetting the autopilot 
(in the launch wizard) did not result in the window closing.
On the second launch attempt, all four lift rotors engaged at a low power setting. The plane did not 
come close to lifting out of the stand. The “Enable user launch control” button was open, but grayed 
out and we were not able to enable user launch control or command Cut motors and safe vehicle (from 
that window). The autopilot aborted the launch. VTOL status window said “Landed”.
We produced a second AAR w/ FDR.
We disconnected from the plane, closed the GCS software, and restarted the GCS laptop. We 
disconnected the aircraft main power cable from the main battery, waited 10 seconds, and 
reconnected it to fully reset the plane. Third launch attempt was like the first: the screen continued to 
say Waiting to detect launch and the VTOL status said Entering RTL mode. A third AAR w/ FDR was 
produced and the plane was put away.”
VTOL Autopilot stuck in RTL Loop During Second Launch

## Page 5

5
Vehicle in SAFE mode during first launch [Updated 2024‐09‐10 jscherer]
Edge Autonomy Proprietary Information
• SAFE Mode is disabled for motor testing.
• SAFE Mode is NOT disabled prior to launch.
VTOL Fails to Disable SAFE Mode Which Prevents First Launch
During the first launch attempt the safe mode is successfully disabled to perform motor tests. Then prior to launch, the SAFE mode is not disabled before arming the vehicle. This
indicates the VTOL autopilot did not receive the SAFE off command prior to actual launch, but did receive this same command during motor testing.
T95_VT539_240521_142311_vtl00080.csv
UTC 
(HHMMSS.MS)

## Page 6

6
VTOL AP in RTL Loop after first launch [Updated 2024‐09‐10 jscherer]
Edge Autonomy Proprietary Information
• VTOL AP is stuck in landing loop after first launch failed
• Operator commanded reset does not reset the VTOL AP
• Second launch is successful in disabling SAFE mode and ARMing the vehicle, however
the VTOL AP immediately switches to RTL mode to land the vehicle.
Log Messages Show Repeated Landing Commands
After the second launch, the VTOL autopilot is stuck in a software loop that commands landing. The Operator reset the vehicle for the second launch attempt, however, that did not
reset the VTOL autopilot. After the second launch the VTOL ap immediately switches to landing mode (RTL).
VTOL Mode Immediately Changes to RTL After Launch

## Page 7

7
CAN Timeouts – First Launch Attempt [Updated 2024‐09‐11 jscherer]
Edge Autonomy Proprietary Information
• During this launch attempt the SAFE mode only switches of for the motor tests. The vehicle is in SAFE
ON mode when the launch is commanded.
• This CAN timeout was recorded by both the XComm and VTOL AP microcontrollers.
• VTOL Offline status is driven by messages received over CAN, so having it match the CAN timeouts
makes sense.
• XComm datalog does not include one of the motor tests which would be reported over CAN from VTOL
to XC
During the first launch attempt, a CAN bus timeout is recorded after motor testing and before launching. A timeout means that no CAN messages are received for at least 2 seconds.
First Launch Attempt
VTOL Offline
CAN Timeout
Motor Tests
ARMed
SAFE 
Mode Off
0
0.1
0.2
0.3
210004
21010…
21010…
21011…
21012…
21022…
21022…
21023…
21024…
21025…
21025…
21030…
21031…
21031…
21032…
21033…
21034…
21034…
21035…
21041…
21042…
21043…
21043…
21044…
21045…
21050…
21050…
21071…
21082…
21083…
21084…
21084…
VTOL Report of Throttle During Motor Test
CHAN_MCMOTOR1 CHAN_MCMOTOR2
CHAN_MCMOTOR3 CHAN_MCMOTOR4
0
0.1 0.2
0.3
XComm Report of VTOL Throttle During Motor Test
vtThr1 vtThr2 vtThr3 vtThr4
All 4 Motors
Only 3 
Motors
T95_VT539_240521_142311_vtl00080.csv
T95_V539_240521_142311_xcl00072.csv
Xcomm Does Not Log Test of motor #3 (First Launch Attempt)
NOTE: 
Logs are not 
time synced

## Page 8

8
CAN Timeouts – Second Launch Attempt [Updated 2024‐09‐11 jscherer]
Edge Autonomy Proprietary Information
• During the second flight the SAFE mode switches off for both the motor tests as
well as the launch attempt.
• All three timeouts are recorded by the VTOL AP microcontroller.
• The middle timeout (21:18:00 – 21:19:00) was also recorded by the XComm
microcontroller.
• VTOL Offline status is driven by messages received over CAN, so having it match
the CAN timeouts makes sense.
• XComm datalog does not include two of the motor tests which are reported
over CAN from VTOL to XC
Second Launch Attempt
During the second launch attempt, three CAN bus timeouts are recorded with one being before the motor test while two are after but before the launch. A timeout means that no CAN
messages are received for at least 2 seconds.
VTOL Offline
CAN Timeouts
ARMed
SAFE 
Mode Off
Motors Spinning
Motor Tests
Motor Tests
XC Missing 2 
Motor Tests
