# VXEP-380: VXE 541 D4500638 Fuel cell faults during preflight and during flight

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Confirmed
- **Priority:** Highest
- **Created:** 2024-04-26
- **Updated:** 2026-03-02
- **Resolved:** 2024-08-30
- **Reporter:** Pat Wells
- **Assignee:** Sean Wendling
- **Creator:** Pat Wells
- **Labels:** USASOC, Weekly-incident-tracker
- **Links:** relates to RMA-242 (D4500638 Plus Fuel Cell 240418-5)
- **Customer:** USASOC
- **Vehicle Tail Number:** 541
- **Corrective Action:** Stack Replacement is primary corrective action. Exact cause of crack unknown.
- **Issue Status:** Triage and Rework steps confirmed, awaiting replacement stack.
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

From Operator:
During preflight we noticed the error, restarted the system and it went away. After beginning flight received alerts saying fuel cell had shut itself off. Pressed start button and after third try it turned back on but we still had the error showing so we landed. 

AAR file attached
Screenshot of error attached
10th SFG
Under investigation by EAES team. Live Investigation report can be found at this link: VXEP-380 (VXE 541 Fuel cell faults during preflight and during flight)

## Plan

RMA Plan: 
- Requested Stack Replacement.
- Awaiting MTR for new Stack for Repair
- Dissection and confirmation of suspected Failure Mode.
- Confirmed to be Cell Crack
- Misreporting Cathode (In AAR) likely due to data transmission # of bits.
- Receive Stack and return unit to customer after repair complete.

Fuel cell serial number:
D4500638

## Root Cause

Suspected internal cell crack. Due to shipping conditions, exact root cause is extremely difficult to assess. Stack failure due to cell & reactor holder cracking is known to be a common failure mode caused by hard landings and propagates over time.

## Comments (7)

### Cameron Chapman, 2024-04-28

@Tom Westrich @Sean Wendling

### Sean Wendling, 2024-04-29

@Cameron Chapman @Pat Wells Hey Team, I have reviewed this data preliminarily and I suspect that this fuel cell has failed, and would ask that we process it as an RMA and return to Ann Arbor so we can dissect and review cause of failure. We will plan to re-stack this unit as based on cycle count it failed prior to warranty expiration. Report is started, and I will update as I uncover more from the AAR. Thanks!

### Sean Wendling, 2024-06-18

@Sean Odell , this is https://jenaero.atlassian.net/browse/RMA-242?atlOrigin=eyJpIjoiNzNhYzUzMjdmOTg0NDdjY2I0OTkzOThkYjM2ZDJlYWQiLCJwIjoiaiJ9 , Could we link them together and update the Jira ticket. Looks like there was a serial number representation was incorrect inside the MCU of this unit.

### Sean Odell, 2024-06-18

@Sean Wendling Linked the issues as requested.

### Greg Fryer, 2024-08-30

@Sean Wendling and/or @Sean Odell Did we finish this? There’s been no activity recorded in a couple months, did we finish the work and not finish the tickets?

### Sean Wendling, 2024-08-30

Hey @Greg Fryer , apologies. Yes I believe the dissection and failure analysis is complete. I will verify. I do remember it was difficult to pinpoint exact failure mode as they shipped us the fuel cells in a cardboard box and the handling likely blurred the exact failure mode. We have not returned the RMA stack at this time, but I think we can close out the engineering ticket and leave open the RMA specific actions.

### Sean Wendling, 2024-08-30

Cell Cracking is a common source of system failure and can occur from a number of root causes. In this case, it is difficult to surmise exact cause as the unit was returned in improper shipping case, resulting in additional damage to the system. Replacement stack is requested.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V541_240424_111043_pack.zip | archive | 2525 | 2024-04-26 | listed only |
| image000001.jpeg | image | 80 | 2024-04-26 | listed only |
