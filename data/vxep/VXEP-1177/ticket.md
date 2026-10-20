# VXEP-1177: VXE 808 State of Charge discrepancy

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-03-26
- **Updated:** 2025-05-20
- **Resolved:** 2025-05-20
- **Reporter:** Drew Hildreth
- **Assignee:** Drew Hildreth
- **Creator:** Drew Hildreth
- **Labels:** Edge_Asset, Weekly-incident-tracker
- **Links:** relates to VXEP-1136 (VXE 557 Inaccurate SoC Model Causing Battery State to Fluctuate (OCT 12th Incident) ); relates to VXEP-762 (Check if VXE30 checker SOC is accurate for Main Batteries (I suspect no). Update manuals and charger+checker firmware to instruct not to use this feature and remove it if so.  )
- **Vehicle Tail Number:** VXE-808
- **Corrective Action:** Update Manuals and charger checker firmware to instruct not to use this feature.
- **Problem Type:** Discovered Issue
- **Plan:** See 4/29 meeting notes. Update cust documents to use new charger, not reference SOC on current equipment.
- **Incident Type:** Near Miss
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

AAR from 3/26/25 flyoff flights. On the first flight we landed with a main battery reading of 42-44% on the flight software. When we pulled the battery and plugged it into a battery charger post flight, the charger had an initial reading of 9%.

## Issue Status

on 04/01/2025 we plugged in a HLB to the main battery harness and as we were moving it around it arched against the side of the aircraft upon inspecting the harness we noticed a small cut in the wire. I belive that this could have caused the state of charge discrepancy. Photos are attached.

## Comments (3)

### Jackson Riley Curvin, 2025-04-02

@Cameron Chapman  when you get a chance could you please look at this and see if I'm on the right path?

### Cameron Chapman, 2025-04-16

@Jackson Riley Curvin sorry for the delay.  Good work. 
Checkout, share, improve, etc this page for our typical investigation process. https://jenaero.atlassian.net/wiki/spaces/EF/pages/23363854/Incident+Troubleshooting+and+Resolution+Tracking. FYI @Pat Wells   
As you investigate, I recommend updating the plan (next steps) and root cause fields as identified. 
In this case:
“When we pulled the battery and plugged it into a battery charger post flight, the charger had an initial reading of 9%.”
- The chargers are not accurate for main battery SOC and should not be used for that. This is the likely cause of the first problem. Is your group available to implement these CAs? https://jenaero.atlassian.net/browse/VXEP-762

“on 04/01/2025 we plugged in a HLB to the main battery harness and as we were moving it around it arched against the side of the aircraft upon inspecting the harness we noticed a small cut in the wire”
- This is almost certainly a separate incident with a separate C/CA, so it would be better logged as a separate linked incident. 
- Causes: Silicone wire is not very rugged and are not prevented from contacting sharp fuselage edges.
- CA:
- B35 should resolve many/all of these causes. You could link to that project.
- We could make similar changes to B30, but will likely recommend focusing on B35.
- The operator may have been routing the power cable out of the fuselage for ground power (indicated by the damage location to the wire and braid). We could check documents and training to excercise caution doing this.
- There are some previous occurrences of this that could be linked.

|  | HLB |  |  |  |  | Main Battery |  |  |
| Wh disch % | %SOC | Vnl calc | V/cell |  |  | %SOC | Pack Voltage (no load) | Cell Voltage |
| 0 | 100 | 29.31 29.3*2=58.6 4.2*14=58.8 | 4.19 |  |  | 100 | 29.9 | 4.3 |
| 10 | 90 | 28.58 | 4.08 |  |  | 75 | 27.83 | 3.98 |
| 20 | 80 | 28.00 | 4.00 |  |  | 50 | 26.3 | 3.76 |
| 30 | 70 | 27.50 | 3.93 |  |  | 20 | 24.7 | 3.53 |
| 40 | 60 | 27.06 | 3.87 |  |  | 15 | 24.4 | 3.49 |
| 50 | 50 | 26.73 | 3.82 |  |  | 5 | 23.7 | 3.38 |
| 60 | 40 | 26.49 | 3.78 |  |  | 0 | 21.3 | 3.05 |
| 70 | 30 | 26.32 | 3.76 |  |  | 30 | 25.4 | 25.4/7=3.6286 |
| 75 | 25 | 26.23 | 3.75 |  |  |  |  |  |
| 80 | 20 | 26.14 | 3.73 |  |  |  |  |  |
| 90 | 10 | 25.80 | 3.69 |  |  |  |  |  |
| 100 | 0 | 24.54 | 3.51 |  |  |  |  |  |

### Cameron Chapman, 2025-04-16

@Jackson Riley Curvin sorry for the delay.  Good work. 
Checkout, share, improve, etc this page for our typical investigation process. https://jenaero.atlassian.net/wiki/spaces/EF/pages/23363854/Incident+Troubleshooting+and+Resolution+Tracking. FYI @Pat Wells   
As you investigate, I recommend updating the plan (next steps) and root cause fields as identified. 
In this case:
“When we pulled the battery and plugged it into a battery charger post flight, the charger had an initial reading of 9%.”
- The chargers are not accurate for main battery SOC and should not be used for that. This is the likely cause of the first problem. Is your group available to implement these CAs? https://jenaero.atlassian.net/browse/VXEP-762

“on 04/01/2025 we plugged in a HLB to the main battery harness and as we were moving it around it arched against the side of the aircraft upon inspecting the harness we noticed a small cut in the wire”
- This is almost certainly a separate incident with a separate C/CA, so it would be better logged as a separate linked action. 
- Causes: Silicone wire is not very rugged and are not prevented from contacting sharp fuselage edges.
- CA:
- B35 should resolve many/all of these causes. You could link to that project.
- We could make similar changes to B30, but will likely recommend focusing on B35.
- There are some previous occurrences of this that could be linked.

|  | HLB |  |  |  |  | Main Battery |  |  |
| Wh disch % | %SOC | Vnl calc | V/cell |  |  | %SOC | Pack Voltage (no load) | Cell Voltage |
| 0 | 100 | 29.31 29.3*2=58.6 4.2*14=58.8 | 4.19 |  |  | 100 | 29.9 | 4.3 |
| 10 | 90 | 28.58 | 4.08 |  |  | 75 | 27.83 | 3.98 |
| 20 | 80 | 28.00 | 4.00 |  |  | 50 | 26.3 | 3.76 |
| 30 | 70 | 27.50 | 3.93 |  |  | 20 | 24.7 | 3.53 |
| 40 | 60 | 27.06 | 3.87 |  |  | 15 | 24.4 | 3.49 |
| 50 | 50 | 26.73 | 3.82 |  |  | 5 | 23.7 | 3.38 |
| 60 | 40 | 26.49 | 3.78 |  |  | 0 | 21.3 | 3.05 |
| 70 | 30 | 26.32 | 3.76 |  |  | 30 | 25.4 | 25.4/7=3.6286 |
| 75 | 25 | 26.23 | 3.75 |  |  |  |  |  |
| 80 | 20 | 26.14 | 3.73 |  |  |  |  |  |
| 90 | 10 | 25.80 | 3.69 |  |  |  |  |  |
| 100 | 0 | 24.54 | 3.51 |  |  |  |  |  |

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V808_250326_061141_pack.zip | archive | 1252 | 2025-03-26 | listed only |
| 808 main harness 1.jpg | image | 1208 | 2025-04-02 | listed only |
| 808 main harness 2.jpg | image | 1078 | 2025-04-02 | listed only |
| 808 main harness 3.jpg | image | 1516 | 2025-04-02 | listed only |
