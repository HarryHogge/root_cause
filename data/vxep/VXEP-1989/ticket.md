# VXEP-1989: VXE 932 Crash

- **Issue type:** Incident (8D)
- **Status:** D2 - Gathering Information
- **Priority:** Highest
- **Created:** 2026-09-04
- **Updated:** 2026-10-15
- **Reporter:** Jackson Riley Curvin
- **Assignee:** David Grosher
- **Creator:** Jackson Riley Curvin
- **Labels:** Crash, MOLSON, RCCA, Weekly-incident-tracker
- **Links:** relates to RMA-1102 (VXE-932 260908-1); relates to VXEP-1774 (VXE-933 During launch wizard, Error pops up saying "The autopilot has detected that one or more of its sensors have failed")
- **Customer:** MOLSON
- **Vehicle Tail Number:** VXE 932
- **Vehicle Configuration:** VXE 30 ADV NAV main battery, E140
- **Problem Type:** Other (explain in description)
- **Issue Status:** Sharepoint Location (slide deck, data, photos)
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical
- **Components (EA Aircraft):** Aircraft, full assembly
- **Executive Summary:** VXE 932 fuselage with 933 center wing failed to transition to FW flight.

## Description

Relevant logs appear to be XCL00138, VTOL00079
Description:
- On launch, vehicle 932 fuselage with 933 center wing failed to transition from VTOL to forward flight. Witnesses indicate the forward propeller stopped.
- Air vehicle is described as “in pieces.”

Operators Statement:
We flew for 2.5hrs during the mornings training. We landed for lunch. Post lunch (IVO 1250) we attempted to send the aircraft back up for the afternoons training. After power cycling for close to an hour, the system became compliant and allowed me to actually run through the entirety of the launch wizard. 
Front prop power hit 1460 watts. The vehicle entered VTOL lift off. Crabbed into the wind. Hit altitude of 200’. Began to gain forward momentum. When the transition phase was completed and the VTOL motors stopped spinning the aircraft fell out of the sky. 
It appears as the front prop stopped spinning as the last data sent to VXESUAV showed 56 watts and the last message was FIXED WING FLIGHT. 
Matt

## Plan

Updated 9/23/2026 by C. Smisek
System is in SLO RMA (9/21/2026)
- Over 6hrs of runtime on IB without replication of issue (both with and without incident VTOL AP). Issue appears to have occurred with use of both 932 and 933 fuse avionics, so IB avionics has been used to date. Attempted to recreate through various methods such as heating, cooling and vibrating. See slide deck for more information.
- @Samuel Lopez was asked to consider ideas of what to look into next.
- Review and respond to Eric’s questions (copy/pasted below)
- @Michael Lindsay thanks. A couple questions about the statement:
- what errors were they seeing resulting in having to power cycle for an hour? Did they make any changes in order to become compliant (I assume that meant pass the launch wizard?)
- What were the weather conditions for the takeoff, how much wind and from what direction?
- Did they notice any issues with pressing pitot or the airspeed measurement before takeoff?
- What was the history of the fuselage/center wing and why were they mismatched, was there an issue with one or the other?

## Comments (21)

### Michael Lindsay, 2026-09-17

@Alexander Alan Arnold @Jackson Riley Curvin @Drew Hildreth I completed a full pull of the data from 932, this aircraft was a mix of 932 Fuselage adn 933 Center wing this the files are labelled 932 and 933.  I sla  ved in a nose cone to get the data as there is nothing left of the nose.  We will be shipping it back to SLO tomorrow which we have the shipping details I will provide them.

### Alexander Alan Arnold, 2026-09-17

@David Grosher @Eric Brewer weve gotten some data in here is any of it useable for you guys? @Jeremy Kostel date of incident was reported as 1 september, we received notification a few days after incident

### Cody Smisek, 2026-09-17

xcomm 138 seems to be the one. seems like we don’t have the relevant xcomm event log though

### Eric Brewer, 2026-09-17

@Cody Smisek I believe it’s this one, it mentions that same .csv file. 
[embedded: image-20260917-161850.png]

### Eric Brewer, 2026-09-17

