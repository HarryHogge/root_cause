# microDRIVE_LP_Datasheet_V1_0 (2).pdf

Attachment 63741, pdf, 1892 KB, added 2026-07-28 by Jeremy Kostel.

## Page 1

Datasheet
Version 1.0
Updated 16/02/24
hargravetechnologies.com
microDRIVELP

## Page 2

microDRIVE LP
Contents
01 Safety 2
02  At a Glance 3
03  Specifications 4
04  Performance 6
05  Quick Start 8
06  Integration 9
07  States 11
08  Safety Features 12
09  Errors/Warnings 13
10 Ordering Options 15
11 Pinouts 16
12  Powered by GateKEEPER 17
13  Revisions 18
14  Disclaimer 18
01 Safety
Motor controllers channel substantial power. Fault currents can 
exceed 1 kA and while extremely rare, major failures can result in 
fire. Design your vehicle accordingly. ESCs should be fused from 
batteries and isolated from flammable components.
Always ensure you are connecting the motor controller with the 
correct polarity. Failure to do so can result in a fire.
Never exceed the rated voltage of the motor controller. Failure to 
do so can result in premature failure or a fire.
microDRIVE LP is rated for submersion in fresh water at 1 m (3ft) 
depth for 30 minutes. Exceeding this can result in unit failure.
Do not attempt to disassemble or modify the product in any way. 
Doing so will void your warranty and more importantly, cause 
damage that results in a failure.
This controller will regeneratively brake by default. Synchronous 
rectification must be turned off to use it with a one-way power 
source.
Do not extend the leads beyond recommended values without 
consulting Hargrave. This may result in insufficient capacitance 
and subsequent failure.
While there are multiple fail safes in place, it should be assumed 
that a powered ESC can start a motor at any time. Take 
appropriate precautions.
This is not the sort of safety page you skip!
We take the utmost care in development 
and assurance of our products, but power 
electronics have inherent risk. Used 
improperly, there is risk of fire, serious  
injury and damage to property. 
Please read this datasheet carefully prior  
to integration.
HARGRAVE TECHNOLOGIES             Datasheet Version 1.0 February 2024
2
01 SAFETY

## Page 3

microDRIVE LP
02 At a Glance
15 - 60 V
INPUT  
VOLTAGE
60 A
CONTINUOUS  
CURRENT
FOCAL
+ TRAPEZOIDAL
DroneCAN
+ DSHOT, PWM
94 g
BASE WEIGHT
IP67
PROTECTION
microDRIVE LP is the smallest unit in our DRIVE 
Series, optimised for minimum weight and a 
micro form factor. 
With a modern communications and telemetry 
suite and advanced environmental protection, 
microDRIVE LP is ready to tackle the most 
demanding UAS applications.
HARGRAVE TECHNOLOGIES             Datasheet Version 1.0 February 2024
3
02 AT A GLANCE

## Page 4

microDRIVE LP
1
A
2 3 4 5 6 7 8
1 2 3 4 5 6 7 8
B
C
D
E
F
A
B
C
D
E
F
THIS  DRAWING  IS  CONFIDENTIAL.  BOTH  IT
AND  THE  COPYRIGHT  IN  THE  DRAWING  ARE
THE  PROPERTY  OF  HARGRAVE INDUSTRIES
PTY LTD AND  MAY  NOT  BE REPRODUCED
OR OTHERWISE  USED  WITHOUT  THE
WRITTEN CONSENT OF THE OWNER. DO NOT SCALE DRAWING
Qty Weight Material
Title
Scale Created by
Approved by
Drawing Number
Rev. Date of issue Sheet
2/09/2023
1/5
100454
Quang Le1:5
81 [3.19]
85 [3.35]
38 [1.50]
42 [1.65]18 [0.71]
2[0.08]
A
A (1:1)4x Ø2.2 [Ø0.09] 
USB Type-C® 
RGB LED 
Electrical
PARAMETER (UNIT) VALUE NOTES
Nominal Power Supply Voltage (V) 15 – 60 [4S – 14S] The recommended operating range for the units.
Absolute Power Supply Voltage (V) 12 – 63 Breaching absolute limits will result in unexpected 
shutdowns or unit failures.
Rated Phase Current (A) 60 Indefinitely, refer to page 6 for performance data.
Peak Phase Current (A) 110 Appropriately cooled.
Voltage Measurement Accuracy (%) ± 5 Input voltage measurement accuracy across the  
full-scale range.
Current Measurement Accuracy (%) ± 5 Input current measurement accuracy across the  
full-scale range.
Decoupling Capacitance (µF) 550 Integrated capacitor bank for up to 3 m of input  
lead length.
Regenerative Braking ✓ Configurable operation.
Max. Regenerative Current (A) 60 Indefinitely, appropriately cooled.
Motor Temperature Sensing ✓ NTC or PTC supported, software configurable.
Isolated Serial Input and Output ✓ DShot/PWM are isolated, including telemetry.
Data Logging ✓ Configurable rate, automatic circular logging.
Hardware Self Tests ✓ Unit will test bridge hardware on power up.
Self-Correcting Memory ✓ Use of onboard backups and ECC memory.
03 Specifications
All dimensions in  
mm [inches].
See page 15 for cable 
lengths.
HARGRAVE TECHNOLOGIES             Datasheet Version 1.0 February 2024
4
03 SPECIFICATIONS

