# VXEP-1802: VXE 620 Suffered a VTOL Failure-unable to replicate

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2026-03-31
- **Updated:** 2026-09-03
- **Resolved:** 2026-08-10
- **Reporter:** Stephan Johnson
- **Assignee:** Cameron Chapman
- **Creator:** Stephan Johnson
- **Labels:** Hardware, RCCA, TIQUILA, Weekly-incident-tracker
- **Links:** relates to RMA-961 (VXE-620 RMA 260407-4); relates to VXEP-628 (Systemic VXE30 VTOL ESC Reliability Issues )
- **Customer:** TIQUILA
- **Vehicle Tail Number:** VXE-620
- **Vehicle Configuration:** AdvNav; Fuel Cell
- **Issue Status:** Unable to replicate issue/determine C/CA
- **Incident Type:** Aircraft Loss
- **Severity:** 1 - Flight Critical

## Description

- The Aircraft launched without issue and completed 2:10 of Flight prior to the incident.
- The flight had drawn to a close, and the detachment initiated the recovery process, giving a ‘go to’ IP 1 to initiate a VTOL recovery. The aircraft completed the final approach up until after IP 5 without incident. In the final phase, passing IP5 where the aircraft transitions from forward flight to VTOL it was initiated in the air and on the VTOL control window that the aircraft had transition to VTOL however the visual of the aircraft, the aircraft can be seen attempting to initiate VTOL flight however only 3 of the 4 VTOL propellors is seen to engage. The Aircraft then initiated a left hand spiral and descended quickly towards the ground. The RPAS C U/I attempted some corrective action with input of positional nudge without effect. Owing to the proximity of the descending vehicle to the detachment (Approx 30 m) and the speed, lack of control over the aircraft and lack of present Emergency procedures lead the aircrew to judge that the aircraft be left to descend in place to alleviate any further issues. In addition, there was little time to enact any other controls prior to impact with the ground.
- It is pertinent to note that there were no issues flagged on the VTOL Control window. The window shows no emergency popups or warnings and no other indications of ANY emergency. The wind was light and well within limits for Eagle VXE 30.

## Corrective Action

Future recommendations, not implemented yet:
- Replace B30 ESCs with B40 ESCs or a smaller variant. https://jenaero.atlassian.net/browse/VA-444
- Link to launch abort and other feature requests.  https://jenaero.atlassian.net/browse/VXEP-1519
- Pre-landing motor checks., fixed wing landing if not acceptable.  I think Dave mentioned that these were not very feasible and would not prevent many issues. Check if it comes up again.
- Pre-launch error detection and launch prevention https://jenaero.atlassian.net/browse/VXEP-1469

TBD
- Did we implement screening/functional test of B30 and B40 ESCs (including spares) @Daniel Ceja?

## Plan

Reviewing questions from TIQ: 
- 8/21 Added more information and updates to the investigation report. @Drew Hildreth  @Scott Lovett do you think we should open this investigation again? Where does it rank in priority?

Customer followed up with these questions. Plan to answer and review internally here. 
AV 620: 
- Please can RW provide an assessment of VTOL propulsion failures across wider VXE30 fleet, including any similar occurrences, known failure trends to support an assessment of whether this event is considered tail specific or has potential fleet-wide applicability.
- Many are linked to this one. Some other related incidents may not be linked. https://jenaero.atlassian.net/browse/VXEP-628. VTOL ESCs appear to be some of the highest failure and least documented (from an operational limits perspective) hardware on B30.  @Cameron Chapman  plans to link and organize the causes and potential CAs, and CA status for these incidents.
- Can RW provide further detail on how each element of the functional chain between the flight controller command and motor thrust was assessed, including the rational for the investigation focusing on C2 equipment, motor/propeller and ESC. In particular whether other assets of the propulsion chain e.g. VTOL interface board, wiring, connectors etc were assessed and if so how these were eliminated as potential contributors.
- More information provided and added to the investigation. VTOL interface board, wiring, connectors etc. were inspected and tested. No anomalies detected. Details added to investigation report.
- Are there any other credible failure mechanisms, whether any could represent intermittent faults and whether any interim inspections/monitoring are considered appropriate ie tail specific versus fleet-wide.
- Not that we are aware of or have measured. Most ESC investigations have conclusive failure causes that permanently affect operation. Some previous intermittent issues with ESC operation.
- Contacts coming loose on the interface board: CAs implemented long before this aircraft was built, such as insertion inspections, pull tests, connector retention, etc.  No repeat issues since then.
- Controller firmware corruption: No evidence of firmware corruption in this ESC as was observable in that incident.
- How much of AV 620 had to be rebuilt as part of root cause analysis? Ie could the fault credibly have been hardware and unable to be confirmed due to level of damage to air vehicle post crash?
- The relevant hardware on AV 620 was tested without any repairs or modifications performed. There were no modifications made that could have eliminated evidence to the cause of this issue.


