# VXEP-431: VXE 558 drift on landing and crash

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-06-10
- **Updated:** 2026-03-02
- **Resolved:** 2024-08-23
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** GNSS-Rate, USASOC, Weekly-incident-tracker
- **Links:** relates to RMA-275 (RMA 061724 VXE-558 Goodwill - Replaced with 694)
- **Customer:** USASOC
- **Vehicle Tail Number:** 558
- **Plan:** Run HIL test to determine if errors are annunciated to the user.
- **Issue Status:** Investigating
- **Root Cause:** GPS loss during approach results in wings level command and vehicle descent.
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

Report received from customer 7th Grp: 
Preflight: Aircraft was powered on and connected without issue. GPS location of AV and GCS were accurate using 12 satellites. Initial temperature of VTOL battery was yellow. Once prop test and VTOL motor test were completed, battery warmed and was verified green. Airspeed test read 90 and returned to zero as normal.
 
Initial Takeoff and Climb:
Launch was smooth and VTOL ascent was stable. Transitioned to fixed wing at ~200ft AGL and proceeded to the first orbit, climbing in route to 600ft AGL.
 
Flight: No anomalies present. GPS and Link remained stable.
 
Landing:
AV entered IP1 at 600ft AGL. AV entered IP2 began descent to recovery/transition altitude, exited at IP3 and moved to IP4 to start final recovery steps. AV entered IP5 (at this point, abort is unavailable) and proceeded to the PLZ. “Transition to VTOL” was displayed in VTOL System Menu (right side of screen) while CC verified VTOL motors on. Following the transition to VTOL, “Climb Abort, Lift System Fault” in the VTOL System Menu. AV continued to fly past the PLZ by ~80m while in VTOL. AV began descent while correcting it’s position flying backwards (AV heading was 0 degrees while moving Southeast). Once the AV was above the desired landing point, CC called for a “Pause.” The pause button was pressed and manual correction was attempted. The AV was now at ~50 ft drifting past the PLZ in the opposite direction until AV crashed.
 
 
After looking at the components, the following parts are damaged:
HD55 – EO Lens loose, IR lens cracked, payload housing dented, servos grinding
Nose Cone – Dented and cracked
Right Lift Boom – front lift propeller broken, rear lift propeller scratched, lift boom scratched
Left Lift Boom – front lift propeller broken, rear lift propeller scratched, lift boom scratched, lift boom teeter joint area cracked/broken
Rear Landing Pad – Missing
Rutter – Scratched
Wing Mount Bolts – all 4, broken and stuck in fuselage threads
Fuselage – cracked near payload opening
 
AAR attached

## Corrective Action

Avoid GPS loss during approach.
Run HIL test to determine if any errors are annunciated to the operator.

## Comments (10)

### David Grosher, 2024-06-11

@Eric Brewer Can you look into this? 
@Scott Whitney FYI

### Pat Wells, 2024-06-12

@David Grosher @Eric Brewer is anyone able to look at this. 
Aircraft belongs to deployed USASOC customer and we really should get something for them in terms of where we are at with the investigation.
Thanks

### Eric Brewer, 2024-06-12

@Pat Wells @David Grosher See summary slides here.  It looks like GPS dropped out on approach.  In that case the vehicle goes to pitch/roll level and descends, so unfortunately this is expected system behavior in the event of GPS loss during approach.

### Pat Wells, 2024-06-12

@Eric Brewer @David Grosher thanks for quick turnaround on this one. 
Are there any work arounds that the operator can or could have performed in this scenario?  I would like to offer them this information as well if there is something they can do if this happens again.

### Eric Brewer, 2024-06-12

@Pat Wells @David Grosher I talked briefly with @Cody Smisek , in the case of GPS outage a manual nudge mode landing would be required.  See section 4.5 of the user’s manual.
Note: in addition to the “!DR!” alert, a GPS outage could also be indicated by:
GPS has been lost for more than %d seconds.\r\nThe vehicle will now attempt to dead reckon and land automatically at the designated LZ.\r\nYou may activate U-drive mode at any time to override control of the vehicle
One thing I’m unclear on - I’m not positive if the operator would have an indication if the fixed-wing GPS still had a fix but the VTOL GPS did not.  I could use some help from someone more familiar with the GCS code, on a quick look I couldn’t see anywhere it looked at VTOL GPS specifically (or OR’d together fixed-wing and vtol).

### David Grosher, 2024-06-12

@Eric Brewer You should ask @Kurt Burian and @Michael Berger regarding the behavior. I think the GCS GPS data only comes from one of the receivers. It used to be the FW, but I think with the last release some (or all) of the data is now provided from the VTOL.

### Eric Brewer, 2024-06-13

Thanks.  We believe that a GPS loss should get annunciated through the VT_FAULT_FAIL_VT status, and should display a sensor error, but I didn’t see that in xcomm or on the GCS display, and the operators note above that there were no errors or cautions related to GPS.
@David Grosher , Cody looked through the Tiquila test logs and it doesn’t look like we tested a case there where the VTOL GPS was failed but fixed-wing wasn’t.  It may be worth testing this in the HIL to see if we annunciate anything to the operator.  In this particular case, the GPS wasn’t completely failed, it just had some of the uncertainty checks fail.  In that case VTOL won’t use the GPS, and this should have been annunciated to the operators.  Let me know who you’d recommend to run this test, I suspect we need to run it on a HIL that has real GPS receivers

### David Grosher, 2024-06-13

@Eric Brewer I think an iron bird run would be what you need to test. Although I’m not sure if error reporting would change as a function of flight phase, if so then we would need to wait for speedgoat. Regardless, I think knowing what the operators would see is worthwhile.

### Pat Wells, 2024-06-17

@David Grosher @Eric Brewer I see that the GNSS Rate label has been added to this incident.
Where are we at with messaging to the customer at this point?  I have not sent them anything yet based on Dave’s comment on an email stating that this is still an ongoing investigation.

### Eric Brewer, 2024-06-17

@David Grosher please confirm, but I believe the current plan is that we will release a patch for the GNSS rate issue, followed by a more permanent fix in 6.3.x.  I do not know what we’ve communicated on timeline. @Pat Wells

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V558_240608_195519_01_pack.zip | archive | 8013 | 2024-06-10 | listed only |
