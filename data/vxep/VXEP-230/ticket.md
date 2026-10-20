# VXEP-230: Tail 499 crash during VTOL landing from 10-15', system disarm/re-arm and launch post-crash. NCR 1787

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-12-18
- **Updated:** 2024-08-23
- **Resolved:** 2024-08-23
- **Reporter:** Greg Fryer
- **Assignee:** David Grosher
- **Creator:** Greg Fryer
- **Labels:** VTOL-AP-WD
- **Links:** relates to VXEP-41 (TPTR-74 VXE 510: (VTOL AP WD) Consolidated Watch Dog tracking); relates to VXEP-11 (TPTR-5 VXE 407: (VTOL-AP-WD) Unexpected Behavior Seen During Vertical Landing)
- **Corrective Action:** - Embedded SW Robustness Initiative
- **Root Cause:** WDT incident
- **Severity:** 1 - Flight Critical

## Description

NCR List - VXE499 - SCO - Lift System Failure Causing Mishap (sharepoint.com)

## Plan

Link the WD investigation. 
Dave to determine plan for the hardware. NCR: “the VTOL AP should be red-tagged and replaced.” Asked Dave if he would like any additional hardware from this vehicle. 
Install and label hardware into HIL for additional testing.

## Issue Status

This was a WDT event and we have included it along with our wider investigation. We have data to suggest that when these events happen there tend to be repeated events on the same hardware, given that the VTOL AP should be red-tagged and replaced.

## Comments (4)

### Greg Fryer, 2023-12-18

@David Grosher Need someone assigned to look at the logs in the listed NCR from ~Nov 1. It’s sure acting like a WD reset or similar (the whole crash/re-arm/takeoff patter).

### Cameron Chapman, 2023-12-19

Notes from Dave on phone call. Was a WD timer. Folded into that investigation. Surprisingly similar to 407. We should link to that investigation. 
Dave to determine plan for the hardware. NCR: “the VTOL AP should be red-tagged and replaced.” Asked Dave if he would like any additional hardware from this vehicle.

### Matt Philley, 2024-02-12

@David Grosher @Cameron Chapman @Greg Fryer FYSA due to AEWE crash this AC 499 ASSET is being pushed through repair in order to be shipped out to AEWE. It does not look like this investigation is fully closed and there was no response if more components are needing replacement. 
Current repair plan is as follows, please confirm we believe this repair to make this AC safe to fly again… it looks like the result of the investigation was that it was a WD issue so not hardware related beyond the Avionics Board Assy…? 
Scope of repair: 
-FUSE: Replace Aft Landing Pad PN: 965-1-01-1044 (QTY 1)
-FUSE: NOTE- Minor chips around battery entrance and payload, no action required. (QTY 1)
-FUSE: Repair Avionics Box Mount Holes with Wet Layup
-Center wing: VTOL Avionics Assembly PN: 107-101161 (QTY 1)
-Center Wing: Note - Slight wrinkle on underside, near the "Cable Access" seal. No action required at this time. (Qty 1)
-Wing Tip Assembly, RIGHT PN: 107-100459-R (QTY 1)
-SCO and Flight Test (QTY 1)
-Replace Tail Boom Assy 
@Kyle DeBernardi @Kyle England @Artis Bertulis @Ruysser Gabler @Carson Buckley FYSA

### Matt Philley, 2024-02-13

Closing NCR based on comment in NCR from Dave G. AC will be shipped for use at AEWE

## Attachments (0)
