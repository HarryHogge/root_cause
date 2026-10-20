# InvestigationReport_VIT2-500_Rev1.pdf

Attachment 26213, pdf, 1329 KB, added 2025-02-13 by Sean Wendling.

## Page 1

Investigation Summary 
VIT2-500 – Fuel Cell Flameout  
Incident Number: VIT2-500 / VXEP-732 
Revision: 1 
Author: S. Wendling 
Approver: T. Westrich 
Date: February 13, 2025 
 
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

Investigation Summary:  (Fuel Cell Flameout in Flight) 
 
02/2025 Edge Autonomy Proprietary Information 2 
1 Table of Contents 
1 Table of Contents.................................................................................................................. 2 
2 Introduction and Executive Summary .................................................................................... 4 
2.1 High Level Summary – Updated 1/29/2025. ................................................................... 4 
2.2 Operator Description of the Incident ............................................................................. 4 
2.3 Status .......................................................................................................................... 5 
2.4 Root Cause .................................................................................................................. 5 
2.5 Corrective Actions ........................................................................................................ 6 
3 Root Cause Investigation Details ........................................................................................... 7 
3.1 VIT2-500 Preliminary Data Review ................................................................................. 7 
3.2 Incoming Failure Analysis ............................................................................................. 9 
3.2.1 Incoming Physical Inspection .................................................................................... 9 
3.2.2 Fuel System Leak Check ........................................................................................... 9 
3.2.3 Fuel Flow Sweep ....................................................................................................... 9 
3.3 Teardown of System ................................................................................................... 12 
3.4 Conclusion of Root Cause .......................................................................................... 12 
4 Corrective Action Development Study ................................................................................. 13 
4.1 Overview of Corrective Actions ................................................................................... 13 
4.1.1 Correction of Flow Direction & Re-calibration .......................................................... 13 
4.2 Risks to System Health ............................................................................................... 14 
5 Verification of Corrective Action .......................................................................................... 15 
5.1 D4500509 Verification Testing ..................................................................................... 15 
5.1.1 Incoming Operational Cycle .................................................................................... 15 
5.1.2 Fuel Accuracy Endurance Verification Cycle ............................................................ 15 
5.2 D4500510 Verification Testing ..................................................................................... 19

## Page 3

Investigation Summary:  (Fuel Cell Flameout in Flight) 
 
02/2025 Edge Autonomy Proprietary Information 3 
List of Figures 
Figure 1: IMG_2821 Full Tank Following Liquid Propane Fill (1220g). ............................................... 7 
Figure 2: IMG_2825 Tare Mass of Tank prior to fill procedure(299g). ................................................ 7 
Figure 3: Chart displaying Fuel Flow (LPM) & Estimated Fuel Burn (g) over flight time. (Unit 
D4500510) ................................................................................................................................... 8 
Figure 4: Chart displaying Fuel Flow (LPM) & Estimated Fuel Burn (g) over flight time. (Unit 
D4500509) ................................................................................................................................... 8 
Figure 5: Mock-up of Verification testing for reported Fuel Flow inaccuracy. ................................. 10 
Figure 6: Actual Test Setup: Lower Left - Lab Calibrated Mass Flow Sensor, Center - Fuel Cell 
D4500509, Right - Tank with Regulator on Scale. ......................................................................... 10 
Figure 7: Results of "Fuel Sweep" test on unit D4500509. Seeing peak error of 10.9% on fuel 
accuracy. .................................................................................................................................. 11 
Figure 8: Results of "Fuel Sweep" test on unit D4500510. Seeing peak error of 16% on fuel accuracy.
 ................................................................................................................................................. 11 
Figure 9: Proper Plumbing of Fuel System. .................................................................................. 12 
Figure 10: Plumbing on D4500509. ............................................................................................. 12 
Figure 11: Post Re-calibration of unit D4500509, showing flow accuracy throughout test no greater 
than 2.0%. ................................................................................................................................. 13 
Figure 12: Post Re-calibration of unit D4500510, flow accuracy within 2% throughout all flow rates.
 ................................................................................................................................................. 14 
