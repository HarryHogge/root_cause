# VXEP-1801: VXE 672 AS150 Plug Arcing

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** Medium
- **Created:** 2026-03-30
- **Updated:** 2026-04-29
- **Reporter:** Cameron Chapman
- **Assignee:** Drew Hildreth
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-553 (AS150 Plug/Pin Connector Issue Systemic Collector)
- **Severity:** 1 - Flight Critical

## Description

We’ve had some reports of users experiencing connector arching. We’ve advised them to clean the connectors well before and after use to reduce these occurrences, however some of the connectors have sustained some damage.
 
Could we provide any advice on the serviceability state of the connector and any remedial actions they may be able to take?
 
I’ve attached some pictures 😊
 
Thanks,
Dhruti Shah
Systems Engineer Sr
Lockheed Martin UK, Rotary and Mission Systems
M: +44 (0)7583095199
E: dhruti.shah@global.lmco.com[embedded file]

## Plan

@Drew Hildreth  this is likely caused by either a failure of the anti-spark resistor on the pin (possibly from overheat or tolerance issues), or a tolerance issue where the return pin connects after the + pin connects the non-resistor portion. I recommend the following. 
- Replace the power cable and send back to global support. Ensure new connector does not spark. Sparks can potentially damage electronics or make the power connector overheat. Any harness with consistent sparks should be replaced.
- Measure resistance of antispark resitor and dimensions vs drawing.
- List C/CA

## Comments (2)

### Drew Hildreth, 2026-03-31

@Cameron Chapman Dhruti and the LM UK Team would really like to not have to send the aircraft back. Is there anything we can do in the field for them? It is two aircraft total. I told her that the cable replacement would have to be done here.

If left as is, what additional potential damage do you foresee? We could have them measure for us if needed.

### Cameron Chapman, 2026-03-31

@Drew Hildreth We previously had people field install these cables. we could decide if customer or FSR could do that
 That seems like the best option. Not sure what document it was in. It was definitely part of the b25 to 30 conversion
I think it should be replaced. Hard to measure or quantify risk to flight. These contacts have had reliability issues.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 672 arching (2).docx | docx | 3462 | 2026-03-30 | no text found |
