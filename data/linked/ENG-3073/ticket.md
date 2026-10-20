# ENG-3073: 538 Altitude Drop During Landing

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-05-21
- **Updated:** 2026-06-16
- **Resolved:** 2026-06-16
- **Reporter:** Daniel Lloyd
- **Assignee:** Pat Wells
- **Creator:** Daniel Lloyd
- **Labels:** TIQUILA
- **Links:** relates to VXEP-415 (VXE 538 Altitude Drop During Landing)

## Description

During a training flight the student pilot was practicing manual nudge during a vertical landing. With the aircraft paused they were maneuvering around when it stopped pausing and started to descend. At around 20 feet it started to behave erratically, contacted the ground, slid, and then became airborne again before landing. Damage was limited to the aft landing pad. 
Here’s the student’s notes, “During a paused manual nudge, whilst correcting forward movement with the xbox controller the system seemed to override the pause at approx 20ft. Control was lost and the system began to decend in a forward motion,  landing off from the LZ by approx 10m into the scrub. Motors stopped upon landing before this was selected via GCS”
@Pat Wells @Garret Moose @matthew.curran

## Comments (12)

### Pat Wells, 2024-05-22

@Daniel Lloyd received.  Investigation underway.  Will update when information is available.

### Pat Wells, 2024-05-22

@Daniel Lloyd who is the customer for this incident?

### Daniel Lloyd, 2024-05-22

Tiquila

### Pat Wells, 2024-05-22

@Daniel Lloyd 
Could you please inspect the power contacts on the HLB and center wing side for damage or solder reflow?  Send pictures if able.

### Daniel Lloyd, 2024-05-22

The center wing power connector exhibits signs of distress. The HLB for that flight showed no signs. The resistor on the center wing connector was measured at 5.7 ohms.
@Pat Wells

### Pat Wells, 2024-05-22

@Daniel Lloyd pictures received. Passed along to investigation team.

### Daniel Lloyd, 2024-05-23

@Pat Wells could you ask if there is any concern with us using manual nudge control? I suspect that the software is OK to use.

### Pat Wells, 2024-05-23

@Daniel Lloyd currently there are no concerns with the nudge control.  They have discovered a drastic voltage drop on the HLB that may be the culprit for what was observed.  Obviously this is specific to the aircraft, not the fleet.

### Daniel Lloyd, 2024-05-23

Thanks @Pat Wells

### Daniel Lloyd, 2024-05-30

Is there any update on this investigation?
@Pat Wells

### Pat Wells, 2024-06-03

@Daniel Lloyd initial findings point to a failure of the center wing power connector.

### Christa Meck, 2026-06-16

The related incident was closed.  Closing this as well.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V538_240521_105006_pack.zip | archive | 4019 | 2024-05-21 | listed only |
| IMG_2447[1].JPG | image | 2535 | 2024-05-22 | listed only |
| IMG_2448[1].JPG | image | 2907 | 2024-05-22 | listed only |
| IMG_2449[1].JPG | image | 2766 | 2024-05-22 | listed only |
| IMG_2450[1].JPG | image | 2740 | 2024-05-22 | listed only |