Figure 13: Tank Mass after filling prior to test (1234.7g) ................................................................ 16 
Figure 14: Empty Tank Mass (315.6g) .......................................................................................... 16 
Figure 15: Test Setup (D4500509) ............................................................................................... 16 
Figure 16: Pre & Post Test Tank Mass' .......................................................................................... 17 
Figure 17: Reported Fuel Cell Output of Raw Stack Power & Output Delivered Power (W). ............. 18 
Figure 18: Reported instantaneous fuel flow in SLPM & to FC calculated fuel burned in g/hr. ........ 18

## Page 4

Investigation Summary:  (Fuel Cell Flameout in Flight) 
 
02/2025 Edge Autonomy Proprietary Information 4 
2 Introduction and Executive Summary 
2.1 High Level Summary – Updated 2/09/2025. 
On November 13, an aircraft equipped with a fully serviced propane tank and a Tequila baseline 
HD55 payload experienced a fuel cell error after 5.2 hours of flight, despite being on track for a 6.5-
hour endurance. As a result of this error, HLB had insufficient power to perform primary landing 
plan, prompting an ELZ glide landing. Post-flight analysis revealed the fuel tank was empty, 
although the software indicated one hour of fuel remaining. 
On November 14, the same aircraft, with a different fuel tank and components, encountered a 
similar issue after approximately six hours of flight. The fuel cell stopped producing power due to 
fuel starvation, despite the software indicating fuel remained. Aircraft continued flight plan without 
indication or response to the fuel cell error. Client recommending the system prioritize fuel cell 
power loss as a critical event and execute an Automatic Low-Energy Return to Base (RTB). 
In response to this error, Energy Systems group launched an investigation into fuel reporting 
accuracy in parallel to VXE Aircraft engineering team exploring the possibility of integration of this 
event response into the active software on the VXE30 aircraft. 
Primary Contributing root cause of the issue has been identified, and a corrective action verified in 
order to address the issue. Inaccuracy due to a manufacturing defect in the fuel cell fuel system 
results in an error in mass flow measurement by fuel cell. This defect is affecting the two units 
addressed within this report, as well as 80 other units currently in the field. Fleetwide Advisory and 
Quality investigation has been initiated to respond to the implications of the issue to the fielded 
products.  
 
2.2 Operator Description of the Incident 
Description provided by LMCO Flight Operator: (Posted in VIT2-500 Description) 
Flight profile was to fly a full endurance fuel cell flight with Tequila baseline HD55 payload.  
On the 13 November flight the aircraft was loaded with a fully serviced propane tank (922g of 
propane). Weight and balance was checked, aircraft weight was 44.7lbs. The aircraft was flown in a 
racetrack pattern. The flight was on track for an estimated 6.5 hrs when at about 5.2 hrs the fuel cell 
indicated an error and was no longer charging the hybrid battery. The HLB was approximately 55% 
and the VTOL control window indicated about 7 min of battery remaining. The fuel cell was 
commanded to stop, and then start was commanded. This did not correct the problem. The hybrid 
battery charge state was a little questionable for a VTOL landing so an uneventful glide landing was 
performed. Post flight it was determined that the cause of the fuel cell error was fuel starvation. The 
fuel tank was empty but the software indicated one hour of fuel remaining.

## Page 5

Investigation Summary:  (Fuel Cell Flameout in Flight) 
 
02/2025 Edge Autonomy Proprietary Information 5 
On the 14 November flight the aircraft was again loaded with a fully serviced propane tank (922g of 
propane). Prior to flight we leaked checked the system (from fuel tank to the fuel cell fitting in the 
nose) with the tank and manifold that was flown the day prior – no leaks detected.  We then leak 
checked using the manifold we were going to fly for the second flight– no leaks detected.  We flew 
the same plane, V732, with a different fuel tank, a different manifold, and different filter, and different 
fuel cell.  At approximately 6:00 into the flight, fuel cell control window indicated ~100 grams of 
propane remaining, and fuel cell control window and GCS telemetry indicated ~45 minutes 
endurance remaining, and the fuel cell stopped producing power.  The fuel cell status in the GCS 
telemetry said ERROR and flashed red.  The aircraft remained on mission.  The aircraft was 
commanded Go to IP4 of the PLZ while the HLB still had plenty of energy for a vertical landing with no 
issues. Post flight it was determined that the cause of the fuel cell error was fuel starvation. The fuel 
tank was empty but the software indicated fuel remaining.  
When the fuel cell stops in flight, or “shuts down” the software will begin non-stop chiming, there’s a 
pop-up that the fuel cell has shutdown inflight, and that the aircraft will automatically RTB for low 
energy. These things did not happen for either flight when the fuel cell quit generating power. On the 
first flight the data will show that those events occurred but that was because we commanded a 
shutdown. 
Without intervention, we believe the plane would have remained on mission until the HLB was at 21 
volts, commanded zero throttle, and glided down to the ground while continuing to navigate the 
mission.  We believe the aircraft should treat a loss of fuel cell power as a “fuel cell has stopped” 
and execute an Automatic Low-Energy RTB. 
 