## Page 5

microDRIVE LP
Motor Control
PARAMETER (UNIT) VALUE NOTES
Minimum Switching Frequency (kHz) 4 Automatic switching, configurable range.
Maximum Switching Frequency (kHz) 64 Automatic switching, configurable range.
Commutation Types FOCAL and 
Trapezoidal Configurable motor control algorithm.
Efficiency Up to 99% Maximum achievable efficiency.
Maximum RPM (Trapezoidal) (eRPM) 500,000 2-pole motor speed.
Maximum RPM (FOCAL) (eRPM) 200,000 2-pole motor speed.
Bi-Directional Drive ✓ Throttle input can be mapped to cover reverse and  
forward rotation.
Protection Mechanisms ✓ Temperature (Bridge and Motor), Current, Voltage, 
Demagnetisation, RPM.
Propeller Parking ✓ Supports active parking with external hall sensor.
Sensorless Drive ✓ –
Sensored Drive Optional
Units have hardware capability for hall-effect sensored 
drive if motor cable is installed. This will become available 
as a firmware update. 
Motor Type BLDC, PMSM –
Communications
PARAMETER (UNIT) VALUE NOTES
CAN Bus Support DroneCAN Other protocols can be requested.
CAN Bus Termination ✓ Software-controlled termination resistor.
Telemetry ✓ CAN, Serial and PWM telemetry supported.
Firmware Updates ✓ USB and CAN interfaces are supported.
DShot Support DShot150 – 
DShot600 Standard and Bi-Directional DShot supported.
Servo PWM Support ✓ 50-499 Hz input frequencies supported.
Input Resolution 10-bit Resolution on DShot and PWM input signals.
Physical
PARAMETER (UNIT) VALUE NOTES
Weight (g) 94 [3.3 oz] Base weight only, not including cables.
Operating Temperature (°C) -20 – 110 
[-4 - 230°F]
Continuous operation above 85°C [185°F] may reduce 
lifetime of unit.
IP Rating IP67* *Internally validated, external certification pending.
Cables ✓ See page 15 for ordering options.
RGB Indication LED ✓ See page 11 for indications.
USB ✓ USB Type-C® for configuration and log access.
Configuration Tool ✓ USB or CAN accessible configuration.
NDAA Compliance Optional See page 15 for further details.
Country of Origin Australia –
RoHS/REACH Compliance ✓ –
HARGRAVE TECHNOLOGIES             Datasheet Version 1.0 February 2024
5
03 SPECIFICATIONS

## Page 6

microDRIVE LP
04 Performance
Many factors influence the final performance of an ESC in any 
real world use. This section is intended to provide a simplified 
method of evaluating ESC performance based on the most 
critical factors. Results from this method should be considered 
indicative only. 
Required Phase Current
It is important to make the distinction between bus current 
and phase current. Motor controllers are rated based on phase 
current, as this is the primary factor in thermal load. 
Our ESCs vary motor speed by changing the phase voltage.  
For a given input power, dropping phase voltage requires 
boosting the phase current. 
You can estimate the instantaneous phase current required 
using:
where: 
= Expected Bus Power. (W)
= Loaded* Motor KV. (rpm/V)
= Operational RPM. (rpm)
*Motor manufacturers typically report unloaded KV, whereas 
loaded KV should be used. Note this is often substantially 
different to unloaded KV.
Continuous Phase Current
The continuous phase current capability of the microDRIVE 
LP is dependent on a number of factors. You can calculate 
this using the nominal phase current rating, and condition 
modifiers, which you can determine using these steps: 
1. Calculate allowable temperature rise for your application. 
 
 We recommend a Tlimit of 85°C [185°F] for long term 
reliability.  
Up to 110°C [230°F] is available for short term use. 
2. Use the allowable temperature rise in the Temperature Rise 
Graph to work out Rated Phase Current.
3. From the Airflow, Ambient Temperature and Bus Voltage 
modifier graphs, determine your conditional phase current 
modifiers.
4. Multiply the calculated Rated Phase Current and 
conditional Phase Current Modifiers to determine the 
maximum continuous phase current. 
 
