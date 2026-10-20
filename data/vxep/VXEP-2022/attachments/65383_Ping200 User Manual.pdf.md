# Ping200 User Manual.pdf

Attachment 65383, pdf, 1102 KB, added 2026-10-14 by Stephan Johnson.

## Page 1

UAV-1007121-001   
Rev C 
 
 
 
ping200XRTM TSO 
User and Installation Guide

## Page 2

UAV-1007121-001  2 
Rev C 
© 2023 - 2024 uAvionix Corporation. All rights reserved.  
 
Except as expressly provided herein, no part of this guide may be 
reproduced, transmitted, disseminated, downloaded or stored in any 
storage medium, for any purpose without the express written permission of 
uAvionix.  uAvionix grants permissions to download a single copy of this 
guide onto an electronic storage medium to be viewed for personal use, 
provided that the complete text of this copyright notice is retained.  
Unauthorized commercial distribution of this manual or any revision hereto 
is strictly prohibited. 
 
uAvionix® and Ping® are registered trademark s of uAvionix Corporation and  
may not be used without express permission of uAvionix.  
 
ping200X, ping200XR, tailBeaconX, skyBeaconX, tailBeacon, skyBeacon , 
AV-30-C, AV-30-E and skyBeacon Installer are trademarks of uAvionix 
Corporation and may not be used without express permission of uAvionix.  
 
ForeFlight is a registered trademark of ForeFlight LLC and is used with 
permission. 
 
Patent uavionix.com/patents

## Page 3

UAV-1007121-001  3 
Rev C 
1 Revision History 
Revision Date Comments 
A 2/26/2024 Initial release 
B 7/31/2024 GPS antenna port current specification  
C 10/25/2024 Updated part descriptions

## Page 4

UAV-1007121-001  4 
Rev C 
2 Warnings / Disclaimers 
All device operational procedures must be learned on the ground.  
uAvionix is not liable for damages arising from the use or misuse of this 
product. 
This equipment is classified by the United States Department of 
Commerce's Bureau of Industry and Security (BIS) as Export Control 
Classification Number (ECCN) 7A994.   
 
These items are controlled by the U.S. Government and authorized for 
export only to the country of ultimate destination for use by the ultimate 
consignee or end-user(s) herein identified. They may not be resold, 
transferred, or otherwise disposed of, to any other country or to any person 
other than the authorized ultimate consignee or end -user(s), either in their 
original form or after being incorporated into other items, without first 
obtaining approval f rom the U.S. government or as otherwise authorized by 
U.S. law and regulations .

## Page 5

UAV-1007121-001  5 
Rev C 
3 Limited Warranty 
uAvionix certified products are warranted to be free from defects in material 
and workmanship for two years from the installation of ping200XR in or on 
the aircraft. For the duration of the warranty period, uAvionix, at its sole 
discretion, will repair or replace any product which fails in normal use. Such 
repairs or replacement will be made at no charge to the customer for parts 
or labor, provided that the customer shall be responsible for any 
transportation cost. 
 
Restrictions: This warranty does not apply to cosmetic damage, 
consumable parts, damage caused by accident, abuse, misuse, fire or 
flood, theft, damage caused by unauthorized servicing, or product that has 
been modified or altered. 
 
Disclaimer of Warranty:  IN NO EVENT, SHALL UAVIONIX BE LIABLE 
FOR ANY INCIDENTAL, SPECIAL, INDIRECT OR CONSEQUENTIAL 
DAMAGES, WHETHER RESULTING FROM THE USE, MISUSE OR 
INABILITY TO USE THE PRODUCT OR FROM DEFECTS IN THE 
PRODUCT. SOME STATES DO NOT ALLOW THE EXCLUSION OF 
INCIDENTAL OR CONSEQU ENTIAL DAMAGES, SO THE ABOVE 
LIMITATIONS MAY NOT APPLY TO YOU.  
 
Warranty Service: Warranty repair service shall be provided directly by 
uAvionix. Proof of purchase for the product from uAvionix or authorized 
reseller is required to obtain and better expedite warrant y service.  
Please email or call uAvionix  support with a description of the problem you 
are experiencing.  Also, please provide the model, serial number, shipping 
address and a daytime contact number.   
You will be promptly contacted with further troubleshooting steps or return 
instructions.  It is recommended to use a shipping method with tracking and 
insurance.

## Page 6

UAV-1007121-001  6 
Rev C 
4 Table of Contents 
 
1 Revision History ........................................................................................... 3 
2 Warnings / Disclaimers ............................................................................... 4 
3 Limited Warranty ......................................................................................... 5 
4 Table of Contents ........................................................................................ 6 
5 System Information ..................................................................................... 9 
5.1 Certification ............................................................................................. 9 
5.2 TSO Authorization  ............................................................................... 10 
5.3 System Functions ................................................................................ 10 
5.4 TSO Deviations and Incomplete  ........................................................ 11 
5.5 FCC ID .................................................................................................. 12 
5.6 Device Marking .................................................................................... 13 
5.6.1 ping200XR Hardware  .................................................................. 13 
5.6.2 ping200XR Software .................................................................... 13 
5.7 Environmental Qualification Form  ...................................................... 14 
5.8 Continued Airworthiness  ..................................................................... 15 
5.9 System Limitations............................................................................... 16 
5.10 Regulatory Compliance .................................................................... 16 
6 System Specifications  ............................................................................... 18 
6.1 System Functionality ........................................................................... 18 
6.2 ping200XR TSO Specifications  .......................................................... 18 
6.2.1 General Specifications ................................................................ 18 
6.2.2 Mode S Transponder Specifications  .......................................... 19 
6.2.3 Altitude Encoder Specifications .................................................. 19 
6.2.4 GPS/SBAS Specification  ............................................................ 19 
6.2.5 Control Interface Specifications  ................................................. 20 
6.2.6 System Interfaces ........................................................................ 20

## Page 7

UAV-1007121-001  7 
Rev C 
7 Installation .................................................................................................. 22 
7.1 Unpacking and Inspecting ................................................................... 22 
7.2 Authorized Part Numbers .................................................................... 22 
7.3 Included Parts - UAX-90111-01 ......................................................... 22 
7.4 Non-TSO Optional Part Numbers  ...................................................... 22 
7.5 Installation Materials and Tools .......................................................... 22 
7.6 Additional Required Equipment .......................................................... 23 
7.7 Mounting ............................................................................................... 23 
7.8 Wiring .................................................................................................... 25 
7.9 Transponder Antenna .......................................................................... 26 
7.10 GPS Antenna .................................................................................... 27 
7.11 Static Pressure Port ......................................................................... 27 
7.12 Cooling Requirements  ..................................................................... 28 
8 Control and Configuration Interface  ........................................................ 29 
9 Configuration and Calibration  .................................................................. 29 
9.1 Configuration ........................................................................................ 30 
9.1.1 ICAO Address .............................................................................. 31 
9.1.2 Aircraft Maximum Speed  ............................................................. 31 
9.1.3 Aircraft Stall Speed  ...................................................................... 32 
9.1.4 Aircraft Length / Width  ................................................................. 32 
9.1.5 Aircraft Registration  ..................................................................... 32 
9.1.6 GPS Antenna Lateral / Longitudinal Offset  ............................... 32 
9.1.7 Aircraft Emitter Type  .................................................................... 33 
9.1.8 ADS-B In Capability ..................................................................... 33 
9.1.9 Baro Altitude Source .................................................................... 33 
9.1.10 Serial Port Baud Rate .................................................................. 34 
9.1.11 SIL / SDA ...................................................................................... 34 
9.1.12 Default Control Mode................................................................... 34 
9.1.13 Default Squawk ............................................................................ 34

