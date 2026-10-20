# VXEP-416: VXE 539 Failure to launch

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-05-22
- **Updated:** 2026-03-02
- **Resolved:** 2025-04-08
- **Reporter:** Pat Wells
- **Assignee:** Jason Scherer
- **Creator:** Pat Wells
- **Labels:** FlightSystems, TIQUILA, Weekly-incident-tracker
- **Links:** relates to ENG-3074 (539 Failure to Launch); relates to FS2-1992 (VXEP-416 Investigation (v539) Failure to Launch); relates to FS2-1993 (VXEP-416 Failure to Launch - Vehicle Investigation); relates to RMA-358 (VXE-539 TIQ 240924); relates to FS2-2320 (Make XComm->VTOL SAFE On/Off messages require acknowledgements); relates to FS2-2854 (Jason's Open Investigations); relates to VXEP-1568 (VXE-818 Lift System didn't disengage - Crash - CAN bus error )
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 539
- **Plan:** Implement defined corrective actions.
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Current Investigation Report: Vehicle Investigation VXEP-416 v539.pptx

Information as reported by Lockheed FSR
During a training flight the aircraft was armed, and launch was selected. The aircraft did not respond. Three attempts were made. During one attempt the VTOL message “Launch abort, lift power fault” was displayed.

Additional information received from Lockheed FSR on 5/22
“Yesterday, V539 flew its first flight of the day with no issues.  During Launch Wizard for its second flight, it failed the first Sensor Calibration, then passes a few seconds later, and passed the second Sensor Calibration the first attempt.  When commanded to Launch, the screen said “Waiting to detect launch” for about a minute, the window to “Enable User Launch Control / Abort“ was open.  I noticed the VTOL status window on the right of the screen said Entering RTL mode (RTL = Return To Launch point).  The plane had aborted the launch before engaging the lift rotors.  The “Waiting to detect launch” and “Enable User Launch Control / Abort” windows remained open.  We enable user launch control and commanded “Cut motors and safe vehicle”.  Instead of closing, the window changed back to “Enable User Launch Control / Abort” window.  We disconnected from the plane and closed and restarted the CGS software.  The “Cut motors and safe vehicle” was still open.  Resetting the autopilot (in the launch wizard) did not result in the window closing. 
On the second launch attempt, all four lift rotors engaged at a low power setting.  The plane did not come close to lifting out of the stand.  The “Enable user launch control” button was open, but grayed out and we were not able to enable user launch control or command Cut motors and safe vehicle (from that window).  The autopilot aborted the launch.  VTOL status window said “Landed”.
 We produced a second AAR w/ FDR. 
We disconnected from the plane, closed the GCS software, and restarted the GCS laptop.  We disconnected the aircraft main power cable from the main battery, waited 10 seconds, and reconnected it to fully reset the plane.  Third launch attempt was like the first: the screen continued to say Waiting to detect launch and the VTOL status said Entering RTL mode.  A third AAR w/ FDR was produced and the plane was put away.”

AAR files attached

## Corrective Action

1.Update software to ensure delivery of SAFE ON/OFF commands between XComm and VTOL. 
- https://jenaero.atlassian.net/browse/FS2-2320

2.Fix logging software to positively confirm transmission of the SAFE OFF message. 
- https://jenaero.atlassian.net/browse/FS2-2205

3.Update software to reset VTOL autopilot during software resets. 
- The GCS now does this in the new release.

## Issue Status

Investigation Complete. Corrective actions consist of firmware changes, and have been defined and queued for resources to implement.

## Root Cause

A missing SAFE off command from XComm to VTOL AP prevented first launch and put the VTOL AP into an RTL loop which prevented second launch.

## Comments (27)

### Jason Scherer, 2024-09-11

@Cameron Chapman I’m still adding some supporting documentation to the report, but I’ve added the CAN timeout evidence. I would like to get a hardware engineer to weigh in on the health of the CAN bus on this vehicle considering the reported CAN bus timeouts between XC and VT. I’m not sure if this is a general VXE issue, or specifically related to this vehicle. We do have other flights recorded in our database that show even greater numbers of CAN timeouts, although disconnecting CW can also produce timeout events based on my HIL testing. I can rule out CW disconnects as the cause for this incident because the VTOL event log doesn’t show power resets. 
One idea we could try is to have them switch CW and see if the timeouts continue.

### Cameron Chapman, 2024-09-11

@Jason Scherer please coordinate with @Mark Squillante

### Mark Squillante, 2024-09-12

@Pat Wells I spoke with @Jason Scherer and we both agree that we will need the aircraft shipped back to determine the reason for the CAN failure.

### Pat Wells, 2024-09-13

@Mark Squillante @Jason Scherer Got it. We’ll request that the customer sends the aircraft in for further evaluation.
@Sean Odell please begin the RMA process and ensure that it’s delivered to Engineering when we receive it and update the group upon receipt.

### Pat Wells, 2024-09-24

@Sean Odell  have you received this aircraft from LM?

### David Grosher, 2024-09-24

@Jason Scherer Create tickets for CAs

### Sean Odell, 2024-09-30

@David Grosher Aircraft photographed and inventory taken. Aircraft has been delivered to Engineering to continue the investigation. Please assign to whoever on your team you would like.
@Pat Wells FYSA

### David Grosher, 2024-09-30

@Jason Scherer AV is available.

### Jason Scherer, 2024-10-18