90
80
70
60
50
40
30
20
10
0
T emperature Rise (∆°C)
10
20
30
40
50
60
70
RATED PHASE CURRENT 
@ 50 V, 8 M/S AIRFLOW, 25°C AMBIENT
Phase Current (A)
T emperature Rise
HARGRAVE TECHNOLOGIES             Datasheet Version 1.0 February 2024
6
04 PERFORMANCE

## Page 7

microDRIVE LP
Transient T emperature Response
You can also calculate the transient temperature response 
using the following:
where:
= Ambient Temperature (°C)
= Temperature Rise, using Iphase (°C)
= Unit Temperature at t = 0 (°C)
= Thermal Time Constant (s)
= Time since start (s)
Speak to us
If you have any questions about performance in your 
application, reach out to our engineering team at:
contact@hargravetechnologies.com
Phase Current Multiplier
Ai/r_f.ligalow (m/s)
1.3
1.1
0.9
0.7
0.5
0
5
10
15
20
25
30
Airflow Modifier
Thermal Time Constant, τ (s)
Ai/r_f.ligalow (m/s)
800
700
600
500
400
300
200
2
4
6
8
10
Thermal Time Constant
15
20
25
30
35
40
45
50
55
60
1.1
1.0
0.9
0.8
0.7
Phase Current Multiplier
Bus Voltage (V)
Trapezoidal
FOCAL
Bus Voltage Modifier
1.50
1.30
1.10
0.90
0.70
0.50
0.30
0.10
Phase Current Multiplier
-40
-20
0
20
40
60
80
100
Air Temperature (°C)
Air T emperature Modifier
HARGRAVE TECHNOLOGIES             Datasheet Version 1.0 February 2024
7
04 PERFORMANCE

## Page 8

microDRIVE LP
05 Quick Start
Wiring
 • If using a tethered system or unidirectional power supply for 
input power, confirm the AFW setting is disabled.
 • Check VCC is supplied when using DShot or PWM.
Configurator
Try our guided Quick Start and configure your 
microDRIVE LP with the Hargrave Configurator Tool at:
configurator.hargravetechnologies.com 
All settings are also available over DroneCAN.
Communications
 • When using CAN Bus communication, ensure CAN Bus 
is enabled. The unit will use DroneCAN for control and 
telemetry. The input of DShot and PWM is disabled. 
Disabling this setting enables other protocols.
 • If using CAN, set the DroneCAN ESC Index as per the flight 
controller output number. This designates the ESC position 
within the system/aircraft.
 • Set the motor pole pairs setting to match the motor 
connected, such that mechanical RPM is reported (rather 
than electrical RPM).
 • Enable the CAN terminator on the unit furthest away from 
flight controller if no other CAN devices are terminating the 
bus.
Mounting
 • Ensure cables are externally strain-relieved for long-term 
reliability.
 • Minimise cable bending radii. Tight bending at the seal may 
promote water and dust ingress.
Protection Systems
Activation of protection mechanisms may 
cause unexpected system responses, 
including motor shut down. It is important you 
understand these behaviours and configure 
them for your system. You can find more 
information on page 12.
Documentation
You can find more detailed operational information in 
our product documentation at:
docs.hargravetechnologies.com
This quick start guide is a helpful starting point 
for integrating the microDRIVE LP into your 
system, but by no means exhaustive. 
Please read the datasheet and online 
documentation before full vehicle testing.
HARGRAVE TECHNOLOGIES             Datasheet Version 1.0 February 2024
8
05 QUICK START

## Page 9

microDRIVE LP
06 Integration
Unidirectional Power Supplies
If you are using the inverter with a power source that is not 
able to sink current, such as a unidirectional power supply, it 
is critical that you disable synchronous rectification. This is 
to prevent regenerative braking from causing damage to the 
controller or power supply.
Capacitance
Sufficient input capacitance is essential for reliable operation 
of any motor controller. It’s important that you measure that 
there is enough capacitance in your specific application. 
To do this, install the motor controller in it’s intended use 
application and apply the maximum load the unit will see in 
service. Measure the voltage ripple at the input terminals to 
the motor controller. The ripple should not exceed 5% of the 
bus voltage.  
Please contact Hargrave if you have any concerns about the 
capacitance in your application. 
Signal Isolator Supply
microDRIVE LP requires a 3.3 - 18 V source alongside the 
signal. The power is used for the onboard isolation, providing 
galvanic isolation from the power ground for increased noise 
immunity. Ground connections should be star connected at 
the flight computer wherever possible.
Power Sequencing
 • CAN is available when VBUS > VMIN.
 • DShot/PWM is enabled 140 ms after VDshot present AND  
VBUS > VMIN.
 • Powering down VDShot should not be used as a make-safe, as 
