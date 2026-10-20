# VXEP-1563: New ADP SA camera flares

- **Issue type:** Problem
- **Status:** Assigned
- **Priority:** High
- **Created:** 2025-10-21
- **Updated:** 2026-01-15
- **Reporter:** Artis Bertulis
- **Assignee:** Kurt Burian
- **Creator:** Artis Bertulis
- **Links:** relates to FS2-3868 (Investigate: SA camera flares); relates to XKIT-5226 (SA CAM turned green and was unusable during VTOL landing); relates to XKIT-5113 (B40 Non Flight-blocker flight test issue collector/Squawk List)

## Description

The new ADP SA camera exhibits noticeable red flares when flying toward the sun. Please see the image below, and I’ve also attached several videos for reference.
[embedded: SA Flare-20251021-192856.png]
While the flare is brief, it’s visually disruptive and can be quite distracting for the operator. This issue has been consistently observed across multiple new vehicles equipped with the latest ADP system - it’s not isolated to a specific unit or platform. The attached videos were selected from different vehicles on various days, highlighting how frequently this occurs.
Although the issue was previously reported via an NCR, the follow-up investigation was minimal and did not result in any significant action. For further details, please refer to the NCR documentation - AC 567 - Flight Test - SA camera flash 

I’d appreciate it if this issue could be investigated further, as I anticipate it may lead to customer complaints in the near future. Below are snippets from several videos capturing the flare occurrence - there are many more available if needed.
This behavior appears only when the vehicle is facing the sun, so on clear, sunny days, it can affect approximately 20–30% of the flight duration when operating in an orbit.

The first video is one of the worst ones:
[embedded: one of the worst ones.ts]
[embedded: vlc-record-2025-10-21-12h25m12s-MISB-10212025-120133-0.mpg-.ts]
[embedded: vlc-record-2025-10-21-12h25m53s-MISB-10212025-120133-0.mpg-.ts]
[embedded: vlc-record-2025-10-21-12h26m38s-MISB-10172025-110007-1-0.mpg-.ts]
[embedded: vlc-record-2025-10-21-12h27m46s-MISB-10172025-104455-0.mpg-.ts]
[embedded: vlc-record-2025-10-21-12h28m16s-MISB-10172025-104455-0.mpg-.ts]
[embedded: vlc-record-2025-10-21-12h29m17s-MISB-10172025-104455-0.mpg-.ts]
[embedded: vlc-record-2025-10-21-12h31m04s-MISB-10212025-104046-0.mpg-.ts]
[embedded: vlc-record-2025-10-21-12h31m41s-MISB-10212025-104046-0.mpg-.ts]
[embedded: vlc-record-2025-10-21-12h33m49s-MISB-10212025-104046-0.mpg-.ts]
[embedded: vlc-record-2025-10-21-12h35m33s-MISB-10212025-120133-0.mpg-.ts]

## Plan

Not-MVP. Linked dropout issue likely is. Same plan for both. 
- Need to identify an alternate ADP/SA camera setup to test. @Rajesh Budhabhatti  can you please status this.
- Test new FW and settings from sightline.

## Issue Status

Occurred again on B40 flight 11/26 Flight 2 - 65lb AFT
Teams chat Cody Smisek: will pull ESC logs and CAN data | B40 Flight Test Chat | Microsoft Teams

## Comments (6)

### Artis Bertulis, 2025-10-21

@Grant Goodman @Greg Fryer @Scott Stuckey Not sure if this is the right avenue for reporting this, but please move, transfer, or report as required. I’m happy to assist in any way.

@Wes Bracken @Ruysser Gabler @Carson Buckley for awareness

### Greg Fryer, 2025-10-23

@Grant Goodman moved this to @Scott Whitney just like the other SA cam item. Like other camera issues in VBN, likely needs a combo team

### Scott Whitney, 2025-10-23

FYSA @Kurt Burian

### Kurt Burian, 2025-10-23

@Scott Whitney @Grant Goodman This is going to be an issue with the gains/config of the Dual SA SLA1750 encoder. We can play with values and likely make this go away, but we will need to come up with a way to simulate in the shop or do some tuning during flight test.

### Cameron Chapman, 2025-12-01

After 12/1 flight test 
[embedded: image-20251201-231227.png]

### Kurt Burian, 2025-12-08

Information regarding turning green added to other ticket, dont think its flare related.

## Attachments (13)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| SA Flare-20251021-192856.png | image | 339 | 2025-10-21 | listed only |
| one of the worst ones.ts | video | 2507 | 2025-10-21 | listed only |
| vlc-record-2025-10-21-12h25m12s-MISB-10212025-120133-0.mpg-.ts | video | 4020 | 2025-10-21 | listed only |
| vlc-record-2025-10-21-12h25m53s-MISB-10212025-120133-0.mpg-.ts | video | 4656 | 2025-10-21 | listed only |
| vlc-record-2025-10-21-12h26m38s-MISB-10172025-110007-1-0.mpg-.ts | video | 1566 | 2025-10-21 | listed only |
| vlc-record-2025-10-21-12h27m46s-MISB-10172025-104455-0.mpg-.ts | video | 4751 | 2025-10-21 | listed only |
| vlc-record-2025-10-21-12h28m16s-MISB-10172025-104455-0.mpg-.ts | video | 2538 | 2025-10-21 | listed only |
| vlc-record-2025-10-21-12h29m17s-MISB-10172025-104455-0.mpg-.ts | video | 6503 | 2025-10-21 | listed only |
| vlc-record-2025-10-21-12h31m04s-MISB-10212025-104046-0.mpg-.ts | video | 1837 | 2025-10-21 | listed only |
| vlc-record-2025-10-21-12h31m41s-MISB-10212025-104046-0.mpg-.ts | video | 5344 | 2025-10-21 | listed only |
| vlc-record-2025-10-21-12h33m49s-MISB-10212025-104046-0.mpg-.ts | video | 6317 | 2025-10-21 | listed only |
| vlc-record-2025-10-21-12h35m33s-MISB-10212025-120133-0.mpg-.ts | video | 5757 | 2025-10-21 | listed only |
| image-20251201-231227.png | image | 135 | 2025-12-01 | listed only |
