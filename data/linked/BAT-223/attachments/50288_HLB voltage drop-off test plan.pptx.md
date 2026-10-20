# HLB voltage drop-off test plan.pptx

Attachment 50288, pptx, 2875 KB, added 2026-03-24 by Tom Westrich.

## Slide 1

VXE30 HLB Voltage Drop-Out Test Planning
1/30/2026

## Slide 2

Overview of Test Types
PROPRIETARY AND CONFIDENTIAL THE INFORMATION CONTAINED IN THIS DOCUMENT IS THE PROPERTY OF EDGE AUTONOMY. ANY REPRODUCTION IN PART OR AS A WHOLE WITHOUT THE WRITTEN PERMISSION OF EDGE AUTONOMY IS PROHIBITED.
Self-Discharge
Approximate Duration, 48hrs
Capacity
Approximate Duration, 2hrs
DCIR
Approximate Duration, 0.75hrs
BK Battery Tester Program File
BK Battery Tester Sequence File
VTOL Flight Discharge
Approximate Duration, 1hrs
Source: BatteryTester INI

## Slide 3

Self-Discharge Test
PROPRIETARY AND CONFIDENTIAL THE INFORMATION CONTAINED IN THIS DOCUMENT IS THE PROPERTY OF EDGE AUTONOMY. ANY REPRODUCTION IN PART OR AS A WHOLE WITHOUT THE WRITTEN PERMISSION OF EDGE AUTONOMY IS PROHIBITED.
This test helps to detect things like dendrite formation but is not helpful for HLB Voltage Drop-Out Issue

Charge to Full
Record Cell Voltages & Time at which DUT’s enter Storage
Store in Temperature Controlled Environment (20-25°C) for 48hrs
Record Cell Voltages & Time at which DUT’s exit Storage
[picture]

## Slide 4

Capacity Test
PROPRIETARY AND CONFIDENTIAL THE INFORMATION CONTAINED IN THIS DOCUMENT IS THE PROPERTY OF EDGE AUTONOMY. ANY REPRODUCTION IN PART OR AS A WHOLE WITHOUT THE WRITTEN PERMISSION OF EDGE AUTONOMY IS PROHIBITED.
Voltage Drop Out is Primarily a Concentration caused Phenomenon (Electrolyte Loss)
Capacity Test is Better for SOH, Fresh but Dried Electrolyte Battery may Appear Healthy until Discharge Rates Increase
Acquiring Data would Help to Correlate HLB Lifetime Expectation (and DCIR -> Capacity Relationship); Would Help Justify Keeping Partially Used HLBs in the Field if they Pass DCIR or Flight Discharge

Charge to Full
Let Battery Cool to >20°C  and <30°C if Heated During Charge
Record Cell Voltages
Discharge Battery at 1C until 1st Cell Reaches 3.0V or the Pack Reaches 21V 
Let Battery Cool to <40°C if Heated During Discharge
Record Cell Voltages, Test Capacity, Test Energy
[picture]
Example Data for B40 HLB at C/3 CC Discharge

## Slide 5

DCIR
PROPRIETARY AND CONFIDENTIAL THE INFORMATION CONTAINED IN THIS DOCUMENT IS THE PROPERTY OF EDGE AUTONOMY. ANY REPRODUCTION IN PART OR AS A WHOLE WITHOUT THE WRITTEN PERMISSION OF EDGE AUTONOMY IS PROHIBITED.
Best Value & Effectiveness for Voltage Drop-Out Detection
 
Charge Storage Voltage
Let Battery Cool to >20°C  and <30°C if Elevated
Execute 3, 24C Pulses
Let Battery Cool to <40°C if Heated During Discharge
Record Cell Voltages, Test Capacity, Test Energy, DCIR Measurements
Repeat for 6C & 12C* Pulse Substitutions 
Lower Pulse Rate, Lower Thermal Build Up, Lower Noise, Cheaper Instruments, Faster Test
* 6C allows for 1.5W BK, 12C 3kW BK, 24C requires 6kW BK. It would be Ideal if we could validate DCIR is primary method – less time and equipment.
[picture]
[chart]
3min Rest
20s Pulse

## Slide 6

VTOL Discharge Test
PROPRIETARY AND CONFIDENTIAL THE INFORMATION CONTAINED IN THIS DOCUMENT IS THE PROPERTY OF EDGE AUTONOMY. ANY REPRODUCTION IN PART OR AS A WHOLE WITHOUT THE WRITTEN PERMISSION OF EDGE AUTONOMY IS PROHIBITED.
Best Indicator of Issue
Highest Discharge Rate, Most Representative Test, Most Data to Compare

Charge to Full
Let Battery Cool to >20°C  and <30°C if Heated During Charge
Get OCV Voltages by Resting at 0W for 5s
VTO Discharge at 4000W for 35s
Rest at 0W for 250s
VTL Discharge at 2500W until Pack Voltage <22.0 or any Cell <3.0V
Let Battery Cool to <40°C if Heated During Discharge
Record Cell Voltages, Test Capacity, Test Energy, DCIR Measurements
[picture]
Example Data from Production SCO
[picture]

## Slide 7

Recommendation
PROPRIETARY AND CONFIDENTIAL THE INFORMATION CONTAINED IN THIS DOCUMENT IS THE PROPERTY OF EDGE AUTONOMY. ANY REPRODUCTION IN PART OR AS A WHOLE WITHOUT THE WRITTEN PERMISSION OF EDGE AUTONOMY IS PROHIBITED.
MVP 
DCIR and VTOL Discharge Test
Down-Select Fielded Application
Only DCIR or Only VTOL Discharge Test
If Possible:
Static Capacity, DCIR and VTOL Discharge Test
Down-Select Fielded Application
Only DCIR or Only VTOL Discharge Test
Capacity Based State of Health Comparison
Backup Down-Selection and User Instructions Post-Test
Verify 50 Cycle Lifetime

## Slide 8

(no text)
