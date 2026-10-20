# UBIQ_IDS_User_Manual.pdf

Attachment 26493, pdf, 1246 KB, added 2025-02-25 by Cameron Chapman.

## Page 1

User Manual 
 
Ice Detection Sensor  
Date: 02/2025 
Author: Lars-Stephan Klein 
Project: IP00303 IDS Wing 
Classification: Private 
Revision Description Initial Date 
A Initial version LSK 17 FEB 2025 
    
 
List of Acronyms.......................................................................................................................... 2 
Introduction.................................................................................................................................. 3 
Content of Package......................................................................................................................3 
Technical Specifications..............................................................................................................6 
Mechanical installation................................................................................................................ 6 
Fixed-Wing Aircraft Installation.................................................................................................6 
Assumptions for Mechanical Integration:............................................................................7 
Installation Instructions for Wing.........................................................................................7 
Multicopter Aircraft Installation................................................................................................. 9 
Electrical Connections...............................................................................................................12 
Operational Interface Cable....................................................................................................12 
Power Requirements........................................................................................................ 12 
Sensor Communication Interface............................................................................................. 13 
1. CAN Communication for the IDS........................................................................................13 
Network Configuration and Termination......................................................................13 
Considerations When Not Using CAN........................................................................13 
2. UART Communication for the IDS......................................................................................14 
Wiring and Connection Guidelines............................................................................. 14 
3. GPIO Communication for the IDS...................................................................................... 14 
Limitations & Electrical Considerations:......................................................................14 
Automatic Mode Detection at Power-Up:....................................................................14 
Communications Protocols.......................................................................................................14 
If you use CAN: DroneCAN.............................................................................................. 14 
If you use UART: MAVLink................................................................................................16 
If you use GPIO................................................................................................................ 17 
Private 
UBIQ Aerospace AS 
The information in this document is proprietary and confidential to UBIQ Aerospace and is available to authorized 
recipients only – copying and onward distribution is prohibited other than for the purpose for which it was made 
available.

## Page 2

Sensor Calibration..................................................................................................................... 17 
Pre-Calibration Preparation.............................................................................................. 18 
Calibration Methods..........................................................................................................18 
1. Calibration via DroneCAN and/or MAVLink...................................................... 18 
2. Calibration via the Testing and Calibration Unit................................................ 18 
Calibration Verification......................................................................................................18 
Testing and Calibration Unit......................................................................................................18 
Testing and Calibration Cable.................................................................................................19 
1. Wireless Access Point Mode........................................................................................ 20 
2. Ethernet Gadget Mode................................................................................................. 20 
Web interface....................................................................................................................21 
Sensor Operation....................................................................................................................... 23 
Water and ice detection..........................................................................................................23 
Recommended Detection Thresholds........................................................................ 23 
Temperature........................................................................................................................... 23 
Ice Detection Consideration in Mild Icing Conditions..................................................23 
Sensor states..........................................................................................................................24 
Maintenance................................................................................................................................24 
Troubleshooting......................................................................................................................... 24 
1. Initial Checks.......................................................................................................... 24 
2. Connecting to the Testing and Calibration Unit.......................................................25 
3. Further Diagnosis................................................................................................... 25 
Appendix..................................................................................................................................... 27 
Technical Drawings.................................................................................................................27 
a) Flexible Sensor Strip (Wing version)...................................................................... 27 
b) Flexible Sensor Strip (Multicopter version).............................................................28 
c) Sensor Control Unit................................................................................................ 29 
List of Acronyms 
CAN Controller Area Network 
DC Direct Current 
DHCP Dynamic Host Configuration Protocol 
GND Ground 
GPIO General-Purpose Input/Output 
IDS Ice Detection Sensor 
NC Not Connected 
PCB Printed Circuit Board 
SCU Sensor Control Unit 
Confidential UBIQ Aerospace AS Page 2 of 29

## Page 3

SMD Surface-Mounted Device 
TCU Testing and Calibration Unit 
UART Universal Asynchronous Receiver-Transmitter 
UAV Uncrewed Aerial Vehicle 
VCC Voltage at the Common Collector 
Introduction 
The UBIQ Aerospace Ice Detection Sensor (IDS) is an advanced capacitance-based sensor 
designed to detect aircraft exposure to Instrument Meteorological Conditions (IMC), such as rain 
and clouds, while distinguishing between icing and non-icing environments. The IDS operates by 
analyzing the electrical properties on the surface of the sensor, exploiting the differing properties 
of air, liquid water, and ice. 
The IDS is available in two versions: 
● Fixed-Wing Aircraft: Installed on the wing or winglet. 
● Multicopter: Mounted on a motor boom. 
This user manual provides details on sensor integration, operation, and specifications. The 
manual will guide you through the steps that are required to integrate the sensor into your 
aircraft. The steps of the integration as outlined in this manual are shown below: 
 
