# VXEP-363: VXE 546 Loss of aircraft on landing

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2024-04-16
- **Updated:** 2026-03-02
- **Resolved:** 2025-02-11
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** FlightSystems, USASOC, Weekly-incident-tracker
- **Links:** relates to FS2-1750 (VXEP-363 Investigation (Landing Abort Issue)); relates to RMA-238 (VXE-546 240422-2 USASOC GW AC)
- **Customer:** USASOC
- **Vehicle Tail Number:** 546
- **Other Stakeholder (as required):** Pat Wells
- **Problem Type:** Other (explain in description)
- **Incident Type:** Aircraft Loss
- **Severity:** 1 - Flight Critical

## Description

From customer:
Mishap report from 7SFG(A) Stalker 546 below:
 
WHO: Legion Air; SPC Tyler Dobbins, Aircraft Operator; SPC Nicholas Delitta, Crew Chief
WHAT: Stalker 546 crash and total loss
WHEN: o/a 1416C on 13APR2024
WHERE: XXXXXXXX
WHY: Automated Landing Pattern / Rotary Lift System Fault
 
Illuminating information and timeline of events (all times in C):
 
1154: Stalker 546 takeoff for operations
1400: Stalker 546 returns to base for end of mission
1410: Stalker 546 enters automated landing pattern of IP1-IP5 (IP = initial point, a segment of the automated landing pattern)
1415: Stalker 546 enters IP5 at the loiter point encompassing the roof of B5A and C street on XXX. Stalker attempts to enter VTOL (vertical takeoff or land) mode to begin descent.
1416: Stalker 546 attempts to engage rotary propellers to begin descent. Stalker GCS (ground Control Station; laptop) notes the following anomaly: “Climb abort, lift system fault.” Aircraft enters fixed-wing mode automatically with the full propulsion of the front propeller and flies’ due WEST of the landing zone, pitched downward, and crashes with last known grid location of XXXXXXXX. Aircraft did not execute lost link protocol of emergency landing protocol.
1418: Last known grid location of XXXXXXXX passed to AOB-S Battle Captain to dispatch QRF for recovery.
o/a 1440: QRF dispatches to recover aircraft.
o/a 1507: QRF finds aircraft at XXXXXXXX.
o/a 1517: QRF recovers aircraft.
o/a 1545: QRF returns to XXX w/ recovered aircraft. Legion Air secures aircraft and begins assessment.
 
No recoverable parts.
 
NARRATIVE: The aircraft enters an automated landing pattern during which time the operator does not use controls of the aircraft. The operator will only operate during the landing sequence once the aircraft has entered VTOL mode and only to pause/nudge the aircraft at 200ft AGL and below to safely land in a landing zone. In this case, the aircraft’s automated landing pattern did not successfully transition to VTOL mode and presented the error of “Climb abort, lift system fault.” The aircraft immediately transitioned to fixed-wing mode at high speed and crashed roughly 500m W/NW of XXX proper. This is not part of the lost link protocol or emergency landing protocol.
 
ASSESSMENT / IMPACT: This was more likely system error that operator error. 
 
WAY FORWARD: Legion Air will reach back to Edge Autonomy with flight data with the express intent to correct any errors in the SkyLink software and garner a replacement aircraft and payload. Stalker VXE30 is organic to 7SFG(A); Legion Air will initiate a FLIPL w/ home station unit to assess the loss in property. Legion Air will update readiness and capabilities accordingly.

## Plan

Customer unable to recover VTOL data. Returning aircraft. Estimate 1 mo from 4/23
 @Jason Scherer can you please keep these fields updated as investigations progress, use one of the standard investigation templates as you work on investigations, save files to a shared location? https://jenaero.atlassian.net/wiki/spaces/EF/pages/23363854/Incident+Troubleshooting+and+Resolution+Tracking.

## Issue Status

From linked task: @Jason Scherer can you please keep these fields updated as investigations progress? 
Summary So Far: Although a VTOL land abort was logged and initiated due to an attitude fault, the abort was most likely not the cause of the crash. While log message timestamps are not precise due to internal system latency, the abort likely occurred after, or during, the impact.
Review of the XComm logs indicates the vehicle consumed normal lift current with non-typical sustained throttle. VTOL GPS reported 32 satellites. Battery voltages remained above limits and the hybrid lift battery had a reported 60% State of Charge (SoC) at the conclusion of the landing. The forward motor also maintained high throttle longer than typical during transition to VTOL for landing.
At the end of the XCOM data log the vehicle was in the state of waiting for proximity to the LZ. Neither the fixed wing autopilot nor the VTOL autopilot had advanced to the descension state. This means the vehicle should not have started descending.

## Comments (20)

### Sean Odell, 2024-04-16

