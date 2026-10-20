# VXEP-600: VXE 600 Communication errors

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-09-04
- **Updated:** 2026-03-02
- **Resolved:** 2026-01-14
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** TIQUILA, Weekly-incident-tracker
- **Links:** relates to ENG-3140 (600 Communication Errors); relates to FS2-2486 (Generate Preliminary SW Analysis of VXEP-600); relates to RMA-459 (VXE-600 Card Swap & Expansion 250429-9); relates to FS2-3015 (Test Comms on 600); relates to FS2-3023 (Investigate VXEP-600); relates to VXEP-1069 (Multiple RMA Aircraft Unable to Connect to Xcomm); relates to VXEP-1061 (VXE 548 Command AUX SERVO fail)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 600
- **Vehicle Configuration:** Fuel Cell configuration
- **Issue Status:** Investigation complete. Ready for review.
- **Incident Type:** Mission Failure/Abort
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Received from LM FSR:
After a successful flight yesterday, we were unable to get through the Launch Wizard with V600 today.  Numerous ‘Critical command sent to the aircraft failed’ warnings, even through the aircraft had immediately responded to the command (e.g. surface check, motor test, etc.).  The one thing the aircraft did not immediately respond to was pitot tests.  The pitot would be pressed, released, pressed again, released, and 20 or 30 seconds later the autopilot would beep and the blue bar would raise on the screen, go down, then raise again.  The Launch Wizard was restarted, the GCS software was restarted, the autopilot was power cycled, and the aircraft was hard-wired to the CGS laptop with an Ethernet cable.  Each time the results were the same.  On later attempts, there were also several Calibration failures, it always passed after waiting a few seconds and trying again.  Two AARs were captured, but their CD burner has to be inspected for malware before being connected to a GCS laptop and the AARs could not be immediately copied off of the CGS.
AAR Attached
Report: Vehicle Investigation VXEP-600.pptx
SharePoint: Flight Safety - VXEP-600 Communication Errors - All Documents

## Corrective Action

- Update GCS to run mission simulation on separate thread to prevent UI freezing and link timeout.​ [OBE by full sim redesign]
- Improve robustness of failed system commands.​ [No other observed occurrances]
- Provide better error messaging when system commands fail.​ [Implemented WCAs for various messages]

## Plan

- Replace SD cards with new model.​
- Update firmware to latest release.​
- Perform system checkout flights on vehicle monitoring for similar failed system commands.​

## Root Cause

Recorded link outage correlates with system command failures. Testing failed to produce conclusive evidence of exact cause. Suspect GCS processing or system link connectivity issues. Testing indicated vehicle is functioning correctly.

## Comments (30)

### David Grosher, 2025-02-24

@Scott Whitney @Jason Scherer Jason, can you add this above the remaining 29 palms investigations.

### Cody Smisek, 2025-02-24

@Pat Wells can you confirm with the customer that they were not attempting any firmware updates throughout these issues

### Pat Wells, 2025-02-24

@Cody Smisek I will ask.

### Cody Smisek, 2025-02-24

@Pat Wells Is there a reason they were flying outdated SW during this flight? 6.3.4 was released a few weeks prior to this flight, they were flying SW a few versions older.
@David Grosher FYI

### Pat Wells, 2025-02-24

@Cody Smisek yes, this is the TIQUILA customer and their approval process for software updates usually lags a few weeks behind our releases.

### Jason Scherer, 2025-02-24

I’m working on this investigation now along with Cody.

### Pat Wells, 2025-02-25

@Cody Smisek @Jason Scherer per your question- there were not attempting any firmware updates.

### Jason Scherer, 2025-02-25

There was an update to the VTOL controller on Oct 22, after the AAR, but before the vehicle arrived at SLO. The VTOL firmware was updated from 1.53 (6.1 release) to 1.54.02 (6.2 release). The fixed wing is also running firmware from 6.2.
[embedded image-20250225-211109.png]
[embedded VTOL-Firmware-Update-Oct-22-24.png]

