# VXEP-1803: VXE 658 Fuel Cell cut out on Launch and had to be recovered on HLB

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2026-03-31
- **Updated:** 2026-10-05
- **Resolved:** 2026-10-05
- **Reporter:** Stephan Johnson
- **Assignee:** Alexander Alan Arnold
- **Creator:** Stephan Johnson
- **Labels:** RCCA, Software, TIQUILA, Weekly-incident-tracker
- **Customer:** TIQUILA
- **Vehicle Tail Number:** VXE-658
- **Vehicle Configuration:** AdvNav; Fuel Cell
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround
- **Components (EA Aircraft):** Fuel Cell
- **Executive Summary:** Investigating root cause; probable cause Operator Error

## Description

VXE-658 Fuel Cell cut out on Launch and had to be recovered on HLB

## Issue Status

--Cody Smisek writes--
FanEn was set to 0 at startup of fuel cell in xcomm log 42 (dated 3/30/2026). Based on 12v current, fan appears to have been working when enable was set to 1. 
Prior to fan being disabled, appeared FC state was in a state other than idle/off (state 6, not sure if this is cooldown or running)
Xcomm log 35 through 42 all occur on 3/30/2026 for interested parties. 
--END--

## Root Cause

The stack was still in cooldown when initialization was attempted, which caused a fault back into cooldown, then it was initialized a second time from cooldown and began normal operation except the nose cone fan never turned on causing damage to FC electronics.

## Comments (22)

### Jackson Riley Curvin, 2026-07-08

@Charles Sweet Thank you for the quick response. How would we go about testing this?

### Sean Wendling, 2026-07-08

Hey Jackson, 
Aircraft Nose Cone fan should be running whenever the fuel cell is active in the fuselage. You could test it by placing your hands in front of the mesh vents on the nose while the fan should be running and you can feel the airflow there. No airflow means that the fan is not functioning. 
We came to this conclusion due to the AmbTemp on the Fuel Cell reaching 88C which has been an indicator in the past of Nose Cone Failure. 
@Charles Sweet , could you prepare a plot of the fuel cell ambient temperature over the course of the flight. We should observe an ambient temperature starting at outside ambient but then creeping up to that 88C metric you showed me as the stack heats up.

### Charles Sweet, 2026-07-08

[embedded image-20260708-143637.png]
@Sean Wendling Ambient temperature is plotted on the secondary axis to the right.

### Charles Sweet, 2026-07-08

[embedded image-20260708-154339.png]

### Cody Smisek, 2026-07-08

@Sean Wendling nose cone fan turns off during transition to fixed wing. 
@Charles Sweet I would highly recommend including dates/times on these plots so that others can references which dataset you’re referring to. I’m looking at the xcomm log 42 which seems to suggest the nose fan was running when it was set to run.

### Cody Smisek, 2026-07-08

Seems we’ve got a software issue. I’d start chasing why did the fan enable set to off. @Sean Wendling @Charles Sweet @Jackson Riley Curvin 
[embedded image-20260708-170217.png]

### Cody Smisek, 2026-07-08

[embedded image-20260708-173231.png]
[embedded image-20260708-173325.png]

Probably something to do with the state the FC was in prior to all of this. It looks like it was running then shut down then started back up?

### Charles Sweet, 2026-07-09

@Cody Smisek In the beginning of XCL0042 we can see the stack state is still in cooldown, it looks like it was put into initialize before the stack was fully cooled down (CPU Time 515.549). This caused the anode fan to initialize while the cathode fan was still running at high RPM, creating a backpressure within the stack which causes the anode to be unable to flow properly causing the first critical fault 0x3c20, shutting the stack down. It looks like (what I assume to be) a start/stop cycle was able to bypass the critical fault and initialize the stack again.

### Jackson Riley Curvin, 2026-07-20

@Cody Smisek what are you recommended next steps?

### Cody Smisek, 2026-07-20

@Jackson Riley Curvin See comments from July 8. 
[embedded image-20260720-150105.png]
Next steps are for software teams from AA and SLO to collaborate and determine how/why state machines of the system missed enabling the fan.

### Drew Hildreth, 2026-08-27

@Charles Sweet the customer is pushing on this again. Can we get some movement, so we close this out with the customer.

### Charles Sweet, 2026-08-27

@Drew Hildreth  I’m not sure what further can be provided here from the FC side, the stack was still in cooldown when initialization was attempted, which caused a fault back into cooldown, then it was initialized a second time from cooldown and began normal operation except the nose cone fan never turned on causing damage to FC electronics.

### Cody Smisek, 2026-08-27

@Cody Smisek @Drew Hildreth refer to comment above for next steps.

### Drew Hildreth, 2026-08-27

@Cody Smisek Appreciate it.

### Drew Hildreth, 2026-08-27

@Charles Sweet Thanks Charles.

### Drew Hildreth, 2026-08-27

@Alexander Alan Arnold please have the team work on a short report that I can send next week highlighting operator actions within the fishbone.

### Alexander Alan Arnold, 2026-09-01

@Charles Sweet When you have some time can we create a short slide deck referencing investigation, how it got into the state it was in, what the operator should do etc?

### Charles Sweet, 2026-09-01

@Alexander Alan Arnold For sure, I’ll get something started today to review when possible

### Charles Sweet, 2026-09-11

[embedded file]

### Stephan Johnson, 2026-10-05

An unconcluded cooldown cycle prior to initialization of the fuel cell.

### Charles Sweet, 2026-09-11

[embedded file]

### Stephan Johnson, 2026-10-05

An unconcluded cooldown cycle prior to initialization of the fuel cell.

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 20260330_SGCS1-211_ADR_EAGLE_658.zip | archive | 20759 | 2026-03-31 | listed only |
| image-20260708-143637.png | image | 47 | 2026-07-08 | listed only |
| image-20260708-154339.png | image | 15 | 2026-07-08 | listed only |
| image-20260708-170217.png | image | 82 | 2026-07-08 | listed only |
| image-20260708-173231.png | image | 131 | 2026-07-08 | listed only |
| image-20260708-173325.png | image | 8 | 2026-07-08 | listed only |
| image-20260720-150105.png | image | 27 | 2026-07-20 | listed only |
| [InvestigationReport VXEP 1803.docx](attachments/64504_InvestigationReport%20VXEP%201803.docx.md) | docx | 127 | 2026-09-11 | converted |
