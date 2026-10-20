# VXEP-1903: VXE 996 Link Loss on landing

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2026-06-04
- **Updated:** 2026-10-14
- **Resolved:** 2026-10-14
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** RCCA, Software, Weekly-incident-tracker
- **Links:** relates to FS2-4701 (VXE 996 Link Loss on landing); relates to VXEP-1951 (VXE 996 RR Motor detached from boom); relates to RMA-1051 (VXE-996 RMA 260708-2)
- **Customer:** CBP
- **Vehicle Tail Number:** VXE 996
- **Vehicle Configuration:** B40, P5, 140G2Z
- **Incident Type:** Other (Record"Event Type: XXXXXX" in the description)
- **Severity:** 2 - Degraded Performance - No Workaround
- **Executive Summary:** Awaiting next steps from engineering team. Probable cause; Software

## Description

Statement 

First two flights on 996 today: aircraft lost link as soon as we touched the ground/the operator hit Cut/Safe
Motors. The lift props continued to spin for 20-30 seconds

## Comments (16)

### Alexander Alan Arnold, 2026-06-04

UPDATE: Flight Crew has had two successful landings without issue after repositioning of Silvus antennas on ground. Leaving open in case engineering still would like to review data

### David Grosher, 2026-06-04

@Kurt Burian There are indications of FW AP WD Boot in these AARs, although it doesn’t appear to be happening during the flights. Can you chase down the code that is dumped with the WD boots? Also, there are a lot of power cycles in the FDR, so I’m not sure when these issues occurred. It may not align with the other data in the AAR. @Scott Whitney FYSA
[embedded: image-20260604-215000.png]

### Kurt Burian, 2026-06-14

@Alexander Alan Arnold @David Grosher 
I was wondering if we have any information on what payload was plugged in to the diagnostic port?

It seems like the vehicle was having issues with the fixed AP connection that may have presented as a Silvus link issue or at minimum happened concurrently. The device on the ‘diagnostic port’, XCOMM Switch 1 Port 2, gets its network connection reset numerous times. I don't know if its related, but the AP serial link experiences issues around the same time, causing status flags to show AP link failure. I would normally blame this on the AAR data collection, but this event happens prior to the start of the landing task on both flights.
I tried to track down the source of the WD_BOOT messages in the FDR, but the breadcrumbs provided little help so far as they all appeared normal, will revisit.
[embedded: image-20260615-054130.png]
[embedded: image-20260615-054141.png]

### Alexander Alan Arnold, 2026-06-16

There were no payloads plugged into the diagnostic/aux hood payload port during the training. The only payload used was a gimbal connected to the Alden plug in the fuselage. @David Grosher @Kurt Burian

### Alexander Alan Arnold, 2026-07-06

@Eric Brewer can someone look at this log for excessive vibration, this aircraft just crashed, operator statement claims RR motor became detached during landing seqeunce and I am waiting on data from the crash. @Matt Philley This asset falls under the wire crimp issue to my knowledge @Pat Wells @Drew Hildreth 

Understand it is not data from crash just hoping to see if it aids before we have crash data

### Eric Brewer, 2026-07-07

@Alexander Alan Arnold vibe appeared on par with other B40 aircraft.

### Matt Philley, 2026-07-07

@Alexander Alan Arnold yes AC 996 is within scope of the JST investigation. 
Can you clarify what is the situation? This ticket looks like its from last month and related to an issue where the AC lost connection. 
Did the AC crash and will get a new Incident Ticket but you are tagging on this one because you think it might be related? Or are you calling this event on this ticket a crash?

### Eric Brewer, 2026-07-10

@Alexander Alan Arnold reviewed the flight log, there was definitely a good bit of vibe in the pitch and roll axes on the transition out.  The climb looked on the high side of normal (our abort limits are above 1 for Axyz and 30 for rpy for more than a second, so it was below that during the climbout).  It’s hard to know if the vibe was due to the hardware failure or if the vibe caused the hardware failure.  hopefully physical inspection would yield some clues here.
[embedded: image-20260710-185856.png]

### Eric Brewer, 2026-07-10

Moving to ticket here.[VXEP-1951] VXE 996 RR Motor fail - Jira

### David Grosher, 2026-08-26

@Kurt Burian Is there anything more that can be done here? Is there other data between this event and the incident? If so, it might indicate if this issue was persistent or simply a one off here. This type of issue is rare and difficult to debug so we may not be able to close it with a resolution.

### Kurt Burian, 2026-08-26

@David Grosher I’ll jump back on this issue and try to make sure its resolved by the end of this week.

### Alexander Alan Arnold, 2026-09-23

@Kurt Burian Were you able to make any progress on this issue or do we need to consider it as cannot duplicate/solve?

### Kurt Burian, 2026-09-24

@Alexander Alan Arnold Please see linked task https://jenaero.atlassian.net/browse/FS2-4701 
Here's a hard copy in pdf form.[embedded: V996_FINAL_REPORT.pdf]

### Zachary K Malik, 2026-10-13

Hey @Kurt Burian Is there any corrective actions that need to be implemented so we can close this out?

### Kurt Burian, 2026-10-13

@Zachary K Malik If not already done, Flight Systems might want to create a backlog task to implement a fix to prevent AAR collection until both the fixed wing and vtol autopilots agree, but nothing specific to this vehicle. I’ll mention this to @Eric Brewer , we should be good to close.

### Zachary K Malik, 2026-10-14

No further action required.

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V996_B40_20260604T165813Z.zip | archive | 43743 | 2026-06-04 | listed only |
| AAR_V996_B40_20260604T182857Z.zip | archive | 48122 | 2026-06-04 | listed only |
| [Mishap Report Loss link on Cut and Safe.pdf](attachments/60208_Mishap%20Report%20Loss%20link%20on%20Cut%20and%20Safe.pdf.md) | pdf | 365 | 2026-06-04 | converted |
| image-20260604-215000.png | image | 9 | 2026-06-04 | listed only |
| image-20260615-054130.png | image | 176 | 2026-06-14 | listed only |
| image-20260615-054141.png | image | 138 | 2026-06-14 | listed only |
| image-20260710-185856.png | image | 248 | 2026-07-10 | listed only |
| [V996_FINAL_REPORT.pdf](attachments/64870_V996_FINAL_REPORT.pdf.md) | pdf | 235 | 2026-09-24 | converted |