@Pat Wells @David Grosher @Scott Whitney @Cameron Chapman Update
After initial EE review the CAN bus appeared to be electrically healthy. I’ll have to let @Mark Squillante report on that when he returns from leave (10/29). 
After the initial electrical checkout, I recorded a series of data captures with CAN bus data on this vehicle. I then analyzed this data using a logic analyzer, CAN protocol analyzer, and a custom application. 
My conclusion is that this vehicle CAN bus is working properly. 
Detailed explanation: A CAN timeout is defined by our software as, more than a second of gap between CAN data from a given processor. So for example, if XComm doesn’t see any CAN data from the VTOL processor for over 1 second, it flags it in the data log as a timeout for VTOL CAN data. This is what we saw in the AAR provided by the customer in this incident. I now believe that we have a general software issue, that deserves more investigation but is not specific to this vehicle.
In a 53-minute capture, I have no evidence of a timeout occurring. The max delay, in 53 minutes of data, is 505 milliseconds from the XComm processor, which is to be expected as XComm generates less traffic than the other processors.
Here is a summary of the data captured in the last 53 minute capture file.
[embedded image-20241018-173301.png]
So, while we did see some timeouts (1-3) logged in the AAR (which is actually a low number compared to the incident flight db), I believe this vehicle has a functional CAN bus. As I said above, there is probably a general software related issue with CAN data that needs further investigation.
Regarding the root cause of this incident, which is a missing SAFE Off message to the VTOL, we have created tickets for corrective action in the firmware which requires positive confirmation of message delivery before proceeding with the launch sequence.
With all that having been said, I believe this vehicle is functioning as well as the rest of our vehicles, and I think we can button it back up and return it to the customer.
Thoughts? Is there any further testing/data that should be completed before we can close this investigation?

### Scott Whitney, 2024-10-23

@Cameron Chapman - Mark is until Tuesday (10/28). Is there another engineer that can review the CAN bus and give the thumbs up to ship back to the customer?

### Mark Squillante, 2024-10-29

@Scott Whitney I agree with @Jason Scherer's assessment regarding the hardware. I saw nothing that would point to a hardware issue on the CAN bus. The CAN signals looked healthy and the wiring looked good.

### Jason Scherer, 2024-10-29

@Sean Odell @Scott Whitney Vehicle 539 has been delivered to RMA to prep for return to the customer.

### Scott Whitney, 2024-10-29

FYSA @Sean Odell - the CW hatch needs to be resealed and the Avionics needs to be reinstalled.

### Pat Wells, 2024-11-05

@David Grosher @Cameron Chapman Is the final report approved on the engineering side for release to the customer?

### Cameron Chapman, 2024-11-06

@Pat Wells I recommend asking @Jason Scherer who made the report, but since the report says investigating status, it does not look complete.

### Alexander Alan Arnold, 2024-12-10

@Jason Scherer Should this be moved out of D4 and is the report close to being completed?

### Pat Wells, 2025-02-04

@Jason Scherer Please confirm as to whether or not the final report is complete.

### Jason Scherer, 2025-02-04

@Pat Wells @David Grosher @Cameron Chapman @Alexander Alan Arnold This This This Investigation has been complete since Oct 29 when the vehicle was returned to RMA. Corrective actions have been defined, but we currently still do not have spare engineering time to implement. I have updated the report to show the next steps as implementing corrective actions. I have also updated the Plan and Issue Status of this ticket to reflect that status.

### Pat Wells, 2025-02-18

Report provided to customer on 18Feb25

### Pat Wells, 2025-03-17

@David Grosher reference below.  Which new release version was this corrected in? 


## Corrective Action

1.Update software to ensure delivery of SAFE ON/OFF commands between XComm and VTOL.
- https://jenaero.atlassian.net/browse/FS2-2320

2.Fix logging software to positively confirm transmission of the SAFE OFF message.
- https://jenaero.atlassian.net/browse/FS2-2205

3.Update software to reset VTOL autopilot during software resets.
- The GCS now does this in the new release.

### Pat Wells, 2024-11-05

@David Grosher @Cameron Chapman Is the final report approved on the engineering side for release to the customer?

### Cameron Chapman, 2024-11-06

@Pat Wells I recommend asking @Jason Scherer who made the report, but since the report says investigating status, it does not look complete.

### Alexander Alan Arnold, 2024-12-10

@Jason Scherer Should this be moved out of D4 and is the report close to being completed?

### Pat Wells, 2025-02-04

@Jason Scherer Please confirm as to whether or not the final report is complete.

### Jason Scherer, 2025-02-04

@Pat Wells @David Grosher @Cameron Chapman @Alexander Alan Arnold This This This Investigation has been complete since Oct 29 when the vehicle was returned to RMA. Corrective actions have been defined, but we currently still do not have spare engineering time to implement. I have updated the report to show the next steps as implementing corrective actions. I have also updated the Plan and Issue Status of this ticket to reflect that status.

### Pat Wells, 2025-02-18

Report provided to customer on 18Feb25

### Pat Wells, 2025-03-17

@David Grosher reference below.  Which new release version was this corrected in? 


## Corrective Action

1.Update software to ensure delivery of SAFE ON/OFF commands between XComm and VTOL.
- https://jenaero.atlassian.net/browse/FS2-2320

2.Fix logging software to positively confirm transmission of the SAFE OFF message.
- https://jenaero.atlassian.net/browse/FS2-2205

3.Update software to reset VTOL autopilot during software resets.
- The GCS now does this in the new release.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V539_240521_105943_pack.zip | archive | 1078 | 2024-05-22 | listed only |
| T95_V539_240521_142311_pack.zip | archive | 1423 | 2024-05-22 | listed only |
| T95_V539_240521_143419_pack.zip | archive | 875 | 2024-05-22 | listed only |
| image-20241018-173301.png | image | 11 | 2024-10-18 | listed only |
