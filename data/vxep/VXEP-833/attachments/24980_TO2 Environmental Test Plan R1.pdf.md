# TO2 Environmental Test Plan R1.pdf

Attachment 24980, pdf, 1621 KB, added 2024-12-12 by Ryan Babigian.

## Page 1

TO2 Environmental Test Plan 
 
Document Number: 111-24810 
 
Revision: A 
 
Release Date: 12/09/2024 
 
 
 
 
 
 
 
  CONFIDENTIAL AND PROPRIETARY DATA: 
Portions of this document contain proprietary technical data pertaining to items, or 
components, or processes, or other matter developed or acquired at the private expense of 
Edge Autonomy and is restricted to use only by Edge Autonomy employees or other persons 
authorized by Edge Autonomy in writing to use it. Neither said document nor said technical 
data shall be furnished or disclosed to, or copied or used by, persons outside Edge Autonomy, 
without the express written approval of Edge Autonomy. Markings on this page regarding 
confidentiality and proprietary information apply to this entire document. 
 
EXPORT CONTROL WARNING NOTICE: 
WARNING – this document may contain technical data whose export is restricted by the Arms 
Export Control Act (Title 22, U.S.C. Sec 2751 et seq) or the Export Administration Act of 
1979 (Title 50, U.S.C., App. 2401, et seq) as amended.  Violations of these export laws are 
subject to severe criminal penalties.  Disseminate in accordance with provisions of DoD 
Directive 5230.25.   Contains Export Controlled Information Not releasable to Foreign Persons 
unless authorized by 22 C.F.R. 120-130 or 15.C.F.R. 730-774.

## Page 2

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 2 
 
 
Approval Sheet 
 
 
 
 
Doug Baker, Senior Director of Programs 
Edge Autonomy 
 
Date 
Greg Fryer, Director of Products - VXE30 
Edge Autonomy 
Date 
Ryan Babigian, Staff Project Engineer 
Edge Autonomy 
 
Date 
Dhruti Shah, Senior Systems Engineer 
Lockheed Martin UK 
Date 
John Mackoway III, Supplier Manager 
Lockheed Martin Corporation 
 
Date

## Page 3

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 3 
 
 
Table of Contents 
1 Introduction ............................................................................................................................. 5 
1.1 Purpose ............................................................................................................................ 5 
1.2 Scope ............................................................................................................................... 5 
1.3 Test Approach ................................................................................................................. 6 
2 Test Objectives...................................................................................................................... 11 
2.1.1 High Temperature – Operational .......................................................................... 11 
2.1.2 Low Temperature – Operational ........................................................................... 13 
2.1.3 Temperature Shock ............................................................................................... 15 
2.1.4 Humidity ............................................................................................................... 17 
2.1.5 Solar Radiation...................................................................................................... 19 
2.1.6 Dust ....................................................................................................................... 21 
2.1.7 Sand....................................................................................................................... 23 
2.1.8 Waterproof Rain.................................................................................................... 25 
3 Acronyms .............................................................................................................................. 27 
4 Appendix A – Operational Checkout Procedure .................................................................. 28

## Page 4

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 4 
 
 
List of Figures 
Figure 1 TO2 Transit Case Details ................................................................................................. 7 
Figure 2 Full Aircraft and UUT Supported by Aircraft Stand ........................................................ 8 
Figure 3 UTT Thermocouple Placement ........................................................................................ 9 
Figure 4 Test Logic ....................................................................................................................... 10 
Figure 5 MIL-STD-810H Solar Radiation Procedure I Cycling Test........................................... 21 
 
List of Tables 
Table 1-1 TO2 Environmental Tests and Locations ....................................................................... 6 
Table 2-1 Test Procedure: MIL-STD-810H High Temperature ................................................... 12 
Table 2-2 Test Procedure: MIL-STD-810H Low Temperature .................................................... 14 
Table 2-3 Test Procedure: MIL-STD-810H Temperature Shock – Low ...................................... 16 
Table 2-4 Test Procedure: MIL-STD-810H Temperature Shock – High ..................................... 16 
Table 2-5 Test Procedure: MIL-STD-810H Humidity (Tailored) ................................................ 18 
Table 2-6 Test Procedure: MIL-STD-810H Solar Radiation ....................................................... 20 
Table 2-7 Test Procedure: MIL-STD-810H Dust ......................................................................... 22 
Table 2-8 Test Procedure: MIL-STD-810H Sand ........................................................................ 24 
Table 2-9 Test Procedure: MIL-STD-810H Rain ......................................................................... 25

