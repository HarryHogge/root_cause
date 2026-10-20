# VXEP-1231: Training Software in the Loop (SIL)

- **Issue type:** Major Project
- **Status:** In Review
- **Priority:** High
- **Created:** 2025-02-24
- **Updated:** 2026-05-12
- **Reporter:** Jason Scherer
- **Assignee:** Scott Whitney
- **Creator:** Jason Scherer
- **Links:** relates to VXEP-1560 (LRR Software for April 2026 Final Delivery)
- **Sprint:** FS2 Sprint 31, FS2 Sprint 32, FS2 Sprint 30

## Description

Customer Handoff in April 2026
SharePoint Folder: https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/200%20-%20Software/Training%20SIL?csf=1&web=1&e=XQZsjj 
Confluence Page: Training SIL - Flight Systems - Confluence
Charter: LRR - Project Charter: SIMLAT Testing - SEIT Initiatives - Confluence
**Project Description**

The project aims to develop a stand-alone software simulation of the Stalker vehicle for training purposes. Focusing on a software-only solution eliminates dependency on physical vehicle hardware. The simulation will replicate the flight dynamics and operational scenarios of the Stalker vehicle. Targeted for the X86 architecture, the software will provide a robust training platform compatible with existing operator interfaces, specifically the Legacy Ground Control Station (GCS) and Onboard GCS (OGCS). It will simulate multiple vehicle configurations, including the VXE-30 Standard Stalker, VXE-30 MAGNSS, and VXE-30 HAVOC configurations, with extensible support for various payloads. An instructor interface will enable real-time control over the simulation, allowing pauses, environmental adjustments, and fault injection to enhance training realism and adaptability.
**Internal Release Schedule: https://jenaero.atlassian.net/wiki/x/EwD_Pg**

**Project Requirements**

Software requirements are captured here.
**General Requirements**

- Software-Only Solution: The simulation must operate independently of vehicle hardware, relying solely on software to emulate flight behavior and system interactions.
- Platform Compatibility: Must run natively on the X86 architecture to ensure accessibility on standard computing hardware.
- Existing Interface Integration: Seamlessly integrate with the Legacy GCS and OGCS applications, ensuring compatibility with their existing communication protocols and data formats. (OGCS is MVP, Legacy is not MVP)

**Simulation Capabilities**

- Stalker Flight Dynamics: Accurately model Stalker VTOL and Fixed wing flight modes, including transitionary phases, reflecting realistic aerodynamics and control responses.
- Vehicle Configurations: Support simulation of the following Stalker configurations:
- VXE-30 Standard Stalker (Priority 3)
- VXE-30 MAGNSS (Priority 1)
- VXE-30 HAVOC (Priority 2)
- Payload Flexibility: Include a modular framework to accommodate various payload configurations
- Jennings Payloads?
- Octopus Sensors
- Trillium Sensors (Not required for LRR)
- Mod Payload Sensors? (Note: There is a requirement in LRR for an API/SDK to allow for extension of capability for other 3rd party sensors. I think we would want some type of interface that allows us to track specific payload states relative to the aircraft so that it can be provided to the CONOPS sim. This is non-MVP. ) 
- Payload Meta Data?
- INS feeds?

**Instructor Interface**

- Simulation Control: Provide an intuitive interface allowing instructors to: (This interface may be provided by the CONOPS sim environment)
- Pause and resume the simulation at any point.
- Modify environmental conditions (e.g., wind speed, turbulence, weather) in real-time.
- Trigger faults (e.g., engine failure, sensor malfunctions) to simulate emergency scenarios.
- Mission Simulations Service for Real Flights
- User Feedback: Display real-time simulation status and fault conditions to the instructor for effective training management.

**Performance and Usability**

- Real-Time Performance: Ensure the simulation runs in real-time on X86 hardware, maintaining responsiveness during complex scenarios and transitions.
- Scalability: Design the software to allow future expansion, such as additional vehicle configurations or advanced training modules, without requiring significant rework.
- Initialization: The sim should be able to be initialized on the ground or in flight.

**Development and Support**

- Documentation: Provide documentation, including user manuals for instructors and technical guides for integration with GCS/OGCS systems.
- Testing: Validate compatibility with Legacy GCS and OGCS through rigorous testing, ensuring no disruption to existing operator workflows.

