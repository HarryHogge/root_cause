# AC 533-NCR-240617 Aborted TO after start of transition-Initial-Analysis.pptx

Attachment 27069, pptx, 695 KB, added 2025-03-11 by Jason Scherer.

## Slide 1

NCR 240617 - 3540 (v533)
Aborted TO after start of transition
Initial Analysis of flight data
Jason Scherer

## Slide 2

Summary
V533 successfully launched and climbed to the commanded altitude of ~310’ AGL before the fixed wing autopilot detected a loss of uplink and commanded a launch abort. The vehicle was in launch state 13 “wait for threshold airspeed, monitor timeout, health” prior to the abort.
Launch abort resulted in a successful landing.
GCS logs don’t really show indication of loss of datalink during time of abort. However, XComm logs do show indication of a drop in traffic on the network port connecting XComm to the datalink radio.
Fixed Wing maintains uplink status by updating a timestamp variable when various GCS messages are received. If one of the monitored messages are not received with ~5 second window the uplink is considered lost.
[picture]
vtRelAlt

## Slide 3

Lost link during transition on launch
[picture]
[picture]
0010 1001 0100 1111
vt status: 10575 = 0x294F
[picture]
[picture]

## Slide 4

[picture]
[picture]
[picture]
ManageLostLink() is called from Cvtol::Poll() which runs @10Hz
[picture]
UplinkStatus is a short declared in hostintf.cpp that is used to track uplink status.
hostintf.cpp
[picture]
Initialized to FALSE
Fixed Wing AP Firmware
[picture]
[picture]
Updated on line 4780 after parsing a serial message with address of ADDR_VEHICLE
[picture]
[picture]
Called when receiving various types of messages from the GCS where “sec” is set to “ONLINE_TIME” which is defined as 5
NewUplinkFrequency() sends three sys_queries and waits 2 seconds
If was good and now bad
Clear buffer and restart the serial port
Check link status again
[picture]

## Slide 5

[chart: Lift Throttles]
[chart: Uplink Rx - netS2P4RxComm]
Launch Abort
Decrease in RX traffic on XComm

## Slide 6

[chart: Lift Throttles]
[chart: Uplink Rx - netS2P4RxComm]
[chart: XCom<->FWAP Serial Traffic]
Launch Abort
Decrease in RX traffic on XComm results in a decrease of traffic on the serial port connected to FWAP

## Slide 7

GCS Data Log
[chart]
Launch Abort
[chart: GCS Uplink Tx/Rx]
[chart]