the isolator may be powered by the DShot/PWM signal. 
 • Do not switch the isolated PSU by severing the Signal GND 
connection. 
Port and Pin Electrical T olerances
PORT/PIN MAX. CURRENT (mA) ABS. MAX. VOL TAGE (V) ABS. MIN. VOL TAGE (V) PASSIVE LOADING
Main Bus (VBUS) — 63 - 0.4 —
Motor Phases — VBUS + 0.6 - 0.4 —
VCC In 30 Sig_GND + 18 Sig_GND + 3.3 —
CAN_H, CAN_L 115, Differential Mode CAN_GND + 12 CAN_GND - 12 Switchable 120 Ohm 
termination when powered.
CAN_GND — Bus_GND + 0.6 Bus_GND - 0.7 —
UART RX 10 Sig_GND + 5.5 Sig_GND - 0.3 Pulled to 3.3 V via 5.1k resistor.
TLM 10 Sig_GND + 5.5 Sig_GND - 0.3 Open drain, pulled to 3.3 V via 
5.1k resistor.
SIG 10 Sig_GND + 5.5 Sig_GND - 0.3
Pulled to 3.3 V via 5.1k 
resistor. Bidirectional DShot 
response driven with output 
impedance of 120 Ohms.
HALL A, B, C 1 Bus_GND + 5.5 Bus_GND - 0.2 Pulled to 3.3 V via 2.7k 
resistor.
NTC 0.33 Bus_GND + 3.3 Bus_GND —
5 V Out 20 5.25 4.75 —
HARGRAVE TECHNOLOGIES             Datasheet Version 1.0 February 2024
9
06 INTEGRATION

## Page 10

microDRIVE LP
Mounting
The microDRIVE LP offers 4 mounting holes to secure the unit 
to your application. These are best suited to M2 socket head 
bolts. Ensure you use a tightening torque appropriate to the 
fastener and mounting material you are using. 
The microDRIVE LP is primarily designed for use in aerial 
vehicles; vibration isolation of the unit, particularly in land-
based applications, will increase the longevity of the unit. 
Ensure there is appropriate mechanical strain relief on all 
cables attached to the unit. This will reduce the chance of 
cable joints failing, and improve the reliability of the sealing.  
Ingress Protection
The microDRIVE LP is rated to IP67 (IEC 60529). 
For water ingress, this allows for immersion in 1 m [3 ft] of 
water for 30 minutes. Exceeding this could result in damage or 
failure of the unit. 
For dust ingress, the unit is placed under vacuum for up to 8 
hours in a dust filled chamber to draw dust in. No dust ingress 
can be observed. 
Any Questions?
We’re here to help. Reach out directly to our 
engineering team at:
contact@hargravetechnologies.com
Thermal Management
The microDRIVE LP is offered with an integrated housing that 
fulfils the thermal management requirements for the unit 
in most applications. To achieve the full 60 A phase current 
rating in this configuration, the heatsink will require at least 8 
m/s airflow parallel to the heatsink.  
Motor Selection
A motor controller is only one part of a larger propulsion 
system. To achieve peak performance, it is important to select 
an appropriate motor for your load. The loaded KV of the 
motor should result in the motor reaching maximum required 
operational speed at minimum bus voltage. This ensures the 
peak load on controller occurs near 100% motor duty cycle, 
where the controller is the most efficient. 
You can find more information about selecting an appropriate 
motor for your microDRIVE LP at:
hargravetechnologies.com
Input Signals
The microDRIVE LP supports several communications 
protocols:
 • DShot
 • Bidirectional DShot
 • PWM
 • DroneCAN
To maintain effective command of your motor controller, it is 
important to ensure good signal integrity. Do not route signal 
lines alongside bus or other high power, high noise wires. 
You can find the appropriate pinout for your unit in the Pinouts 
section on page 16. 
HARGRAVE TECHNOLOGIES             Datasheet Version 1.0 February 2024
10
06 INTEGRATION

## Page 11

