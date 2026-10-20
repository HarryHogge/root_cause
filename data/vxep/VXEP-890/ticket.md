# VXEP-890: XCOMM Firmware - Forward Mag+Baro State data to MAIM

- **Issue type:** Sub-task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-01-08
- **Updated:** 2025-01-24
- **Resolved:** 2025-01-24
- **Reporter:** Kurt Burian
- **Assignee:** Joshua Boren
- **Creator:** Kurt Burian
- **Parent:** VXEP-880 MAIM v4 Software Release

## Description

Ping for MAIM board on expected IP address. If found, stream mag, baro, and UTC to MAIM address over UDP.

## Comments (2)

### Joshua Boren, 2025-01-21

Kurt Burian, how long after XComm power up should the MAIM be expected to be able to respond to a ping?
Is the XComm required to ping just once on startup?  A given duration after startup? Or periodically ping the MAIM waiting for a response until launch?
Discussed with Kurt and the path forward is to the the XComm listen for a hello message from the MAIM, and only configure the OEM7700 and start sending AirMagData once that datagram is received.  See https://jenaero.atlassian.net/browse/VXEP-883?focusedCommentId=46803

### Joshua Boren, 2025-01-24

Done, work captured in PR tied to VXEP-883

## Attachments (0)
