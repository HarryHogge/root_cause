# VXEP-453: VXE 592 crash on landing

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-07-01
- **Updated:** 2026-09-03
- **Resolved:** 2024-08-23
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** GNSS-Rate, MOLSON, Weekly-incident-tracker
- **Links:** relates to RMA-278 (VXE-592 240701 MOLSON); relates to RMA-292 (Octopus Gimbal E-140 EPS6170 - MOLSON ); relates to FS2-2059 (Investigate v592 Crash on Landing); relates to FS2-2058 (v592 Crash on Landing); relates to VXEP-1291 (VXE 592 Crash)
- **Customer:** MOLSON
- **Vehicle Tail Number:** 592
- **Issue Status:** On hold pending feature deliveries.
- **Incident Type:** Aircraft Loss
- **Severity:** 1 - Flight Critical

## Description

Relevant Files: 
Incident Logs: VXE 592 Crash on Landing
Incident Report: Has not been made yet 

Information received from customer:
Incident 6/27:
- Attempted landing (straight in pattern)
- Transitioned from glide to VTOL. 3 of 4 motors turned on. The 4th looked like it was trying to initiate.
- Front propeller turned back on.
- GCS indicated initiation of emergency glide down but they were parallel to active runway so they sent it for another pass back to IP 1. HLB was at 60%.
- The aircraft flew 200m and initiated VTOL with all 4 VTOL motors active in a  climb.
- Aircraft transition towards the original landing zone where it nose dived into a moving truck.
- HLB were at 30% at the time of the crash.

____________________
Provided procedures for post incident data collection. Customer unable to complete, AAR file not provided.
As of 7/1 aircraft is being shipped to SLO for hardware investigation and retrieval of data for investigation.

## Corrective Action

- Reconfigure receiver to send data at a lower rate.
- Use the actual delta time in the GPS update calculations
- Increase baud rate of the serial port to add margin to serial messages
- Land Abort fixes documented in linked issues.

## Root Cause

- PLZ Overshoot caused by the GNSS receiver rate change.
- Land Abort bug resulted in both APs trying to control the vehicle.

Both are known issues and are being addressed in the upcoming SW release.

## Comments (19)

### Pat Wells, 2024-07-01

@Sean Odell please ensure you create RMA ticket for return and link to this investigation.
When the aircraft arrives in SLO in must be delivered to engineering on the same day to expedite the investigation process.

### Sean Odell, 2024-07-01

@Pat Wells RMA ticket Created

### Alexander Alan Arnold, 2024-07-01

added AAR file from incident

### Alexander Alan Arnold, 2024-07-01

@David Grosher Can you please review the attached AAR when able. Thanks in advance!

### Pat Wells, 2024-07-01

AAR is incomplete.  Aircraft has been shipped to SLO and will be delivered to Engineering for recovery of the data.
@Alexander Alan Arnold @David Grosher

### Sean Odell, 2024-07-10

@Greg Fryer @Cameron Chapman Aircraft has been delivered to the engineering racks. Please have your team start there investigation on the physical plane. 
@Pat Wells FYSA

### Cameron Chapman, 2024-07-10

@Adrian Garcia can you please pull all logs around this incident from this aircraft? Due to damage, please inspect equipment and PCBs and power up carefully (resistance check first).

### David Grosher, 2024-07-11

@Eric Brewer @Jason Scherer An initial look into this seems to indicate the following: 
- PLZ Overshoot was likely due to large descent and non-optimal GNSS update rate.
- A Land Abort was issued due to a power fault (probably low power), but the Lift system remained active. Note: the hostState shows that the VTOL system returned to FW Flight but the lift system was still engaged. It is unclear to me that this would be fixed with the current fixes.


Note: the data is at the link above, not the attachment. VTL00063.csv is where the incident occurs.

### David Grosher, 2024-07-11

@Scott Whitney FYI, see below. Can you create FS2 tickets to track this investigation for Jason and Eric.

### Scott Whitney, 2024-07-11

Created https://jenaero.atlassian.net/browse/FS2-2059 to track work.

### Jason Scherer, 2024-07-11

@David Grosher This land abort occurred during the LAND_WAITTRANS TestLandAbort (LA-02-008-02) code path which has been confirmed to activate the land abort bug. The bug which causes simultaneous independent control by both autopilots. I believe the current release candidate, that we are testing right now, would resolve this behavior since it would have cut the vtol motors thereby preventing the vtol from effecting the vehicle. 
The debug/xcomm event logs indicate the abort was caused by a low power fault. Meaning the lift system did not consume enough power during landing. This would indicate the lift system was not functioning properly.
You have to look at the XComm data to confirm low power since XComm is the one monitoring and triggering power faults. The power chart on XComm shows low power (<500W) for a large chunk of the landing which is not normal. Based on XComm data, the lift system was not consuming the expected amount of power.
The below figure is XComm data charted with the XComm event log. The log messages in the XComm event log have been matched to the fixed wing code that triggered the abort.
A summarized sequence of events that would lead to this abort would be the following:
1.) Fixed Wing is managing the landing by sending commands to VTOL
2.) The XComm is accumulating error counters based on low power consumption by the lift system. Eventually the error counter reaches the threshold which triggers a low power fault.
3.) The fixed wing ap has reached the LAND_WAITVTOL state by this time. Once the fault is triggered by XComm the fixed wing autopilot initiates the abort.
[embedded image-20240711-201820.png]
The charts and annotations are in the excel file XCL00055-JS.csv which have been uploaded to the SharePoint folder.

### Eric Brewer, 2024-07-22

@Jason Scherer nice work.  Note that the VTOL low power is caused in large part by the 5hz GPS update rate issue we’ve observed previously.  Due to attitude errors in the VTOL controller, the vehicle does not pitch up far enough on transition and the speed is not arrested.  As a result, when the VTOL system kicks on it commands a low power setting since we are still getting too much lift from the fixed-wing system.  Let me know if you need me to add plots, but it’s the same signature we’ve seen on several other birds. @David Grosher FYI.

### David Grosher, 2024-07-22

@Eric Brewer Please add the plots. I think Pat wants to provide them a solid report on the incident.

### Eric Brewer, 2024-07-22

@David Grosher @Pat Wells @Jason Scherer added plots to summary slides here.  Let me know if there are questions or any requests for modification.

### Pat Wells, 2024-07-25

@Eric Brewer @Jason Scherer @David Grosher customer reached out today for an estimated completion date on the mishap report.  Has this one been approved for final release?

### David Grosher, 2024-07-25

@Pat Wells Yes, you can send them the final report.

### Pat Wells, 2024-07-26

Report provided to customer on 7/25

### Sean Odell, 2024-10-10

@David Grosher Does your team need any of the hardware from this incident. We need the transit cases in Final Assembly to get prepped and cleaned for the replacement.  
@Cameron Chapman @Greg Fryer FYSA

### David Grosher, 2024-10-10

@Sean Odell No, we have completed the investigation.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 1000000834.jpg | image | 1322 | 2024-07-01 | listed only |
| T95_V592_240627_162830_pack(AAR Canada).zip | archive | 570 | 2024-07-01 | listed only |
| image-20240711-201820.png | image | 387 | 2024-07-11 | listed only |