microDRIVE LP
07 States
The operation of the microDRIVE LP is defined by an internal state machine. Below is an overview of these internal states and 
permitted transitions, depending on the operating conditions. The current running state is logged, communicated over CAN and 
displayed by the onboard RGB LED.
STATE LED PURPOSE ACTION
Idle
Blinking PURPLE Unit is powered on, and awaiting 
detection of valid signal.
State will automatically exit with valid 
signal or error detected.
Disarmed
Blinking YELLOW Valid signal is detected, however 
due to safety lockout, motor drive is 
disabled.
State will exit when safety catch has 
cleared, likely due to non-zero throttle 
applied, or an error is detected.
Armed
Blinking AQUA Valid signal is detected, and zero 
throttle signal applied.
State will exit with an error detected, 
or motor drive commanded with non-
zero throttle signal.
Running
Blinking GREEN Motor is currently operational, unit will 
respond to any valid input signal.
State will continue indefinitely once 
started, unless error is detected, 
throttle is set to zero or unit powered 
off.
Soft Error
Blinking RED Error was detected, and motor was 
shut down to prevent unwanted 
operation.
State will exit once all errors are 
cleared, or unit is power cycled.
Hard Error
Solid RED Critical error has occurred in firmware 
and recovery.
Contact Hargrave via your technical 
contact or at:
contact@hargravetechnologies.com
Lockout
Blinking ORANGE Motor drive and certain features are 
disabled. State is used for processing 
incoming large data files such as 
firmware updates.
State will automatically exit with error 
or completion of file transfer.
USB Mode
Solid PINK Unit is in USB mode, allowing access 
to onboard logs, settings and firmware 
updates. Motor drive is disabled.
Unit will exit USB mode when 
repowered with no USB connection.
HARGRAVE TECHNOLOGIES             Datasheet Version 1.0 February 2024
11
07 STATES

## Page 12

microDRIVE LP
08 Safety Features
PROTECTION NAME DEFAUL T THRESHOLD DEFAUL T BEHAVIOUR RESET REQUIREMENTS
Bridge Over Temperature
Bridge temperature 
exceeded 100°C [212°F] 
during operation. Threshold 
is configurable.
Unit will reduce maximum 
output duty cycle to 50%. 
Behaviour is configurable.
Bridge temperature dropped 
5°C [9°F] below configured 
threshold.
Over Voltage Bus voltage exceeded 63 V. 
Threshold is configurable.
Unit will shut down drive 
to motor. Behaviour is 
configurable.
Bus voltage drops to below 
the threshold.
Under Voltage
Bus voltage dropped to 
below 15 V. Threshold is 
configurable.
Unit will not intervene. 
Behaviour is configurable.
Bus voltage rises above the 
threshold.
Over Bus Current
Bus current exceeds 80 A 
during operation. Threshold 
is configurable.
Unit will limit maximum 
output duty cycle while 
running at threshold.
Bus current drops to below 
threshold.
Over Phase Current
Phase current exceeds 100 A 
during operation. Threshold 
is configurable.
Unit will limit maximum 
output duty cycle while 
running at threshold.
Phase current drops to below 
threshold.
Loss of Signal
No signal detected for 
over 500 ms (regardless 
of protocol). Period is 
configurable.
Unit will shut down drive to 
motor.
Signal regained, and 0% 
throttle supplied to resume 
drive.
Loss of Arming
No arming detected for 
over 5000ms. Period is 
configurable.
Unit will shut down drive to 
motor.
Arming regained, and if 
require zero throttle is set, 0% 
throttle supplied to resume 
drive.
Motor Saturation Motor saturation detected 
while driving under load.
Unit will limit the maximum 
output duty cycle while 
running at saturation limit.
Automatic reset occurs once 
saturation clears.
Too Low RPM
KV is incorrectly selected 
(too low) for current bus 
voltage.
Maximum RPM to motor is 
reduced.
Correct KV and voltage 
combination used.
Onboard Memory Corruption
Firmware or settings was 
detected to be corrupt upon 
power on.
Unit is locked out. Connect to configuration 
tool for reset options.
Motor Over Temperature 
(requires motor temperature 
sensor)
Motor temperature exceeded 
120°C [248°F] during 
operation.
No action. Configurable to 
limit duty cycle.
Motor temperature dropped 
below configured limit.
HARGRAVE TECHNOLOGIES             Datasheet Version 1.0 February 2024
12
08 SAFETY FEATURES

## Page 13

microDRIVE LP
09 Errors/Warnings
Errors
The microDRIVE LP logs and reports two separate error sectors. Details of each entry are described below. The bits are set when 
the described event occurs. 
Error 1
NAME DESCRIPTION
Configuration Corrupt Loaded configuration was corrupted on unit. Connect to the configuration tool for reset. 
Motor drive is disabled.
Configuration Reset Configuration on unit was corrupt. Successfully reset to defaults.
Power Supply Fault 1 Onboard power supply for logic circuit faulted. Likely hardware issue. Contact us for 
assistance.
Power Supply Fault 2 Onboard power supply for logic circuit faulted. Likely hardware issue. Contact us for 
assistance.
Bridge Test Fault Bridge test returned negative result, indicating hardware or motor damage. Inspect or 
replace unit.
Over Voltage Fault Bus voltage exceeded unit maximum. Motor drive shut down and will resume once event 
clears.
Under Voltage Fault Bus voltage dropped below unit minimum. Motor drive shut down and will resume once 
event clears.
Over Config Voltage Fault Bus voltage exceeded configured maximum. Motor drive was shut down and will resume 
once event clears.
Under Config Voltage Fault Bus voltage dropped below configured minimum. Motor drive was shut down and will 
resume once event clears.
Absolute Over Temperature Fault Unit reached its absolute maximum over temperature limit 135°C [275°F], and motor drive 
disabled. Event will clear after temperature drops.
Signal Input Lost Loss of valid signal for configured period will stop motor drive. Drive resumes when valid 
signal returns, and throttle is 0%.
Bootloader Reported Fault Bootloader reported fault with either firmware or recovery sections. Likely failed update or 
hardware fault.
Error 2
Currently unused, reserved for future use. 
HARGRAVE TECHNOLOGIES             Datasheet Version 1.0 February 2024
13
09 ERRORS/WARNINGS