2.3 Status 
At this time, team has determined the primary root cause, and has demonstrated successful 
implementation of corrective action on one of the two provided units including full endurance 
verification cycle and description of results. D4500509 is to be shipped back to the customer, while 
D4500510 is under continued investigation by AA team.  
 
2.4 Root Cause 
The primary root cause determined to be a manufacturing defect in the fuel routing through a 
directionally sensitive mass flow meter.  While plumbed in the correct flow orientation, the mass 
flow meter is able to accurately report fuel consumed within a 5% error margin.  When fuel is 
plumbed in the incorrect (reverse) direction, the measured fuel flow rate can become inaccurate, 
resulting in the under-reporting of fuel consumed.  The degree of inaccuracy is a function of the 
ambient temperature and fuel temperature at the time of use but is generally 8% to 13% over the -
20°C to 50°C operational range of the D450 . This has serious implications for the aircraft’s 
operation as the endurance estimations can result in up to 150g deficit in the most extreme cases.  
See Section 3.3 of the report for more detailed investigation findings.

## Page 6

Investigation Summary:  (Fuel Cell Flameout in Flight) 
 
02/2025 Edge Autonomy Proprietary Information 6 
Results of this report have triggered the beginning of an ongoing CAR led by the Edge Autonomy 
Quality Department that is to be an ongoing effort to assess and correct this issue fleetwide. This 
report will discuss the corrective action required specifically for these units and serve to provide 
evidence and information for the ongoing CAR. 
2.5 Corrective Actions  
Team has been able to verify correction of issue through defect repair and recalibration of the fuel 
system. This is demonstrated in Section 5 of this report. Both units delivered to Ann Arbor for this 
incident will receive recalibration and retesting to certify conformance to standard outgoing 
specifications and then be returned to the customer.  
At this time, the corrective action is only available onsite at Ann Arbor manufacturing facility; 
however, development is ongoing to prepare a field service alternative for units that have low 
operational hours to be repaired by technician at equipment site or preferred customer location. 
This is intended to address the issue on a fleetwide level and minimize impact to customers. 
Further information regarding options will be provided along with the ongoing CAR.

## Page 7

Investigation Summary:  (Fuel Cell Flameout in Flight) 
 
02/2025 Edge Autonomy Proprietary Information 7 
3 Root Cause Investigation Details 
3.1 VIT2-500 Preliminary Data Review 
Users provided the following to supplement written account: 
AAR Data File FC Serial Number 
T95_V732_241113_073820_pack.zip D4500509 
T95_V732_241114_081728_pack.zip D4500510 
 
Photos of Pre-Flight Fuel Fill Tank Mass’s: 
 
Flight Detail for Fuel Cells: 
Fuel Cell SN: D4500509 HR:MIN:SS Fuel Cell SN: D4500510 HR:MIN:SS 
Warmup 00:13:52 Warmup 00:12:35 
Operate (State Transition-to-Fault) 06:03:28 Operate (State Transition-to-Fault) 05:29:49 
Cooldown N/A Cooldown 00:16:14 
 
Figure 2: IMG_2825 Tare Mass of Tank prior 
to fill procedure(299g). 
Figure 1: IMG_2821 Full Tank Following Liquid 
Propane Fill (1220g).

## Page 8

Investigation Summary:  (Fuel Cell Flameout in Flight) 
 
02/2025 Edge Autonomy Proprietary Information 8 
 For Flight completed with unit D4500509, fuel flow ranged from 0.51LPM to 1.81LPM with an 