### Jason Scherer, 2025-02-25

Vehicle firmware has been reverted back to 6.1.2 release versions and configs.
[embedded image-20250225-212709.png]

### Jason Scherer, 2025-02-25

Pulled new AAR from vehicle (T95_V600_250225_132526_pack). Added to SharePoint folder.

### Jason Scherer, 2025-03-03

So far, we have been unable to recreate the issues in the original AAR with simple motor tests or air data calibration. After looking deeper into the AAR data the vehicle seems to have been experiencing significant data rates on the (Diag2) Payload port. The data averages 4-5 Mbs, but frequently spikes up to nearly 15mbs. New leading theory is that network data congestion is to blame. 
[embedded image-20250303-220547.png]
Next step is to add sensor data and try to recreate the incident issues. 
Another theory that needs to be looked into is, if multiple links were active and contributing to the issue. The operator reported using a hard link. Need to look for log data that can confirm/dispute if multiple active links (both radio and hard wire) were active. If so, then that could also be a contributing factor.

### Jason Scherer, 2025-03-11

Picking this up again after working on https://jenaero.atlassian.net/browse/VXEP-1061 which had similar syscmd failures.

### Jason Scherer, 2025-03-20

@Pat Wells @David Grosher @Cody Smisek After testing multiple days, I cannot recreate the issue without manually disconnecting link during the surface check part of the launch wizard.
I have confirmed that:
- GCS Mission Simulation blocks the GCS from sending any messages to the vehicle which can create a vehicle connection timeout after 50 seconds. I have been able to recreate a timeout on the vehicle with mission simulation alone. This could be a contributing factor to the failed system commands, but testing is not conclusive.
- Link Inconsistency (simulated by briefly removing Ethernet connection on GCS) prior to advancing to the surface check page on the LW will result in the servo/disarm system command failures that are seen in this vehicles AARs. Due to the expected lossy nature of our ground to vehicle connection, the GCS should better handle dropped system commands (message retries, link health check before sending, etc).

Conclusion: At this point I suspect something on the ground network. Maybe a faulty GCS or Ethernet cables. Since both radio and Ethernet links resulted in this behavior, along with the delayed pitot press, I’m suspecting the GCS.
Next Steps: I will update the report. Then I propose that we swap SD cards since we have the opportunity. Update firmware to latest release allowed by customer. Have the vehicle run though our SCO process to confirm healthy vehicle function.

### Jason Scherer, 2025-03-20

@Pat Wells @David Grosher I updated the report. Let me know if you have any questions or if you want further details added. I suggest we button this vehicle back up, swap sd cards, and update the firmware. Then have SCO perform flight validation. If you guys concur, then I will deliver the vehicle to RMA.

### Alexander Alan Arnold, 2025-04-08

@Pat Wells Please review Jason's Comments/report.

### Alexander Alan Arnold, 2025-04-22

Moved to D6 based on email traffic with Dave. I am reviewing the report @Jason Scherer

### Alexander Alan Arnold, 2025-04-22

Is this aircraft still needed or do you still believe this can be returned to RMA? @Jason Scherer@David Grosher 
FYSA
@Drew Hildreth @Pat Wells

### Alexander Alan Arnold, 2025-04-22

@Jason Scherer The RMA team will be swinging by to remove VXE 600 from your area when they get a chance.

### Christa Meck, 2025-08-05

@Alexander Alan Arnold @David Grosher @Pat Wells What is the status of this investigation?
Leaving open until 12 Aug for feedback.

### Pat Wells, 2025-08-05

@Drew Hildreth @Jackson Riley Curvin @Alexander Alan Arnold See below from Christa
Please advise and close out if necessary.

### Jason Scherer, 2025-03-03