System Architecture: AP Firmware Functional Breakdown.vsdx
Initial Concept (04-01-25) from System Architecture doc above. This is subject to change as system design matures but provides an initial look at the application design.
[embedded: image-20250408-221049.png]
**Simlat (Products | Simlat)**

Simulation Environment & Control with synthetic full motion video (FMV) will be provided by Simlat software.
Simlat uses the gRPC protocol: Introduction to gRPC | gRPC
- Requirements Analysis: 
- Confirm System Requirements
- Refine system requirements into software requirements
- Scope all Operator Inputs (Work with Ted to understand/capture full list of GCS inputs).
- Design: (Create Hierarchical State Machine Design for)
- Need to Confirm Design Tool (Visual Paradigm or something else like Enterprise Architect)
- Need to procure licenses for chosen design tool
- Flight Modes
- Mission Management,
- VSM/GCS interface
- Logging
- …
- Development
- VSM/GCS integration
- Handshaking & Control/Reporting: Leverage documentation created for VSM development.
- Messages: Leverage message definition code from the VSM codebase.
- Documentation?

## Comments (11)

### Jason Scherer, 2025-02-24

@David Grosher  When you get a minute, please validate the requirements list. Let me know if I’m missing anything.

### Jason Scherer, 2025-02-24

@Scott Whitney  FYSA I created this EPIC to capture the work effort for the Training SIL deliverable needed by July. The description, design, requirements, and notional schedule are based on a discussion today between Dave, Ben, Scott H, and myself. Feel free to take over the Epic if you want.

### David Grosher, 2025-02-24

@Jason Scherer Requirements reviewed. Notes added.

### Jason Scherer, 2025-02-27

[embedded: image-20250227-193108.png]

### Jason Scherer, 2025-02-27

Current definition of a Waypoint in Fixed Wing code. From latlon.h
[embedded: image-20250227-193746.png]

### Jason Scherer, 2025-02-27

Summarized discussion on Waypoints between Ben and Jason regarding separation of logic between the “XComm SIL” and Simulink.
- The “XComm SIL” will perform mission management and waypoint Activation.
- The “XComm SIL” will send the next commanded waypoint to Simulink.
- Simulink will maintain an array three of waypoints
- Commanded (Where we are headed, after we get to the active waypoint) Waypoint (Last Commanded)
- Active Waypoint (Where we are headed now)
- Previous (Where we came from)
- Simulink will provide an event to indicate the active waypoint has been achieved.
- The “XComm SIL” will, if available, provide the next waypoint in the mission to Simulink when the “waypoint achieved” event triggers.

### Jason Scherer, 2025-02-27

Summarized discussion on launch sequence
- The “XComm SIL” will provide basic VTOL commands
- Launch with desired altitude.
- Abort
- Land Now (any time during flight)
- Simulink will manage the “get the vehicle in the air an at the desired altitude”.
- Simulink will not transition until a commanded waypoint is received.

### Jason Scherer, 2025-03-11

“XComm SIL” Software Requirements moved to sub task FS2-3096

### Jason Scherer, 2025-03-25

@Jo Brown Making you aware of this project in case you are not. This is an LRR product requirement. The intent is to run this on the GCS using a msys2 build environment. We are developing the build system now, and at some point, in the next few weeks, we should meet to ensure that our plan for environment, networking, etc. will work on a hardened GCS laptop.

### Scott Whitney, 2025-10-31

@Taylor Warner  @Gabriel Staples - we need to pull in the documentation and training (V1.0.0 - MVP - First Customer Release [Target mid-April 2026] [4 weeks]:). This can be done in parallel to V 0.4.0 and then wrapped up shortly after completing full mission capabilities (v0.5.0).

We need to aim to get the customer release done by end of March

### Taylor Warner, 2025-11-05

@Scott Whitney I’ve moved documentation/training into V0.4.0

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20250227-193108.png | image | 133 | 2025-02-27 | listed only |
| image-20250227-193746.png | image | 145 | 2025-02-27 | listed only |
| image-20250408-221049.png | image | 187 | 2025-04-08 | listed only |