average flow rate of 1.14LPM. Given a 1.14LPM average flow, the calculated fuel burn would be 
124.9g/hr of fuel. This burn with a 922g fuel reserve would yield an estimated endurance of 7.38hrs. 
Calculated error from the actual burned fuel results in an approximate error of burn rate of 10.8%.  
Throughout the duration of this flight, the fuel flow ranged from 0.66LPM to 1.83LPM with an 
average flow of 1.22LPM. At 1.22LPM, the calculated fuel burn would be approximately 133.7g/hr of 
fuel and result in an estimated endurance with a full 922g tank of 6.9hrs. Calculated error on this 
flight was estimated to be 13.3%. 
Figure 3: Chart displaying Fuel Flow (LPM) & Estimated Fuel Burn (g) over flight time. (Unit D4500510) 
Figure 4: Chart displaying Fuel Flow (LPM) & Estimated Fuel Burn (g) over flight time. (Unit D4500509)

## Page 9

Investigation Summary:  (Fuel Cell Flameout in Flight) 
 
02/2025 Edge Autonomy Proprietary Information 9 
Data provided confirms fuel cells are exhibiting extremely abnormal behavior consistent with a 
significant variation between the calculated endurance and the actual observed endurance of the 
unit. Request submitted for the return of both units for investigation. 
 
3.2 Incoming Failure Analysis 
All investigations contributing to the verification of the reported behavior and initial investigation 
into the root cause of failure. To mitigate risks associated with excessive fueling, additional 
investigation is to be performed on the root cause prior to operational study of these fuel cells. In a 
later draft of the report, additional findings on the incoming health of the fuel cells can be shared.  
 
3.2.1 Incoming Physical Inspection 
Upon receipt of the system, the RMA & Quality team performed a standard incoming inspection to 
verify paperwork and note any visual indications of physical damage to the unit. This included the 
following items: 
• Inspection of Case and Physical Unit Hardware. 
• Power-up of Main Controller and collection of Incoming Calibration Parameters. 
Both D4500509 & D4500510 did not display any obvious indications of damage and were handed 
over to engineering for evaluation of prior to the standard incoming operational test due to the 
nature of the reported failure. Given potential for fuel leak or misreporting of fuel, engineering 
requested for performance of failure specific Balance of Plant testing. 
 
3.2.2 Fuel System Leak Check 
Due to the use of two different fuel cells and the replacement of the entire fuel system between 
tests, this cause was not determined to be likely, however testing was still performed to eliminate 
risk of flawed data. This test consisted of a pressurized tank with an opened regulator connected to 
the fuel cell and left for one hour to identify any loss of mass in the tank. 
For both units, change in the mass measured by the tank was not detectable by scale with 
accuracy of ±2g. Eliminating the likelihood of leaks resulting in the error observed through testing. 
 
3.2.3 Fuel Flow Sweep 
Based on customer findings, initial testing was performed intended to verify fuel reporting accuracy 
by use of calibrated standard OMEGA Mass Flow Sensor and Tank with Scale.

## Page 10

Investigation Summary:  (Fuel Cell Flameout in Flight) 
 
02/2025 Edge Autonomy Proprietary Information 10 
Test Setup: 
 
Setup required removal of protective plastics and isolation of the fuel system, downstream is a 
Mass Flow Sensor measuring the outgoing flow of the fuel cell and upstream is tank with a scale to 
measure the mass change to verify the flow. 
Method: 
Performance of the test consisted of directing Fuel Cell to flow at 0.5LPM for 30s and increasing 
flow at 0.5LPM intervals, observing the 30s stabilization period, and repeating until the top end of 
the fuel flow range 2.0LPM.  
This is to be performed while data is being recorded from both the Fuel Cell Data Stream and 
Omega Mass Flow Sensor at 1.0s timestep intervals. 
Figure 5: Mock-up of Verification testing for reported Fuel Flow inaccuracy. 
Figure 6: Actual Test Setup: Lower Left - Lab Calibrated Mass Flow Sensor, Center - Fuel Cell 
D4500509, Right - Tank with Regulator on Scale.

## Page 11

Investigation Summary:  (Fuel Cell Flameout in Flight) 
 
02/2025 Edge Autonomy Proprietary Information 11 
Results:  
Upon performance of the test, both systems exhibited errors greater than 10% in the measurement 
of the FC internal fuel system against the standard measurements. Assessment of fuel flow 
performance of the isolated fuel system yielded results consistent with customer findings. 
 
Figure 7: Results of "Fuel Sweep" test on unit D4500509. Seeing peak error of 10.9% on fuel accuracy. 
 