## Page 5

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 5 
 
 
1 Introduction 
1.1 Purpose 
This document describes Edge Autonomy’s environmental test plan for the Task Order 2 (TO2) 
VXE30 Pre-MAGNSS Stalker aircraft in accordance with Military Standard (MIL-STD) 810H. 
The TO2 aircraft configuration, when compared to the standard VXE30 aircraft, incorporates a 
new redesigned Avionics Enclosure and associated electrical interconnect cables. The TO2 
Avionics Enclosure contains a new Mission Compute Module (MCM) and UBLOX8 GPS 
Receiver connected to an L1 antenna, in addition to the standard XCOMM and Fixed-Wing 
AutoPilot (FWAP) electronics found in the standard VXE30 Avionics. 
Environmental testing of the standard VXE30 was previously conducted under a separate effort. 
The purpose of the current testing is to collect environmental test data for the TO2 aircraft 
configuration and to compare those data with the results obtained from the standard VXE30 
environmental testing. Due to several test constraints – including available internal volume of the 
test chambers – the primary Unit Under Test (UUT) for most of the testing will be an 
abbreviated TO2 aircraft assembly, consisting of the fuselage (with new Avionics Enclosure 
installed) and Centerwing. For these tests, the remaining unassembled aircraft components will 
be subject to the same test conditions, i.e. temperature, as the UUT but will not be electrically 
connected to the UUT, instrumented, or monitored during testing. 
1.2 Scope 
The scope of the TO2 MIL-STD-810H environmental testing covers temperature, shock, 
humidity, solar radiation, dust, sand, and rain testing. Two (2) separate test facilities were 
selected for the environmental testing: Experior, located in Oxnard, CA, and Element, located in 
Huntsville, AL. The two (2) test facilities were selected based on several factors including 
availability, cost, test chamber size, and capability to conduct the requested environmental 
testing. Table 1-1 lists each test type and the test facility where the test is planned to be 
performed. 
The Experior test facility was selected to perform MIL-STD-810H Temperature, Shock, and 
Humidity testing. Experior personnel will be responsible for test scheduling, handling and 
transport of the UUT within the test facility, preparation of the UUT including installing required 
test instrumentation, operation of the test chambers, and data acquisition. Within two (2) weeks 
of test completion, Experior will furnish a test report to Edge Autonomy that contains the results 
of the environmental testing performed. The remainder of the MIL-STD-810H environmental 
tests will be conducted at the Element test facility. 
The Element test facility is responsible for performing Solar Radiation, Dust, Sand, and 
Waterproof Rain environmental testing. Element personnel will be responsible for test

## Page 6

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 6 
 
 
scheduling, handling and transport of the UUT within the facility, and operation of the test 
chambers, and data acquisition. The scope of the environmental testing at Element does not 
require that the UUT be instrumented during testing. Within two (2) weeks of test completion, 
Element will furnish a test report to Edge Autonomy that contains the results of the 
environmental testing performed. 
Table 1-1 TO2 Environmental Tests and Locations 
Test Name UUT Chamber Size 
(L x W x H) 
Test 
Facility 
High Temperature - Operational 
Fuselage with 
Avionics 
Enclosure & 
Centerwing 
9' x 4.5' x 5.5' 
Experior 
Low Temperature - Operational 9' x 4.5' x 5.5' 
Shock 9' x 4.5' x 5.5' 
10' x 11' x 8' 
Humidity 6' x 6' x 7' 
Solar Radiation 
Full Aircraft 
18' x 32' x 18' 
Element Dust 37' x 14' x 11’ 
Sand 37' x 14' x 11’ 
Waterproof Rain 20' x 20' x 20' 
 
To accommodate environmental testing at two different locations, a total of two (2) TO2 aircraft 
will be used for testing. One (1) aircraft will be shipped to each location prior to the start of 
testing. The two (2) aircraft that will undergo environmental testing will be provided through 
bailment by Lockheed Martin United Kingdom (LMUK) to Edge Autonomy. In addition to the 
two (2) aircraft, LMUK will also provide quantity two (2) Trillium gimbal payloads that will be 
installed on each of the aircraft during testing. 
Depending on the type of environmental testing being performed, the UUT will be instrumented 
with thermocouples (TCs) to collect temperature data during the tests. All testing will be 
conducted by test facility personnel with the direct support from a member of the Edge 
Autonomy Flight Operations (FLOPs) team. 
1.3 Test Approach 
Quantity one (1) TO2 aircraft shipset and quantity one (1) Trillium gimbal payload assembly will 
be provided to each test facility prior to the start of testing. The TO2 aircraft shipset is comprised 
of two (2) transit cases: one (1) case contains the fuselage, tailboom, and stabilizers and one (1) 
case contains the centerwing and wingtips. Figure 1 shows a depiction of the transit case along 
with dimensions.

## Page 7

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 7 
 
 
 
Figure 1 TO2 Transit Case Details 
For environmental tests that require the abbreviated UUT, the transit cases containing the 
remainder of the aircraft components may be placed inside the test chamber along with the UUT. 
Otherwise, the aircraft components will be removed from the transit cases and placed inside the 
test chamber. At all times, care must be taken not to damage the exterior finish of the UUT or 
related aircraft components. A collapsable aircraft stand is provided in each fuselage transit case. 
This stand can be used to support both the full aircraft as well as the UUT during environmental 
testing. The stand with UUT can also be placed onto a rolling cart for transport within the test 
facility. Figure 2 shows both the full aircraft and UUT supported by the aircraft stand.

## Page 8

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 8 
 
 
 
Figure 2 Full Aircraft and UUT Supported by Aircraft Stand 
The assembly of the test article, whether UUT or full aircraft, will be performed by Edge FLOPs 
personnel. Instrumentation of the UUT will be performed by the test house. Edge Autonomy will 
provide placement locations for the TCs that will be used for MIL-STD-810H thermal testing. 
For environmental testing at Experior – which includes Temperature, Shock, and Humidity 
testing – the UUT will be instrumented with TCs that are used to collect temperature data. TCs 
will be affixed to the UUT at several external locations. These locations were selected based on 
direction from LMUK. Figure 3 identifies the locations where the TCs are to be installed.

