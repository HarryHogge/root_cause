# VXEP-451: VXE 523 landing anomaly, vehicle landed 300m from PLZ

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-06-28
- **Updated:** 2026-03-02
- **Resolved:** 2025-02-25
- **Reporter:** Pat Wells
- **Assignee:** Josh Burrell
- **Creator:** Pat Wells
- **Labels:** USASOC, Weekly-incident-tracker
- **Links:** relates to SMUP-49 (Determine if behavior for landing with no GPS is accurate in the Manual.)
- **Customer:** USASOC
- **Vehicle Tail Number:** 523
- **Plan:** Needs data review
- **Issue Status:** Root Cause investigation complete
- **Root Cause:** No Issue. The vehicle landed at the current location because GPS was lost and position control was no longer possible.
- **Incident Type:** Aircraft Damage
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Report received from operator: 
Attached is the Flight Data Report and After-Action Report logs from our last flight. Below is a description of what happened during the landing portion of the flight that caused two VTOL props (one CCW, one CW) and one Elevator retention screw to be replaced.
 
During recovery, once the AV reached the VTOL recovery altitude of 350ft AGL within IP2-3, as it transitioned from IP4 to IP5 the AV disappeared from the GCS and a Dead Reconning (DR) Window populated. After roughly 10 seconds the AV repopulated on the GCS apprx. North 300m away from the PLZ and still descending but now in VTOL mode. The Ground Observer (GO) lost visual of the AV at this time while also confirming that the GCS was reporting an incorrect DR position. Once the AV finished its decent in VTOL it repopulated out of DR at the correct position which was almost center of IP1 which was within the compound.
 
During all of this no battery or power warnings populated. The AV had apprx. 24% main battery and 75% HLB. The GO had a reading of 11kts 120 degrees winds on the ground. 
 
Although not present for landing, during physically recovering the AV, it appeared that the VTOL props struck a T-Wall. No other damage, other than the Elevator retention screw, was observed during the recovery. 
 
My assumption is that some sort of jammer was turned on and caused the AV to enter DR during its final decent for recovery. 
AAR attached
7th Group

## Corrective Action

Determine if the Operators Manual or Training needs to be updated so that operators are informed of behavior. @Dana Holley

## Comments (14)

### Pat Wells, 2024-06-28

@David Grosher FYSA new incident

### John Clark, 2024-06-28

FW FDR suggests loss of GPS signal
[embedded image-20240628-154910.png]

[embedded image-20240628-154821.png]

### John Clark, 2024-06-28

Also, available in XComm. Note tha DR (Dead Reckoning) is a directive caused by loss of GPS

[embedded image-20240628-160047.png]

[embedded image-20240628-155845.png]

[embedded image-20240628-155639.png]

[embedded image-20240628-155528.png]

### David Grosher, 2024-08-12

@Ryan Christino Hi Ryan, can you complete this investigation? The current theory is that GPS was lost and so the AV landed where it was at as intended by the design. Thanks

### Ryan Christino, 2024-08-12

@David Grosher Yep, I’ll start working on documenting this stuff and getting it into a report.

### Ryan Christino, 2024-08-14

@David Grosher @Pat Wells 
Here is a link to what I have so far for the report: Vehicle Investigation Report VXEP-451.pptx
Please review and provide feedback for this incident report.

### David Grosher, 2024-09-05

@Pat Wells @Dana Holley There is no issue here. Just an action to determine if the manual or training needs to be updated to address awareness of the designed behavior.

### Dana Holley, 2024-09-05

@David Grosher We briefly train on emergencies within the training course, it’s mainly discussed through lecture and not performed in practical exercises, such as a SIM. The manual states that with a GPS failure during landing, the aircraft will continue landing (presumably using DR). The DR solution should be more accurate to it’s PLZ as the time and distance of travel from IP4/5. Landing 300m away is a long distance from it’s intended and commanded point. We don’t have any information on the accuracy of the INS without GPS over a set period of time or test if the the aircraft will still accept waypoint commands with GPS failure. What I’ve seen that works well, is figuring out the time DR is accurate for, and the system ignoring waypoint commands after that time period. Our current loss of GPS signal checklist mainly covers how to perform a GPS failure while on mission.

### David Grosher, 2024-09-05

@Dana Holley Right now it won’t dead reckon when GPS is lost while it is in the landing sequence, it will simply land where it is at. I think it would be OK to dead recon and is probably desirable to landing someplace unintended. 
@Sam Miller Do you have any history on this behavior?
@Pat Wells  FYSA

### Alexander Alan Arnold, 2024-12-10

@David Grosher Is D5 still accurate for this investigation?

### David Grosher, 2024-12-10

@Alexander Alan Arnold I created a manual CA and will move this along in the process.

### Josh Burrell, 2025-01-30

@David Grosher just going through some of these tickets and see your comment below. Can you send me what the manual CA is so we can try to get it in the next REV?

### David Grosher, 2025-01-30

@Josh Burrell I’m not familiar enough with the manual to know if the description is correct. The CA at this point is to do that evaluation. We have seen similar questions on this topic a few times. The Aircraft will land where it is if it loses GPS and that is unexpected for some operators. It seems that there is either a manual issue or a training issue that needs to be resolved.

### Josh Burrell, 2025-01-30

@David Grosher my apologies I took “I created a manual CA and will move this along in the process.” as in you had something for us to implement. I’ll get with FLOPS and see what they say.

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V523_240627_001610_pack.zip | archive | 2484 | 2024-06-28 | listed only |
| [flightdataloggcs-6.2.9-0.csv](attachments/21304_flightdataloggcs-6.2.9-0.csv.md) | csv | 113 | 2024-06-28 | converted |
| image-20240628-154821.png | image | 7 | 2024-06-28 | listed only |
| image-20240628-154910.png | image | 7 | 2024-06-28 | listed only |
| image-20240628-155528.png | image | 8 | 2024-06-28 | listed only |
| image-20240628-155639.png | image | 8 | 2024-06-28 | listed only |
| image-20240628-155845.png | image | 20 | 2024-06-28 | listed only |
| image-20240628-160047.png | image | 21 | 2024-06-28 | listed only |
