# VXEP-1925: VXE 942 VTOL GPS fault reported in Fixed, aircraft never recovered

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2026-06-21
- **Updated:** 2026-07-31
- **Resolved:** 2026-07-06
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** GS_Closed, InternalIncident, RCCA, Weekly-incident-tracker
- **Links:** relates to RMA-1074 (VXE-942 RMA 260731-1)
- **Customer:** Redwire
- **Vehicle Tail Number:** VXE 942
- **Vehicle Configuration:** VXE 30 ADV NAV OGCS E140G2 BATTERY CONFIGURATION
- **Incident Type:** Aircraft Loss
- **Severity:** 1 - Flight Critical

## Description

The AARS attached are from previous flights as we have not recovered the aircraft yet 

21 JUN winds on ground calm 12-15 at altitude from the south launch at 1958 CDT 
While in battery flight on our 4th flight of the day 942 suffered a critical failure in air. 
approx. five to ten minutes after launch The aircraft was headed west to our mission area no more than 2.5 kilometers away from our SGCS 2 antenna with good link, during the climb the aircraft displayed a VTOL GPS fault around 2000ft agl and then we immediately lost connection before we could trouble shoot the fault or command rtb. We immediately asked people in our vicinity to walk out from the tree line and conduct scans for the aircraft. After two minutes we did not see the aircraft entering the lost comms orbit or the ELZ or PLZ. After the logic timers expired, we departed the launch and recovery site and we checked out ELZ location first then headed to the last known grid of the aircraft and began searching the woods, it was low light conditions and quickly turned dark after approximately two hours of walking through the woods the OCTs asked us to return to the launch area where we remained until 2345 
When the aircraft displayed lost comms, we lost SA, Gimbal, and position data from the aircraft immediately. We refreshed the webpage to see if it was due to a caching issue like we had experienced at IVY STING and the OGCS webpage did not return. Neither the SGCS2 or SGCS1 radios displayed the aircraft node on the network. We had flown this route roughly 8 times over the course of two days with no link issues.
The behavior is similar to the CBP 864 crash, and we believe the aircraft crashed in the restricted area and are planning on continuing our search tomorrow morning. I will relay any updates as soon as I have them.  
We just got back to the hotel and plan to depart in 6 hours to get back to the box to continue searching.

## Comments (5)

### Alexander Alan Arnold, 2026-06-21

Only two issues we have seen with this aircraft was a VTOL launch abort so we moved the aircraft 30 feet restarted LW and it took off and flew no issue, second flight there was a decent “blip” that we thought was caused by a power surge for the SGCS 2 we were using, after the “blip” the aircraft flew and recovered without issue. I will provide the epsilon video when I can condense it but there appears to be substantial pitch/yaw/roll before loss of link occurs. we will work to recover aircraft tomorrow @David Grosher @Eric Brewer

### Eric Brewer, 2026-06-22

Thanks @Alexander Alan Arnold . I took a quick look through the logs we have and nothing apparent in those.  No WDT’s and GPS looks good throughout both flights.  Keep us posted when we find the aircraft and have logs and we can diagnose.

### Cody Smisek, 2026-06-22

If Silvus dropped out and was not a result of the aircraft losing line of sight with SGCS, this would indicate complete power failure on the vehicle. Power for Silvus comes from IP Comm which comes from nose current sense board.

### Scott Lovett, 2026-07-06

Aircraft crashed, never recovered.

### Scott Lovett, 2026-07-06

Aircraft lost.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V942_B30N_20260621T204522Z.zip | archive | 82177 | 2026-06-21 | listed only |
| AAR_V942_B30N_20260621T234021Z.zip | archive | 93326 | 2026-06-21 | listed only |
| pitch down for 942.jpg | image | 1185 | 2026-06-21 | listed only |
