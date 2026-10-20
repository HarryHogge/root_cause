# PLD-54: VXE 734 E140ZG2 SN 6421 unable to regain GPS after power cycling.

- **Issue type:** Bug
- **Status:** Backlog
- **Priority:** Low
- **Created:** 2025-09-15
- **Updated:** 2025-09-18
- **Reporter:** Cameron Chapman
- **Assignee:** Mike DeJesus
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-1509 (MOLSON report: E140 unable to get GPS fix and unable to slew to GPS location)

## Description

@Mike DeJesus  We are currently in flight and have observed the following:
- With both MAPS and DTED enabled on Epsilon, the “Look Here” function operated correctly.
- With no MAPS and with DTED, the “Look Here” function also operated correctly.
- while trying MAPS without DTED  we cycled power on the gimbal using Custom Payload Control, closed the Epsilon software, and then reopened it. After this action, GPS functionality was lost and has not yet been restored.

We have cycled power 3–4 times, and while the system reconnects successfully, GPS remains unavailable.
Im working on uploading pictures of diagnostics that were ran in flight.
Harness PN:2124207-01 REV: C3 LOT#05449-011

Plan:
- Record what fixed the issue and any C/Cas

## Comments (4)

### Cameron Chapman, 2025-09-15

teams chat 
We are currently in flight and have observed the following:
- With both MAPS and DTED enabled on Epsilon, the “Look Here” function operated correctly.
- With no MAPS and with DTED, the “Look Here” function also operated correctly.
- while trying MAPS without DTED  we cycled power on the gimbal using Custom Payload Control, closed the Epsilon software, and then reopened it. After this action, GPS functionality was lost and has not yet been restored.

We have cycled power 3–4 times, and while the system reconnects successfully, GPS remains unavailable.
Im working on uploading pictures of diagnostics that were ran in flight.
 
 
E140 GPS Diag General Info.PNG
E140 GPS Diag GPS Coord.PNG
E140 GPS Diag Signal Health.PNG
E140 GPS Fail 2.PNG
E140 GPS Fail.PNG
 
what does GPS indicator show
 
Is there anything else the team would like the flight ops team to test.  Otherwise they are going to RTB as it's a long drive back to the office. 
 
those last two images likely indicate the VN board is not initializing. we've seen similar issues here when troubleshooting MANI. 
 
and what are the first 3 images from, are they before or after the GNSS issue
 
Cody Smisek
those last two images likely indicate the VN board is not initializing. we've seen similar issues here when troubleshooting MANI.

any identified fixes during flight or after for that?
 
all of these are taken after the issue

### Cody Smisek, 2025-09-15

Questions for Riga,
What is the min CNO set to in register 99?
What is the Signal Strength a ratio of (as reported in Epsilon)? Guessing observed CNO / 50.
What does temp 2 indicate in the telemetry window?

What are all the possible errors in this window and what do they correspond to?
[embedded: image-20250915-224720.png]

### Cody Smisek, 2025-09-15

@Jackson Riley Curvin please include gimbal SN, harness SN, aircraft SN

### Cameron Chapman, 2025-09-18

Info from teams 
Info from MOLSON:
 
While conducting flight operations the GPS lost connection during the flight. The team power cycled the gimbal using the Aux payload on/off switch in the VXE30 software but was unsuccessful. They completed their mission with no gimbal GPS and on return changed swap the propane tank and power cycled the air vehicle which was also unsuccessful in gaining GPS connection.
 
 We tried again and this gimbal would not connect using either latest version of the epsilon software and we also tired versions 3.5.5.0. This gimbal has the first prototype cable installed and not one of the new cables, we then tested the remaining gimbals with the new cables and two of the came up with yellow for GPS connection and the third came up red. The new cable that came up red we installed the cable on as it was at QETE for laser safety testing.
 
Next week we are going to test the remaining gimbals to see if we have any additional issues. As we have had these cables replaced a variety of times over the last 6 weeks I am wondering if we have damage the GPS cable of connector.
 
Pat Wells added Jackson Curvin and 2 others to the chat and shared all chat history.
 
The unable to recover gps sounds like the issue Hsv experienced during flight. 
 I think Cody mentioned that gimbal status is usually yellow until the imu gets a fix from movement, usually aircraft flight. 
Mike DeJesus were they able to recover gps from the gimbal from the Monday flight?
 Does the imu description above sound accurate?
 
The imu description is accurate. Yellow is correct on the ground without an IMU fix (movement is required).
 No we were not able to recover from GPS Monday.
 This sounds like a case of poor GPS coverage, especially since the aircraft experienced it as well.
 I don’t see evidence here that the gimbal or cables are faulty.
 
GPS in the area on other devices was not effected. Only the gimbal
 “They completed their mission with no gimbal GPS and on return changed swap the propane tank and power cycled the air vehicle which was also unsuccessful in gaining GPS connection.” 
"we then tested the remaining gimbals with the new cables and two of the came up with yellow for GPS connection and the third came up red."
 
They have been testing gimbals on their bases in Canada with similar GPS connection issues.
 It sounds like there was some sort of interference issues, the gimbals behaved correctly on the ground without the yellow status. The one that wouldn’t acquire is a bit concerning but ive seen them take up to 5 minutes to acquire sometimes. Is there more details on how long they waited, where they were when they tested (indoors or out) etc? 
They are doing more testing today. They will provide more details including GPS fixes on other equipment and serial numbers of the equipment being used. ... MTF
 Awesome, thanks 
Tim Muchmore if they experience the gimbal GPS issue again in flight during their testing it would be helpful to have the AAR from the aircraft for that flight. We can look at the GPS logs from the aircraft to rule out or determine if they are in a GPS degraded environment.  
 
Mike DeJesus
Is there more details on how long they waited, where they were when they tested (indoors or out) etc?

Outdoors. Non-degraded environment. 10 minutes. 
 
Pat Wells
Tim Muchmore if they experience the gimbal GPS issue again in flight during their testing it would be helpful to have the AAR from the aircraft for that flight. We can look at the GPS logs from the aircraft to rule out or determine if they are in a GPS degraded environment.

They are getting the AARs 
 
Have them check the telemetry tab and record signal strength, PDOP, and satellites.
 Have they been in touch with GS during the testing/troubleshooting?
 

Mike DeJesus 
The imu description is accurate. Yellow is correct on the ground without an IMU fix (movement is required). No we were not able to recover from GPS Monday. This sounds like a case of poor GPS coverage…

 Is gps on that flight gimbal working now? Could it be a similar issue where it wouldn’t recover after power cycles. 
 It would be useful to record serial numbers of everything. If unrecoverable in the current config, testing with the ground cable and swapping gps antennas could be helpful, unless they would prefer to return the non functional ones for us to troubleshoot.

 
the aircraft from the flight is on it's way back to Ottawa. It was never able to reconnect. They flew three hours after propane tank swap manually steering gimbal to POI/Tgts the whole time.
 
Drew Hildreth has there been comms with MOLSON on this issue?
 Through Tim. No direct comms on this one. Last was epsilon maps.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20250915-224720.png | image | 37 | 2025-09-15 | listed only |
