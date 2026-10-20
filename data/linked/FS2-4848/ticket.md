# FS2-4848: VXEP-1929 investigation

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2026-06-30
- **Updated:** 2026-07-06
- **Resolved:** 2026-07-06
- **Reporter:** Scott Whitney
- **Assignee:** Eric Brewer
- **Creator:** Scott Whitney
- **Links:** relates to VXEP-1929 (VXE 878 - Lithuanian Border Guard Near Miss - GPS Fault)
- **Sprint:** FS2 Sprint 38

## Description

Customer has grounded fleet due to multiple flight seemingly going through to abort landings
- Vehicle aborted landing a couple time.
- Initial thoughts were jamming.
- Vtol sats and CN0 look good, but I am wondering if there are drops in Sat data going to XCOMM → FWAP or if it is just a data frequency

[embedded: image-20260701-022056.png]

## Comments (1)

### Eric Brewer, 2026-07-06

@Scott Whitney I commented in the other issue.  The CN0 and accuracies are dropping frequently which looks like either jamming or a hardware issue.  Given I saw dropouts on both fixed-wing and vtol gps I’d suspect jamming first.
Also note this is a VXE30 standard (not advanced nav).

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20260701-022056.png | image | 180 | 2026-06-30 | listed only |
