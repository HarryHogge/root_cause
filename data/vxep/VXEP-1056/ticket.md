# VXEP-1056: VXE 401 Magnetometer Maintenance required message

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-02-28
- **Updated:** 2026-10-08
- **Resolved:** 2025-05-19
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Eric Brewer
- **Creator:** Alexander Alan Arnold
- **Labels:** Hardware, No_crash, PMA263, Weekly-incident-tracker
- **Customer:** PMA263
- **Vehicle Tail Number:** VXE 401
- **Vehicle Configuration:** VXE 30 Main Battery configuration
- **Incident Type:** Mission Failure/Abort
- **Severity:** 3 - Degraded Performance - With Workaround
- **Executive Summary:** Known magnetometer issues on 6.3.4 -- 6.4.0 disables fixed wing magnetometer alleviating issues

## Description

Please see attached FDR from a flight from yesterday where we got multiple mag errors in flight (which we see quite often). Upon landing under action required it said something like magnetometer giving bad data , tried to get a screenshot but it closed quickly.
 
We did preflight this morning and it passed all tests,

## Root Cause

This was attributed to 6.3.4 6.40 firmware fixed the issue.
Known magnetometer issues on 6.3.4 -- 6.4.0 disables fixed wing magnetometer alleviating issues

## Comments (4)

### Eric Brewer, 2025-02-28

@Alexander Alan Arnold confirmed - this is the known magnetometer software issue with 6.3.4.  I see that the VTOL mag failed 3 times and was declared permanently failed.  When this occurs the VTOL autopilot uses the fixed-wing mag with this version of software.  This is a software issue with 6.3.4 and does not indicate any real issue with the magnetometer.  They can continue flying this bird.  The issue is addressed in the 6.4 release that we’re working on now (I don’t know release timeline of that but it’s ‘soon’).
@Scott Hunter @David Grosher FYI.

### Alexander Alan Arnold, 2025-02-28

Understood. Do you want to link the known issue to it before I close it? @Eric Brewer

### Eric Brewer, 2025-02-28

@Scott Hunter do you have an issue number you can assign to this? I didn’t see one on a quick database search but I know you fixed it in 6.4.

### David Grosher, 2025-05-19

Fixed in v6.4

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V401_250227_144956_pack.zip | archive | 4320 | 2025-02-28 | listed only |
