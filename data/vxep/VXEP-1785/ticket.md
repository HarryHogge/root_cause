# VXEP-1785: B30 Multiple HLB Voltage Measurements Outside of Voltage Limits. Suspect VTOL AP or voltage sense circuit (harness, ground iso, etc)

- **Issue type:** Incident (8D)
- **Status:** D6 - Implementing Corrective Actions
- **Priority:** High
- **Created:** 2026-03-23
- **Updated:** 2026-10-05
- **Reporter:** Cameron Chapman
- **Assignee:** Trevor Gronner
- **Creator:** Cameron Chapman
- **Labels:** EE-Intern
- **Issue Status:** Initial C/CA identified. Investigating if this design/tolerances are acceptable for HLB SOC accuracty.
- **Severity:** 1 - Flight Critical

## Description

Investigation Sheet https://jenaero.sharepoint.com/:x:/r/sites/JAI_Operations/Shared%20Documents/NCR%20Investigations/VXEP-1785B30%20Multiple%20HLB%20Voltage%20Measurements%20Outside%20of%20Voltage%20Limits.%20Suspect%20VTOL%20AP%20or%20voltage%20sense%20circuit%20(harness,%20ground%20iso,%20etc).xlsx?d=w3a1a0159e9ca4c189338a55f176ca42b&csf=1&web=1&e=sIm69U
Chat Maddie Masiello: B30 HLB IB Voltage Limits Investigation.xlsx I also had this one... | HLB Voltage Issue | Microsoft Teams
See 1010  NCR List - AC 1010 HLB voltage outside limits. Dispo each
881 NCR-260224 - 8656 
941 NCR-260108 - 8115 removed and replaced red AP--MB
old SN: T-S105699, new SN: ES-100598
940 NCR-260106 - 8077 Tried another battery - did not work. Still outside of limits
NCR-260227 - 8710 SN ES-102789

removed T-S105700 and replaced red AP ES-100602
HLB voltage is out of limits.
SB: 29.0 - 29.6v
IS: 29.7v
VTOL control window and webpage show 29.7v and XComm webpage shows 29.38v. After about 10 minutes, voltage dropped to 29.6v on VTOL control window and webpage and 29.34v on XComm webpage. This was checked with two HLB's, both had the same issue. This is a new AC.

## Corrective Action

Before closing
- Update checkout to ensure HLB is fully charged (~29.3V) and tolerance to be 28.75-29.86V.  Report any measurements outside of this range. @Trevor Gronner  who can this task be assigned to update and verify? https://jenaero.atlassian.net/browse/VXEP-1993 
- This tolerance range referenced below does mean that operators might see anywhere from <90% (and not be able to launch) or >100% on a fully charged battery, which would lead to frustration and lost time/assets. Should be rare as that is worst case. If that is not acceptable, then one of the CAs in the linked JIRA could be pursued.
- Determine COA if resistor stackup caused a full HLB to read <90% SOC and therefore would not launch (replace resistors on relevant PCBs?) This may be ok to hold until/if the rare case that it happens, but might be a good reason to just update the PCB BOMs. @Jeremy Kostel

Longer term
- https://jenaero.atlassian.net/browse/VXEP-1994
- https://jenaero.atlassian.net/browse/VXEP-1995

## Plan

- Update procedures according to CA. Report any issues.
- Dispo all NCRs.
- NCR List - AC 635 HLB voltage outside of limits
- NCR List - AC 1010 HLB voltage outside limits
- @Eric Brewer would a <2% voltage inaccuracy be an issue for HLB SOC and other calculations. I would guess no, especially due to voltage losses/inaccuracy over the wire at high currents. If it was, then changing to the BMS measured value seems like it would be a better option.

## Root Cause

