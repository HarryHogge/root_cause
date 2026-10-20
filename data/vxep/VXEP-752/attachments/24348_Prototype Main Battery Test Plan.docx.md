# Prototype Main Battery Test Plan.docx

Attachment 24348, docx, 368 KB, added 2024-11-01 by Rodney Linch.

Prototype Main Battery

Test Plan

Stalker VXE30

Standard & HAVOC Configurations

| Document Number: | 1xx-xxxxxx | Revision: | A |
| CAGE Code: | 9F8H9 | Date (yyyy.mm.dd): | 2024.07.15 |
| CONFIDENTIAL AND PROPRIETARY DATA: Portions of this document contain proprietary technical data pertaining to items, or components, or processes, or other matter developed or acquired at the private expense of Edge Autonomy and is restricted to use only by Edge Autonomy employees or other persons authorized by Edge Autonomy in writing to use it. Neither said document nor said technical data shall be furnished or disclosed to, or copied or used by, persons outside Edge Autonomy, without the express written approval of Edge Autonomy. Markings on this page regarding confidentiality and proprietary information apply to this entire document. | CONFIDENTIAL AND PROPRIETARY DATA: Portions of this document contain proprietary technical data pertaining to items, or components, or processes, or other matter developed or acquired at the private expense of Edge Autonomy and is restricted to use only by Edge Autonomy employees or other persons authorized by Edge Autonomy in writing to use it. Neither said document nor said technical data shall be furnished or disclosed to, or copied or used by, persons outside Edge Autonomy, without the express written approval of Edge Autonomy. Markings on this page regarding confidentiality and proprietary information apply to this entire document. | CONFIDENTIAL AND PROPRIETARY DATA: Portions of this document contain proprietary technical data pertaining to items, or components, or processes, or other matter developed or acquired at the private expense of Edge Autonomy and is restricted to use only by Edge Autonomy employees or other persons authorized by Edge Autonomy in writing to use it. Neither said document nor said technical data shall be furnished or disclosed to, or copied or used by, persons outside Edge Autonomy, without the express written approval of Edge Autonomy. Markings on this page regarding confidentiality and proprietary information apply to this entire document. | CONFIDENTIAL AND PROPRIETARY DATA: Portions of this document contain proprietary technical data pertaining to items, or components, or processes, or other matter developed or acquired at the private expense of Edge Autonomy and is restricted to use only by Edge Autonomy employees or other persons authorized by Edge Autonomy in writing to use it. Neither said document nor said technical data shall be furnished or disclosed to, or copied or used by, persons outside Edge Autonomy, without the express written approval of Edge Autonomy. Markings on this page regarding confidentiality and proprietary information apply to this entire document. |
|  |  |  |  |
|  |  |  |  |

APPROVALS

| Name | Role | Date |
| Eric Cain | Author | 2024.07.15 |
| Stephen Peters | Component Engineer | - |
| Eric Cain | Systems Engineer | 2024.07.15 |
| Cameron Chapman | Electrical Engineer | 2024.07.15 |
| Kurt Burian | Software Engineer | 2024.07.15 |
| Cody Smisek | Test Engineer | 2024.07.15 |
| Carl Graf | Project Engineer | 2024.07.15 |
| Travis Blaschke | Project Manager | 2024.07.15 |

REVISION HISTORY

| Revision | Date | Change Description |
| A | 2024.07.15 | Initial Release |
| B | 2024.10.15 | Updated to reflect generic prototype main battery for Standard or HAVOC VX30 Configurations, and to include ESR test protocols. |

Table of Figures

Figure 1: VXE30 Standard Main Battery Module Overview	5

Figure 2: HAVOC Main Battery Module Overview	6

Figure 3: Aircraft Low Voltage Test Configuration	7

Figure 4: Aircraft Integrated Battery Test Configuration	7

## Scope

The purpose of this document is to define the testing approach to qualify prototype main batteries for use in flight testing for the VXE30 Stalker Standard Configuration or HAVOC configuration aircraft. The testing involves verifying the ability for the aircraft to use the battery under expected operating conditions for a demonstration flight.

## References

A list of Edge Autonomy reference documents is given in Table 1.

| Table 1: Edge Reference Documents | Table 1: Edge Reference Documents |
| Document Number | Description |
| 1xx-xxxxxx | Prototype Amprius Battery Endurance Demonstration Test Plan Stalker VXE30 Standard Configuration |
| 1xx-xxxxxx | Main battery_model-cam.xlsx |