@Cody Smisek @Michael Lindsay @Alexander Alan Arnold it looks to me like an airspeed sensor issue.  The airspeed measurement is varying pretty wildly during preflight, and then shortly after transition the airspeed measurement goes to 0.  
[embedded: image-20260917-165948.png]
There is some logic in fixed-wing that will detect landing if the airspeed is too low, it looks like this triggered:
[embedded: image-20260917-170027.png]
The interesting part is that the vtol and xcomm event logs cut off almost immediately after that event.  It is somewhat typical for the xcomm logs to cut off before impact, but usually the vtol will continue writing for a bit longer, so it makes me suspicious if there was a potential power issue also, not sure.
Xcomm logs:
XCL00138.CSV'); % event log xc000101.T10
VTOL logs: VTL00079.CSV, VTEV_LOG.txt

Do you know why this had mismatched fuselage and center wing, were they having some other issues with the bird?

### Alexander Alan Arnold, 2026-09-17

@Eric Brewer Mike L is waiting on response from customer about swapping centerwings, the operator wont be in until monday.

### Michael Lindsay, 2026-09-17

@Alexander Alan Arnold @Eric Brewer @Cody Smisek Operator statement has been added to the ticket.

### Eric Brewer, 2026-09-17

@Michael Lindsay thanks.  A couple questions about the statement:
1. what errors were they seeing resulting in having to power cycle for an hour? Did they make any changes in order to become compliant (I assume that meant pass the launch wizard?)
2. What were the weather conditions for the takeoff, how much wind and from what direction?
3. Did they notice any issues with pressing pitot or the airspeed measurement before takeoff?
4. What was the history of the fuselage/center wing and why were they mismatched, was there an issue with one or the other?

### Michael Lindsay, 2026-09-17

@Eric Brewer I have reached out most likely will not get anything back until next week.  I will be up at the unit on Tuesday (22Sept), if you need and additional info just let me know.

### Alexander Alan Arnold, 2026-09-21

IN the building awaiting intake. @David Grosher where would you like this sent once intake is completed?

### David Grosher, 2026-09-21

@Alexander Alan Arnold Please give this to @Jeremy Kostel. @Eric Brewer Can you take a quick look at the data around the transition to FW flight to see if we can’t reduce the scope of any hardware investigation?

### Eric Brewer, 2026-09-21

@David Grosher I think my previous comments got buried below, but it looked to me like an issue with the air data sensor, it was varying wildly on the ground and then went to 0 shortly after transition triggering the ‘landed’ logic.  I would start the investigation there, along with anything additional we learn from my questions on the statement below.  @Jeremy Kostel @Alexander Alan Arnold

### Eric Brewer, 2026-09-21

@Michael Lindsay thanks. Do let me know what you hear on the questions above.

### Jeremy Kostel, 2026-09-21

Quick look at the logs doesn’t show anything immediately concerning on the power train. From the logs, looks like FWD motor appropriately responded to throttle commands. Battery voltages and currents look healthy with FWD motor pulling ~1500W
[embedded: image-20260921-200255.png]

### Mathew Papaleo, 2026-09-21

@Cody Smisek intake complete for 992, well keep it stacked back here. let me know if theres anything i can do to help

### Michael Lindsay, 2026-09-23

@Eric Brewer @Alexander Alan Arnold @David Grosher I have attached some pictures of the faults that they received during the launch wizard.  They didn’t change anything to correct this, only power cycled the air vehicle.  They reported no issues when they complete the airspeed measurement check prior to takeoff.  The fuselage/center wing are mismatched by error as a new member of the team  just grabbed a wing and fuselage and didn’t look at the serial numbers.  weather was sunny and they don’t recall the exact winds but they were within OEM limits.
[embedded: IMG_0750.jpg]
[embedded: IMG_0749.jpg]
[embedded: IMG_0748.jpg]
[embedded: 9370D33D-9E3F-4D6A-97E5-F6E7826C1956.jpg]
[embedded: 72950042-CBBF-4133-81E5-3A2167C3E858.jpg]
[embedded: 31F004C0-B6AD-4025-9A9B-04FB2116EAC3.jpg]

