# AC556_Investigation.pptx

Attachment 22228, pptx, 3691 KB, added 2024-07-31 by Wesley Reynolds.

## Slide 1

Investigation Report
AC556 – VTOL Landing Transition at 2500ft AGL

Author: Flight Systems Team
July 30, 2024
[picture]
[picture]

## Slide 2

Summary – Statement from Operator
Verbal Statement from Operator
Vehicle transitioned to VTOL landing at 2500 ft AGL.
Operator unable to abort.
HLB depleted and vehicle crashed.
Written Statement from Operator
During a test flight at Ft. Liberty, NC, a Stalker VXE-30 (Group 2 sUAS) appeared to suffer a failure in the battery system that led to vertical takeoff/landing (VTOL) propulsion failure during the landing phase of flight. The propulsion failure resulted in the aircraft losing lift and crashing from approximately 1200 ft in altitude and 200m away from the intended landing point.
When the Operator commanded the Stalker to RTB, the crew said it went to its preplanned mission points and started to descend at around 2500 ft AGL. The Stalker VXE-30 should transition into its vertical take-off/ landing (VTOL) at around 100-300 ft AGL. Once the Operators saw the Stalker transition into VTOL at a higher altitude (1200 ft AGL), they immediately tried to abort the landing but were unable to due to the software ghosting out the option. Before crashing, the crew tried everything they could to put the Stalker into fixed wing flight but were unsuccessful.

## Slide 3

Summary – Statement from Edge Autonomy Flight Systems Team
Conclusion from Edge Autonomy Flight Systems Team
The vehicle was not commanded to RTB.
The vehicle was commanded to GoTo IP4.
The vehicle transitioned to VTOL Landing around 2,500 ft AGL. The VTOL battery system does not support a transition to VTOL Landing from this altitude.
The VTOL battery system did not fail. The VTOL battery system ran out of energy as expected after a VTOL Landing from this altitude.
Once the VXE30 has transitioned to VTOL Landing, there is no option to Abort Landing. This is intentional as the VTOL battery system does not have the energy capacity to support this.
Plans to Mitigate Issue in the Future
The GCS can implement checks that will warn the operator if they issue a command to the vehicle that will cause a transition to VTOL Landing at an unsupported altitude.
The operator can avoid using the GoTo command to trigger a landing in favor of using the RTB command. The IP2 waypoint in the landing pattern is critical to ensure that the vehicle descends to a safe altitude before beginning the transition to VTOL Landing.

## Slide 4

[picture]
Log Analysis – XComm Event Log
The XCEVLOG.TXT file is the XComm event log.
This is a log of all the important events that occurred in the XComm system onboard the vehicle.
At approximately 17:24 UTC (or 3,909 seconds after the vehicle was powered on), the operator issued a GoTo command to command the vehicle to GoTo the waypoint IP4.
The explanation for why “GoTo m,w 1 3” represents a command to GoTo IP4 is in the following slides.
Approximately 43 seconds after the GoTo command was issued, the vehicle began to transition to VTOL Landing.

## Slide 5

[picture]
Log Analysis – XComm Event Log – Explanation
In the source code for the XComm system, there is only one code path that can log a message of the form “GoTo m,w X Y”.
The stack trace for how the cmd data gets filled is very long and beyond the scope this report, but the following slides present the core logic used to fill this data.

## Slide 6

[picture]
Log Analysis – XComm Event Log – Explanation – Continued
Every waypoint in a mission is defined using 2 parameters.
Parameter 1 represents which pattern the waypoint is in. The patterns are represented by an enumeration where Launch=0, Primary Landing=1, Alternate Landing=2, etc.
Parameter 2 represents which waypoint within the pattern is being referenced. This waypoint indexing begins at 0. That is to say that the first waypoint in a pattern will have Parameter 2=0, the second waypoint in a pattern will have Parameter 2 = 1, etc.
Thus, the unique waypoint with Parameter 1=1 and Parameter 2=3 is the fourth waypoint in the Primary Landing Pattern. This corresponds to the waypoint called IP4. 
It follows that the message “GoTo m,w 1 3” represents the command to GoTo the waypoint IP4.
[picture]

## Slide 7

