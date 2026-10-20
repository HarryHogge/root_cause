# VXEP-365: VXE 426 Slow descent on VTOL landing, crash landing into a fence

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-04-17
- **Updated:** 2026-08-14
- **Resolved:** 2024-08-23
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** GNSS-Rate, MARSOC, Software, Weekly-incident-tracker
- **Links:** relates to FS2-1753 (v426 Investigation (Slow descent, land on fence)); is a parent of FS2-1768 (VXEP-365 Slow descent in VTOL landing); relates to VXEP-412 (VXE 426 Overshoot on landing, becoming progressively worse)
- **Customer:** MARSOC
- **Vehicle Tail Number:** 426
- **Corrective Action:** Software update to ignore LRF measurements made during fixed-wing flight
- **Problem Type:** Other (explain in description)
- **Incident Type:** Near Miss
- **Severity:** 1 - Flight Critical

## Description

Summary received from operator:
Last flight we had issues with the stalker going down slow and draining the battery to 12 percent and landed in a tough spot and we almost lost the aircraft. I am gonna send the video on signal. But had issues guiding the aircraft back in and when it got low it wasn't taking commands anymore and it landed in a fence. luckily we cut the engines and the AV was safely recovered with no damage"
From the logs it does seem like nudge was giving if I am reading it right, the video the VXE does seem to hover at altitude for a bit before getting locked on to its spot for landing. It takes a decent amount of time to descend before getting to a low battery and resting on the fence APX 15 meter from the landing site.

AAR attached
Video of crash attached
Vehicle Investigation VXE426 Slow Descent.pptx (It was in the linked FS2 ticket)

## Plan

- @Pat Wells can you please ask them to quarantine this aircraft and battery until we have investigated?
- Data review

## Issue Status

This issue is resolved. The problem was identified and a software fix has been implemented. The laser range finder occasionally picks up spurious range measurements during fixed wing flight and  the VTOL INS incorporates this range data into its relative altitude estimates. The software has been updated to ignore any LRF range measurements made during fixed-wing flight. 
VXE426 Slow Descent powerpoint report attached.

## Root Cause

Spurious LRF measurements made during phases of flight in which they aren’t expected and used in INS estimates for AGL altitude. The AV then thinks it is much closer to the ground than it actually is. As a result, it enters the slow descent phase of VTOL landing too soon and a very slow descent from high altitude results. The battery on the vehicle appears somewhat degraded and the charge level was not high to begin with. The slow descent resulted in battery exaustion resulting in loss of attitude control near the fence on the ground.

## Comments (4)

### Cameron Chapman, 2024-04-17

@Pat Wells can you please ask them to quarantine this aircraft and battery until we have investigated?

### Pat Wells, 2024-04-17

@Cameron Chapman I will pass along to the operators.  Note: This aircraft is at a deployed operational location and it is their only asset.  They will expect a swift resolution on the final status of the aircraft.

### David Grosher, 2024-06-13

@Ben Triplett Do we have a fix ready for the baro-offset issue that was seen here?

### Ben Triplett, 2024-06-13

@David Grosher No but I can create one. Just add a task for me, or anyone else you would like to implement the fix

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| C1190CCE-855B-48F1-BF5C-0627AB1BCE27.jpeg | image | 2570 | 2024-04-17 | listed only |
| IMG_4518.MP4 | video | 43933 | 2024-04-17 | listed only |
| T95_V426_240412_125855_pack.zip | archive | 6276 | 2024-04-17 | listed only |
