# Vehicle 401 incident report.pptx

Attachment 14131, pptx, 6823 KB, added 2023-04-21 by John Clark.

## Slide 1

Vehicle 401
Incident Log Analysis
J Clark
4/20/2023

## Slide 2

Summary Final Flight V401 230419 134913
Notes from PIC :
crash landing, VTOL failure 10-15 off ground during landing, catastrophic damage.

## Slide 3

Summary Final Flight V401 230419 134913
Previous Flight Logs indicate system power abnormalities in Landing Phase.
[21:22:58.607 2183.607] DebugMsg Climb abort, lift system fault
[21:22:58.608 2183.609] VT pwr fault: land bv min pwr diff thr  0x31
[21:23:00.223 2185.223] DebugMsg Climb abort, lift system fault
[21:23:00.224 2185.225] VT pwr fault: land bv min pwr  0x21
The above messages indicate Battery Voltage (bv) Power Faults and are causing lift system failure.

## Slide 4

Summary Final Flight V401 230419 134913
The Logs associated with the Final Flight strongly indicate complete power failure in the VTOL Lift System

## Slide 5

Summary Final Flight V401 230419 134913
This Chart illustrates the relationship between: 
Autopilot Main Battery Voltage (apVbatt)
VTOL System reported Lift Battery Voltage (vtVbatt)
Autopilot reported AGL (apAgl)
[chart: Final Flight V401 230419_134913]

## Slide 6

Summary Final Flight V401 230419 134913
This Chart illustrates the Roll Axis over the same period as the previous slide: 
Autopilot Main Battery Voltage (apVbatt)
[chart: apEr Ap reported attitude estimate, roll axis, degrees
]

## Slide 7

Conclusion:
The VTOL Lift System appears to have suffered rapid loss of Voltage approximately 10’ above final level. 
As VTOL Power was lost the VTOL Autopilot reported rolling quickly to around 60 degrees.
