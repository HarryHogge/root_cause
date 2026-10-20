# Investigation Report VXE-545.pdf

Attachment 23332, pdf, 2604 KB, added 2024-09-20 by Pat Wells.

## Page 1

Investigation Report 
VXE- 545  
Incident Number: VXEP-384 
Revision: 1 
Author: Raj Budhabhatti 
Reviewer: Hayden Jeanor 
Date: 9/20/2024 
 
CONFIDENTIAL AND PROPRIETARY DATA: 
Portions of this document contain proprietary technical data pertaining to items, or components, or processes, or 
other matter developed or acquired at the private expense of Edge Autonomy and is restricted to use only by Edge 
Autonomy employees or other persons authorized by Edge Autonomy in writing to use it. Neither said document 
nor said technical data shall be furnished or disclosed to, or copied or used by, persons outside Edge Autonomy , 
without the express written approval of Edge Autonomy. Markings on this page regarding confidentiality and 
proprietary information apply to this entire document.

## Page 2

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  2 
Table of Contents 
1 Description ............................................................................................................................................ 5 
1.1 Operator Description of the Incident .......................................................................................... 5 
2 Summary ............................................................................................................................................... 5 
3 Issue Status ........................................................................................................................................... 6 
4 Plan ....................................................................................................................................................... 6 
5 Root Cause ............................................................................................................................................ 6 
6 Investigation Overview ......................................................................................................................... 7 
6.1 Potential Cause: Software or Configuration issues. .................................................................... 7 
6.2 Potential Cause: User Error ......................................................................................................... 7 
6.3 Potential Cause: Malfunction of Autopilot or electronics ........................................................... 7 
6.4 Potential Cause: VTOL Motor issues ............................................................................................ 8 
6.4.1 VTOL Motor Issue- Motor-ESC History .................................................................................... 9 
6.5 Potential Cause: Manufacturing Issue. ...................................................................................... 10 
6.5.1 Defective Motor MOSFET Check ........................................................................................... 11 
6.6 VTOL Soft-Start circuit issue ...................................................................................................... 13 
7 Corrective Actions and Recommendations ......................................................................................... 15 
7.1 Include a motor fault flag during the LW spin up test that triggers if the VTOL controller 
detects current anomaly. ........................................................................................................................ 15 
7.2 Remove or bypass soft start circuit from VTOL ESCs. ............................................................... 15 
7.3 Corrective Recommendations: .................................................................................................. 15 
7.3.1 Improve wire routing and support of VTOL ESCs. ................................................................. 15 
7.3.2 Increase air flow to VTOL ESC heat sinks .............................................................................. 16 
7.3.3 Add temperature sensor to VTOL ESCs. Abort launch at limits. ........................................... 16 
8 Implication to the Aircraft ................................................................................................................... 16

## Page 3

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  3 
9 Conclusion ........................................................................................................................................... 17 
10 Appendix1 Motor Total Harmonic Distortion Test ........................................................................ 18 
10.1 VXE545 Motor ........................................................................................................................... 18 
10.2 Stock Motor ............................................................................................................................... 18 
10.3 Overlaid Comparison. ................................................................................................................ 19 
11 Appendix 3 Motor 3 low Force investigation ................................................................................. 20 
11.1 Summary .................................................................................................................................... 20 
11.2 Current Measurement ............................................................................................................... 22 
 
 
Figure 1 VXE-545 Force compared to a standard motor .............................................................................. 8 
Figure 2 VXE-545 Force compared to a standard motor .............................................................................. 9 
Figure 3 VXE-545 Current draw compared to a standard motor .................................................................. 9 
Figure 4 Figure 4 VXE-545 ESC .................................................................................................................... 10 
Figure 5 Figure 5 Comparing reassembled VXE-545 to stock motor .......................................................... 11 
Figure 6 Figure 6 Current state of VXE-545 Motor-ESC .............................................................................. 11 
Figure 7 ESC-Motor performance with one Low-Side MOSFET removed. ................................................. 12 
Figure 8 ESC-Motor performance with one Hi-Side MOSFET removed. ..................................................... 12 
Figure 9 Soft-start Circuit ............................................................................................................................ 13 
Figure 10 Motor Operation with Soft-start circuit disabled. ...................................................................... 14 
Figure 11 Motor Operation after Soft-start circuit damaged ..................................................................... 14 
Figure 12 Suggested Solder position ........................................................................................................... 16 
Figure 13 VXE545 Motor THD ..................................................................................................................... 18 
Figure 14 Stock Motor THD ......................................................................................................................... 19 
Figure 15 VXE545 and Stock Motor THD Side-by-side. ............................................................................... 20 
Figure 16 Right rear thrust command at or near maximum. ...................................................................... 20 
Figure 17 Uncommented pitch/roll excursion. ........................................................................................... 21

