# TPTR-55 Incident Investigation - 1.8.24.pptx

Attachment 18259, pptx, 3646 KB, added 2024-01-08 by Sean Wendling.

## Slide 1

Investigation Report
VXEP-22
FUEL CELL SN249
Tail# 510, Fuel Cell SN 249
Author: Sean Wendling
October 2023
[picture]
[picture]

## Slide 2

Links and Locations
VIT2-320 - TPTR-55 Fuel Cell Fault SN D4500249 /247
VXEP-22 - TPTR-55 Fuel Cell Failure Immediately after launch
VA-614 - Given unable to replicate, document possible causes and any CAs

## Slide 3

D450XR SN: 249 – Error Occur During Launch
Reporter: Allen Gardner (Summarized by Sean Wendling)
Severity: 3 - Degraded Performance - With Workaround
Summarize Major Findings
Edge Autonomy Proprietary Information
Aircraft 510 had a fuel cell fault during the launch wizard. Operators report that they cycled power on the fuel cell to clear the error. After launch, the fuel cell errored again, and the aircraft was landed. Fuel cell S/N 4006249. Error code 19472.
Code 19472 is described as: “K_Fault_ReactorTemp_Unexpected High” indicating system overheat in Reactor area of Fuel Cell Stack. This is observed in attached data files, as system exceeds 850°C for continuous 30 seconds. 
Cathode (Cooling System) RPM is noted at ~9600 RPM during operation, and ambient fuselage temperature (measured at Main control MCU) is ~44°C. Ambient Temp is high, but not uncommon for ground temperature prior to forward flight.

## Slide 4

Investigation Overview – Status: CA Applied, Verified, Prepping for Shipment - [Updated 01-8-2024]
Edge Autonomy Proprietary Information
3. Cathode fan intermittent malfunction.
2. Aircraft Nose Cone fan not functioning.
1.1 During fault Flights, Cathode RPM Notably higher than previous flights. Variation in Cathode units could yield weaker cooling in this article.
1. Cathode Fan not capable of reaching sufficient Cooling Flow.
[picture]
[picture]
[picture]
Investigated but inconclusive
Not the root cause or contributing factor
Root cause or contributing factor
2.1 High Amb-Temp readings during faulted flights. Known failure mode includes system overheat on Tarmac without nose cone function prior to forward flight.
3.1 Possible intermittent failure of cathode fan or control board on SN249 would cause inability to regulate temperature.
Fuel Cell Fault 19472 during VTOL launch.
Investigation Plan: 
Startup and Run System to observe Cathode Behavior in attempt to replicate.
Compare Ambient Temperature to supplied flight data.
Observe cathode for intermittent failure or inability to maintain system temperature.
Discuss with EA Flight team about environmental conditions, and nose cone function.
Perform Data review of AAR Report against collected FC cycle data.
Corrective Actions: 
Replace Cathode Blower with new unit and perform additional full system test. 
Remove and Isolate Fuel Control system, validate performance, replace malfunctioning components, and perform additional full system test.
[picture]
4. Fuel Control Failure causing system to oversupply fuel.
4.1 Fuel Solenoid or FMS Sensor malfunction could cause over-fueling leading to increased temperatures.
[picture]
[picture]
[picture]

## Slide 5