## Page 8

UAV-1007121-001  8 
Rev C 
9.1.14 Baro Altitude Resolution .............................................................. 35 
9.1.15 In / Out Protocols ......................................................................... 35 
9.2 Control ................................................................................................... 35 
9.3 Post-Installation Checks...................................................................... 35 
9.4 Software Part Number  ......................................................................... 38 
9.5 Altitude Encoder Calibration  ............................................................... 39 
10 Normal Operation ...................................................................................... 40 
11 Maintenance .............................................................................................. 40 
12 Support ....................................................................................................... 40 
Appendix A Control Interface......................................................................... 41 
Appendix B Equipment Compatibility and Interconnect Drawings  ............ 45

## Page 9

UAV-1007121-001  9 
Rev C 
5 System Information 
5.1 Certification 
This installation manual provides mechanical and electrical information 
necessary to install ping200XR. It is not equivalent to an approved 
airframe-specific maintenance manual, installation design drawing, or 
installation data package. The content of this manual assumes use by 
competent and qualified personnel using standard maintenance procedures 
in accordance with Title 14 of the Code of Federal Regulation and other 
related accepted procedures. The conditions and tests required for 
approval of this artic le are minimum performance standards. Those 
installing this article either on or within a specific type or class of aircraft 
must determine that the aircraft installation conditions are within the 
standards which include any accepted integrated functions n ot specified by 
the standards. TSO articles, articles approved with 14 CFR Part 21.8(d), 
and any accepted integrated function(s) not specified in the standard must 
have separate approval for installation in an aircraft. The article may be 
installed only according to 14 CFR Part 43 or the applicable airworthiness 
requirements. This is an incomplete system intended to provide the 
functions identified in, and when installed according to , this installation 
manual.

## Page 10

UAV-1007121-001  10 
Rev C 
5.2 TSO Authorization  
ping200XR complies with the following TSOs when properly installed and 
interfaced with equipment as detailed in this guide.  
Function TSO / MPS Class / Type 
Air Traffic Control Radar Beacon 
System/Mode Select (ATCRBS / 
Mode S) Airborne Equipment 
TSO-C112e 
RTCA/DO-181E 
Level 2els, 
Class 1 
[1] 
Extended Squitter Automatic 
Dependent Surveillance – 
Broadcast (ADS-B) and Traffic 
Information Service – Broadcast 
(TIS-B) Equipment Operating on 
the Radio Frequency of 1090 
MHz 
TSO-C166b 
RTCA/DO-260B Class B1S 
Automatic Pressure Altitude 
Reporting Code-Generating 
Equipment 
TSO-C88b 
SAE/AS8003 N/A 
Airborne Navigation Sensor 
Using the Global Position System 
(GPS) Augmented by the 
Satellite Based Augmentation 
System (SBAS) 
TSO-C145e 
INCOMP 
RTCA/DO-229E 
Beta 1 
[1] Anticipating RTCA/DO-181F Level 2 Transponder requirements, 
ping200XR does not support the UM protocol, does not support the 
Comm-A protocol, and does not have the capability to process and 
transmit air-initiated Comm-B messages.  See Section 5.4 for 
additional details. 
5.3 System Functions 
System Function TSO DO-178C DAL DO-254 DAL 
Mode S Transponder  TSO-C112e C C 
1090ES Transmitter TSO-C166b C C 
Altitude Encoder TSO-C88b C C 
GPS/SBAS TSO-C145e C C

## Page 11

UAV-1007121-001  11 
Rev C 
5.4 TSO Deviations and Incomplete  
TSO Deviation 
C112e uAvionix was granted a deviation from TSO -C112e 
Paragraphs 3.e and 6.f to use RTCA/DO -178C in place of 
RTCA/DO-178B. 
C112e uAvionix was granted a deviation to not implement Utility 
Message (UM Field) support, consistent with RTCA/DO -181F 
and FAA/TSO-C112f Level 2 transponder requirements.  
 
This impacts the Mode S Level 2 transponder SARPs 
requirements as contained in ICAO Annex 10 Volume IV 
§§3.1.2.6.5.3.1, 3.1.2.6.11.3.2.1.3, 3.1.2.6.11.3.4.2.2, and 
3.1.2.7.9.2.3. 
C112e uAvionix was granted a deviation to not implement Comm -A 
support, consistent with RTCA/DO -181F and FAA/TSO-C112f 
Level 2 transponder requirements.  
 
This impacts the Mode S Level 2 transponder SARPs 
requirements as contained in ICAO Annex 10 Volume IV 
§§2.1.5.1.2, 3.1.2.6.11.1.2, and 3.1.2.10.5.2.1.1.  
C112e uAvionix was granted a deviation to not implement broadcast 
interrogation support, consistent with RTCA/DO -181F and 
FAA/TSO-C112f Level 2 transponder requirements.  
 
This impacts the Mode S Level 2 transponder SARPs 
requirements as contained in ICAO Annex 10 Volume IV 
§§2.1.5.1.2, 3.1.2.6.11.1.2, and 3.1.2.10.5.2.1.1.  
C112e uAvionix was granted a deviation to not implement multi -site 
message support, as it applies to the Comm -B operation of 
Level 2 transponders, consistent with RTCA/DO -181F and 
FAA/TSO-C112f Level 2 transponder requirements.  
 
This impacts the Mode S Level 2 transponder SARPs 
requirements as contained in ICAO Annex 10 Volume IV 
§§2.1.5.1.2 and 3.1.2.6.11.3.

## Page 12

UAV-1007121-001  12 
Rev C 
C112e uAvionix was granted a deviation to not implement Air -Initiated 
Comm-B support, consistent with RTCA/DO -181F Level 2 and 
FAA/TSO-C112f transponder requirements.  Air-initiated 
Comm-B messages are neither processed nor transmitted.  
 
This impacts the Mode S Level 2 transponder SARPs 
requirements as contained in ICAO Annex 10 Volume IV 
§§2.1.5.1.2 and 3.1.2.6.11.3. 
C112e uAvionix was granted a deviation to not reply to 
ATCBRS/Mode S All-Calls, as required by ICAO Annex 10 
Volume IV §3.1.2.1.5.1.1.1 on or after January 1, 2020, and 
consistent with RTCA/DO-181F and FAA/TSO-C112f 
requirements. 
C166b uAvionix was granted a deviation from TSO -C166b 
Paragraphs 3.e and 6.h to use RTCA/DO -178C in place of 
RTCA/DO-178B. 
C166b uAvionix was granted a deviation to not implement Airborne 
Velocity Subtypes 3 and 4, consistent with RTCA/DO -260C 
and FAA/TSO-C166c requirements. 
C88b uAvionix was granted a deviation from TSO -C88b Paragraphs 
3.e and 6.h to use RTCA/DO -178C in place of RTCA/DO -
178B. 
C88b uAvionix was granted a deviation from TSO -C88b Paragraph 
3.d to use RTCA/DO-160G in place of RTCA/DO -160E. 
C145e uAvionix was granted a deviation from TSO -C145e Paragraph 
3.g to use RTCA/DO-160G in place of RTCA/DO-160E. 
 