## Page 4

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  4 
Figure 18 Abort commanded after position excursion. .............................................................................. 21 
Figure 19 Abort commanded after position excursion. .............................................................................. 22 
Figure 20 Current Measurement ................................................................................................................ 23 
Figure 21 Comparison of Current draw. ..................................................................................................... 23 
Figure 22 Current Draw ............................................................................................................................... 23 
Figure 23 Throttle comparison. .................................................................................................................. 23 
Figure 24 Current, Throttle values, measured and calculated ................................................................... 24 
Figure 25 Comparison Contd. ..................................................................................................................... 25 
Figure 26 Current measurement-During Rotor test ................................................................................... 26 
Figure 27 Current Measurement during Reference flight .......................................................................... 27

## Page 5

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  5 
1 Description 
1.1 Operator Description of the Incident 
The trials team arrived on location at approx. 0845 to set up the GCS and support equipment for the 
day's flying. As we were operating in a new location a magnetometer check was carried out and a 
subsequent magnetometer swing completed. Following this the UA was used for ground testing for 
approx. 2 hrs. For the ground testing only the payload and main battery were fitted. On completion of 
the ground testing the UA was fully assembled with all pre-flight checks and GCS launch wizard 
completed successfully. These checks include motor checks for all 4 VTOL lift motors and main motor, 
pitot-static checks, payload operation and control surface operation. The immediate area around the UA 
was cleared (out to 30m) and it was confirmed that all trial pers and support pers were in the designated 
area. With no indication of issues or faults the command was given to launch the UA. On launch, the 
UA's VTOL motors spun up and lifted the UA clear of its cradle, approx. 3ft above ground, but 
the UA appeared to be underpowered and unstable. The UA then dipped its right wing and 
travelled backwards (either being blown by the wind or following its automatic abort profile). 
The right-wing tip impacted the ground and dragged until the aircraft settled on the ground 
(prior to the RP's commanded abort) . The command was given to abort the take -off which the RP 
carried out using first, the hand controller and then the Ctrl-A keyboard shortcut until the rotors stopped 
spinning. The UA was made safe and returned to the cradle. The UA wa s inspected for damage with 
preliminary minor damage found of the right -wing tip and payload housing. The launch wizard was 
carried out as a post flight activity and all systems functioned correctly. As the reason for the UA's 
behavior was still unknown and further investigation required the UA, payload, and batteries were 
quarantined. The planned sortie was subsequently flown with our second UA without incident. 
2 Summary  
During a flight test lift-off, the aircraft did not execute a vertical take-off but instead it dragged backwards 
and failed to lift off. This was caused by the rear -right motor not producing sufficient thrust. Motor -ESC 
pair were shipped to SLO site and tested on a Dynamometer. Upon test, it was determined that the rear-
right motor was producing considerably lower torque than expected. While trying to determine if the

## Page 6

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  6 
motor or ESC were malfunctioning, we tested each with a stock Motor or ESC. Both performed normally. 
When we put them together, the original pair performed normally, and the problem was gone.  
Upon further investigation we found the problem with the soft-start circuit and managed to replicate this 
problem on stock ESC in house. When the soft-start circuit is malfunctioning, it reduces the force delivered 
by the motor . Thermal imaging indicated that one of the 4 parallel connected MOSFETs was shorted 
between Source and Drain. This would essentially bypass the current limiting due to disabled soft start 
feature and deliver normal current to the motor.  Over time this circuit gets damaged with one or more 
MOSFETs Q20-Q23 drain-source short.  While it does not provide soft -start function, the ESC delivers 
normally rated force.  
To prove this theory, we shorted the gate of soft -start circuit of a standard ESC and ran the test on 
Dynamometer. Test results were identical to what we saw with VXE545 motor -ESC pair; low force until 
throttle PWM=1500 and thereafter normal force. Upon ex amining the ESC, we found that same as the 
VXE545 ESC, one of the soft-start MOSFETs was shorted between Source and Drain.  
At this point we concluded that the issue with VXE545 was a faulty soft -start circuit limiting current to 
motor and delivering low force.  
 
3 Issue Status 
Investigation complete. See C/CAs 
 
4 Plan 
1. Investigation complete. See C/CAs 
 
5 Root Cause  
Soft-start circuit in the VXE545 position 3 VTOL ESC was permanently OFF (i.e.. MOSFETs Q20-Q23 Off). 
This was causing the motor to get less current and deliver lower f orce. With the Soft start function OFF,

## Page 7

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  7 
the bulk capacitors would be disconnected from the circuit . The  motor would operate, but with 
considerably lower force, as noticed by the customer. These components could have been defective from 
the manufacturer, or damaged from heat or transients.  
6 Investigation Overview 
 
6.1 Potential Cause: Software or Configuration issues. 
Field team did not find any software or configuration issues. This possibility was discarded. 
6.2 Potential Cause: User Error 
This possibility was also discarded based on the flight report submitted by the user. 
6.3 Potential Cause: Malfunction of Autopilot or electronics 
This possibility was also discarded because the aircraft checked out during the pre-flight checks.  
2. User Error 
 4. VTOL Motor 
issues 
6. VTOL Soft-
Start Circuit 
Soft-Start circuit 
issue 
Investigated but inconclusive. 
Not the root cause of contributing factor  
  Root cause or contributing factor. 
1. Configuration 
or software 
3. VTOL Autopilot 
or Electronics 
5. Manufacturing 
Defect 
X 
X 
X 
 ? 
X 
 
X 
? 


## Page 8

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  8 
6.4 Potential Cause: VTOL Motor issues 
Based on customer’s experience, it seemed that the Right- Rear motor was under -powered. This motor 
was returned to us. Motor -ESC were examined but did not show any external damage or smell of burnt 
electronics. Thereafter this Right rear (motor position 3) motor/ESC Assy from VXE -545 was run on a 
Dynamometer and compared against a standard stock motor ESC assembly.  
 
Assemblies Serial Numbers 
VXE-545 Motor-ESC C-S100345 
Stock Motor-ESC 018 
  
 VXE-545 Motor-ESC exhibited an unusual behavior in response to a throttle ramp profile that needed 
further examination. As can be seen, the motor delivered lower Force at low to moderate throttle.  
Dyno results and plots are shown below in Figures 1-3: 
  
 
Figure 1 VXE-545 Force compared to a standard motor

## Page 9

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  9 
 
Figure 2 VXE-545 Force compared to a standard motor 
 
Figure 3 VXE-545 Current draw compared to a standard motor 
6.4.1 VTOL Motor Issue- Motor-ESC History 
Incident Date/Time: 4/29/2024 1:57 PM 
VXE545 was involved in a total of 22 flights with 14.1 hours of flight time with the customer. During all 
these flights it used the same Left and Right Lift booms and lift motors, indicating there were no motor or 
ESC swaps and these motors performed as expected. As a matter of fact, other than the main and HLB 
batteries, no other component was swapped throughout the 14.1 -hour flight time over 22 flights. Both 
main and HLB batteries were used in previous successful flights.

## Page 10

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  10 
There was a take-off aborted on 4/23/2024, 6 days before the date of incident. This 4/23 flight was 
scheduled for a single flight of 0.67 hours but was immediately aborted. Flight was carrying HD55 payload 
that it had carried 4 times before. There is no indication why this flight was aborted. Flight log calls it the 
first mission which could mean it was being tested for mission on 4/29/2024. Log does not indicate any 
repairs. 
 
6.5  Potential Cause: Manufacturing Issue. 
Once it was determined that VXE-545 Motor-ESC combination was malfunctioning, we tried to isolate the 
problem between the motor and ESC. While separating the ESC from motor, the engineer noticed one of 
the phase wiring solder joints was covered by potting material. We suspected that this could have caused 
a bad solder joint.  
  
Figure 4 Figure 4 VXE-545 ESC 
When tested independently, the motor and ESC each produced expected throttle response behavior and 
did not exhibit the low power at low throttle behavior. The combination was re-assembled and re-tested 
running the same throttle sweeping profile as before. When compared to the original baseline, the pair 
worked normally, and we could not recreate the earlier issue. We suspected the solder contamination in 
one of the phases was causing the motor -ESC pair to malfunction and once the pair was put together 
again, it worked normally. To recreate the problem, we inserted 0.15Ω resistors in series with the 3 motor 
phases. The motor still performed normally. We have not been able to recreate the problem seen in the 
field or during our in itial test. Disconnecting one phase was also tried but when one phase was 
disconnected, the motor did not operate at all. 
After this effort we concluded that the issue was not caused by a bad solder joint to the phase.

## Page 11

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  11 
 
Figure 5  Comparing reassembled VXE-545 to stock motor 
 
Figure 6  Current state of VXE-545 Motor-ESC 
6.5.1 Defective Motor MOSFET Check 
To eliminate a possibility of a defective MOSFET  device or connection  we removed MOSFETs from Low 
and High sides. ESCs uses set of 3 MOSFETs in parallel in Hi-side and Low-Side. We ran two tests, one with 
one Hi-Side MOSFET removed and another with one Low-Side MOSFET removed. Neither of these two 
test results resembled the results we saw earlier.

## Page 12

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  12 
 
Figure 7 ESC-Motor performance with one Low-Side MOSFET removed. 
Figure 7 depicts the stock ESC performance with one low-side MOSFET removed. 
As can be seen, for a short run, the motor performs well with 2 out of 3 MOSFETs driving a phase. 
 
The above chart depicts ESC-Motor performance when one of the three Hi-Side MOSFET was removed. 
The above tests were performed to eliminate the possibility that the strange behavior displayed by VXE-
545 motor-ESC at customer site and earlier tests at the factory were caused by a defective MOSFET in 
ESC. 
-2
0
2
4
6
8
10
12
14
0
5
10
15
20
25
30
35
40
1200 1250 1300 1350 1400 1450 1500 1550 1600 1650
1 Low-Side MOSFET removed (S# 082)
Powertrain 1 - current (A) Powertrain 1 - force Fz (thrust) (kgf)
Powertrain 1 - torque MZ (torque) (N⋅m)
-2
0
2
4
6
8
10
12
14
0
5
10
15
20
25
30
35
40
1200 1250 1300 1350 1400 1450 1500 1550 1600 1650
1-Hi-Side MOSFET removed
Powertrain 1 - current (A) Powertrain 1 - force Fz (thrust) (kgf)
Powertrain 1 - torque MZ (torque) (N⋅m)Figure 8 ESC-Motor performance with one Hi-Side MOSFET removed.

## Page 13

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  13 
6.6 VTOL Soft-Start circuit issue 
While probing the ESC we found that the soft-start circuit MOSFETs were shorted.  
 
Figure 9 Soft-start Circuit 
Upon further investigation, we found that Q20 was shorted. ( Thermal camera image showed that Q20 
heated up when a small voltage was applied between the Drain-Capacitor node and Ground.) This would 
explain the loss of force because of phase MOSFETs being starved of current.  
As can be seen from figure 9 above, if resistors R40 or R41 did not make proper connection, capacitor C12 
would not charge up to turn the MOSFETs Q20-Q23 ON. With Q20-Q23 Off, they will be subjected to the 
full range of back EMF spikes. As the motor ramps up, these spikes would be sufficient to damage the 
weakest of 4 MOSFETs creating a path to ground . This would explain the motor  generating low force 
initially and at certain speed when ESC blows the MOSFET, the motor starts generating normal level force. 
We also noticed that the Soft-start circuit was permanently remaining Off, i.e. the MOSFET gate voltage 
was 0V. This would cause MOSFETs Q20-23 to remain OFF. Without the protection of Capacitors C9 and 
C10, voltage spikes from Motor back EMF destroyed the Soft -start MOSFETs shorting their Source and 
Drain. To verify this finding, we took a stock ESC and shorted the gate node with a 100 Ω resistor to ground 
and ran the ramp test. The ramp test replicated the fault we had noticed  earlier. For PWM<1500 the 
motor delivered lowered force, at PWM=1500, the force shot up. See the result below: 
Shorted to Ground 
104 Ωs to 
Ground

## Page 14

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  14 
 
Figure 10 Motor Operation with Soft-start circuit disabled. 
Capacitors C9 and C10 provide energy to the motor  and reduce ripple to the FETs . W h e n  t h e  E S C  i s  
operated with Soft-start circuit disabled, MOSFETs Q20-Q23 is subjected to the excessive back EMF from 
the motor and get destroyed (Source-Drain short). This places the soft-start circuit in permanent disabled 
mode. Thermal camera check showed that 3 of Q20-Q23 MOSFETs were damaged.  
With the Soft-start circuit disabled (i.e. MOSFETs Source-Drain shorted), the motor performed normally 
as shown in the result below. It should be noticed that with the Soft-start circuit disabled, the ESC will not 
have anti-spark protection when it is being plugged in. 
 
Figure 11 Motor Operation after Soft-start circuit damaged 
This observation is consistent with what we saw in the case of VXE-545 position 3 Motor-ESC and confirms 
our assertion that the issue was caused because of damaged Soft-start circuit.  
-2
0
2
4
6
8
10
12
14
0
5
10
15
20
25
30
35
40
1200 1250 1300 1350 1400 1450 1500 1550 1600 1650
ESC SN-082  Soft-Start circuit disabled
Powertrain 1 - current (A) Powertrain 1 - force Fz (thrust) (kgf)
Powertrain 1 - torque MZ (torque) (N⋅m)
-2
0
2
4
6
8
10
12
14
0
5
10
15
20
25
30
35
40
1200 1250 1300 1350 1400 1450 1500 1550 1600 1650
ESC SN-082 Soft-Start MOSFET shorted
Powertrain 1 - current (A) Powertrain 1 - force Fz (thrust) (kgf)
Powertrain 1 - torque MZ (torque) (N⋅m)

## Page 15

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  15 
7 Corrective Actions and Recommendations 
7.1 Include a motor fault flag during the LW spin up test that triggers if the VTOL 
controller detects current anomaly.  
In this case, comparing the ibatt1/ibatt 2 current with the expected current and flagging a fault if less 
than expected current is observed would detect this problem.  The software may also have to be 
changed to prevent an operator from running two motors at once during launch wizard.  
7.2 Remove or bypass soft start circuit from VTOL ESCs.  
Since the current assembly procedure requires connecting the anti-spark connections last, the soft start 
circuit in the ESCs is no longer required. Bypassing it would make the ESCs more reliable.  
7.3 Corrective Recommendations:  
Below are a few recommendations, while not directly related to this issue, they can prevent failures in 
future: 
7.3.1 Improve wire routing and support of VTOL ESCs.  
 
Motor uses 10 AWG  phase wires. These wires enter the side of ESC case and bend at 0.5” radius to be 
soldered to the ESC board. This is a stranded conductor 0.15” thick. Per IPC/WHMA-A-620, the minimum 
bend radius should be 0.9”. Such a short radius on heavy gauge wiring induces considerable stress on the 
solder joint holding the wire to the ESC board. It is recommended we allow more space for the wires to 
bend at a larger bend radius. Additionally, we should provide some form of stress relief to the phase wiring 
inside the ESC housing. This could be used to hold the wires and reduce the stress on the solder joints. A 
temporary fix would be to solder the phase wires as shown below to achieve 0.9” bend radius.

## Page 16

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  16 
 
Figure 12 Suggested Solder position 
7.3.2 Increase air flow to VTOL ESC heat sinks  
Mount the ESC on the top side of the boom. Presently the ESC is mounted on the bottom side of the 
boom where the heat sink is facing away from the airflow.  
7.3.3 Add temperature sensor to VTOL ESCs. Abort launch at limits.  
Incorporate a temperature sensor in the ESC and have software access to abort a launch in case of 
excessive temperature rise.  
8 Implication to the Aircraft 
This fault was localized to position 3 ESC. Lift ESCs are powered by the HLB while the aircraft is powered 
by the main battery. Electronics in the aircraft are optically isolated from the ESC so there is little 
possibility that this fault could have caused any damage to the rest of the aircraft circuitry. Based on this 
investigation, we can confirm that once the ESC position 3 is replaced, the aircraft will be flight-worthy. 
See the details in the diagram below:

## Page 17

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  17 
 
9 Conclusion 
The issue was caused by malfunctioning of Soft -start circuit starving the motor from current, and thus 
delivering low Force.

## Page 18

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  18 
10  Appendix 1 Motor Total Harmonic Distortion Test 
Additionally, the VXE -54 5Motor was assessed  on a separate test platform that excites the motor using 
pure sine wave of varying frequency and extracts motor’s Total Harmonic Distortion (THD) and phase 
imbalance that may be caused by mismatching magnetic properties of its stator. (20% variation in 
magnetic properties of various pole materials  is common among motors.)  Below are the results  of this 
test: 
10.1 VXE545 Motor 
Below is the map of Total Harmonic Distortion for the VXE545 motor. The phase imbalance was about 
0.5V. Highest level of distortion was observed at about 2K-3K Hz and is deemed normal. 
 
Figure 13 VXE545 Motor THD 
10.2 Stock Motor 
A stock motor was excited under the same setup and displayed similar results but slightly higher THD. This 
higher THD was attributed to motor being EOL. The phase imbalance was like the VXE545 motor.

## Page 19

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  19 
 
Figure 14 Stock Motor THD 
 
10.3 Overlaid Comparison.  
Below is the graph of two results superimposed on one another. As can be seen, there is slight difference 
in THD. VXE545 motor seems to have its highest level of THD at about 1KHz while the stock motor seems 
to have peak THD between 2-3KHz; however, the amount of THD and phase imbalance look like what it 
expected within acceptable range for our aircrafts.  
These tests further demonstrate that VXE545 motor is in normal operating conditions.

## Page 20

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  20 
 
Figure 15 VXE545 and Stock Motor THD Side-by-side. 
11  Appendix 3 Motor 3 low Force investigation 
Before the motor-ESC were returned to SLO site and we had opportunity to test them on Dynamometer , 
we had done some analysis on possible software issues. Following section details the analysis to locate a 
possible software issue: 
11.1 Summary 
 
 
Figure 16 Right rear thrust command at or near maximum.

## Page 21

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  21 
  
Figure 17 Uncommented pitch/roll excursion. 
  
Figure 18 Abort commanded after position excursion.

## Page 22

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  22 
  
Figure 19 Abort commanded after position excursion. 
 
11.2 Current Measurement 
• ibatt1 
o Current sensor signal from "left side" lift system load, amps. Filtered values from 
the analog handler. 
• ibatt2 
o Current sensor signal from "right side" lift system load, amps. Filtered values from the 
analog handler. 
 
The left side is drawing less current, which is consistent with left side not commanding as much throttle.

## Page 23

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  23 
 
 
Figure 20 Current Measurement 
Reference flight, similar magnitude of current draw. Y-axis is amps. 
 
 
Figure 21 Comparison of Current draw. 
  
Figure 22 Current Draw 
 
Figure 23 Throttle comparison.

## Page 24

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  24 
  
Figure 24 Current, Throttle values, measured and calculated

## Page 25

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  25 
  
Figure 25 Comparison Contd.

## Page 26

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  26 
  
Figure 26 Current measurement-During Rotor test

## Page 27

Investigation Summary: VXE-545  
 
[9/20/2024] Edge Autonomy Proprietary Information  27 
  
Figure 27 Current Measurement during Reference flight