## Page 9

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 9 
 
 
 
Figure 3 UTT Thermocouple Placement 
A total of five (5) TCs will be installed on the UUT: One (1) near the Antenna cover on the TO2 
Avionics Enclosure; one (1) on the heat fins of the Avionics Enclosure; one (1) on the 
centerwing near the Vertical Takeoff and Landing (VTOL) button one (1) near the Air Data Pod 
(ADP) heatsink; and one (1) on the front of the Silvus radio. These TCs will be used to 
continuously collect thermal data throughout the environmental thermal (High/Low 
Temperature, Shock, and Humidity) testing. 
Operational High and Low Temperature testing will be conducted with the UUT powered on. 
The UUT will be powered by a 28VDC, 5A power supply or similar. Positive and negative cable 
leads with banana terminations will connect the power supply to the aircraft main power cable. 
The aircraft batteries will not be used as a power supply for any environmental testing due to the 
planned duration of each test being greater than the battery discharge time, as well as the amount 
of time required between tests to recharge an aircraft battery. 
 Prior to each test performed, regardless of test type or facility, the aircraft will undergo an 
operational check to ensure that the UUT was not damaged in the previous test and is ready for 
further testing. The operational check will be performed by Edge Autonomy FLOPs technicians 
using a GCS laptop with an ethernet cable connected between the laptop and UUT. The 
procedures for the operational check are presented in Appendix A of this test plan. 
The test cycle logic prescribed in MIL-STD-810H Section 5.11.2 will be used both during testing 
as well as for pre-test operational checkouts for in-tolerance or out-of-tolerance failures. Figure 4

## Page 10

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 10 
 
 
shows the test cycle logic that will be used during environmental testing. The Edge Autonomy 
Project Engineer will be responsible for determining if a particular failure is considered in-
tolerance or out-of-tolerance.  
 
Figure 4 Test Logic 
If the UUT or subcomponent thereof experiences an in-tolerance failure, then testing will 
continue. If the UUT or subcomponent experiences an out-of-tolerance failure, then the test 
duration will be reduced in order to complete as much of the test as possible without damaging 
the UUT. If the UUT is damaged as a result of an out-of-tolerance failure, then the UUT or

## Page 11

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 11 
 
 
subcomponent will be repaired or replaced and testing will continue under planned test 
conditions. 
2 Test Objectives 
This section describes the test objectives for the TO2 MIL-STD-810H environmental testing. 
Each of the test objectives presented in this section contain details on the UUT, test limitations, 
pre-test requirements, test procedures, and post-test actions. 
2.1.1 High Temperature – Operational 
Purpose 
Use high temperature tests to obtain data to characterize TO2 aircraft safety, integrity, and 
performance under high temperature conditions. High Temperature testing will be performed to 
50ºC which represents the TO2 aircraft operational high temperature limit.  
Required Equipment 
• TO2 Aircraft (P/N 127-117680), qty 1 (two transit cases) 
• Main Battery (P/N 107-101050), qty 1 
• GCS Laptop, qty 1 
• Ethernet cable, qty 1 (6ft or as required) 
• Trillium payload, qty 1 
• Adhesive tape, qty 1 (10ft or as required) 
Limitations 
Due to the limited internal volume of the test chamber, an abbreviated UUT will be used for 
testing. 
Test Method 
MIL-STD-810H, Method 501.7 High Temperature – Procedure II 
UUT Configuration 
The UUT for this test will be the TO2 aircraft fuselage with Avionics Enclosure installed and 
connected, centerwing installed and connected, Main Battery installed and connected, and 
Trillium installed and connected. Other TO2 aircraft components including the tailboom, 
horizontal and vertical stabilizers, wingtips, and lift booms shall be placed inside the chamber 
along with the UUT, unconnected.

## Page 12

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 12 
 
 
All openings that would otherwise not be exposed with an assembled aircraft, e.g. centerwing 
tips, must be covered with tape to prevent ingress of external elements including moisture and 
debris. 
All unconnected electrical connectors should be covered with dustcaps or tape to prevent ingress 
of external elements including moisture and debris. 
Pre-Test 
Facility test personnel shall ensure that the TCs are installed on the aircraft per section 1.3 of this 
test plan. Pre-test TC measurement reading should be collected to capture the baseline 
temperature environment of the test chamber and to verify that the instrumentation is working 
normally. 
FLOPs technicians must record part and serial numbers of UUT and related components. 
Photos and video must be collected capturing the test setup including test articles, TC locations, 
and the test chamber. 
Test Procedure 
Table 2-1 Test Procedure: MIL-STD-810H High Temperature 
Step Procedure Responsibility 
Step 1 Place the UUT with TCs installed and other aircraft 
components inside the test chamber. Facility Technician 
Step 2 Position the GCS Laptop outside of the test chamber. Connect 
an ethernet cable from the GCS laptop to the UUT. FLOPs Technician 
Step 3 Power ON the UUT and establish an ethernet data connection 
between the GCS laptop and the UUT. FLOPs Technician 
Step 4 Adjust the chamber air conditions to the required temperature 
of 50ºC not to exceed 3°C/min (5°F/min). Facility Technician 
Step 5 
Allow the UUT temperature to stabilize. Use the TC reading 
from the Avionics Enclosure to verify UUT temperature 
stabilization. Maintain the test chamber conditions for 120 min 
following UUT temperature stabilization. If the test item fails 
to operate as intended, follow the guidance in Figure 4 for test 
item failure. 
Facility Technician 
FLOPs Technician 
Step 6 
Power OFF the UUT and adjust the chamber air temperature to 
20ºC and maintain until the test item temperature has 
stabilized. 
Facility Technician 
FLOPs Technician 
Step 7 
Conduct a complete visual examination and operational 
checkout (see Appendix A) and document the results for 
comparison with pretest data. 
FLOPs Technician 
Post-Test