## Page 14

microDRIVE LP
Warnings
The microDRIVE LP logs and reports two separate warning sectors. Details of each entry are described below. The bits are set 
when the described event occurs. 
Warning 1
NAME DESCRIPTION
Motor Started Motor is running.
Motor Saturated ESC detected motor saturation and started reducing output drive for a period of time.
ESC Over Temperature Limit Temperature on ESC exceeded configured temperature limit.
Bus Over Voltage Config Limit Bus voltage crossed over configured voltage limit.
Bus Under Voltage Config Limit Bus voltage crossed under configured voltage limit.
Bridge Tests Failed Startup bridge tests failed, indicating a hardware failure or motor short. Unit should be 
inspected or replaced.
Bus Over Voltage Absolute Limit Bus voltage crossed above absolute limits of hardware, resulting in hard shutdown.
Bus Under Voltage Absolute Limit Bus voltage crossed below the absolute limits of hardware, resulting in hard shutdown.
Bus Voltage Maximum Ripple Unit requires extra capacitors on bus or repairs if in service for some time (capacitors worn 
out).
Firmware Updated Firmware was successfully updated within last boot-up of unit.
Firmware Corrupt Error detected and successfully repaired in firmware section on last boot. Indicates 
possible firmware update failure, or less likely, a memory fault.
Recovery Corrupt Error detected and successfully repaired in recovery section on last boot. Indicates 
possible firmware update failure, or less likely, a memory fault.
CAN Bus Off Occurred Bus-off error was reported from CAN system. May indicate a hardware fault is present.
Motor Temperature Sensor Error Motor Temperature Sensor has experienced error, typically indicating a hardware fault.
AFW Engaged Active Freewheeling (AFW) is currently engaged. No action is necessary, useful for 
debugging purposes.
Not Using Calibration Factory calibrated values are currently not in use, measurements will have more error.
Warning 2
Currently unused, reserved for future use. 
More questions?
You can find more details about these warnings and errors here:
docs.hargravetechnologies.com
HARGRAVE TECHNOLOGIES             Datasheet Version 1.0 February 2024
14
09 ERRORS/WARNINGS

## Page 15

microDRIVE LP
10 Ordering Options
XXXXXX - A00 - B00 - C00 - D00
Variant
100500  :  Standard
100550  :  NDAA*
Control Signal  
Cable (8 x 28 AWG)
TERMINATION
A  : Bare Wire
B  : CAN (JST GHR-04V-S)
C : DShot (JST GHR-05V-S)
LENGTH
01 : 50 mm  (1.97 in)
03 : 150 mm (5.91 in)
06 : 300 mm (11.81 in)
12 : 600 mm (19.69 in)
20 : 1000 mm (39.37 in)
30 : 1500 mm (59.06 in)
Bus Power  
Cables (12 AWG) 
TERMINATION
A : Bare Wire
B : XT60
LENGTH
01 : 50 mm  (1.97 in)
03 : 150 mm (5.91 in)
06 : 300 mm (11.81 in)
12 : 600 mm (19.69 in)
20 : 1000 mm (39.37 in)
30 : 1500 mm (59.06 in)
Motor Signal  
Cable (6 x 28 AWG)
TERMINATION
0 : No Cable
A : Bare Wire
B : Motor (JST GHR-06V-S)
LENGTH
01 : 50 mm  (1.97 in)
03 : 150 mm (5.91 in)
06 : 300 mm (11.81 in)
12 : 600 mm (19.69 in)
20 : 1000 mm (39.37 in)
30 : 1500 mm (59.06 in)
Motor Power  
Cables (12 AWG)
TERMINATION
A : Bare Wire
B : MR30
LENGTH
01 : 50 mm  (1.97 in)
03 : 150 mm (5.91 in)
06 : 300 mm (11.81 in)
12 : 600 mm (19.69 in)
20 : 1000 mm (39.37 in)
30 : 1500 mm (59.06 in)
*The secret is in the source
All Hargrave Technologies products are 
engineered, manufactured and tested in 
Australia from first class components. Australia 
is classed as a domestic source under Title III 
of the United States Defense Production Act.
Because of this, we can produce units that are compliant with 
the United States National Defense Authorization Act 2023 - 
generally required for suppliers to United States Government 
agencies. The NDAA version is functionally identical to the 
Standard version, but with all legislated components sourced 
outside of the NDAA “countries of concern”, including the 
People’s Republic of China. It is also EO13981-compliant. 
Bolded options represent default configuration.  
For example, this configuration would be 100500-B03-A03-0-A03
HARGRAVE TECHNOLOGIES             Datasheet Version 1.0 February 2024
15
10 ORDERING OPTIONS