For any inquiries or support, contact UBIQ Aerospace Customer Support at: 
support@ubiqaerospace.com 
Content of Package 
The components included in the IDS package vary depending on the selected version 
(fixed-wing or multicopter). The table below shows the components belonging to each version.  
IDS for Wing IDS for Multicopter 
1x Flexible Sensor Strip for wing 1x Flexible Sensor Strip for multicopter 
Confidential UBIQ Aerospace AS Page 3 of 29

## Page 4

(the narrow supply stretch to the left is below 
referred to as ‘flat cable’) 
 
(the narrow supply stretch to the bottom is 
below referred to as ‘flat cable’) 
 
 1x Sensor Control Unit 
(Paper clip for size comparison; not included) 
 
1x Testing and Calibration Unit  
1x USB-A to micro USB cable (length: 1m) 
Confidential UBIQ Aerospace AS Page 4 of 29

## Page 5

1x Operational Interface Cable  (length: 0.2m) 
 
1x Testing and Calibration Cable (length: 0.2m) 
1x Aluminium tape 60 cm 
Note: You may also use other tape. Ensure that it is certified for the flying conditions used at. 
1x SCU bracket  1x SCU mounting assembly 
User manual (PDF file; digital) 
 
Flexible Sensor Strip application template 
 
N/A 
 
A digital data package with CAD models for mounting parts is also included. 
The Testing and Calibration Unit and associated cable are not a part of the airborne IDS setup 
and are solely included for configuration and demonstration purposes. See section Testing and 
Calibration Unit for further details. In addition, the application template is only used for 
manufacturing purposes and not part of the airborne setup. 
Upon receipt, please inspect the IDS for damages or missing components. Report any 
discrepancies to UBIQ Aerospace Support. 
Confidential UBIQ Aerospace AS Page 5 of 29

## Page 6

Technical Specifications 
 
Specification Value Unit 
Ambient temperature range 
for operation 
-20 to +55 
all components specified to 
-40 
°C 
-4 to +130 
all components specified to 
-40 
°F 
Ambient humidity range* 0 to 100 % RH 
Supply voltage (DC) 4.5 - 40 V 
Current draw 80 mA 
Ice detection time < 15 s 
Weight** 15 g 
0.53 oz 
Aircraft velocity*** 10 - 50 m/s 
Cable connector to user 
platform   
(Operational Interface Cable) 
Pixhawk (male) to pigtail  
Minimum bending radius of 
Flexible Sensor Strip 
4 mm 
0.157 inch 
* For the Flexible Sensor Strip only 
** Weight of Flexible Sensor Strip, SCU, and operational interface cable 
*** Approved IDS velocity 
Mechanical installation 
This section outlines the mechanical integration of the IDS sensor onto an aircraft.  
Fixed-Wing Aircraft Installation 
To ensure accurate and reliable detection of ambient conditions, the sensing surface must be 
positioned in an area with high droplet impingement. The installation location should be 
outside the wake of components that could significantly alter the liquid water content. 
● Placement Considerations: 
○ Behind a propeller: Acceptable if not affected by the tip vortex. 
Confidential UBIQ Aerospace AS Page 6 of 29

## Page 7

○ On the wing: Should not be placed too close to the wingtip, as the wingtip 
vortex reduces liquid water content. 
For optimal mechanical integration, the recommended placement is on the pressure side of 
the wing, as close as possible to the leading edge. If the leading edge curvature allows, the 
sensing surface can be wrapped around the leading edge to enhance detection across the 
full operational envelope. 
If there are uncertainties regarding the ideal installation location , please contact customer 
support for guidance. 
Assumptions for Mechanical Integration: 
● The Flexible Sensor Strip  is mounted on the pressure side of the wing near the 
leading edge. 
● The wing is hollow, allowing for the installation of the Sensor Control Unit (35 × 23.5 × 
13 mm) inside. 
● The Flexible Sensor Strip flat cable can protrude through the wing surface for 
connection to the Sensor Control Unit. 
● The sensing side of the Flexible Sensor Strip shall not be covered  by paint, resin, or 
other additional layers. 
Installation Instructions for the Wing 
 
Mounting the Flexible Sensor Strip on the wing surface 
 
1 .  Identify a suitable location on the wing or winglet. Place the application template in this 
location and temporarily fasten it with tape. It is important to take the following into 
consideration when placing the application template 
 
Confidential UBIQ Aerospace AS Page 7 of 29

## Page 8