A list of external reference documents is given in Table 2.

| Table 2: External Reference Documents | Table 2: External Reference Documents |
| Document Number | Description |
| XXXXXX |  |
| YYYYYY |  |

## VXE30 Standard Configuration Main Battery Module Description

The Main Battery Module for VXE30 Standard Configuration (Std-Main) is designed to be a direct replacement of the previous Main Batteries used in the VXE30 Standard aircraft. The battery is packaged within the same form factor as earlier battery designs to enable interoperability with the existing aircraft. The battery cells are arranged in a 7SXP configuration providing nominally 28VDC power for all aircraft systems, potentially including the VTOL motors. The chemistry of the cells may be variable, and results in an operational voltage range from 17.5-29V, depending on State of Charge (SOC). Battery capacity is expected to be 1,100Whr for Small Std-Main batteries (7S4P configuration) and 2,750Whr for Large Std-Main batteries (7S10P configuration).

An image of the Std-Main Battery Module is shown in Figure 1.

Figure 1: VXE30 Standard Main Battery Module Overview

## VXE30 HAVOC Configuration Main Battery Module Description

The Main Battery Module for VXE30 HAVOC Configuration (HVC-Main) is designed to be used in the VXE30 HAVOC aircraft. The battery is packaging is to be determined.  The battery cells are arranged in a 14SXP configuration providing nominally 56VDC power for all aircraft flight systems, potentially including the VTOL motors.  Aircraft avionics and payload power must be supplied from a secondary power output port at 28V nominal power. The chemistry of the cells may be variable, and results in an operational voltage range from 35.0-58.8V, depending on State of Charge (SOC). Battery capacity is expected to be 1,100Whr for Small HVC-Main batteries (14S2P configuration) and >2,750Whr for Large HVC-Main batteries (14S5P or 14S6P configuration).

An image of the Std-Main Battery Module is shown in Figure 1.

Figure 2: HAVOC Main Battery Module Overview

## Test Objectives and Requirements

This test campaign is established as a prototype demonstration of capability and does not verify any contractual or company requirements. However, to facilitate test definition and ensure a safe and useful demonstration of the aircraft performance with the new battery, the following test objectives have been identified in Table 3.

| Table 3: Test Objectives | Table 3: Test Objectives |
| Objective ID | Objective |
| 1 | Main battery shall fit within the VXE30 aircraft with no modifications required. |
| 2 | Develop configuration INI file for main battery under test. |
| 3 | Std-Main Battery shall provide at least 500W of continuous power at all SOC levels, and HVC-Main Battery shall provide at least 750W of continuous power at all SOC levels. |
| 4 | VXE30 Standard shall operate normally with SOC as low as 5% |
| 5 | GCS shall report battery State of Charge (SoC) +/-5% No Load, |
| 6 | GCS shall report battery State of Charge (SoC) +/-5% Motor Load, Battery, various SoC |
| 7 | The VXE30 Standard and HAVOC configurations shall have an endurance >1 hour |

## Test Configuration

The following configurations and equipment are used:

Figure 3: Aircraft Low Voltage Test Configuration

Figure 4: Aircraft Integrated Battery Test Configuration

| Table 4: Software & Firmware Configurations | Table 4: Software & Firmware Configurations | Table 4: Software & Firmware Configurations |
| Component | Version | Notes |
| Ground Control Station (GCS) | 0.2.11 |  |
| Fixed Wing Autopilot | 6.05o | 0605000F – C4D9 |
| VTOL Autopilot | 1.54 | 04000044 – 5F8F |
| XCOMM | 4.68 | 01000036 – 24F0 |

## Test Approach

There are four test events planned to satisfy the objectives outlined above. The events are shown in Table 5 and explain in detail within the following sections.

| Table 5: Test Events | Table 5: Test Events | Table 5: Test Events | Table 5: Test Events |
| Event ID | Objective(s) | Description | Location |
| 1 | 3,5,6 | ESR Measurement | Ground/Benchtop |
| 2 | 2 | Configuration Table | Analysis |
| 3 | 1 | Fit check | Ground/Benchtop |
| 4 | 4,5 | Aircraft Low Voltage Test | Ground/Benchtop |
| 5 | 3,6 | Aircraft Integrated Battery Test | Ground/Tethered |
| 6 | N/A | Aircraft SCO | Flight |
| 7 | 7 | Flight Demonstration | Flight |

