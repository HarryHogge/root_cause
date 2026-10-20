# VXEP-1016: Failure Mode Tests of LEMB Connectors

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2025-02-14
- **Updated:** 2025-05-20
- **Resolved:** 2025-05-20
- **Reporter:** Hayden Jeanor
- **Assignee:** Dylan Peters
- **Creator:** Hayden Jeanor
- **Parent:** VXEP-1003 LEMB Test Plan and Execution
- **Epic Link:** VXEP-1003

## Description

Plug in connections the wrong way using proposed pinout designs to ensure no failures: LEMB pinouts.xlsx
- [embedded image-20250311-165822.png]
- [embedded image-20250311-165837.png]
- [embedded image-20250214-204601.png]

## Issue Status

Failure mode 2 re-created (see details below). Need to re-created failure modes 1 and 3 once assets become available (NDAA charger for 1 and LEMB BMS for mode 3)

## Comments (8)

### Hayden Jeanor, 2025-02-14

@Adrian Garcia please document effect of scenario 1

### Adrian Garcia, 2025-02-17

@Hayden Jeanor is this ticket good to close now?

### Hayden Jeanor, 2025-02-17

Copy and pasted from Issue Status field: 

 To safely replicate scenario 1 I removed BP1 (the white lead of the connector) from the housing. The first image shows that cell reads when BP1 is not connected. It shows cell 0 to have 2.02V and cell 1 to be 4.15V with the rest at ~3.1V. When putting the charger in charge mode an error appears and does not allow charging as shown in photo 2. 
In short, by not connecting BP1, the charger will not charge the battery, thus the proposed pinout should work.  
[embedded image-20250214-231114.png]
Cell voltages when BP1 disconnected 
[embedded image-20250214-231218.png]
Charging attempt when BP1 is not connected

### Hayden Jeanor, 2025-02-17

@Adrian Garcia see new issue status

### Hayden Jeanor, 2025-03-07

@Adrian Garcia please see updates to pinout. please re-test i charger will not function if BP1 and BP0 are swapped

### Adrian Garcia, 2025-03-07

@Hayden Jeanor I swapped BP1 (white wire) and BP0 (grey wire)

[embedded image-20250307-191452.png]
and here are the results of that: 
[embedded image-20250307-191514.png]
[embedded image-20250307-191524.png]

### Hayden Jeanor, 2025-03-11

@Dylan Peters @Stephen Peters please create scenario 1’s failure mode to ensure no catastrophic failures and that the NDAA charger wont function

### Dylan Peters, 2025-05-20

Due to the wiring of the LEMB, the cells connected to the header on the charge board changed. We have accepted the risk and recognized these are for LEMB only

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20250214-204601.png | image | 27 | 2025-02-14 | listed only |
| image-20250214-231114 (fa545db4-9bfb-47ac-9a76-00fc9a086cbf).png | image | 826 | 2025-02-17 | listed only |
| image-20250214-231218 (322fe446-12f4-4ea4-b4f4-23a2be32e387).png | image | 11387 | 2025-02-17 | listed only |
| image-20250307-191452.png | image | 3734 | 2025-03-07 | listed only |
| image-20250307-191514.png | image | 744 | 2025-03-07 | listed only |
| image-20250307-191524.png | image | 10627 | 2025-03-07 | listed only |
| image-20250311-165822.png | image | 21 | 2025-03-11 | listed only |
| image-20250311-165837.png | image | 13 | 2025-03-11 | listed only |
