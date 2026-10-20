# ENG-2947: [Remove from VXEP] VXE 797 Main Battery Low Voltage

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-03-06
- **Updated:** 2026-06-08
- **Resolved:** 2026-06-08
- **Reporter:** Cody Smisek
- **Assignee:** Jeremy Kostel
- **Creator:** Cody Smisek
- **Labels:** EE-Intern
- **Links:** relates to VXEP-1197 (Battery discharged below safe voltage range); relates to XKIT-1857 (XKIT_HLB0010 Discharged below 3V)
- **Vehicle Tail Number:** 797
- **Plan:** See corrective actions.
- **Incident Type:** Near Miss
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Software team initially reported difficulty connecting to VXE 797 via Silvus. Upon checking webpages, it was noted that the xcomm webpage was accessible but Silvus webpage was not. 
Software team reset vehicle power (vehicle was powered via standard main battery) and forward motor ESC startup beeps were not noticed. Main battery was disconnected and voltage was checked. Voltage indicated 6-7V. Main battery was immediately removed and red tagged. 
Main battery SN3-1995 MFG Date 240627

## Corrective Action

Disposition and discard any batteries that are no longer needed in engineering yellow fire cabinet
Determine/implement method to clearly identify non useable batteries. 
Determine/implement method to check battery voltages prior to use in software area. (Battery checkers, chargers, GCS reading should all work for this).
Provide engineering personnel with basic training for operating aircraft if their role requires aircraft operation
- Training people not to do this.  @Barry Mendez could discuss this in the next all hands?
- Procedural improvements. Flashing lights? Attach your car keys to the aircraft?
- GCS improvements: notify users when approaching a battery damaging voltage, especially during ground operations. @Ted Trowbridge 
- We could automate shutoff for B35 @Erik Hanson

## Root Cause

Main battery was ~20V at time of installation on 3/5/2025 (shown in xcomm logs). Battery was not charged between 3/5 and 3/6 and was re-used. 
Battery was at insufficient voltage for use in powering vehicle leading to degraded communications state. Battery was at 7V at time of removal from aircraft. 
Main battery was likely utilized previous to above dates without being charged or managed appropriately due to lack of process and training. Battery voltage was not checked using battery checker or DMM prior to installation in aircraft. 
[embedded: image-20250306-222006.png]

## Comments (9)

### Cody Smisek, 2025-03-06

@Cameron Chapman @Barry Mendez @Greg Fryer @David Grosher 
Please refer to ticket above for information regarding an event that occurred this afternoon. I’ve taken my best stab at recommending a path forward to prevent a similar occurrence in the future. Feel free to add additional comments/recommendations.

### Cameron Chapman, 2025-03-06

@Cody Smisek thank you for the detailed reporting. Do we need to use batteries in the software area? An option may just be to provide wired power connections. Batteries may be needed for BMS checks, but checking voltages and limiting duration could be part of the procedures.

### Cody Smisek, 2025-03-06

@Cameron Chapman I defer to software team. they were using the battery so that they could conduct mag checks which requires a bunch of tumbles and turns. If in wired config, that would likely not work.

### Cameron Chapman, 2025-03-06

@David Grosher are there any low voltage GCS warnings that would warn an operator when battery voltage is below a safe operational voltage for ground test?

### Jeremy Kostel, 2025-03-07

@Cameron Chapman we have an intern starting soon right (I think Hayden said end of month)? This could be a good first project. Clean up batt cabinet, add some sort of tracking sheet for last known batt voltages, assemble a checker/charger station, etc. Doesn't necessarily need to come from EE team but might make the most sense

### Cameron Chapman, 2025-03-12

@Jeremy Kostel good idea. Assigning to Ranchit’s mentor @Hayden Jeanor and adding EE intern flag.

### Jeremy Kostel, 2025-04-08

@Cameron Chapman This same thing just happened again. Battery was plugged into vehicle and used for about an hour before reported to me. Battery measures at ~5V total pack voltage. Ticket linked to this issue https://jenaero.atlassian.net/browse/VXEP-1197

### David Grosher, 2025-05-20

This issue is not a VXEP incident and should not be in this project.  This is an internal process issue. @Pat Wells do you want to close this issue?

### Pat Wells, 2025-05-20

@David Grosher yes close. We were not tracking this.

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V797_250306_124645_pack.zip | archive | 5191 | 2025-03-06 | listed only |
| [XCL00056.csv](attachments/26946_XCL00056.csv.md) | csv | 591 | 2025-03-06 | converted |
| [XCL00058.csv](attachments/26943_XCL00058.csv.md) | csv | 624 | 2025-03-06 | converted |
| [XCL00059.csv](attachments/26944_XCL00059.csv.md) | csv | 1455 | 2025-03-06 | converted |
| [XCL00061.csv](attachments/26942_XCL00061.csv.md) | csv | 657 | 2025-03-06 | converted |
| [XCL00062.csv](attachments/26941_XCL00062.csv.md) | csv | 646 | 2025-03-06 | converted |
| [XCL00063.csv](attachments/26940_XCL00063.csv.md) | csv | 528 | 2025-03-06 | converted |
| image-20250306-222006.png | image | 20 | 2025-03-06 | listed only |
