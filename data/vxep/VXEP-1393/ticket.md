# VXEP-1393: 2121367-01 C - Camera Cavity Harness Pinout flipped during production

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-07-08
- **Updated:** 2025-09-05
- **Resolved:** 2025-09-05
- **Reporter:** Rajesh Budhabhatti
- **Assignee:** Catherine Wagner
- **Creator:** Rajesh Budhabhatti
- **Links:** relates to VA-2802 (Duplicate 2121367-01 - Camera Cavity Harness - ADP Review redlines); relates to VA-2848 (Camera Cavity Harness pinout discrepancy (Micro-D receptacle 9 pin))
- **Start date:** 2025-07-08
- **Issue Status:** Production will rewire the camera cavity harnesses per released drawings.

## Description

QC misread the datasheet and flipped pinouts on 14 pin Picoblade connector P1.

Flipped FLIR J1 pinout view, verbally approved by Raj B. - Cam R.

## Plan

Picoblade manufacturers drawings are misleading. Make sure that harnesses are build correctly. Quarantine any existing harnesses and correct wiring.

## Comments (8)

### Rajesh Budhabhatti, 2025-07-08

previous jira task that directed the connector flip change: https://jenaero.atlassian.net/browse/VXEP-1295 
Delivered the incorrect harness to production and awaiting its return.

### Catherine Wagner, 2025-07-11

@Rajesh Budhabhatti A photo of the actual build was included to show what we were actually looking at vs. the drawing. QC is clear on reading the datasheet and the connector marking of POS 1.
Please review FLIR J1 - REAR. Red/black color code is swapped. Red should be in POS 1.
[embedded image-20250711-231932.png]

### Catherine Wagner, 2025-07-14

REV C - CAM J1 - REAR VIEW does not match supplied part.  
[embedded image-20250714-163804.png]
Note also that supplied part (DCHM9S6N5-36.0MN-HT1) is standardized color code starting with Black, so superseding that with drawing (yellow as POS 1) may cause confusion.
[embedded image-20250714-164134.png]
@Kevin Aban @Nina Menon @Rajesh Budhabhatti

### Nina Menon, 2025-07-14

@Camron Richardson @Grant Goodman another one for SA Cam cavity

### Rajesh Budhabhatti, 2025-07-14

Changed made and approved.

### Camron Richardson, 2025-07-14

@Nina Menon @Catherine Wagner Changes are made and uploaded, if you guys could review that the changes are what was requested and sign off on it here, then I can get it to Cameron C. for release. Thanks!

### Cameron Chapman, 2025-07-14

@Catherine Wagner  released. The connector is a COTS part, so I don’t think anyone could have miswired the connector, but please ensure all parts conform to the new drawing or are reworked if not and needed. 
GYI @Camron Richardson @Grant Goodman

### Rajesh Budhabhatti, 2025-07-15

Thank you Catherine,
Camron Richardson has made this correction.
Raj

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20250711-231932.png | image | 8 | 2025-07-11 | listed only |
| image-20250714-163804.png | image | 16899 | 2025-07-14 | listed only |
| image-20250714-164134.png | image | 19 | 2025-07-14 | listed only |
| image001.png | image | 0 | 2025-07-15 | listed only |
| image002.png | image | 23 | 2025-07-15 | listed only |