Figure 8: Results of "Fuel Sweep" test on unit D4500510. Seeing peak error of 16% on fuel accuracy. 
-0.05
0.05
0.15
0.25
0.35
0.45
0
0.5
1
1.5
2
2.5
3
% Error
Fuel Flow (SLPM)
D4500509 Incoming Measurement Error
FC Measured FuelFlow (SLPM) Standard Mflow (SLPM) % Error
-0.05
0.05
0.15
0.25
0.35
0.45
0
0.5
1
1.5
2
2.5
3
% Error
Fuel Flow (SLPM)
D4500510 Incoming Measurement Error
FC Measured FuelFlow (SLPM) Standard Mflow (SLPM) % Error

## Page 12

Investigation Summary:  (Fuel Cell Flameout in Flight) 
 
02/2025 Edge Autonomy Proprietary Information 12 
In the nominal operational range of the fuel cell during flight as calculated to be approximately 
1.2LPM, the results of this test point to a conclusive result relating inaccuracy in fuel burn observed 
in the field consistent with the error exhibited in the accuracy testing. 
 
3.3 Teardown of System 
System’s D4500509 & D4500510 delivered initially August 2023, are among known 80 units 
affected by manufacturing defect from early production that affected the plumbing of the fuel 
system resulting in reverse flow calibrations during testing.  
The secondary calibration of these units, and study of the impact to calibration and lab testing 
once discovered, led engineering team to determine that use of these units was not a functional 
risk to the fuel cell. Internal Mass Flow Sensor accuracy requirement of <5% error was still met by 
the defective units, and repeatability of these values were verified. However, additional verification 
due to the identificaiton of significant error in these two returned units is to be performed to further 
understand risks and develop corrective actions. 
 
3.4 Conclusion of Root Cause 
Based on findings from the sweep of fuel flow and its consistency with the observations from the 
preliminary data provided with the ticket, it is determined that the primary contributing root cause 
is the lack of accuracy of the mass flow measurement performed by the fuel cell internal sensor. 
This inaccuracy is suspected to be the result of the calibration defect (reverse calibration); 
however, the root cause and total scope of this inaccuracy is still to be determined through a larger 
investigation into fuel accuracy.  
This conclusion results in the quarantine of all affected units to be reported in upcoming fleetwide 
advisory notice. Until true root cause is determined, containment effort aims to limit risks out of an 
abundance of caution to the users and equipment in the field. Advisement on the mitigation and 
repair options for fleetwide affected systems to be provided as soon as more information is 
available.  
  
Figure 9: Proper Plumbing of Fuel 
System. 
Figure 10: Plumbing on D4500509.

## Page 13

Investigation Summary:  (Fuel Cell Flameout in Flight) 
 
02/2025 Edge Autonomy Proprietary Information 13 
4 Corrective Action Development Study 
Characterization of Corrective Action development is summarized below. 
4.1 Overview of Corrective Actions 
D4500509 & D4500510 displayed 10.8% and 13.3% Fuel Error respectively. In evaluation of root 
cause, until continued study is performed on the effects of the previously identified defect with UAI 
disposition the primary suggested corrective action is correction of the defect and recalibration of 
the unit. For guaranteed correction of the issue, the probable result is to correct the defect and re-
calibrate the fuel flow sensor.  
 
4.1.1 Correction of Flow Direction & Re-calibration 
To verify the success of the recalibration, the fuel sweep testing is repeated following the same 
procedure as noted above in section 3.2.3. Both D4500509 and D4500510 were disassembled, 
repaired, and recalibrated with the production tools used during assembly. Their results confirmed 
<5% error through all flow setpoints. 
Results:  
Throughout the verification testing, the units were monitored for their accuracy using Calibrated 
Omega Mass Flow Sensor as standard. Each flow point was commanded for approximately 
1minute through the full range of operational flow for D450 fuel cell (0.5LPM – 1.9LPM). 
-0.05
0
0.05
0.1
0.15
0.2
0.25
0
0.5
1
1.5
2
2.5
3
% Error
Fuel Flow (SLPM)
D4500509 Post-Calibration Fuel Measurement
FC Measured Fuel Flow (SLPM) Standard Mflow (SLPM) % Error
Figure 11: Post Re-calibration of unit D4500509, showing flow accuracy throughout test no greater than 2.0%.

