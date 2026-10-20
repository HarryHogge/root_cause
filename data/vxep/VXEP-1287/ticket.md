# VXEP-1287: B30 757 LEMB SOC SN 009 fluctuation during flight

- **Issue type:** Problem
- **Status:** New
- **Priority:** Medium
- **Created:** 2025-05-16
- **Updated:** 2025-10-06
- **Reporter:** Cameron Chapman
- **Assignee:** Stephen Peters
- **Creator:** Cameron Chapman
- **Links:** clones VXEP-1286 (B30 ??? LEMB chargers not charging to full )
- **Plan:** - Compare accuracy to system and flight requirements . @Ryan Christino ? AAR AAR_V757_20250516T172411Z.zip

## Description

using 6.5 software? And OGCS? See images in comment. 
SN 009 LEMB. B30 757 aircraft

- SOC Inaccuracy - Software has battery coefficients applied in reverse order leading to a large decrease in SOC at the beginning and a large / quick drop in SOC at the end.

[embedded: image-20250519-135520.png]
Coefficients should be applied in order from 100% SOC to 0% SOC.
Correct:
Interp_Table =  [ 1 3 4 0 -3 -3 -4 -5 -5 -5 -5 -5 -7 -9 -10 -10 -9 -8 -6 -3 0 ] ;
Incorrect:
Interp_Table_Switched =  [ 0 -3 -6 -8 -9 -10 -10 -9 -7 -5 -5 -5 -5 -5 -4 -3 -3 0 4 3 1 ] ;

- SOC Variation - I suspect the SOC values jump around largely as a result of variation in the current measurement. The larger term that dominates the noise is the current measurements which then get multiplied by the ESR values.

[embedded: image-20250519-144100.png]

Need to confirm what temperature is being used for the ESR lookup to provide the plot determining, which is noisier, the current or the ESR value. 


- SOC Drop During Initial Battery Sag -
- Higher Throttle Values - TBD on Summary

[embedded: image-20250519-145136.png]


- Flight Endurance -

[embedded: image-20250516-212421.png]
Average Power Consumption Coming in at about 380W.

## Comments (1)

### Cameron Chapman, 2025-05-16

SN 009 LEMB
B30 757 aircraft 
[embedded: image-20250516-171924.png]
[embedded: image-20250516-171930.png]

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20250516-171924.png | image | 4741 | 2025-05-16 | listed only |
| image-20250516-171930.png | image | 4717 | 2025-05-16 | listed only |
| image-20250516-212421.png | image | 61 | 2025-05-16 | listed only |
| image-20250519-135520.png | image | 59 | 2025-05-19 | listed only |
| image-20250519-144100.png | image | 53 | 2025-05-19 | listed only |
| image-20250519-145136.png | image | 57 | 2025-05-19 | listed only |