Backside of the Flexible Sensor Strip. 
This side shall point towards the wing. 
The thermistors are visible as the small 
black units. 
Front side of the Flexible Sensor Strip: 
This side shall be exposed to the 
environment. The bright conductor paths 
are visible on this side. 
2 .   
a.  The front side (side with conductive paths) must be exposed to the airflow. The 
back side (uniform side with SMD components) must face the wing. 
b.  The sensing surface must be positioned where droplet impingement is not 
obstructed by the fuselage or other structures. 
c.  Ensure sufficient space inside the wing  for the Sensor Control Unit, which 
must be installed downstream of the sensing surface. 
3 .  Use a marker to mark the final thermistor positions through the two holes in the 
application template. Outline the sensing surface with a temporary marker to assist 
with precise placement. 
4 .  Remove the application template. 
5 .  Drill a 1 mm deep indent at each marked thermistor position using an M3 (3 mm) drill 
bit. Test the indent depth by placing the Flexible Sensor Strip in position and checking 
for bumps at the thermistor locations. 
6 .  Position the Flexible Sensor Strip  within the marked outline and temporarily secure it 
with tape at the short edges. 
7 .  Apply tape along the outer 3 mm edges only, avoiding the interdigital traces to prevent 
interference with sensor measurements. Start by taping the frontal long edge, ensuring 
the Flexible Sensor Strip adheres tightly to the wing surface without air pockets. Do 
not tape the flat cable yet. 
 
Mounting the Sensor Control Unit inside the wing 
Confidential UBIQ Aerospace AS Page 8 of 29

## Page 9

1. Identify a suitable location inside the wing  for the installation of the Sensor Control 
Unit. Take note of the following when choosing a location: 
a. The exposed pads on the tip of the Flexible Sensor Strip flat cable must 
face down when inserted into the Sensor Control Unit flat cable connector.  
b. If the Flexible Sensor Strip is mounted on the pressure side (bottom) of the 
wing, the Sensor Control Unit should ideally be installed through a top-side 
cutout. If the Sensor Control Unit is installed through a bottom-side cutout, the 
flat cable must be twisted 180°, which effectively shortens it. 
c. The cutout must be large enough to accommodate the Sensor Control Unit and 
allow for the placement of the power and data cables together with their 
connectors. 
2. Carefully cut the hole in the wing, ensuring precision if the removed section will be 
reused as a lid. 
3. Cut a 10 mm long slit in the wing for the Flexible Sensor Strip flat cable to pass 
through. Alternatively, the cable can enter through the lid opening. 
4. Install the Sensor Control Unit Bracket inside the wing. It is intended as a  
5. Use the provided CAD file in the digital data package to manufacture a bracket suitable 
for your wing. Before mounting the Sensor Control Unit bracket, connect the flat cable 
to the Sensor Control Unit flat cable connector and securely screw the Sensor Control 
Unit into its bracket. This ensures a proper connection. 
6. Once both the Sensor Control Unit and Flexible Sensor Strip are installed, secure the 
exposed portion of the flat cable on the wing using tape. Lastly, tape over the slit 
where the flat cable enters the wing  to prevent exposure to airflow and environmental 
factors. 
 
Multicopter Aircraft Installation 
 
⚠ IMPORTANT: The current version of the IDS designed for installation on a multicopter is 
optimized for platforms with circular motor booms of at least 110 mm in length. If your 
multicopter does not meet this specification, please refer to the supplied CAD files for the 
Sensor Control Unit mounting assembly and modify them accordingly to ensure compatibility. 
If you require assistance, please contact us at support@ubiqaerospace.com. 
 
It is essential to ensure that the Flexible Sensor Strip is sufficiently exposed to droplet 
impingement to accurately detect droplets and icing conditions. For further guidance on the 
impingement study, please reach out to support@ubiqaerospace.com. 
Due to variations among multicopter platforms, installation may require customization by the 
platform owner. While we provide components for a recommended installation method , a 
tailored solution may be preferable depending on your specific multicopter design. The CAD 
files for the proposed components are included in the digital data package accompanying this 
sensor. 
Confidential UBIQ Aerospace AS Page 9 of 29

## Page 10

UBIQ Aerospace is available to support you in finding the optimal installation solution for your 
aircraft. Please do not hesitate to contact us for further assistance. 
For installing the Flexible Sensor Strip on the boom of a multicopter using the parts for 
the suggested installation method, please follow these instructions: 
1 .  Ensure that the flat cable is clean and completely dry before proceeding. Insert the flat 
cable of the Flexible Sensor Strip into the flat cable connector on the Sensor Control Unit 
and fasten the Sensor Control Unit to the PCB mounting bracket using the included 
screws.  
Note that the exposed pads on the Flexible Sensor Strip flat cable must face 
downward in the connector. The connection is correctly aligned if it looks like in the 
photo below. 
 
The Sensor control Unit (green) in its Mounting Bracket (black; left hand side) and the Flexible 
Sensor Strip (right hand side). In the configuration as visible in the photo, the motor boom spans 
horizontally under them with the motor on the right hand end of the boom. 
 
2. Secure the PCB mounting bracket to a motor boom of the multicopter, ensuring the 
PCB is positioned vertically and the Flexible Sensor Strip flat cable exits to the side 
of the boom. 
3. Wrap the Flexible Sensor Strip around the boom, ensuring that the thermistors point 
inward toward the boom. At this stage of the Installation, confirm the following:  
a. The conductor patch faces outward toward the air, while the thermistors 
face inward toward the boom. 
b. The conductor patch covers both the top and front sides of the boom. 
c. The Flexible Sensor Strip flat cable adheres closely to the surface, leaving 
no air gap in between. 
4. After identifying a suitable position for the PCB casing , mark the casing position on 
the boom. Then, fold the Flexible Sensor Strip  so that it sits flush with the 
underlying geometry and mark its endpoint. This step is crucial to ensure that the 
Confidential UBIQ Aerospace AS Page 10 of 29

