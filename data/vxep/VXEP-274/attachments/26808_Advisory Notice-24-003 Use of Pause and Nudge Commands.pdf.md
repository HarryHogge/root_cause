# Advisory Notice-24-003 Use of Pause and Nudge Commands.pdf

Attachment 26808, pdf, 208 KB, added 2025-03-04 by Cameron Chapman.

## Page 1

Date: 10.Dec.2024 
Rev: A 
 
 Advisory Notice 
(AN)_Pause_and_Nudge_Usage_Guidelines_2024-
12-10 
  
 
    
 
 
 
  
Advisory  Notice  (A N) 
Advisory Notice -24 -00 3 
 
Use of Pause and Nudge Com mands  
 
 
 
Revision A  
December 10, 2024

## Page 2

Date: 10.Dec.2024 
Rev: A 
 
 Advisory Notice 
(AN)_Pause_and_Nudge_Usage_Guidelines_2024-
12-10 
  
 
    
 
  
Supplemental Documentation 
This document is updated on a continuous basis as new equipment and procedures become available for 
the VXE30. However, certain conditions (such as an equipment modification or safety concerns) make it 
necessary to notify users before a revised manual is released. These documents are distributed as part of 
Edge Autonomy customer support, and are available in four types: 
 
Airworthiness Safety Alert (ASA)  
Previously designated as an Airworthiness Directive (AD), an Airworthiness Safety Alert notifies users of an 
airworthiness related problem and a solution with OEM directed mandatory corrective actions to mitigate loss 
of aircraft. The document notifies users of procedures or modifications Edge Autonomy developed to correct 
the issue. Airworthiness safety alerts are a procedural change.    
 
Advisory Notice (AN)  
An Advisory Notice is an informative document outlining a system component or components that have been 
found to have an unresolved issue as part of an ongoing investigation. The information contains descriptions 
of the issue and mitigation procedures that should be taken.   
 
Service Bulletins (SB)  
A service bulletin is a document notifying users of modifications or improvements to Edge Autonomy products 
in terms of modifying or installing new components within the operational system.  
 
Operational Supplement (OS)  
An operational supplement is a descriptive document outlining a system component that is not a part of the 
standard baseline configuration. This information contains operational descriptions and special procedures 
and only applies to operations when that component is being utilized.

## Page 3

Date: 10.Dec.2024 
Rev: A 
 
 Advisory Notice 
(AN)_Pause_and_Nudge_Usage_Guidelines_2024-
12-10 
  
 
    
 
Notice 
This information is the PROPRIETARY PROPERTY of Edge Autonomy and shall be subject to and comply 
with all applicable U.S. export control laws, economic sanctions laws and regulations. No part of this 
document shall be disclosed in any manner to a third party without the prior written consent of Edge 
Autonomy. This document and its contents shall not be transferred, disclosed, modified, or otherwise 
provided to or made accessible to any persons or entities not authorized to receive or have access to the 
document without written authorization from Edge Autonomy. 
 
Please see Home - Edge Autonomy for more details. 
 
Contact us: 
United States Support Office 
831 Buckley Road, San Luis Obispo, CA 93401 USA 
E-mail: Globalsupport@edgeautonomy.io 
Phone: +1 855-334-3457 
  
European Support Office 
1 Jaunbridagi, Marupes nov. LV-2167, Latvia 
Phone: +371 2026-2126

## Page 4

Date: 10.Dec.2024 
Rev: A 
 
 Advisory Notice 
(AN)_Pause_and_Nudge_Usage_Guidelines_2024-
12-10 
  
 
    
 
        
        
       
 
Overview 
Purpose 
To prevent potential damage or total loss of the VXE30 aircraft by clarifying the 
appropriate use of the "Pause" and "Nudge" commands during VTOL launch and recovery 
operations. 
 
Scope 
Recent incidents have highlighted the misuse of the VTOL "Pause" and "Nudge" 
commands. These functions are designed to enable horizontal positional adjustments in 
emergencies to mitigate damage to persons, property, or the aircraft. Emergency use cases 
include GPS-denied landings, loss of GPS during takeoff, use within tight spaces to avoid 
obstacles during takeoff or landing (i.e. rooftops or within a small clearing of trees or buildings), 
and in training operations.  The “Pause” feature is not intended to be used for prolonged hover, 
and the operator should limit time in this mode.  Edge Autonomy is revising the VXE30 
Operations Manual to classify these commands as Emergency Procedures. This notice aims to 
prompt operators to review relevant training, recommendations made in this document, and 
operational guidelines. Section references below can be found in the current release of the 
VXE30 Operations Manual v1.6. 
 
