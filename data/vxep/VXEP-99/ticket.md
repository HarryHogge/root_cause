# VXEP-99: VXE-482 loss of altitude and crash

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-09-21
- **Updated:** 2026-08-14
- **Resolved:** 2025-02-04
- **Reporter:** Pat Wells
- **Assignee:** Cameron Chapman
- **Creator:** Pat Wells
- **Labels:** Hardware, MARSOC, Top-issue
- **Links:** relates to ENG-3065 (AC 482 Crash); is blocked by VA-605 (VXE-482 crash investigation); relates to RMA-207 (VXE-482 231130)
- **Customer:** MARSOC
- **Vehicle Tail Number:** 482
- **Corrective Action:** Link to ESC replacement. Replacing with more reliable ESC data connection.
- **Other Stakeholder (as required):** Adrian Garcia
- **Problem Type:** Other (explain in description)
- **Incident Type:** Aircraft Loss
- **Severity:** 1 - Flight Critical

## Description

File storage VIT2-448

As reported from the deployed customer: MARSOC
VXE-482 experienced loss of altitude control over target objective in orbit 4. Operator recommanded orbit 4 however the aircraft was unable to maintain altitude. Orbit 3 was commanded to fly the aircraft away from objective. Aircraft was still unable to maintain altitude and U-drive was commanded to attempt to regain altitude control and manually steer the aircraft away. Link was lost at 367 feet before the U-drive command could be sent. MSOC declined to recover aircraft due to partner force protection and operational concerns.

Aircraft not recovered.  AAR file not available.

## Plan

Files: VIT2-448
Review provided AAR for Root Cause
- Review logs before around and before 1375 seconds for if the throttle issue was happening before that, or any other potential causes.   
- [embedded file]
- Record flight hours on ESC and vehicle temps. Does this feed into lifespan calculations?

## Issue Status

VIT2-448_VXE-482_Investigation.pptx
1.In a standard VXE aircraft. The load difference from 0 throttle vs 100% with no propeller is ~30W. Since there is no corresponding power change with throttle changes after the sudden loss of propulsion, this indicates that the motor is not spinning.
2.Since power and other data was recorded and communicated after the loss of propulsion, this indicates that power was present at least to the current sense board in the nose. This indicates a likely failure of harness between the CSB and ESC, the throttle signal harness, or something in the ESC assembly.
3. Issue seems to be present around 1380. This is when power stops tracking throttle. 
4. Flight hours on ESC is 15.3hrs and there is no data on vehicle temp since VTOL and XCOMM logs are not available.
5. Low power, high throttle seen around 1550 and 1700

## Root Cause

Investigating
Likely forward ESC failure or forward motor failure (less likely).

## Comments (8)

### Pat Wells, 2023-09-21

Comment from Matt Curran on VIT2-448

”The preflight power was 42.7W, the power during and after the altitude loss was 50 W. The added 7W is likely due to servos. Commanded throttle was 100% during descent with what look like ESC throttle resets.
If the no load power on the nose motor is greater than 7 W, then the cause might be the spinner coming off.
If the no load power is less than 7 W, then the ESC may have stopped driving the motor.
What is the no load power from the motor at 100% throttle?
Is the AP limiting the power on the climb because the HLB is low?”

### Greg Fryer, 2023-09-26

Epic created, initial data analysis task assigned. Priority increased from medium (prevented alerts from going off, would have been trapped tomorrow 9/26).

### John Clark, 2023-09-28

@Greg Fryer updated investigation report attached.

### Greg Fryer, 2023-10-02

New tasks created for Cameron’s next steps. See tasks under the epic.

### Cameron Chapman, 2023-10-30

@John Clark can you please post the excel plots and other files you generated here? VIT2-448

### Cameron Chapman, 2023-12-12

Updated inv plan

### Cameron Chapman, 2023-12-14

@Adrian Garcia thanks for your help with this. Please review the ppt and make the following changes. 
- Remove old info. Ex: next steps on slide 3, slide 4
- Add esc or motor failure to likely cause on fishbone.
- Update almost all fields above. Link ESC replacement and in corrective action.

### Greg Fryer, 2025-02-03

@Pat Wells @Cameron Chapman Here’s an old incident that I think is fully closed. We know there is an improvement we could make (re-designing the nose) but that is basically (Havoc or next gen plane)

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V482_230911_124215_pack (1).zip | archive | 539 | 2023-09-21 | listed only |
| VIT2-448_VXE-482_Investigation[1].pptx | pptx | 4 | 2023-09-28 | failed: BadZipFile: File is not a zip file |
| image-20231212-192215.png | image | 48 | 2023-12-12 | listed only |
