# Vehicle Incident Report MOLSON VXE591.pdf

Attachment 25066, pdf, 1894 KB, added 2024-12-18 by Pat Wells.

## Page 1

Investigation Report
V591
Author: Cody Smisek
Dec 18, 2024

## Page 2

Summary
• Aircraft was operated in icing conditions (weather forecast/report provided by 
customer indicated freezing fog). Post incident photos show significant leading edge 
icing on horizontal stab and undetermined portion of wing. VTOL lift props appear to 
also have icing build up. Fuel cell operated as designed, outputting >450W throughout 
the flight (and 500W when in ‘emergency’ mode). Aircraft was in orbit for first 30mins 
averaging ~700W of power consumption resulting in a decrease of HLB SoC from 70% 
(after VTOL launch) to 50%. A climb was subsequently commanded to 800ft AGL, 
throttle initially increased to 100% but quickly decreased to ~60%, likely due to power 
limit implemented in AP code based on HLB SoC (to prevent using all power in a 
climb), thus aircraft did not climb as commanded. Flight was continued in attempt to 
charge battery, however energy consumption never decreased below fuel cell output, 
leading to glide landing at ELZ. 
Horizontal Stab Icing
Wing icing
Icing conditions

## Page 3

AVG Power Consumption > 
max FC output for ~30 minutes

## Page 4

Initial 500ft orbit
Operator attempts to initiate climb to 800ft
Vehicle does not follow commanded climb, 
likely due to AP power limiting based on HLB 
SoC and current power for forward flight

## Page 5

apThr
AP initially commands max throttle 
after commanded climb to 800ft 
AGL but returns to ~.5. Power limit 
likely in effect due to SoC <60%.

## Page 6

HLB Fully charged & Fuel cell 
ramps down output. Followed by 
VTOL Launch, HLB discharge 
and FC ramp up to 450W
Fuel Cell increases to 500W 
(emergency mode)

## Page 7

Ground speed changes with yaw (heading), indicating 
winds aloft. Possible to deduce that apIAS is relatively 
accurate and pitot not obstructed by icing

## Page 8

GPS altitude and apALT track. Indicating 
no substantial static blockage from icing. 
(Offset due to difference in MSL and AGL)

## Page 9

Current published VXE30 Fuel Cell 
Supplement available on WebManuals is 
limited to recommendations during cruise.

## Page 10

Current published VXE30 Operations 
Manual available on WebManuals explicitly 
prohibits flight in icing conditions

## Page 11

User sending multiple start commands 
during preflight. Possibly related to 
misunderstanding of GCS indications.