## Page 14

Investigation Summary:  (Fuel Cell Flameout in Flight) 
 
02/2025 Edge Autonomy Proprietary Information 14 
 
Figure 12: Post Re-calibration of unit D4500510, flow accuracy within 2% throughout all flow rates. 
Both unit D4500509 & D4500510 flow accuracy improved to within the acceptable threshold of 
error <5% upon calibration. Successful calibration is now to be verified through operational testing 
of the fuel cell units.  
 
4.2 Risks to System Health 
At this time, the team is performing additional verification to determine the risks to the health of the 
fuel cell system subjected to excessive fuel flow. Known behavior of fuel cells operating with 
excessive fuel includes the potential for carbon deposition near internal catalytic reactors that 
could cause damage to the cell’s electrolyte layer and thereby reduce performance of the unit. The 
effects of this phenomenon depend heavily on the duration of operation in fuel-rich conditions and 
the magnitude of the fuel measurement accuracy.  
Units provided within this ticket once corrected, will be tested operationally to verify their health. 
Based on results, units will receive any maintenance / repair that is deemed necessary in order to 
bring equipment back to full function including the replacement of the fuel cell stack should that 
be deemed necessary.  
 
  
-0.05
0.05
0.15
0.25
0.35
0.45
0
0.5
1
1.5
2
2.5
3
% Error
Fuel Flow (SLPM)
D4500510 Post-Calibration Fuel Measurement
FC Measured FuelFlow (SLPM) Standard Mflow (SLPM) % Error

## Page 15

Investigation Summary:  (Fuel Cell Flameout in Flight) 
 
02/2025 Edge Autonomy Proprietary Information 15 
5 Verification of Corrective Action 
Following implementation of corrective action, each unit was re-assembled and verification testing 
performed. The observations of this testing are discussed in this section. 
5.1 D4500509 Verification Testing 
 
5.1.1 Incoming Operational Cycle 
Upon implementation of corrective action, D4500509 is subjected to test to simulate standard 
RMA return analysis. Consisting of “Top-up” request to warm-up and produce nominal 450W 
output. This test is to evaluate health of stack and system prior to return to customer. Fuel Cell 
Data log identified this unit to have 28.2 operational hours on the stack upon receipt in Ann Arbor.  
Shortly into the unit’s operation, stack exhibits behavior consistent with stack failure including 
inability to produce 450W, and low stack voltage.  
This behavior constitutes suspension of the test to preserve any useful data in the discovery of 
failure root cause. This investigation is ongoing by Fuel Cell Senior Scientist, more information will 
be shared as it becomes available. In the meantime, it is confirmed that the system should be re-
stacked to return to customer. Due to the failure of Stack on D4500509, system was re-stacked 
and performed burn-in and outgoing performance test. Standard outgoing certification of 
conformance data collected on new stack, and provided along with new unit. 
 
5.1.2 Fuel Accuracy Endurance Verification Cycle 
In order to verify accuracy of fuel burn throughout full duration flight cycle, the following laboratory 
experiment was conducted. This consisted of a full fuel tank, calibrated scale, single use filter, and 
laboratory test stand with power supply, load, and fuel cell diagnostic software.

## Page 16

Investigation Summary:  (Fuel Cell Flameout in Flight) 
 
02/2025 Edge Autonomy Proprietary Information 16 
Test Setup: 
Standard 2.2L Fuel Tank filled completely from empty tare mass of 316g to suggested 1234g 
totaling in 919g in the tank: 
Fuel Cell Setup on test stand with single use filter and standard regulator: 
Figure 13: Tank Mass after filling prior to test (1234.7g)  
Figure 15: Test Setup (D4500509) 
Figure 14: Empty Tank Mass (315.6g)

## Page 17

Investigation Summary:  (Fuel Cell Flameout in Flight) 
 
02/2025 Edge Autonomy Proprietary Information 17 
Method: 
Test designed to simulate energy requirement profile exhibited during the initial endurance flight 
where incident occurred. This flight profile exhibited standard warmup and operate transition, then 
450W operation for approximately 5min in order to recharge the HLB, and finally a profile consisting 
of an average power need of 375W throughout the remainder of the test.  
Test data is to be recorded at a 1.0s timestep interval throughout duration and include occasional 
record of reported mass of the scale for verification of accuracy from fuel cell.  
 
