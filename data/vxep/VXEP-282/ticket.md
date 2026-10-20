# VXEP-282: VXE 533 VTOL power issue on transition led to Uncontrolled drift and crash on landing

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** High
- **Created:** 2024-02-21
- **Updated:** 2026-03-02
- **Resolved:** 2025-01-31
- **Reporter:** Pat Wells
- **Assignee:** Adrian Garcia
- **Creator:** Pat Wells
- **Labels:** USASOC, Weekly-incident-tracker
- **Links:** relates to FS2-1512 (VTOL Abort logic fix); is cloned by VXEP-283 (VXE-533 Uncontrolled drift and crash after failed VTOL abort); relates to RMA-221 (VXE-533 240222); relates to FS2-1983 (v533 NCR Aborted TO after start of transition); relates to VXEP-639 (VXE 515- HLB Unexpected Voltage fluctuation. Aircraft flown multiple times after, leading to damage)
- **Customer:** USASOC
- **Vehicle Tail Number:** 533
- **Vehicle Configuration:** Battery only.
- **Problem Type:** Other (explain in description)
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

This issue tracks the VTOL failure in transition. See linked issue for failed abort logic.  https://jenaero.atlassian.net/browse/VXEP-283 
Files: VXE-533 Uncontrolled drift and crash on landing
Investigation Report Working Copy: 533 Investigation Report.pptx
Location: FT Moore.
75th RR
Weather: Calm and clear
John's description from operator perspective:
 On flight Number 4 the student was instructed to RTB the aircraft. After entering into ip4 I told the student to be ready to activate user nudge panel. The aircraft over shot landing zone, went into abort logic then did a quick turn It initiated VTOLs like it was trying to perform a VTOL landing. I tried to send the aircraft to an active waypoint but it appeared to be trying to VTOL and fixed wing flight at the same time eventually coming down in Tree line
 
Description from various students who witnessed the aircraft prior to VTOL transition:
 They described the aircraft heading north in its expected transition vector (IP5 to Landing) then overshooting the intended landing spot, turning approximately 90 degrees left, climbed steeply at which point it appeared to stall, rotate over left and entered a steep dive at which point they heard the VTOL motors kick in.
 
Scott's Description as an observer:
I was instructing from the GCS on the other aircraft at the site at the time of the incident.  When I first looked up I saw 533 in a steep very fast dive with an approximate east heading (where the previous student description ends).  The VTOL motors were on and never appeared to turn off for the rest of the incident.  Despite VTOL Motors being on it appeared to be flying fixed wing and pulled out of it's dive and flew back to the south climbing slightly and eventually coming to a standstill over a tree line approximately ¼ mile south where it slowly descended in a fairly standard VTOL descent before disappearing behind some trees.

VTOL and XCOM logs attached

## Corrective Action

https://jenaero.atlassian.net/browse/FS2-1512 
Replace 1409P01D, 1901P01A1, 1911P01A, 107-102264, and 107-102065 https://jenaero.atlassian.net/browse/RMA-221

## Plan

- I think we should create a document of what is a normal looking connector vs known connector defects (solder flow, scuffing, etc). It has been hard to tell in the past

## Issue Status

6/17 Aircraft has been delivered to Engineering for further investigation. Production was planning to deliver this week (they were not aware of the investigation), so it is pretty hot. 
Looks to me like there is some type of VTOL power failure with some sort of failed abort logic after the fact (similar to 496).
6/17 checked power connector and there was a scuff mark but unable to identify if it was dues to wear and tear or arching. There were also some solder blobs at the bottom of the connectors 
6/18 Analyzing data. Using XCL00031 and VTL00054 
6/20 Data is still being analyzed but it seems like one of the sensors stopped sensing for various different points in time. Further investigation suggest that this is a measurement issue. R133’s pad was ripped off when measured  Investigation is ongoing and will not be able to be delivered by the end of the week 
6/21 More data analysis, VBATT and BMS voltage readings are do not align during a certain time frame. Read 533 Investigation Report.pptx for more info
As of 6/25 no concrete data was found to definitively issue a root cause, however, the systems that were inspected and suspected to be the root cause are the CSB and AP board. @Hayden Jeanor is going over this investigation when he has time before it is closed 
7/2/24 Assigning back to @Cameron Chapman