## Page 13

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 13 
 
 
Verify that all test data have been acquired and stored. Shut down test chamber and prepare 
chamber for next test. 
Collect photos and videos of test environment if not already completed. Document any 
issues/failures encountered during testing. 
2.1.2 Low Temperature – Operational 
Purpose 
Use low temperature tests to obtain data to characterize TO2 aircraft safety, integrity, and 
performance under low temperature conditions. Low Temperature testing will be performed to -
20ºC which represents the TO2 aircraft operational low temperature limit.  
Required Equipment 
• TO2 Aircraft (P/N 127-117680), qty 1 (two transit cases) 
• Main Battery (P/N 107-101050), qty 1 
• GCS Laptop, qty 1 
• Ethernet cable, qty 1 (6ft or as required) 
• Trillium payload, qty 1 
• Adhesive tape, qty 1 (10ft or as required) 
Limitations 
Due to the limited internal volume of the test chamber, an abbreviated UUT will be used for 
testing. 
Test Method 
MIL-STD-810H, Method 502.7 Low Temperature – Procedure II 
UUT Configuration 
The UUT for this test will be the TO2 aircraft fuselage with Avionics Enclosure installed and 
connected, centerwing installed and connected, Main Battery installed and connected, and 
Trillium installed and connected. Other TO2 aircraft components including the tailboom, 
horizontal and vertical stabilizers, wingtips, and lift booms shall be placed inside the chamber 
along with the UUT, unconnected. 
All openings that would otherwise not be exposed with an assembled aircraft, e.g. centerwing 
tips, must be covered with tape to prevent ingress of external elements including moisture and 
debris. 
All unconnected electrical connectors should be covered with dustcaps or tape to prevent ingress 
of external elements including moisture and debris.

## Page 14

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 14 
 
 
Pre-Test 
Facility test personnel shall ensure that the TCs are installed on the aircraft per section 1.3 of this 
test plan. Pre-test TC measurement reading should be collected to capture the baseline 
temperature environment of the test chamber and to verify that the instrumentation is working 
normally. 
FLOPs technicians must record part and serial numbers of UUT and related components. 
Photos and video must be collected capturing the test setup including test articles, TC locations, 
and the test chamber. 
Test Procedure 
Table 2-2 Test Procedure: MIL-STD-810H Low Temperature 
Step Procedure Responsibility 
Step 1 Place the UUT with TCs installed and other aircraft 
components inside the test chamber. Facility Technician 
Step 2 Position the GCS Laptop outside of the test chamber. Connect 
an ethernet cable from the GCS laptop to the UUT. FLOPs Technician 
Step 3 Power ON the UUT and establish an ethernet data connection 
between the GCS laptop and the UUT. FLOPs Technician 
Step 4 Adjust the chamber air conditions to the required temperature 
of -20ºC not to exceed 3°C/min (5°F/min). Facility Technician 
Step 5 
Allow the UUT temperature to stabilize. Use the TC reading 
from the Avionics Enclosure to verify UUT temperature 
stabilization. Maintain the test chamber conditions for 120 min 
following UUT temperature stabilization. If the test item fails 
to operate as intended, follow the guidance in Figure 4 for test 
item failure. 
Facility Technician 
FLOPs Technician 
Step 6 
Power OFF the UUT and adjust the chamber air temperature to 
20ºC and maintain until the test item temperature has 
stabilized. 
Facility Technician 
FLOPs Technician 
Step 7 
Conduct a complete visual examination and operational 
checkout (see Appendix A) and document the results for 
comparison with pretest data. 
FLOPs Technician 
 
Post-Test 
Verify that all test data have been acquired and stored. Shut down test chamber and prepare 
chamber for next test. 
Collect photos and videos of test environment if not already completed. Document any 
issues/failures encountered during testing.

