# FS2-2699: External Mag Release Notes & Documentation

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-01-08
- **Updated:** 2025-03-24
- **Resolved:** 2025-03-24
- **Reporter:** Scott Whitney
- **Assignee:** Scott Hunter
- **Creator:** Scott Whitney
- **Parent:** FS2-2697 6.4 Release Wrap Up
- **Links:** relates to FS2-2634 (6.4 Release Operation Manual); relates to FS2-2698 (MAGNSS Release Notes & Documentation)
- **Epic Link:** FS2-2697
- **Sprint:** FS2 Sprint 30, FS2 Sprint 31, FS2 Sprint 29

## Description

Requirement:
- Outline of all the release notes and reasoning
- Outline of all the changes the operator may see or be affected by


source material for release notes attached.
For the user experience, we’ve deleted the STANAG alerts that include “VTOL using FW MAG” That text will no longer appear in any alert messages because the VTOL isn’t using the FWAP mag data.
We’re also going to need some documentation on the new mag calibration procedure when it finalizes

## Comments (6)

### Scott Hunter, 2025-01-29

Scope = Capture the whole user experience for this new release for mag changes.
The change associated with changes I made is a change in wording for the stanag1100 alerts. I believe the mag changes to disable the FWAP mag would mean deletion of the mag calibration in the field. I’ll need to learn a little more to understand if the operator has different course of action when things go bad.

### Scott Hunter, 2025-01-29

This is the list of PRs that may impact the user experience. Where features were added to both XCOMM and VTOL builds I’ve deleted the PR in the XCOMM.
VTOL
I don't know if there's something in the manuals now about mag fail/heal at startup.
PR 230 - Vehicle Class displayed
PR 229 - System resets with no web connections. This won't be seen by customers but maybe FLOPS?
PR 223 - MAGNSS prelaunch difference when there's < 4 sats at the ublox
PR 224 - Adds log levels to some logging. I don't think this impacts the user
PR 221 - GCS commanded SD format
PR 220 - WMM.COF update, user may see a difference in magvar vs what they're used to.
PR 218 - Copyright update
PR 216 - Improve format sd messaging may impact FLOPS.
PR 212 - Prevent launch with bad SD card. Ties into GCS command to format
PR 209 - MAGNSS configuration
PR 207 - VTOL mag forward to FWAP. No more FWAP to VTOL. Changes to the stanag1100 alerts
PR 143 - SD Card key dump. I remember there being a problem without leading 0's. If there's something about that in the manuals it can be removed
PR 188 - MAGNSS changes. I'm imagining operators in a jammed environment and the GCS having GPS trouble. I don't know if they need MAGNSS docs to understand wha
PR 185 - Big MAGNSS merge.
PR 125 - The git hash was added to what's reported in the version. Does the user ever need to verify the whole version+hash

XCOMM
PR  91 - Web page includes GIT hash along with the version string. External customers don't see this but internal customers do.
PR  87 - Big MAGNSS merge.
PR  93 - MAGNSS sats used forwarded to FWAP. I don't know if/when the customer would see the effect of this
PR  88 - MAGNSS high variance data to FWAP. I don't know if/when the customer would see the effect of this
PR  60 - SD Card key dump. I remember there being a problem without leading 0's. If there's something about that in the manuals it can be removed
PR  92 - GCS commands to control payload and MCM power
PR 130 - Smart battery heater always enabled. Does this impact the user?

### Scott Hunter, 2025-02-02

I believe the only change to the user is deletion of the STANAG alerts that include “VTOL using FW MAG” That text will no longer appear in any alert messages.
We’re also going to need some documentation on the new mag calibration procedure.

### Scott Hunter, 2025-02-03

Candidate release notes attached.

### Scott Whitney, 2025-02-04

@Scott Whitney to review

### Scott Whitney, 2025-03-24

Thanks. Moving to done!

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [magReleaseNotes.txt](attachments/25873_magReleaseNotes.txt.md) | text | 5 | 2025-02-03 | converted |