5.5 FCC ID 
Model FCC ID 
ping200XR TSO 2AFFTP200S

## Page 13

UAV-1007121-001  13 
Rev C 
5.6 Device Marking   
5.6.1 ping200XR Hardware 
 
5.6.2 ping200XR Software 
The software contained in ping200XR is identified by electronic marking. 
Reference Section 9.4 for information on determining the software part 
number.

## Page 14

UAV-1007121-001  14 
Rev C 
5.7 Environmental Qualification Form  
Conditions DO -160G 
Section  Description of Conducted Tests  
Temperature and Altitude 4.0 Equipment tested to Categories B2,C4 
Low temperature ground survival 4.5.1 -55°C 
Low Temperature Short-Time 
Operating 
4.5.1 -35°C 
Low Temperature Operating 4.5.2 -35°C (see Note 1) 
High Temperature Operating 4.5.4 +70°C 
High Temperature Short-Time 
Operating 
4.5.3 +70°C 
High Temperature Ground Survival 4.5.3 +85°C 
Loss of Cooling 4.5.5 Cooling air not required (+70°C operating without 
cooling) 
Altitude 4.6.1 35,000 ft (see Note 2) 
Decompression 4.6.2 Equipment identified as Categories B2,C4 – no test 
Overpressure 4.6.3 Equipment identified as Categories B2,C4 – no test 
Temperature Variation 5.0 Equipment tested to Category B 
Humidity 6.0 Equipment tested to Category A 
Operation Shocks  7.0 Equipment tested to Category B 
Crash Safety 7.0 Equipment tested to Category B Type 5 
Vibration 8.0 Aircraft zone 2: type 5 Category S level M 
Explosion 9.0 Equipment identified as Category X – no test 
Waterproofness 10.0 Equipment identified as Category X – no test 
Fluids Susceptibility 11.0 Equipment identified as Category X – no test 
Sand and Dust 12.0 Equipment identified as Category X – no test 
Fungus 13.0 Equipment identified as Category X – no test 
Salt Spray 14.0 Equipment identified as Category X – no test 
Magnetic Field 15.0 Equipment tested to Category Z 
Power Input 16.0 Equipment tested to Category BX 
Voltage Spike 17.0 Equipment tested to Category B 
AF Conducted Susceptibility 18.0 Equipment tested to Category B 
Induced Signal Susceptibility  19.0 Equipment tested to Category AC 
RF Susceptibility 20.0 Equipment tested to Category TT 
RF Emissions 21.0 Equipment tested to Category B 
Lightning Induced Transient 
Susceptibility 
22.0 Equipment tested to Category A2XXXX (see Note 3) 
Lightning Direct Effects 23.0 Equipment identified as Category X – no test 
Icing 24.0 Equipment identified as Category X – no test  
Electrostatic Discharge 25.0 Equipment tested to Category A 
Fire, Flammability 26.0 Equipment identified as Category X – no test 
Notes: 
1. Tested to operating low of -45°C when used with an external altitude encoder 
2. Tested to 50,000 ft 
3. 4-wire serial/power conductors tested to A2XXXX, MMCX GPS conductors tested to A1XXXX

## Page 15

UAV-1007121-001  15 
Rev C 
5.8 Continued Airworthiness  
Maintenance of the ping200XR is "on condition" only.  
Periodic regulatory function checks of the transponder and altitude encoder 
must be performed. Every 24 months, or after any maintenance is 
performed where data correspondence error could be introduced:  
1. The transponder must be tested, inspected, and found to comply with 
the requirements of 14 CFR Part 91.413, as described in 14 CFR 43 
Appendix F. 
2. The altitude encoder must be tested to ensure correspondence to the 
primary flight altimeter, as described in AC 43 -6D and 14 CFR 43 
Appendix E, to meet the maintenance requirements of 14 CFR Part 
91.411. If the altitude encoder demonstrates correspondence errors 
in excess of ±125 feet, then calibration as described in Section  9.5 
must be performed. If the error cannot be corrected using the 
calibration procedure, the unit must be repaired or replaced.  
Annually, confirm the ADS-B software version is current per Service 
Bulletins available at the uAvionix website. 
The aircraft must be returned to service in a means acceptable to the 
appropriate aviation authority.  
Note: Transponders certified after January 1, 2020 must not respond 
to ATCRBS/Mode S All-Calls (Long P4 interrogation). This may 
cause unexpected results to be obtained by transponder test 
sets. 
Note: Mode S transponders must only respond to Mode S Only All-
Calls when airborne. ping200XR can be placed in an airborne 
state for test purposes by entering “Ground Test Mode” using 
the “ping200X Control & Config” Windows  application, or by 
using certain compatible control heads . For more details see 
Section 9.3.

## Page 16

UAV-1007121-001  16 
Rev C 
5.9 System Limitations 
Installation 
This article meets the minimum performance and quality control standards 
required by a technical standard order (TSO). Installation of this article 
requires a separate approval . 
GNSS Fault Detection Prediction  
Cannot be used for navigational guidance where Fault Detection (FD) 
prediction capability is required, such as during execution of certain 
approach operations outside of SBAS coverage.  
GNSS Supported Modes  
ping200XR’s truFYX GNSS does not implement LNAV approach mode . It 
operates in En Route/Terminal mode only . 
SatCom 
The ping200XR GPS has not been demonstrated as compatible with 
SatCom equipment and should not be installed on SatCom equipped 
aircraft1.   
Note 1: SatCom equipment is defined as radio transmitters transmitting 
on or near the L1/L2 frequency bands.   This does not include 
passive receive -only systems such as additional GPS receivers 
or unidirectional satellite data link receivers. 
5.10 Regulatory Compliance  
Aircraft using ping200X R must evaluate their needs to be compliant with 14 
CFR 91.215, 91.225 and 91.227.  While in transponder airspace specified in 
14 CFR 91.215, ping200X R must be maintained to 14 CFR Part 91.413. 
While in ADS-B OUT airspace specified in 14 CFR 91.225, ping200X R 
must be configured and equipped to meet the requirements of 14 CFR 
91.225 and 91.227.  
To meet 14 CFR 91.225 and 91.227 with no operational limitations, 
dynamic (in-flight) control is necessary.  See Section 8 and Appendix A for 
details on the control interface, and Appendix C for compatible equipment.

## Page 17

UAV-1007121-001  17 
Rev C 
For additional guidance on ADS -B OUT installation and approvals, 
reference AC 20-165B.

## Page 18

