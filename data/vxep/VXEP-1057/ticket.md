# VXEP-1057: VXE 398 Aborted Takeoff after 10 feet

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-02-28
- **Updated:** 2026-09-09
- **Resolved:** 2025-06-02
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** No_crash, PMA263, Training, Weekly-incident-tracker
- **Links:** relates to VXEP-1179 (498 Aborted Launch); relates to VXEP-1047 (VXE-729 Aborted launch)
- **Customer:** PMA263
- **Vehicle Tail Number:** VXE 398
- **Vehicle Configuration:** VXE 30 Main Battery Config
- **Plan:** Have an Engineer confirm the issue status.
- **Issue Status:** After analyzing data it appears that the GCS and vehicle logs show a drop in received network traffic.
- **Root Cause:** Dropped Radio Link, possibly misconfigured radios
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Operator states that Aircraft aborted takeoff sequence after reaching approximately ten feet

## Comments (4)

### David Grosher, 2025-02-28

[14:32:37.930 2976.930] ap dbg: vt lost link during lch, aborting
[14:32:37.932 2976.932] ap dbg: vt lch abort triggered

### Pat Wells, 2025-03-17

@David Grosher @Jason Scherer is this issue related to this: https://jenaero.atlassian.net/browse/VXEP-1047

### David Grosher, 2025-05-19

@Pat Wells @Jackson Riley Curvin It was mentioned in the incident meeting that other PMA-263 operators were having issues with un-commanded aborted launches but were not formally reporting those incidents. Is that happening with the same group or at the same location or with the same ground radio? Given that FLOPS is not experiencing this type of behavior and that we aren’t receiving incidents from other fleets or customers I think these potential links need to be explored further.  (Same comment as the other issue)

### Jackson Riley Curvin, 2025-06-02

closing issue due to customer not responding when asked for relevant data.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V398_250226_093218_pack.zip | archive | 3295 | 2025-02-28 | listed only |
| 398 VtThr.png | image | 122 | 2025-04-15 | listed only |
| 398.png | image | 88 | 2025-04-15 | listed only |
