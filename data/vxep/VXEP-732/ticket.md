# VXEP-732: VXE 628 Crash on VTOL descent

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-10-21
- **Updated:** 2026-09-09
- **Resolved:** 2026-01-20
- **Reporter:** Pat Wells
- **Assignee:** Cameron Chapman
- **Creator:** Pat Wells
- **Labels:** Crash, PMA263, Training, Weekly-incident-tracker
- **Links:** relates to RMA-359 (VXE-628  240924-3); relates to FS2-2451 (Investigate VXEP-732 - Crash on VTOL Descent); relates to FS2-2321 (Create a consolidated report on mismatched SW/FW versions for VXE-572/573/574/628/688/594); relates to ENG-2992 (VXE 444 Crash in Landing Pattern)
- **Customer:** PMA263
- **Vehicle Tail Number:** 628
- **Corrective Action:** Customer should use updated firmware.
- **Issue Status:** Investigating CW failure
- **Incident Type:** Aircraft Loss
- **Severity:** 1 - Flight Critical

## Description

Note: This is from the large grouping of crashes that occured Aug 2024 at 29 Palms.  GySgt Powell incident.
Note: It is AV 628 fuselage with the rest of the components belonging to AV 501.  Fuselage and Wing cases are labled with 501.

Statement from operator:
AV made hard right turn in VTOL descent and crashed into ground.
Edge Autonomy GCS was used to extract logs and generate AAR. Ignore GCS version/logs. We have no GCS logs/data for this incident.

SharePoint Folder: VXEP-732 - Crash on VTOL Descent
Investigation Report: Vehicle Investigation VXEP-732.pptx

## Plan

Determine cause of CW failure.
- Investigate related HW. Inspect XCOM for a similar failure as this issue https://jenaero.atlassian.net/browse/VIT2-252 . 
- @Pat Wells what is the status and plan for this HW?

## Root Cause

Aside from using flight firmware multiple iterations and flight-safety warnings out of date, the avionics lost communication with the CW during VTOL transition resulting in a failed land abort. Land abort likely failed due to no airspeed data, and there is log data to indicate airspeed faults after the landing abort started.

## Comments (26)

### Greg Fryer, 2024-10-21

@Scott Whitney Is there anyone free who could do a data pull and then analysis? (Can be separate people… 🙂 ) We’ll hear from Sean when it’s avaialable.

### Sean Odell, 2024-10-22

@Scott Whitney @Greg Fryer @Pat Wells Aircraft evaluated (Paperwork in case) and delivered to Engineering for your investigation efforts.

NOTE: Aircraft is in VXE-501 Case!

### Scott Whitney, 2024-10-24

@Greg Fryer - after initial investigation the vehicle was running firmware that could date back to 2022 (Jason’s findings below). Based on this, I asked Jason to hold off on any further investigation. Let me know how you want to handle this.

https://jenaero.atlassian.net/browse/FS2-2451?focusedCommentId=43345 
Vehicle was running old firmware. I checked with John and the VTOL/XComm versions were released before Edge Autonomy. Best guess is ~2022. The Fixed Wing is the same version that we were using when I started around September last year.
Based on initial analysis the fixed wing ap issued a land abort due to exceeding attitude limits during transition to VTOL for landing. VTOL data stops updating on XComm logs about the same time as CAN timeouts are recorded for both VTOL and Air data. This is about the impact time. Prior to the stale VTOL data and CAN timeouts an airspeed fault is logged. The Airspeed and Ground speed data in the FDR differ a decent amount. I did see IAS data dropouts in the FDR during the fixed wing flight phase. Could be a bad ADP. Overall battery and current levels look ok.
Bottom line. Something bad happened during transition from fixed wing to VTOL which caused the vehicle to fall quickly. VTOL throttles looked ok, until they stopped.
Based on the old firmware it sounds like we might not need to look any further. Standing by for further direction on this ticket.
Firmware Versions
- AP 6.05m
- XComm: 4.60
- VTOL: 1.44

