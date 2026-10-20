# VXEP-1965: VXE 557 odd behavior on landing

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** Medium
- **Created:** 2026-07-16
- **Updated:** 2026-09-02
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** HLB_bad_cell, RCCA, Software, Weekly-incident-tracker
- **Customer:** SOCOM(SUMS)
- **Vehicle Tail Number:** VXE 557
- **Vehicle Configuration:** VXE 557 standard vxe , battery, trillium/jennings turret
- **Incident Type:** Other (Record"Event Type: XXXXXX" in the description)
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

“We had to pause/nudge and the aircraft took the pause command but didn’t nudge command , the motors started pulsing audibly at 20ft and abruptly dropped a little lower and kept pulsing after landing”
aircraft is still intact customer is worried about mission capability as they are currently deployed adn would like OEM clearance to operate system 
initial statement I will update as we get more info

## Executive Summary

Relayed battery was problematic to customer. cleared to fly with different battery. needs additional review to investigate nudge issue. Probable cause; Battery Issue.

## Comments (17)

### Alexander Alan Arnold, 2026-07-16

I will comb through debug and event log.

### Alexander Alan Arnold, 2026-07-16

“The pause flood from 15:54:59 onward kept the vehicle in position hold with a 10-second timer that was reset every ~300ms. The vehicle was never "un-paused" long enough for a nudge stick deflection to produce lateral movement. The operator's nudge input was reaching the vehicle, but the position hold loop from the active pause was clamping it.” is this an accurate statement?

### Alexander Alan Arnold, 2026-07-16

[embedded image-20260717-025312.png]
HLB seems to really drop during landing could this cause the nudge issues?

### Alexander Alan Arnold, 2026-07-16

https://jenaero.atlassian.net/wiki/spaces/~712020da3dae791ed54f4cb9012467656c902e/pages/1253900289/VT557+Landing+Event+Review+Pause+Flood+AP+XCOMM+Link+and+HLB+Assessment?atlOrigin=eyJpIjoiZGE0OGIyYThiODBkNDE3ODk5OTYxNzUwMjI5NjE2MjciLCJwIjoiYyJ9 please have someone review the information in the attached link to validate the pause flood as the issue. @David Grosher

### David Grosher, 2026-07-17

@Alexander Alan Arnold It would be good to overlay the plot above with the relevant events from the event log. That HLB cell drop would cause critical control issues. If nudge commands were received it may not have responded in an expected manner given that. Even if the HLB is not the cause of the missed nudge commands it is a critical issue. The HLB should be replaced. 

@Craig Burton @Ted Trowbridge Could one of you confirm that nudge commands were sent to the AP?

### Craig Burton, 2026-07-17

@David Grosher Just doing a quick scan of the available logs: was this a Jennings flight?  I do not see any MCM logs.  @Alexander Alan Arnold

### David Grosher, 2026-07-17

@Scott Lovett FYSA

### Scott Lovett, 2026-07-17

Can we get this battery shipped to HSV so it can be run through the HLB Tester?

### Alexander Alan Arnold, 2026-07-20

@Craig Burton yes this was jennings.

### Alexander Alan Arnold, 2026-08-10

equipment is overseas we will not get this battery back

### Pat Wells, 2026-08-10

@David Grosher could we get someone to look at this.

### David Grosher, 2026-08-10

@Eric Brewer Can you overlay the pauses on the HLB cell balance data to get an idea if this is causing issues with the HLBs.

### David Grosher, 2026-08-10

@Ted Trowbridge Can you look into whether the nudge commands were sent? @Eric Brewer Can you verify that nudge commands that were sent/received were acted upon by the AP?

### Ted Trowbridge, 2026-08-10

@David Grosher I can’t tell from the GCS logs whether the operator was nudging x/y, just that 10 seconds pauses were being issued continuously.
The VTOL telemetry indicates small ovrY (lateral) and ovrR (unused) inputs so it’s possible there was a very slight nudging.  I’m not sure of the units here but VTOL logged it as -0.114
@Eric Brewer

### Eric Brewer, 2026-08-10

@David Grosher pause commands began here, it looks like the voltage was pretty steady for >10s after the pauses started. 
[embedded image-20260810-210626.png]

### Eric Brewer, 2026-08-10

@Ted Trowbridge @David Grosher confirm there was nudging present. It appears that the autopilot is responding to the commands (note the position command and feedback slewing per the override inputs). The nudging begin at about 260' AGL.

[embedded image-20260810-211156.png]

### David Grosher, 2026-08-10

@Pat Wells @Alexander Alan Arnold It appears that nudging was working although the inputs were minor and that extensive pausing occurred, but I think significant imbalance on the cells was occurring prior to the pausing. Although pausing certainly wouldn’t have helped the situation.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V557_260717_003057_pack.zip | archive | 3733 | 2026-07-16 | listed only |
| image-20260717-025312.png | image | 34 | 2026-07-16 | listed only |
| image-20260810-210626.png | image | 32 | 2026-08-10 | listed only |
| image-20260810-211156.png | image | 83 | 2026-08-10 | listed only |
