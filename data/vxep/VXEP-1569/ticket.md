# VXEP-1569: VXE-828 Launch Abort - Air Data Fault - CAN bus error

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-10-24
- **Updated:** 2026-03-02
- **Resolved:** 2026-02-18
- **Reporter:** Jackson Riley Curvin
- **Assignee:** Eric Brewer
- **Creator:** Jackson Riley Curvin
- **Labels:** 25thID, LRR, Weekly-incident-tracker
- **Links:** relates to VXEP-1568 (VXE-818 Lift System didn't disengage - Crash - CAN bus error )
- **Customer:** 25thID, LRR
- **Vehicle Tail Number:** VXE-828
- **Vehicle Configuration:** BLOCK 35x lemb
- **Severity:** 1 - Flight Critical

## Description

As the aircraft was transitioning to fixed-wing flight, an air data fault was indicated on the OGCS. The aircraft briefly pitched down, then immediately pitched up, executed a 180-degree turn, and recovered. It returned to the launch point and landed safely.

## Comments (9)

### Drew Hildreth, 2025-10-30

@David Grosher I will have the FSR Team here start looking at the data and getting some plots dropped in for you

@Michael Mohr @Jackson Riley Curvin Dig into the AAR and see if you find anything that could be helpful for Dave and plot it.

### Jackson Riley Curvin, 2025-10-30

[embedded: image-20251030-190752.png]

### Jackson Riley Curvin, 2025-10-30

[embedded: image-20251030-190846.png]

### Jackson Riley Curvin, 2025-10-30

[embedded: image-20251030-190935.png]

### Jackson Riley Curvin, 2025-10-30

[embedded: image-20251030-192219.png]

### Jackson Riley Curvin, 2025-10-30

[embedded: image-20251030-192303.png]

### Eric Brewer, 2025-10-31

@Jackson Riley Curvin the airspeed fault was caused by a dropout of CAN messages.  From a preliminary analysis it looks like this might be related to V818.  @David Grosher FYI.

### Jackson Riley Curvin, 2025-11-04

@Eric Brewer  i received 10 more AARs from 828 and uploaded them into condor out of those 3 of them experienced CAN Drop messages I have uploaded those in the ticket

### Scott Lovett, 2026-02-18

Root cause identified. Aircraft did NOT crash, no report required.

## Attachments (9)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V828_20251024T002213Z.zip | archive | 13077 | 2025-10-24 | listed only |
| image-20251030-190752.png | image | 26 | 2025-10-30 | listed only |
| image-20251030-190846.png | image | 31 | 2025-10-30 | listed only |
| image-20251030-190935.png | image | 31 | 2025-10-30 | listed only |
| image-20251030-192219.png | image | 72 | 2025-10-30 | listed only |
| image-20251030-192303.png | image | 55 | 2025-10-30 | listed only |
| AAR_V828_20251021T021311Z.zip | archive | 15509 | 2025-11-04 | listed only |
| AAR_V828_20251021T214908Z.zip | archive | 17113 | 2025-11-04 | listed only |
| AAR_V828_20251022T195833Z.zip | archive | 23669 | 2025-11-04 | listed only |
