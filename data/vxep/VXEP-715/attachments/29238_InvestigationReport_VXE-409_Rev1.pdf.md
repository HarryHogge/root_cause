# InvestigationReport_VXE-409_Rev1.pdf

Attachment 29238, pdf, 787 KB, added 2025-05-21 by Sean Wendling.

## Page 1

Investigation Summary 
VXE 409 – Fuel Cell In-Flight Failure  
Incident Number: VXEP-715 
Revision: 1 
Author: S. Wendling 
Date: May 21, 2025 
 
CONFIDENTIAL AND PROPRIETARY DATA: 
Portions of this document contain proprietary technical data pertaining to items, or components, or processes, or 
other matter developed or acquired at the private expense of Edge Autonomy and is restricted to use only by Edge 
Autonomy employees or other persons authorized by Edge Autonomy in writing to use it. Neither said document 
nor said technical data shall be furnished or disclosed to, or copied or used by, persons outside Edge Autonomy, 
without the express written approval of Edge Autonomy. Markings on this page regarding confidentiality and 
proprietary information apply to this entire document. 
 
EXPORT CONTROL WARNING NOTICE:  
WARNING – this document may contain technical data whose export is restricted by the Arms Export Control Act 
(Title 22, U.S.C. Sec 2751 et seq) or the Export Administration Act of 1979 (Title 50, U.S.C., App. 2401, et seq) as 
amended.  Violations of these export laws are subject to severe criminal penalties.  Disseminate in accordance with 
provisions of DoD Directive 5230.25.   Contains Export Controlled Information Not releasable to Foreign Persons 
unless authorized by 22 C.F.R. 120-130 or 15.C.F.R. 730-774.

## Page 2

Investigation Summary:  (Fuel Cell Stopped Functioning in Flight) 
 
05/2025 Edge Autonomy Proprietary Information 2 
1 Table of Contents 
1 Table of Contents.................................................................................................................. 2 
2 Introduction and Executive Summary .................................................................................... 4 
2.1 High Level Summary – Updated 5/19/2025. ................................................................... 4 
2.2 Operator Description of the Incident ............................................................................. 5 
2.3 Status .......................................................................................................................... 5 
2.4 Root Cause .................................................................................................................. 5 
2.5 Corrective Actions ........................................................................................................ 5 
3 Root Cause Investigation Details ........................................................................................... 6 
3.1 VXEP-715 Preliminary Data Review ................................................................................ 6 
3.1.1 Timeline: .................................................................................................................. 6 
3.1.2 Root Cause Analysis Plan ........................................................................................ 11 
3.2 Preliminary Conclusion of Root Cause ........................................................................ 11

## Page 3

Investigation Summary:  (Fuel Cell Stopped Functioning in Flight) 
 
05/2025 Edge Autonomy Proprietary Information 3 
Figure 1: Photo of Equipment Provided by Operators. 
Figure 2: Flight Overview from AAR Data displaying AC range from GCS, and Altitude (ft) 
Figure 3: Power Sys Profile – Launch including HLB Charge (%), Aircraft Altitude AGL (ft), & Fuel Cell 
Power Output (W). 
Figure 4: Fuselage Temperature & Fuel Cell Stack Temperatures (°C) for forward flight prior to fault. 
Figure 5: Battery Charge (%), Fuel Cell Power (W), & Aircraft Power Use (W) during the forward flight 
period prior to fault. 
Figure 6: Raw SOFC Voltage (V) and Current (A) & Output Voltage (A) & Current (I) through the 
period of the crash. 
Figure 7: Fuselage & Fuel Cell Internal Temperatures after Crash. 
Figure 8: Fuel System Data including; Solenoid Duty Cycle and Fuel Flow Setpoint & Measured Flow 
Rate (LPM) after crash.

## Page 4

Investigation Summary:  (Fuel Cell Stopped Functioning in Flight) 
 
05/2025 Edge Autonomy Proprietary Information 4 
2 Introduction and Executive Summary 
2.1 High Level Summary – Updated 5/19/2025. 
Reported Failure of Electrical Power System on VXE-409 including D450XR Fuel Cell Serial Number: 
D4500072. Aircraft experienced a critical fault approximately 98min 15sec after takeoff, requiring 
immediate RTB. The aircraft was unable to safely RTB and crashed resulting in significant damage 
to the vehicle and equipment. 
The mission captured by the AAR shows a maximum elevation of approximately 1700ft, and a 
maximum winds aloft of 20mph. The power system throughout the flight experienced significant 
needs and minimally recovered HLB voltage throughout the flight leading to an average % charge of 
60% in fixed wing flight prior to fault occurrence.  
At this time, the team has been provided with a photo of the aircraft/equipment and the After-
Action Report Generated after the flight. The photo is shown below, and AAR can be found in the 
incident report folder. 
  