## ESR Measurement

To complete the measurement of Equivalent Series Resistance (ESR), the prototype Main Battery must start at a fully charged state (100% SOC), and the battery connected to an electronic load that can apply the following discharge profile:

30-second initial pulse at 30 Amps (simulates climb and drives internal heating of the pack)

15-minute, 300W load

10-second, 30A load

Continue steps 2&3 until the Main battery reaches 0% SOC

The captured battery data can be analyzed to determine the ESR.  An example sheet can be found here: Main battery_model-cam.xlsx.  After the ESR is determined from this data analysis, an estimate of the Battery SOC corrections can be made to fine-tune the SOC estimates in the autopilot.  These estimates can also be found in the data analysis excel file.  Both the ESR and the Battery SOC corrections will be used to generate the configuration ini file (7.2 Configuration Table).

Appendix A– ESR Test Procedures is a good test procedure reference.

## Configuration Table

Fill out Table 6 to complete the configuration ini file used by the GCS to communicate main battery information to the aircraft.

| Table 6: Main Battery Configuration Table | Table 6: Main Battery Configuration Table | Table 6: Main Battery Configuration Table | Table 6: Main Battery Configuration Table |
| Name | Description | Value (Amicell main battery shown) |
| [NAME] | Battery ID | [VXE_MAIN] |
| MotorCutoff | Voltage of motor cutoff (mV) | 21000 |
| MotorStart | Voltage of motor start (mV) | 24000 |
| BattFull | Voltage of at 100%SOC (mV) | 29000 |
| BattEmpty | Voltage at 0%SOC (mV) | 23500 |
| BattCapacity | Derated Energy Capacity (90% of full battery energy in kWsec) | 5040 |
| NominalEndure | Minutes of endurance | 240 |
| PowerLimit | Power limit (W) | 0 |
| BasePower | ? (W) | 0 |
| ESR | Equivalent Series Resistance | 30 |
| HybridUpperLimit | Hybrid sate limits (%) | 0 |
| HybridLowerLimit | Full panic hybrid state | 0 |
| HybridPowerLimit | Happy hybrid state | 0 |
| Spare1 |  | 0 |
| Spare2 |  | 0 |
| Spare3 |  | 0 |
| Options | Bitmapped to use these configuration data: #define BOBITS_MOTORCUTOFF 0x0001 #define BOBITS_MOTORSTART 0x0002 #define BOBITS_BATTFULL 0x0004 #define BOBITS_BATTEMPTY 0x0008 #define BOBITS_BATTCAPACITY 0x0010 #define BOBITS_NOMINALENDURE 0x0020 #define BOBITS_POWERLIMIT 0x0040 #define BOBITS_BATTTABLE 0x0080 #define BOBITS_BASEPOWER 0x0100 #define BOBITS_ESR 0x0200 #define BOBITS_HYB 0x0400           // hybrid control values valid, hupper, hlower, hpower #define BOBITS_LIPO11 0x0800            // use ESD11 battery correction table   #define BOBITS_FUELCELL 0x1000      // true to allow fuel cell to operate if installed | 767 |
| BatteryTable[00] | 100% SOC correction.  Must be ZERO | 0 |
| BatteryTable[01] | 95% SOC Correction (additive %) | 1 |
| BatteryTable[02] | 90% SOC Correction (additive %) | 0 |
| BatteryTable[03] | 85% SOC Correction (additive %) | -2 |
| BatteryTable[04] | 80% SOC Correction (additive %) | -2 |
| BatteryTable[05] | 75% SOC Correction (additive %) | -2 |
| BatteryTable[06] | 70% SOC Correction (additive %) | -1 |
| BatteryTable[07] | 65% SOC Correction (additive %) | -1 |
| BatteryTable[08] | 60% SOC Correction (additive %) | -1 |
| BatteryTable[09] | 55% SOC Correction (additive %) | -1 |
| BatteryTable[10] | 50% SOC Correction (additive %) | -3 |
| BatteryTable[11] | 45% SOC Correction (additive %) | -4 |
| BatteryTable[12] | 40% SOC Correction (additive %) | -5 |
| BatteryTable[13] | 35% SOC Correction (additive %) | -4 |
| BatteryTable[14] | 30% SOC Correction (additive %) | -4 |
| BatteryTable[15] | 25% SOC Correction (additive %) | -5 |
| BatteryTable[16] | 20% SOC Correction (additive %) | -5 |
| BatteryTable[17] | 15% SOC Correction (additive %) | -6 |
| BatteryTable[18] | 10% SOC Correction (additive %) | 0 |
| BatteryTable[19] | 5% SOC Correction (additive %) | 1 |
| BatteryTable[20] | 0% SOC correction.  Must be ZERO | 0 |
| BatteryTable[21] | ?? | 0 |

