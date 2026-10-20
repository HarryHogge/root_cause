# VXEP-67: Firmware release process is inadequate and results in improper testing of semaphore allocation.

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-09-18
- **Updated:** 2026-02-02
- **Resolved:** 2025-05-19
- **Reporter:** David Grosher
- **Assignee:** David Grosher
- **Creator:** David Grosher
- **Links:** relates to FS2-948 (Investigate Debug Assertion that has been disabled to enable Debugging with ICE); relates to FS2-970 (Add Control loop integrator states to VTOL AP log file); relates to FS2-971 (Audit samephore use in FwAero.c on external get functions); relates to FS2-969 (Evaluate Assertion DEBUG changes)
- **Issue Status:** Complete
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

In the VTOL AP release build Edge macros are used to take and give semaphores.  In these macros, there are checks if the provided semaphore is null and if it is then it won’t request to take/give the semaphore.  No error is thrown and the program continues.  This means that if a semaphore is null then the program will not fail and will not protect shared resources between tasks and presents the possibility of random “low rate” (needs to be defined) memory corruption.  
[embedded: image-20230919-031537.png]
In Debug builds of the VTOL AP, these macros are not used. The result is that uninitialized or null semaphores can be identified and fixed. However, when attempting to run tests in debug mode a null semaphore was identified in the airdata task (UPDATE 9/26) FwAero.c component. This indicates that proper tests with the Debug build have never been executed or were executed with an improper configuration that masks exceptions from the null semaphore.  
Further, the current debug methodology specifically configures the application to ignore these exceptions. 
The full impact of this issue is unclear and is currently being prioritized.  
The above was discovered during the course of the WDT investigation but the current expectation is that it is unlikely to be the cause of the WDT events and should be tracked independently due to the potential severity and required process changes that will be necessary to address the issue. 
UPDATE 23-09-21: Incident Response Team for this Issue: 
@Sam Miller - Airworthiness Authority
@Greg Fryer - Deputy Airworthiness Authority, VXE Product Owner
@David Grosher  - Director of Flight Systems, Investigation lead
Investigation Team: @John Clark @Scott Hunter @Kurt Burian @Former user 
UPDATE 23-09-22:  Test builds were created in both release and debug configurations. 
Changes to the debug build were made such that it was no longer configured to ignore the exceptions described above, it also trapped the process on an exception such that it could be more easily debugged. During testing with the debug build, it was found that one semaphore was not initialized properly, aeroMutex in FwAero.c. Data protected by this semaphore flows into various navigation functions and a function in which an IMU correction is performed.  Updates were made to address the issue and a pull request is currently under review by the team.  
A release build without the checks for null pointers in the semaphore give/take macros was created to validate issues identified and fixed during testing with the debug build. 
During discussion with the team, the preferred solution was to implement static allocation of the semaphores upon declaration bypassing any issues with asynchronous initialization. However, this solution is only enabled in FreeRTOS v10, which is currently in progress as part of the Embedded SW robustness initiative.  In the meantime, the intent is to address the issue of null semaphores procedurally by updating the regression test matrix to include test points with a debug configured build to enable identification of any null semaphore that could possibly have been introduced during the SW development process. Further, the debug build documentation will be updated to remove any procedure that masks these errors. 
Lastly, we are considering identifying a training program on embedded SW best practices for real-time safety critical systems. 
UPDATE 23-09-26: The pull request was built and tested independently by David C. The pull request was approved following some additional review.  The pull request went to main and will be included with the upcoming GNSS fixes that will be delivered at the end of the current sprint scheduled for Oct 8th. 
The team also identified additional low frequency diagnostics that will be useful for identifying if/when data corruption occurs and if it flows through the control system.  An issue was created and linked to this issue with a target delivery of the upcoming release. 
Additional research is on-going for longer term improvements related to this issue with respect to the semaphore implementation and allocation strategy. 
Due to the work executed related to running debug firmware images with an ICE tool, I have transitioned the state of this issue to INSPECTING HARDWARE and then to FIRST LOOK ASSESSMENT. 
The severity level of this issue will not be updated, it is still 1-Flight Critical. The issue state will be transitioned to UPDATING SEVERITY LEVEL where it will stay while containments are discussed.  
The current proposed containment is as follows: 
- Upcoming immanent release of the hotfix merged to main to fix the initialization of the semaphore in FwAero.c and the update to the Debug build to facilitate future issues with null semaphores.
- Changes to the release testing procedures to include test points with a debug image to identify null semaphores.
- Including low rate logging of control loop integrator states as a tool to indicate whether invalid data can percolate down to the control loops.
- Some form of advisory notice (AWD, Safety Advisory or Service Bulletin to inform end users. This is to be determined.


UPDATE: 1/30/2024
It has been discovered that 32-bit writes are atomic on the processor. Therefore the impact of this bug in the current build is limited to non-existent.  Having said that the proposed corrective actions (1), (2) and (4) will still be implemented. The Severity of the issue has been modified to reflect this new learning.

## Corrective Action

The current proposed containment is as follows: 
- Upcoming immanent release of the hotfix merged to main to fix the initialization of the semaphore in FwAero.c and the update to the Debug build to facilitate future issues with null semaphores.
- Changes to the release testing procedures to include test points with a debug image to identify null semaphores.
- Some form of advisory notice (AWD, Safety Advisory or Service Bulletin to inform end users. This is to be determined.

## Root Cause

Non-initialized semaphore used and ignored in code. Test procedure didn’t include a test point to test with a debug build that could catch the error.

## Comments (4)

### David Grosher, 2023-09-18

@Greg Fryer FYI, this is not displaying on the VXE Problem Kanaban board due to the filter settings for Major Problems. I could not update the filter because you are the owner. Could you update the filter, thanks.

### David Grosher, 2023-09-18

@Former user This issue will follow the 8D workflow that we discussed. Please add or correct details as required.

### Former user, 2023-09-21

Asserts are used for a reason. They are meant to trap on errors that are detrimental to the operation of the system. The bigger issue is determining an assertion failure. In some cases, asserts can happen in very early initialization (I.e. segment copies into RAM .data, .bss, etc.). This occurs way before a UART can even be initialized (can’t initialize drivers without variables). So even hooking up to a serial port will be frustratingly un-effective. 
The solution is to use what is called semi-hosting. This spec will cause printf’s to redirect to the JTAG debugger as opposed to a UART. You will see assertions by way of a debugging console connected directly through the JTAG debugger. You can also do some pretty advanced debugging by way of fopen. The file can actually be opened on the host debugging machine and all data written to it can be captured and viewed there instead of trying to write to a flash file system of sorts.
We probably should look into using a SEGGER J-LINK probe as an evaluation. I know that it does support Microchip’s IDE and their ICSP interface. We can also use Ozone, which is a much more capable debugger then MPLABX.
Here is more information:
J-Link BASE Compact (8.19.00) - SEGGER U.S. Web Shop ($498)
Microchip MPLAB X (segger.com)
Semihosting - SEGGER Wiki

### David Grosher, 2025-05-19

This issue was addressed in v6.3.4. Regression test procedures were updated to account for the process gap.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20230919-031537.png | image | 63 | 2023-09-18 | listed only |
