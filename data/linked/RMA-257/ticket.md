# RMA-257: D4500252 240606  (439 Incident)

- **Issue type:** Fuel Cell
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-06-06
- **Updated:** 2024-07-02
- **Resolved:** 2024-07-02
- **Reporter:** Sean Odell
- **Assignee:** Sean Odell
- **Creator:** Sean Odell
- **Links:** relates to VXEP-306 (VXE 439 Fuel cell not reaching adequate power in flight)
- **Customer:** PMA263
- **Part Number(s):** D450XR
- **Vehicle Tail Number:** SN D4500252
- **Root Cause:** Main Control board failure
- **RMA Number:** 240606
- **Serial Number:** 0252
- **Received Date:** 2024-06-07

## Description

VXE 439 aircraft using a Fuel cell not reaching adequate power in flight.
Evaluate and potentially rework/repair depending on findings.

Edge RMA
POC:
Address:

## Comments (13)

### Sean Odell, 2024-06-06

@Sean Wendling The RMA you can use for this fuel cell is the following: 240606
@Pat Wells FYI

### Sean Odell, 2024-06-07

Tracking for shipment from customer to Edge Ann Arbor. 721133678175

@Sean Wendling @Robert Redfield @Pat Wells FYI

### Pat Wells, 2024-06-07

@Sean Wendling this is the fuel cell linked to ACFT 439 investigation.

### Pat Wells, 2024-06-11

@Sean Odell end user listed above is incorrect.

### Sean Odell, 2024-06-11

@Pat Wells It is not PMA263?  The aircraft it was involved with was.

### Pat Wells, 2024-06-11

@Sean Odell  you have 7th group listed above.

### Pat Wells, 2024-06-14

@Sean Odell has this been received? Shows as under evaluation on Share Point site.

### Sean Wendling, 2024-06-14

Hey All, this has been received in Ann Arbor. @Robert Redfield will be working the investigation and keeping Jira up to date.

### Robert Redfield, 2024-06-14

Fuel cell received on June 7 2024
No physical damage observed on unit.

### Robert Redfield, 2024-06-14

It was observed that the fuel cell would not power on.   No LED activity observed.
No signs of physical damage to control board. (deformation, electrical scorching, or otherwise)
Unable to pull cycle count/hours
Unable to extract calibration file

Root cause of the main control board failure indicates an electrical short of the 3.3vdc circuit.  Failure of this circuit will prevent the microcontroller of the circuit board to function.   There is also the potential that a failure/defect within the microcontroller could damage the 3.3vdc circuit.   It is unknown at this time which failure could have happened first.  (the chicken or egg scenario)
It should be mentioned that a complete control board failure mid operation could cause damage to the fuel cells within the stack due the system not being able to perform it’s cooldown operation successfully. 

Next steps will include a replacement of the control board, and a full calibration sweep of the anode assembly.  Once these are completed I can then perform in incoming QC to test the stack health.

### Robert Redfield, 2024-06-19

replaced main control board (PCA0120)  Performed full calibration sweep of Anode assembly. 
Performed incoming QC. 
Stack health is found to be good. (28.2vdc)
Next steps to include full reassembly of unit and an outgoing QC.

### Robert Redfield, 2024-06-25

System has passed all outgoing quality checks.

### Sean Odell, 2024-07-02

Fed Ex Tracking no.: 777147037513

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [D4500252 Incoming QC.txt](attachments/21052_D4500252%20Incoming%20QC.txt.md) | text | 1235 | 2024-06-19 | converted |
| [D4500252 Final QC.txt](attachments/21227_D4500252%20Final%20QC.txt.md) | text | 2077 | 2024-06-25 | converted |
| [D4500252 QC1.txt](attachments/21228_D4500252%20QC1.txt.md) | text | 1846 | 2024-06-25 | converted |