## Fit Check

The fit check simply verified the physical fit of the Main Battery within the VXE30 Stalker ensures that no modifications to the aircraft are required.

PASS/FAIL Criteria: Std-Main Battery is installed into a VXE30 Standard aircraft and removed without modification.  HVC-Main Battery is installed into a VXE30 HAVOC aircraft and removed without modification.

## Aircraft Low Voltage No Load Test

This test checks the ability of the aircraft to operate at the battery’s minimum SoC. At low SoC and high load, the bus voltage is expected to drop as low as 17 VDC and 34VDC for Standard and HAVOC configurations, respectively. The aircraft must be tested to see if any undesirable impacts to system functions come from operating at this low voltage.

To achieve this, an external power supply will be used in place of the Main Battery to provide aircraft power and the bus voltage slowly reduced until any of the aircraft system begin to present unexpected behavior or the minimum test voltage limit is reached.

During this test, the accuracy of the Ground Control Station (GCS) SoC estimates will be checked against the expected results for given bus voltage. System electrical load will be kept low (no forward motor) to get as close to no-load condition as possible while taking voltage measurements.

After the voltage has been reduced to 19.5V/ 0% SOC (Standard configuration) or 39V / 0% (HAVOC configuration), the throttle will be increased until the motor power reads 500W (Standard Configuration) or 750W (HAVOC Configuration), or max throttle if unable to reach 500W or greater.

After the test is completed, an After Action Report (AAR) will be downloaded/checked from the aircraft to ensure system behaviors that cannot be readily observed in real time are as expected and there are no detrimental effects of the low bus voltage. At a minimum, the parameters listed in Table 6 will be checked for detrimental behaviors.

Appendix B– Aircraft Low Voltage Test Procedures is a good test procedure reference.

| Table 7: System Parameters to Observe at Low Voltage | Table 7: System Parameters to Observe at Low Voltage |
| Parameter | GCS Location |
| Voltage | GCS Sidebar |
| Power | GCS Sidebar |
| ADB | Lift AP/Instrument page or |
| GPS | tools/GPS Signal Quality GSV ON-has GPS satellite info.  tools/Custom Payload Control/Aux 1 Power Off |
| AP Mag | GCS/tools/Instrument Panel/Yaw. Note 1 |
| Fwd motor | Controller. |
| VTOL GPS | Measure the effect on Cn0 from the new equipment powered and not powered |
| VTOL Mag | Lift AP/Sensor page. |
| LRF | Lift AP/Hardware |
| Payload | Skylink for Trillium turret-Not installed |
| SA Cam | GCS SW |
| Servos (flight controls) | Move RC stick and verify surfaces respond correctly. |
| Silvus Radio | See spectrum scan. Ask Kurt |
| VTOL CSA | Lift AP/Sensors/ib1 and 2 |
| AP CSA | XCOM/Sensors/i12? |

PASS/FAIL Criteria:

All required parameters are within expected limits and system operates without detrimental effects at the bus voltage of 17.0V (Standard Configuration) or 34.0V (HAVOC Configuration).

GCS reports SoC within +/-5% of expected values for all test points

## Aircraft Integrated Battery Test

This test event will check the Prototype Main Battery’s ability to meet basic performance requirements when integrated in an aircraft. The ability for the battery to sustain power output on the aircraft and the accuracy of the battery SoC calculations will be checked. The aircraft systems are used to draw power from the battery, with the forward motor being the primary load on the system. For this reason, the aircraft will be strapped down to prevent movement under the propeller thrust. An RC controller will be used to control motor throttle and therefore system electrical load. During this test, the individual cell voltages will also be monitored using the Charge Port on the battery.

Test will follow the steps outlined in Table 8 and begin with the battery SoC ~25%. The system is powered up and with the minimum systems running, SoC reported by the aircraft checked against pre-test measurements. Throttle will then be lowered to zero and SoC and Voltage checked. The throttle will then be raised until 500W (for Standard Configuration, 750W for HAVOC configuration) is drawn and maintained until discrete SoC readings are indicated where no-load SoC will be checked by returning throttle to zero. After each no-load SoC check is completed, the throttle is raised again until the next no-load test point is reached and repeated until the SoC reads 0%.

