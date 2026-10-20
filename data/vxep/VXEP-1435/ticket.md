# VXEP-1435: VXE-674 Second Hard Landing

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-07-18
- **Updated:** 2026-06-30
- **Resolved:** 2026-06-30
- **Reporter:** Jackson Riley Curvin
- **Assignee:** Stephen Peters
- **Creator:** Jackson Riley Curvin
- **Labels:** Edge_Asset, GS_Closed, HLB_bad_cell, Weekly-incident-tracker
- **Links:** relates to VXEP-1413 (HLB Issues 4139, 3908, and 3867); relates to VXEP-1407 (VXE 801 Hard landings after Aborts); relates to VXEP-1398 (VXE-808 Aborted launch cell balance ); Linked issue cannot finish until this issue finishes. VXEP-1449 (Systemic Hybrid lift battery unexplained cell failures in flight); relates to VXEP-1485 (VXE-499 Hard Landing/ HLB Cell Drop Out)
- **Vehicle Tail Number:** VXE-674
- **Vehicle Configuration:** VXE-30, Battery Configuration
- **Corrective Action:** Do not use HLB and added to master ticket.
- **Problem Type:** Other (explain in description)
- **Root Cause:** HLB cell drop out.
- **Severity:** 1 - Flight Critical
- **Components (EA Aircraft):** Aircraft, full assembly

## Description

Aircraft aborted for second day in a row not landing as hard as the previous flight yesterday.

## Comments (11)

### Jackson Riley Curvin, 2025-07-18

Battery Serial Number: 2-3748
DOM:240722
Cycle Count:22

### Jackson Riley Curvin, 2025-07-18

[embedded: image-20250718-194248.png]

### Jackson Riley Curvin, 2025-07-18

[embedded: image-20250718-194436.png]

### Pat Wells, 2025-07-18

@Cameron Chapman another suspected issue with battery on take off.

### David Grosher, 2025-07-18

@Jackson Riley Curvin I made a request on the other 674 task for data from previous flights. Please look for that data as well with respect to this battery serial number and any other battery that has experienced issues.

### Jackson Riley Curvin, 2025-07-18

@David Grosher I'm working to get the other AARs now

### Jackson Riley Curvin, 2025-07-18

T95_V674_250715_134057_pack.zip
[embedded: image-20250718-203239.png]

### Jackson Riley Curvin, 2025-07-18

T95_V674_250630_115454_pack.zip
[embedded: image-20250718-203546.png]

### Jackson Riley Curvin, 2025-07-18

@David Grosher  here are the two previous flights on this GCS using this battery

### David Grosher, 2025-07-18

@Cameron Chapman @Stephen Peters @Jackson Riley Curvin It looks like cell 6 can been seen sagging on a previous flight prior to the observed failure in this incident. One caveat though is that it can only be seen in one of the two previous flights, and it appears to not be the most recent. I think we should try and secure prior data on the FLOPS failures to see if it is something we could detect reliably. If so, this could be an effective containment.

### Jackson Riley Curvin, 2026-06-30

Added to master ticket quarantined the HLB.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V674_250718_105742_pack.zip | archive | 1442 | 2025-07-18 | listed only |
| image-20250718-194248.png | image | 8008 | 2025-07-18 | listed only |
| image-20250718-194436.png | image | 38 | 2025-07-18 | listed only |
| image-20250718-203239.png | image | 24 | 2025-07-18 | listed only |
| image-20250718-203546.png | image | 29 | 2025-07-18 | listed only |