## Page 15

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 15 
 
 
2.1.3 Temperature Shock 
Purpose 
Use the temperature shock test to determine if the TO2 aircraft can operate after withstanding 
sudden changes in temperature without experiencing physical damage. 
Required Equipment 
• TO2 Aircraft (P/N 127-117680), qty 1 (two transit cases) 
• Main Battery (P/N 107-101050), qty 1 
• GCS Laptop, qty 1 
• Ethernet cable, qty 1 (6ft or as required) 
• Trillium payload, qty 1 
• Adhesive tape, qty 1 (10ft or as required) 
Limitations 
Due to the limited internal volume of the test chamber, an abbreviated UUT will be used for 
testing. 
Test Method 
MIL-STD-810H, Method 503.7 Temperature Shock – Procedure I-D 
UUT Configuration 
The UUT for this test will be the TO2 aircraft fuselage with Avionics Enclosure installed and 
connected, centerwing installed and connected, and Trillium installed and connected. The Main 
Battery should be removed from the aircraft prior to testing. Other TO2 aircraft components 
including the tailboom, horizontal and vertical stabilizers, wingtips, and lift booms shall be 
placed inside the chamber along with the UUT, unconnected. 
All openings that would otherwise not be exposed with an assembled aircraft, e.g. centerwing 
tips, must be covered with tape to prevent ingress of external elements including moisture and 
debris. 
All unconnected electrical connectors should be covered with dustcaps or tape to prevent ingress 
of external elements including moisture and debris. 
Pre-Test 
Facility test personnel shall ensure that the TCs are installed on the aircraft per section 1.3 of this 
test plan. Pre-test TC measurement reading should be collected to capture the baseline 
temperature environment of the test chamber and to verify that the instrumentation is working 
normally.

## Page 16

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 16 
 
 
FLOPs technicians must record part and serial numbers of UUT and related components. 
Photos and video must be collected capturing the test setup including test articles, TC locations, 
and the test chamber. 
Test Procedure 
Table 2-3 Test Procedure: MIL-STD-810H Temperature Shock – Low 
Step Procedure Responsibility 
Step 1 Place the UUT with TCs installed and other aircraft 
components inside the test chamber. Facility Technician 
Step 2 Stabilize the UUT at a controlled ambient temperature of 23ºC. Facility Technician 
Step 3 
Transfer the test item in no more than one minute to an 
atmosphere of -20ºC and stabilize the temperature for a period 
of 4 hours. Use the TC reading from the Avionics Enclosure to 
verify UUT temperature stabilization. 
Facility Technician 
Step 4 
Transfer the test item in no more than one minute to a 
controlled ambient temperature of 23ºC and stabilize the 
temperature for a period of at least 4 hours. 
Facility Technician 
FLOPs Technician 
Step 5 Repeat Steps 1 thru 3 two (2) additional times for a total of 
three (3) cycles. Facility Technician 
Step 6 Position the GCS Laptop outside of the test chamber. Connect 
an ethernet cable from the GCS laptop to the UUT. FLOPs Technician 
Step 7 
Install the battery in the UUT and Power ON the UUT. 
Establish an ethernet data connection between the GCS laptop 
and the UUT. 
FLOPs Technician 
Step 8 
Conduct a complete visual examination and operational 
checkout (see Appendix A) and document the results for 
comparison with pretest data. 
Facility Technician 
FLOPs Technician 
Post-Test 
Verify that all test data have been acquired and stored. Shut down test chamber and prepare 
chamber for next test. 
Collect photos and videos of test environment if not already completed. Document any 
issues/failures encountered during testing. 
Table 2-4 Test Procedure: MIL-STD-810H Temperature Shock – High 
Step Procedure Responsibility 
Step 1 Place the UUT with TCs installed and other aircraft 
components inside the test chamber. Facility Technician 
Step 2 Stabilize the UUT at a controlled ambient temperature of 23ºC. Facility Technician

## Page 17

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 17 
 
 
Step 3 
Transfer the test item in no more than one minute to an 
atmosphere of 50ºC and stabilize the temperature for a period 
of 4 hours. Use the TC reading from the Avionics Enclosure to 
verify UUT temperature stabilization. 
Facility Technician 
Step 4 
Transfer the test item in no more than one minute to a 
controlled ambient temperature of 23ºC and stabilize the 
temperature for a period of at least 4 hours. 
Facility Technician 
FLOPs Technician 
Step 5 Repeat Steps 1 thru 3 two (2) additional times for a total of 
three (3) cycles. Facility Technician 
Step 6 Position the GCS Laptop outside of the test chamber. Connect 
an ethernet cable from the GCS laptop to the UUT. FLOPs Technician 
Step 7 
Install the battery in the UUT and Power ON the UUT. 
Establish an ethernet data connection between the GCS laptop 
and the UUT. 
FLOPs Technician 
Step 8 
Conduct a complete visual examination and operational 
checkout (see Appendix A) and document the results for 
comparison with pretest data. 
Facility Technician 
FLOPs Technician 
Post-Test 
Verify that all test data have been acquired and stored. Shut down test chamber and prepare 
chamber for next test. 
Collect photos and videos of test environment if not already completed. Document any 
issues/failures encountered during testing. 
2.1.4 Humidity 
Purpose 
To determine the resistance of the TO2 aircraft to the effects of a warm, humid atmosphere. 
Required Equipment 
• TO2 Aircraft (P/N 127-117680), qty 1 (two transit cases) 
• Main Battery (P/N 107-101050), qty 1 
• GCS Laptop, qty 1 
• Ethernet cable, qty 1 (6ft or as required) 
• Trillium payload, qty 1 
• Adhesive tape, qty 1 (10ft or as required) 
Limitations 
Due to the limited internal volume of the test chamber, an abbreviated UUT will be used for 
testing. 
Test Method

