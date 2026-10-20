# VXEP-8: TPTR-6 VXE 489 fuse 408 CW VTOL Motor delayed start

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-08-23
- **Updated:** 2026-09-03
- **Resolved:** 2025-08-05
- **Reporter:** Allen Gardner
- **Assignee:** Cameron Chapman
- **Creator:** Allen Gardner
- **Links:** relates to VA-362 (TPTR-6 VXE 489 VTOL Motor delayed start with Drop Payload); relates to ENG-3040 (VXE 489 fuse 408 CW Forward Rotors not Starting On Landing Transition); is blocked by VA-391 (Address loose bus bar on VTOL AP board. Determine if service bulletin or AD are recommended. Create tasks for that if so. ); is blocked by VA-476 (Investigate if autopilot was reused from previous incident and could have contributed to latest crash. ); relates to VA-1030 (TPTR-6 (VXE 489 w/408 CW VTOL partial start) and loose bus bar)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** VXE 489
- **Plan:** Complete report and send to review: see https://jenaero.atlassian.net/browse/VA-240
- **Incident Type:** Near Miss
- **Severity:** 1 - Flight Critical
- **Impacted Disciplines:** Hardware, Quality Assurance

## Description

During training in a battery configuration, and drop payload the system came in to its final approach to transition into VTOL. The 2 front VTOL motors did not start. Causing the nose of the AP to tilt forward and the UAV speed forward. A few seconds the front 2 VTOL motors started. The system then levelled off and transitioned to its planned landing point then landed

## Corrective Action

This issue was not related to the vehicle operating with a drop payload.  
Possible Root Cause 1:
Quality: CARS in place for production (complete?) @Greg Fryer or @Matt Philley do you have a link to these CARS? -Cam
Engineering: assess current mounting method.  Determine whether AD and SB are required.  (on going)
- https://jenaero.atlassian.net/browse/VA-391
- https://jenaero.atlassian.net/browse/VA-444


Possible Root Cause 2:
Software: 
- Run lift motors ahead of landing sequence, capture current, if lower than expected, notify operator, go to ELZ patternhttps://jenaero.atlassian.net/browse/FS2-755
- Review autopilot code for arming sequence in recovery
- Add to backlog development: potential ESC firmware update
- https://jenaero.atlassian.net/browse/AP-3

## Root Cause

Two possibilities exist:
- Likely:
Quality or design issue: VTOL controller mass damping bar (brass bar) detached, causing shorts, and damaging the circuit board.
- Much less likely:
Simultaneous issue with both front Lift Motors/ESCs or chip hardware issue impacting only the front two.

## Comments (5)

### Allen Gardner, 2023-08-25

@Sam Miller Sam can you create a list of all necessary corrective actions to resolve this problem?

### Matt Philley, 2023-09-06

@Marc Richardson who from the QA team should be involved on this one? Looks like Engineering is investigating on https://jenaero.atlassian.net/browse/VA-391 and CA’s will most likely be in Electronics to the Avionics Board Assy.

### Marc Richardson, 2023-09-06

@Matt Philley We will have @Brad Crampton work on this.

### Christa Meck, 2025-04-17

Removed parent to prep for Incident hierarchy change.  Parent is linked as Linked issue.

### Christa Meck, 2025-08-05

Closing this incident as it’s from August 2023 and any investigation is likely done at this point.

## Attachments (0)