### Greg Fryer, 2024-10-24

@Scott Whitney Definitely halt investigation.
@Pat Wells See below on ancient firmware configuration. Need to escalate to PM (though I’m sure they are tired of issuing this message…). I’m guessing from location and it being a Gunny, this is @J Vo ?

### Pat Wells, 2024-10-25

@Greg Fryer yes this is Gunny Powell’s work. We’re tracking that most, if probably not all, of his aircraft that he crashed we’re running mismatched firmware. Customer is aware.  Working with @David Grosher to release one consolidated report for all of Gunny’s mishaps outlining the severity of the software mismatch etc.  I concur with halting the investigation on this aircraft.

### J Vo, 2024-10-28

@Greg Fryer PMA is aware that operators are not updating software as instructed.  Technically, the non-updated vehicles should be downed, but these are non-aviation centric entities doing their own thing.  Definitely discussion topic for the FoSUAS visit to Huntsville next month.

### Pat Wells, 2024-12-05

@Greg Fryer @David Grosher do we intend to investigate this further or will it be closed based on the software mismatch issues?

### Greg Fryer, 2024-12-05

@Pat Wells Sorry, I didn’t click the button. No, we will not further investigate ancient versions like this.

### Rodney Linch, 2025-01-02

I pulled VXE-501’s Avionics Box ftrrom VXE-628’s. Avionics box is now with 501’s fuselage.

### Jason Scherer, 2025-02-11

Moving ticket from Done to In Process. An investigation has been requested to support the miss-match firmware report. The investigation was previously not completed due to outdated firmware.

### Jason Scherer, 2025-02-11

@David Grosher @Cameron Chapman @Adrian Garcia This crash was likely caused by loss of CW systems (VTOL/ADP). Landing was aborted, but fixed wing flight failed due to airspeed faults. Not sure we can successfully recover with no ADP. I found some interesting voltage data during the time of abort that you guys might want to take a look at. Need hardware team input to continue.

### Cameron Chapman, 2025-02-14

@Jason Scherer good work on the investigation and report. Comments from reviewing it.
- It seems like whatever fault occured, it affected multiple measurements and busses on the XCOM (something like a large transient or short, rather than a CW disconnection)
- The occurrence during transition is likely not a coincidence. How does the timing of this event compare to VTOL throttles, current, and voltage. Perhaps it could be due to the large transients when the motors kick on or ramp to full power.
- We could check ground isolation status, if FET was closed during this time, it could make VTOL AP more susceptible to transients.
- Are there any known issues that could cause similar behavior fixed with firmware updates since this old firmware?
- @Adrian Garcia  and @Giovanni Gonzalez  can you please inspect for any obvious faults? Loose connection, burn smell or evidence, etc.

### Cameron Chapman, 2025-02-14

Are any payloads mentioned in the flight logs?

### Jason Scherer, 2025-02-17

@Cameron Chapman 
- It seems like whatever fault occurred, it affected multiple measurements and busses on the XCOM (something like a large transient or short, rather than a CW disconnection)
- Agreed -JS.
- The occurrence during transition is likely not a coincidence. How does the timing of this event compare to VTOL throttles, current, and voltage. Perhaps it could be due to the large transients when the motors kick on or ramp to full power.
- We could check ground isolation status, if FET was closed during this time, it could make VTOL AP more susceptible to transients.
- “ground isolation status” I’ll have to see if this is logged anywhere. If it’s only logged on VTOL (likely) we may not have data during the incident. I’ll Check. - JS
- Are there any known issues that could cause similar behavior fixed with firmware updates since this old firmware?
- There is over 3 years of fixes that include tweaks from Gordon himself. So, it’s hard to say for sure without spending a lot of time going through the Git Repos. I’ll take a brief look for anything obvious. - JS

### Jason Scherer, 2025-02-17