### Jackson Riley Curvin, 2026-10-12

@Jeremy Kostel could we get an update on this please?

### Jeremy Kostel, 2026-10-12

@Jackson Riley Curvin The linked report should be up to date on the testing efforts done so far. We are back to the drawing board. All attempts to recreate the issue have failed thus far. I’ll try and sort out a plan for next steps this week

### Samuel Lopez, 2026-10-15

@Jeremy Kostel @David Grosher 
I previously worked on an investigation to VXE 512 for which root cause was inconclusive.  The crux is, 512 went into vertical take-off, ascended, transitioned to fixed wing, and six seconds later, lost all power.
Then I looked at 932 and it looked similar (as shown below).  Although the airspeed is a defect, I also wonder if it's incidentally related to the reason the aircraft lost power and not causal.   If so, then we are looking in the wrong place.

[embedded: image-20261015-183021.png]

### Jeremy Kostel, 2026-10-15

@Samuel Lopez Can you elaborate? Im not sure I understand the point you’re trying to make. 
- To me it looks like a “successful” transition where VTOLs had shut off and fixed wing flight had been intiated.
- The pitch deviation looks very aggressive to me, I think it's entirely plausible that with the logging buffer we have - the logs cut off at the time of impact. 200ft of altitude would be a very quick descent at 1500W from the FWD motor.
- Eric mentioned the IAS reading zero triggered some sort of landing command. (@Eric Brewer @Everett Werner can you explain a little more what you would have expected the aircraft to do with the IAS dropout? Or does the outcome align pretty closely with expectations)
- FWD motor looks to be operating properly (unless we’re missing data when things went wrong) is there any explanation for the aggressive pitch deviation?

[embedded: image-20261015-185633.png]
[embedded: image-20261015-193452.png]

### Samuel Lopez, 2026-10-15

@Jeremy Kostel 
the only point I was trying to make was that in both cases, shortly after fixed wing flight begins, the logs abruptly stop and the two cases looked similar in that aspect.

## Attachments (22)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| signal-2026-09-04-14-33-33-004.jpg | image | 372 | 2026-09-04 | listed only |
| signal-2026-09-04-14-33-43-774.jpg | image | 218 | 2026-09-04 | listed only |
| signal-2026-09-04-14-33-55-569.jpg | image | 232 | 2026-09-04 | listed only |
| signal-2026-09-04-14-34-10-018.jpg | image | 218 | 2026-09-04 | listed only |
| VTOL_VXE933.zip | archive | 46107 | 2026-09-17 | listed only |
| XCOMM_VXE932.zip | archive | 15280 | 2026-09-17 | listed only |
| image-20260917-161850.png | image | 8 | 2026-09-17 | listed only |
| image-20260917-165948.png | image | 40 | 2026-09-17 | listed only |
| image-20260917-170027.png | image | 66 | 2026-09-17 | listed only |
| V932_933_RelevantLogs.zip | archive | 931 | 2026-09-21 | listed only |
| image-20260921-200255.png | image | 278 | 2026-09-21 | listed only |
| 31F004C0-B6AD-4025-9A9B-04FB2116EAC3.jpg | image | 591 | 2026-09-23 | listed only |
| 72950042-CBBF-4133-81E5-3A2167C3E858.jpg | image | 588 | 2026-09-23 | listed only |
| 9370D33D-9E3F-4D6A-97E5-F6E7826C1956.jpg | image | 632 | 2026-09-23 | listed only |
| IMG_0748.jpg | image | 740 | 2026-09-23 | listed only |
| IMG_0749.jpg | image | 547 | 2026-09-23 | listed only |
| IMG_0750.jpg | image | 644 | 2026-09-23 | listed only |
| IMG_0751.jpg | image | 633 | 2026-09-23 | listed only |
| IMG_0752.jpg | image | 324 | 2026-09-23 | listed only |
| image-20261015-183021.png | image | 184 | 2026-10-15 | listed only |
| image-20261015-185633.png | image | 284 | 2026-10-15 | listed only |
| image-20261015-193452.png | image | 261 | 2026-10-15 | listed only |
