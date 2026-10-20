# VIT_V647_RTB_Investigation.pptx

Attachment 39760, pptx, 1510 KB, added 2026-01-16 by Ryan Christino.

## Slide 1

Investigation Report
AC 467 Low Energy RTB 
Author: Ryan Christino
Jan 14th, 2026
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

## Slide 3

Investigation Overview – Status: INVESTIGATING –  INCONCLUSIVE [1/12/2026]
Edge Autonomy Proprietary Information
Incorrect Sensor Reading
Triggers Low Energy RTB
[picture]
[picture]
[picture]
Investigated but inconclusive
Not the root cause or contributing factor
Root cause or contributing factor
Conclusion & Corrective Action:
Leading theory is that an unlikely corruption event occurred and triggered an incorrect warning.
[picture]
Low Energy RTB Warning Triggered Prematurely; Operator Continued Flight
Excessive U-Drive commands could have triggered roll fault. This could have cascaded to a corruption event. No direct evidence available for this.
Low Energy RTB was Triggered as Designed
Next Steps:
Monitor aircraft for similar events.
Corrupted Data Triggered Low Energy RTB
[picture]
[picture]
Available flight data (slow recording rate) shows no evidence for incorrect sensor readings that could trip a low energy RTB.
Flight data captured at the timestep closest to the RTB plugged into the RTB calculation indicates this should not yield a low energy RTB.

## Slide 4

Investigation Status / Known Conclusions
Aircraft was reported to have RTB’d for low energy while in U-Drive mode at 57% SOC.

Aircraft did indeed register a low energy RTB at 66% SOC while flying relatively close to the launch / landing zone.

Several other fault flags including roll, turret, and fuel cell were triggered two minutes prior to the RTB.

Flight data at slow recording rate shows no evidence for corrupted values or values that would trigger an RTB.

## Slide 5

Investigation Plan
Review provided AAR for Root Cause

## Slide 6

GCS Debug Log and Event Log
GCS:
[15:07:54.969] VTOL MSG: Takeoff
[15:18:42.535] Show Caution(): Low Energy RTB
~ 10 Min and 48 Sec in for flight

XCOMM:
Time: 031:37.547  Launch detected: 0.000000  0.000000
Time: 034:55.265  U-Drive activated
Time: 034:55.265  U-Drive activated
Time: 034:55.422  U-Drive activated
Time: 034:55.468  U-Drive activated
Time: 040:10.062  Fault Status Changed: 0x00114000
Time: 040:20.047  Fault Status Changed: 0x00014000
Time: 042:19.000  Vehicle low energy RTB: 0.000000  0.000000
*Occurred at 642.453 Seconds (or 10 Minutes and 42.453 Seconds)
Observations:
A roll fault occurred during U-Drive operation which could have been caused by excessive operator turn rate input for a prolonged amount of time (~10 seconds). This wouldn’t trigger a low energy RTB but could have led to a potential corruption event.
2 minutes is the timeframe for the averaging of the power readings. Power readings from the data indicates this shouldn’t be an issue
0x00100000 = AP_FAULT_ROLL - Roll control fault detected
0x00010000 = VT_FAULT_LINK_TURRET - Loss of link to turret system
0x00004000 = VT_FAULT_LINK_FC - Loss of link to fuel cell system

## Slide 7

Theoretical RTB Calculation
Sensor Values:
Range = 2433 ; AP Reported GCS Slant Range (ft)
SOC = 0.66 ; AP Reported Aircraft SOC
Flight Speed = 64.4 ; Predicted Aircraft Ground Speed with Wind Estimate Included
Nominal Endurance = 240 ; % Uploaded from Config File (Standard VXE30 Gains – “T95_V674_251112_150801_gain.apx.txt”)

RTB Equation:
Recovery Time = (Range / GS) + 60 ;
Endurance = (Nominal Endurance * SOC ) * 60 ;
Recoveries Possible = Endurance / Recovery Time ;
If Recoveries Possible < 1.2 -> Low Energy RTB

Conclusion:
Approximately 97 recoveries possible at that distance and SOC. The threshold needed to trip the RTB is 1.2 recoveries. A low energy RTB does not make sense in this situation.


*In XCOMM event log, in flight data recording set to 1 sample every 20 seconds for fixed wing flight. RTB occurred at ~ 6106.253. The time step of 6105.612 from the XCOMM log was used for RTB evaluation.

## Slide 8

RTB Related Functions Upstream
Related Functions:
// vflight = gpsnav->HowFastToBase() 
// HowFastToBase() = WindTriangleGS(WindVector.Radius, CruiseSpeed, WindVector.Angle, heading)
// WindTriangleGS() = airspeed * sqrt(1 - (crosswind/airspeed)^2) – headwind