UAV-1007121-001  18 
Rev C 
6 System Specifications 
6.1 System Functionality 
ping200XR is a Mode S, Level 2els, Class 1 transponder with ADS -B 
extended squitter, elementary surveillance , SI code support and internal 
Class Beta 1 SBAS/WAAS GPS position source . The ping200XR has a 
nominal power output of 250W and meets the power output requirements 
for a Class 1 transponder. The ADS-B function meets DO-260B Class B1S. 
This transponder replies to both legacy Mode A/C interrogations and to 
Mode S interrogations from both ground radar and airborne collision 
avoidance systems. In all cases, the interrogations are received by the 
transponder on 1030MHz and replies are transm itted on 1090MHz.  
6.2 ping200XR TSO Specifications 
6.2.1 General Specifications 
Characteristics Specifications 
Width 47.00 mm 
Height 10.07 mm 
Depth 71.47 mm 
Weight 51g 
Operating temperature range -35°C to +70°C (internal barometer)  
-45°C to +70°C (external barometer)  
Maximum pressure altitude 35,000 ft (internal barometer)  
50,000 ft (external barometer) 
Input voltage range 9 to 30.3 VDC 
14V current 0.16A idle  
0.25A maximum 
28V current 0.13A idle 
0.20A maximum 
Inrush Current Limit [1] 1A 
Export Compliance ECCN 7A994 
[1] Inrush and internal short -circuit protection is internally current limited to 1A

## Page 19

UAV-1007121-001  19 
Rev C 
 
6.2.2 Mode S Transponder Specifications  
Characteristics Specifications 
Transmit frequency  1090 MHz 
Transmit power 54 dBm (250 W) 
Receive frequency  1030 MHz 
ATCRBS sensitivity -74 dBm 
Mode S sensitivity -74 dBm 
RF Impedance 50 Ω 
RF Connector SMA 
 
6.2.3 Altitude Encoder Specifications 
Characteristics Specifications 
TSO-C88b Operating Range -1,000 ft to 35,000 ft (TSO compliant) 
Maximum Differential 
Pressure Altitude (static port 
to installation environment)  
36,000 ft 
Maximum Rate of Altitude 
Change 
20,000 fpm 
Static Pressure Port M3 barb fitting 
 
6.2.4 GPS/SBAS Specification 
Characteristics Specifications 
Number of Channels  15 (12 GPS and 3 GPS/SBAS) 
Frequency 1575.42 MHz L1, C/A code

## Page 20

UAV-1007121-001  20 
Rev C 
Sensitivity 
Tracking 
Reacquisition 
Cold Start 
Hot Start 
 
-166 dBm 
-160 dBm 
-148 dBm 
-160 dBm 
Horizontal position accuracy  5 m RMS with SBAS 
Velocity accuracy  3 m/s 
TTFF (Time to First Fix)  58 seconds typical with current 
almanac and position 
Reacquisition 1 second typical 
Position update interval 0.2 second (5 Hz)  
Time Mark ±30 nSec of UTC 
Datum WGS-84 
Altitude output Height Above Ellipsoid (HAE)  
SDA (System Design Assurance)  2 
SIL (Source Integrity Level) 3 
 
6.2.5 Control Interface Specifications 
Characteristics Specifications 
Physical RS-232 
Rate and properties  57,600 bps 8N1 
Protocols UCP, UCP-HD, Apollo and Mavlink 
(Navigation message only)  
 
For more control interface details, see  Appendix A .  
6.2.6 System Interfaces

## Page 21

UAV-1007121-001  21 
Rev C

## Page 22

UAV-1007121-001  22 
Rev C 
7 Installation 
7.1 Unpacking and Inspecting  
Carefully unpack the device and make a visual inspection of the unit for 
evidence of any damage incurred during shipment. If the unit is damaged, 
notify the shipping company to file a claim for the damage. To justify your 
claim, save the original shipping container and all packing materials.  
7.2 Authorized Part Numbers 
Item P/N 
ping200XR Hardware UAV-1007127-( ) 
ping200XR Software1 UAV-1002393-( ) 
1 – Verified through the ping200X Control & Config application UAV-1004567-001 
7.3 Included Parts - UAX-90111-01 
Item(s) P/N 
ping200XR Hardware UAV-1007127-( ) 
Certificate of Conformance UAV-1008218-001 
Getting Started Card  UAV-1005282-009 
 
7.4 Non-TSO Optional Part Numbers  
Non-TSO Optional Item(s) P/N 
Ping200X Control & Config Application 1 UAV-1004567-001 
Male SMA to Female BNC Adapter, 6in  UAV-1001011-002 
Male SMA to Female BNC Adapter, 9in  UAV-1001011-003 
Quarter Wave Monopole , Rigid Ball Assembly, 
1090MHz 
UAV-1001009-002 
pingAntenna, 120Deg Dipole, Overmold 6in SMA, 
1090MHz 
UAV-1004675-003 
Adhesive Mount GPS Antenna, 46cm MMCX (m)  UAV-1007165-001 
 
7.5 Installation Materials  and Tools 
ping200XR requires configuration, either using the available uAvionix 
Windows-based application, or dynamically using the described 
configuration protocol. Typical installations will be configured using:

## Page 23

UAV-1007121-001  23 
Rev C 
• “ping200X Control & Config ” Windows application, UAV-1004567-
001 
• USB/RS-232 serial adapter (not included)  
ping200XR may require standard aviation parts for installation , such as: 
• Screws or appropriate hardware  
• Wire 
• Shielded wire (2 or 3 conductor) 
• Circuit breakers  
• Environmental splices  
• Ring terminals for grounding  
• Static pressure lines and fittings  
• Thread locking compound . We recommend Loctite® 242 or 243 
which works well with stainless steel hardware.  
Minimally, ping200XR installation requires access to the following tools:  
• Screwdriver or other appropriate driver  
• Appropriate crimping tool(s)  or soldering equipment 
7.6 Additional Required Equipment 
ping200XR is a “remote” transponder . To fully function it requires 
connection to a controlling device, often referred to as a control head . It is 
possible to statically configure ping200X R, but certain capabilities, such as 
changing the squawk code and responding to annunciations, will not be 
available when no controlling device is connected.  
For transmission of complete ADS -B data elements, and 14 CFR 
91.225 compliance, ping200XR requires connection to a compliant 
position source .  
The following table details the functions provided directly by ping200XR. 
Transponder ADS-B 
Transmitter 
Altitude 
Encoder 
GPS 
Receiver 
GPS 
Antenna 
Transponder 
Antenna 
Control Head w/ 
Annunciation 
X X X X    
In typical configurations, the control head provides control, display, and 
annunciation. 
7.7 Mounting 
!

## Page 24

UAV-1007121-001  24 
Rev C 
The ping200XR is designed to be mounted in any convenient location in 
the cockpit, the cabin, or an avionics bay.  
The following installation procedure should be followed, taking care to allow 
adequate space for installation of cables and connectors.  
• Select a position in the aircraft that is not too close to any high 
external heat source. The ping200X R is not a significant heat source 
itself and does not need to be kept away from other devices for this 
reason. 
• Avoid sharp bends and placing the cables too near to the aircraft 
control cables. 
Secure the transponder to the aircraft via the two integrated mounting 
brackets. The brackets are designed to accept screws up to size M3 or 4 -
40. Thread locking compound should be used as appropriate, and the 
ping200XR should be mounted on a flat surface.  
Note: Installation of the ping200XR must be in accordance with AC 43.13 -
2B, Chapter 1.

## Page 25

UAV-1007121-001  25 
Rev C 
7.8 Wiring 
ping200XR requires connections to power, ground and an RS-232 control 
interface.  
4-wire Control Interface  
Color Type Function 
Red Power 
Input Aircraft Power 
Black Power 
Input Aircraft Ground 
Grey Data 
Output Control RS-232 Transmit 
Orange Data 
Input Control RS-232 Receive 
 
