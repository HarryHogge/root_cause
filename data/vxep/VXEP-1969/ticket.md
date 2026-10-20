# VXEP-1969: VXE 889 - aircraft lost comms, was commanded to land immediately. Found that ini. file was corrupt.

- **Issue type:** Incident (8D)
- **Status:** D4 - Release RCR
- **Priority:** Highest
- **Created:** 2026-07-27
- **Updated:** 2026-10-20
- **Reporter:** Stephan Johnson
- **Assignee:** Alexander Alan Arnold
- **Creator:** Stephan Johnson
- **Labels:** Crash, Hardware, Investigating, PMA263, RCCA, Weekly-incident-tracker
- **Issue color:** yellow
- **Asset type:** VXE30
- **Customer:** Air_PMO
- **Vehicle Tail Number:** VXE 889
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

No operator Statement

## Vehicle Configuration

VXE30
SUAV 6.6.1

## Executive Summary

Awaiting FTP data and operator statement for aircraft. Ted discovered ini had been changed. Probable cause Operator Error

## Comments (7)

### David Grosher, 2026-07-29

@Ted Trowbridge Can you take a look at this one.

### Ted Trowbridge, 2026-07-29

@David Grosher @Alexander Alan Arnold 
LandOnError=1 is enabled in the gcs.ini
From the logs I can see that the vehicle lost communications and was commanded to Land Immediately.  I suspect it was unable to nudge for the same reason there was comm loss, continuing to investigate.
```
[09:51:21.703] Show Caution(): Master Caution
[09:51:21.705] MessageBoxTop(): LOSS OF DOWNLINK WARNING
[09:51:21.759] OnAfterTrackingLayerDrawMap1 blocked ms=35375
[09:51:21.760] Reset Comm/GPS Loss Timers
[09:51:21.781] PollMainLoop blocked ms=35390
[09:51:21.829] mci stopped receiving replies, reconnect required
[09:51:24.765] Show Caution(): Master Caution
[09:51:24.765] MessageBoxTop(): LOSS OF DOWNLINK LANDING
```

### Ted Trowbridge, 2026-07-29

Interesting to note that gcs.ini is not corrupt in other ways previously seen.  The colors and labels that had bad values which we highlighted in the SB are not observed and there would have been no indication to the operator LandOnError was set.

### Alexander Alan Arnold, 2026-08-07

Emailed customer to gather conduct FTP on aircraft.

### Alexander Alan Arnold, 2026-08-12

@Ted Trowbridge confirm separate from originally created AN capturing the ini issue, creating report and i need to indicate that it more than likely someone changed it rather than the system corrupting it

### Alexander Alan Arnold, 2026-09-16

@Ted Trowbridge I was able to get an FTP and other logs from the customer, loaded them into this ticket.

### Stephan Johnson, 2026-10-05

@Ted Trowbridge do we have a report for this investigation that isn’t in code? Not sure who Jonathan Koziol is, but his attached investigation isn’t readable.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V889_260624_092808_pack_land immediately incident.zip | archive | 461 | 2026-07-27 | listed only |
| [RE VXE-30 Incident Report 07-15-26.eml](attachments/63803_RE%20VXE-30%20Incident%20Report%2007-15-26.eml.md) | eml | 2338 | 2026-07-29 | converted |
| DOD SAFE-XUFOrQYD7E7seMrm.zip | archive | 45942 | 2026-09-16 | listed only |
