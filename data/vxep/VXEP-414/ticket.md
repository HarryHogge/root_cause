# VXEP-414: VXE 468 crash after transition to forward flight

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2024-05-22
- **Updated:** 2026-08-14
- **Resolved:** 2025-12-01
- **Reporter:** Pat Wells
- **Assignee:** Lauren Velasquez
- **Creator:** Pat Wells
- **Labels:** Hardware, MARSOC, Weekly-incident-tracker
- **Links:** relates to RMA-250 (VXE-468 240523 Goodwill Full Aircraft); relates to FS2-2002 (VXE-468 Data Recovery); relates to FS2-310 (VXEP - SD Card file corruption (VXEP-236,237,414)); relates to VA-1750 (Evaluate CAN servos and add to next gen diagram (separate from as built diagram)); relates to VXEP-637 (VXE 401 loss of control, aircraft flying in loops)
- **Customer:** MARSOC
- **Vehicle Tail Number:** 468
- **Plan:** - Review Investigation PPT
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

EE Checklist: V468 EE checklist.xlsx
Relevant Files: https://jenaero.sharepoint.com/sites/FlightSafety/Shared%20Documents/Forms/AllItems.aspx?csf=1&web=1&e=dp79vR&CID=d8f1cb48%2D3366%2D403b%2Db278%2D98a1b6cdc45c&FolderCTID=0x012000D03119522A011A40817D7F0F59E3A7EF&id=%2Fsites%2FFlightSafety%2FShared%20Documents%2FIncident%20Reports%2FVIT%2D414%20VXE%20468%20crash%20after%20transition%20to%20forward%20flight&viewid=7181a7a2%2Dd286%2D47c9%2Dbdd3%2D9195ef18282c 
Information received from operator:
AV was flown for approx 1 hour then recovered with no issues. VO swapped batteries and was on standby for launch. During preflights there were no issues or anomalies during any checks. During launch AV climbed in VTOL mode to 300 ft, turned directly into wind, and started flying towards 1st waypoint (into wind). Near the top of the VTOL climb (last 100ft of climb), the main propeller started spinning. After flying approx 100m away, as the VTOL motors cut off, the main propeller seemed to either degrade or turn off (unsure because it was still spinning) and nose dived into the ground. No people or property were effected other than stalker, only pieces that seemed salvageable was left wing, payload, rudder, and elevator. Unable to download FDR.
Currently awaiting AAR from operator.
Incident report from operator attached.
Replacement aircraft is being provided immediately:  VXE-662

Note: Aircraft was equipped with customer supplied Silver Surfer GPS configuration.

## Corrective Action

- https://jenaero.atlassian.net/browse/VXEP-606
- Added servo feedback to this project requirements. https://jenaero.atlassian.net/browse/VXEP-607
- Link to next gen ESC having telemetry requirement.

## Issue Status

Report: VXEP-414 VXE 468 Crash After Transition to Forward Flight.pptx
Boost board: 
Elevator boost board was not showing responding the Iron bird’s and 468 avionics box when connected. 

[embedded image-20240912-152903.png]

ODU’s boot was slipping down so I removed it and when I did the connectors were not attached to it 
[embedded image-20240912-153938.png]
When inspecting the ODUs it is evident that the harness was ripped from the connector. This leads to the question whether it was caused from the crash or if it was from stress from disconnecting and connecting the elevator from the tail.  
- Given the receipt inspection damage and that all 3 wires are ripped off, it seems likely this damage was from the crash. 
[embedded image-20240913-164156.png]

[embedded image-20240912-154516.png]
[embedded image-20240912-154525.png]
After finding that the ODUs were torn off, I conducted a series of tests
- I used a servo controller to check if a servo would respond to the boost board. It did not
- I put the boost board onto the iron bird and tried to control the servo by moving around the avionics box. Using the Iron bird and 468’s avionics box, the servos were not responding to the servo
- Hooked it up to the load tester in the Eshop and saw that when given an input there was no output. This could be due to incorrect setup . 
- test completed and with newly terminated output harness the boost board worked as intended