Figure 1: Photo of Equipment Provided by Operators.

## Page 5

Investigation Summary:  (Fuel Cell Stopped Functioning in Flight) 
 
05/2025 Edge Autonomy Proprietary Information 5 
2.2 Operator Description of the Incident 
Description provided by Flight Operator: (Posted in VXEP-715 Description) 
“Fuel cell stopped functioning in flight; operator executed emergency procedure - Land 
immediately commanded. HLB was depleted before aircraft was able to touch down. Aircraft 
crashed with moderate damage.” 
 
2.3 Status 
Initial Review of After-Action Data confirms Fuel Cell critical fault and operator description of 
events. The issue is currently still under investigation to attempt to identify the exact root cause of 
the fuel cell failure.  
RMA requested for all equipment involved in the incident in order to evaluate and provide 
assessments of repairs. Preliminary Data Review summarized and provided within published 
report.  
 
2.4 Root Cause 
Root Cause is still under investigation for this incident. Data review yielded a loss of DC current 
flow between Hybrid Lift System and Fuel Cell Generator as the fault condition that caused the 
failure, though additional investigation of the equipment is required to provide additional guidance 
and repair options.  
Leading Potential Root Cause Contributing Factors: 
• Failure of individual cells within the HLB.  
• Excessive Current Flow Resulting in Failure of Electrical Hardware. 
• Intermittent Fuel Cell DCDC Regulation Failure.  
 
2.5 Corrective Actions  
Upon determination of exact root cause, the EAES team will provide immediate asset related 
corrective actions including in-warranty / out of warranty repair requirements for Electrical Power 
System as well as provide guidance on risk mitigation and reduction.

## Page 6

Investigation Summary:  (Fuel Cell Stopped Functioning in Flight) 
 
05/2025 Edge Autonomy Proprietary Information 6 
3 Root Cause Investigation Details 
3.1 VXEP-715 Preliminary Data Review 
Users provided the following to supplement the photo and written account: 
AAR Data File FC Serial Number 
T95_V409_241009_003203_pack.zip D4500072 
 
3.1.1 Timeline: 
Flight Overview:  
Summary of the flight includes an initial climb to approximately 600ft within close proximity to the 
GCS home position, followed by a rapid climb from 600ft to ~1600ft as the aircraft moved away 
from the home position to approximately 22mi away and remained at this range and altitude up 
until the point of fault. Power system was operating in maximum output conditions for the majority 
of the flight, and HLB % charge was continuously in the range of 40-60%. Fault resulted in 
immediate command for Land Immediately, however the remaining HLB charge was not sufficient 
to bring aircraft to controlled landing, and it crashed. 
Following the fault and moderate crash resulting from the failure, the fuel cell continued to operate 
in some capacity until loss of fuel pressure through suspected leak or exhaustion of the remaining 
fuel in the tank. 
 
 
Figure 2: Flight Overview from AAR Data displaying AC range from GCS, and Altitude (ft)

## Page 7

Investigation Summary:  (Fuel Cell Stopped Functioning in Flight) 
 
05/2025 Edge Autonomy Proprietary Information 7 
 
Launch:  
In the XCL, the fuel cell was operating prior to the start of the data recorder; however, the fuel cell 
warmup behavior is captured by the fuel cell log and appears to be normal beginning the flight. The 
fuel cell health prior to the flight appears normal and does not indicate any SOFC Stack damage or 
improper subsystem performance.  
VTOL takeoff at T=586 to approximately 600ft, which appears to be uneventful.  Fuel Cell and 
battery behavior is normal. ~20% depletion of the HLB during VTOL period, followed by Fuel Cell 
Power output response climbing to 450W, aircraft loiter at 600ft to stabilize power system. 
Figure 3: Power Sys Profile – Launch including HLB Charge (%), Aircraft Altitude AGL (ft), & Fuel Cell Power Output (W). 
 
During Flight – Up to Point of Fault:  
After a brief period at 600ft AGL, the aircraft begins to climb to 1600ft in elevation. While the HLB 
maintains a charge state of approximately 60%, this climb results in surges up to 800W from the 
forward flight system of the aircraft. The fuel cell, due to the combination of surge power needs and 
low HLB Charge State maintains 450W, then increases its output to 500W in an attempt to maintain 
the output through excessive power need in this time period. 
For the 28min leading up to fault, a consistent downward trend in the HLB voltage can be seen as 
the HLB reaches a low of 35%. The aircraft appears to attempt to reduce its surge power by 
lowering AGL position which has a positive effect on the HLB, and an increase in the 5 min prior to 
the fault from 35% to 47%. The fuel cell is in steady 500W output, with a maximum internal 
temperature of 840°C. This is slightly higher than the nominal temperature but given the increased 
fuel burn required to sustain 500W, this is unsurprising.