## Page 18

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 18 
 
 
MIL-STD-810H, Method 507.6 Humidity – Procedure II (Tailored) 
UUT Configuration 
The UUT for this test will be the TO2 aircraft fuselage with Avionics Enclosure installed and 
connected, centerwing installed and connected, and Trillium installed and connected. The Main 
Battery should be removed from the aircraft prior to testing. Other TO2 aircraft components 
including the tailboom, horizontal and vertical stabilizers, wingtips, and lift booms shall be 
placed inside the chamber along with the UUT, unconnected. 
All openings that would otherwise not be exposed with an assembled aircraft, e.g. centerwing 
tips, must be covered with tape to prevent ingress of external elements including moisture and 
debris. 
All unconnected electrical connectors should be covered with dustcaps or tape to prevent ingress 
of external elements including moisture and debris. 
Pre-Test 
Facility test personnel shall ensure that the TCs are installed on the aircraft per section 1.3 of this 
test plan. Pre-test TC measurement reading should be collected to capture the baseline 
temperature environment of the test chamber and to verify that the instrumentation is working 
normally. 
FLOPs technicians must record part and serial numbers of UUT and related components. 
Photos and video must be collected capturing the test setup including test articles, TC locations, 
and the test chamber. 
Test Procedure 
Table 2-5 Test Procedure: MIL-STD-810H Humidity (Tailored) 
Step Procedure Responsibility 
Step 1 Place the UUT with TCs installed and other aircraft 
components inside the test chamber. Facility Technician 
Step 2 Adjust the chamber temperature to 23 ± 2°C and 95% relative 
humidity and maintain for 24 hours. Facility Technician 
Step 3 Position the GCS Laptop outside of the test chamber. Connect 
an ethernet cable from the GCS laptop to the UUT. FLOPs Technician 
Step 4 
Install the battery in the UUT and Power ON the UUT. 
Establish an ethernet data connection between the GCS laptop 
and the UUT. 
FLOPs Technician 
Step 5 
Conduct a complete visual examination and operational 
checkout (see Appendix A) and document the results for 
comparison with pretest data. 
Facility Technician 
FLOPs Technician

## Page 19

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 19 
 
 
Step 6 Power OFF the UUT, remove the Main Battery, and disconnect 
the GCS Laptop. FLOPs Technician 
Step 7 Repeat Steps 1 thru 6 nine (9) more times for a total of 10 
cycles. 
Facility Technician 
FLOPs Technician 
Post-Test 
Verify that all test data have been acquired and stored. Shut down test chamber and prepare 
chamber for next test. 
Collect photos and videos of test environment if not already completed. Document any 
issues/failures encountered during testing. 
Repack the aircraft in the two (2) transit cases and prepare for return shipment to Edge 
Autonomy. 
2.1.5 Solar Radiation 
Purpose 
To determine the heating effects of solar radiation on the TO2 aircraft. 
Required Equipment 
• TO2 Aircraft (P/N 127-117680), qty 1 (two transit cases) 
• Main Battery (P/N 107-101050), qty 1 
• GCS Laptop, qty 1 
• Ethernet cable, qty 1 (6ft or as required) 
• Trillium payload, qty 1 
Limitations 
None 
Test Method 
MIL-STD-810H, Method 505.7 Solar Radiation – Procedure I 
UUT Configuration 
The UUT for this test will be the TO2 aircraft fully assembled with Trillium payload installed. 
The Main Battery should be removed from the aircraft prior to testing. 
Pre-Test 
Facility test personnel shall ensure that the TCs are installed on the aircraft per section 1.3 of this 
test plan. Pre-test TC measurement reading should be collected to capture the baseline 
temperature environment of the test chamber and to verify that the instrumentation is working 
normally.

## Page 20

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 20 
 
 
FLOPs technicians must record part and serial numbers of UUT and related components. 
Photos and video must be collected capturing the test setup including test articles, TC locations, 
and the test chamber. 
Test Procedure 
Table 2-6 Test Procedure: MIL-STD-810H Solar Radiation 
Step Procedure Responsibility 
Step 1 Place the UUT with TCs installed inside the test chamber. Facility Technician 
Step 2 Adjust the chamber temperature to A1 temperatures and stabilize 
the UUT for time 0000 (See Figure 5). Facility Technician 
Step 3 Expose the UUT to a continuous 24-hour cycle of controlled 
simulated solar radiation and dry-bulb temperatures per Figure 5.  Facility Technician 
Step 4 Position the GCS Laptop outside of the test chamber. Connect an 
ethernet cable from the GCS laptop to the UUT. FLOPs Technician 
Step 5 
Install the battery in the UUT and Power ON the UUT. Establish 
an ethernet data connection between the GCS laptop and the 
UUT. 
FLOPs Technician 
Step 6 Conduct an operational checkout on the UUT (see Appendix A) 
and document the results. 
Facility Technician 
FLOPs Technician 
Step 7 Power OFF the UUT, remove the Main Battery, and disconnect 
the GCS Laptop. FLOPs Technician 
Step 8 Repeat Steps 1 thru 7 six (6) more times for a total of seven (7) 
cycles. FLOPs Technician

## Page 21

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 21 
 
 
 
