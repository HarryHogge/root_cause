# MS-395: Prevent Landing Pattern Previews from being created prior to Calibration/establishment of Reference Altitude

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-08-28
- **Updated:** 2024-10-24
- **Resolved:** 2024-09-04
- **Reporter:** Craig Burton
- **Assignee:** Craig Burton
- **Creator:** Craig Burton
- **Labels:** VSM
- **Sprint:** MS Sprint 18 & 19

## Description

This task will address the following related set of tasks:
- Prevent Previews of landing patterns if reference altitude has not been set. ✅
- Print landing pattern Purpose field as enumerated type in logs for easier troubleshooting. ✅
- Add landing pattern interactions to VSM event log (not there presently). ✅
- Send Aborted/Rejected (900.04==2) where possible (not possible with landing patterns). ✅

See NCR NCR-240826 - 4158 for additional details.

## Comments (1)

### Craig Burton, 2024-09-03

On the issue of Aborted/Rejected when the reference altitude hasn’t been set, it appears that VCSi doesn’t handle it properly.  We would expect them to inhibit uploading again, but, they keep on sending:

[embedded: image-20240903-211715.png]
Additionally, their progress widget in the UI shows 50%, a value that was not sent by the VSM:
[embedded: image-20240903-211822.png]

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240903-211715.png | image | 28 | 2024-09-03 | listed only |
| image-20240903-211822.png | image | 99 | 2024-09-03 | listed only |
