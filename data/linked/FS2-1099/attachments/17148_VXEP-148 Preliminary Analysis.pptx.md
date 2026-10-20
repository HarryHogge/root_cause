# VXEP-148 Preliminary Analysis.pptx

Attachment 17148, pptx, 3022 KB, added 2023-11-01 by Jason Scherer.

## Slide 1

VXEP-148 Preliminary Analysis
AC 401 loss of control and crash – Jason Scherer

## Slide 2

Reported Data
From the customer: Re-cap:  We are testing a payload in heavy weight configuration with antennas mounted on the outer wings.  We have noticed that when in VTOL, there is oscillations causing the wings to flap up and down. The pilot aborted take-off and tried to move the aircraft.  From the pilots perspective, he said he no longer had control of it at that point.  It stayed in the air and wouldn’t come down and he couldn’t adjust its location.  The plane hovered for a while and then started to drift towards a building near the runway.  Once it was over the building it then began to descend trying to land.  It softly landed on the building but then slid down the gable and hit the ground.  Damage included breaking a tail and props.  Further analysis is needed to check structure of components.  We are trying to source repair parts but one concern is the autopilot in 401, we have lost confidence unless we know what caused the lack of control.

## Slide 3

Analysis Summary
During a customer flight (v401) experienced a wing oscillation (flapping) which is suspected to be due to vehicle weight exceeding MAGTOW. 
The vehicle launched vertically to about 35’ AGL.
The launch was aborted using the launch abort feature of the GCS.
The vehicle remained in the air for ~2 more seconds before a “Land Immediately” command was issued from the GCS.
The vehicle then switched from RTL to ALT_HOLD then back to DESCENT. During this transition, the update mode was switched to only update attitude until the remainder of the descent which caused a landing drift.

## Slide 4

Firmware Versions
XComm: V4.67.XEVT
VTOL: V1.52

## Slide 5

[picture]
VTOL Flight Sequence
~3 Sec Launching
~11 Sec Launched
~68 Sec Landing
Landed
35’ AGL (LRF)

## Slide 6

VTOL States
[picture]
Descent
Takeoff
Land Prep
Descent
Landed
[picture]
Transition
[picture]
Climb

## Slide 7

[picture]
[picture]
Position Drift during descentMulti_Mode (fmMc): Never goes back into position update mode
AC Position 
starts to deviate
MULTI_MODE_POSITION
MULTI_MODE_ATTITUDE
[picture]
[picture]
fmMc should change to position mode in mclandTrigger
fmMc changes to
Attitude mode here
ap_mavlink.c
ap_mavlink.c

## Slide 8

First RTL
[picture]
[picture]
[picture]

## Slide 9

Second RTL
[picture]
[picture]
[picture]
[picture]
Switch to Attitude update mode
[picture]

## Slide 10

[picture]
[picture]
[picture]
“Event 5”
[picture]
[picture]
Rcinput.c
[picture]

## Slide 11

Crash Dive Activated
[picture]
[picture]
[picture]
[picture]
[picture]
GCS Source
FW AP Source
[picture]
Xcomm Message Log
[picture]
GCS Debug Log
[picture]
GCS Event Log

## Slide 12

[picture]
Code locations that set mc mode to Position
MultiControl.cpp

## Slide 13

Places where we enter mcmode Position
[picture]
[picture]
[picture]
[picture]
[picture]
[picture]

## Slide 14

MultiControl.cpp
MultiControlHandleRcEvent(CONTROL_EVENT_MODE4)
multiControlPosMode()
[picture]
[picture]
[picture]
Flight AnalysisCode paths to multiControlPosMode()
MultiLand.c
mclandTriggerRTL()
mclandTrigger()
MultiLaunch.c
mclaunchTrigger()
ap_mavlink.c
handleMessage() 
Case: MAVLINK_MSG_ID_SET_POSITION_TARGET_GLOBAL_INT
[picture]
Starts during landing but never executes
See slide 11
Fully Executes
during launch
[picture]
Fully Executes 3 times
during launch
Executes right after launch
[picture]
[picture]
never executes
[picture]
Immediately next in the log