Figure 5 MIL-STD-810H Solar Radiation Procedure I Cycling Test 
Post-Test 
Verify that all test data have been acquired and stored. Shut down test chamber and prepare 
chamber for next test. 
Collect photos and videos of test environment if not already completed. Document any 
issues/failures encountered during testing. 
2.1.6 Dust 
Purpose 
To evaluate the ability of the TO2 aircraft to resist the effects of dust that may obstruct openings 
and penetrate into cracks, crevices, bearings, and joints. 
Required Equipment 
• TO2 Aircraft (P/N 127-117680), qty 1 (two transit cases) 
• Main Battery (P/N 107-101050), qty 1 
• GCS Laptop, qty 1

## Page 22

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 22 
 
 
• Ethernet cable, qty 1 (6ft or as required) 
• Trillium payload, qty 1 
Limitations 
None 
Test Method 
MIL-STD-810H, Method 510.7 Sand and Dust – Procedure I: Blowing Dust 
UUT Configuration 
The UUT for this test will be the TO2 aircraft fully assembled with Trillium payload installed. 
The Main Battery may be installed in the aircraft prior to test. 
Pre-Test 
No instrumentation is required to be installed on the UUT for this test. Test chamber 
measurements of temperature, flow rate, etc. can be used to verify test environment conditions. 
FLOPs technicians must record part and serial numbers of UUT and related components. 
Photos and video must be collected capturing the test setup including test articles, TC locations, 
and the test chamber. 
Test Procedure 
Table 2-7 Test Procedure: MIL-STD-810H Dust 
Step Procedure Responsibility 
Step 1 
Place the UUT inside the test chamber stabilized at ambient 
temperature. Adjust the air velocity to 8.9 ±1.3 m/s. Adjust 
RH to less than 30% and maintain throughout the test. 
Facility Technician 
Step 2 Adjust the dust feed control for a dust concentration of 10.6 
±7 g/m3. Facility Technician 
Step 3 Maintain the conditions of Steps 1 and 2 for 6 hours.  Facility Technician 
Step 4 
Stop the dust feed and reduce the air velocity to 1.5 ±1 m/s 
and set the chamber temperature to 50ºC at a rate less than 
3ºC/min. 
Facility Technician 
Step 5 Allow the UUT temperature to stabilize and maintain 
conditions for 1 hour. Facility Technician 
Step 6 Position the GCS Laptop outside of the test chamber. Connect 
an ethernet cable from the GCS laptop to the UUT. FLOPs Technician 
Step 7 Power ON the UUT. Establish an ethernet data connection 
between the GCS laptop and the UUT. FLOPs Technician

## Page 23

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 23 
 
 
Step 8 Conduct an operational checkout on the UUT (see Appendix 
A) and document the results. FLOPs Technician 
Step 9 Power OFF the UUT and disconnect the GCS Laptop. FLOPs Technician 
Step 10 
Adjust the air velocity to 8.9 ±1.3 m/s and restart the dust 
feed. Adjust the dust feed control for a dust concentration of 
10.6 ±7 g/m3. 
Facility Technician 
Step 11 
Maintain the conditions of Step 6 at 50ºC temperature for 6 
hours. Periodically rotate the aircraft by increments of 90º to 
ensure full exposure of the UUT to the dust. 
Facility Technician 
Step 12 Stop the dust feed and adjust the chamber to ambient 
temperature. Facility Technician 
Step 13 Repeat Step 6 thru Step 9. FLOPs Technician 
Post-Test 
Verify that all test data have been acquired and stored. Shut down test chamber and prepare 
chamber for next test. 
Collect photos and videos of test environment if not already completed. Document any 
issues/failures encountered during testing. 
2.1.7 Sand 
Purpose 
To evaluate the ability of the TO2 aircraft to be operated in blowing sand conditions without 
degrading performance, effectiveness, reliability, and maintainability due to abrasion or 
clogging. 
Required Equipment 
• TO2 Aircraft (P/N 127-117680), qty 1 (two transit cases) 
• Main Battery (P/N 107-101050), qty 1 
• GCS Laptop, qty 1 
• Ethernet cable, qty 1 (6ft or as required) 
• Trillium payload, qty 1 
Limitations 
None 
Test Method 
MIL-STD-810H, Method 510.7 Sand and Dust – Procedure II: Blowing Sand 
UUT Configuration

## Page 24

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 24 
 
 
The UUT for this test will be the TO2 aircraft fully assembled with Trillium payload installed. 
The Main Battery may be installed in the aircraft prior to test. 
Pre-Test 
No instrumentation is required to be installed on the UUT for this test. Test chamber 
measurements of temperature, flow rate, etc. can be used to verify test environment conditions. 
FLOPs technicians must record part and serial numbers of UUT and related components. 
Photos and video must be collected capturing the test setup including test articles, TC locations, 
and the test chamber. 
Test Procedure 
Table 2-8 Test Procedure: MIL-STD-810H Sand 
Step Procedure Responsibility 
Step 1 
Place the UUT inside the test chamber and set the chamber 
temperature to 50ºC at a rate less than 3ºC/min. Allow the 
UUT to stabilize. 
Facility Technician 
Step 2 Adjust the air velocity to 18 m/s. Facility Technician 
Step 3 Set the sand feeder to a mass flow rate of 0.18 g/m3, ±0.2 g/m3. Facility Technician 
Step 4 
Maintain the conditions of Step 1 thru 3 for six (6) hours. 
Periodically rotate the aircraft by increments of 90º to ensure 
full exposure of the UUT to the dust. 
Facility Technician 
Step 5 Stop the sand feed and set the chamber temperature to ambient. 
Allow the UUT to stabilize. Stop all air flow in the chamber. Facility Technician 
Step 6 Visually inspect the UUT for sand clogging effects, abrasions, 
etc. and document with photographs. Facility Technician 
Step 7 Position the GCS Laptop outside of the test chamber. Connect 
an ethernet cable from the GCS laptop to the UUT. FLOPs Technician 
Step 8 Power ON the UUT. Establish an ethernet data connection 
between the GCS laptop and the UUT. FLOPs Technician 
Step 9 Conduct an operational checkout on the UUT (see Appendix 
A) and document the results. FLOPs Technician 
Step 10 Power OFF the UUT and disconnect the GCS Laptop. FLOPs Technician 
Post-Test 
Verify that all test data have been acquired and stored. Shut down test chamber and prepare 
chamber for next test. 
Collect photos and videos of test environment if not already completed. Document any 
issues/failures encountered during testing.

