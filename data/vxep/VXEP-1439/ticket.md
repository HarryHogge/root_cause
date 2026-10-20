# VXEP-1439: Evaluate B40 batteries optimized for 55lb MGTOW

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-07-21
- **Updated:** 2025-07-28
- **Resolved:** 2025-07-25
- **Reporter:** Cameron Chapman
- **Assignee:** Stephen Peters
- **Creator:** Cameron Chapman
- **Parent:** VXEP-1437 Evaluate B40 configuration optimized for 55lb (B30 successor)
- **Epic Status:** To Do
- **Epic Color:** ghx-label-14
- **Issue color:** dark_orange
- **Plan:** Will continue to refine as needed @Cameron Chapman
- **Issue Status:** First draft estimates uploaded

## Description

Evaluate HLB mass deltasEvaluate MB massEvaluate mixed chem. mass
### HLB Configs. and Mass Deltas

Assumptions:
- ME and EE designs/system remain same as SB35/40 HLB
- Battery mass is primary mass delta driver
- Mass savings in mixed chem. concept only applicable to battery only configuration, FC config. needs larger (3.85Ah) HLB design

| HLB Related HB5 Mass Deltas: 65lbs → 55lbs MGTOW |
| Configuration | Performance | Masses (Assuming No HW Changes) | Development Scope |
| MGTOW | Series | Parallel | Ah | Wh | Cell Mass | Battery Mass | HB5 Mass Delta | Time →ConDR | Time →PDR | Time →CDR | Est. Scope | Notes |
| 49lbs | 7 | 2 | 3.3Ah | 171Wh | 77g | 1078g | - | - | - | - | - | Baseline |
| 55lbs | 16 | 1 | 3.3Ah | 196Wh | 77g | 1235g | -0.73lbs | 0 | 2 | 2 | ~3months | Some ME&EE |
| 55lbs | 14 | 1 | 3.9Ah | 199Wh | 89g | 1246g | -0.71lbs | 0 | 1 | 2 | <3months | Limited ME |
| 65lbs | 14 | 1 | 4.4Ah | 228Wh | 112g | 1568g | - | - | - | - | - | Baseline |
| Mixed Chem. Concept | 14 | 1 | 1.2Ah | 60Wh | 26g | 364g | -2.12lbs* | 3 | 3 | 2 | 6-9months | Full Dev. Cycle |
| 14 | 1 | 2.2Ah | 114Wh | 52g | 728g | -1.48lbs* |
| *Requires HW changes (both ME & EE), tracking 80% of battery only mass delta. 1.2Ah cell in mixed chem. is not expected as to be a feasible solution. |

### Main Battery Configs. and Mass Deltas

Assumptions:
- ME and EE designs/system remain same as SB35/40 HLB
- Battery mass is primary mass delta driver (14S1P module mass = battery mass + cell expansion/contraction ME design + module sense HW = 1440g + Xg = Yg, X/Y < 0.1)
- 500-620W Nominal Cruise, 4hr Endurance

| Energy Budget |
| 10min 2000W | 333Wh |
| 4hr 500W | 2000Wh |
| 4hr 620W | 2480Wh |
| Total @ 500W | 2333Wh |
| Total @ 620W | 2813Wh |
| MB Configuration |
| 14S1P | 552Wh |
| Config. @ 500W | 14S4P |
| Config. @ 620W | 14S5P |
| MB Mass, 500W | +/-0.0lbs | 16.5lbs |
| MB Mass, 620W | +3.45lbs | 20.0lbs |

## Comments (0)

## Attachments (0)