## Root Cause

Dave: “Grouped with 496”. Compound failure. Power failure led to VTOL abort. In both cases, stuck in a race condition between APs trying to control the vehicle. Building out test matrix to verify fixes for all applicable states. 
Specific components for power failure is undetermined however it has been isolated down to the voltage sensing circuitry: 1409P01D, 1901P01A1, 1911P01A, 107-102264, and 107-102065. Vref and AUX2 were behaving abnormally. Further testing can not be performed since the aircraft has been shipped back to the customer with new parts.

## Comments (42)

### Adrian Garcia, 2024-06-18

@Brandon Slater Thank you

### Adrian Garcia, 2024-06-19

@Hayden Jeanor

### Adrian Garcia, 2024-06-20

@John Clark Here is the ticket for more reference

### Hayden Jeanor, 2024-06-20

is there any SA cam footage of the incident?

### Pat Wells, 2024-06-21

@Hayden Jeanor no there is not any SA cam video available.

### Adrian Garcia, 2024-06-21

Was given a word doc for documentation and added most of info there but going to continue through ppt per confluence instructions

### Adrian Garcia, 2024-06-21

@Cameron Chapman @Sean Odell Did this vehicle fly again after this incident

### Cameron Chapman, 2024-06-23

@Adrian Garcia the word doc should also be acceptable. Whatever is preferred. Who instructed ppt?
Yes. See NCR in linked RMA

### Adrian Garcia, 2024-06-24

We are still having a hard time figuring out the root cause of the incident and will not be ready for production any time soon. As of right now the main theories is that we lost connection because we see voltage being read in the BMS but at the same time the VTOL is oscillating. This could also be a grounding issue that Abel is working on right now which can be inferred from the Aux2 and Vref readings 
[embedded image-20240624-231655.png]
[embedded image-20240624-231524.png]

### Adrian Garcia, 2024-06-25

The investigation is starting to look inconclusive, Hayden is going to take one last look into the system but as of today nothing new/concrete can be found to definitively say what caused the incident

### Cameron Chapman, 2024-07-05

@Adrian Garcia see comments in red of the investigation.

### Adrian Garcia, 2024-07-12

@Cameron Chapman PPT is ready to review, linked at the top

### Cameron Chapman, 2024-08-06

@Pat Wells Should this issue be added back to the tracker? The HW investigation is not complete.

### Cameron Chapman, 2024-08-06

@Adrian Garcia please update the fields above now and every time you make progress on an investigation. If you have completed all tasks requested, these should not be in the plan. 
## Plan

- See comments and actions in ppt.
- These plots do not line up. We should figure out a way to plot them correctly (see if another time stamp could be used, or manually line them up in excel)
- They should be the same data just saved on different processors/logs/logging rates. The XCOM VTOL voltage being a lot lower seems to indicate a transmission or processor issue. @David Grosher what do you think could cause this?

### Alexander Alan Arnold, 2024-12-10

@Cameron Chapman @Adrian Garcia I have this as D6 on the incident tracker, but the ticket is showing D2. Can I get an accurate status of this investigation?

### Adrian Garcia, 2024-12-10

@Alexander Alan Arnold The power issue for this investigation was deemed inconclusive.

### Alexander Alan Arnold, 2024-12-10

Since it is inconclusive are you going to investigate further or close this item out? @Adrian Garcia

### Cameron Chapman, 2024-12-10

@Adrian Garcia please clean up ppt, plan, status, root cause, linked issues etc. We need to at least have a suspected root cause and justification of why we cannot investigate further. Please have Laszlo assist if helpful.

### Pat Wells, 2025-01-02

@Cameron Chapman any updates on this?

### Adrian Garcia, 2025-01-07

@Pat Wells This aircraft was shipped back to the customer in September 2024 with the following parts replaced: 
- CW Auto Pilot: 107-101161
- Harness: 107-102065
- Current Sense Harness: 107-103302
- Dual Current Sense Assembly: 107-102264
- Ground Isolation Board: 107-12264

### Brandon Slater, 2024-06-18

@Adrian Garcia Thanks!

### Brandon Slater, 2024-06-18

@Pat Wells @Sean Odell @Adrian Garcia Attached is the AAR

### Adrian Garcia, 2024-06-18

@Brandon Slater Thank you