After these tests were performed, I cut the heat shrink incasing the boost board and saw that it was covered in the tough seal potting material. 
[embedded image-20240912-155217.png]
[embedded image-20240912-155222.png]
I proceeded to carefully remove the the potting material by dumping it into alcohol to soften it and using tweezer and an exacto knife. I came to a point where I was satisfied to begin probing and testing connections. 
- Looking at the schematic and I did a continuity test on the switching regulator and everything had continuity
- I checked the output voltage. I inputted 6V and measured the output and it measured 6.2V , which is expected.
- Using a servo controller, I checked the signal output voltage and when increasing and decreasing the PWM the voltage would range from 0.18V-0.5V (0.18V when the servo controller was at the lowest pulse width and 0.5V when it was at the highest pulse width). This voltage range was compared to a known good elevator boost board and was consistent.

After these tests were done the output wires ripped off from the board due to handling
[embedded image-20240912-160334.png]
9/16/2024: 
re-terminated output side of boost board with new wires and ODU and board is functioning properly
Connected a servo controller to the boost board and a servo to the output and the servo was responding to the controller 
Connected the boost board to the Iron Bird with IB avionics box and 468 avionics box and servos were responding. I also connected the tail boom to the iron bird and the servos responded. 
Connected boost board to load tester and on the load side 6.2V was being seen with no load (expected) and load test passed as expected.

## Root Cause

Previous evidence points to a faulty boost board however the issue can not be replicated:
Possible root causes 
- harness on ODU side stripped too far and when disconnecting the elevator from the harness it had too much stress and ripped. 
- This is evident by seeing the ripped ODU, however this is still inconclusive because this could be a symptom from crashing but seems like the most likely cause.

## Comments (35)

### Cameron Chapman, 2024-09-05

@Ryan Christino good analysis. I added some comments to the report. Some suggestions, 
- it can be useful to add a summary of findings/conclusions to the fishbone, slides, etc.
- Linking the titles or numbers of the fishbones to specific slides can help indicate which slides refute or support different items.
- What makes you think the elevator was working correctly? given power stays high with throttle, it does not seem like a typical ESC issue (but still possible). Seems more like bad elevator or some other control/lift, or bad prop maybe

@Adrian Garcia can you inspect and test the following. It may be challenging with the damage from the crash, but worth trying. 
- Please use the investigation checklist of this sheet on every investigation, improve it, and train others to use it. EE Checklists.xlsx
- Inspect aircraft, but specifically parts, harness, and electronics involved in the elevator servo (and boost board) and forward prop and ESC.

### Adrian Garcia, 2024-09-05

@Cameron Chapman @Sean Odell @David Grosher elevator is not in the case, does anyone know where it might be or can point me to who would know?

### Adrian Garcia, 2024-09-05

Quick findings: 
- one of the tail servo boosters does not have continuity between pins but most likely a result of crash
- second tail servo booster does not have continuity across the power line. GND and Signal lines do have continuity. the discontinuity could be caused by the crash but if power was not going to the servo that is a potential root cause. Note: look into logs to see if there is any logging for the voltage
- ODU connector on FWD ESC is bent, likely caused by the crash


[embedded image-20240905-180655.png]

[embedded image-20240905-180706.png]

[embedded image-20240905-180714.png]

[embedded image-20240905-180721.png]

[embedded image-20240905-180729.png]

### Sean Odell, 2024-09-05

@Adrian Garcia The elevator was delivered with the rest of the aircraft in the case to engineering. The customer already got a replacement, but please take a moment to look around the engineering area for that part as time allows.

### Adrian Garcia, 2024-09-05

Looking into the logs Vservo3 is getting 6V so the discontinuity I mentioned earlier is highly likely caused by the crash

### Cameron Chapman, 2024-09-07

@Adrian Garcia “second tail servo booster does not have continuity across the power line. Logs indicate that tail servos were getting power so discontinuity is likely a cause from the crash”
- The logs are measurements of voltages at the XCOM. Nothing is measured at the servos. A fault in the boost board could absolutely cause this issue. Please try to determine if there is any evidence of a fault in the boost boards before the crash.

### Ryan Christino, 2024-09-09

@Cameron Chapman  Thanks for the feedback on the report, I implemented your feedback and can help update the report when the hardware investigation is wrapped up.

### Adrian Garcia, 2024-09-09

@Cameron Chapman suspicious boosted board did not pass any tests. The first test conducted was using it with a servo controller and the servo did not perform as excepted. Second test was to put it on Iron Bird and it did not work either. Last test was a load test and it was not giving any/accurate voltage on the output side.

### Cameron Chapman, 2024-09-09

Thanks @Adrian Garcia please work with the EE team to see if you can determine if it was damaged from the crash or malfunctioning before (remove potting carefully and inspect components).

