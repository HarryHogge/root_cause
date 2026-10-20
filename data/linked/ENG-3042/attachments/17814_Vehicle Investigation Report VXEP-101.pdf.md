# Vehicle Investigation Report VXEP-101.pdf

Attachment 17814, pdf, 1116 KB, added 2023-12-12 by Pat Wells.

## Page 1

1
Investigation Report
VXEP -101
V487
Author: Jason Scherer
Dec 11, 2023

## Page 2

2
Investigation Overview – Status: Investigation Ongoing - [Updated 2023-12-11]
Edge Autonomy Proprietary Information
Motors stopped at 90ft 
during VTOL landing
V X EP- 101
v 4 0 1
Connector Failure WD ResetOld Firmware
Investigated but inconclusive
Not the root cause or contributing factor
Root cause or contributing factor
Old firmware 
installed
Next Step s : 
1. R e v i e w  I n v e s t i g a t i o n  R e p o r t
C o n c l u s i o n  &  C o r r e c t i v e  Ac t i o n:
1. M o s t  l i k e l y  t h e  r e s u l t  o f  a  f a i l e d  c o n n e c t o r
JScherer
 The VTOL Debug Message 
Log was not able to be 
recovered
JScherer
VTOL Flight Data indicates a possible 
connector failure. Connector has damage. 
Connector failed resistance checks
JScherer
AP Connection Faults
Logs show multiple AP link faults 
indicating possible wire/hardware 
failure in Avionics
Loss of Control

## Page 3

3
-200
0
200
400
600
800
1000
1200
1400
Utc
201020.873
201024.173
201027.473
201030.773
201213.073
201437.472
201440.673
201443.973
201447.273
201450.573
201453.873
201457.173
201500.473
201503.773
201600.273
201603.573
201606.873
201610.173
201613.473
201616.773
201620.073
201623.373
201626.673
201629.973
201633.273
201636.573
201639.873
201643.173
201646.473
201649.773
201653.073
201656.373
201659.673
201702.973
201706.273
201709.573
201712.873
201716.173
201719.473
201722.773
202103.873
202633.873
203203.873
203733.873
204303.873
204833.873
205403.873
205933.873
210503.873
211033.873
211603.873
212133.873
212703.873
213233.873
213803.873
214333.873
214903.873
215433.873
220003.873
220533.873
221103.873
221633.873
222203.873
222559.273
222602.573
222605.873
222609.173
222612.473
222615.773
222619.073
222622.373
222625.673
222628.973
222632.273
222635.573
222638.873
vtRelAlt (XCOM Flight Log) VTOL LandingFixed Wing FlightVTOL Launch
Overall Timeline
Launch 
detected
HLB Voltage 
Dropout ~110’ AGL
~31 Seconds ~2hrs, 9min, 30sec ~41 Seconds
Altitude as reported by the
VTOL AP and recorded by
XComm

## Page 4

4
Summary [Updated 2023-12-11 JScherer]
Reporter: Jason Scherer
Severity: 1 – System Failure - No Workaround
Edge Autonomy Proprietary Information
Aircraft 487 successfully launched 
and transitioned to fixed wing flight. 
Fix winged flight lasted for ~2hrs, 10 
min before successfully 
transitioning back to VTOL flight. 
During descent from VTOL the HLB 
voltage dropped to as low as 7.5V. 
This occurred at approximately 110’ 
AGL resulting in the lift system 
failure. The flight data, visual 
inspection, and connector tests 
point to a connector failure as the 
most likely culprit for the incident.
Damaged Connector
HLB voltage dropout at end of flight

## Page 5

5
XComm Loss of Control Shutdown
XComm debug message log shows multiple XComm-AP link failures
Xcomm Debug Message Log
The XComm debug message log shows a final error 
message indicating loss of control and issues a 
shutdown command
Xcomm Debug Message Log – Loss of Control

## Page 6

6
AP Link Faults
XComm debug message log shows multiple XComm-AP link failures
Xcomm Debug Message Log Xcomm Debug Message Log
The XComm debug message log shows multiple link 
dropouts to the fixed wing AP . These connections 
are recovered. The outage occurs in the direction of 
sending data to the AP . Possibly resulting from a 
faulty cable.

## Page 7

7
Old Firmware
Air vehicle 487 was operating old firmware with known issues
Old Firmware Installed Service Bulletin VXE -SB-23-014
Supported Firmware
Firmware Installed
• Fixed Wing Autopilot: 6.05j
• XComm Processor: V4.60
• VTOL Autopilot: 1.44
Supported Firmware (VXE-SB-23-014)
• Fixed Wing Autopilot: 6.05m
• XComm Processor: V4.67
• VTOL Autopilot: 1.53

## Page 8

8
Connector Failure
Log data, visual inspection, and resistance testing point to a failed connector as the most likely culprit for the lift failure
VTOL Log data shows a simultaneous voltage and current dropout Visual Inspection – Damaged Connector
Connector FailedResistance Measurement
• Initial resistance measured: 305uOhms
• After cleaning measured 253uOhms
• Pass value is less than 180uOhms in production, 235uOhms in field
Current Drop
Voltage Drop
Current Drop

## Page 9

9
BACKUP