### Adrian Garcia, 2024-06-19

@Hayden Jeanor

### Adrian Garcia, 2024-06-20

@John Clark Here is the ticket for more reference

### Hayden Jeanor, 2024-06-20

is there any SA cam footage of the incident?

### Pat Wells, 2024-06-21

@Hayden Jeanor no there is not any SA cam video available.

### Adrian Garcia, 2024-06-21

Was given a word doc for documentation and added most of info there but going to continue through ppt per confluence instructions

### Adrian Garcia, 2024-06-21

@Cameron Chapman @Sean Odell Did this vehicle fly again after this incident

### Cameron Chapman, 2024-06-23

@Adrian Garcia the word doc should also be acceptable. Whatever is preferred. Who instructed ppt?
Yes. See NCR in linked RMA

### Adrian Garcia, 2024-06-24

We are still having a hard time figuring out the root cause of the incident and will not be ready for production any time soon. As of right now the main theories is that we lost connection because we see voltage being read in the BMS but at the same time the VTOL is oscillating. This could also be a grounding issue that Abel is working on right now which can be inferred from the Aux2 and Vref readings 
[embedded image-20240624-231655.png]
[embedded image-20240624-231524.png]

### Adrian Garcia, 2024-06-25

The investigation is starting to look inconclusive, Hayden is going to take one last look into the system but as of today nothing new/concrete can be found to definitively say what caused the incident

### Cameron Chapman, 2024-07-05

@Adrian Garcia see comments in red of the investigation.

### Adrian Garcia, 2024-07-12

@Cameron Chapman PPT is ready to review, linked at the top

### Cameron Chapman, 2024-08-06

@Pat Wells Should this issue be added back to the tracker? The HW investigation is not complete.

### Cameron Chapman, 2024-08-06

@Adrian Garcia please update the fields above now and every time you make progress on an investigation. If you have completed all tasks requested, these should not be in the plan. 
## Plan

- See comments and actions in ppt.
- These plots do not line up. We should figure out a way to plot them correctly (see if another time stamp could be used, or manually line them up in excel)
- They should be the same data just saved on different processors/logs/logging rates. The XCOM VTOL voltage being a lot lower seems to indicate a transmission or processor issue. @David Grosher what do you think could cause this?

### Alexander Alan Arnold, 2024-12-10

@Cameron Chapman @Adrian Garcia I have this as D6 on the incident tracker, but the ticket is showing D2. Can I get an accurate status of this investigation?

### Adrian Garcia, 2024-12-10

@Alexander Alan Arnold The power issue for this investigation was deemed inconclusive.

### Alexander Alan Arnold, 2024-12-10

Since it is inconclusive are you going to investigate further or close this item out? @Adrian Garcia

### Cameron Chapman, 2024-12-10

@Adrian Garcia please clean up ppt, plan, status, root cause, linked issues etc. We need to at least have a suspected root cause and justification of why we cannot investigate further. Please have Laszlo assist if helpful.

### Pat Wells, 2025-01-02

@Cameron Chapman any updates on this?

### Adrian Garcia, 2025-01-07

@Pat Wells This aircraft was shipped back to the customer in September 2024 with the following parts replaced: 
- CW Auto Pilot: 107-101161
- Harness: 107-102065
- Current Sense Harness: 107-103302
- Dual Current Sense Assembly: 107-102264
- Ground Isolation Board: 107-12264

## Attachments (10)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 533 pictures_2-21-2024.zip | archive | 247577 | 2024-02-21 | listed only |
| VTOL_VXE533.zip | archive | 33781 | 2024-02-21 | listed only |
| XCOMM_VXE533.zip | archive | 6662 | 2024-02-21 | listed only |
| image-20240221-205229.png | image | 47 | 2024-02-21 | listed only |
| image-20240221-205635.png | image | 182 | 2024-02-21 | listed only |
| image-20240221-212048.png | image | 184 | 2024-02-21 | listed only |
| image-20240222-001217.png | image | 164 | 2024-02-21 | listed only |
| T95_V533_240618_104428_pack.zip | archive | 2234 | 2024-06-18 | listed only |
| image-20240624-231524.png | image | 27 | 2024-06-24 | listed only |
| image-20240624-231655.png | image | 76 | 2024-06-24 | listed only |