## Page 11

Flexible Sensor Strip is neither under tension nor too loose when mounted. Next, 
fold back the Flexible Sensor Strip  to expose the thermistors, and mark their 
placement on the boom using a marker. 
 
 
 
 
It is recommended to mount the semi-circular clamp to hold the PCB casing in place. 
 
5. Fold back the Flexible Sensor Strip  and drill a 1 mm deep hole at the marked 
thermistor positions using a ⌀ 4 mm drill bit. Reposition the Flexible Sensor Strip and 
verify that the holes are sufficiently deep  by checking for a slight bump at the 
thermistor locations. 
6. Fasten the Flexible Sensor Strip to the boom using aluminum tape, securing it by 
taping over the edges of the Flexible Sensor Strip . Do not place tape over the 
interdigital traces—instead, apply the tape over the 3 mm border of dead space on 
the Flexible Sensor Strip. 
7. Fasten the Flexible Sensor Strip flat cable so that it adheres tightly to the structure 
behind it, preferably using non-metallic tape to avoid interference with the 
capacitance measurement signal. 
a. If it is necessary to loosen the Flexible Sensor Strip flat cable for easier 
connection or disconnection from the Sensor Control Unit, use a suitable tape 
with appropriate adhesion strength . The tape should be removable without 
damaging the Flexible Sensor Strip flat cable. 
8. If the Test and Calibration Unit (TCU) will be used to calibrate and configure the IDS, 
perform this step now while the Sensor Control Unit is still easily accessible (refer to 
the instructions below). 
Confidential UBIQ Aerospace AS Page 11 of 29

## Page 12

9. Prepare the operational interface cable by terminating the CAN system in a suitable 
manner for the customer system. This is described below in the CAN communication 
section. Read the color coding of the cable below closely. If you do not plan to use CAN 
communication, you can skip this step. 
10. Connect the operational interface cable to the IDS. 
11. Place both sliding walls into their slots to close the short edges of the box. Lead the wires 
of the operational interface cable above the sliding wall on its side and down under the 
long o-ring that goes around the whole box.  
12. Connect the other side of the operational interface cable to the customer system. Fasten 
the operational interface cable securely to the frame of the multicopter and protect it from 
harm.  
Electrical Connections 
Operational Interface Cable 
The Operational Interface Cable is ensuring continuous power and data transmission between 
the IDS and the onboard avionics system. The IDS features a 6-pin JST-GH connector for power 
supply and communication, supporting CAN, UART, and GPIO interfaces for interoperability with 
other components. 
 
⚠ IMPORTANT: Follow the designated color coding precisely to ensure proper functionality 
and prevent potential damage. 
 
The color coding of the Operational Interface Cable is explained in the below table.  
 
Pin 1 Pin 2 Pin 3 Pin 4 Pin 5 Pin 6 
Red Black Yellow Green Blue White 
VCC CAN_H CAN_L GND UART TX UART RX 
 
More details on how to connect the Operational Interface Cable to the onboard avionics system 
are given in the section Sensor Communication Interface. 
Power Requirements 
The IDS operates within a supply voltage range of 4.0 V to 40 V DC, requiring a maximum 
current of 80 mA across all voltage levels. 
For optimal performance: 
● A regulated power supply of at least 5.0 V is recommended. 
● A minimum of 12 V is advised when using an unregulated power source. 
Confidential UBIQ Aerospace AS Page 12 of 29

## Page 13

Although the IDS supports input voltages up to 40 V, it is recommended to use the lowest 
suitable voltage to reduce power dissipation in the onboard LDO regulator. 
Sensor Communication Interface 
The Sensor Communication Interface section details the hardware- and software-level 
interfaces required for integrating the IDS to the user platform. The sensor supports three ways 
of communication which are outlined below. Please only choose one of them. 
 
 
 
1. CAN Communication for the IDS 
The IDS supports CAN bus communication  for data transmission. CAN (Controller Area 
Network) is a robust protocol designed for reliable real-time data exchange between sensors 
and electronic control units. The IDS utilizes the DroneCAN protocol, which operates on top of 
the physical CAN layer. Refer to the section below for protocol details. 
Network Configuration and Termination 
The CAN network allows daisy-chaining of connected devices and requires 120 Ω 
termination resistors at both ends of the chain to ensure signal integrity. The resistor shall be 
placed between the CAN_H and the CAN_L line. If the IDS is the last device in the chain, it 
must provide termination. 
Termination can be implemented in two ways: 
1. On-Board Termination: Enable the built-in 120 Ω termination resistor by bridging 
jumper pad J1 on the SCU with a solder blob. 
2. External Termination: Use an external 120 Ω resistor, positioned as close as possible 
to the IDS. No changes have to be made on the SCU. 
Considerations When Not Using CAN 
If CAN communication is not utilized, it is recommended to: 
● Leave the CAN pins unconnected. 
Confidential UBIQ Aerospace AS Page 13 of 29

