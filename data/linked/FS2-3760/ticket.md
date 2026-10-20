# FS2-3760: Testing for Observed NovAtel Heading Drift

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-10-09
- **Updated:** 2026-06-03
- **Resolved:** 2026-06-03
- **Reporter:** Eric Brewer
- **Assignee:** Eric Brewer
- **Creator:** Eric Brewer
- **Links:** relates to VXEP-1547 (VXE 930 One or more VTOL Sensor fail)
- **Sprint:** FS2 Sprint 35, FS2 Sprint 37, FS2 Sprint 36

## Description

NovAtel heading drift is causing some ‘VTOL SENSOR FAULT’ failures during launch wizard.  It was observed at Apex, and there is also a ticket here.  
[VXEP-1547] VXE 930 One or more VTOL Sensor fail and Battery Discrepancies - Jira

Given we are sending heading updates from VTOL, there is no good reason that the heading should drift away from the FWAP and VTOL estimates.  At this point we need to either:
A. Find and address root cause for heading to drift away from what the VTOL heading updates 
B. Alternatively, reset INS heading when it differs too far from VTOL
The recommended testing steps are as follows:
1. Place the vehicle somewhere far from the SLO repeater (at flight field is a great place to test this)
2. Enable NovEdge logging (@Ryan Smith can help with this)
3. Allow vehicle to sit for about 5 minutes, observe if heading drifts, and if so how far.  Anecdotally this seems worse in wind, so ideally find a location that has 10-15 knots wind.
4. Repeat 3 5-10 times, then review logs to determine next steps.

## Comments (7)

### Cameron Chapman, 2026-01-13

@Eric Brewer could GS help execute this test, or do you need FS to run it?

### Eric Brewer, 2026-01-14

@Cameron Chapman GS or FS would be capable of running the testing.

### Cameron Chapman, 2026-01-14

FYI @Drew Hildreth @Scott Lovett @Alexander Alan Arnold if you have anyone available to run this, please coordinate with Eric.

### Drew Hildreth, 2026-01-14

@Alexander Alan Arnold @Michael Mohr @Jackson Riley Curvin Can you take a look at the above? Please coordinate with Eric.
@Eric Brewer @Cameron Chapman FYSA

### Jackson Riley Curvin, 2026-01-14

@Eric Brewer @Cameron Chapman I just teams messaged @Ryan Smith on how to enable NovEdge logging.

### Eric Brewer, 2026-02-17

@Jackson Riley Curvin @Drew Hildreth a quick update on this - we’ve implemented a couple changes on the VBN development branch that may address this issue.  They are:
- Increase heading update rate to novatel
- If novatel heading disagrees with fixed-wing heading by more than 10 degrees, reset the filter state.

We’ll be testing these out over the next month and will plan to merge the features in once VBN is merged with the main branch.

### Eric Brewer, 2026-06-03

Resolved in apex builds with faster and lower uncertainty heading updates.

## Attachments (0)
