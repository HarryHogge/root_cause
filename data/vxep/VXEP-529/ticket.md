# VXEP-529: VXE 674 Erractic landing behavior, not accepting operator commands

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-08-07
- **Updated:** 2026-01-15
- **Resolved:** 2024-12-05
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** E140_Mag, Edge_Asset, FlightSystems, Weekly-incident-tracker
- **Links:** relates to FS2-2196 (VXEP-529 - Investigate inability to send operator commands); relates to VXEP-530 (VXE 490 GCS displaying erractic aircraft icon position data and not maintaining size of commanded loiter)
- **Vehicle Tail Number:** 674
- **Root Cause:** Not an issue. No evidence of abort in logs. Goto was ignored because it was too far along in the landing sequence.
- **Incident Type:** Near Miss
- **Severity:** 1 - Flight Critical

## Description

This is an Edge FLOPS asset running software version 6.2.10.  Team is currently at an active demonstration/exercise in Michigan.  All aircraft are configured with this software version.

Statement from Operator:
I was operating A/C 674 at Complex30 Grayling, MI. I was flying in a 400ft AGL orbit directly North of our Primary Landing Plan. I set the Primary Landing Plan as a straight in approach due to the area’s obstructions and minimal space. As I was directed to come in for landing, I noticed the aircraft icon on the software was severely crabbing. However, the SA camera looked normal. I have seen aircraft icon crabbing abnormally on the software before, but not like this. I had sent the aircraft to IP1 very shortly after noticing this icon issue, however; I made the call to continue with the recovery since ground crew verified my aircraft was flying straight and my SA camera looked normal. I believe this was an operator error and I should have continued flying the orbit to troubleshoot.
 
Shortly after entering IP1 the icon continued to show erratic orbits as it was in IP2 descent. Ground crew verified that altitude variations were erratic and that I should abort. I used the hand controller to abort, but the command did not take. I immediately tried commanding GoTo Orbit 2 (at 400ft AGL). The command did not take. By this short period of time, the aircraft transitioned to VTOL and the motors kicked on. Ground crew notified me of this, and I responded that I did not have control of the aircraft as the user landing control window had not popped up. The ground crew notified me that the aircraft overshot the PLZ, and then corrected back to the PLZ point I had planned. At this point, the user landing control activated, and I was able to pause/nudge, if needed.
 
The aircraft continued in its VTOL descent to the correct PLZ point. Everything continued normally.

AAR attached

## Issue Status

Landing Abort Ignored:
The operator reported two types of abort input to the system.
- Commanded landing abort using “hand controller” which I a believe is the Xbox controller.
- I don’t see any evidence in any of the logs (GCS Debug/GCS Event/XComm Event) of this abort.
- Commanded Go To with a primary mission waypoint.
- This command was logged, but the landing state machine on the fixed wing autopilot had already passed the state that allows aborts. Since the abort was not valid for the state of the fixed wing when the message was received the landing abort command was ignored. This is the expected behavior.

## Comments (11)

### David Grosher, 2024-08-07

@Eric Brewer can you take a look at this?

### Eric Brewer, 2024-08-07

@David Grosher @Greg Fryer @Pat Wells on a quick data review it looks to me like the heading from the fixed-wing ap was erroneous for some reason.  Best guesses would be:
1. If this is a non-standard configuration vehicle, investigate whether anything that has been added to the vehicle might be impacting the fixed-wing magnetometer
2. If it’s a standard configuration bird, consider replacing the fixed-wing autopilot and recalibrating the mag.

### Pat Wells, 2024-08-07

@Eric Brewer @David Grosher @Greg Fryer 
Aircraft was in standard battery configuration with Octopus E140Z G2 payload.  No additional devices or payloads installed. 

Previously have noted magnetometer issues on other Edge asset VXE30’s during preflight with E140 payload installed.
In this instance the team experienced this and had to perform a mag cal in order to pass pre-flight.  
Including this information as it could be relevant to the anomaly seen here with the erroneous heading. 

FLOPS team is still participating in an active demonstration /exercise.  They have grounded this aircraft.  Is there any cause for concern software version wise for their remaining two aircraft?  These are also running the same version, 6.2.10.

### David Grosher, 2024-08-07

@Pat Wells @Eric Brewer @Greg Fryer I would recommend for E140 flights that the gimbal be stowed in the same position at which the magnetometer was calibrated. 

Also note, there are different mag cal procedures. You need to specifically calibrate the FW AP Mag for the E140, not the VTOL.

### Pat Wells, 2024-08-23

@David Grosher @Eric Brewer Are we attributing this to the E140 payload and not an aircraft issue?

### David Grosher, 2024-08-23

@Pat Wells We intend to pick up some of these lingering tickets now that MAGNSS is complete. This investigation is not complete at this point. We certainly need to understand the inability to send operator commands (@Jason Scherer ) in addition to the potential magnetometer errors (@Eric Brewer ).

### Eric Brewer, 2024-08-23

@Pat Wells I can’t say definitively if the issues were related to E140 or something else, although it seems likely if we’ve had issues with that payload.  The easiest way to tell is to run the GCS mag checks - ideally with the E140 in the position it was during flight (or if the payload was moving during flight, we can try moving the payload to see how that impacts the fixed-wing heading estimate).

### Jason Scherer, 2024-09-24

@David Grosher I don’t see any evidence in the logs of a commanded abort (not sure why), but I do see the “GoTo Orbit 2 (at 400ft AGL)” command. By the time the fixed wing autopilot received the go to command it was already too far into the landing state machine (State: LAND_HOLD). So the fixed wing ignored the go to command and completed the VTOL landing.

### David Grosher, 2024-12-04

@Pat Wells Can we close this given Jason’s comment below?

### Pat Wells, 2024-12-05

@David Grosher yes I concur.

### David Grosher, 2024-12-05

No issue was present. Behaved as expected.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V674_240807_120706_pack.zip | archive | 2210 | 2024-08-07 | listed only |
