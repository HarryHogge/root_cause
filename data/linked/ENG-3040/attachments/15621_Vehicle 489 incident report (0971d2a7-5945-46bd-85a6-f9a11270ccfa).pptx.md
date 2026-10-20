# Vehicle 489 incident report (0971d2a7-5945-46bd-85a6-f9a11270ccfa).pptx

Attachment 15621, pptx, 777 KB, added 2023-07-31 by John Clark.

## Slide 1

Vehicle 489 (408 Center Wing)
Incident Log Analysis
J Clark
7/11/2023
Updates
7/31/2023

## Slide 2

Summary
Aircraft 489, operating with 408 wing set, transitioned for vertical landing and the forward rotors did not immediately start. Aircraft pitched hard nose down, lost 100 feet of altitude and then recovered to vertical flight. Aircraft climbed back to landing pattern altitude, 200+ feet, and then taxied back to the PLZ where it performed a normal descent.

## Slide 3

Observation VTOL Logs are Corrupt
[picture]

## Slide 4

[chart: Throttles and Altitude at VTOL Transition]
Using Available Data from XComm to Determine Root Cause
Altitude loss AGL at VTOL Transition
VTOL Throttles 1&2 Full

## Slide 5

[chart: Throttles and Current and Voltage at VTOL Transition]
Using Available Data from XComm to Determine Root Cause
Current at VTOL Transition. Throttles 1&2 are at maximum

## Slide 6

[chart: Throttles and Pitch and Roll at VTOL Transition]
Using Available Data from XComm to Determine Root Cause
Pitch and Roll at VTOL Transition

## Slide 7

Initial Conclusion:
The front motors, 1 and 2, were making no power at 8848 when the rears turned on. Vtol current is very low while the front throttles are railed from 8848-8850.
The lift from the front motors from 8848-8850 is insufficient to prevent the aircraft from pitching and rolling into a dive.
Current is available after 8852 and the aircraft recovers.

## Slide 8

Updates Since Root Cause Findings:
Finding: The nylon screw (P/N: 100-102984) that fastens the ballast weight (p/n: 107-102859) to the VTOL AP interface board (P/N: 107-107306) sheared off. 
During the incident flight when the vehicle pitched up to transition to VTOL landing, the ballast weight swung to the extreme of its arc, making contact with pin 8 of T4 and the GND pad of C60.
This would cause the TX5_N ethernet line that is designated for main vehicle communication to be pulled to ground.
Engineering conducted an additional investigation to help tie vehicle loss of pitch control with ballast weight contact.

## Slide 9

Updates Since Root Cause Findings:
Proposed Finding: Loss of Ethernet Tx Contributed to Vehicle Loss of Control.
Contrary Finding in Analysis: The observed Loss of Ethernet Connectivity occurs significantly after the pitch and roll events that cause altitude loss.
Altitude Loss begins at prior to 8850 seconds of flight.
Ethernet Loss of connectivity does not start until after 8860 seconds of flight.

## Slide 10

Proposed Loss of Ethernet Connectivity
[chart: Ethernet Sw #1]
Transmit Data Loss in Incident Timing Window

## Slide 11

Proposed Loss of Ethernet Connectivity
[chart: Ethernet Sw #2]
Transmit Data Loss in Incident Timing Window

## Slide 12

Proposed Loss of Ethernet Connectivity
[chart: Ethernet Sw #1 to Sw #2]
Complete Loss of Connectivity Sw 1 Sw 2 in Incident Timing Window

## Slide 13

Updates Since Root Cause Findings:
Finding: Loss of Ethernet Connectivity Occurred Throughout the Flight.

## Slide 14

[chart: Ethernet Sw #1 to Sw #2]
Loss of Ethernet Connectivity
Complete Loss of Connectivity Sw 1 Sw 2 in Flight Prior to Incident