Appendix C– Aircraft Integrated Battery Test is a good test procedure reference.

| Table 8: Aircraft Integrated Battery Test Events | Table 8: Aircraft Integrated Battery Test Events | Table 8: Aircraft Integrated Battery Test Events |
| Seq. # | Battery SoC | Test Condition |
| 1 | 25% | Initial Condition |
| 2 |  | Load = 500W (Standard), or 750W (HAVOC) |
| 3 | 15% | No-Load SoC Measurement |
| 4 |  | Load = 500W (Standard), or 750W (HAVOC) |
| 5 | 10% | No-Load SoC Measurement |
| 6 |  | Load = 500W (Standard), or 750W (HAVOC) |
| 7 | 5% | No-Load SoC Measurement |
| 8 |  | Load = 500W (Standard), or 750W (HAVOC) |
| 9 | 0% | No-Load SoC Measurement |
| 10 |  | VTOL Strapped down Takeoff/Landing Simulation |

AAR data will be downloaded and checked against expected SoC tables. The depleted battery will be removed and final battery open-circuit voltage will be measured. The battery is then recharged for later testing.

PASS/FAIL Criteria:

Battery is able to power the aircraft at 500W (Standard, or 750W HAVOC) sustained to 0%SoC

GCS reports SoC within +/-5% of expected values for all test points

Note: 0% SoC is value calculated from battery voltage vs SoC table, but a small capacity margin remains in the battery at this reading)

## Aircraft SCO Flight

A single System Checkout (SCO) flight of the demonstration aircraft will be performed using a legacy “Standard” main battery to ensure full system functionality of the basic aircraft without risking damage to the prototype Amprius Main Battery. This flight will follow standard operating procedures for the VXE30 Stalker Standard Configuration aircraft.

PASS/FAIL Criteria:

Aircraft completes SCO flight with no open issues

## Flight Demonstration

This test demonstrates the real-world flight endurance of the VXE30 with the Prototype Main Battery in support of customer program proposals and provided engineering data on the performance of the battery in flight conditions. The aircraft will be weighed with mass simulant to represent the weight of Trellis Repeater and E140 payloads. The E140 mass simulant will also represent the sensor physical profile to ensure drag is representative of a real payload. These payloads are not active, so will not be drawing power from the battery and the true flight endurance of the aircraft with both payloads operating must be calculated after flight data is collected.

The Main Battery under test will be charged to 100% prior to flight. The mission profile will consist of a standard VTOL takeoff, transition to 400 ft MSL altitude flown in a circular orbit or racetrack until SoC reaches 5%. The aircraft will then immediately return to the landing point and conduct a VTOL landing.

After flight, the AAR will be downloaded and data reviewed for battery capacity and endurance with operating payloads estimated using nominal power draws for operating Trellis Repeater and E140 sensor turret.

Appendix D– Flight Demonstration is a good test procedure test reference.

PASS/FAIL Criteria:

Data collected on maximum endurance of Prototype Main Battery

## – ESR Test Procedures

|  | TASK | LEAD | DESCRIPTION |
|  |  |  | SETUP |
|  | TD | Attach the prototype battery under test to an electronic load capable of 30A & 60V input.  Ensure that the electronic load control software is able to generate a test procedure that will operate in a constant load, followed by periodic high current pulses.   Measure/Calculate/Analyze the prototype battery voltage at 100% and 0% SOC.  Start with the prototype battery at 100% SOC. |
|  |  |  | ESR TEST CONDITIONS |
|  |  | Ensure that the electronic load program is setup to operate at: -30A for 30 seconds -Cyclic performance of 300W / 15 minutes, and 30A / 10 seconds -End test condition at a battery voltage of < = 0% SOC -Save all data: voltage, current, power, integrated Amp-hour capacity, integrated Watt-hour energy. |
|  |  | ALL | WARNING The next step will apply electrical power to the battery. Risk of injury from electronic equipment may occur.  Ensure all personnel are clear of battery before connecting battery to the load. |
|  | TD | Plug in battery to electronic load and ensure that the battery voltage is displayed on the electronic load and on the electronic load control software.  Start electronic load program. |
|  | TD | Observe battery voltage and cancel the test if the battery voltage drops to less than 0% SOC.  Monitor battery temperature and cancel the test if visible signs of overheating exist (smoke, severe discoloration, swelling). |
|  | TD | Record time when the battery test completes. |
|  | TD | Open saved data file and copy recorded data into template. |
|  | TD | Adjust ESR parameters in template to achieve a reasonable fit of calculated data during the 30A pulse events |
|  | TD | Record error value at 5% SOC intervals to fine-tune battery SOC table. |
|  | TD | Save data, and store resulting ESR and Battery SOC correction values. |