## Page 16

microDRIVE LP
11 Pinouts
GREEN
YELLOW
WHITE
BLACK
RED
GREY
PURPLE
BLUE
CAN_GND
CAN_L
CAN_H
DSHOT_GND
DSHOT_V+
DSHOT
DSHOT_TLM
RXD
Control Signal - Bare Wire
Control Signal - CAN
JST GHR-04V-S
Pixhawk Standard
Mates to: 
JST BM04B-GHS-TBT (vertical)
JST SM04B-GHS-TB (side entry)
Control Signal - DShot
BLACK
RED
BLUE
GREEN
YELLOW
WHITE
GND
5V
HALL_C
HALL_B
HALL_A
MOT_NTC
Motor Signal - Bare Wire
Motor Signal - JST GH
1
A
2 3 4 5 6 7 8
1 2 3 4 5 6 7 8
B
C
D
E
F
A
B
C
D
E
F
THIS  DRAWING  IS  CONFIDENTIAL.  BOTH IT
AND  THE  COPYRIGHT  IN  THE  DRAWING
ARE  THE  PROPERTY  OF  HARGRAVE
INDUSTRIES  PTY LTD  AND  MAY  NOT  BE
REPRODUCED  OR  OTHERWISE  USED
WITHOUT  THE  WRITTEN  CONSENT  OF THE
OWNER. DO NOT SCALE DRAWING
Qty Weight Material
Title
Scale Created by
Approved by
Drawing Number
Rev. Date of issue Sheet
16/02/2024
1/1
GHR-04V-S
Quang Le10:1
PIN 4 CAN_GND
PIN 3 CAN_L
PIN 2 CAN_H
PIN 1  NC
GREEN
YELL O W
WHITE
BLA CK
RED
GRE Y
PURPLE
BL UE
C AN_ GND
C AN_L
C AN_H
DSHO T _GND
DSHO T _V+
DSHO T
DSHO T _TLM
RXD
1
A
2 3 4 5 6 7 8
1 2 3 4 5 6 7 8
B
C
D
E
F
A
B
C
D
E
F
THIS DRAWING IS CONFIDENTIAL. BOTH IT
AND THE COPYRIGHT IN THE DRAWING
ARE THE PROPERTY OF HARGRAVE
INDUSTRIES PTY LTD AND MAY NOT BE
REPRODUCED OR OTHERWISE USED
WITHOUT THE WRITTEN CONSENT OF THE
OWNER. DO NOT SCALE DRAWING
Qty Weight Material
Title
Scale Created by
Approved by
Drawing Number
Rev. Date of issue Sheet
16/02/2024
1/1
GHR-06V-S
Quang Le10:1
PIN 6 GND
PIN 5 5V
PIN 4 HALL_C
PIN 3 HALL_B
PIN 2 HALL_A
PIN 1  MOT_NTC
BLACK
RED
BLUE
GREEN
YELLOW
WHITE
GND
5V
HALL_C
HALL_B
HALL_A
MOT_NTC
1
A
2 3 4 5 6 7 8
1 2 3 4 5 6 7 8
B
C
D
E
F
A
B
C
D
E
F
THIS DRAWING IS CONFIDENTIAL. BOTH IT
AND THE COPYRIGHT IN THE DRAWING
ARE THE PROPERTY OF HARGRAVE
INDUSTRIES PTY LTD AND MAY NOT BE
REPRODUCED OR OTHERWISE USED
WITHOUT THE WRITTEN CONSENT OF THE
OWNER. DO NOT SCALE DRAWING
Qty Weight Material
Title
Scale Created by
Approved by
Drawing Number
Rev. Date of issue Sheet
16/02/2024
1/1
GHR-05V-S
Quang Le5:1
PIN 5 GND
PIN 4 DSHOT_V+
PIN 3 DSHOT
PIN 2 TLM
PIN 1  RXD
GREEN
YELLOW
WHITE
BLACK
RED
GREY
PURPLE
BLUE
CAN_GND
CAN_L
CAN_H
DSHOT_GND
DSHOT_V+
DSHOT
DSHOT_TLM
RXD
JST GHR-05V-S
Mates to: 
JST BM05B-GHS-TBT (vertical)
JST SM05B-GHS-TB (side entry)
JST GHR-06V-S
Mates to: 
JST BM06B-GHS-TBT (vertical)
JST SM06B-GHS-TB (side entry)
HARGRAVE TECHNOLOGIES             Datasheet Version 1.0 February 2024
16
11 PINOUTS

