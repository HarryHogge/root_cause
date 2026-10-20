# OGCS-526: Websocket Auth Refresh Causes False 'Reconnecting...' Alert

- **Issue type:** Bug
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2026-01-30
- **Updated:** 2026-02-11
- **Resolved:** 2026-02-11
- **Reporter:** Ted Trowbridge
- **Assignee:** Ted Trowbridge
- **Creator:** Ted Trowbridge
- **Affects versions:** 1.3.3 (TIQ #5)
- **Fix versions:** 1.4.0 (LRR #3)
- **Parent:** OGCS-485 Technical Debt (1.4.0)
- **Links:** fixes VXEP-1685 (VXE 942 Lost comms after 21 minutes in flight, reestablished control but Reconnecting never went away)
- **Epic Link:** OGCS-485
- **Sprint:** MS Sprint 33

## Description

Based on the observed behavior (telemetry was streaming, the vehicle was moving on the map, and the UI was populating), we know the vehicle was actually connected. High-rate telemetry updates are received via WebSocket, confirming that connection was active. Commands like "go to waypoint" and flight mode changes are issued as atomic REST/HTTP requests, and those were also working. The "Reconnecting..." spinner was incorrect and operators made the correct decision to ignore it and continue flight.
The logs indicate that around the time Craig noted heartbeats stopped, there were two WebSocket disconnections. The first was due to an auth token expiring, which was successfully refreshed and reconnected after ~5 seconds. One minute later, at 2026-01-29T22:51:01.796Z, there was an abnormal WebSocket disconnect which corresponds exactly to heartbeats stopping.
Analysis of the code indicates the auth refresh logic is flawed, causing two WebSocket connections to be opened rather than reusing the existing connection. When one of the two connections closes, the system incorrectly reports a full disconnection despite the other remaining open and receiving telemetry. This is a logic error and synchronization issue.
Refreshing the page would likely have resolved the issue, but it’s understandable why that was avoided because it could’ve exacerbated comms issue - and we specifically warn not to via an OGCS dialog.

## Comments (1)

### Ted Trowbridge, 2026-02-11

OBE following STANAG 4586 refactor and new logic to determine ‘Reconnecting…’ state.

## Attachments (0)