## – Aircraft Low Voltage Test Procedures

|  | TASK | LEAD | DESCRIPTION |
|  |  |  | SETUP |
|  | TD | Configure aircraft and test setup per Figure 3. Ensure aircraft is strapped down for Forward Motor/Propeller operation.  Ensure Amprius GCS is installed with ini file that enables RC controller.  Need to run launch wizard to main battery ok. Click next. Battery percentage should change. Cancel then. |
|  |  | ALL | CAUTION This test will apply power to the forward motor and propeller. Failure to properly secure the aircraft may result in damage to flight hardware Ensure aircraft is strapped to stable platform for forward motor operations. |
|  |  |  | TEST CONDITIONS – NO MOTOR LOAD PORTION |
|  |  |  |  |
|  |  | ALL | WARNING The next step will apply electrical power to the aircraft. Risk of injury from rotating propellers may occur.  Ensure all personnel are clear of propellers before connecting battery. |
|  | TD | Turn on external power supply, set to 28VDC and output power to aircraft power harness and Record time of Power-On |
|  | TD | Conduct aircraft configuration steps through GCS. Open “Launch Wizard” and “Cancel” the window to ensure battery tables are uploaded to aircraft. |
|  | TD | Slowly raise Power Supply output voltage to 30.0V, observe system for unexpected behaviors Notes: |
|  | TD | Record Power Supply Voltage and Battery SoC reported on GCS |
|  | TD | Slowly reduce Power Supply output voltage to 28.0V, observe system for unexpected behaviors Notes: |
|  | TD | Record Power Supply Voltage and Battery SoC reported on GCS |
|  | TD | Slowly reduce Power Supply output voltage to 26.0V, observe system for unexpected behaviors Notes: |
|  | TD | Record Power Supply Voltage and Battery SoC reported on GCS |
|  | TD | Slowly reduce Power Supply output voltage to 24V, observe system for unexpected behaviors Notes: |
|  | TD | Record Power Supply Voltage and Battery SoC reported on GCS |
|  | TD | Slowly reduce Power Supply output voltage to 22.0V, observe system for unexpected behaviors Notes: |
|  | TD | Record Power Supply Voltage and Battery SoC reported on GCS |
|  | TD | Slowly reduce Power Supply output voltage to 21.0V, observe system for unexpected behaviors Notes: |
|  | TD | Record Power Supply Voltage and Battery SoC reported on GCS |
|  | TD | Slowly reduce Power Supply output voltage to 20.0V, observe system for unexpected behaviors Notes: |
|  | TD | Record Power Supply Voltage and Battery SoC reported on GCS |
|  | TD | Slowly reduce Power Supply output voltage to 19.5V, observe system for unexpected behaviors Notes: |
|  | TD | Record Power Supply Voltage and Battery SoC reported on GCS |
|  | TD | Slowly reduce Power Supply output voltage to 19.0V, observe system for unexpected behaviors Notes: |
|  | TD | Record Power Supply Voltage and Battery SoC reported on GCS |
|  | TD | Slowly reduce Power Supply output voltage to 18.5V, observe system for unexpected behaviors Notes: |
|  | TD | Record Power Supply Voltage and Battery SoC reported on GCS |
|  | TD | Slowly reduce Power Supply output voltage to 18.0V, observe system for unexpected behaviors Notes: |
|  | TD | Record Power Supply Voltage and Battery SoC reported on GCS |
|  |  |  | Verify Motor Cuts off as voltage reached 17.1V. Motor should restart at 17.48V. |
|  |  |  | Disable motor cut offs before proceeding. |
|  | TD | Slowly reduce Power Supply output voltage to 17.5V, observe system for unexpected behaviors Notes: |
|  | TD | Record Power Supply Voltage and Battery SoC reported on GCS |
|  | TD | Slowly reduce Power Supply output voltage to 17.0V, observe system for unexpected behaviors Notes: |
|  | TD | Record Power Supply Voltage and Battery SoC reported on GCS |
|  |  |  | TEST CONDITIONS – MOTOR LOADED PORTION |
|  |  | Return the power supply voltage to the level that indicates 0% SOC. |
|  |  |  | Check each of the indicated systems below. For each system, ensure the low voltage is not impacting performance.  Check each system at 0 throttle,  Ramp the forward motor current to 500W (or full throttle if the aircraft cannot reach 500W). If 500W was not full throttle, ramp to full throttle. Check each system at full throttle.  Record results. |
|  |  | TD | Return Power Supply voltage to 28V |
|  |  |  | POST-TEST |
|  | TD | Collect After Action Report (AAR) data (Data files to be transferred to: [LOCATION TBD]) |
|  | TD | Power down aircraft and test equipment and Record time of aircraft power-off |

