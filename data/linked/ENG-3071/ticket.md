# ENG-3071: Aircraft 380 Launch Abort

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-09-25
- **Updated:** 2025-06-02
- **Resolved:** 2025-05-28
- **Reporter:** Daniel Lloyd
- **Assignee:** Carl Graf
- **Creator:** Daniel Lloyd
- **Labels:** FBI, lmco
- **Links:** relates to VXEP-102 (VXE-380 Launch abort)

## Description

During FBI training the customer reported a launch abort.
Vehicle ascended to commanded launch altitude, then began to decend without any command from RPIC. RPIC then selected Abort Launch within the Override Launch Control menu, and had control of the aircraft during its remaining descent.  RPIC nudged aircraft slightly left, before it landed safely.  HLB landed with 57% battery life. Nominal winds, 73 degrees F, sunny, approx. 11:50 AM CST.
The HLB was swapped and the aircraft relaunched without issue.

## Comments (1)

### Pat Wells, 2023-10-03

@Daniel Lloyd investigation complete. 
Root cause: Loss of GPS signal near transition altitude, system aborted launch per standard.
Final report slide deck attached.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V380_230921_115114_pack.zip | archive | 1650 | 2023-09-25 | listed only |
| [Vehicle Investigation Report VXEP-102.pptx](attachments/16830_Vehicle%20Investigation%20Report%20VXEP-102.pptx.md) | pptx | 4145 | 2023-10-03 | converted |
