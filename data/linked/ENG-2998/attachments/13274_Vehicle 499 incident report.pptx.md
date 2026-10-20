# Vehicle 499 incident report.pptx

Attachment 13274, pptx, 70 KB, added 2023-03-27 by John Clark.

## Slide 1

Vehicle 438
Incident Log Analysis
J Clark
3/27/2023

## Slide 2

Summary
First Failed Flight:
The launch wizard was completed without incident and the aircraft was armed for launch. The aircraft appeared to liftoff about one foot before aborting and landing to the left of the stand. The VTOL system was still armed (red light flashing). The VTOL control window indicated a launch abort for a VTOL system failure. 
Log for this flight indicated a Magnetometer Fault
[23:58:48.452 3111.452] DebugMsg Climb abort, VTOL controller fault
[23:58:48.453 3111.453] DebugMsg   Sensor: magnetometer fault
[23:58:48.454 3111.454] DebugMsg RTL

## Slide 3

Summary
Second Failed Flight:
On this flight the aircraft lifted to approximately two feet and again aborted. After landing the VTOL system stopped, but because of the angle it could not be immediately determined if the system was still armed. A few seconds after touching down the lift rotors briefly spun up and stopped. The VTOL control window indicated a launch abort for a VTOL system failure and a magnetometer error. 
Log for this flight also indicated a Magnetometer Fault
[00:12:48.313 3951.313] vtol fault during climb, RTL
[00:12:48.314 3951.314] DebugMsg Climb abort, VTOL controller fault
[00:12:48.315 3951.316] DebugMsg   Sensor: magnetometer fault

## Slide 4

Supporting Evidence Gathered from: VT414_230320_201705_vtl00046
Yaw Angle measurement from Magnetometer at Launch
[chart]
