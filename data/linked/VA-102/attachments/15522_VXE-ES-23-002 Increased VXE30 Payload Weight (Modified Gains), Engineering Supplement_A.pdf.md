# VXE-ES-23-002 Increased VXE30 Payload Weight (Modified Gains), Engineering Supplement_A.pdf

Attachment 15522, pdf, 1060 KB, added 2023-07-19 by Cody Smisek.

## Page 1

Edge Autonomy Proprietary Information 1 
 
 
 
 
 
Engineering Supplement 
 
 
VXE-ES-23-002  
 
Increased VXE30 Payload Weight 
(Modified Gains Configuration) 
 
NOT FOR GENERAL RELEASE 
 
Revision A 
Dated: 7/18/2023

## Page 2

Edge Autonomy Proprietary Information 2 
 
Copies and Support:  
 
© 2023 Edge Autonomy Unpublished work.  All rights reserved. 
.

## Page 3

Edge Autonomy Proprietary Information 3 
 
Revision History: 
 
Rev Description Written by Checked by Approved by Date 
A Initial Release R. Christino C. Smisek S. Miller 7/18/23

## Page 4

Edge Autonomy Proprietary Information 4 
 
1. APPLICATION:  
This engineering supplement is applicable to all VXE30 systems and once complete, allows for  
an MGTOW of up to 52 lb. with a density altitude limitation of 7,500 ft. 
 
2. PURPOSE: 
 
The purpose of this engineering supplement is to provide instructions for modifying system 
parameters to allow for operation of the Stalker VXE30 at an increased Max Gross Take Off 
Weight (MGTOW). Parameters are modified through the VTOL webpage and through the GCS . 
These parameters include airspeed setpoints for fixed wing flight and the climb rate for the 
VTOL operation. When operating in this Modified Gain Configuration the transition altitude 
must be reduced to 200ft for all missions.  
Setting a 300ft transition in the Modified Gain Configuration will cause a low climb rate to be 
applied for a normal climb distance. This results in an extended period of thermal stress on the 
system and will most likely overheat and damage lift system components.  
This Modified Gain Configuration is outside of the normal operating conditions for the system, 
and while flights have been successfully demonstrated in this configuration, operators will still 
be liable for any aircraft incidents while flying in this configuration. 
 
3. PROCEDURE: 
 
3.1 Review the VXE30 Operations Manual and VXE30 Payload ICD for all additional payload 
considerations such as power draw, increased drag, and lateral imbalance. 
 
Record the weight of the aircraft in the desired payload loadout. 
 
If the MGTOW of the aircraft exceeds the limitations specified in the VXE30 Operators 
Manual, the following supplement must be completed.

## Page 5

Edge Autonomy Proprietary Information 5 
 
3.2 Change Fixed Wing Gains (Airspeed Setpoints): 
 
3.2.1 Power on a Stalker VXE30 and connect via the GCS. 
 
3.2.2 Under the “Tools” drop down, open the “Gains” dialog window. 
 
 
Figure 1. Typical GCS Window with Tools Drop Down Highlighted 
 
Figure 2. Gains Dialog Window

## Page 6

Edge Autonomy Proprietary Information 6 
 
3.2.3 Press “Get From AP”, wait a couple of seconds to ensure the gains have been loaded 
correctly. Record the checksum values. 
 
 
Figure 3. Gains Dialog Window with "Get From AP" Highlighted 
 
 
 
3.2.4 Find these 3 entries in the “Gains” dialog window. (Baseline Values Indicated Below) 
1. Landing Speed (fps) = 51 
2. Climb Speed = 52 
3. Cruise Speed = 53 
 
NOTE: Figure values do not represent the baseline listed above. 
 
 
Figure 4. Autopilot Airspeed Setpoints Highlighted in the Gains Dialog Window

## Page 7

Edge Autonomy Proprietary Information 7 
 
3.2.5 Refer to the following look up table for Autopilot Setpoints based on the desired 
weight. Input the values for the recorded aircraft weight into the “Gains” dialog. 
 
TOW (lb.) LandSpd (fps) ClimbSpd (fps) CruiseSpd (fps) 
48 51 52 53 
49 52 53 54 
50 53 54 55 
51 53 54 55 
52 54 55 56 
Table 1. TOW vs Airspeed Setpoint Lookup Table 
 
NOTE 
Round up to the nearest weight if recorded aircraft weight is in between values. 
 
3.2.6 Once the values are input, Press “Send to AP”. 
 
 
 
NOTE 
You should hear an audible beep from the aircraft when the gains are sent over. 
 
 
3.2.7 Select “Get from AP” to verify values do not change.  
3.2.8 Power cycle the aircraft and confirm the gains have been properly updated by 
navigating back to the window. Record the checksum values.

## Page 8

Edge Autonomy Proprietary Information 8 
 
3.3 Change VTOL Climb Rate: 
 
3.3.1 With the GCS still open and the aircraft still powered on, Open the VTOL webpage 
using the “IP Address Calculator” located under the “Tools” drop down menu. 
 
 
Figure 5. IP Address Calculator with VTOL Highlighted 
3.3.2 In the VTOL webpage, open the “Configuration” page. 
NOTE: Configuration page username is “stalker” and password is “[password removed]”.  
 
Figure 6. VTOL Webpage with Configuration Page Highlighted

## Page 9

Edge Autonomy Proprietary Information 9 
 
 
 
3.3.3 Within the “Configuration” page, open the “Multicopter” sub-page. 
 
 
Figure 7. Configuration Page with Multicopter Page Highlighted 
 
 
3.3.4 Locate the variable “m_alt.outmax” in Altitude Stab. Set this value to 6 fps. 
 
 
Figure 8. VTOL Climb Rate Highlighted

## Page 10

Edge Autonomy Proprietary Information 10 
 
 
3.3.5 Press both the “Update” and “Save” buttons. The order does not matter. 
 
 
Figure 9. Top of Multicopter Page with Update and Save Buttons Highlighted 
 
3.3.6 Power cycle the aircraft and ensure changes have been saved by navigating back to 
the location and confirming the set value of 6 fps for climb rate. 
 
3.4 Review the limitations of the Modified Gain Configuration 
 
The limitations for flying with the correct modified gain values is as follows: 
 
MGTOW (lb.) Density Altitude Endurance (Hrs.) 
52 7,500 ft 3 
 
 
Note: When connecting to an aircraft with this non-baseline configuration, the GCS 
software will prompt the operator to update the configuration.  It is the operator’s 
responsibility to manually track this special configuration, and it is recommended that 
the operator physically note the change on the aircraft.

## Page 11

Edge Autonomy Proprietary Information 11 
 
Figure 11. Checking Aircraft CG 
3.5 When planning the mission and before launch, ensure the transition altitude is set for a 
200ft maximum. 
 
 
Figure 10. Waypoint L Edit Menu with 200 ft Transition Highlighted 
3.6 Before flying, make sure to perform a CG check on the aircraft using the CG tool. 
 
Ensure that the aircraft sits within the acceptable CG range of 4.2” to 5.3” in the desired 
flight loadout.  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
This engineering supplement is now complete.
