# VXEP-1699: VXE 897 Incident on landing

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2026-02-11
- **Updated:** 2026-04-16
- **Resolved:** 2026-02-20
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** RCCA, USSS, Weekly-incident-tracker
- **Links:** relates to RMA-918 (VXE-897 RMA 260206-1)
- **Customer:** USSS
- **Vehicle Tail Number:** 897
- **Vehicle Configuration:** ADV NAV, SUAV, Battery, Octopus gimbal
- **Corrective Action:** None.
- **Issue Status:** Complete
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

2026-01-22Is the date of the incident but we did not create the VXEP until data was provided. 
VXE 897 experienced issues upon landing *Awaiting Operator Statement*

Report: [embedded file]

## Plan

Investigate claim that aircraft was not behaving correctly during flight to ensure initial root cause claim that operator error is cause of incident.

## Root Cause

After interviews with the operators and a thorough review of the data, it has been determined that the ultimate root cause of the incident was an uncontrolled decent as a result of battery exhaustion. However, the events leading up to the battery exhaustion are equally responsible for the overall incident. 
At some point during the flight, the operator selected “Land Now” instead of “Return to Base (RTB)”. When the operator noticed the landing area was not clear of obstacles, they paused the landing sequence and attempted to nudge the aircraft to a position where it was safe to continue the descent. The operator spent almost two minutes in VTOL attempting to correct landing location but were possibly using the micro-nudge feature which was not effective in moving the aircraft far enough to avoid the ground obstacles. During the continued attempts to move the aircraft, the main battery became exhausted from the station keeping (hover) activity, at which point the aircraft could no longer maintain lift and crashed to the ground vertically, partially impacting a vehicle directly beneath it.
No faults found prior to Land Immediately (addressing comment of odd behavior), but no GCS log available to verify completely. The chain of events initiated with the user selecting land now instead of RTB. It is unsure if that action was intentional, however the action to pause the landing sequence was deliberate, and the ensuing attempt to move the aircraft with the wrong commands while in stationary VTOL was a human induced error, leading to battery exhaustion.

## Comments (14)

### Jackson Riley Curvin, 2026-02-12

[embedded image-20260212-164104.png]

### Jackson Riley Curvin, 2026-02-12

[embedded image-20260212-164457.png]

### Alexander Alan Arnold, 2026-02-12

[embedded image (4).png]

### Alexander Alan Arnold, 2026-02-12

@Scott Lovett Weve gotten some data from this incident loaded, currently working to get the rest of the logs attached.

### Jackson Riley Curvin, 2026-02-12

[embedded image-20260212-172041.png]

### Alexander Alan Arnold, 2026-02-12

@David Grosher We got the AV in house currently in the RMA area I believe. Cody helped us comb through some of the logs. The Operators did not create an AAR after the incident, so we loaded everything from the aircraft in the ticket.  We assume Operator error based on the land now command rather than an RTB command and just need to ensure the aircraft was functioning correctly up until the land now command.

### David Grosher, 2026-02-12

@Alexander Alan Arnold - Land Now was commanded from the GCS. It would try to land where it is at along with any nudges that it receives. Note: extensive pauses could result in the lift system overheating. This is an emergency procedure that should only be used if the aircraft can’t otherwise be recovered. 
[embedded image-20260212-183744.png]

### Alexander Alan Arnold, 2026-02-12

Thank you Dave! @David Grosher

### Greg Fryer, 2026-02-13

@Alexander Alan Arnold If you’re good with the info, can you move this to closed? I’m not sure it’s clear who all should do it, but the lingering tickets are cluttering up any reports.

### Jackson Riley Curvin, 2026-02-13

@Greg Fryer in the operator statement they mentioned that something strange happened before they hit land now, we just need someone to verify that there were no anomalies prior.

### Jeremy White, 2026-02-20

@Greg Fryer Where are we on this status? USSS needs feedback ASAP so we can get work started and back to them.

### Greg Fryer, 2026-02-20

@Jeremy White @Jackson Riley Curvin @Alexander Alan Arnold 
Messaged @David Grosher on Teams, to have whoever looked at the logs just tell us “no faults logged prior to Land Immediately event” Usually that is understood (would have said if there was a fault).

### David Grosher, 2026-02-20

@Jackson Riley Curvin Where is the operator statement?

### Greg Fryer, 2026-02-20

@Jeremy White @Jackson Riley Curvin @Alexander Alan Arnold See closure comment, I verified with Dave there were no faults in the info/logs we have prior to the Land Immediately command.

## Attachments (12)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 897 data.zip | archive | 1024 | 2026-02-12 | listed only |
| Image (47).jpg | image | 2744 | 2026-02-12 | listed only |
| Image (48).jpg | image | 2571 | 2026-02-12 | listed only |
| T115_V897_260211_135811_pack.zip | archive | 2974 | 2026-02-12 | listed only |
| VTOL_VXE897.zip | archive | 46475 | 2026-02-12 | listed only |
| XCOMM_VXE897.zip | archive | 12300 | 2026-02-12 | listed only |
| image (4).png | image | 121 | 2026-02-12 | listed only |
| image-20260212-164104.png | image | 89 | 2026-02-12 | listed only |
| image-20260212-164457.png | image | 117 | 2026-02-12 | listed only |
| image-20260212-172041.png | image | 91 | 2026-02-12 | listed only |
| image-20260212-183744.png | image | 25 | 2026-02-12 | listed only |
| [VXEP-1699.pptx](attachments/53810_VXEP-1699.pptx.md) | pptx | 526 | 2026-04-16 | converted |
