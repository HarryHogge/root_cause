# FS2-1579: Implement CAs from v540 investigation

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-03-04
- **Updated:** 2024-04-26
- **Resolved:** 2024-04-26
- **Reporter:** Scott Whitney
- **Assignee:** Jason Scherer
- **Creator:** Scott Whitney
- **Parent:** FS2-1774 Crash after transition (v540)
- **Links:** relates to VXEP-284 (VXE-540 Crash after transition at training event); relates to FS2-1774 (Crash after transition (v540)); relates to FS2-1806 (Mission received validation error on the GCS)
- **Epic Link:** FS2-1774
- **Sprint:** FS2 Sprint 16, FS2 Sprint 17

## Comments (6)

### John Clark, 2024-03-18

@Scott Whitney could I get a link to the 540 investigation in question?

### Scott Whitney, 2024-03-19

@John Clark - here is the v540 issue. https://jenaero.atlassian.net/browse/VXEP-284

### Jason Scherer, 2024-04-12

@Scott Whitney New branch created (bugfix/FS2-1579-implement-cas-from-v540-investi). 
Pull request to merge with main created. (edgeautonomy / fixed-wing-ap / Pull Request #14: Check mission status before arm/launch of VTOL. Added debug messages that are not merged into main yet to avoid merge conflict later. — Bitbucket)

### David Grosher, 2024-04-22

@Jason Scherer Was a GCSS task created to explain and track the validation error on the GCS? 
@Scott Whitney FYSA.

### Jason Scherer, 2024-04-22

@David Grosher I don’t believe so. @Craig Burton @Michael Berger How do we create a GCS ticket to determine cause and resolve this issue on the GCS. 
Summary, The GCS does not have positive confirmation that the mission is received by the aircraft allowing the vehicle to launch VTOL with no mission. Issue can be reproduced by disconnecting the link prior to uploading the mission in the launch wizard (The VTED will require link before progressing though). 
A fix for this issue has been merged into the FWAP upcoming release 6.05p which prevents VTOL launch if no mission is loaded.

### Scott Whitney, 2024-04-22

Created https://jenaero.atlassian.net/browse/GCSS-272 to track on GCS board.

## Attachments (0)