Compliance 
To ensure the safe operation of the aircraft in the VTOL phases of flight, operators must 
understand that the “Pause” and “Nudge” commands are for use as an Emergency Procedure 
only: 
• VXE30 Operations Manual Section 1.2.3: Landing requirements 
• VXE30 Operations Manual Section 3.16.7 Semi-Autonomous Flight Modes 
• VXE30 Operations Manual Section 3.17 Landing

## Page 5

Date: 10.Dec.2024 
Rev: A 
 
 Advisory Notice 
(AN)_Pause_and_Nudge_Usage_Guidelines_2024-
12-10 
  
 
    
 
VTOL Pause and Nudge Function Overview and Additional Guidance 
 
NOTE 
Pause Landing is only available if there is enough HLB energy to safely hover for the additional 
time during pause. 
 
Pause Landing (vertical landing only) 
During descent, the “Pause VTOL Landing” button is enabled. Allows the operator to 
command a pause, causing the vehicle to stop descending and hover in place.  Holding the 
pause button will continue to hold the vertical position of the vehicle until released or insufficient 
Hybrid Lift Battery (HLB) energy remains. Allow the vehicle to descend to roughly 50 ft / 15 
m AGL, or a point where it is easy to visually anticipate where the vehicle will land. Push the 
pause button. When the pause button is held down, descent stops.  
 
Auto Position Nudge (vertical takeoff and landing) 
Allows the operator to command incremental changes to the vehicle's horizontal position 
target, either while climbing or descending, or during a “pause.”  This override is best used in 
conjunction with a pause to arrest the vehicle's descent prior to repositioning the vehicle.   
• Nudge buttons in the dialog box or using the left joystick of the hand controller will move 
the vehicle forward, aft, left and right.  
• The dialog buttons and joystick make incremental changes to the vehicle position. 
• Clicking “Forward” or holding the joystick forward, then releasing typically causes the 
vehicle to move forward 10-20 feet / 3-6 m and hold station (while continuing to climb or 
descend). If the operator stops nudging, the vehicle quickly stops moving horizontally. 
CAUTION 
The vehicle is very sensitive and easy to over-correct when in Manual Nudge. Large control 
inputs can command the aircraft to maneuver abruptly, which could cause the aircraft to 
crash. Control inputs should be very small until the operator fully understands their impact on 
the vehicle position. 
Intermittent C2 during nudge events may lead to delayed response, resulting in an 
overcorrection.  Proceed with caution using Pause and Nudge in a known contested C2 
environment. 
 
Manual Nudge (vertical takeoff and landing): Allows the operator to have manual, direct control 
of how fast and in what direction the vehicle moves horizontally. This control method is very 
effective but requires operator skill and care to be used safely.

## Page 6

Date: 10.Dec.2024 
Rev: A 
 
 Advisory Notice 
(AN)_Pause_and_Nudge_Usage_Guidelines_2024-
12-10 
  
 
    
 
 
• Used if GPS is lost or highly dynamic operator control is needed. 
• Dialog buttons or nudge stick cause the vehicle to hold an attitude rather than a GPS 
position. Effectively, the vehicle will accelerate in the direction commanded, proportionally 
to the nudge stick deflection. 
• Deceleration is very slow, effectively negligible unless the vehicle is commanded in the 
opposite direction. When operating in this mode, the operator is responsible for arresting 
the horizontal movement with opposite stick input.  
• The operator is responsible for horizontal station keeping in wind, which may be 
challenging in winds above 5 kts or gusty conditions.  In this environment, diverting the 
vehicle away from persons or property will highly depend on the operator's skill.   
 
   
 
 
Recommendations for using "Pause or Nudge" Command 
1. If ascending, it is unsafe to continue the current ascent route due to obstacles or other 
safety concerns, and it is not possible to abort the landing. 
o Position Nudge the aircraft in a direction to avoid the obstacle or safety concern 
2. If while descending, it is unsafe to land at the presumed touchdown spot. 
o Position Nudge the aircraft in the direction of the desired touchdown spot. 
o Pause the aircraft only if necessary, just long enough for the ground crew to get 
visual confirmation of the desired landing spot.