### Adrian Garcia, 2024-09-10

Servo was opened and trying to currently remove potting 
[embedded 710afe58-08ae-46f4-a545-ae22a8f7b5bd.jpg]
[embedded e2aaab6d-4aa0-4e71-b862-ee80ff360075.jpg]

### Adrian Garcia, 2024-09-12

@Cameron Chapman Stepping away for a few days to focus on SD card issues and getting havoc IB functional. I updated the issue status with all my findings on the boost board

### Cameron Chapman, 2024-09-13

Actions and questions for @Adrian Garcia. 
- This seems higher priority than havoc IB. Please continue with this investigation.
- Please always keep the plan field updated, especially when transitioning to another task.
- Please combine information from the status and the attached doc into an investigation report. Please see steps and template here and update the investigation checklist with the locations. https://jenaero.atlassian.net/wiki/spaces/EF/pages/23363854/Incident+Investigation+Troubleshooting+and+Resolution+Tracking
- Please update your plan and root cause fields.
- See comments above in plan. Specifically:
- Please repair ODU, PCB, and repeat functional test with all aircraft parts including XCOM, intermediate harnesses and elevator servo.
- Please reinforce solder joints (tape, etc) and handle evidence more carefully in the future.

### Adrian Garcia, 2024-09-19

@Ryan Christino I added a hardware section to your investigation report, let me know if you want me to reformat or something else, if not it is ready for review @Cameron Chapman

### Cody Smisek, 2024-10-07

Hardware is currently stored under the engineering stairwell area. Ready to return to RMA when appropriate.

### Cody Smisek, 2024-12-23

@Adrian Garcia @Cameron Chapman what's next for this issue? I see CA added but ticket is D4.

### Cameron Chapman, 2024-12-23

@Adrian Garcia please update root cause field. Does it seem like the connector was the likely cause of the issue, potential, unlikely but possible, etc. How likely is it that the connector broke during flight and caused this issue, or would it likely have been caught pre-flight if caused by that?

### Christa Meck, 2025-08-05

@Lauren Velasquez and/or @Pat Wells What is the status of this investigation?  
Leaving open until 12 Aug for feedback then canceling.

### Pat Wells, 2025-08-05

@Drew Hildreth @Jackson Riley Curvin @Alexander Alan Arnold See below from Christa
Please advise and close out if necessary.

### Alexander Alan Arnold, 2025-08-05

@Pat Wells This was the silver surfer aircraft do we want to keep this open since we know the config was not one we had tested

### David Grosher, 2025-08-15

@Drew Hildreth This investigation did not produce a conclusive root cause.  Therefor there are no near term corrective actions. The only corrective actions are for long term requirements in next generation designs. I suggest closing this ticket as Bremuda Triangle.

### Cameron Chapman, 2024-09-07

@Adrian Garcia “second tail servo booster does not have continuity across the power line. Logs indicate that tail servos were getting power so discontinuity is likely a cause from the crash”
- The logs are measurements of voltages at the XCOM. Nothing is measured at the servos. A fault in the boost board could absolutely cause this issue. Please try to determine if there is any evidence of a fault in the boost boards before the crash.

### Ryan Christino, 2024-09-09

@Cameron Chapman  Thanks for the feedback on the report, I implemented your feedback and can help update the report when the hardware investigation is wrapped up.

### Adrian Garcia, 2024-09-09

@Cameron Chapman suspicious boosted board did not pass any tests. The first test conducted was using it with a servo controller and the servo did not perform as excepted. Second test was to put it on Iron Bird and it did not work either. Last test was a load test and it was not giving any/accurate voltage on the output side.

### Cameron Chapman, 2024-09-09

Thanks @Adrian Garcia please work with the EE team to see if you can determine if it was damaged from the crash or malfunctioning before (remove potting carefully and inspect components).

### Adrian Garcia, 2024-09-10

Servo was opened and trying to currently remove potting 
[embedded 710afe58-08ae-46f4-a545-ae22a8f7b5bd.jpg]
[embedded e2aaab6d-4aa0-4e71-b862-ee80ff360075.jpg]

### Adrian Garcia, 2024-09-12

@Cameron Chapman Stepping away for a few days to focus on SD card issues and getting havoc IB functional. I updated the issue status with all my findings on the boost board

### Cameron Chapman, 2024-09-13