[picture]
Log Analysis – GCS Event Log
The T95_V556_240715_131205_event.txt file is the GCS event log.
This is a log of all the important events that occurred in the GCS Software that runs on the SGCS1 Laptop.
At approximately 12:22:23 EDT (time is taken from the clock on the SGCS1 Laptop), the GCS Software was started.
This information is relevant to the following slide.

## Slide 8

[picture]
Log Analysis – GCS Event Log – Continued
Approximately 63 minutes after the GCS Software was started, the vehicle was issued a command to GoTo the 4th waypoint in the Primary Landing Zone mission.
63 minutes and 31 seconds after 12:22:23 EDT is equivalent to 13:25:54 EDT. This is equivalent to 17:25:54 UTC. This is the time in which the incident of concern occurred.
The 4th waypoint in the Primary Landing Zone mission is the waypoint titled IP4.

## Slide 9

[picture]
Log Analysis – GCS Event Log – Continued
This is a GCS event log that was created to illustrate the system behavior. It was not one of the files submitted by the customer.
When an RTB command is issued, an entry into the GCS event log is created that states “RTB Now Command – primary LZ active”.
It could say “RTB Now Command – alternate LZ active” if the alternate LZ was indeed active.

## Slide 10

[picture]
Log Analysis – GCS Event Log – Continued
These are screenshots of the GCS event log that was submitted by the customer.
There are two entries in the GCS event log file of the form “RTB Now Command – primary LZ active”. However, both entries were generated by different flights than the one being considered for this investigation.
Neither of this flights occurred on 07/15/24, the date of the incident.
[picture]
[picture]
[picture]

## Slide 11

[picture]
Timeline – When Descent Began
This is a graph that plots the CPU Time since the XComm began (Blue) and the recorded Barometric Altitude (Red).
The scale on the left is number of seconds since the XComm began.
The scale on the right is AGL altitude in feet of the vehicle.
The cursor show where the 3,915.095 second mark is.
Around 3,915 seconds after the XComm began, the vehicle began to descent rapidly. Prior to this, the vehicle maintains altitude as would be expected during fixed-wing flight.
This information lines up with the observations made previously in the XComm Event Log.
GoTo command issued at CPU Time=3,909 s.
Vertical descent began at CPU Time=3,937 s.

## Slide 12

Conclusions
The vehicle was not commanded to RTB.
When the vehicle is commanded to RTB, the message “RTB Now Command – primary LZ active” is logged in the GCS event log. This message was never logged during the flight in which the incident occurred.
The vehicle was commanded to GoTo IP4.
Approximately 63 minutes after the GCS Software was started, the message “Change active waypoint: : Mission: Primary LZ  Waypoint: 4” was logged in the GCS event log. This means the vehicle was commanded to GoTo IP4.
This caused the vehicle to skip IP2. IP2 is a descending orbit that is critical to ensure that the transition to VTOL Landing occurs at a safe altitude.
The vehicle transitioned to VTOL Landing around 2,500 ft AGL.
Standard procedure is to transition into vertical descent at 300 ft AGL. Vertical transition altitude adjustment (higher and lower) is not recommended. See section 1.2.3 Landing Requirements in the VXE30_Operations_Manual.
The VTOL battery system did not fail.
The VTOL battery system ran out of energy as expected after a VTOL Landing from this altitude.
Once the VXE30 has transitioned to VTOL Landing, there is no option to Abort Landing.
This is intentional as the VTOL battery system does not have the energy capacity to support this. See the graphic in section 1.2.3 Landing Requirements in the VXE30_Operations_Manual.

## Slide 13

Next Steps
The GCS can implement checks that will warn the operator if they issue a command to the vehicle that will cause a transition to VTOL Landing at an unsupported altitude.
This will not prevent the operator from commanding a transition to VTOL Landing at an unsupported altitude, but it will make it clear that preforming this transition will risk crashing the vehicle. Thus, the operator will have to explicitly allow this risky action, and they cannot do it by accident.
The operator can avoid using the GoTo command to trigger a landing in favor of using the RTB command.
The IP2 waypoint in the landing pattern is critical to ensure that the vehicle descends to a safe altitude in fixed-wing flight before beginning the transition to VTOL Landing.
