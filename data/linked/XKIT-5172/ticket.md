# XKIT-5172: B40 CAN Issues Investigation

- **Issue type:** Epic
- **Status:** In Process
- **Priority:** Medium
- **Created:** 2025-11-04
- **Updated:** 2026-09-16
- **Reporter:** Jeremy Kostel
- **Assignee:** Abel J. Markow
- **Creator:** Jeremy Kostel
- **Links:** relates to VXEP-1568 (VXE-818 Lift System didn't disengage - Crash - CAN bus error ); relates to XKIT-5113 (B40 Non Flight-blocker flight test issue collector/Squawk List); relates to FS2-3875 (B40 Investigations ); relates to XKIT-5384 (Evaluate Using Update CAN Servo FW (2.3.0) ); relates to VXEP-1999 (B30 ADVNAV CANJAM CAN Issues)

## Description

@Jeremy Kostel need status on MVP, workarounds found… what will it take to get higher confidence included in MVP? high priority to be included in MVP.

Main ticket for tracking B40 CAN issues

Helpful Links:
Sharepoint Data: IRAD - Documents - CAN Investigations - All Documents
V882 Ground CAN Monitoring: IRAD - Documents - V882 Ground CAN Monitoring - All Documents
Electrical Investigation: CAN Investigation.pptx

Environment / Bus Setup
- Topology: Linear
- Termination: 120 Ω in tail harness + 120 Ω in left boom harness (correct)
- Bitrate: 500 kb/s
- Node count: 14
- XCOM + VTOL AP CAN transceivers: not transformer-coupled
- ESC CAN ground reference: “28 V Critical RTN” (separate from power ground)

Issue
When any/all ESCs are powered on the system, the CAN bus exhibits ~2% error rate. Dominant error class: ACK Delimiter related. With ESCs unpowered, the bus is error-free.
Observations
- Errors begin only after ESCs power-up.
- Network otherwise stable and properly terminated.
- Most error reports point to ACK Delim violations.
- Digital ground for ESCs tied to 28 V Critical RTN; CAN and power grounds are intentionally separate.

Hardware Concerns (suspected contributors)
- Lack of transformer coupling on XCOM/AP CAN transceivers may reduce common-mode noise immunity.
- ESC digital ground referencing (28 V Critical RTN) could introduce ground potential differences / common-mode shifts during ESC power states.

Impact
- ~2% bus error rate with ESCs powered; risk to command/telemetry reliability.

## Plan

- Plan for 11/25/26 is to continue collecting CAN data and perform a hover test, with the goal of flying tomorrow morning. Hargrave has signed off on flying with this firmware and confirmed it doesn’t change any motor-drive or other safety-critical parameters, so it should be safe to fly as is.
- @Abel J. Markow is working on two different PCBs to potentially introduce into the system. 
- The first board will deal with transformer coupling the output from both the XCOM and VTOL AP
- The second board will handle better isolation of returns at the ESC

## Issue Status

Error rate: 
Our CAN controllers use a parameter called SJW, which lets the node shift its sampling point on each bit to track edges. A large SJW allows big shifts; a small SJW only allows small corrections. We know our AP hardware produces slightly odd-shaped ACK pulses, and I can reproduce those on the bench with just the XCOM and VTOL boards.
 Per our request, Hargrave provided firmware that makes the sample point configurable. To do that, they had to significantly reduce the SJW value so the sample point stayed where we intended. This effectively prevents the ESCs from “chasing” our deformed ACK edges and pulling the sampling point into bad timing regions, which is what appears to have been causing the errors.
 The key point is that these slightly deformed ACKs are still valid and readable by all nodes; the ESC was just trying to be overly “smart” in compensating for older hardware behavior. I’ve asked Hargrave for a second firmware variant with configurable SJW so we can fully validate this theory, but so far all the data supports it: we now have several hours of CAN logs with 0.0% errors (confirmed by the ESC, PCAN logger, internal tools, XCOM, and VTOL) on the vehicle.
 Plan for today is to continue collecting CAN data and perform a hover test, with the goal of flying tomorrow morning. Hargrave has signed off on flying with this firmware and confirmed it doesn’t change any motor-drive or other safety-critical parameters, so it should be safe to fly as is.

Best update found here: https://jenaero.atlassian.net/browse/XKIT-5230 
But changing SJW parameter gives us a 0.0% error rate and will be continued in use for MVP

## Comments (3)

### Jeremy Kostel, 2025-11-12

A few notes i want to write down:
- the voltage shift on SOF both exists with AND without ESC powered - but are frequently not associated with errors. These are present on B35X as well
- [embedded: T3DSO2204A_PNG_496-20251112-100902.png]
- Every message FROM the ESCs consists of deformed square waves. One is displayed here with an error - but error free exhibits the same behavior 
- [embedded: T3DSO2204A_PNG_494-20251112-100612.png]
- The image below is a nice demonstration of the first message FROM the AP and the second one FROM the ESC. You can see the deformation of the waveform
- [embedded: T3DSO2204A_PNG_491-20251112-094532.png]

### Jeremy Kostel, 2025-11-12

Additional finding: while putting the ESCs on the same 28V bus does clean up the waveform - the same errors persist

[embedded: T3DSO2204A_PNG_507-20251112-111004.png]

### Cameron Chapman, 2025-11-25

11/25 Update from Jeremy
Here’s a brief summary of the recent CAN changes and why they help.
 
Our CAN controllers use a parameter called SJW, which lets the node shift its sampling point on each bit to track edges. A large SJW allows big shifts; a small SJW only allows small corrections. We know our AP hardware produces slightly odd-shaped ACK pulses, and I can reproduce those on the bench with just the XCOM and VTOL boards.
 
Per our request, Hargrave provided firmware that makes the sample point configurable. To do that, they had to significantly reduce the SJW value so the sample point stayed where we intended. This effectively prevents the ESCs from “chasing” our deformed ACK edges and pulling the sampling point into bad timing regions, which is what appears to have been causing the errors.
 
The key point is that these slightly deformed ACKs are still valid and readable by all nodes; the ESC was just trying to be overly “smart” in compensating for older hardware behavior. I’ve asked Hargrave for a second firmware variant with configurable SJW so we can fully validate this theory, but so far all the data supports it: we now have several hours of CAN logs with 0.0% errors (confirmed by the ESC, PCAN logger, internal tools, XCOM, and VTOL) on the vehicle.
 
Plan for today is to continue collecting CAN data and perform a hover test, with the goal of flying tomorrow morning. Hargrave has signed off on flying with this firmware and confirmed it doesn’t change any motor-drive or other safety-critical parameters, so it should be safe to fly as is.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T3DSO2204A_PNG_491-20251112-094532.png | image | 62 | 2025-11-12 | listed only |
| T3DSO2204A_PNG_494-20251112-100612.png | image | 57 | 2025-11-12 | listed only |
| T3DSO2204A_PNG_496-20251112-100902.png | image | 61 | 2025-11-12 | listed only |
| T3DSO2204A_PNG_507-20251112-111004.png | image | 70 | 2025-11-12 | listed only |