@Cameron Chapman Are any payloads mentioned in the flight logs?
Seems like there is a payload installed and operated during the flight. I base this on a few things in the data.
- Trillium park commands in XComm log.
- Payload Retract current spikes up to 0.6A (which seem to happen at the same time as the incident)
- Network connection to diag2 (XComm switch 1 port 2) is connected until the incident. I believe this port is the payload Ethernet port.

For a quick look, here is the retract current compared to the Ethernet drops of both Diag (Payload?) and CW. 
[embedded: image-20250217-171650.png]

### Cameron Chapman, 2025-02-18

@Jason Scherer the retract at the time of failure may not be a coincidence. Can you please add this to the investigation report?
@Connor Peebles  worked on a previous issue that crashed after the retract command. I think he discovered XCOM damage. @Connor Peebles can you please link to this one and update investigation plans for this one based on findings from the other?

### Jason Scherer, 2025-02-18

@Cameron Chapman @Connor Peebles I zoomed in on the data and added the payload voltage. The retract current seems to occur directly after the network drop on the CW/Payload. But, it does all happen within a few hundred milliseconds. I’ve updated the slides.
[embedded: image-20250218-180656.png]

### Cameron Chapman, 2025-02-18

@Jason Scherer good observation. Strange. Could the current log be delayed in any way (ex: log buffer), or do you think this indicates that the current came after the 12V anomaly (and is likely unrelated)? Was the retract an automatic or user command?

### Jason Scherer, 2025-02-18

@Cameron Chapman The retract command is automated on landing. Each tick mark is 100ms. So, the Ethernet drops happened 200-400 ms before the voltage drop. There is some moving avererages involved in data sampling, so tha could be part of the dealy. I don’t know if that time range is within the reaction of the moving average or not. We could run tests to determine log reaction time.

### Connor Peebles, 2025-02-18

I found this one that was more recently worked that just seems like retract was coincidentally at the beginning of cascading failure: [VXEP-427] VXE 430 abnormal landing behavior - Jira
The one I worked on where I_retract went above 1A was [VIT2-252] VXE 444 Crash in Landing Pattern - Jira, 
[embedded: image-20250218-181914.png]
“Spike in current is seen when payload retract is activated which is very similar when a functioning C20 is shorted open with a low value resistor. It could be a defect elsewhere in the xcomm or AP that causes this spike, and that spike induces a ripple that makes it to C20. This electrical stress could lead to a short on C20.
When swapping a known good xcomm with 444’s xcomm - and vice-versa with the AP – we do not see that same retract spike when it is good xcomm + 444AP, while we do see that same retract spike when it is 444 xcomm + good AP. So, the defect that is causing the retract spike is somewhere in 444’s xcomm.“
However, we weren’t able to conclusively pin the C20 failure on this at the time. @Cameron Chapman @Jason Scherer

### Jason Scherer, 2025-02-18

@Cameron Chapman @Connor Peebles I added a timeline to the slide with retract current. The park command is sent before the Ethernet connections are lost. Then the voltage fault occurs, then the current spike.
2786.061 – Transition to hovering flight
2786.072 - A Trillium park command is logged on the XComm event log.
2789.376 – Payload Ethernet connection lost
2789.576 – CW Ethernet connection lost
2789.879 – Payload Voltage fault recorded (Voltage drops below 12V)
2790.494 - The XComm data log shows an increase in the payload retract current.

### Jason Scherer, 2025-02-18

I guess my updates were local and not uploaded. They are saved now.

### Jason Scherer, 2025-03-22

Report added to the 29 Palms software mismatch report.

### Jason Scherer, 2025-03-22

@Cameron Chapman I believe all software investigations have been complete. CW failure cause unknown.

### Christa Meck, 2025-08-05

@Cameron Chapman Where are we at on this investigation?

### David Grosher, 2026-01-14

@Drew Hildreth I think we should consider closing this incident.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20250217-171650.png | image | 64 | 2025-02-17 | listed only |
| image-20250218-180656.png | image | 68 | 2025-02-18 | listed only |
| image-20250218-181914.png | image | 16 | 2025-02-18 | listed only |