## Page 14

● Do not bridge jumper pad J1, as this would increase the IDS’s current consumption. 
2. UART Communication for the IDS 
The IDS supports communication via a 3.3 V UART port, which allows for point-to-point 
connections only. The IDS utilizes the MAVLink protocol over the physical UART layer. Refer 
to the section below for protocol details. 
Wiring and Connection Guidelines 
● The TX line of the IDS must be connected to the RX line of the receiving device. 
● The RX line of the IDS must be connected to the TX line of the transmitting device. 
● Keep the TX and RX wires as short as possible to minimize electrical interference 
and support higher bit rates. 
⚠ IMPORTANT: The TX and RX lines are not 5 V tolerant. Ensure only 3.3 V levels are used. 
If interfacing with a 5 V system, a level shifter must be used to prevent damage to the IDS.  
3. GPIO Communication for the IDS 
The TX and RX lines of the UART interface can be configured to function as GPIO outputs to 
indicate ice detection status. 
Limitations & Electrical Considerations: 
● In GPIO mode, the TX and RX pins operate in push-pull mode. Any external devices 
connected to these lines must use high-impedance inputs only. 
● A pull-down resistor of 4.7 kΩ or higher may be used on the TX and RX pins. 
● A pull-up resistor of 100 kΩ or higher to 3.3 V is allowed on the TX and RX pins. 
Automatic Mode Detection at Power-Up: 
● As a safety measure and to facilitate reconfiguration, the TX and RX lines are checked 
at power-up. 
● If either TX or RX is driven high or pulled high with a low-value resistor, the IDS will 
default to UART communication mode instead of GPIO mode. 
● This configuration remains in effect until the next power cycle. 
Communications Protocols 
Based on your choice of communication (CAN, UART or GPIO) you will find in this section the 
details of each communication protocol and their implementation. 
Confidential UBIQ Aerospace AS Page 14 of 29

## Page 15

If you use CAN: DroneCAN 
The IDS uses the DroneCAN protocol on the CAN bus. It supports CAN 2.0 (also known as 
BxCAN or Classical CAN) and CAN FD, with bit rates up to 1 Mbit/s. It supports both static and 
dynamic node ID allocation. The factory default settings are as follows: 
Bit rate 1 000 000 
CANFD 0 
Node ID 0 (dynamic allocation) 
 
The following standard DroneCAN messages are understood by the IDS: 
● uavcan.protocol.dynamic_node_id.Allocation (used if no static node ID is configured) 
● uavcan.protocol.NodeStatus (broadcast every second by the IDS after node ID 
allocation) 
● uavcan.protocol.GetNodeInfo 
● uavcan.protocol.param.GetSet 
● uavcan.protocol.param.ExecuteOpcode 
● uavcan.protocol.RestartNode 
Furthermore, once a node ID is allocated, the IDS will broadcast the message 
com.ubiqaerospace.ids.Status (message ID 20809), which has the following definition: 
#   
# Ice detection status 
# 
float16 temperature         # Sensor temperature in Kelvin 
float16 water_level          # Water saturation level (0.0 to 1.0)   
float16 ice_level              # Ice saturation level (0.0 to 1.0) 
uint8 status_flags            # Sensor status 
 
uint8 STATUS_FLAG_WATER = 1  # Water detected 
uint8 STATUS_FLAG_ICE = 2    # Ice detected or water detected during freezing temperatures 
uint8 STATUS_FLAG_ERROR = 4  # Error detected 
Parameters can be changed using the GetSet message. Some parameter changes do not take 
effect immediately, instead an ExecuteOpcode message with OPCODE_SAVE must be sent to 
save the parameters to non-volatile storage, then a RestartMessage must be sent to restart the 
IDS. 
The following parameters are supported: 
Index Name Type Default 
value 
Description 
0 can_bitrate float 1 000 000 CAN bitrate. Valid values: 12500, 
Confidential UBIQ Aerospace AS Page 15 of 29

## Page 16

250000, 500000, 800000, 
1000000. 
1 can_fd float 0 1 = send CAN FD frames 
2 can_node_id float 0 DroneCAN node ID (1 to 127), or 0 
for dynamic allocation 
3 uart_baudrate float 1 000 000 UART bitrate. Valid values: 38400, 
57600, 115200, 230400, 460800, 
500000, 921600, 1000000. 
4 system_id float 1 MAVLink system ID (0 to 255) 
5 component_id float 73 MAVLink component ID (0 to 255) 
6 gpio_enable float 0 1 = use UART TX/RX as digital I/O 
7 baseline_low float   Baseline capacitance for low 
frequencies. Write 0 or a negative 
number to calibrate this parameter. 
8 baseline_high float   Baseline capacitance for high 
frequencies. Write 0 or a negative 
number to calibrate this parameter. 
9 water_level float 
(read-only) 
 Water saturation level (0.0 to 1.0) 
