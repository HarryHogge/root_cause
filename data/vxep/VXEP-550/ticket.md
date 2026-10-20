# VXEP-550: VXE 509 Connection to HLB BMS is causing ground issues, current offsets, and possible transients and damages.

- **Issue type:** Bug
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2024-08-21
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Cameron Chapman
- **Assignee:** Abel J. Markow
- **Creator:** Cameron Chapman
- **Parent:** VXEP-456 Create list of issues discovered, improvement ideas, tests recommended. Prioritize the list and determine implementation plan
- **Links:** relates to ENG-2945 (Quantify transients and risk to equipment of having the HLB data connector plugged in when plugging in the main battery  power (this bypasses the ground isolation board functionality).); relates to ENG-2944 ([REMOVE from VXEP] VXE 689 - VTOL battery voltage sensor stopped working after power cycling. )
- **Epic Link:** VXEP-456

## Plan

@Adrian Garcia please add or link transient measurement findings here. 
link to Jira ticket that has my notes for 8/21 https://jenaero.atlassian.net/browse/VXEP-547

## Issue Status

NCR 4110: AC 509 (RMA/Engr Retro) - SCO - Lift Motor Current Sense Issue with Payload
8/21 Testing with MAGNSS and VXE30. 509 troubleshooting.xlsx
Summary
- Payload turns on, lift motor current goes down.
- Initially, left boom was reporting significantly.
- About 5A of fluctuation at 160A (approx. climb loads). While not ideal, this seems low risk and should not gate flight.

 
Discoveries
- Resolved with disconnecting HLB data connection. Issue resumes when reconnected.
- Gets worse with more payload current.
- Issue repeats with new MAGNSS fuse, and reportedly new CW. Have not fully verified yet. Repeats with another MAGNSS fuse.
- No load is the same behavior on VXE30 and 2 magnss vehicles.
- Same behavior on MAGNSS and VXE30.

## Comments (1)

### Matt Philley, 2024-08-21

Dispo for NCR:
Based on troubleshooting it has been determined that the issue is an existing behavior that appears to be more noticeable on this aircraft, but poses no additional risk from the standard hardware/software configuration. Acceptable to use as is.

## Attachments (0)