## Page 8

Investigation Summary:  (Fuel Cell Stopped Functioning in Flight) 
 
05/2025 Edge Autonomy Proprietary Information 8 
At 76 min from launch, the fuel cell power appears to drop immediately from 500W to -26W output. 
The negative output power is consistent with the 26W power needs of the fuel cell internal 
functions indicating that the Auxiliary FC systems are still operating. This behavior indicates loss of 
current flow from the battery or fuel cell system. This loss can be seen in the immediate return to 
OCV (Open Current Voltage) state on the fuel cell. It is difficult to distinguish the source of the loss 
of current transmission in this system from the data in the AAR alone; however, this loss of energy 
distribution causes the initial fault condition of the fuel cell.  
 
Figure 5: Battery Charge (%), Fuel Cell Power (W), & Aircraft Power Use (W) during the forward flight period prior to fault. 
 
Fault Occurrence:  
The Fuel Cell can be seen with a -26W output for approximately 290 seconds, in this time, the HLB 
is driven to the critically low charge state of 8% which is supplemented by the restart and function 
of the Fuel Cell, though this is too late to recover control of the aircraft.  
Figure 4: Fuselage Temperature & Fuel Cell Stack Temperatures (°C) for forward flight prior to fault.

## Page 9

Investigation Summary:  (Fuel Cell Stopped Functioning in Flight) 
 
05/2025 Edge Autonomy Proprietary Information 9 
 
 
Figure 6: Raw SOFC Voltage (V) and Current (A) & Output Voltage (A) & Current (I) through the period of the crash. 
This Fault condition attributed to the immediate loss of DC current flow between the Fuel Cell and 
HLB does not immediately affect Critical Flight systems. The Aircraft continues to communicate 
and operate at the onset of the failure.  
The Fuel Cell behaves consistently with expected behavior; initiating a restart and beginning to 
recharge the hybrid lift battery after returning to operation. The Fuel Cell is able to successfully 
return to normal function, reducing the likelihood that physical damage caused the initial fault. 
Additional physical inspection and hardware review can provide better assessment of pre-crash 
damage. Following the land immediately series of events, during the transition to VTOL, the aircraft 
Hybrid Lift System is unable to support the complete VTOL, and results in the crash.  
 
After Crash:  
Aircraft continues to stream data after the crash. Following the landing, the cooling systems in the 
aircraft are not functioning, resulting in ambient temperatures increasing to up to 98°C inside of the 
fuselage.

## Page 10

Investigation Summary:  (Fuel Cell Stopped Functioning in Flight) 
 
05/2025 Edge Autonomy Proprietary Information 10 
 
Figure 7: Fuselage & Fuel Cell Internal Temperatures after Crash. 
Additionally, it is suspected that from crash to recovery fuel cell continues to operate until the 
remainder of fuel is completely consumed or expelled from the system as the proportional valve in 
the fuel cell fully opens due to the reduction of all fuel pressure in the fuel system.  
 
Figure 8: Fuel System Data including Solenoid Duty Cycle and Fuel Flow Setpoint & Measured Flow Rate (LPM) after 
crash. 
Either the excessive temperature or the loss of fuel pressure resulted in the eventual shutdown of 
the fuel cell which proceeds as normal and indicates functioning auxiliary processes on the fuel 
cell.

## Page 11

Investigation Summary:  (Fuel Cell Stopped Functioning in Flight) 
 
05/2025 Edge Autonomy Proprietary Information 11 
3.1.2 Root Cause Analysis Plan 
To establish an exact root cause, the following items will need to be assessed upon return of the 
equipment: 
Incoming Performance Evaluation: 
• Functional Fuel Cell QC Test to assess health and performance. 
o Does SOFC Stack need replacement? 
o Does FC Control Unit need repair or replacement? 
• DC Regulation System Review (Possible failure between Raw Stack Output and Regulated 
Charge Output 
• Assessment of Control Board Function and Communication Accuracy 
• Hybrid Lift Battery Individual Cell Voltage Analysis (Cell-to-Cell Variation indicates internal 
battery failure) 
• Connector / Harness Damage due to over-draw or discharge of energy during high current 
use. 
 
3.2 Preliminary Conclusion of Root Cause 
Loss of DC current flow in the Electrical Power System can be the result of a number of contributing 
factors. The exact root cause can only be determined by evaluation of both the Hybrid Lift Battery 
and Fuel Cell for damage or subcomponent failure.   
• Failure of individual cells within the HLB, resulting in a reduction in charge / discharge 
performance in the Power System.  
• Excessive Current Flow Resulting in Failure of Electrical Hardware (connectors, harnesses, 
PCBs). 
• Fuel Cell DCDC Regulation Circuit Intermittent Failure.
