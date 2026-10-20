# VXEP-1641: E140 MWIR VectorNav Not Communicating

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-12-13
- **Updated:** 2026-08-05
- **Resolved:** 2026-08-05
- **Reporter:** Cody Smisek
- **Creator:** Cody Smisek
- **Links:** relates to PLD-139 (E95 SN 8098 and  8115 Vector nav not responding when tested with 987.); relates to PLD-138 (E95 EPS-8093 and EPS-8090 Customer Issues -camera would not connect to software. Camera would not power cycle or power off); relates to RMA-790 (EPS6222 ); relates to RMA-706 (EPS140G2-Z S/N 6097 RMA # 250602-3)
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

SLO Engineering E140 MWIR labeled Franky V3.2 (unknown SN) position does not update. 
In Epsilon Errors
-Critical error - Tilt Encoder No Index
-Secondary error - GPS no communication GPS init failed

As a part of troubleshooting, using Epsilon Beta SW for INS pass-through, unable to connect to VectorNav through Control center and serial connection.

## Comments (6)

### Cody Smisek, 2025-12-13

@Cameron Chapman @Greg Fryer @Mike DeJesus @Grant Goodman FYI. Unassigned not sure who is POC

### Connor Peebles, 2025-12-18

Franky was completely un-reachable. Had to reflash Sightline FW and then reflash Epsilon FW worked around . Afterwards we regained gimbal control but GPS was non-functional, we carried on without GPS as that was not the issue we were focused on fixing at the time. Confident that this issue is not related to Adv-nav.

### Connor Peebles, 2026-01-26

@Cody Smisek @Mike DeJesus  Franky was sent back to HSV (I think, Cody to clarify)

### Cody Smisek, 2026-01-26

@Connor Peebles Returned under 6469- RMA 260123-5

### Christa Meck, 2026-08-05

@Pat Wells It looks like this one has been resolved.  The two linked RMAs are complete.  OK to close this out?

### Pat Wells, 2026-08-05

@Christa Meck Yes

## Attachments (0)