## – Aircraft Integrated Battery Test

|  | TASK | LEAD | DESCRIPTION |
|  |  |  | SETUP |
|  | TD | Configure aircraft and test setup per Figure 4. Ensure aircraft is strapped down for Forward Motor/Propeller operation. Remove existing GCS program from laptop. Ensure Amprius GCS is installed with ini file that enables RC controller.  Need to run launch wizard to main battery ok. Click next. Battery percentage should change. Cancel then. |
|  |  | ALL | CAUTION This test will apply power to the forward motor and propeller. Failure to properly secure the aircraft may result in damage to flight hardware Ensure aircraft is strapped to stable platform for forward motor operations. |
|  |  |  | TEST CONDITIONS |
|  |  |  | Begin recording individual battery cell voltages on data logger. Set alarm voltage to 2.5V/Cell |
|  |  |  | CAUTION  Low cell voltages may cause permanent damage to battery cells.  Monitor cell voltages throughout this test. Immediately cut throttle and stop the test if any of the cells drop below 2.5V/cell (~17.5V total). |
|  |  | ALL | WARNING The next step will apply electrical power to the aircraft. Risk of injury from rotating propellers may occur.  Ensure all personnel are clear of propellers before connecting battery. |
|  | TD | Connect Main Battery to aircraft power harness and Record time of Power-On |
|  | TD | Conduct aircraft configuration steps through GCS. Open “Launch Wizard” and “Cancel” the window to ensure battery tables are uploaded to aircraft. |
|  | TD | With minimum required equipment running on aircraft, Record reported bus Voltage, Power Consumption and Battery SoC |
|  | TD | Using RC Controller, increase forward motor throttle until system power consumption indicates 1500W and maintain setting for 3 minutes |
|  | TD | Reduce throttle until system power consumption indicates 500W and maintain until Battery SoC indicates 15% |
|  | TD | Reduce throttle until forward motor/propeller is completely off. Record system Voltage, Power and SoC |
|  | TD | Increase throttle until system power consumption indicates 500W and maintain until Battery SoC indicates 10% |
|  | TD | Reduce throttle until forward motor/propeller is completely off. Record system Voltage, Power and SoC |
|  | TD | Increase throttle until system power consumption indicates 500W and maintain until Battery SoC indicates 5% |
|  | TD | Reduce throttle until forward motor/propeller is completely off. Record system Voltage, Power and SoC |
|  | TD | Increase throttle until system power consumption indicates 500W and maintain until Battery SoC indicates 1% |
|  | TD | Reduce throttle until forward motor/propeller is completely off. Record system Voltage, Power and SoC |
|  | TD | Power down aircraft by disconnecting battery and Record time of Power-off |
|  |  |  | Reconfigure aircraft for tethered VTOL flight |
|  |  | ALL | CAUTION This test will apply power to the VTOL motors and propellers. Failure to properly secure the aircraft may result in damage to flight hardware Ensure aircraft is tethered for VTOL motor operations. |
|  |  | ALL | WARNING The next step will apply electrical power to the aircraft. Risk of injury from rotating propellers may occur. Ensure all personnel are clear of propellers before connecting battery. |
|  | TD | Connect Main Battery to aircraft power harness and Record time of Power-On |
|  | TD | Conduct aircraft configuration steps through GCS. Open “Launch Wizard” and “Cancel” the window to ensure battery tables are uploaded to aircraft. |
|  | TD | Record system Voltage, Power and SoC |
|  | TD | Initiate VTOL takeoff and monitor system for unexpected behaviors. Hover for minimum 30s[TBR] and land aircraft. |
|  | TD | Record system Voltage, Power and SoC |
|  |  |  | POST-TEST |
|  | TD | Collect After Action Report (AAR) data (Data files to be transferred to: [LOCATION TBD]) |
|  | TD | Power down aircraft and test equipment and Record time of aircraft power-off |
|  | TD | Remove Main Battery and connect to charger. Charge to 80% SoC = 3.87 V/cell in anticipation of flight test. If no test is planned within 7 days, charge to storage SOC. 3.62V/Cell 25.34 |

