# FS2-2320: Make XComm->VTOL SAFE On/Off messages require acknowledgements

- **Issue type:** Story
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2024-09-25
- **Updated:** 2026-10-12
- **Resolved:** 2026-10-12
- **Reporter:** Jason Scherer
- **Assignee:** Jason Scherer
- **Creator:** Jason Scherer
- **Labels:** sw_inReview
- **Parent:** FS2-1993 VXEP-416 Failure to Launch - Vehicle Investigation
- **Links:** relates to VXEP-416 (VXE 539 Failure to launch); relates to FS2-2404 (Test XCOMM->VTOL Safe On/Off message); relates to VXEP-1568 (VXE-818 Lift System didn't disengage - Crash - CAN bus error )
- **Epic Link:** FS2-1993

## Description

During launch XComm sends a series of MAVLink messages with checking confirmation of delivery. In the releated ticket this caused a launch failure due to not disabling SAFE mode before launch,
This report ([embedded: XComm MAVlink-Retransmit-Overview.pptx] ) provides an overview of the issue, current design (existing code), and two proposed solutions for consideration.

## Sprint

FS2 Sprint 33, FS2 Sprint 27, FS2 Sprint 24, FS2 Sprint 30, FS2 Sprint 28, FS2 Sprint 31, FS2 Sprint 25, FS2 Sprint 26, FS2 Sprint 32, FS2 Sprint 29

## Comments (5)

### Jason Scherer, 2024-09-25

@David Grosher @Scott Whitney This ticket is for updating XComm to require confirmation of MAVlink messages like SAFE On/Off to prevent the failure to launch issue in the related ticket. I created, and attached, an initial report on the issue and the existing code. I have also included a couple proposals for change in the report. Before I get too far, I would like to have a quick discussion, with firmware engineers, to review the proposed changes, brainstorm on alternatives, and determine the best path forward.
I don’t mind setting up a meeting, but I wasn’t sure who I should bring in. I was thinking Scott H, Gabe, and Kurt.
I’m also not sure how this task fits in priority to the other tasks. The effort here is probably 1-2 weeks for design, development, test and code review.

### David Grosher, 2024-09-25

@Jason Scherer One request from my side is that the solution be generic and extensible to different Mavlink messages. I think that is what you are proposing, but I just wanted it to make sure it was said.

### Scott Whitney, 2025-01-23

@Jason Scherer - is this in the 6.4 release? Looks like it has been tested but the PR has not been merged?

### Jason Scherer, 2025-02-06

@Scott Whitney I’m waiting for review of a design approach to fixing the problem. No development has started yet to address this problem. Moving back to ToDo for now.

### Christa Meck, 2026-10-12

No work done in over a year.  Canceling.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [XComm MAVlink-Retransmit-Overview.pptx](attachments/23480_XComm%20MAVlink-Retransmit-Overview.pptx.md) | pptx | 774 | 2024-09-25 | converted |
