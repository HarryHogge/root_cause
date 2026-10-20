# GCSS-99: Force Restart of GCS Following Load of DTED

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2023-09-06
- **Updated:** 2026-09-23
- **Resolved:** 2026-09-23
- **Reporter:** Craig Burton
- **Assignee:** Michael Berger
- **Creator:** Craig Burton
- **Links:** is caused by VA-439 (Record 371 YPG near miss incident, the procedure you used to fix it, and any recommended corrective actions to prevent it in the future? ); blocks VXEP-45 (371 mis-configured (ready for flight then DTED loaded))

## Description

There are probably several ways to programmatically avoid the scenario described in the attached email.  We should consider all options to ensure that pitot calibration is consistent with DTED at the time of operation.  Please see attached email.

## Comments (2)

### Michael Berger, 2023-09-12

When DTED is changed (added/removed), block the starting of the Launch Wizard until GCS Software is restarted. Also,  if you are already in the Launch Wizard exit the Launch Wizard immediately.

### Christa Meck, 2026-09-23

No work done in over a year.  Canceling.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [RE Issue with loading DTED in flight .msg](attachments/16129_RE%20Issue%20with%20loading%20DTED%20in%20flight%20.msg.md) | msg | 146 | 2023-09-06 | converted |