## Slide 15

MultiControl.cpp
multiControlPosVelMode()
Code paths to multiControlPosVelMode()
ap_mavlink.c
handleMessage() 
Case: MAVLINK_MSG_ID_SET_POSITION_TARGET_GLOBAL_INT
[picture]
Messages are received during launch, but the program never reaches into this if statement
[picture]

## Slide 16

McLand Trigger
[picture]
Code gets here
Code Never Gets here
[picture]
[picture]
[picture]
[picture]
During the second RTL mclandTrigger() is again called, but this time the state is already landing causing the execution to return false on line 152. This prevents the switch from attitude update mode back to position update mode.

## Slide 17

HIL “Recreation”
[picture]
MULTI_MODE_POSITION
MULTI_MODE_ATTITUDE
AC Position 
starts to deviate
Start Landing
End Landing
To recreate this issue in the HIL I simply launched a normal flight, then aborted that flight using the GCS “Abort Launch” capability. Finally, before the descent was complete, I issued a “Land Immediately” command from the GCS which results in a second RTL, switch to attitude update mode, and the horizontal landing drift.
[picture]
[picture]
[picture]

## Slide 18

HIL Patched
I patched the VTOL firmware with the above changes to let the execution proceed during the second RTL to a point where the mode can be switched back to position update.
[picture]
[picture]
MULTI_MODE_POSITION
MULTI_MODE_ATTITUDE
MULTI_MODE_POSITION
Start Landing
End Landing

## Slide 19

Questions
Should we allow the “Land Immediately” command to be sent during an already aborted launch?
Should we prevent the McLandTrigger() function from executing a second time during a landing.
Is the patched update used in my HIL testing an appropriate solution to this issue?
Why should the AC switch to attitude update versus position update during an ALT_HOLD mavlink update. Is this the desired behavior?

## Slide 20

Log Analysis
The following slides are the result of log analysis to validate the code execution flow during the real flight.

## Slide 21

RTL after launch
[picture]
Commanded AGL ~209 ft
Launch detected / complete
Updated mode
Climb State Active
RTL Trigger
RTL – AGL Landing Mode
Start of Landing Phase
Begin Descent
[picture]
~7 Seconds
VTOL Message Log
XComm Message Log
Logs keep going and the second RTL is activated

## Slide 22

[picture]
VTOL State Changes
[picture]
[picture]
[picture]
[picture]
[picture]
[picture]
[picture]
[picture]
[picture]
~4 seconds
~10 seconds
~8 seconds
~22 seconds
~1 seconds
~8.4 seconds
~37 seconds
~13.29 minutes
[picture]
RTL Trigger
[picture]
<-81 Times
[picture]
[picture]
[picture]
[picture]
[picture]
[picture]
[picture]
[picture]

## Slide 23

XComm during Descent Phase
[picture]
[picture]
~2 Seconds
[picture]
~21 Seconds
[picture]
~2 Seconds
~25 Seconds

## Slide 24

[picture]
Mc Land Pause
[picture]
[picture]
[picture]
[picture]
[picture]
Second RTL?

## Slide 25

NAK 193
[picture]
[picture]
ap_mavlink.c
[picture]
[picture]
[picture]

## Slide 26

Xcomm Sends MAVlinkpause message to VT
[picture]
[picture]
ApmParser.c

## Slide 27

VT receives pause MAVlink message
[picture]
[picture]
[picture]
Multiland.cpp->mclandPause()
ap_mavlink.c->handleMessage()

## Slide 28

FW AP
[picture]

## Slide 29

XComm Log Errors
[picture]

## Slide 30

VTOL Messages During Landing
[picture]

## Slide 31

VTOL Log Errors
[picture]
[picture]
[picture]
[picture]

## Slide 32

Event Log Faults
[picture]
[picture]

## Slide 33

Reference Slides
[picture]
[picture]

## Slide 34

[picture]

## Slide 35

Landstate 3
[picture]
[picture]
[picture]