Additional investigation that could be performed
- Potentially repeat cycles under load to test for processor locking up or similar issues. -See previous investigation for an example (running flight profile on this ESC on dyno)

Investigation report folder: https://jenaero.sharepoint.com/:f:/s/FlightSafety/IgDMJYDWWi9RQoz4uhjYD_yDAd6J63VoUEfAMNyABqAqpl4?e=BaQ052
Investigation summary: https://jenaero.sharepoint.com/:p:/s/FlightSafety/IQB6I7G3PLYARqSqNrfdCgtYAbVtLSAf84TSddrA8uzuVKE?e=7bEkk5

## Root Cause

Unable to replicate so far. Firmware hangup seems like a more likely cause. Potentially due to corruption, but unable to determine. These are pretty rare, but have occurred before. 
B30 VTOL ESCs have had multiple failures. Tracking here https://jenaero.atlassian.net/browse/VXEP-628

## Comments (20)

### Cody Smisek, 2026-03-31

@Drew Hildreth I’d recommend updating the subject line of this ticket. VTOL prop failure would lead me to believe the VTOL propeller fell off or something similar. This sounds like a lift motor / lift system issue.

### Drew Hildreth, 2026-03-31

@David Grosher Mike has dropped the zip file in.

### Eric Brewer, 2026-03-31

@Drew Hildreth @David Grosher logs and video show that RR motor never started up after transition.  It is not spinning in the video and the commands for the RR are maxed out.  The autopilot tries to maintain attitude the best it can in these cases - one vtol motor failed is not recoverable unfortunately.

[embedded: image-20260331-191058.png]

### Lawrence Nichols, 2026-04-14

VXE 620 intake in progress, @Laszlo Juhasz and I will be able to prepare a boom test when all data is pulled.

### Jackson Riley Curvin, 2026-04-27

@Lawrence Nichols can we get an updated status on this?

### Drew Hildreth, 2026-05-12

@Lawrence Nichols Is there any additional testing that is planned for this? Or are we to a point where we are unable to reproduce the failure at all.

### Lawrence Nichols, 2026-05-13

@Drew Hildreth At the moment I don’t have any additional testing planned, and I was not able to recreate the failure.

### Drew Hildreth, 2026-05-13

@Lawrence Nichols Thank you Lawrence. I know that Cameron says there is additional stuff that we can test, but B40 has taken over every effort at the moment. so maybe another day.

### Lawrence Nichols, 2026-05-13

@Drew Hildreth Sounds good, I am open to suggestions for future testing effort.

### John Clark, 2026-05-22

I was requested to investigate this Ticket for the possibility of corruption in the firmware and control logic on the ATmega8 that drives the motor. I was delivered two motors by @Lawrence Nichols and worked with Drew Miyahara to validate the firmware and configuration.
We used the avrdude programmer to pull the information from the motors with the following command:
avrdude.exe -C C:\Users\Public\PublicDesktop\kkmulticopterflashtool_0.77\lib\avrdude\windows\usbtiny\avrdude.conf -p m8 -P usb -c usbtiny -vvvvv -U flash:r:flash.hex:i
- -p Part number
- -P Port
- -c Programmer
- -vvvvv Ultimate verbose
- -U Memory Command
- flash - primary program memory
- op: r - flash read
- flash.hex - target file for read
- : i intelhex format

Attached are identical output produced by the configuration file (avrdude.conf) also attached.
Lastly the two intelhex record files are also attached, also identical
As a final step I converted one of the two extracted .hex files to the 16byte format used to program the motors in production using the below command/utility. It also compared identically.
srec_cat input_file.hex -Intel -o output_file.hex -Intel -Output_Block_Size=16
Please feel free to reach out with any further questions or tests. --jc[embedded: C-S102221 CCW flash.hex] [embedded: avrdude.conf] [embedded: C-102197 CW flash.hex] [embedded: C-S102197 CW motor ESC flash hex 1.txt] [embedded: C-S102221 CCW motor ESC flash hex 1.txt] @Eric Brewer @David Grosher

### Drew Hildreth, 2026-06-02