- Based on the tolerance stack up of the 1% resistors on this board, an actual voltage of 29.32V could read anywhere from 28.74-29.86V (not including any variation in the autopilot, temperature, etc.). See https://jenaero.sharepoint.com/:x:/r/sites/JAI_Operations/Shared%20Documents/NCR%20Investigations/VXEP-1785B30%20Multiple%20HLB%20Voltage%20Measurements%20Outside%20of%20Voltage%20Limits.%20Suspect%20VTOL%20AP%20or%20voltage%20sense%20circuit%20(harness,%20ground%20iso,%20etc).xlsx?d=w3a1a0159e9ca4c189338a55f176ca42b&csf=1&web=1&e=sIm69U 
- This tolerance range referenced below does mean that operators might see anywhere from <90% (and not be able to launch) or >100% on a fully charged battery, which would lead to frustration and lost time/assets. Should be rare as that is worst case. If that is not acceptable, then one of the CAs in the linked JIRA could be pursued.
- [embedded image-20260505-225101.png]

## Comments (5)

### Ben Norris, 2026-05-06

@David Grosher @Cameron Chapman From talking with various folks it seems like the there are a few possible solutions to fix the issue of this voltage measurement causing up to ±10% SOC error. From an electrical standpoint we can adjust the BOM of the board to call for 0.1% tolerance resistors for R75 and R79 which yields a ±2% SOC error which Ryan Christino agreed would be sufficient. From a software standpoint we can either use the BMS reported HLB voltage, or one time calibrate the span for VBATT in the VTOL AP to correct the error, or we could combine both techniques and use the BMS voltage as a reference to dynamically reset the span on boot. Lastly in the interim till either an electrical or software solution is implemented we can have the electronics production team test out the >5% SOC boards by checking the voltage reading from the AP against a known voltage. The following table is the reference for the AP for voltage to SOC.
| Voltage | SOC |
| 28.75 V | 90.7% |
| 28.80 V | 91.5% |
| 28.90 V | 93.2% |
| 29.00 V | 94.8% |
| 29.10 V | 96.4% |
| 29.20 V | 98.1% |
| 29.32 V | 100.0% ← last breakpoint |
| 29.32 V – 29.86 V | 100.0% (clamped) |

### Trevor Gronner, 2026-09-14

@Cameron Chapman Can I get some additional context on this request? From reading through the ticket, it looks like when batteries are at 29.32V, we expect to read anything from 28.75V to 29.86V on the VTOL Autopilot. It looks like you are requesting that every battery get charged to 100% on intake, checked to verify that the voltage reads 28.75V to 29.86V, then discharged back down to storage. Is that what engineering is requesting here or am I misunderstanding?
@Desiray Johnston @Catherine Wagner@Aidan Calvet  @Kyle Sharp FYSA, this looks like it would be a huge increase in battery processing on intake if I am understanding correctly. If this is a new engineering requirement, the check will likely fall into receiving inspection.

### Catherine Wagner, 2026-09-14

@Trevor Gronner Thank you for the heads up - going to tag in @Natalie Lusk

### Cameron Chapman, 2026-09-14

@Trevor Gronner @Desiray Johnston @Catherine Wagner@Aidan Calvet  @Kyle Sharpyou are welcome to message or meet if easier. I’ll paste this in a message.
 I am not requesting any additional steps. I am just recommending that anywhere the HLB voltage is checked it will have a wide tolerance range. If the HLB is full as it seems to be when these NCRs were written, the tolerance of voltage measurement will be 28.75V to 29.86V depending on component tolerances on the board. 
This could be problematic for operators. See recommended CAs above “This tolerance range referenced below does mean that operators might see anywhere from <90% (and not be able to launch) or >100% on a fully charged battery, which would lead to frustration and lost time/assets. Should be rare as that is worst case. If that is not acceptable, then one of the CAs in the linked JIRA could be pursued.”

### Zachary Mann, 2026-10-05

Flight Ops Team has been notified and a formal process is in works. Will update when finalized.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20260505-225101.png | image | 48 | 2026-05-05 | listed only |