If new power wiring is required, refer to AC 43.13-1B Chapter 11 for 
guidance. The wiring should present an impedance of less than 0.5  Ω. The 
following table provides guidance for typical aircraft hook -up wire. 
Gauge ohm/km Maximum Length for 0.5 Ω 
20 AWG 35 14.2 m 
22 AWG 64 7.8 m 
 
Refer to Appendix B for example wiring diagrams and installations.

## Page 26

UAV-1007121-001  26 
Rev C 
7.9 Transponder Antenna  
An appropriate L-band antenna, designed to receive and transmit vertically 
polarized signals at 1030 and 1090  MHz, must be installed.  
Prior to powering the ping200X R, ensure an appropriate antenna 
or commercially available 50 Ω load is connected to the SMA 
port. Powering the ping200XR without an attached load will 
result in damage to the device  not covered under warranty. 
The following antennas may be used:  
• Standard 50Ω vertically polarized antenna with VSWR ≤ 1.5:1 over 
the 1030 to 1090 MHz frequency band  
• TSO-C74( ) or TSO-C112( ) antennas that meet the above 
specification 
• uAvionix non-TSO SMA dipole, P/N UAV-1004675-003 
Take into consider ation the antenna manufacturer’s installation instructions. 
General guidance is provided below.  
• The antenna should be mounted external to the airframe, and 
typically on the bottom of the aircraft.  
• The antenna should be mounted in a vertical orientation when the 
aircraft is in level flight.  For uAvionix  UAV-1004675-003, see below 
for proper orientation. 
 
  
!

## Page 27

UAV-1007121-001  27 
Rev C 
 
• Keep the cable lengths as short as possible and avoid sharp bends in 
the cable to minimize the Voltage Standing Wave Ratio (VSWR) (i.e. 
Return Loss). 
• Ensure that cable and connector losses do not reduce power output 
below allowed levels for your aircraft operation.  
• Conventional monopole antennas require an appropriate ground 
plane. For metallic aircraft, ensure good ground connection to the 
antenna. For composite aircraft, a ground plane must be installed.  
• The antenna connection s should be protected from the elements , and 
antenna cabling should be installed to minimize RF energy radiated 
inside the aircraft. 
 
The antenna used must be installed to provide a separation 
distance of at least 20 cm from all persons.  
7.10 GPS Antenna 
ping200XR provides a 5 VDC bias voltage  (25mA max current)  for active 
DO-301 antenna operation.  Only an appropriate TSO-C190 or DO-301 
compliant antenna with an MMCX connector and 5VDC bias voltage should 
be integrated with ping200XR . This antenna should be mounted at a 
minimum of 4 feet from any aircraft transmit antennas and have a clear 
view of the sky with no obstructions.  
For applications where a TSO antenna is not required, uAvionix non-TSO 
GPS antenna (part number UAV-1007165-001) has been shown 
compatible. 
7.11 Static Pressure Port 
ping200XR contains a TSO-C88b altitude encoder.  The barb fitting (size 
M3) located on the unit’s enclosure should be securely attached to the 
aircraft’s static pressure system.  Minimize static pressure line lengths as 
possible. Press-plastic tubing (PVC, soft nylon or polyurethane) with a 
nominal ID of 1/8” (3.18mm) can be used, and secured with a small tie 
wrap. Adapters may be used to convert the barb to match the aircraft’s 
current static plumbing. Ensure any fittings are free from leaks.  
!

## Page 28

UAV-1007121-001  28 
Rev C 
Upon completion of installation, a case leak test should be performed per 
14 CFR Part 43 Appendix E. 
If an external altitude encoding source is configured , the internal altitude 
encoder is unused, and the static pressure system does not need to be 
connected to the ping200X R static pressure port . The Maximum Operating 
Altitude listed on the ping200X R nameplate is not applicable when used 
with an external altitude encoding source  – instead reference the 
Environmental Qualification Form in Section 5.7. 
7.12 Cooling Requirements  
ping200XR is designed to meet all applicable TSO requirements without 
forced-air cooling. 
Attention should, however, be given to the incorporation of cooling 
provisions to limit the maximum operating temperature if ping200X R is 
installed in close proximity to other avionics  which would otherwise cause 
operational temperature limits to be exceeded (see Section 5.7 
Environmental Qualification Form ).

## Page 29

UAV-1007121-001  29 
Rev C 
8 Control and Configuration Interface 
ping200XR has a control and configuration serial interface. It is used to 
configure the equipment at installation time, and to control the device while 
operating. Typically, a control head or unmanned aircraft flight control 
computer is connected to the device during operation.  
Transponder control  provides the ping200XR with data such as operating 
mode, emergency status, squawk code, IDENT, and optionally external 
pressure altitude information . Status and annunciation information is 
provided by ping200XR over the control interface.  
For 14 CFR 91.225 compliance with no operational limitations, dynamic (in -
flight) control is necessary.  
For details on the ping200X R control interface, refer to Appendix A. 
For typical installations, refer to Appendix C. 
9 Configuration and Calibration 
The transponder system must be configured during initial system 
installation. This can take place on the bench or in the aircraft, but device 
power and connection to a PC must be available.  
Prior to powering the ping200X R, ensure an appropriate antenna 
or commercially available 50 Ω load is connected to the SMA 
port. Powering the ping200XR without an attached load will 
result in damage to the device  not covered under warranty. 
Connect the ping200XR to a PC running the Configuration and Control 
application via the USB COM port adapter.  
 
!

## Page 30

UAV-1007121-001  30 
Rev C 
Set ‘Conn Type’ to ‘Serial’, ‘Port’ to the USB or serial port connected to the 
ping200XR, ‘App Baud’ to ‘57600’ and ‘Protocol’ to ‘UCP’.   
 
Click ‘Start’.   
9.1 Configuration  
The configuration items list below should be used to document the system 
installation for future reference. These items can be found on the 
‘Configuration’ tab and are permanently stored in the ping200X R. 
Configuration Item Default Configured 
ICAO Address 0x000000  
Aircraft Maximum Speed (kts)  < 75  
Aircraft Stall Speed 0  
Verify the COM Settings

## Page 31

UAV-1007121-001  31 
Rev C 
Aircraft Length (m) L ≤ 15  
Aircraft Width (m) W ≤ 23  
Aircraft Registration “        “  
GPS Antenna Lateral Offset (m)  0  
GPS Antenna Longitudinal Offset (m)  Applied by 
sensor  
Aircraft Emitter Type  No Information 
Available  
ADS-B In Capability UAT RX NO  
1090ES RX NO  
Baro Altitude Source  Internal  
Serial Port Baud Rate (bps)  57600  
SIL <= 1E-7 (3)  
SDA <= 1E-5 (2)  
Default Control Mode None (Off)  
Default Squawk 1200  
Baro Altitude Resolution (ft)  25  
In Protocols UCP  
Out Protocols UCP  
 
