# VXEP-549: MAGNSS vehicles unable to connect to Edge GCS due to VSM taking command.

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-08-21
- **Updated:** 2024-09-19
- **Resolved:** 2024-09-19
- **Reporter:** Cameron Chapman
- **Assignee:** Craig Burton
- **Creator:** Cameron Chapman

## Description

- Cause is OGCS is taking over control.
- MAGNSS fix. Change to disable by default.
- Premagnss fix. Disable when edge GCS is needed.
- Update SCO and flight ops procedures accordingly.
- How to disconnect. https://jenaero.atlassian.net/wiki/spaces/MS/pages/340885515/Quick-Start+Setup+Guide+for+MCM+VSM+OGCS+VCSi

FYI @Carson Buckley @Scott Whitney @Ryan Babigian

## Comments (3)

### Craig Burton, 2024-08-21

Jo B and I will be turning off the automatic connect function on the MCM for the four MAGNSS vehicles:
- 509 ✅
- 517 ✅
- 575 ✅
- 576 ✅

### David Grosher, 2024-09-19

@Pat Wells I propose to close this issue. It is not an incident, it was an internal integration issue that has been resolved.

### Pat Wells, 2024-09-19

@David Grosher   I concur.  I was not tracking this at all.

## Attachments (0)