10 ice_level float 
(read-only) 
 Ice saturation level (0.0 to 1.0) 
 
If you use UART: MAVLink 
The IDS uses the MAVLink protocol version 2.0 on the UART port. It supports bit rates up to 1 
Mbit/s. The system and component IDs can be freely configured. The factory default settings are 
as follows: 
Bit rate 1 000 000 
System ID 1 
Component ID 73 
 
The following standard MAVLink messages are understood by the IDS: 
● HEARTBEAT (sent every second by the IDS) 
● PARAM_REQUEST_LIST 
● PARAM_REQUEST_READ 
● PARAM_SET 
Confidential UBIQ Aerospace AS Page 16 of 29

## Page 17

● COMMAND_LONG 
○ MAV_CMD_PREFLIGHT_STORAGE 
○ MAV_CMD_PREFLIGHT_REBOOT_SHUTDOWN 
○ MAV_CMD_REQUEST_MESSAGE 
■ COMPONENT_INFORMATION_BASIC 
Furthermore, the IDS will broadcast the message ICE_DETECTION_STATUS (message ID 
20809), which has the following definition: 
Field Name Type Description 
temperature float Sensor temperature in degrees Kelvin 
water_level float Water saturation level (0.0 to 1.0) 
ice_level float Ice saturation level (0.0 to 1.0) 
status_flags uint8_t Sensor status bitmask: 
● 1: Water detected 
● 2: Ice detected 
● 4: Error 
 
The EXTRA_CRC byte for this message has the value 0x5D. 
Parameters can be changed using the PARAM_SET message. Some parameter changes do not 
take effect immediately, instead an MAV_CMD_PREFLIGHT_STORAGE command with 
PARAM_WRITE_PERSISTENT must be sent to save the parameters to non-volatile storage, 
then a MAV_CMD_PREFLIGHT_REBOOT_SHUTDOWN command must be sent to restart the 
IDS. 
The list of parameters supported is identical to the ones for the DroneCAN protocol (see above). 
If you use GPIO 
If GPIO is enabled, the UART TX and RX lines are used to send the IDS state as follows: 
RX TX State 
low low Dry 
high low Water detected 
low high Ice detected 
high high Error 
 
⚠ IMPORTANT: During power-off, the RX and TX lines remain in a high-impedance state. If 
required, pull-up or pull-down resistors should be used to maintain a well-defined signal 
state at all times. 
Confidential UBIQ Aerospace AS Page 17 of 29

## Page 18

Sensor Calibration 
The IDS utilizes a capacitive sensor to detect the presence of water and ice. However, the 
baseline capacitance of the sensing element varies depending on the installation 
configuration on the user platform. 
To ensure accurate measurements, a one-time calibration  must be performed after 
installation. This one-time calibration consists of three main steps. 
Step 1: Pre-Calibration Preparation 
● Ensure the sensing surface is clean and dry. 
● Use a dry microfiber cloth to remove any dust or particles from the sensor surface. 
● Ensure that no objects are covering the sensing element during calibration. 
Step 2: Calibration Methods 
The baseline capacitance values can be set using one of the following two methods: 
1. Calibration via DroneCAN and/or MAVLink 
This method requires that the sensor control unit is connected via CAN and/or UART. 
 
● Using the respective protocol, write the value  0.0 to the parameters 
baseline_low and baseline_high. This will cause these parameters to be 
recalibrated by the IDS. 
● Send the appropriate message to store the new values into non-volatile 
memory. See the Communication Protocols section for more details. 
 
2. Calibration via the Testing and Calibration Unit  
 
● Refer to the Testing and Calibration Unit section below for usage instructions. 
Step 3: Calibration Verification 
After performing the calibration, verify the following: 
● The IDS should report a DRY condition with water_level and ice_level values close to 
0.0. 
● Touch the sensing element with a wet cloth and confirm that the IDS reports WATER 
conditions. 
● After removing the cloth and allowing the sensor to dry, it should revert to DRY condition 
within a few seconds. 
Confidential UBIQ Aerospace AS Page 18 of 29

## Page 19

Testing and Calibration Unit 
To simplify initial testing and calibration  of the IDS, UBIQ provides a Testing and Calibration 
Unit (TCU) that connects directly to the sensor. The Testing and Calibration Unit hosts a 
web-based interface, allowing real-time sensor monitoring, configuration, and calibration. If 
you select calibration via DroneCAN and/or MAVLink as stated above, then you will not need 
the Testing and Calibration Unit and you can skip this chapter. 
 
⚠ IMPORTANT: The Testing and Calibration Unit is not designed for permanent 
installation in a drone. It is intended solely for testing and calibration purposes on the 
ground. 
 