Results: 
Testing begins at 07:33 initiating fuel cell startup with a scale mass of 1311.7 (77g added due to 
regulator & associated fuel lines and harness) and completed cooldown at 15:25 with a scale mass 
of 403.1. The deficit from the scale 901.2g and calculated burn from the fuel cell of 926.0g. The 
error % from this test is approximately 2.7%, which is within acceptable accuracy tolerance and 
significantly reduced from error observed in flight incident.   
Flight summary shown below: 
Fuel Cell SN: D4500509 HR:MIN:SS 
Warmup 00:19:49 
Operate 07:24:13 
Cooldown 00:08:48 
Figure 16: Pre & Post Test Tank Mass'

## Page 18

Investigation Summary:  (Fuel Cell Flameout in Flight) 
 
02/2025 Edge Autonomy Proprietary Information 18 
 
Figure 17: Reported Fuel Cell Output of Raw Stack Power & Output Delivered Power (W). 
 
Figure 18: Reported instantaneous fuel flow in SLPM & to FC calculated fuel burned in g/hr. 
Throughout test, the system operated at approximately 1.1LPM flow, with estimated burn rate of 
120.5g/hr, consistent with the average fuel flow requested during flight cited in the incident. In this 
case, expected endurance was achieved and error was reduced from 10.8% to 2.7%. 
System will be prepared for shipping and returned to customer for any additional validation. 
-50.0
50.0
150.0
250.0
350.0
450.0
550.0
7:32:35 AM
7:45:52 AM
7:59:09 AM
8:12:26 AM
8:25:43 AM
8:39:02 AM
8:52:19 AM
9:05:36 AM
9:18:53 AM
9:32:10 AM
9:45:27 AM
9:58:44 AM
10:12:01 AM
10:25:18 AM
10:38:35 AM
10:51:52 AM
11:05:09 AM
11:18:26 AM
11:31:43 AM
11:45:00 AM
11:58:17 AM
12:11:34 PM
12:24:51 PM
12:38:08 PM
12:51:25 PM
1:04:42 PM
1:17:59 PM
1:31:16 PM
1:44:33 PM
1:57:50 PM
2:11:07 PM
2:24:24 PM
2:37:41 PM
2:50:58 PM
3:04:15 PM
3:17:32 PM
Power (W)
Power Output During Test 
Stack (Raw) Power Output FC Output Power (Delivered)
0
100
200
300
400
500
600
700
800
900
1000
0
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
1.8
2
7:32:35 AM
7:42:35 AM
7:52:35 AM
8:02:35 AM
8:12:35 AM
8:22:35 AM
8:32:37 AM
8:42:37 AM
8:52:37 AM
9:02:37 AM
9:12:37 AM
9:22:37 AM
9:32:37 AM
9:42:37 AM
9:52:37 AM
10:02:37 AM
10:12:37 AM
10:22:37 AM
10:32:37 AM
10:42:37 AM
10:52:37 AM
11:02:37 AM
11:12:37 AM
11:22:37 AM
11:32:37 AM
11:42:37 AM
11:52:37 AM
12:02:37 PM
12:12:37 PM
12:22:37 PM
12:32:37 PM
12:42:37 PM
12:52:37 PM
1:02:37 PM
1:12:37 PM
1:22:37 PM
1:32:37 PM
1:42:37 PM
1:52:37 PM
2:02:37 PM
2:12:37 PM
2:22:37 PM
2:32:37 PM
2:42:37 PM
2:52:37 PM
3:02:37 PM
3:12:37 PM
3:22:37 PM
Fuel Burned (g/hr)
Fuel Flow (SLPM)
Fuel Flow & Calc Burned
FC Measured FuelFlow (SLPM) Fuel Cell Calculated Burn (g/hr)

## Page 19

Investigation Summary:  (Fuel Cell Flameout in Flight) 
 
02/2025 Edge Autonomy Proprietary Information 19 
5.2 D4500510 Verification Testing 
Upon completion of repair to D4500510, stack will perform similar testing and be returned. At this 
time, the system is still undergoing re-assembly and will be subjected to standard outgoing QC 
testing prior to return in order to verify health and accuracy of fuel approximations. Certificate of 
Conformance will be supplied and updated version of this report will be generated.