@John Clark Apologies that we had not seen this prior. So am I understanding correctly that there is nothing we can reproduce as an error at this time?

@Lawrence Nichols has there been any additional load testing done to these?

### Lawrence Nichols, 2026-06-02

@Drew Hildreth working on getting the motors on a test stand and uploading motor control commands from the provided logs to try and recreate the issue as a next step.

### John Clark, 2026-06-02

@Drew Hildrethwouldnt say that. But firmware corruption in the motor doesn't seem the cause. If the motors test okay. I'd perhaps turn to the electrical system. The software on the VTOL and even the FW is also something that can be further analyzed. We have a great flight science team that can help with the logs.

### Cameron Chapman, 2026-06-24

@John Clark Thank you for doing this. Have you seen corruption on previous ESCs with this method, or did we just determine corruption was likely because the ESC didn’t work right before reflashing and it did work right after on a previous investigation.

### Alexander Alan Arnold, 2026-07-01

@Scott Whitney since Dave is out deferring to you, johns comment reads as if someone from flight science may be able to weigh in?

### John Clark, 2026-07-01

@Cameron Chapmancorruption of the motor firmware has been a suspect before. The test to detect is worth the effort IMO, to rule it out. If we did ever find it there is a path forward with programming fuses and even a crc check.

### John Clark, 2026-07-01

@Alexander Alan Arnoldmy feeling was we should be looking at the motor itself and the electrical in the AC. As said below I think we should continue to verify the firmware whenever we feel it may be suspect.

### Alexander Alan Arnold, 2026-07-20

Report under review, GS team will review report and pass to customer.

### Alexander Alan Arnold, 2026-08-10

Closing due to inconclusive data from testing. Motor swapped.

### Cameron Chapman, 2026-08-17

Old status: RR Motor failed - Unclear at this point why it failed. Delay issue or just straight failure?
(4/20) Lawrence N: Testing performed on Right Boom, documentation linked in plan field, boom/esc’s/lift motors seems to be functioning normally. Moving onto testing center wing connections and further hardware up the chain.
(4/23) Lawrence N: Connected CW to B30 IB, ran motor test for all 4 VTOL motors. All motors operated normally, performed wiggle test while operating which had no impact.
(4/28) Lawrence N: Opened CW and exposed APB, visually inspected with nothing of note, wiggle tested internal connections while running motor test with no failure of any motors.
(5/18) Lawrence N: Opened ESC enclosures for right boom, inspected visually and did not notice any major signs of damage, pictures added to investigation report.
Due to last working day will be reassigning to @Laszlo Juhasz for continuation

## Attachments (13)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 20260330_SGCS1-209_ADR_EAGLE_620.zip | archive | 58634 | 2026-03-31 | listed only |
| Crash pic.jpg | image | 353 | 2026-03-31 | listed only |
| VID-20260331-WA0003.mp4 | video | 3006 | 2026-03-31 | listed only |
| image-20260331-191058.png | image | 168 | 2026-03-31 | listed only |
| [20260330 - 620_PCM_question set - O.pdf](attachments/51778_20260330%20-%20620_PCM_question%20set%20-%20O.pdf.md) | pdf | 105 | 2026-04-01 | converted |
| [20260330_EAGLE_620_DASOR_S2_26_3260.pdf](attachments/51780_20260330_EAGLE_620_DASOR_S2_26_3260.pdf.md) | pdf | 15266 | 2026-04-01 | converted |
| [20260401 - 620_PCM_DT_RFI - O.pdf](attachments/51779_20260401%20-%20620_PCM_DT_RFI%20-%20O.pdf.md) | pdf | 168 | 2026-04-01 | converted |
| 805305a8-8bb7-4c1d-ad5e-b94c83c84bc8.jpg | image | 76 | 2026-04-01 | listed only |
| C-102197 CW flash.hex | other | 19 | 2026-05-22 | listed only |
| [C-S102197 CW motor ESC flash hex 1.txt](attachments/57949_C-S102197%20CW%20motor%20ESC%20flash%20hex%201.txt.md) | text | 38 | 2026-05-22 | converted |
| C-S102221 CCW flash.hex | other | 19 | 2026-05-22 | listed only |
| [C-S102221 CCW motor ESC flash hex 1.txt](attachments/57950_C-S102221%20CCW%20motor%20ESC%20flash%20hex%201.txt.md) | text | 38 | 2026-05-22 | converted |
| avrdude.conf | other | 434 | 2026-05-22 | listed only |
