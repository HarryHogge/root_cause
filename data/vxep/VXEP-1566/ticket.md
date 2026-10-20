# VXEP-1566: VXE-828 Rough Transition to VTOL

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-10-21
- **Updated:** 2026-03-02
- **Resolved:** 2026-01-21
- **Reporter:** Jackson Riley Curvin
- **Assignee:** David Grosher
- **Creator:** Jackson Riley Curvin
- **Labels:** 25thID, LRR, Weekly-incident-tracker
- **Links:** relates to VXEP-426 (VXE 489 Erratic Landing Behavior)
- **Customer:** 25thID, LRR
- **Vehicle Tail Number:** VXE-828
- **Vehicle Configuration:** Block 35X LEMB
- **Corrective Action:** None.
- **Plan:** Ensure the CAN bus integrity on landing was robust.
- **Issue Status:** Complete
- **Root Cause:** None. Aircraft behaved as expected.
- **Severity:** 4 - Annoyance

## Description

during transtion from fixed wing to VTOL aircraft appeared to be delayed causing the aircraft to drop 30 to 40 feet before fully engaging the VTOL props.

## Comments (8)

### Jackson Riley Curvin, 2025-10-21

[embedded image-20251021-230050.png]

### Jackson Riley Curvin, 2025-10-21

[embedded image-20251021-230140.png]

### Jackson Riley Curvin, 2025-10-21

@David Grosher  looks like right around transition the CNO dropped below 40 and the satellites dropped below 20 not sure if this had anything to do with it? Also winds are high.

### David Grosher, 2025-10-21

@Jackson Riley Curvin It looks like the lift motors are on but low throttle because we are actually above the target altitude. Then we have an attitude disturbance (probably due to wind) and they ramp up to stabilize the air vehicle. It looks like there is a bit of overshoot. @Eric Brewer FYSA
[embedded image-20251021-235229.png]

### David Grosher, 2026-01-14

@Eric Brewer Can you look at the CAN bus health on transition for landing? This was the vehicle that eventually crashed and this was flagged prior to that occurring.

### Eric Brewer, 2026-01-15

@David Grosher CAN looks fine. This looks like a case of the motor delay after the LR throttle was low on transition. 
[embedded image-20260115-161623.png]

### David Grosher, 2026-01-15

Linked to https://jenaero.atlassian.net/browse/VXEP-426, It may be related to that issue as there was a delay for about 0.75 seconds on one of the motors. Having said that the altitude loss appears to be expected. FYSA @Jackson Riley Curvin

### Jackson Riley Curvin, 2026-01-21

Aircraft performed as expected.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V828_20251021T214908Z.zip | archive | 17113 | 2025-10-21 | listed only |
| image-20251021-230050.png | image | 34 | 2025-10-21 | listed only |
| image-20251021-230140.png | image | 31 | 2025-10-21 | listed only |
| image-20251021-235229.png | image | 194 | 2025-10-21 | listed only |
| image-20260115-161623.png | image | 251 | 2026-01-15 | listed only |
