# VXEP-283: VXE-533 Uncontrolled drift and crash after failed VTOL abort

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-02-21
- **Updated:** 2026-08-05
- **Resolved:** 2024-08-23
- **Reporter:** Cameron Chapman
- **Assignee:** David Grosher
- **Creator:** Cameron Chapman
- **Labels:** Land_Abort_Logic, USASOC
- **Links:** clones VXEP-282 (VXE 533 VTOL power issue on transition led to Uncontrolled drift and crash on landing); relates to FS2-1512 (VTOL Abort logic fix); relates to RMA-221 (VXE-533 240222); relates to VXEP-233 (VXE-496 with 550 wing- abnormal behavior after transition to VTOL led to crash); relates to XKIT-1958 (Havoc 550 fuse 371 CW - Land Transition Failure 20240423); relates to XKIT-2421 (XKIT - Demo Prep Incident 20240612); relates to VXEP-1970 (VXE 525 Nose dive after transition )
- **Customer:** USASOC
- **Vehicle Tail Number:** 533
- **Vehicle Configuration:** Battery only.
- **Problem Type:** Other (explain in description)
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

This issue tracks the failed abort logic. See linked issue for VTOL failure in transition. 
Files: VXE-533 Uncontrolled drift and crash on landing
Location: FT Moore.
Weather: Calm and clear
John's description from operator perspective:
 On flight Number 4 the student was instructed to RTB the aircraft. After entering into ip4 I told the student to be ready to activate user nudge panel. The aircraft over shot landing zone, went into abort logic then did a quick turn It initiated VTOLs like it was trying to perform a VTOL landing. I tried to send the aircraft to an active waypoint but it appeared to be trying to VTOL and fixed wing flight at the same time eventually coming down in Tree line
 
Description from various students who witnessed the aircraft prior to VTOL transition:
 They described the aircraft heading north in its expected transition vector (IP5 to Landing) then overshooting the intended landing spot, turning approximately 90 degrees left, climbed steeply at which point it appeared to stall, rotate over left and entered a steep dive at which point they heard the VTOL motors kick in.
 
Scott's Description as an observer:
I was instructing from the GCS on the other aircraft at the site at the time of the incident.  When I first looked up I saw 533 in a steep very fast dive with an approximate east heading (where the previous student description ends).  The VTOL motors were on and never appeared to turn off for the rest of the incident.  Despite VTOL Motors being on it appeared to be flying fixed wing and pulled out of it's dive and flew back to the south climbing slightly and eventually coming to a standstill over a tree line approximately ¼ mile south where it slowly descended in a fairly standard VTOL descent before disappearing behind some trees.

VTOL and XCOM logs attached

## Corrective Action

Combine with 496 CA and have someone redesign and test all of the abort cases at different phases of the landing sequence to sort out the mode logic.  fF an abort is ordered, and an abort is allowed then it should actually abort (abort to FW should disable VTOL control).

## Plan

- Data review. I think this could use a timeline for what the aircraft did as this progressed if anyone is available for that.

## Issue Status

6/17 Aircraft has been delivered to Engineering for further investigation
Looks to me like there is some type of VTOL power failure with some sort of failed abort logic after the fact (similar to 496).
The FW throttles down right in landing prep
They start fighting each other once the abort is issued when the low power state is recognized. There is an error counter and once enough error types are registered for long enough then it will abort. They fight each other after that point because there is some sort of RACE condition in mode logic. But that is after the failure of the lift system 
In this case it took ~9 seconds to abort
In this case the mode in the VTOL AP returned to FW flight. But it seems that didn't cut the lift system from trying to spool up.

## Comments (7)

### Sean Odell, 2024-06-17

@Cameron Chapman @David Grosher @Pat Wells Aircraft has been delivered to Engineering for further investigation into electrical system and avionic/Red AP.

### Sean Odell, 2024-07-23

@David Grosher Are we at a point in the investigation where we know how to repair 533? I would like to get the RMA closed while you continue your investigation. Who on your team would know what I need to do?  I believe it is just a dual current sense, but I will await confirmation. 
@Cameron Chapman @Pat Wells FYSA

### David Grosher, 2024-07-23

@Sean Odell The issue holding it up is the linked https://jenaero.atlassian.net/browse/VXEP-282 that @Cameron Chapman is working. The software will be fixed with the upcoming v6.3.2 release.

### Cameron Chapman, 2024-07-23

@Sean Odell we have not been able to determine the cause yet.

### Pat Wells, 2024-07-24

@Cameron Chapman is this being blocked by software or hardware?  
Would like to expedite the return of this aircraft to the customer if possible. 
@Sean Odell  FYSA

### Cameron Chapman, 2024-07-24

@Pat Wells this aircraft is being blocked by the linked https://jenaero.atlassian.net/browse/VXEP-282 . We currently have no one to work on it without delaying critical IRAD projects.

### Pat Wells, 2024-07-31

@Jeremy White  FYSA on 533 status.  Investigation still ongoing.

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 533 pictures_2-21-2024.zip | archive | 247577 | 2024-02-21 | listed only |
| VTOL_VXE533.zip | archive | 33781 | 2024-02-21 | listed only |
| XCOMM_VXE533.zip | archive | 6662 | 2024-02-21 | listed only |
| image-20240221-205229.png | image | 47 | 2024-02-21 | listed only |
| image-20240221-205635.png | image | 182 | 2024-02-21 | listed only |
| image-20240221-212048.png | image | 184 | 2024-02-21 | listed only |
| image-20240222-001217.png | image | 164 | 2024-02-21 | listed only |