short WindTriangleGS(short windspeed, short airspeed, short windangle, short course)
    // *** WIND IMPACT ANALYSIS: For 15 fps wind (windspeed=15) ***
    // *** WORST CASE: Direct headwind reduces groundspeed by full wind speed ***
    // *** EXAMPLE: 50 fps airspeed - 15 fps headwind = 35 fps groundspeed (30% reduction) ***
    if(airspeed==0) return 0;						// *** vflight = 0: No airspeed ***
    short xwind = (windangle - course) + 1800;				// *** Relative wind angle (1800 = 180 deg) ***
    short swc = (short) (((long) windspeed * (long) sin(xwind)) / airspeed);			// *** Crosswind component ***
                                               						// *** 15 fps wind: Max crosswind = 15 * sin(90°) = 15 ***
    if(abs(swc)>1000)     						// *** Wind > airspeed check *** return 0;			
    short gs = (short) ((long) airspeed * (long) lsqrt((unsigned long)(1000000L - (long)swc*swc)) / 1000L);
                                       						 // *** Forward speed accounting for crosswind drag ***
                                      						 // *** 15 fps crosswind: gs = airspeed * sqrt(1 - (15/50)²) = 0.95 * airspeed ***
    gs = gs - (short) (((long) windspeed * (long) cos(xwind)) / 1000L);			// *** Subtract headwind component ***
    							// *** MAX REDUCTION: 15 fps direct headwind *** // *** 50 fps cruise - 15 fps 								headwind = 35 fps (30% reduction) ***
    return gs;

## Slide 9

RTB Related Functions Upstream (Continued)
short GPSNavigation::HowFastToBase()
    Waypoint lzwp;
    lzwp = *navm->GetLZWaypoint();
    short heading = hereNoEx->Bearing(&lzwp);	// heading for rtb
    short groundspeed = WindTriangleGS((short)WindVector.Radius, outerloop->GetCruiseSpeed(false), WindVector.Angle, heading);	
// *** vflight CALC: Wind triangle calculation ***
    return groundspeed;					
// *** vflight RETURN: Can be 0 if wind calc fails ***

## Slide 10

RTB Related Functions Upstream (Continued)
// Step 1: Get bearing to LZ
Short heading = hereNoEx->Bearing(&lzwp); // Returns: 045°(northeast)
// Step 2: Wind triangle calculation
// BUT: Wind data is corrupted during roll fault recovery
short windspeed = WindVector.Radius;     // Could be: 20 knots (normal)  
short airspeed = outerloop->GetCruiseSpeed(false);  // Could be: 50 knots (normal)
short windangle = WindVector.Angle;     // IF CORRUPTED: 1845° instead of 270°!
short course = heading;                 // 045°// Step 3: Wind triangle math
short xwind = (1845 - 045) + 1800 = 3600;  // Should wrap to 0, but...
short swc = (20 * sin(3600)) / 50;     // sin(3600) ≈ sin(0) ≈ 0, so swc ≈ 0// Step 4: BUT if there's ANY corruption in the angle wrapping...
if (xwind becomes some bad value due to overflow/corruption)
   { swc could become > 1000
    if(abs(swc) > 1000) return 0;  // RETURNS 0!}

Observations:
It seems unlikely without the upstream functions really blowing up from a corrupted value that a low energy RTB will be triggered

## Slide 11

Plotting RTB Relevant Data
[picture]

## Slide 12

Plotting Data
[picture]

## Slide 13

Plotting Data
[picture]

## Slide 14

Corruption Protection
In the SOC calculation, a 30 second average is taken for endurance calculations providing some additional corruption protection for short inaccuracies in battery measurements.

eave = new DataBox(30); // *** SOC TIMING: 30-second endurance averaging - corruption protection ***

## Slide 15

Roll Fault Error
The following is how the roll fault error is set off. It is a summation of both turn rate error and bank angle error. This is then compared against a config file defined threshold.
abs(tracc) > TrErrorSumThresh * 100 and 10 deg/sec sustained error for 4+ seconds (minus leak rate)
if(abs(trerr) > (short)NvBuffer2.data.TrErrorThresh)
    	tracc += trerr;    // Add turn rate error

if(abs(baerr) > (short)NvBuffer2.data.TrErrorThresh)  
	 tracc += baerr;    // Add bank angle error
[picture]
[picture]

## Slide 16

Plotting Extra Data
[picture]

## Slide 17

Plotting Extra Data
[picture]

## Slide 18

Plotting Extra Data
[picture]

## Slide 19

Plotting Extra Data
[picture]

## Slide 20

Plotting Extra Data
[picture]

## Slide 21

Incident Summary
Reporter:
Severity: Low. A low energy RTB warning at the incorrect SOC can confuse the operator potentially leading to serious issues if completely ignored, but operators can apply best judgement to work around the situation depending on the mission.
Key Findings from Summary
Follow Up Actions
Edge Autonomy Proprietary Information
Monitor for future incidents.
Low energy RTB was prematurely triggered.
Possible theory is a prior roll fault led to a corruption event triggering the low energy RTB.
Inconclusive evidence on the exact cause of this issue.

## Slide 22

BACKUP
[picture]
[picture]