Actions and questions for @Adrian Garcia. 
- This seems higher priority than havoc IB. Please continue with this investigation.
- Please always keep the plan field updated, especially when transitioning to another task.
- Please combine information from the status and the attached doc into an investigation report. Please see steps and template here and update the investigation checklist with the locations. https://jenaero.atlassian.net/wiki/spaces/EF/pages/23363854/Incident+Investigation+Troubleshooting+and+Resolution+Tracking
- Please update your plan and root cause fields.
- See comments above in plan. Specifically:
- Please repair ODU, PCB, and repeat functional test with all aircraft parts including XCOM, intermediate harnesses and elevator servo.
- Please reinforce solder joints (tape, etc) and handle evidence more carefully in the future.

### Adrian Garcia, 2024-09-19

@Ryan Christino I added a hardware section to your investigation report, let me know if you want me to reformat or something else, if not it is ready for review @Cameron Chapman

### Cody Smisek, 2024-10-07

Hardware is currently stored under the engineering stairwell area. Ready to return to RMA when appropriate.

### Cody Smisek, 2024-12-23

@Adrian Garcia @Cameron Chapman what's next for this issue? I see CA added but ticket is D4.

### Cameron Chapman, 2024-12-23

@Adrian Garcia please update root cause field. Does it seem like the connector was the likely cause of the issue, potential, unlikely but possible, etc. How likely is it that the connector broke during flight and caused this issue, or would it likely have been caught pre-flight if caused by that?

### Christa Meck, 2025-08-05

@Lauren Velasquez and/or @Pat Wells What is the status of this investigation?  
Leaving open until 12 Aug for feedback then canceling.

### Pat Wells, 2025-08-05

@Drew Hildreth @Jackson Riley Curvin @Alexander Alan Arnold See below from Christa
Please advise and close out if necessary.

### Alexander Alan Arnold, 2025-08-05

@Pat Wells This was the silver surfer aircraft do we want to keep this open since we know the config was not one we had tested

### David Grosher, 2025-08-15

@Drew Hildreth This investigation did not produce a conclusive root cause.  Therefor there are no near term corrective actions. The only corrective actions are for long term requirements in next generation designs. I suggest closing this ticket as Bremuda Triangle.

## Attachments (24)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [468 Stalker UAS Incident Report 20240521.xlsx](attachments/20632_468%20Stalker%20UAS%20Incident%20Report%2020240521.xlsx.md) | xlsx | 50 | 2024-05-22 | converted |
| 468 Crash Data.zip | archive | 1353 | 2024-06-25 | listed only |
| VXE-468VTOL.zip | archive | 500 | 2024-06-25 | listed only |
| image-20240626-223744.png | image | 15 | 2024-06-26 | listed only |
| image-20240626-223813.png | image | 22 | 2024-06-26 | listed only |
| image-20240626-223845.png | image | 12 | 2024-06-26 | listed only |
| image-20240626-223907.png | image | 12 | 2024-06-26 | listed only |
| image-20240626-234231.png | image | 11 | 2024-06-26 | listed only |
| image-20240626-234550.png | image | 11 | 2024-06-26 | listed only |
| image-20240905-180655.png | image | 21470 | 2024-09-05 | listed only |
| image-20240905-180706.png | image | 13513 | 2024-09-05 | listed only |
| image-20240905-180714.png | image | 15812 | 2024-09-05 | listed only |
| image-20240905-180721.png | image | 10458 | 2024-09-05 | listed only |
| image-20240905-180729.png | image | 12341 | 2024-09-05 | listed only |
| 710afe58-08ae-46f4-a545-ae22a8f7b5bd.jpg | image | 36 | 2024-09-10 | listed only |
| e2aaab6d-4aa0-4e71-b862-ee80ff360075.jpg | image | 37 | 2024-09-10 | listed only |
| image-20240912-152903.png | image | 5026 | 2024-09-12 | listed only |
| image-20240912-153938.png | image | 5886 | 2024-09-12 | listed only |
| image-20240912-154516.png | image | 27216 | 2024-09-12 | listed only |
| image-20240912-154525.png | image | 8416 | 2024-09-12 | listed only |
| image-20240912-155217.png | image | 15117 | 2024-09-12 | listed only |
| image-20240912-155222.png | image | 9671 | 2024-09-12 | listed only |
| image-20240912-160334.png | image | 15174 | 2024-09-12 | listed only |
| image-20240913-164156.png | image | 1881 | 2024-09-13 | listed only |