9.1.1 ICAO Address 
The ICAO address is a 24 -bit number issued to the aircraft by the 
registration authority of the aircraft. These addresses are usually written as 
a 6-digit hexadecimal number, although you may also encounter one 
written as an 8-digit octal number. The ping200X R understands the 
hexadecimal format. An octal number must be converted to hexadecimal 
format before entering.   
Tip: By using the N-Number Look Up function on https://www.faa.gov, 
locate and use the “Mode S Code (base 16 / hex)” value.  Applies to U.S. 
registered aircraft only.  
9.1.2 Aircraft Maximum Speed 
Mode S transponders can transmit their maximum airspeed characteristics 
to aircraft equipped with TCAS. This information is used to identify threats 
and to plan avoidance action by the TCAS equipped aircraft. The airspeeds 
are grouped in ranges.

## Page 32

UAV-1007121-001  32 
Rev C 
9.1.3 Aircraft Stall Speed 
The default aircraft stall speed is 0.  Set as appropriate for your aircraft to 
allow automatic air/ground state determination. Set to 0 to lock in airborne 
state, or to allow switching by the control head. See Appendix A for more 
details. 
9.1.4 Aircraft Length / Width  
When on the ground, ADS-B transmits encoded aircraft size information 
which is used by ATC to identify taxiing routes and potential conflicts. Enter 
the length and width (wingspan) fields and the appropriate size codes will 
be calculated for transmission.  
Aircraft Length in Meters  Aircraft Width in Meters  
L ≤ 15 W ≤ 23 
15 < L ≤ 25 28.5 < W ≤ 34 
25 < L ≤ 35 33 < W ≤ 38 
35 < L ≤ 45 39.5 < W ≤ 45 
45 < L ≤ 55 45 < W ≤ 52 
55 < L ≤ 65 59.5 < W ≤ 67 
65 < L ≤ 75 72.5 < W ≤ 80 
75 < L ≤ 85 W > 80 
L > 85 Any 
 
9.1.5 Aircraft Registration 
The Aircraft Registration can be up to an 8 alpha -numeric code that 
corresponds to the tail number of the aircraft. (0 -9, A-F).  This value is used 
by default in the ADS-B “Callsign” field, unless a valid “Flight ID” is provided 
via the control interface.  
Note: This is typically your aircraft N -number, unless otherwise advised by 
the FAA or ATC.  
9.1.6 GPS Antenna Lateral / Longitudinal Offset  
The GPS antenna offset is used in conjunction with the length and width to 
manage taxiway conflicts. A typical GPS does not report the geographic 
position of the center of the aircraft, or even the tip of the nose of the 
aircraft; instead, it usually repor ts the location of the actual GPS antenna 
(not the GPS receiver). In normal flight operation, this distinction is of no 
importance at all, but if ADS -B is used to manage taxiway conflicts, a

## Page 33

UAV-1007121-001  33 
Rev C 
significant offset in antenna position could mean the aircraft footprint is not 
in the same place as the ADS -B reported position. Although the GPS 
Antenna Offset is primarily intended for position correction on large 
transport aircraft, General Aviation ai rcraft can also have a significant 
offset. For example, if the aircraft has a long tail boom and the GPS 
antenna is on top of the tail, the GPS position could be 4 meters or more 
from the nose of the aircraft.  
GPS Antenna Lateral Offset from 
roll axis (meters) 
GPS Antenna Longitudinal Offset 
from aircraft nose ( meters) 
0  
 
 
0 to 60 meters in 2-meter 
increments 
 
Left 2 
Left 4 
Left 6 
Right 2 
Right 4 
Right 6 
 
9.1.7 Aircraft Emitter Type 
The aircraft emitter type default is  ‘No Information Available’. This must be 
configured as appropriate for the host aircraft.  
9.1.8 ADS-B In Capability  
The ADS-B transmissions include an indication to the ground stations of 
whether the aircraft includes a 1090MHz ADS -B receiver, a UAT ADS-B 
receiver, or both. This data is used to transmit ADS -R or TIS-B broadcasts 
to your aircraft if conditions indicate.  ping200XR does not include an ADS-
B receiver.  Only select these items if you have a separate ADS -B receiver 
on-board. 
9.1.9 Baro Altitude Source 
By default, ping200XR utilizes pressure altitude measurements from an 
internal TSO-C88b altitude encoder for Mode C,  S and ADS-B messages.  
If desired, an existing or external altitude encoder can be used in lieu of the 
internal altitude encoder . To do so, change the ping200X’s “Baro Altitude 
Source” from “Internal” to “External”.  If set to “External”, t he ping200XR will 
use the barometric pressure altitude reported in the Control Message  in all 
Mode C, S and ADS-B messages.

## Page 34

UAV-1007121-001  34 
Rev C 
9.1.10 Serial Port Baud Rate  
This setting configures the speed of the control interface serial baud rate in 
bps. 
9.1.11 SIL / SDA 
Set SIL according  to the advertised integrity level of the GPS source .   
• If the ping200XR is configured to use the internal GPS source, set the 
SIL to 3 (default).   
• If an external GPS source is interfaced, set the SIL based on the 
external GPS source.  
Per AC 20-165B, ping200X’s System Design Assurance (SDA) must report 
the lowest SDA value of the ADS -B system.  The ADS-B system includes 
both the SDA of the ping200XR and the external GPS position source.   
• If the ping200XR is configured to use the internal GPS source, set the 
SDA to 2 (default). 
• If the paired external GPS source has an advertised  SDA that is less 
than 2, configure the ping200X R SDA value to the SDA of the 
external GPS source.  For GPS’s SDAs greater than or equal to 2, 
configure the ping200XR SDA to 2.   
9.1.12 Default Control Mode 
Select the default operating mode, to be used prior to arrival of control 
messages. This setting configures the ping200X R for Mode A, Mode C, 
Mode S and ADS-B Extended Squitter transmissions.   
• None selected disables all modes  
• Mode A - Squawk 
• Mode C – Altitude 
• Mode S – Addressed Identification and Altitude  
• Mode ES – ADS-B Identification and Position reporting  
When not used with a control head or equivalent device, modes A / C 
/ S / ES must be enabled by default to meet all authorized TSOs.   
9.1.13 Default Squawk 
The default squawk is 1200. To assist ATC tracking of aircraft, an aircraft 
squawk is transmitted. The configured value is the squawk code that will be 
transmitted in lieu of available control data.  
!

## Page 35

UAV-1007121-001  35 
Rev C 
9.1.14 Baro Altitude Resolution 
The barometric pressure  altitude source resolution default is 25 (ft).  
9.1.15 In / Out Protocols 
The default In / Out protocols are UCP. 
9.2 Control 
The ‘Control’ tab allows the installer to exercise and verify the 
transponder’s operation.  This simulates a control head or similar 
equipment. 
Serial Port Setup
Control
GPS Simulator
Serial Activity Viewer
Ownship Display
Fault Status
Transponder Status
Packet Statistics
 
9.3 Post-Installation Checks  
Post-installation checks must be performed by the installer, after 
configuration, as appropriate for the aircraft and type of installation.

## Page 36

UAV-1007121-001  36 
Rev C 
To ensure compliance with regulations in the United States, verify 
functionality identified in 14 CFR Part 43 Appendix F (ATC Transponder 
Tests and Inspections) and 14 CFR Part 43 Appendix E (Altimeter System 
Test and Inspection). 
Aircraft with ping200XR installed may be subject to requirements in 14 CFR 
91.215, 91.225 and 91.227. For additional details reference Section 5.10. 
A complete post-installation check may be performed by using a ramp 
tester such as a VIAVI IFR6000. A simplified post -installation check 
procedure follows.  
STEP CHECK 
Launch the ‘ping200X Control & Config ’ Windows 
application 
 
