# Investigation Report VXE-530&600_9OCT2024.pdf

Attachment 23933, pdf, 685 KB, added 2024-10-14 by Pat Wells.

## Page 1

Investigation Summary 
VXE- 530 & 600 
Incident Number: VXEP-597 
Revision: 1 
Author: S. Wendling 
Date: 9 October 2024 
 
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

Investigation Summary: VXEP-597  
 
Oct 9, 2024 Edge Autonomy Proprietary Information 2 
Table of Contents 
1 Introduction and Summary ................................................................................................................... 3 
1.1 Operator Description of the Incident .......................................................................................... 3 
1.2 Summary ...................................................................................................................................... 3 
1.3 Investigation Plan ........................................................................................................................ 4 
1.4 Root Cause ................................................................................................................................... 4 
1.5 Conclusion ................................................................................................................................... 4 
2 Investigation Details .............................................................................................................................. 5 
2.1 Investigation Results .................................................................................................................... 5 
2.2 Explanation of Expected Behavior ............................................................................................... 6 
 
List of Figures 
Figure 1: IMG_1595 provided with After Action Report from Operator 
Figure 2: Graph of "supFanEn" - Nose Cone Fan Enabled (0,1), "ReactorTemp" - Internal Fuel Cell 
Temperature (°C), "apAlt" - Aircraft Altitude (ft). Primary y-axis data (y1), Secondary y-axis (y2). 
Figure 3: HLB Battery Connections. Orange - VTOL Lift Connector; Red - FC, Avionics, Front Nose Fan.

## Page 3

Investigation Summary: VXEP-597  
 
Oct 9, 2024 Edge Autonomy Proprietary Information 3 
1 Introduction and Summary 
1.1 Operator Description of the Incident 
“The nose fan on V530 and V600 failed to shut off once the fuel cell is cooled down. GCS had already 
been packed up, so don’t have the actual temperature on V530, but V600’s fan was still running while 
temp was <100°C. In both cases, battery power was disconnected while the fan was still running. 
See photo of temperature reading attached. 
AAR for V600 is attached for configuration. Fuel cell might have cooled below 150°C before the FDR was 
successfully downloaded.” 
1.2 Summary 
LM FSR Describes discrepancy where VXE Forward Nose Cone Fan was operational after the battery is 
disconnected from Aircraft. They supplied AAR Report from the incident in question as well as a photo of 
the GCS Screen showing fuel cell temperature under 100°C. 
Figure 1: IMG_1595 provided with After Action Report from Operator

## Page 4

Investigation Summary: VXEP-597  
 
Oct 9, 2024 Edge Autonomy Proprietary Information 4 
1.3 Investigation Plan 
1. AAR Data Review to identify non-conforming behavior. 
2. Determination of Airworthiness and whether equipment requires return. 
3. Provide Preliminary Explanation to Forward Team 
4. Generate Report describing Root Causes/Corrective Actions if Applicable 
1.4 Root Cause  
Suspected Operator Error. Fuel Cell cannot operate Nose Cone Fan without connected to battery at 
described temperature/operation state as there are no other sources of power on aircraft. Possible 
partial disconnect of the battery by removing VTOL Harness (from center wing) and not Avionics/Fuel 
Cell/Nose Cone Fan harness (from Fuselage).   
 
1.5 Conclusion 
Behavior reported is determined to be normal and does not pose a risk to operation of aircraft or fuel 
cell system. Data supplied for the flight in question shows Nose Cone Fan is enabled when the aircraft 
lands and is operational throughout the duration of the cooldown that can be seen from FDR. Fuel Cell is 
unable to generate power to energize the Nose Fan without being connected to the battery, and from 
provided screenshot battery connection is confirmed by observation of a reporting Voltage and Battery 
Life value on the Fuel Cell Dialog (FCD).

## Page 5

Investigation Summary: VXEP-597  
 
Oct 9, 2024 Edge Autonomy Proprietary Information 5 
2 Investigation Details 
2.1 Investigation Results 
In available data, Nose Cone Fan begins to operate after Aircraft has been recovered and is on the 
ground. This is considered normal behavior, as Nose Cone Fan should always be engaged when fuel cell 
is online, >150°C, and not in forward flight state. Data terminates after FDR is successfully generated, 
and reported abnormal behavior occurs after termination of data stream.  
Fuel Cell unit does not possess internal energy storage, and when not in “operate” state, requires energy 
from the HLB to warmup to nominal temperature and cooldown to safe (<150°C) temperature. When 
Fuel Cell System state is not “Operate” (650-830°C), it is not possible for fuel cell to generate any energy 
to power the nose cone fan, this requires battery connection to HLB. 
 
In the provided image, we can see that battery is still connected to the Aircraft Avionics (RH Harness) 
because battery state and life % are reported on FCD. Note, disconnecting only the center wing LH 
connection to the HLB is not a complete disconnection from the battery. Avionics, forward flight 
mechanics, and front fan are all connected through the connection on the RH side of the battery and will 
still be energized if the conditions for operation are met. 
Figure 2: Graph of "supFanEn" - Nose Cone Fan Enabled (0,1), "ReactorTemp" - Internal Fuel Cell Temperature (°C), "apAlt" - 
Aircraft Altitude (ft). Primary y-axis data (y1), Secondary y-axis (y2).

## Page 6

Investigation Summary: VXEP-597  
 
Oct 9, 2024 Edge Autonomy Proprietary Information 6 
Without battery connection to RH connector, the Fuel Cell, Avionics, and Front Nose Cone Fan are no 
longer energized and not able to function.  
 
2.2 Explanation of Expected Behavior 
Power system on VXE-30 in Fuel Cell Configuration consists of a Hybrid Battery (Energy Storage) and a 
Solid Oxide Fuel Cell (Electrical Generator) converting fuel to electrical energy. The Fuel Cell System does 
not possess internal energy storage, and when it is not in “operate” (state “5”, “Generating”) requires 
connection to the HLB to function. In order to reach operation and cooldown after use, it consumes 
energy from the HLB, and therefore during cooldown cannot operate without HLB being connected via 
the power harness on the starboard side of the aircraft.  
 
This connection of the battery is required until the fuel cell is “off” and under 150°C. Afterward, battery 
can be disconnected from the fuel cell and avionics via power harness. Nose Cone Fan will shut off after 
the fuel cell has completely shut down. It is critical that the battery remains connected until the fuel cell 
has completely shut down, otherwise the fuel cell will be de-energized while hot, resulting in damage to 
the Fuel Cell Stack and reduced performance. Additionally, Nose Cone Fan is required to manage the 
heat generated by the fuel cell inside of the fuselage. 
  
Conditions for Nose Cone Fan Operation are as follows: 
• Aircraft on the ground and not in forward flight mode. 
• Fuel Cell online and >150°C. 
Figure 3: HLB Battery Connections. Orange - 
VTOL Lift Connector; Red - FC, Avionics, Front 
Nose Fan.
