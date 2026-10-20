# VXEP-1848: 918 MCM Failure

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** Low
- **Created:** 2026-04-16
- **Updated:** 2026-09-02
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Bethany Ponce
- **Creator:** Alexander Alan Arnold
- **Labels:** GS_Closed, Precision
- **Links:** relates to RMA-933 (VXE-918  RMA 260310-1)
- **Customer:** Precision
- **Vehicle Tail Number:** 918
- **Vehicle Configuration:** ADV NAV VXE 30
- **Plan:** Attempt to connect via GbE and AircraftNetwork Attempt to connect via Serial
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Justin Peterson conducted trouble shooting with Precision crew and recommended the MCM be swapped.

Unknown on why mcm failed

## Corrective Action

A full reflash from a single consistent L4T BSP package covering all firmware partitions is recommended. It is probable that a reflash using the current process would remedy this error.

## Issue Status

Unable to gain access through either interface. No ping on either interface. Serial shows activity on boot but does not reach login and does not accept input.
Analyzed serial output in order to understand possible causes. Serial output (near fault point) attached above with analysis.

## Root Cause

Unsure of exact cause cannot be definitely determined since the device history is not completely known. Given that the intake form shows that the device was functional at some point, it seems most likely that a hard power cycle during one of the EKS payload file writes has corrupted the boot flow (the security components check out during auth but when the system actually tries to use them, it crashes and fails to boot up.) A second possibility could be that the system has some kind of firmware component mismatch, but, if the aircraft has flown before this is less likely.   
Notably, though, we’ve had a several issues with MCMs overheating when not in flight or not actively cooled (the small fan that is attached for HIL testing isn’t always enough.) Depending on the condition of the MCM before testing occurred (was it powered on for a period without movement or a fan? was it uploading data or otherwise ”working” without active cooling?) it COULD be that there was an issue with heat that caused a break down in the functionality that could not be restored. @Justin Peterson

## Executive Summary

Probable that hardpower cycle corrupted boot flow. Customer recieved replacement in April. Probable cause; Hardware Issue.

## Comments (7)

### Alexander Alan Arnold, 2026-04-16

@Justin Peterson Can you paste a write up of what you did with precision and why you recommended the MCM be swapped in this aircraft?

### Alexander Alan Arnold, 2026-04-16

@Lauren Velasquez @Samuel Lopez

### Justin Peterson, 2026-04-16

@Alexander Alan Arnold 
Background: I had a call from precision that they were unable to ping the MCM or get any of the functions on the MCM.
Steps performed by Precision:
- Went through several ping tests while directly wired to the aircraft
- Tried several default IP addresses that the MCM could have been set to
- Tested power cycling the aircraft
- Checked temperature of the MCM - it was warm to touch, indicating it was likely on and running
- Used wireshark to try and identify any stray IP addresses that were set on the system - did not identify any communication

Direction given to Precision:
- Start an RMA and we will resolve and return the product with a working MCM.


Direction given to @Jessica Meyers  and @Alexander Alan Arnold 
- Do a quick smoke test with the customer’s hardware as returned.  See if we can reproduce
- If the MCM is still not communicating, swap the MCM assembly
- If new MCM is talking, then cool, ship the hardware back and this is an MCM issue
- Send MCM to SW engineering to test and scan for IPs and configuration
- If engineering cannot talk to the board, send to electrical
- If the new MCM does not talk, then there’s likely a wiring/electrical issue
- Probably electrical - test wiring on aircraft

I have lost the ball on what step we are in our RMA process

### Justin Peterson, 2026-04-22

MCM is with Bethany Ponce for investigation.

### Bethany Ponce, 2026-04-22

Worked with this MCM and added not4s and recommendations above @Justin Peterson

### Bethany Ponce, 2026-04-23

What can I do for next steps here? I can deliver it to e-shop for further analysis if that is most beneficial?

### Justin Peterson, 2026-04-27

@Bethany Ponce Thanks for the analysis and log files.  I would concur that we should proceed with a reflash.  It seems likely that this MCM may have been sitting idle for some time, but it is unlikely to have been run in any extreme conditions.
Recommend that we note this as an outlier and watch for any other issues in MCMs failing during an overheat with the rest of the fleet.  Another long-term thermal analysis like what has posted at the link below might be necessary - especially as MCM usage increases
https://jenaero.sharepoint.com/:p:/s/EngineeringTeam/IQDYKBXod2q5RYmGuWDDEGGWAd8kv1pWsGtg-Sy-_e-gPEo?e=dbuCcg

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [jetson_serial_output.txt](attachments/54307_jetson_serial_output.txt.md) | text | 3 | 2026-04-22 | converted |
