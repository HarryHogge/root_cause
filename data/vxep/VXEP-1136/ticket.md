# VXEP-1136: VXE 557 Inaccurate SoC Model Causing Battery State to Fluctuate (OCT 12th Incident)

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-03-13
- **Updated:** 2026-04-22
- **Resolved:** 2026-04-22
- **Reporter:** Adrian Garcia
- **Assignee:** Cameron Chapman
- **Creator:** Adrian Garcia
- **Labels:** USASOC, Weekly-incident-tracker
- **Links:** split from VXEP-761 (VXE 557 Smoking Smell from Fuselage after connecting main battery); relates to VXEP-1177 (VXE 808 State of Charge discrepancy)
- **Customer:** USASOC
- **Vehicle Tail Number:** VXE 557
- **Incident Type:** Aircraft Damage
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Separating https://jenaero.atlassian.net/browse/VXEP-761 into two different incidences to keep track of C/CA found for the two different dates - OCT 12th and OCT 30th 
From Main Investigation: 
Unknown at this time. Battery passed all of its pre launch checks. It also passed its battery health check after the flight per the maintenance manual. After conducting a RTB at 32% the aircraft main battery percentage started fluctuating from 16-30% rapidly. This started happening after beginning IP 1 and didn’t end until passing into IP4. The aircraft was landed safely and the VXE software reported 30% main battery life on ground. After letting the battery cool off the main battery charger reported the battery at 12%.  
On 30 October 2024 the 3rd SFG(A) conducted an operational check on aircraft 557. This was the first operational check since the aircraft last flew on 12 October. We made sure to use a different main battery then what flew on the 12 October flight. Three minutes into the aircraft being turned on a strong burning smell came from the inside of the aircraft. After disconnecting and powering down the aircraft we noticed that the main power cable that plugs into the main battery had a corrosive substance on it. While out here we have made sure to pay extra attention to these ports to ensure there has been no carbon buildups and we can verify the port was clean prior to use. I believe this issue is what contributed to the rapid battery fluctuation for the flight on 12 October.

## Corrective Action

- https://jenaero.atlassian.net/browse/VXEP-762
- https://jenaero.atlassian.net/browse/VXEP-553

## Plan

- Separate VXE557 investigation report into two different issues -  VXE 557 Inaccurate SoC Model Causing Battery State to Fluctuate (OCT 12th Incident).pptx
- (3/18/25) Review characterization of SOC and review FW code, which will drive an update to the ppt charts, explanation and next steps.
- 3/25/25 State of charge model, find where code lives and replace pcb, find if FW table values have a limit, ensure model works of derived values in table for SOC. complete by 4/1/25

## Issue Status

Copied from https://jenaero.atlassian.net/browse/VXEP-761 : 
- Nothing unusual has been found in the data involving Oct 12th incident other than low sampling rate and evidence of an inaccurate SoC model. I believe that the two incidents are unrelated and the Oct 12th incident would not have been presented to ENG if the fuselage did not smoke on Oct 30th
- Battery Info:
- Both batteries were built in house in SLO - battery data 3-1351 and 3-1353.xlsx
- Main Battery SN : 3-1353 (oct 12th incident) and 3-1351 (oct 30th incident)Send back to RMA and replace Fuselage Power Harness (PN: 107-102189-1 and 107-102189-2)\
- @Pat Wells @Alexander Alan Arnold Are you able to advise the customer to quarantine the battery that was involved in the OCT 30th incident. The battery SN is 3-1351. The suspected cause of the incident is an unmated connection and may be a cause of out of spec sockets on the battery side. Can we get it sent back for testing?
- 4/1/25 Has not moved forward; no resources allocated.

## Root Cause

- Caused by AS150 damage/systemic issue. Tracked here. https://jenaero.atlassian.net/browse/VXEP-761 and here https://jenaero.atlassian.net/browse/VXEP-553
- Inaccurate SoC Model caused the fluctuation of Battery State on OCT 12th
- Logs do not show any explicate signs of  a bad mating connection - Voltage and current dropping simultaneously.
- VLife - Main Battery State in the Logs - shows a large fluctuation when the load is out of the 400W and 30A range. This was also seen on different flights not related to this vehicle

## Comments (2)

### Adrian Garcia, 2025-03-13

@David Grosher , @Cameron Chapman recommended to split this investigation into two different tickets - one for the OCT 12th date where SoC may be the root cause and another form the OCT 30th date where the AS150 is the root cause. I will also be splitting up the investigation reports to coincide with each investigation number 

FYSA @Pat Wells @Alexander Alan Arnold

### Adrian Garcia, 2025-04-01

@Steve Gonzales There is the State of charge curve captured by the vehicle vs the battery model used and the desired SoC model. One thing to note is that the model is based off an unloaded battery. 
[embedded: image-20250401-174156.png]
V557 XCL00198 SoC model Attempt .xlsx
Main battery_model_ESR_Data_analysis.xlsx

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [FW Battery SoC Calculation 3.pptx](attachments/27820_FW%20Battery%20SoC%20Calculation%203.pptx.md) | pptx | 389 | 2025-04-01 | converted |
| image-20250401-174156.png | image | 60 | 2025-04-01 | listed only |
