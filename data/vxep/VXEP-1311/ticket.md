# VXEP-1311: VXE 530 GCS Lag

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Low
- **Created:** 2025-06-18
- **Updated:** 2026-03-02
- **Resolved:** 2025-10-29
- **Reporter:** Drew Hildreth
- **Assignee:** Ted Trowbridge
- **Creator:** Drew Hildreth
- **Labels:** TIQUILA, Weekly-incident-tracker
- **Links:** relates to VXEP-555 (VXE 530 Anomalies on Launch and in flight)
- **Customer:** TIQUILA
- **Severity:** 4 - Annoyance

## Description

During the landing pattern, it was observed that the aircraft position and telemetry on the GCS was 20-30 seconds behind the actual aircraft position.  This could have been an issue if the gap had been longer and the aircraft had landed before the operator was given the option to Enable User Landing Control.  See attached video of GCS showing aircraft on approach to landing while the aircraft was already on the ground.

## Issue Status

This ticket is from https://jenaero.atlassian.net/browse/VXEP-555 We are closing that ticket and this is the last thing needed to be finalized. Breaking out in a separate ticket per Dave's request.

## Comments (6)

### David Grosher, 2025-08-15

@Ted Trowbridge FYI, I told LMUK team that it is unlikely that we have the data in this version of the software to debug this issue, but that later versions does have some diagnostics to help facilitate debugging a laggy GCS.  If you agree there is nothing else to do then we can write that up with the details of the changes to address similar issues in the future and then we can close this out. 
FYSA,  @Drew Hildreth

### Lauren Velasquez, 2025-10-01

@David Grosher @Ted Trowbridge  Do we have a disposition for this aircraft? We are looking to get it into production for repair, and back to the customer. This AC was delivered to engineering 1/14/2025 and has since had quite a few tickets and investigations generated. Trying to lock down the final dispo.
@Drew Hildreth  FYSA

### Ted Trowbridge, 2025-10-01

@Lauren Velasquez this issue would be for the GCS only, unrelated to the aircraft itself.
We don’t have enough information/diagnostics to investigate further, I’m not sure what the final dispo should be given that.

### David Grosher, 2025-10-06

@Lauren Velasquez This should not hold up RMA of the vehicle. 
@Drew Hildreth FYSA, see Ted’s comment below. This can be closed as Bermuda triangle. There isn’t enough data in the log to resolve the issue.

### Lauren Velasquez, 2025-10-06

@David Grosher Are we able to get a Material  Disposition on what was determined to need repair / replaced from your team?

### David Grosher, 2025-10-06

@Lauren Velasquez Please see the reports attached to this ticket. This was an unusual RMA and had a multitude of issues. [VXEP-555] VXE 530 Anomalies on Launch and in flight - Jira. I’m not sure there is any hardware updates that are required.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V530_240822_151625_pack.zip | archive | 1849 | 2025-06-18 | listed only |
| V530 Landing While On the Ground.MOV | video | 23094 | 2025-06-18 | listed only |
