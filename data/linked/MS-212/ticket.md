# MS-212: Integrate Fuel Cell Command and Report

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-04-03
- **Updated:** 2024-10-16
- **Resolved:** 2024-10-16
- **Reporter:** Craig Burton
- **Assignee:** Craig Burton
- **Creator:** Craig Burton
- **Fix versions:** 1.1
- **Parent:** MS-195 Integrate AP Data and Commands with ICD Reports and Commands for v1.1
- **Links:** is blocked by MS-257 (Bundle Fuel Cell Simulator for Distribution); blocks OGCS-4 (Fuel Cell); is blocked by FS2-2328 (XCOMM Message to support Fuel Cell); is blocked by MS-442 (FC HIL Cables)
- **Epic Link:** MS-195
- **Sprint:** MS Sprint 21

## Description

Implement private messages #17005 and #16005 to command and report Fuel Cell status.  Support for the FC will also impact messages #16004 and #1403.

## Comments (10)

### Scott Whitney, 2024-09-12

Need support from Jason to add message to support Fuel Cell

### Jason Scherer, 2024-09-26

@Craig Burton Do you need a custom update to XComm, or do you just need the fuel cell simulator running to test?

### Craig Burton, 2024-09-26

@Jason Scherer I don’t think we’ll need a custom update, unless we run into significant trouble during integration.  For now, I think the simulator and cable will be sufficient.  A high level procedure might be helpful as well.  If there is no documentation, we’ll read the Edge GCS code.

### Jason Scherer, 2024-09-26

@Craig Burton Since you don’t need a development change, I’ll take on the task of creating documentation for existing messaging that you can use on the MCM.

### Craig Burton, 2024-10-01

@Scott Whitney With 1.1 due in 3 weeks, we are in immediate need of two FC HIL cables.  Ideally, we’d have one on Buckeye and I’d have one on HIL 105 so that @Ted Trowbridge and I can work in parallel, since we both have changes for FC integration.  OGCS has to be able to set up a FC within the launch wizard and VCSi needs to be able to control the FC through the VSM.

### Scott Whitney, 2024-10-02

@Craig Burton I will work on getting these created. Is the cable an immediate blocker?

### Craig Burton, 2024-10-02

@Scott Whitney We have plenty to keep us busy, so no.  But this feature is blocked.  If we can get a cable or two early next week, that would be great.

@Jason Scherer  looked at my HIL and thought it might be straightforward to solder the serial cable directly to the harness, which would avoid needing a special connector on each side.  For Buckeye, we may want to use a connector, I don’t know.

### Jason Scherer, 2024-10-02

@Scott Whitney @Craig Burton I can/will create enough to get the two HILs working. I thought we were delivering the cables to partners, so I figured it would be better to have them be more professional. However, given the resource constraints of the hardware team, I can build enough for Craid/Ted to continue development. Craig bring your HIL with you tomorrow, and I can solder a USB to serial cable directly into your harness, and we can give it a quick test.

### Craig Burton, 2024-10-03

@Scott Whitney Setting to “To Do” from “Blocked” – @Jason Scherer modified HIL #105 with a USB/Serial cable and provided a quick tutorial on how to run the FuelCellSimulator application.  Jason is planning on showing @Ted Trowbridge and I an additional overview soon, possibly tomorrow.

### Scott Whitney, 2024-10-04

Great. EE team will have an additional set of harnesses by next week

## Attachments (0)
