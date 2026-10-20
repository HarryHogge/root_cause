# VXEP-1294: VXE-596 "Loss of Control Shutdown."

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Not Verifiable
- **Priority:** Highest
- **Created:** 2025-06-06
- **Updated:** 2026-08-14
- **Resolved:** 2026-02-18
- **Reporter:** Jackson Riley Curvin
- **Assignee:** Jacob Troyer
- **Creator:** Jackson Riley Curvin
- **Labels:** Hardware, PMA263, RCCA, Weekly-incident-tracker
- **Customer:** PMA263
- **Vehicle Tail Number:** VXE-596
- **Vehicle Configuration:** VXE Standard Configuration
- **Root Cause:** Connection to CW appears lost. Need more updates
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

From Olivia Douglass via text: AC 596
After flight operation was complete, tail 596 was commanded to RTB. AV was experiencing a headwind during IP2 orbit. Headwind subsided and AV finished routing to PLZ. AV was approximately 150' above the ground and experienced an error "Loss of Control Shutdown." This resulted in the AV VTOL props cutting off immediately and dropping nose first into the PLZ.
 
Front prop/PDU - crushed into Fuselage, fuselage - nose crushed; front right lift boom - tip crushed; front vtol props - broken carbon fiber support rods, payload - servo broken (no damage to HD40 indicated)
 
Interesting tidbit "prior launch had VTOL props issue, abort launch, and conducted pre-flight checks again."
PowerPoint here. VXE-596LossOfControl
File locations here: Flight Safety - VXE596LossOfControlShutdown - All Documents

## Plan

see VXE-596LossOfControl
- Responding to the email chain via teams (usually faster). It seems like a likely failure of front left ESC. Where is the ESC and HW currently? discussing here. Cameron Chapman: Responding to the email chain via teams (usually faster). It seem... | VXE-596 / VXEP-1294 | Microsoft Teams

## Comments (18)

### David Grosher, 2025-06-06

UPDATED: 

It appears that the VTOL AP, SA camera and airdata board were lost at 9126 XCOMM CpuTime. This happened after 6 sequential VTOL pauses by the operator. The VTOL appears to have cut and safed the motors 1 second prior to that (although there is no mention of it in the event logs). Pitch diverges at XCOMM CpuTime 9123. Note, the vtIBatt drops to 5 amps despite having throttle settings for 2 motors above 50 %. We should explore a heat related failure of the ESCs, Battery Failure, Connector Failure, U11 on XCOMM, or any other systemic issue that can bring down the CW systems. @Jason Scherer @Cameron Chapman @Connor Peebles @Steve Gonzales

### David Grosher, 2025-06-06

@Eric Brewer This seems unrelated to the issue in this incident, but in the video there is no roll divergence only a pitch divergence when it noses down and flips over. I wonder if there is an instability in the nav filters numerical calculations at these extreme attitudes. This is probably not a high priority to track down.

### Eric Brewer, 2025-06-06

@David Grosher this signature looks similar to other incidents where vtol shuts down, I think that’s just how the vehicle falls when all the motors are off.

### Jason Scherer, 2025-06-06

Logs indicate that no SAFE commands were sent to VTOL which typically happen after loss of stability due to ATT fault.
However, after a few pauses during the landing, the XComm log shows Fixed Wing reporting an airspeed fault then the CW network link goes down. (9126-9127 XComm CPU time)
[embedded image-20250606-161410.png]
Fixed Wing altitude at the time shows 120'
[embedded image-20250606-161102.png]
VTOL Rel Altitude shows ~40' at the time, then flat lines.
[embedded image-20250606-161244.png]
VTOL LRF does not appear to be functional during landing. 
[embedded image-20250606-161751.png]
Zoomed during landing
[embedded image-20250606-161814.png]
Zoomed out and showing max value
[embedded image-20250606-161832.png]
However, the LRF did seem to be working during launch. 
[embedded image-20250606-161935.png]

### Jason Scherer, 2025-06-06

@David Grosher @Eric Brewer Based on the above it seems like we lost CW before impact, but it’s hard to say for sure.

### Jason Scherer, 2025-06-06

VTOL Throttles during landing from VTOL Log
[embedded image-20250606-163502.png]
[embedded image-20250606-163830.png]
[embedded image-20250606-165009.png]
[embedded image-20250606-164214.png]
[embedded image-20250606-164450.png]

