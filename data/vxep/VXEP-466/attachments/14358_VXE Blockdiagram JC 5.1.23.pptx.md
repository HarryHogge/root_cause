# VXE Blockdiagram JC 5.1.23.pptx

Attachment 14358, pptx, 54 KB, added 2023-05-03 by John Clark.

## Slide 1

Old VXE Architecture
XCOMM
AP 
VTOL
Radio
Link
Air
Data
FW AP
Mag
GPS
CAN
Pwr
RS232
Lift Motor
Pwr Sensors
(Fuselage)
Eth
Pwr
Fwd Motor,
Servos
Pwr Sensor
(wing)
Pwr
Pwr
Wing
Fuselage
Eth
ST10F168

## Slide 2

New VXE Architecture with FW AP VTOL Combined
XCOMM
AP
VTOL+FW
Radio
Link
Air
Data
Not AP
CAN to servo
IMU to CAN
Analog to CAN
Mag
GPS
CAN
Pwr
RS232
Lift Motor
Pwr Sensors
(Fuselage)
Eth
Pwr
Fwd Motor,
Servos
Pwr Sensor
(wing)
Pwr
Pwr
Wing
Fuselage
Eth
NOT AP is a new PIC32
Using AP Interface Board
VTOL AP PCB
Current path under implementation
Unifies FW and VTOL

## Slide 3

New VXE Architecture with FW AP Discrete From VTOL
XCOMM
VTOL AP
Radio
Link
Air
Data
FW AP
CAN to servo
IMU to CAN
Analog to CAN
Mag
GPS
CAN
Pwr
RS232
Lift Motor
Pwr Sensors
(Fuselage)
Eth
Pwr
Fwd Motor,
Servos
Pwr Sensor
(wing)
Pwr
Pwr
Wing
Fuselage
Eth
FW AP is a new PIC32
Using AP Interface Board
VTOL AP PCB
No time savings but doable

## Slide 4

Proposed VXE Architecture Temporary
XCOMM
AP 
VTOL
Radio
Link
Air
Data
Mag
GPS
CAN
Pwr
RS232
Lift Motor
Pwr Sensors
(Fuselage)
Eth
Pwr
Fwd Motor,
Servos
Pwr Sensor
(wing)
Pwr
Pwr
Wing
Fuselage
Eth
Existing FW AP
Running on Red 
Board
Possibly faster to implement
Uses same debug environment as New VXE
Provides parallel path for development
Ports existing code with known functionality
Already works with XComm and JAI GCS
Uses New VXE Interface board
Needs additional resource 
Will need: 
UART and PWM drivers 
NVM Handler
SPI driver
Pros:
Cons:
