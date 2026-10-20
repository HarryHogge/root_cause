# VXEP-1774: VXE-933 During launch wizard, Error pops up saying "The autopilot has detected that one or more of its sensors have failed"

- **Issue type:** Incident (8D)
- **Status:** D6 - Verifying Corrective Actions Are Complete
- **Priority:** Low
- **Created:** 2026-03-16
- **Updated:** 2026-10-12
- **Reporter:** Zachary Mann
- **Assignee:** David Grosher
- **Creator:** Michael Mohr
- **Labels:** GS_Closed, RCCA, Software, Weekly-incident-tracker
- **Links:** relates to VXEP-1547 (VXE 930 One or more VTOL Sensor fail); relates to VXEP-1989 (VXE 932 Crash)
- **Customer:** MOLSON
- **Vehicle Tail Number:** VXE-933
- **Corrective Action:** heading issue addressed in 6.7.1
- **Root Cause:** SW issues in 6.6.1 will be addressed in 6.7.1
- **Incident Type:** Mission Failure/Abort
- **Severity:** 4 - Annoyance
- **Executive Summary:** Awaiting 6.7.1 software release. Probable cause Software.

## Description

From customer. “That is the same one we got a couple weeks ago”. Assuming they mean aircraft 930. 
Sam Miller gave them some things to look at and try:
- Point the vehicle north using an external compass to validate, open the Tools>Instrument panel and verify that the yaw at the bottom of the window matches within 15 degrees and is not drifting. Then repeat for east, south, and west. If you’re seeing a difference of more than 15 degrees or drifting at any of the ordinals, then try restarting the launch wiz to reset the AP. If that doesn’t work cycle power on the vehicle.  If that doesn’t work, mag cal the airplane for that location and see if it resolves the issue.
- After trying number 1 above, when you’re in the Launch Wizard shield pitot window, open Tools>Debug. Does it say Sensor Health=1? If not, try rotating the vehicle to align North and see if it =1. If it =0, then repeat for east, south, west to see if any of the ordinals results in sensor health =1.
- What are the number and CnO of GPS satellites? (Tools>GPS Satellite Status>GSV on). If low CnO or # of sats, IMU can get confused.

Linking to VXE930 ticket

## Vehicle Configuration

VXE30
AdvNav

## Comments (8)

### David Grosher, 2026-03-16

@Michael Mohr Were they able to get past the error given Sam’s troubleshooting advice?

### Michael Mohr, 2026-03-17

@David Grosher It doesn’t sound like they really even tried it unfortunately. They said they would try the ideas after “March Break”

### Eric Brewer, 2026-05-05

@David Grosher @Michael Mohr can we close this one out? There is a software update 6.7.1 soon which should resolve the heading issue.

### Pat Wells, 2026-08-11

Awaiting release of 6.7.1 software to close this out.  8/11/2026

### Cody Smisek, 2026-09-23

Would suggest a second review of this issue reference findings of https://jenaero.atlassian.net/browse/VXEP-1989 


AAR in this ticket (1774) shows similar characteristics of 1989. Abnormal airspeed indications preflight and during launch. 
[embedded: image-20260923-151314.png]

### Zachary Mann, 2026-10-12

@Eric Brewer Can you review Codys assessment to see if this is actually able to be closed? Please let me know if there is anything that you need from me. Thank you.

### Eric Brewer, 2026-10-12

@Cody Smisek thanks - yes looks like these two airplanes were mixing/matching center wings and fuselages.  @Zachary Mann it looks like the 933 center wing was destroyed in the crash.
The VTOL sensor faults popup causes quite a bit of confusion and in this case a dangerous situation where operators ignored the failures and kept trying to click through the LW.  
OGCS provides a lot more insight into where the errors are coming from and also has readouts of the airspeed measurements over time which might have helped to debug this issue.
Given the aircraft has since had an incident I’m not sure what that means for the disposition of this ticket.

### Alexander Alan Arnold, 2026-10-12

@Eric Brewer I guess once the root cause for the crash of 932 is determined we can revisit this one?

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 822ece6f7531e4b500e14e1b34d5ecf8f979a2c6124b8838043acf78abdd9561.jpg | image | 509 | 2026-03-16 | listed only |
| T115_V933_260310_091558_pack.zip | archive | 1988 | 2026-03-16 | listed only |
| image-20260923-151314.png | image | 113 | 2026-09-23 | listed only |
