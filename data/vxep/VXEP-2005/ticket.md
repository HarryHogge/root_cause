# VXEP-2005: VXE 966 MCM reset led to uncommanded climb

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** High
- **Created:** 2026-09-21
- **Updated:** 2026-10-01
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** Hardware, RCCA, Software, Weekly-incident-tracker
- **Links:** relates to VXEP-1890 (VXE 902 - user power cycled aux 1&2 simultaneously, and lost comms with the A/C for ~2 minutes. CHAOS payload); relates to VXEP-1956 (VXE 880 MCM Reset inflight after gimbal power cycle); relates to VXEP-1315 (B30 Systemic MCM Resets due to payload power); relates to MS-1684 (VSM: Accommodate MCM Restarts in Flight)
- **Customer:** Redwire
- **Vehicle Tail Number:** XVE 966
- **Vehicle Configuration:** VXE 30 ADV NAV, OGCS 1.4.2, firmware 6.7.1, E140 MWIR
- **Plan:** https://jenaero.atlassian.net/browse/VXEP-1315
- **Issue Status:** https://jenaero.atlassian.net/browse/VXEP-1315
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Power cycled the MWIR and had a potential MCM brown out. Lost all mission elements and commanded a loiter here multiple times. Aircraft took orbit waypoint commands but had a continuous climb that was not able to be corrected with U-Drive. At 3800' ft we were able to finally command altitude down in U drive and selected land immediately around 500' AGL. Had no pause/nudge commands on descent from the controller or OGCS

This was an internal asset with purpose of flight used for high profile tv production demonstration. 
REDWIRE Stalker operators are aware of current issue of intermittent MCM reset issues caused by cycling AUX power with primary use of cycling AUX 1 one via OGCS controls to alleviate OCTOPUS gimbal issues. 

This instance was the first reported issue of uncommanded climb after issuing loiter here now at reported ‘1000ft agl’ U Drive actions of descend did not result in immediate descend and positive control of aircraft 
operators were able to verify control and descent of aircraft at approx 3800 ft AGL 

The above issue poses significant risk to operating in FAA regulated airspace and federally authorized restricted operating zones.

## Executive Summary

MCM reset caused flight safety issue resulting in climb almost outside of permitted airspace. FS team investigating to determine safety measures to be implemented in future software release

## Comments (4)

### Alexander Alan Arnold, 2026-09-21

Due to climb after MCM reset is commanding return PLZ still the safest option?
 When commanding return PLZ utilizing OGCS 1.4.2 and aircraft firmware 6.7.1 what is the aircraft logic after sending this command? 
Can the team verify that u drive commands were sent and descent was not received by aircraft? 
If commands were received why did the aircraft not descend? 
Why during the ‘link loss’ and MCM reset did the operators still maintain video and control of gimbal payload? 

@Scott Whitney @Ted Trowbridge@Eric Brewer @Everett Werner 

@David Grosher Please assign to apporpriate team member based on infromation available.  @Pat Wells FYSA

### Alexander Alan Arnold, 2026-09-21

linked VXEP 2003 due to similar behavior of link loss of aircraft but operators maintained control and receipt of video from e140

### Eric Brewer, 2026-09-22

@Alexander Alan Arnold Here’s what I see in the log:
- Link restored at xcomm time 6250 (23:44:22 UTC)
- Altitude command jumps down/up - we suspect due to reference altitude issues but unclear.  Will continue investigating this.
- At xcomm time 6541 (23:47:43 UTC), the altitude command begins decreasing - based upon vsm logs I believe it’s still in loiter mode at this point.
- 16:50:57.466049 (UTC 23:50:57):  switch to u-drive 
- XComm time 6691 (23:51:43 UTC), altitude command finally reaches aircraft altitude and aircraft begins to descend.

[embedded image-20260922-130130.png]
@Scott Whitney @Ted Trowbridge @Everett Werner @David Grosher @Craig Burton

### Eric Brewer, 2026-09-22

@Alexander Alan Arnold after discussion with Craig and Ted, we believe what happened with the high altitude command is that the loiter commands are allowed when the reference altitude is not set.  Since reference altitude was not set, the command essentially gets sent as an MSL command but gets interpreted by the autopilot as an AGL command.  In this case the MSL of the takeoff point was ~4900ft.  Guessing this waypoint was sent with 1000ft AGL intention, so that got translated to 5900ft AGL by the autopilot.

As far as we can tell the altitude command was honored once you switched to u-drive, so basic procedures for this case would be to use udrive and command altitude as needed if you need to navigate around terrain etc and then command plz when safe to do so.  Unfortunately we don’t support any mission uploads after an in-flight reset due to the reference altitude not being set.
@Ted Trowbridge @Scott Whitney @Everett Werner @David Grosher @Craig Burton

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V966_B30N_20260922T001541Z.zip | archive | 26746 | 2026-09-21 | listed only |
| image-20260922-130130.png | image | 31 | 2026-09-22 | listed only |
