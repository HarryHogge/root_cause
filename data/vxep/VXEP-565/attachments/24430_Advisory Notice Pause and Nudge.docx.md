# Advisory Notice Pause and Nudge.docx

Attachment 24430, docx, 64 KB, added 2024-11-08 by Pat Wells.

|  |  |

## Supplemental Documentation

This document is updated on a continuous basis as new equipment and procedures become available for the VXE30. However, certain conditions (such as an equipment modification or safety concerns) make it necessary to notify users before a revised manual is released. These documents are distributed as part of Edge Autonomy customer support, and are available in four types:

Airworthiness Safety Alert (ASA)

Previously designated as an Airworthiness Directive (AD), an Airworthiness Safety Alert notifies users of an airworthiness related problem and a solution with OEM directed mandatory corrective actions to mitigate loss of aircraft. The document notifies users of procedures or modifications Edge Autonomy developed to correct the issue. Airworthiness safety alerts are a procedural change.

Advisory Notice (AN)

An Advisory Notice is an informative document outlining a system component or components that have been found to have an unresolved issue as part of an ongoing investigation. The information contains descriptions of the issue and mitigation procedures that should be taken.

Service Bulletins (SB)

A service bulletin is a document notifying users of modifications or improvements to Edge Autonomy products in terms of modifying or installing new components within the operational system.

Operational Supplement (OS)

An operational supplement is a descriptive document outlining a system component that is not a part of the standard baseline configuration. This information contains operational descriptions and special procedures and only applies to operations when that component is being utilized.

## Notice

This information is the PROPRIETARY PROPERTY of Edge Autonomy and shall be subject to and comply with all applicable U.S. export control laws, economic sanctions laws and regulations. No part of this document shall be disclosed in any manner to a third party without the prior written consent of Edge Autonomy. This document and its contents shall not be transferred, disclosed, modified, or otherwise provided to or made accessible to any persons or entities not authorized to receive or have access to the document without written authorization from Edge Autonomy.

Please see Home - Edge Autonomy for more details.

Contact us:

United States Support Office
831 Buckley Road, San Luis Obispo, CA 93401 USA

E-mail: Globalsupport@edgeautonomy.io
Phone: +1 855-334-3457

European Support Office
1 Jaunbridagi, Marupes nov. LV-2167, Latvia
Phone: +371 2026-2126

Overview

Purpose

To prevent potential damage or total loss of the VXE30 aircraft by clarifying the appropriate use of the "Pause" and "Nudge" commands during VTOL launch and recovery operations.

Scope

Recent incidents have highlighted misuse of the "Pause" and "Nudge" commands. These functions are designed exclusively for small positional adjustments in emergencies, not for routine operations or prolonged control. Edge Autonomy is revising the VXE30 Operations Manual to classify these commands strictly as Emergency Procedures. This notice aims to prompt operators to review relevant training, recommendations made in this document, and operational guidelines. Section references below can be found in the current release of the VXE30 Operations Manual v1.6.

Compliance

To ensure the safe operation of the aircraft in the VTOL phases of flight, operators must understand that the “Pause” and “Nudge” commands are for use as an Emergency Procedure only:

VXE30 Operations Manual Section 1.2.3: Landing requirements

VXE30 Operations Manual Section 3.16.7 Semi-Autonomous Flight Modes

VXE30 Operations Manual Section 3.17 Landing

Pause and Nudge Function Overview

NOTE

Pause Landing is only available if there is enough HLB energy to safely hover for the additional time during pause.

Pause Landing (vertical landing only)

During descent, the “Pause VTOL Landing” button is enabled. Allows the operator to command a pause, causing the vehicle to stop descending and hover in place.  Holding the pause button will continue to hold the vertical position of the vehicle until released or insufficient Hybrid Lift Battery (HLB) energy remains. Allow the vehicle to descend to roughly 50 ft / 15 m AGL, or a point where it is easy to visually anticipate where the vehicle will land. Push the pause button. When the pause button is held down, descent stops.

Auto Position Nudge (vertical takeoff and landing)

Allows the operator to command incremental changes to the vehicle position.  Adjusting the touchdown point or climb position this override is available during pause on landing.

Nudge buttons in the dialog box or using the left joystick of the hand controller will move the vehicle forward, aft, left and right.

The dialog buttons and joystick make incremental changes to the vehicle position.

Clicking “Forward” or holding the joystick forward, then releasing causes the vehicle to move forward 10-20 feet / 3-6 m and hold station (while continuing to climb or descend). If the operator stops nudging, the vehicle quickly stops moving.

CAUTION

The vehicle is very sensitive and easy to over-correct when in Manual Nudge. Large control inputs can command the aircraft to maneuver abruptly, which could cause the aircraft to crash. Control inputs should be very small until the operator fully understands their impact on the vehicle position.

Manual Nudge (vertical takeoff and landing): Allows the operator to command large changes to the vehicle position.

Used if GPS is lost or highly dynamic operator control is needed.

Dialog buttons or nudge stick cause the vehicle to hold an attitude rather than a position. Effectively, the vehicle will accelerate in the direction commanded.

Deceleration is very slow, effectively negligible, unless the vehicle is commanded in the opposite direction.

Recommendations for using "Pause or Nudge" Command

If it is determined, while ascending, that it is unsafe to continue the current ascent route due to obstacles or other safety concerns.

Position Nudge the aircraft in a direction to avoid the obstacle or safety concern

If it is determined, while descending, that it is unsafe to land at the presumed touchdown spot.

Position Nudge the aircraft in the direction of the desired touchdown spot.

Pause the aircraft only if necessary, just long enough for the ground crew to get visual confirmation of the desired landing spot.