## – Flight Demonstration

|  | TASK | LEAD | DESCRIPTION |
|  |  |  | PRE-FLIGHT |
|  | TD | Report “crew onsite” to stakeholders |
| TD | Hold Mission Brief |
|  | RPIC | Unpack and assemble SGCS-1 |
|  | RCP | Unpack Air Vehicle |
|  | RCP | Record Equipment Serial Numbers in table to right: |
|  |  | ALL | WARNING The next step will apply electrical power to the aircraft. Risk of injury from rotating propellers may occur.  Ensure all personnel are clear of propellers before connecting battery. |
|  | RCP | Connect Main Battery and HLB to aircraft power harness and Record time of Power-On |
|  | FTE | Record system Voltage, Power and SoC |
|  | RCP | Finish Air Vehicle Assembly |
|  | RCP | Measure and Record AV Weight & Balance Add ballast as required to achieve X-CG within operating limits Report final Weight & Balance to TD. |
|  |  | RPIC | Configure GCS/Aircraft settings per SOP |
|  | RCP | Verify that RC control is functional |
|  |  | RPIC | Disable “Auto LOS” and “Auto AGL” functions |
|  | RPIC | Finalize and upload Mission Plan |
|  | PIC | Hold pre-flight brief |
|  | RCP | Measure and Record Ambient Temperature & Barometric Pressure |
|  | RPIC | Delegate filming of VTOL Launch and VTOL Landing |
|  | TD | Report “ready for mission” to stakeholders |
|  |  |  | LAUNCH |
|  |  | ALL | NOTE Due to the long duration of this test event, crew time limits and the available time to complete the objectives should be evaluated before initiating flight. Crew Duty Limit is set at 10hours with maximum in-flight time for Pilots limited to 8hrs. |
| ☐ |  | RPIC | Initiate VTOL Take-Off |
|  | TD | Record Take-Off Time |
|  | RPIC | Climb to 300ft, transition to Fixed Wing Flight |
|  | RPIC | Climb to 400ft MSL in a large radius orbit or race-track pattern. Orbit location, direction, altitude, and radius at RPIC’s discretion to optimize safety and endurance. |
|  |  |  | TEST CONDITION 1 - ENDURANCE |
|  |  |  | CAUTION This flight tests a new design battery to maximum endurance and will bring battery State of Charge (SoC) near limit conditions. Low battery voltage/SoC could result in loss of aircraft. Monitor electrical power telemetry regularly throughout the flight. If Bus Voltage <19.5V, return-to-base and land as soon as possible |
|  | RPIC | Remain in orbit within authorized test range & altitudes |
|  | TD | Each Hour of Flight, Record Ground Weather Conditions |
|  | FTE | Each Hour of Flight, Record aircraft power state |
|  | TD | When Voltage is less than 19.5V V Test Condition 1 is COMPLETE |
|  |  |  | RECOVERY |
|  | RPIC | Transition to Landing Site and initiate VTOL Landing |
|  | TD | Record Landing Time |
|  | RPIC | Take Screen capture of GCS display showing flight time, mission flight path (Under “Track” menu, turn off “Show Recent” to show full ground track from flight) and save files. (Files to be transferred to:  Sharepoint\IRAD\Documents\General\Projects\Battery_NextGenForward\30V Amprius Forward\Prototype Battery Test July 2024) |
|  | RPIC | Collect After Action Report (AAR) data (Data files to be transferred to:  Sharepoint\IRAD\Documents\General\Projects\Battery_NextGenForward\30V Amprius Forward\Prototype Battery Test July 2024) |
|  | RCP | Remove Center Wing assembly and disconnect Main Battery & Hybrid Lift Battery, Record Power-Off Time |
|  | TD | Report “Mission Complete” to stakeholders |
|  |  |  | POST-FLIGHT |
|  | FTE | Remove Main Battery and measure open-circuit voltages of individual cells and pack. Record voltages below |
|  | FTE | Connect Main Battery and HLB to chargers and return to 50% SoC minimum |