1.1/3.1 – Cathode Fan not capable of reaching sufficient Cooling Flow.
Inspect & Run system to observe cathode behavior. Signs of failed cathode include:
Prior to Operation:
Missing/poor seals on gaskets.
Bad electrical connections.
During Operation:
Abnormal Noise or Vibration.
Large parasitic current draw during high power operation.
Intermittent Failure of system notable variations in performance.
Investigation Plan
Results
Edge Autonomy Proprietary Information
Failure did not replicate in (2) Full Operational Cycles. Observations included the following:
Reaching maximum acceptable range cathode RPM. 
Above average, but within acceptable range stack temperatures. 
Above average, but within acceptable range stack parasitic power.
Result of Investigation of Cathode Function points to inability to control temperature in high temperatures. Cathode RPM not capable of reaching necessary RPM to further cool the stack is a contributing factor, though system control did not request additional flow to manage temperature.
Corrective Action: Remove and replace Cathode Unit. Re-build system and complete additional cycle to validate performance at operational temperatures
[picture]
[picture]
[picture]
Investigated but inconclusive
[picture]
[picture]
[picture]
[picture]
[chart: Incoming Bench Run #1: Cathode Flow v Stack Temperature ]
[chart: T95_V510_230623_135119 - Fault Flight: Cathode Actuator v Stack Temperature
]
[picture]
Not the root cause or contributing factor
Root cause or contributing factor
[picture]
[picture]
[picture]

Speaker notes:
SW release workflow, simulated flight hours prior to flight test, phased implementation, GNSS denied testing, regression testing refinement.

## Slide 6

2.1 – Aircraft Nose Cone fan not functioning.
Perform Data review of known system behavior during “Nose Cone Fan Non-Operation” Condition and compare to Flight AAR.
Identify and compare behavior of Fuel Cell in T95_V510_230623_135119 against known failure profile of “INOP Nose Cone”.
Look for any additional temperature trends in failure condition.
Investigation Plan
Results
Edge Autonomy Proprietary Information
Noticeable Behavior difference between “INOP Nose Cone” scenario. Temp Rate does not trend in the same fashion as the known nose cone fail condition. 
Ambient Fuselage temperature in fact trends to the negative throughout the test. While this is influenced by fault condition and subsequent FC cooldown, it is seen to mimic normal flight behavior and temperature for a Fuel Cell operating without forward flight driven RAM air flow.
Determined to not be root cause or contributing factor to incident.
[chart: MCU/Amb Temp Behavior - SN249 Fault Flight vs Known "INOP Nose Cone" Data]
[picture]
[picture]
[picture]
[picture]
[picture]
Investigated but inconclusive
Not the root cause or contributing factor
Root cause or contributing factor

Speaker notes:
SW release workflow, simulated flight hours prior to flight test, phased implementation, GNSS denied testing, regression testing refinement.

## Slide 7

4.1 Fuel Control Failure causing system to oversupply fuel.
Investigation Plan
Results
Edge Autonomy Proprietary Information
Additional Validation is required to certify the failure point; however, it is clear from functional run data that either Fuel Solenoid or FMS sensor is not functioning properly. 
Note: Normal FC operation includes small temperature driven Fuel Solenoid Variation <50pwm from initial operation. Signal exceeding 600pwm at 1.5LPM reported flow is highly uncommon.
Throughout flight/cycle in all cases, observation of output creep of fuel solenoid signal points to over fueling leading to above average temperatures. 
Corrective Action: Remove and replace Fuel Solenoid and FMS sensor. Re-build system and complete additional cycle to validate performance at operational temperatures.
[picture]
[picture]
[picture]
Investigated but inconclusive
Not the root cause or contributing factor
Root cause or contributing factor
Inspect & Run system to observe fuel system behavior. Signs of failed fuel system:
Prior to Operation:
Missing/poor seals on gaskets.
Bad electrical connections.
During Operation:
Large change of PWM signal during operation of fuel cell without change in FMS value.
Intermittent Failure of system, notable variations in performance.
[chart: Incoming Bench Run #1: Measured Fuel Flow v Fuel PWM]
[chart: Incoming Bench Run #2: Measured Fuel Flow v Fuel PWM]
[chart: T95_V510_230623_135119 - Fault Flight: Measured Fuel Flow v PWM ]
[picture]
[picture]
[picture]
[picture]

Speaker notes:
SW release workflow, simulated flight hours prior to flight test, phased implementation, GNSS denied testing, regression testing refinement.

## Slide 8

Validation of Corrective Action
Corrective Actions Implemented
Results
Edge Autonomy Proprietary Information
Results indicate that defective Fuel Sensor resulted in likely over fueling resulting in increased temperatures exceeding Cathode functional range. 
After CAs implemented, Fuel Flow reacted as intended and temperature control was maintained. Cathode flow was also reduced to a healthier range and stack performance was not affected. 
Move to close investigation.
In order to improve the temperature control performance in this system, Fuel FMS sensor and cathode unit replaced. Desired result is as follows:
Fuel PWM signal remains constant during operation.
Cathode Flow reduced/constant during operation.
[chart: Applied Corrective Action: Measured Fuel Flow v Fuel PWM]
[chart: Incoming Bench Run #2: Measured Fuel Flow v Fuel PWM]
[chart: Incoming Bench Run #2: Cathode (Cooling Blower) & Fuel Control]
[chart: Applied Corrective Action: Cathode (Cooling Blower) & Fuel Control]

Speaker notes:
SW release workflow, simulated flight hours prior to flight test, phased implementation, GNSS denied testing, regression testing refinement.

## Slide 9

[picture]
[picture]