### Jason Scherer, 2025-06-06

@David Grosher @Eric Brewer Based on the above, it seems like the VTOL logs show throttles and typical current draw until the end of the log. The log shows ~155' AGL (baro data) at the very end of the log. The logs do not show re-SAFEing of the PWM lines.

### Jason Scherer, 2025-06-06

@Connor Peebles What do you make of the large voltage drop right before 8965? Is this typical of a landing?

### Jason Scherer, 2025-06-06

@Eric Brewer  I do see some divergence in VTOL throttles at the end which is also reflected in a divergence of boom current. Does this make sense based on attitude data? Seems odd that it would diverge at the end after stabilizing unless maybe a gust of wind showed up.

### Jason Scherer, 2025-06-06

From XComm data log we see CW network goes down at XComm CPU time 9126. The CAN Air times out at 9127 and the VTOL CAN data times out at 9128. For CAN links, these are 1 second timeouts, so the drop would be 1 second before the timeout is reported.
Based on this we can assume:
- XComm network link to CW drops at 9126
- Can air reports stop at 9126
- VTOL can message stop a 9127

[embedded image-20250606-171019.png]
[embedded image-20250606-173403.png]
It looks like the last HLB BMS can data update occurred at 9125.178. It’s a little hard to tell since the BMS data doesn’t change much, but there is no value differences in BMS data after 9125.178.
[embedded image-20250606-172251.png]

### Connor Peebles, 2025-06-06

@Jason Scherer Look at the current to the booms at the same timestamp. It is either a measuring mistake or a sudden increase in current (power shorted or crazy take off power). 
P.S. seeing that you posted Ibatt 1 and 2 above it haha. Yeah I would say that tracks with the dramatic increase in vtol power.

### Jason Scherer, 2025-06-06

@Eric Brewer What XComm time does it look like impact occurred due to IMU data?

### Eric Brewer, 2025-06-06

@Jason Scherer it looks like about 9126.  That’s when I see AGL go to zero, vertspeed decreases quickly etc.

[embedded image-20250606-180628.png]

### Eric Brewer, 2025-06-06

@Jason Scherer uploaded and linked a template above, we can start populating the figures you’re generating there.

### Jason Scherer, 2025-06-19

XComm shows throttles during shutdown, but VTOL data stops just before the throttles go wonky. 

Top is VTOL, Bottom is XComm.
[embedded image-20250620-003645.png]

### Jackson Riley Curvin, 2025-09-16

@Jason Scherer was this ever confirmed to be a bug in the code?

### Scott Lovett, 2026-02-02

@Jacob Troyer reviving this older investigation to drive to closure. Has there been any updates or discoveries? 
I am adding this to the Tues Meeting agenda.

### Scott Lovett, 2026-02-18

Never received HW from customer. Unable to proceed further.

## Attachments (19)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR 20250408.zip | archive | 9312 | 2025-06-06 | listed only |
| MicrosoftTeams-video (2).mp4 | video | 806 | 2025-06-06 | listed only |
| image-20250606-161102.png | image | 6 | 2025-06-06 | listed only |
| image-20250606-161244.png | image | 6 | 2025-06-06 | listed only |
| image-20250606-161410.png | image | 92 | 2025-06-06 | listed only |
| image-20250606-161751.png | image | 4 | 2025-06-06 | listed only |
| image-20250606-161814.png | image | 4 | 2025-06-06 | listed only |
| image-20250606-161832.png | image | 4 | 2025-06-06 | listed only |
| image-20250606-161935.png | image | 6 | 2025-06-06 | listed only |
| image-20250606-163502.png | image | 253 | 2025-06-06 | listed only |
| image-20250606-163830.png | image | 60 | 2025-06-06 | listed only |
| image-20250606-164214.png | image | 8 | 2025-06-06 | listed only |
| image-20250606-164450.png | image | 10 | 2025-06-06 | listed only |
| image-20250606-165009.png | image | 20 | 2025-06-06 | listed only |
| image-20250606-171019.png | image | 14 | 2025-06-06 | listed only |
| image-20250606-172251.png | image | 29 | 2025-06-06 | listed only |
| image-20250606-173403.png | image | 30 | 2025-06-06 | listed only |
| image-20250606-180628.png | image | 83 | 2025-06-06 | listed only |
| image-20250620-003645.png | image | 155 | 2025-06-19 | listed only |