@Pat Wells @David Grosher @Greg Fryer Files from VXE 546 uploaded to this ticket.

### David Grosher, 2024-04-17

@Pat Wells There is no VTOL data.

### Pat Wells, 2024-04-17

@David Grosher I noticed that as well.  We’ll see if they can come up with it.

### Pat Wells, 2024-04-17

@David Grosher added picture of crashed aircraft.  Should we ask them to manually pull SD card and pull data from it?

### Jason Scherer, 2024-04-18

@Pat Wells If we are able to get the VTOL logs it will help with the investigation. Thanks!

### Pat Wells, 2024-04-18

@Jason Scherer we’re working with the customer to obtain VTOL logs.  Nothing yet…

### Jason Scherer, 2024-05-09

@Pat Wells Dave mentioned there might be VTOL logs for this incident now? Is that correct? I don’t see any new attachments on this ticket.

### Pat Wells, 2024-05-09

@Jason Scherer no VTOL logs. 
Customer was unable to pull them from the damaged aircraft. 
Currently we are waiting for the aircraft to return to SLO from it’s overseas deployed location.

### Sean Odell, 2024-07-10

VXE-546 is in the process of being shipped from Erbil, Iraq. Unknown timeframe at this time. I will update the group when I have tracking or time frame. 
@David Grosher FYSA

### Alexander Alan Arnold, 2024-12-27

546 is on the way to SLO estimated delivery date is Jan 3 2025 tracking number: FOR UPS 1Z6Y3A890341420581 / 1Z6Y3A890341263993 @David Grosher

### Alexander Alan Arnold, 2025-01-10

@Rodney Linch Is this aircraft in the RMA area and if so when will it be delivered to engineering for investigation?

### Alexander Alan Arnold, 2025-01-10

@David Grosher Rodney has informed me that this aircraft has been dropped off in engineering.

### Cody Smisek, 2025-01-10

@Pat Wells  VTOL SD card is missing. Did the customer remove it? 
@David Grosher FYI

### Pat Wells, 2025-01-10

@Cody Smisek yes they did and now they can’t locate it.

### Cody Smisek, 2025-01-10

@Pat Wells Don’t think there’s anything remaining from engineering to do then. The VTOL AP board is also damaged and will not power up.

### Pat Wells, 2025-01-10

@Cody Smisek let me give the customer one more try at locating the SD card.  

@Alexander Alan Arnold FYSA

### Pat Wells, 2025-01-24

@Cody Smisek @David Grosher The customer sent me an AAR, attached.
I suspect it’s from the day prior to the mishap though based on the date.  
I didn’t want to make that determination without someone from the engineering team verifying that it is in fact the wrong set of data.

### Cody Smisek, 2025-01-25

@Pat Wells Correct, the AAR you attached was from 4/12/2024. Incident for this ticket is 4/13/2024
2 Misc. things to note. 1) The AAR from 4/12 does not contain the xcomm log for that particular flight. But it is included in the original data dump for this ticket (XCL00132). 2) During the flight on 4/12, the operator reported in ‘1:00 HR in Flight low energy window’ (as written in the gcs logbook). This is confirmed in debug log. Did a quick glance at data, unsure why that warning popped up 3 times (I believe it can be triggered by numerous checks, of which I’m not sure how to verify). Planned mission duration only shows .32 in gcs logbook, with endurance remaining 2.94. Winds aloft peaked at 24 in xcomm log. avg power ~400w at cruise alt. Looks like max range from GCS was ~2-3nm Probably unrelated to incident observed on the flight of 4/13.

### Pat Wells, 2025-01-27

@Cody Smisek @David Grosher Sam has approved a goodwill replacement for this aircraft.
Is there anything further you can do with what we have?

### Cody Smisek, 2025-01-27

@Pat Wells Please coordinate with @David Grosher. I’m unable to support any further investigation work unless tasks are reprioritized.

## Attachments (11)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| DATALOG.zip | archive | 56429 | 2024-04-16 | listed only |
| MISHAP 13APR24.PNG | image | 3374 | 2024-04-16 | listed only |
| 546 mishap.png | image | 4848 | 2024-04-17 | listed only |
| Media (26).jpg | image | 299 | 2025-01-10 | listed only |
| Media (27).jpg | image | 189 | 2025-01-10 | listed only |
| Media (28).jpg | image | 375 | 2025-01-10 | listed only |
| Media (29).jpg | image | 336 | 2025-01-10 | listed only |
| Media (30).jpg | image | 322 | 2025-01-10 | listed only |
| Media (31).jpg | image | 393 | 2025-01-10 | listed only |
| Media (32).jpg | image | 355 | 2025-01-10 | listed only |
| T95_VT546_240412_225638_vtl00102.zip | archive | 3152 | 2025-01-24 | listed only |
