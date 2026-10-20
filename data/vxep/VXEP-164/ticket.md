# VXEP-164: Hybrid Lift Batteries overweight

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-10-30
- **Updated:** 2024-02-28
- **Resolved:** 2024-02-28
- **Reporter:** Ben Norris
- **Assignee:** Greg Fryer
- **Creator:** Ben Norris
- **Links:** relates to VA-757 (Investigate Hybrid battery weight increase suspected due to potting compound change)
- **Issue color:** purple
- **Part Number(s):** 114-106085

## Description

Hybrid Lift Batteries 114-106085 are showing up as overweight >1475g. The specified weight range of the final assembly has not been reevaluated since changing potting compounds due to exclusion of ToughSeal products. The cables used in 114-106494 as well as the staking and sealing of cables to the lid in 114-106085 have all changed from ToughSeal and we need either a higher specified final weight or a tighter tolerance for the lower level assemblies. NCRs 1689 and 1767 both reference batteries being overweight and have required disposition.

Production HLB Data Spreadsheet: \\condor\Production\Battery Information\Battery Production Data List\VXE30 HL Battery Info\VXE30 HL Battery Datasheet - Self Discharge, High Stress.xlsx

## Comments (3)

### Emalee Johnson, 2023-10-30

@Kelly J Furlong @Desiray Johnston FYI
Hey @Ryan Christino , Hayden said you would be the best person to help us out with this issue.

### Ryan Christino, 2023-11-01

@Emalee Johnson ⁠ @Hayden Jeanor Disposition is added. Ben pointed me in the direction of the weight tracker and I made some plots. It looks like a solid combination of increased non built-up pack weight and the switch in potting compounds are the largest contributors to the weight growth. However, there also appears to be a small but gradual increase in the last 100 or so packs that have been built. I'd like to focus some effort on reducing weight by increasing the tolerances on the lower level assemblies before revaluating the higher specification. I'd recommend a real thorough weight analysis on a quantity of a few packs as a next step. @Emalee Johnson Would you be able to coordinate a weight analysis on a few packs? I can come up with some new weight limitations and try to quantify the expected difference between the potting compounds but I think going through the exercise is going to yield a bit of insight into the issue.
[embedded file]
[embedded file]
[embedded file]
[embedded file]

### Hayden Jeanor, 2023-11-02

Here's another metric that might be helpful 
- formula used to generate plot: =IF(AND((CO1-C1)>200, (CO1-C1)<400), (CO1-C1), #N/A)

[embedded file]
things to also consider. When did we shift to the all weather HLB, and when did we replace TS

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| RawPackWeightLotsofPacks.png | image | 44 | 2023-11-01 | listed only |
| RawPackWeightvsBatteryCount.png | image | 61 | 2023-11-01 | listed only |
| WeightvsBatteryCount.png | image | 61 | 2023-11-01 | listed only |
| WeightvsBatteryCountZoomed.png | image | 96 | 2023-11-01 | listed only |
| image-20231102-171357.png | image | 231 | 2023-11-02 | listed only |