## Page 17

microDRIVE LP
Response Ready.
12 Powered by GateKEEPER
Contact us.
Sales
If you’d like to find out more about how 
you can take off with microDRIVE LP, get 
in touch with our sales engineers at:
sales@hargravetechnologies.com
Documentation
For a detailed technical overview  
and operations manual, visit: 
docs.hargravetechnologies.com
T echnical
For any technical questions, please 
reach out to your technical contact  
at Hargrave or email us at:
contact@hargravetechnologies.com
GateKEEPER is a unified technology core 
that underpins the next generation of 
Hargrave Technologies’ motor controllers. 
It encompasses everything we’ve learnt 
through over a million flight hours with our 
development partners and extends it with CAN, 
sensored drive, extended onboard logging and 
enhanced current measurement. 
Using GateKEEPER, we can share a common hardware and 
firmware foundation across all of our inverters, so they can 
all benefit from the diversity and longevity of applications 
demanded by modern UAS. A flight hour on one GateKEEPER 
ESC is a flight hour across all GateKEEPER ESCs, allowing us 
to minimise long term reliability risks across our entire product 
range. 
We can also use GateKEEPER to rapidly develop bespoke 
controllers specific to your application, with the reliability of 
an extensively flight-validated core shared with our COTS 
products. 
HARGRAVE TECHNOLOGIES             Datasheet Version 1.0 February 2024
17
12 POWERED BY GATEKEEPER

## Page 18

microDRIVE LP
13 Revisions
Revision Date Description
0 16/02/2024 Initial Release
14 Disclaimer
This electronic speed controller (ESC) datasheet is provided 
for informational purposes only. This ESC is designed and 
intended solely for use in uncrewed aerial vehicles (UAVs) and 
drones. It is not intended for any other applications in which a 
malfunction or failure may cause loss of life, injury or property 
damage, including but not limited to crewed aviation.
Hargrave Technologies Pty Ltd (ABN 45 670 453 120) and 
its Related Bodies Corporate are collectively referred to as 
“Hargrave”. Hardware, software and related technologies 
described in this document are collectively referred to as 
“Product”.
By using Product, you agree that:
1. Product is specifically designed only for use in 
UAV propulsion. Any other use is not supported or 
recommended without consultation with Hargrave.
2. Hargrave Technologies reserve the right to change the 
data provided in this datasheet at any time without prior 
notice. It is the responsibility of the user to ensure that they 
have the most up-to-date information.
3. The information contained in this datasheet is proprietary 
and confidential. Reproduction, distribution, or any other 
use of this information without the explicit permission of 
Hargrave is strictly prohibited.
4. Product may be controlled under the Australian Defence 
Trade Controls Act. Unauthorized export or re-export of 
Product is prohibited without explicit permission from 
Hargrave.  It is the responsibility of the user to comply with 
all applicable export control laws and regulations.
5. Reverse engineering of Product, including but not limited 
to disassembly, decompilation, or any other attempt to 
derive the source code or underlying technology, is strictly 
prohibited.
6. Hargrave shall not be liable for any damages, injuries, 
or losses arising from the use of Product in unspecified 
applications.
7. Hargrave shall not be liable for any loss of income, profits, 
or property resulting from the use or inability to use 
Product, even if advised of the possibility of such damages.
8. Hargrave shall not be liable for any damages, injuries, or 
losses resulting from the design, application, or integration 
of Product into customer projects or systems.
9. Any modifications or alterations made to Product are 
strictly prohibited and may result in unsafe operation, 
voiding of warranty, and legal consequences.
10. Product is only certified or compliant to standards and 
legislation explicitly mentioned in this document. Any other 
certifications or compliance not explicitly stated herein are 
not applicable.
11. It is the responsibility of the user to seek guidance 
from Hargrave for any applications other than UAVs to 
determine suitability, compliance, and safety.
12. By using Product, you acknowledge and agree to abide by 
the terms of this disclaimer. If you do not agree with these 
terms, you must not use Product for any purpose.
Please consult Hargrave for guidance on the use of Product in 
applications other than UAVs.
HARGRAVE TECHNOLOGIES             Datasheet Version 1.0 February 2024
18
13 REVISIONS & 14 DISCLAIMER
