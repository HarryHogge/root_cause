# VXEP-1509: MOLSON report: E140 unable to get GPS fix and unable to slew to GPS location

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-09-15
- **Updated:** 2026-03-02
- **Resolved:** 2025-10-30
- **Reporter:** Greg Fryer
- **Assignee:** Mike DeJesus
- **Creator:** Greg Fryer
- **Labels:** MOLSON
- **Links:** relates to VXEP-1452 (New E140 Assemblies video quality issues); relates to VXEP-1497 (VXE 734 E140 Connection Issues ); relates to PLD-54 (VXE 734 E140ZG2 SN 6421 unable to regain GPS after power cycling. )
- **Customer:** MOLSON
- **Problem Type:** Discovered Issue
- **Root Cause:** Root cause is determined to be intermittently degraded environmental conditions.
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Limited additional info as of 2025-09-15 at 0930 pacific. Problem occurred on two separate aircraft. Unknown if separate gimbals, but likely.

## Corrective Action

- Review bench test for all flight modes. Why are look here and laser checks skipped? Can we develop methods to check them?
- Add flight test to checkout procedure. Ensure all functions are checked and recorded.
- Add pass/fail values, procedure steps, version control, traveler recording to gimbal checkout procedure.

## Plan

- Get more information on what issues customer is experiencing. See teams chat posted to comments 9/18. Update plan accordingly.
- Find/create E140 with same C3 cable as MOLSON has. Complete, borrowing USSS Bailment unit in HSV. HSV FLOPS will conduct flight.
- Conduct test flight to replicate issue.
- If not recreated, try removing Epsilon map data. There are reports MOLSON had difficulty loading maps, no public internet connection allowed.
- Update plan and status based on flight test findings. See linked issue.

- Parallel - Review harness C3 flight test card, verify GPS functions in Epsilon were tested. Find someone to testify to events, if possible.
- Gus Has confirmed. GPS functions and look here command were tested during flight test. Only one internal asset was tested. Customer cables only had ground test, which skipped GPS test for some reason.
- @William Lane Medlin Why were GPS, look here, and laser pointer checks skipped? Can you get a camera that can verify laser is working?

## Issue Status

“MOLSON also reported GPS fix issues...That was Thursday” 
Discussing with FLOPS and HSV, look here feature was tested during the flight test (only one unit). 
[embedded: image-20250915-175535.png]

Was not tested on bench for all cables and gimbals. I am investigating why and improvement options to ensure all features are tested on every unit. Please let us know if you have any more info on the issues customers experienced.

## Comments (6)

### Greg Fryer, 2025-09-15

@Pat Wells Here’s our incident ticket. I’m updating status, but just so you have the place to point to.
@Cameron Chapman LMK if you end up needing help chasing down original testing results.
Thank you both.

### Cameron Chapman, 2025-09-18

Info from Teams chat. 

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

### Michael Mohr, 2025-10-29

During Molsen training (22Sept-03Oct 2025), we updated E140ZG2 S/N: 6421 to firmware 3.5.4.1 , inspected the GPS cable and connector, and flew it installed on multiple airframes in battery and fuel cell configuration. We were able to get GPS connection on most of the flights. We cycled power to the gimbal several times and restarted Epsilon as well. We auto and manually connected to the gimbal successfully. In most instances, after power cycling in the air, the GPS would take several minutes to reacquire signal. We tried not to interrupt the training flights, so on the one or two occasions where GPS did not come back up, we did not have the ability to troubleshoot the issue. Collectively though, we believed it was not gimbal related but rather environmental (location of the aircraft) or software. @Cameron Chapman @Greg Fryer @Mike DeJesus

### Greg Fryer, 2025-10-30

@Mike DeJesus I think you are already tracking this, but it was assigned to me so might have gotten lost. Working to get some “Jira mumbo-jumbo” sorted so this can go into your space and make it easy to find.@Christa Meck

### Mike DeJesus, 2025-10-30

I have reviewed the details of this incident and determined it is a result of intermittently degraded environmental conditions.

### Michael Mohr, 2025-10-30

Intermittently degraded environmental conditions

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20250915-175535.png | image | 702 | 2025-09-15 | listed only |