The Testing and Calibration Unit operates independently of an Internet connection, making 
it suitable for remote IDS setup and calibration . It is connected using the Testing and 
Calibration Cable to the Sensor Control Unit. 
Testing and Calibration Cable 
 
The Sensor Control Unit end of the Testing and Calibration Cable is configured as follows: 
 
Red  
NC 
 
NC 
Black Green White 
VCC GND TX RX 
 
The TX line (green) transmits data from the IDS and must be connected to the RX pin of the 
receiving device. Conversely, the RX line (white) must be connected to the TX pin  of the 
receiving device to establish proper communication. If you use the Testing and Calibration Cable 
that is provided by UBIQ, the pins at the sensor control unit are correctly connected upon 
plugging in the cable. 
The cable configuration on the Testing and Calibration Unit side is as follows: 
Red Black White Green 
VCC GND RX TX 
 
The Testing and Calibration Cable is connected to the Testing and Calibration Unit as shown 
below:  
Confidential UBIQ Aerospace AS Page 19 of 29

## Page 20

⚠ WARNING: Incorrect installation of the Testing and Calibration Unit cable can result in 
permanent damage to the IDS and the Testing and Calibration Unit. 
 
 
After the electrical connection is established, the TCU can be accessed using one of the two 
following methods: 
1. Wireless Access Point Mode 
1. Connect a micro-USB cable to the rightmost port of the TCU. 
2. Connect the other end of the USB cable to a computer or any USB power source. 
3. After approximately one minute, a new Wi-Fi network named "UBIQ IDS TCU" will 
appear in the available networks list. 
4. Connect to this network using the password: 
[password removed] 
5. Open a web browser and enter the following address: 
○ http://ids.ubiq/ 
○ If this does not work, try: http://192.168.81.1/ 
⚠ Note: While connected to the "UBIQ IDS TCU" network, Internet access may be 
unavailable unless a wired Ethernet connection is also present. 
 
2. Ethernet Gadget Mode 
⚠ Note: Ethernet Gadget Mode is only supported on Linux and macOS. 
1. Connect a micro-USB cable to the middle port of the Testing and Calibration Unit. 
Confidential UBIQ Aerospace AS Page 20 of 29

## Page 21

2. Connect the other end of the USB cable to a computer. 
3. After approximately one minute, a new Ethernet device should appear in the network 
settings of the connected computer. 
4. If the operating system does not automatically configure the connection , manually 
enable the new Ethernet device. 
5. Ensure that DHCP is enabled to obtain an IPv4 address automatically. 
6. Open a web browser and enter the following address: 
○ http://ids.ubiq/ 
○ If this does not work, try: http://192.168.85.1/ 
Web interface 
Once connected via one of the methods mentioned above, the web interface will display the 
current IDS status and provide options to adjust parameters and calibrate the IDS. The 
interface looks as follows: 
Confidential UBIQ Aerospace AS Page 21 of 29

## Page 22

The configuration can be updated by changing the values in the column “New value” to the 
desired values, and then clicking on “Save parameters”. This will store the new values in 
non-volatile memory and reset the IDS. 
A (re)calibration can be performed by clicking on “Calibrate sensor”. Verify that this will cause 
“Water level” and “Ice level” to be around 0.00, and that “Status” is “DRY”. Save the updated 
calibration value by clicking on “Save parameters”. 
Confidential UBIQ Aerospace AS Page 22 of 29

## Page 23

Sensor Operation 
Upon power-up, the IDS sensor automatically initializes and becomes fully operational 
within one second. 
Water and ice detection 
The IDS can detect the presence and accumulation of water and ice on its surface while also 
distinguishing between the two states. The detected levels are transmitted via DroneCAN 
and/or MAVLink messages (see protocol details above). 
The detection output is a normalized value between 0.0 and 1.0: 
● 0.0 indicates no water or ice present. 
● 1.0 represents sensor saturation with water or ice. 
Recommended Detection Thresholds 
To differentiate between insignificant water/ice presence (caused by humidity or sensor noise) 
and meaningful accumulation, the following threshold levels are recommended: 
Phase Recommended threshold level 
Water > 0.10 
Ice > 0.10 
 
Temperature 
The IDS is equipped with thermistors that measure the temperature of the sensing element. 
The temperature readings are transmitted via DroneCAN and/or MAVLink messages (see 
protocol details below). 
Ice Detection Consideration in Mild Icing Conditions 
a) Water detection may be faster than ice detection  in mild icing conditions 
(temperatures near 0°C). 
b) This is due to a low freezing fraction of supercooled liquid water, which may delay the 
formation of detectable ice. 
c) If water is detected while the temperature is below freezing, icing conditions must 
be assumed, even if ice has not yet been explicitly detected. 
Confidential UBIQ Aerospace AS Page 23 of 29

## Page 24

Sensor states 
During operation, the IDS reports one of four possible states: 
 
