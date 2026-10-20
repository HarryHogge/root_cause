# FS2-1768: VXEP-365 Slow descent in VTOL landing

- **Issue type:** Epic
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2024-04-22
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Scott Whitney
- **Creator:** Scott Whitney
- **Labels:** sw_inReview
- **Components:** Vehicle Incident Support 
- **Fix versions:** Release 6.3.4
- **Links:** is a child of VXEP-365 (VXE 426 Slow descent on VTOL landing, crash landing into a fence)

## Description

Summary received from operator:
Last flight we had issues with the stalker going down slow and draining the battery to 12 percent and landed in a tough spot and we almost lost the aircraft. I am gonna send the video on signal. But had issues guiding the aircraft back in and when it got low it wasn't taking commands anymore and it landed in a fence. luckily we cut the engines and the AV was safely recovered with no damage"
From the logs it does seem like nudge was giving if I am reading it right, the video the VXE does seem to hover at altitude for a bit before getting locked on to its spot for landing. It takes a decent amount of time to descend before getting to a low battery and resting on the fence APX 15 meter from the landing site.

## Comments (4)

### David Grosher, 2024-08-14

@Ben Triplett @Scott Whitney I think this feature is complete with the v6.3.4 release. Ben, how was it validated by the team? That is probably relevant for 1770/1771 tasks.

### Scott Whitney, 2024-09-04

@Ben Triplett  - can you confirm that this was completed? 
@Brandon Slater - do we have test points in the regression test matrix to address the slow descent?

### David Grosher, 2024-10-31

@Scott Whitney @Ben Triplett I believe this was delivered in v6.3.4.

### Scott Whitney, 2024-10-31

@David Grosher  Yes, the work has been completed, and Gabe Z is wrapping up testing.

## Attachments (0)