Set Port to the USB or serial port connected to the 
ping200XR 
 
Set the ‘App Baud’ to ‘57600’  
Set ‘Protocol’ to ‘UCP’ 
- If the ping200XR has been reconfigured for a protocol 
other than UCP, this procedure may not apply  
 
Connect the antenna  
Apply power from a minimum of a 11V, 1A power source   
Press ‘Start’ in ‘ping200XR Control & Config ’ Windows 
application 
 
Confirm activity in ‘Serial Activity Viewer’ and incrementing 
‘Pkts’ in ‘Packet Statistics’ of ‘Control’ tab  
 
Verify ‘ICAO Address’ in ‘Ownship Display’ is correct for 
your aircraft, and not ‘000000’  
 
Confirm ‘Baro Altitude’ in ‘Ownship Display’ shows the 
current pressure altitude; i.e. the current altitude as 
displayed on an altimeter set to 29.92  
 
If a GPS is connected and the GPS antenna has a clear 
view of the sky, allow the GPS time to obtain a position fix ; 
confirm that ‘Latitude’ and ‘Longitude’ are correct  in 
‘Ownship Display’ 
 
Select ‘ALT’ from the ‘Mode’ selection box  in ‘Control’  
Verify ‘TX System’ fault annunciation LED turns green  in 
‘Fault Status’

## Page 37

UAV-1007121-001  37 
Rev C 
STEP CHECK 
If you are in range of Radar  or connected to a n interrogating 
test set, ‘Transponder Status’ will indicate  interrogations 
 
If not already in airborne state, access the ‘Service’ tab and 
select ‘Enable Ground Test Mode’ 
- This will enable airborne state until the ping200X R is 
power cycled 
 
Return to ‘Control’ tab and v erify ‘Air/Ground State’ displays 
‘Airborne’ in ‘Ownship Display’  
 
Perform ramp test procedures as necessary for required 
aircraft operations 
 
An EFB application such as ForeFlight Mobile, when 
connected to an ADS-B receiver such as Sentry, can be 
used to verify ADS-B transmissions; 
- Using ForeFlight Mobile, in the ADS -B Device screen, 
select ‘Ownship’ when detected, and verify transmitted 
parameters

## Page 38

UAV-1007121-001  38 
Rev C 
9.4 Software Part Number 
Launch the ‘ping200X Control & Config’ Windows application.  
 
Confirm the displayed ‘P/N’ and ‘Version’ on the ‘Firmware Version’ section 
of the ‘Service’ tab is current per Service Bulletins listed at:  
https://uavionix.com/support/ping200XR/ 
If not current, apply Service Bulletins as appropriate to update the software.

## Page 39

UAV-1007121-001  39 
Rev C 
9.5 Altitude Encoder Calibration  
STEP CHECK 
Launch the ‘ping200X Control & Config’ Windows 
application 
 
 
 
 
Set Port to the USB or serial port connected to the 
ping200XR 
 
Set the ‘App Baud’ to value noted in Section 9.1  
Set ‘Protocol’ to value noted in Section 9.1  
Apply power from a minimum of a 11V, 1A power source   
Press ‘Start’ in ‘ping200X Control & Config’ Windows 
application 
 
With a Pitot Static Test Set connected, select the ‘Service’ 
tab

## Page 40

UAV-1007121-001  40 
Rev C 
Press ‘Get’ to retrieve the calibration information   
Adjust Pitot Static Test Set to the Low calibration altitude  
Wait for Pitot Static Test Set to reach the Low calibration 
altitude, then click 'Start' 
 
Wait for calibration to complete   
Adjust Pitot Static Test Set to Mid calibration altitude  
Wait for Pitot Static Test Set  to reach the Mid calibration 
altitude, then click 'Start' 
 
Wait for calibration to complete   
Adjust Pitot Static Test Set to the High calibration altitude   
Wait for Pitot Static Test Set  to reach the High calibration 
altitude, then click 'Start' 
 
Wait for calibration to complete   
Click ‘Send’ to send updated calibration to the device   
 
10 Normal Operation 
ping200XR must be enabled, typically in ALT mode  (Mode A, Mode C, 
Mode S, Extended Squitter), during all phases of flight including surface 
movement operations. 
 
11 Maintenance 
The ping200XR is not a user serviceable product. All service must be 
performed either by uAvionix or an authorized uAvionix repair center.  
12 Support 
For additional questions or support please visit: 
https://www.uavionix.com/support/

## Page 41

UAV-1007121-001  41 
Rev C 
Appendix A  Control Interface 
ping200XR is controlled and configured using the data interface specified 
below. 
Characteristics Specifications 
Physical RS-232 
Data rate 57,600 bps (default) 
Parity None 
Data bits 8 
Stop bits 1 
Protocol UCP (RX/TX enabled by default)  
UCP-HD (disabled by default) 
Apollo (disabled by default) 
 
UCP is enabled by default for use as the input protocol. Apollo input can 
optionally be enabled simultaneous with UCP , and messages are 
processed based on the received data format.  
UCP is enabled for use as the output protocol.  Additionally, Apollo output is 
automatically enabled upon receipt of an Apollo input message.  
The data rate and protocols can be configured by the UCP/UCP -HD 
Transponder Configuration message.  UCP or UCP-HD input is required to 
be enabled to allow device configuration.  
A.1 UCP 
uAvionix Control Protocol (UCP) is documented in uAvionix UCP 
Transponder Interface Control Document UAV-1002375-001. This 
document is made available to authorized parties, and may be obtained by 
contacting uAvionix. 
UCP can be used to configure, control, and monitor status of the 
ping200XR. 
A.1.1 Control Message 
The Control message must be supplied to ping200XR as documented in 
the UCP ICD. Minimally, Mode A (squawk) code, IDENT, emergency state, 
and transponder mode are provided in this message.

## Page 42

UAV-1007121-001  42 
Rev C 
Mode 
To set the transponder operating mode, appropriate enable bits must be 
set in the Control message. The mapping of traditional transponder modes 
to required Control message enablement bits follows.  
 
Operating Mode Mode A Mode C Mode S 1090ES 
STBY     
ON (suppress 
altitude) 
X  X X 
ALT X X X X 
 
Flight Identification 
If Flight Identification is provided in the Control message, that value is 
transmitted as Flight ID. If none (all spaces) is provided, the Call 
Sign/Aircraft Registration value configured in the device is transmitted.  
Air-Ground State 
Optionally, air-ground state may be provided in the Control message. To 
use air-ground state from the control message, the device must be 
configured with a VS0 of zero. Air-ground logic is described by the following 
chart. 
 
Airborne subsonic and supersonic state is automatically determined by 
ping200X. 
VS0 == 0 
Use 
control 
input 
Ground 
Auto A-G 
state 
algorithm 
yes 
no 
Airborne 
airborne set 
ground set 
ground 
determined 
airborne 
determined

## Page 43

UAV-1007121-001  43 
Rev C 
A.1.2 Heartbeat Message 
With UCP enabled, the Heartbeat message is sent once per second.  The 
following specific fault indications are available in the Heartbeat message, 
and should be mapped to annunciations compliant with applicable 
regulations. TSO-C166b requires annunciations of ADS -B transmission 
device and function failures (see RTCA/DO -260B §2.2.11.5) 
 
