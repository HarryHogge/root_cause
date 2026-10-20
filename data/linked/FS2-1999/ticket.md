# FS2-1999: Implement Fixed wing Helper Fix

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2024-06-21
- **Updated:** 2025-02-18
- **Resolved:** 2025-02-18
- **Reporter:** Everett Werner
- **Assignee:** Everett Werner
- **Creator:** Everett Werner
- **Labels:** sw_inReview
- **Parent:** FS2-1862 VXEP-315 Landing Performance Improvements
- **Links:** relates to VXEP-315 (VXE 459 Overshoot of LZ Mishap on landing, operator unable to nudge)
- **Epic Link:** FS2-1862

## Description

Move fixed wing helper activation function in VTOL to only kick in after transition has completed. Currently comes in during transition when landing into a headwind and pulls it along.

## Sprint

FS2 Sprint 20, FS2 Sprint 27, FS2 Sprint 24, FS2 Sprint 30, FS2 Sprint 21, FS2 Sprint 22, FS2 Sprint 23, FS2 Sprint 28, FS2 Sprint 25, FS2 Sprint 26, FS2 Sprint 29

## Comments (3)

### Everett Werner, 2024-06-21

[embedded: image-20240621-183552.png]
Before

### Everett Werner, 2024-06-21

[embedded: image-20240621-183627.png]
After

### Everett Werner, 2024-06-21

[embedded: image-20240621-184756.png]
in the mc update function if the function returns false it turns off the fw helper

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240621-183552.png | image | 62 | 2024-06-21 | listed only |
| image-20240621-183627.png | image | 66 | 2024-06-21 | listed only |
| image-20240621-184756.png | image | 44 | 2024-06-21 | listed only |
