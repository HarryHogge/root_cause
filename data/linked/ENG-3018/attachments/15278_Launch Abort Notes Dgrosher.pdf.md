# Launch Abort Notes Dgrosher.pdf

Attachment 15278, pdf, 486 KB, added 2023-06-30 by David Grosher.

## Page 1

When CN0 drops below 40 the launch is aborted. 
This has been reported previously as most likely interference in the GPS L1 band in the area of 
operations, if the source of interference is on the ground in the area the expectation is that as the AV 
gains altitude it will become more exposed to the interference.  
Note: I have NOT processed all of the data, however the first 6 datasets that I looked at all have the 
same issue. 
Questions:
1. Can Edge get data from another location with one or more of these same tail numbers? This will 
help to identify whether or not the AV hardware or environmental conditions is the source of the 
problem. Data from v455 shows no impact to CN0 when flying (assume it is somewhere else, but 
location data was sanitized) 
2. Can we setup a rig with different receiver equipment to collect Cn0 (Signal to Noise Ratio for each 
Satellite) as a function of altitude at the range?  If this is an issue in the AOI then this could help to 
identify hardware configurations that might be more robust.  
T95_VT477_230628_182951 -
• [07:47:14.270 331.270] mc rtl trigger
T95_V477_230628_181715
• [07:34:45.793 1924.794] mc rtl trigger
T95_V474_230512_122640
[14:46:07.698 305.698] mc rtl trigger
Launch Abort
Friday, June 30, 2023 4:04 PM
   Analysis Page 1

## Page 2

T95_V451_230626_183041
• [07:47:59.219 1129.219] mc rtl trigger
T95_V450_230629_134433
• Same issue
• It appears that the XCOMM is masking the nsats with CN0 < 40
   Analysis Page 2

## Page 3

AARdata01
   Analysis Page 3