Fault Description 
Maintenance Required ICAO address not set (RTCA/DO-181E §2.2.10.3) 
ICAO address not set (RTCA/DO-260B §2.2.11.3.1) 
Multiple position sources available – check configuration 
(RTCA/DO-260B §2.2.5.3) 
Failure TX System Transponder replies not enabled or acquisition squitter rate 
failure (RTCA/DO-181E §2.2.10.4) 
Transmit not enabled or extended squitter rate failure 
(RTCA/DO-260B §2.2.11.2.1 and §2.2.11.5.1) 
Failure GNSS No 3D 
Fix 
No valid 3D position from GNSS (RTCA/DO-229E §2.1.2.6) 
Failure GNSS 
Unavailable 
Unable to communicate with GNSS subsystem (RTCA/DO-
260B §2.2.11.6) 
 
A.2 UCP-HD 
uAvionix Control Protocol – Half Duplex (UCP-HD) is documented in 
uAvionix UCP Transponder Interface Control  Document UAV-1002375-
001. This document is made available to authorized parties , and may be 
obtained by contacting uAvionix . 
UCP-HD can be used to configure, control, and monitor status of the 
ping200XR. 
A.2.1 Control Message 
See A.1.1 for a description of the Control message . 
 
A.2.2 Transponder Status 
With UCP-HD enabled, the Transponder Status is sent in response to each 
Control message, as documented in the ICD.  
 
The presence of a fault to annunciate is delivered by the “Fault or Failure 
Indicated” bit being set. To determine the specific fault, query the Heartbeat 
message using a Message Request. See A.1.2 for a description of the fault 
indications available in the Heartbeat message.

## Page 44

UAV-1007121-001  44 
Rev C 
A.3 Apollo 
Apollo can be used to control and monitor status of the ping200X. To use, 
ensure Apollo is enabled as an input protocol . Once an Apollo message is 
received, Apollo message output is enabled until device reset.  
A.3.1 Supported Input Messages 
The following input messages are supported : 
Mode (#MD) 
The Mode message configures the operating mode, Mode A (squawk) 
code, and IDENT. 
Setting Description Mode A Mode C Mode S 1090ES 
‘O’ STBY     
‘A’ ON 
(Altitude 
Suppress) 
X  X X 
‘C’ ALT X X X X 
 
Altitude (#AL) 
The altitude message provides pressure altitude information.  
A.4 Legacy XP Transponder Protocol  
ping200XR supports operational transponder control via the XP 
Transponder Protocol. This includes  Mode A selection, Callsign, 
Emergency Status, IDENT and Transponder Mode (STBY/ON/ALT) control.

## Page 45

UAV-1007121-001  45 
Rev C 
Appendix B  Equipment Compatibility and 
Interconnect Drawings 
ping200XR can be statically provisioned, or dynamically controlled in-flight 
by a control head or unmanned aircraft flight control computer . To meet 
installation or operational requirements , dynamic control may be required 
(e.g. to provide in-flight updates to the squawk code).  
For 14 CFR 91.225 compliance with no operational limitations, dynamic 
control is necessary.  
For 14 CFR 91.225 compliance, a position source is necessary.  
The installation information below serves as a supplement to any manuals 
describing controlling devices , and concern basic wiring of the transponder 
control and position functionalities only. For further installation and 
operating instructions, please reference the appropriate installation manual 
and pilot’s guide. The installer should become fully familiar with the 
installation process for the controlling device. These descriptions are 
informational, and in no way grant an installation approval.  
B.1 Compatible Control Protocols  
ping200XR can be controlled using equipment compatible with UCP, UCP -
HD and Apollo protocols, as documented in Appendix A. 
B.2 Compatible Equipment  
The following equipment has been shown to be compatible with 
ping200XR, and can serve as a controlling device.  
Manufacturer Model ping200XR 
Protocol Controller Configuration 
uAvionix 
AV-20-E UCP-HD [1] Enable “XPDR CTRL” page 
AV-30-E 
UCP-HD [1] 
SERIAL 2: “BEACON X” 
GPS NAV SRC: “BEACON X” (optional, enable if 
GPS track and velocity information desired) AV-30-C 
[1] Protocol must be enabled on ping200XR and baud rate set to 2400  
See below for example interconnect drawings.  
B.2.1 AV-30-C or AV-30-E Control Head  
This installation uses the ping200XR’s internal truFYX GPS for position 
data. The uAvionix AV-30-C or AV-30-E provides control, status, and 
altitude encoder data.

## Page 46

UAV-1007121-001  46 
Rev C 
 
Configure the ping200XR as appropriate, ensuring the following values 
have been updated from defaults:  
Parameter Value 
In Protocols UCP-HD 
Out Protocols UCP-HD 
Serial Port Baud Rate 2400 
Baro Altitude Source  External 
 
B.3 Third-party Equipment 
The following devices are reported to be compatible with supported 
ping200XR control protocols. These EFIS displays have the capability to 
send barometric pressure altitude data and control the mode and squawk 
functions of the ping200X R through any available RS -232 serial output. 
ping200XR configuration must still take place through the “ping200X 
Control & Config” Windows application.

## Page 47

UAV-1007121-001  47 
Rev C 
Manufacturer Model ping200XR 
Protocol Configuration Function Provided 
GRT 
MINI-B 
Apollo Serial Output: SL70/STX175 
Serial Rate: 57600 Control 
MINI-AP 
MINI-X 
Sport EX 
Horizon 
EX 
MGL 
iEFIS 
Apollo Type: STX165(R) 
Serial Rate: 57600 Control Xtreme 
EFIS 
Proper operation of the interface and system, with the specific equipment 
configuration, must be demonstrated at installation time. 
B.3.1 ping200XR Configuration 
Configure the ping200XR as appropriate, ensuring the following values 
have been updated from defaults:  
Parameter Value 
In Protocols UCP and Apollo 
Out Protocols Apollo 
Serial Port Baud Rate 57600 or as appropriate 
Baro Altitude Source  External 
 
B.3.2 Controller Configuration 
Only the EFIS serial OUTPUT is required. If no configuration information is 
provided in the compatible equipment table above, the parameters should 
be set as follows. 
Characteristics Specifications 
Physical RS-232 
Rate and properties  57,600 bps 8N1 (or as configured on 
ping200XR) 
Protocol SL70, STX 165R, or UCP 
 
B.3.3 Interconnect 
Connect the ping200XR control port Orange (RXD) wire to the appropriate 
EFIS serial port transmit (TXD) line.

## Page 48

UAV-1007121-001  48 
Rev C 
Example pinout options for certain compatible EFIS displays are shown 
below. Please consult the EFIS installation manuals for additional options 
and information. 
GRT Mini-X 
/ Mini-AP 
Serial 
1 
Serial 
2 
TXD Pin 5 1 
 
GRT Mini-B Serial 
1 
Serial 
2 
Serial 
3 
TXD Pin 5 1 9 
 
GRT Sport EX 
/ Horizon EX 
Serial 
1 
Serial 
2 
Serial 
3 
Serial 
4 
Serial 
5 
Serial 
6 
TXD Pin A2 A4 A25 A5 A3 A1