Sensor state Description 
DRY No droplets are detected. 
WATER A significant amount of droplets is detected. 
ICE A significant amount of ice accretion is detected* 
ERROR An error with the sensor has been identified. Please 
check if the sensor is used according to the specifications 
and if mechanical damage is visible. 
* Note: The ICE state is also reported when a significant amount of liquid water is detected at 
freezing temperatures. 
The sensor state is transmitted via DroneCAN and/or MAVLink messages and can also be 
output as a digital signal (see GPIO protocol above). 
 
Maintenance 
For optimal sensor performance, the sensing area should be cleaned between flights, 
ideally immediately before takeoff. It is recommended to use isopropyl alcohol (also known 
as isopropanol or 2-propanol) and a microfiber cloth for cleaning. 
Troubleshooting 
If the IDS is not functioning as expected , follow this checklist to identify and resolve potential 
issues: 
1. Initial Checks 
✅ Ensure proper cable connections: Verify that all cables are securely and correctly inserted 
into their respective connectors. 
✅ Check power supply: Confirm that the IDS is receiving power. 
✅ Inspect for physical damage: Look for any visible damage to the cables, Sensor Control 
Unit, or Flexible Sensor Strip. 
✅ Verify communication settings: Ensure that both ends are using the correct protocol 
configurations, including baud rate, CAN node ID, and MAVLink system/component IDs. 
✅ Check the sensing area: Ensure that the sensor is clean and unobstructed. 
Confidential UBIQ Aerospace AS Page 24 of 29

## Page 25

2. Connecting to the Testing and Calibration Unit 
If no obvious issues are found from the above checks, connect the IDS to the Testing and 
Calibration Unit and verify its operation. 
● If the IDS functions correctly with the Testing and Calibration Unit, check that all 
configuration settings are properly set. 
3. Further Diagnosis 
If the issue persists, refer to the troubleshooting table below for further guidance. 
Symptom Possible cause Solution 
No or unreliable 
communication from 
the IDS 
No power to the IDS Ensure the IDS is powered correctly. 
Cable issue Check that the cable between the IDS and 
the rest of the system is not damaged, and 
that it is inserted correctly and securely at 
both ends. 
Communication 
parameter mismatch 
Check that both the IDS and the device it is 
connected to use the same communication 
parameters (baudrate, CAN node ID, 
MAVLink system/component ID). 
Baud rate too high Try to use a lower baud rate. 
Incorrect termination of 
the CAN bus 
Make sure there are exactly two 120 Ω 
termination resistors enabled, one on each 
end of the CAN bus. Check that jumper pad 
J1 on the SCU is properly bridged if this 
device needs termination, and is not bridged 
otherwise. 
GPIO not working 
correctly 
GPIO output not 
enabled 
Check that the gpio_enable parameter is set 
to 1. 
GPIO lines pulled up 
too strongly 
Make sure the GPIO lines are not pulled high 
with resistor values lower than 100 kΩ. 
Error state reported Incorrect calibration Follow the calibration procedure to calibrate 
the IDS. 
Flexible Sensor Strip 
issue 
Check that the Flexible Sensor Strip is 
connected correctly and securely to the 
Sensor Control Unit. 
Check that there is no damage to the Flexible 
Sensor Strip. 
Incorrect water 
and/or ice level 
Incorrect calibration Follow the calibration procedure to calibrate 
the IDS. 
Confidential UBIQ Aerospace AS Page 25 of 29

## Page 26

Flexible Sensor Strip 
issue 
Check that the Flexible Sensor Strip is 
connected correctly and securely to the 
Sensor Control Unit. 
Check that there is no damage to the Flexible 
Sensor Strip. 
Sensing area not clean Check that nothing is covering the sensing 
area, and that it is free from contaminants. 
Clean the sensing area as described in the 
section “Maintenance”. 
 
If the IDS cannot be restored to proper operation  after following the troubleshooting steps, 
please contact UBIQ Aerospace for further assistance. 
 
 
Confidential UBIQ Aerospace AS Page 26 of 29

## Page 27

Appendix 
Technical Drawings 
 
a) Flexible Sensor Strip (Wing version) 
The thickness of the Flexible Sensor Strip is 0.1 mm. At the positions of the thermistors, 
the thickness is 1 mm. 
 
Confidential UBIQ Aerospace AS Page 27 of 29

## Page 28

b) Flexible Sensor Strip (Multicopter version) 
 
Confidential UBIQ Aerospace AS Page 28 of 29

## Page 29

c) Sensor Control Unit 
The PCB is equipped with two holes to place screws. The holes are represented 
by green circles in the drawing below.  
 
 
 
Sensor control unit size: 35.00 x 23.50 mm 
Mounting hole size: M3 
Mounting hole space: 28.00 x 16.50 mm 
Mounting hole location (mm): 31.50 x 3.50 and 3.50 x 20.00  
 
Confidential UBIQ Aerospace AS Page 29 of 29