So far, we have been unable to recreate the issues in the original AAR with simple motor tests or air data calibration. After looking deeper into the AAR data the vehicle seems to have been experiencing significant data rates on the (Diag2) Payload port. The data averages 4-5 Mbs, but frequently spikes up to nearly 15mbs. New leading theory is that network data congestion is to blame. 
[embedded image-20250303-220547.png]
Next step is to add sensor data and try to recreate the incident issues. 
Another theory that needs to be looked into is, if multiple links were active and contributing to the issue. The operator reported using a hard link. Need to look for log data that can confirm/dispute if multiple active links (both radio and hard wire) were active. If so, then that could also be a contributing factor.

### Jason Scherer, 2025-03-11

Picking this up again after working on https://jenaero.atlassian.net/browse/VXEP-1061 which had similar syscmd failures.

### Jason Scherer, 2025-03-20

@Pat Wells @David Grosher @Cody Smisek After testing multiple days, I cannot recreate the issue without manually disconnecting link during the surface check part of the launch wizard.
I have confirmed that:
- GCS Mission Simulation blocks the GCS from sending any messages to the vehicle which can create a vehicle connection timeout after 50 seconds. I have been able to recreate a timeout on the vehicle with mission simulation alone. This could be a contributing factor to the failed system commands, but testing is not conclusive.
- Link Inconsistency (simulated by briefly removing Ethernet connection on GCS) prior to advancing to the surface check page on the LW will result in the servo/disarm system command failures that are seen in this vehicles AARs. Due to the expected lossy nature of our ground to vehicle connection, the GCS should better handle dropped system commands (message retries, link health check before sending, etc).

Conclusion: At this point I suspect something on the ground network. Maybe a faulty GCS or Ethernet cables. Since both radio and Ethernet links resulted in this behavior, along with the delayed pitot press, I’m suspecting the GCS.
Next Steps: I will update the report. Then I propose that we swap SD cards since we have the opportunity. Update firmware to latest release allowed by customer. Have the vehicle run though our SCO process to confirm healthy vehicle function.

### Jason Scherer, 2025-03-20

@Pat Wells @David Grosher I updated the report. Let me know if you have any questions or if you want further details added. I suggest we button this vehicle back up, swap sd cards, and update the firmware. Then have SCO perform flight validation. If you guys concur, then I will deliver the vehicle to RMA.

### Alexander Alan Arnold, 2025-04-08

@Pat Wells Please review Jason's Comments/report.

### Alexander Alan Arnold, 2025-04-22

Moved to D6 based on email traffic with Dave. I am reviewing the report @Jason Scherer

### Alexander Alan Arnold, 2025-04-22

Is this aircraft still needed or do you still believe this can be returned to RMA? @Jason Scherer@David Grosher 
FYSA
@Drew Hildreth @Pat Wells

### Alexander Alan Arnold, 2025-04-22

@Jason Scherer The RMA team will be swinging by to remove VXE 600 from your area when they get a chance.

### Christa Meck, 2025-08-05

@Alexander Alan Arnold @David Grosher @Pat Wells What is the status of this investigation?
Leaving open until 12 Aug for feedback.

### Pat Wells, 2025-08-05

@Drew Hildreth @Jackson Riley Curvin @Alexander Alan Arnold See below from Christa
Please advise and close out if necessary.

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V600_240828_121206_pack.zip | archive | 1040 | 2024-09-04 | listed only |
| T95_V600_240828_135022_pack.zip | archive | 777 | 2024-09-04 | listed only |
| Media (37).jpg | image | 308 | 2025-02-21 | listed only |
| NoChecksum.PNG | image | 47 | 2025-02-24 | listed only |
| VTOL-Firmware-Update-Oct-22-24.png | image | 28 | 2025-02-25 | listed only |
| image-20250225-211109.png | image | 8 | 2025-02-25 | listed only |
| image-20250225-212709.png | image | 11 | 2025-02-25 | listed only |
| image-20250303-220547.png | image | 276 | 2025-03-03 | listed only |