## Page 25

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 25 
 
 
2.1.8 Waterproof Rain 
Purpose 
To determine the capability of the TO2 aircraft to perform after exposure to water, the 
effectiveness of the aircraft water removal systems, and the protection offered to internal 
components from the aircraft body. 
Required Equipment 
• TO2 Aircraft (P/N 127-117680), qty 1 (two transit cases) 
• Main Battery (P/N 107-101050), qty 1 
• GCS Laptop, qty 1 
• Ethernet cable, qty 1 (6ft or as required) 
• Trillium payload, qty 1 
Limitations 
None 
Test Method 
MIL-STD-810H, Method 506.6 Rain – Procedure I 
UUT Configuration 
The UUT for this test will be the TO2 aircraft fully assembled with Trillium payload installed. 
The Main Battery will not be installed during the test. 
Pre-Test 
No instrumentation is required to be installed on the UUT for this test. Test chamber 
measurements of temperature, flow rate, etc. can be used to verify test environment conditions. 
FLOPs technicians must record part and serial numbers of UUT and related components. 
Photos and video must be collected capturing the test setup including test articles, TC locations, 
and the test chamber. 
Test Procedure 
Table 2-9 Test Procedure: MIL-STD-810H Rain 
Step Procedure Responsibility 
Step 1 
Heat the UUT or cool the water so that the stabilized UUT 
temperature is a minimum of 10ºC greater than the rain water 
temperature at the start of each exposure period. Place the 
UUT inside the test chamber. 
Facility Technician

## Page 26

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 26 
 
 
Step 2 Adjust the air velocity to 18 m/s. Set the rain rate to 4 in/hr and 
maintain these conditions for 30 min. Facility Technician 
Step 3 
Measure and document any water found inside the UUT 
fuselage. Take photographs as necessary to capture the post-
test condition of the UUT. 
Facility Technician 
Step 4 Rotate the UUT 90 degrees and repeat Step 1 thru Step 3 until 
all sides of the UUT have been subjected to testing. Facility Technician 
Step 5 Position the GCS Laptop outside of the test chamber. Connect 
an ethernet cable from the GCS laptop to the UUT. FLOPs Technician 
Step 6 
Install the battery in the UUT and Power ON the UUT. 
Establish an ethernet data connection between the GCS laptop 
and the UUT. 
FLOPs Technician 
Step 7 Conduct an operational checkout on the UUT (see Appendix 
A) and document the results. FLOPs Technician 
Step 8 Power OFF the UUT and disconnect the GCS Laptop. FLOPs Technician 
Post-Test 
Verify that all test data have been acquired and stored. Shut down test chamber and prepare 
chamber for next test. 
Collect photos and videos of test environment if not already completed. Document any 
issues/failures encountered during testing. 
Repack the aircraft in the two (2) transit cases and prepare for return shipment to Edge 
Autonomy.

## Page 27

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 27 
 
 
3 Acronyms 
ADP Air Data Pod  
FLOPs Flight Operations 
FWAP Fixed-Wing AutoPilot 
LMUK Lockheed Martin United Kingdom  
MCM Mission Compute Module  
MIL-STD Military Standard  
P/N Part Number 
TC Thermocouple 
TO2 Task Order 2  
UUT Unit Under Test

## Page 28

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 28 
 
 
4 Appendix A – Operational Checkout Procedure 
1. On the GCS laptop, open the GCS (VXE SUAV) and allow the application to load. 
 
 
 
2. From the toolbar at the top of the application, left-click on the “Comm” menu. 
 
 
 
3. From the “Comm” drop-down menu, select “Connect”.

## Page 29

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 29 
 
 
 
 
4. In the “Connect To…” window prompt that opens, enter the tail number of the aircraft 
and click “OK”.

## Page 30

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 30 
 
 
5. From the toolbar at the top of the application, left-click on the “Tools” menu. 
 
6. From the drop-down menu that appears, select “Instrument Panel”.

## Page 31

111-24810 - TO2 Environmental Test Plan 
 
2024.12.09 Edge Autonomy Proprietary Information 31 
 
 
7. The Instrument Panel window will appear. This window can be used to verify data 
connection between the GCS laptop and the aircraft by providing real-time feedback.
