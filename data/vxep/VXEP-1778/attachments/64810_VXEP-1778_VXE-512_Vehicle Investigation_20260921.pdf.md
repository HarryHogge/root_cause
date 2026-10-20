# VXEP-1778_VXE-512_Vehicle Investigation_20260921.pdf

Attachment 64810, pdf, 576 KB, added 2026-09-22 by Drew Hildreth.

## Page 1

© 2026 Redwire. Proprietary, Not for Public Release.
Title: VXEP -1778 Investigation Report
Vehicle: VXE -512
11 May 2026

## Page 2

© 2026 Redwire. Proprietary, Not for Public Release.
Operator Statement
• Winds on ground were 6-7 kts and gusting up to 13. AV VTOL climbed to 300ft AGL then 
transitioned to horizontal flight where it climbed to 400ft and reached wp1. AV then initiated a 
right hand turn towards the mission loiter, after turning roughly 90° AV rapidly descended an 
estimated 200ft while still initiating a right hand turn. At this time the AV operator lost 
connection with the aircraft. AV operator commanded RTB in an attempt to recover the 
aircraft safely. AV continued to descend until it collided the ground.

## Page 3

© 2026 Redwire. Proprietary, Not for Public Release.
Executive Summary
Problem Statement
VXE-512 unexpectedly lost power after transitioning from VTOL to Fixed Wing flight causing aircraft to 
crash.
Sequence of Events per Engineering
• Firmware logs were reviewed and Avionics box was inspected for irregularities. None found.
• Motors were run to reproduce failures in the lab and in SCO were unsuccessful. Failure not 
reproducible.
Ruled out Leading Causes
• Forward motor failures
• Visual inspection of avionics showed no signs of irregularities.
Root Cause 
Root cause was not conclusively established. However, improper mating of the main battery remains 
the likely culprit.
Corrective Actions
Relaying to customers to report main battery serial numbers and date of manufacturing.

## Page 4

© 2026 Redwire. Proprietary, Not for Public Release.
Fishbone Investigation
Aircraft lost power 
transitioning from VTOL to 
Forward Motor
Investigated but inconclusive
Not the root cause or contributing 
factor
Root cause or contributing factor
Legend
Battery
Imbalanced cells 
could cause failure
XCOMM 
microcontroller
can disable 
power to VTOL  
Impedance measures 
~6.0Ω - normal
No loose connections 
in nose
Power and return 
path have normal 
continuity
HarnessFirmware
Mating
Improper mating from 
battery
Forward Motor was
Run at full throttle – no 
failures
Avionics Box
Hardware
Aircraft was left on 
All weekend -  no resets
Avionics Box 
Visual Inspection 
– No irregularities

## Page 5

© 2026 Redwire. Proprietary, Not for Public Release.
1.0 – Executive Summary
On March 15, VXE 512 went through standard pre-flight checks for roughly 29 minutes before vertical 
ascension was initiated.  After reaching an altitude of 300 ft, the aircraft transitioned from VTOL to Fixed 
Wing motors.  Six seconds later, XCOMM and VTOL abruptly lost power causing a crash.
-50
0
50
100
150
200
250
-50
0
50
100
150
200
250
300
350
1730 1735 1740 1745 1750 1755 1760 1765 1770 1775 1780
HLB Current (A)
Altitude (ft)
HLB Current vs Altitude
baroalt IBatt
-10
0
10
20
30
40
50
60
-50
0
50
100
150
200
250
300
350
1730 1735 1740 1745 1750 1755 1760 1765 1770 1775 1780
MB Current (A)
Altitude (ft)
MB Current vs Altitude
baroalt SysIb

## Page 6

© 2026 Redwire. Proprietary, Not for Public Release.
2.0– Observations
SUAV
Suav firmware version is 6.3.4 while the GCS version on the aircraft is 6.6.1.
Avionics Box
Avionics box was tested on B30 bench assembly with no immediate failures (except for those noted in ‘Irregularities’). 
The avionics was then opened and subjected to checkout procedure, upon which it passed. Visual inspection did not 
reveal any issues.

## Page 7

© 2026 Redwire. Proprietary, Not for Public Release.
2.1– Irregularities
HLB
The HLB mating connector’s anti-spark resistor – which should measure 6.0 Ω – measures an open-
circuit.  This could theoretically impact the main power bus which is shared through ground through the 
HLB data connection.  
Checksums
During initial intake, the operator reported an autopilot checksum of 0x3CFF via the GCS. However, 
subsequent bench testing of the avionics box on the iron bird verified the checksum as 0xFCDD, which is 
the expected and correct value. Given that the hardware checksum is verified correct, this discrepancy is 
unlikely to be the root cause.
Log Files
On July 2 and 7, the avionics box was turned on with the bench assembly with no issue.  On July 9, the 
XCOMM webpage would not load.  After 20 minutes of troubleshooting, the webpage loaded, but the log 
files webpage would not load.  Power cycling fixed the issue.  It’s unknown whether this was a test setup 
issue or a real error, however, none of the log files had an XCOMM processor reset.  This behavior did not 
manifest itself after this date.

## Page 8

© 2026 Redwire. Proprietary, Not for Public Release.
2.2– Aircraft Testing
Avionics box was re-installed on the aircraft, and the following tests were conducted.
Motor Test
Forward motor was induced to full throttle twice.  The first time, the aircraft was powered on and the 
forward motor pulled ~52A for two minutes with no resets or other issues.  The motor test was repeated 
after first powering on the aircraft and letting it idle for 30 minutes similar to the failed flight.  Forward 
motor again pulled ~52A with no incident.  Failure not reproducible.
Idle Test
Aircraft was powered on a Friday and sat idle over the weekend.  On Monday morning the logs were 
observed and no resets had occurred.

## Page 9

© 2026 Redwire. Proprietary, Not for Public Release.
Investigation Plan
3.0– Possible Root Causes
Results
Firmware/Microcontroller
As the diagram shows, if the microcontroller on the XCOMM were to fail or reset, this could shut the power down to 
the XCOMM, fixed wing and VTOL boards. If the microcontroller were to reset or outright fail, then the logs could 
show simultaneous and abrupt stop as they do.
However, there is no XCOMM Processor reset to indicate that a reset occurred due to the firmware.

## Page 10

© 2026 Redwire. Proprietary, Not for Public Release.
Investigation Plan
Internal Battery Failure
A short circuit or other internal hardware fault within the battery may have caused the complete power 
loss. Please ask the customer to inspect their batteries and identify any units that are no longer 
functioning.  Primary candidate for root cause
Main Battery Mating
Harness measured perfect continuity throughout length of cable. Additionally, anti-spark resistor 
measured a nominal 6.0Ω. However, if Main Battery AS150 connector was not seated properly, this 
could have caused the aircraft to lose power.  Primary candidate for root cause.
3.1– Possible Root Causes

## Page 11

© 2026 Redwire. Proprietary, Not for Public Release.
4.0– Conclusion
Aircraft VXE-512 had a sudden loss of power to both XCOMM and VTOL.  This failure was not reproducible 
with the aircraft in SLO.
Though there were intermittent yellow flags during testing – log files accessibility, checksums – these 
behaviors cannot be definitively tied to root cause.  Additionally, these behaviors have not re-manifested.
Loss of power could be due to any of these errors, in order of likelihood.
1. Improper Mating
2. Imbalanced Battery
3. Failure on XCOMM microcontroller
4. Firmware
