# VXEP-1905: VXE-959 Tree landing

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** High
- **Created:** 2026-06-05
- **Updated:** 2026-09-09
- **Reporter:** Jackson Riley Curvin
- **Assignee:** David Grosher
- **Creator:** Jackson Riley Curvin
- **Labels:** Crash, Hardware, RCCA, Weekly-incident-tracker
- **Customer:** Air_PMO
- **Vehicle Tail Number:** VXE-959
- **Vehicle Configuration:** VXE-30 Standard Main Battery
- **Problem Type:** Discovered Issue
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical
- **Components (EA Aircraft):** Aircraft, full assembly
- **Executive Summary:** Awaiting RMA from customer to conduct hardware investigation. Probable cause Hardware Issue.

## Description

aircraft was approaching IP5 you can see the front motor shut off but the VTOL motors never turned on aircraft then glided into the trees

## Comments (6)

### Cody Smisek, 2026-06-05

[embedded: image-20260605-160114.png]
[embedded: image-20260605-160126.png]

[embedded: image-20260605-160220.png]

VTOL was commanding all 4 motors. Appears right side may have powered on while left side did not.

### Cody Smisek, 2026-06-05

2nd look at video reveals that forward left motor appears to attempt to home after crash. 
Additionally, apRollTrim is at limits during fixed wing flight. Given issue with left boom motors not starting during transition, this could point towards left aileron servo not receiving commands. 
Suspect left boom data cable not full seated andor some intermittent issue with that connection. 

[embedded: image-20260605-163136.png]

### Alexander Alan Arnold, 2026-06-24

@Samuel Lopez @David Grosher Can we have someone weigh in on Codys assessment? we will work to get this aircraft returned.

### David Grosher, 2026-06-24

@Alexander Alan Arnold I think Cody’s assessment is accurate given the data available. I would inspect the harnessing but given the crash we may not learn anything new.  Also, presumably they would have checked the surfaces prior to flight and would have observed that the aileron wasn’t moving, if there is a video of preflight that would be worth reviewing.

### Drew Hildreth, 2026-06-26

@Jackson Riley Curvin have we started the process to get this RMA’d so the Engineering Team can take a look at it?

### Jackson Riley Curvin, 2026-06-30

@Drew Hildreth JVO was informed that this will need to be RMA’d

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| MISB-05292026-033152-1-2.mpg | video | 14520 | 2026-06-05 | listed only |
| T95_V959_260529_033139_pack.zip | archive | 3381 | 2026-06-05 | listed only |
| image-20260605-160114.png | image | 276 | 2026-06-05 | listed only |
| image-20260605-160126.png | image | 56 | 2026-06-05 | listed only |
| image-20260605-160220.png | image | 326 | 2026-06-05 | listed only |
| image-20260605-163136.png | image | 92 | 2026-06-05 | listed only |
