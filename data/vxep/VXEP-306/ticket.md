# VXEP-306: VXE 439 Fuel cell not reaching adequate power in flight

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** High
- **Created:** 2024-03-25
- **Updated:** 2026-09-15
- **Resolved:** 2024-07-02
- **Reporter:** Pat Wells
- **Assignee:** Sean Wendling
- **Creator:** Pat Wells
- **Labels:** Hardware, PMA263, Weekly-incident-tracker
- **Links:** Linked issue cannot finish until this issue finishes. VXEP-366 (VXE 439 Three minutes after launch and transition the AV went into an automated RTB that could not be corrected); relates to VA-1683 (Consider making fuel cell emulator to test data link, aircraft HIL testing, etc.); relates to VA-1682 (If communication is lost, set fuel cell output power based on fuel cell output voltage. Ex: if it reads low, that indicates that the HLB is draining, so the fuel cell output power should be increased until voltage reaches the target voltage.); relates to RMA-257 (D4500252 240606  (439 Incident))
- **Customer:** PMA263
- **Vehicle Tail Number:** 439
- **Vehicle Configuration:** Fuel cell
- **Other Stakeholder (as required):** Cameron Chapman
- **Problem Type:** Other (explain in description)
- **Incident Type:** Other (Record"Event Type: XXXXXX" in the description)
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

AAR File attached

From customer:
Fuel Cell was confirmed to meet max power on the ground while recharging a less than 90% HLB. Operators say in flight the Fuel Cell was no longer reaching 440-450W, and RTB’d.
The AV was recovered without damage with approximately 4% HLB remaining.

Files: VXEP-306 VXE-439 Fuel Cell not reaching adequate power in flight

## Corrective Action

Recommended CAs: 
- https://jenaero.atlassian.net/browse/VA-1682
- https://jenaero.atlassian.net/browse/VA-1683

## Plan

- Quarantine battery and fuel cell involved until data review complete.
- Plan:
- @Robert Redfield  to replace PCA0130 unit and perform incoming QC test to evaluate stack health and assess what materials are needed to complete repair.
- Data review following inspection and QC test.
- @Sean Wendling update and complete incident report with C/CAs for the failure and summarize repair steps.

## Issue Status

Battery & Fuel Cell Assessment in progress
- Battery has been reviewed and is safe to operate.
- Fuel Cell PCA0120 board replaced in Ann Arbor, retested and returned to customer. 
- Incidence of PCA0120 failure recorded. The current production variation of Main Control Board (PCA0130) design eliminates possibility of this failure mode.

## Root Cause

Confirmed: PCA0120 (D450XR Main Control Board) Short resulting in failure to output power. Comm link was lost to fuel cell as a result of this failure, requiring return of the fuel cell to validate the failure mode. 
Data review and Physical inspection complete. Result is that PCA0120 Main Control Board for the D450XR had an internal short leading to a failure to produce power. This is the first known instance of this occurrence in aircraft operation. 
“The 3V3 and 3V3_SW were shorted together. I removed the P-Channel Mosfet Q3. 3V3 was no longer shorted to GND and only 3V3_SW was shorted to GND. When removing components to find the short, I removed U13 and its coupling capacitors and the 3V3 short was gone”.

## Comments (33)

### Cameron Chapman, 2024-04-24

Pasting teams chat with Sean.
[9:56 AM] Cameron Chapman
Thanks for the troubleshooting help. Can you please update these fields as you proceed. They are helpful for quickly seeing what the status and next steps of an investigation are 
 
like 1
[9:58 AM] Cameron Chapman
These do not seem aligned 
 
[9:58 AM] Cameron Chapman
450 vs 400
[10:00 AM] Sean Wendling
Our output current ramp rate is much slower than the power target. 40 seconds would align with the amount of time I would expect for the system to react
[10:00 AM] Cameron Chapman
I think creating a timeline of events and plotting motor power would be helpful. See ppt template for an example
[10:00 AM] Sean Wendling
My zoom was a bit weird for that chart. 
[10:00 AM] Sean Wendling
Okay, I can do that! 
[10:01 AM] Cameron Chapman
It still seems like it settles 50W less than target 40 seconds after ramp start
[10:01 AM] Cameron Chapman
Is max out possible 400 or 450W

### Cameron Chapman, 2024-04-26

[Wednesday 10:40 AM] Sean Wendling
I suspect that the fuel cell goes offline while the system is ramping. I will check to ensure the ramp rate is in alignment with 100mA/s increase that we target. 
[Wednesday 10:41 AM] Sean Wendling
Do you have a breakdown of what all the log variables are from the flight side? Like a chart that has a written description of each variable?
[Wednesday 10:42 AM] Sean Wendling
The system can do 500W output in an emergency. Nominal is 450W
[Wednesday 10:47 AM] Cameron Chapman
oh ok. So you think it stops communicating when the line goes flat. That would make sense. Do the other variables change at that point, or are all values in the XCOM log stopping at that point?
[Wednesday 10:47 AM] Cameron Chapman
I think the plotter tool has some info on each variable
[Wednesday 10:48 AM] Cameron Chapman
# How to Decipher Data

VXE Documentation - Most complete list of log glossaries, other information.
VXE-FCD-VTOL Log Glossary.docx
VXE-FCD-XCOMM Log Glossary.docx
Cam started this file, which is a list of all of the logs, some info of what they contain. Goal is to fully populate it.
Flight data log descriptions.xlsx
VXE-FCD-XCOMM Log Glossary.docx
VXE-FCD-VTOL Log Glossary.docx
Flight data log descriptions.xlsx
[Wednesday 10:48 AM] Cameron Chapman
https://jenaero.atlassian.net/wiki/spaces/EF/pages/13467649/Flight+Data+Processing+and+Review 
Log in with Atlassian account
Log in to Jira, Confluence, and all other Atlassian Cloud products here. Not an Atlassian user? Sign up for free.
[Wednesday 10:50 AM] Sean Wendling
All Fuel Cell data stops. What is interesting is that not every variable in the entire log stops. Its why I cant really assess whether the fuel cell isnt performing properly.
[Wednesday 10:50 AM] Sean Wendling
Awesome! I will review what you have. lol
[Wednesday 10:59 AM] Cameron Chapman
the top ones are more complete than the one i started. You are welcome to add info to any of them
[Wednesday 11:01 AM] Cameron Chapman

Sean Wendling
All Fuel Cell data stops. What is interesting is that not every variable in the entire log stops. Its why I cant really assess whether the fuel cell isnt performing properly.

 This seems to indicate that the fuel cell or something in the comms chain stopped working while the rest of the aircraft worked. Can you tell if fuel cell power changes after is stopped responding? May be hard to tell. Maybe see if it correlates to battery voltage dropping with the same aircraft power

### Cameron Chapman, 2024-05-29

@Sean Wendling are you able to investigate this further?

### Sean Wendling, 2024-06-03

Hey @Cameron Chapman , apologies for the delay on this. I will review the items we discussed. I do expect that if the fuel cell lost comms that it would ramp down the output regardless as it would not know the needed output from the AC. I will summarize in the report.

### Cameron Chapman, 2024-06-03

Thank you @Sean Wendling. Please always keep these fields above updated as well: (Ex: what are the next steps planned in the investigation, potential and confirmed causes, status and location of the fuel cell, etc.)
See https://jenaero.atlassian.net/wiki/spaces/EF/pages/23363854/Incident+Troubleshooting+and+Resolution+Tracking.  for more info.

[embedded image-20240603-165547.png]

### Cameron Chapman, 2024-06-04

Sean on call: “confident fuel cell was functioning before. Signal lost. Not sure what default power request is available from fuel cell. Suspected cause: signal was lost from aircraft. If no voltage seen via serial, it will not output power” 
Plan: 
- Request fuel cell return. Pat
- Test serial link to aircraft. SLO EEs
- Pull logs for previous flights and post to linked sharepoint. SLO EEs
- Review logs for previous flights. Update investigation status fields above and ppt.

Recommended CA: If communication is lost, set fuel cell output power based on fuel cell output voltage. Ex: if it reads low, that indicates that the HLB is draining, so the fuel cell output power should be increased until voltage reaches the target voltage.

### Cameron Chapman, 2024-06-04

Moved old findings from desc: 
Issue looked at by Ann Arbor team feedback from @Sean Wendling  below:
The fuel cell appears to be operating as it should be, so I am wondering if someone in SLO could speak to the health of the HLB based on the data. The behavior of the fuel cell leads me to think that it is tapering down the output wattage as the battery isnt accepting it. It could help to know if this issue occurs with a different HLB installed. 
- @Sean Wendling  responding to your comment in the description. The connection to the HLB is directly to the terminals. There is no charge limiting. If the battery was not charging, it would be reflected by a higher voltage (which the low SOC reading seems to refute). The issue is likely in the XCOM which tells the fuel cell what to charge to, the fuel cell, or a voltage sensor somewhere. -Cam
- Thanks Cam, Add’tl validation will proceed. Link to Incident report is below.

### Sean Wendling, 2024-06-04

@Cameron Chapman , I got more clarity on this issue in speaking with my team here. I was incorrect in my thought that the fuel cell will not charge the battery when it is not receiving signal. Fuel cell should have reverted to its default output target until the battery returned to full charge or signal was restored. 
I think it was a good call to return the fuel cell. I will add to the plan diving a bit deeper into the data on my end to try to see exactly what power target the fuel cell was after before it depleted prior to receiving it here in Ann Arbor. There are a handful of checks we can complete here to see if there is something more is going on, but at the very least we can say with significantly more confidence that this fuel cell is safe to operate.

### Cameron Chapman, 2024-06-04

@Sean Wendling what is the default power output? What would the fuel cell do if aircraft demand was higher than the default power output? Would it increase its output power based on measured output voltage?

### Sean Wendling, 2024-06-05

Default is 450W, so the fact that the battery drained is strange. Considering apPower was ~ 250W throughout the fixed wing flight something went wrong here. 
Is apPower the primary consumer during fixed wing flight or is there other variables I should be looking a?. I looked through the glossary lastnight, and there were alot of power related variables. I guess i didnt include payload power utilization, though I was suspecting that it wasnt alot.

### Sean Wendling, 2024-06-05

@Cameron Chapman It will cap out at 500W of power output. If the required power exceeds what the fuel cell is capable of outputting, then the HLB will slowly drain.

### Cameron Chapman, 2024-06-05

@Sean Wendling in fuel cell configuration, the fuel cell and HLB power both the fixed wing (apPower on the XCOM log) and VTOL system (vtPbatt), so you would need to add those for total power consumption. In fixed wing flight, it should be mostly apPower, so it does sound like something on the fuel cell side went wrong. There are a lot of fuel cell parameters on the XCOM log that could be useful to review, such as psOut                   Fuel cell output power to command. Of course, these would not mean much if the comm link to the fuel cell was not working.

### Sean Wendling, 2024-06-06

@Cameron Chapman Yeah, once I get the fuel cell back I can review whether there was a failure on the serial communication from the fuel cell. I will take a look at those metrics in particular, and evaluate the total power consumption for the vehicle throughout the flight and put together a timeline while we wait to get it back. Thanks for the info!

### Cyrus Blevins, 2024-06-11

@Sean Wendling @Cameron Chapman I am unable to test the fuel cell serial link, as there is not an accessible fuel cell here. You might want to hand this off to someone else (Raj was given this VXE plane originally so you could ask him). I was able to power the VXE through the battery and extracted some of the most recent files. They are uploaded to the Sharepoint > VXE 439 DATA.

(I will paste these details to my linked ticket for easy access in case this comment gets drowned out later https://jenaero.atlassian.net/browse/VXEP-430 )
2024/06/11 files generated: [XCL00814, XCL00815, XCL00816, FDRRECOV].csv, XCEVLOG.txt
I also grabbed some older files just in case
2024/04/15 files generated: [XCL00813, FDR00813, XCL00809, FDR00809].csv

As per advice by@Brandon Slater FDRRECOV.csv, XCEVLOG.txt, and the most recent XCL files are probably the most important.

### Sean Wendling, 2024-06-14

Hey All, the fuel cell has been received in Ann Arbor. Our team will begin to investigate and get back to you with feedback about what we find and how that might guide the investigation on the aircraft side. @Cameron Chapman , I updated the plan and Issue Status to reflect actions and included @Robert Redfield who is responsible for incoming RMA review in AA. (Let me know if you would like me to create or include VA tasks for this review). Thanks!

### Robert Redfield, 2024-06-14

It was observed that the fuel cell would not power on. No LED activity observed.
No signs of physical damage to control board. (deformation, electrical scorching, or otherwise)
Unable to pull cycle count/hours
Unable to extract calibration file
Root cause of the main control board failure indicates an electrical short of the 3.3vdc circuit. Failure of this circuit will prevent the microcontroller of the circuit board to function. There is also the potential that a failure/defect within the microcontroller could damage the 3.3vdc circuit. It is unknown at this time which failure could have happened first. (the chicken or egg scenario)
It should be mentioned that a complete control board failure mid operation could cause damage to the fuel cells within the stack due the system not being able to perform it’s cooldown operation successfully.

### Dylan Peters, 2024-06-18

Failure analysis for the PCA0120:

The PCA0120 has two 3V3 sources. The original 3V3 that is always on and goes to flight critical parts of the board (Tiva, Comm). It also has another 3V3 source, which we switch on/off (we refer to this as 3V3_SW). The 3V3_SW powers all other aspects, including current sensors, ADCs, thermistors, motor control, etc.

Initially probing, the 3V3 and 3V3_SW were shorted together. I removed the P-Channel Mosfet Q3. 3V3 was no longer shorted to GND and only 3V3_SW was shorted to GND. When removing components to find the short, I removed U13 and its coupling capacitors and the 3V3 short was gone.

Unfortunately, I can’t speak for what caused the failure. I can’t be for sure if a 3V3/3V3_SW surge caused a chip failure or if a chip failure caused the short to GND. U13 is a BLDC motor driving chip that is only used on the D450XR. It only handles signal and is primarily hall-effect driven. 

This is the only failure I’ve seen in this case and is also obsolete now. We changed our software to drive our BLDC motors using separate LIN on the D450+ (PCA0130).

### Sean Wendling, 2024-06-18

@Cameron Chapman , Update to the ticket made following physical inspection. @Robert Redfield is leading the repair along with my support in documenting and developing corrective actions. We should understand what the lead-time for return of the fuel cell sometime this week.

### Robert Redfield, 2024-06-18

I cannot, at this time, commit to a 1-week turnaround for this fuel cell.   Fuel cell failure analysis is still in progress and I do not yet know stack health for this fuel cell.   I will update ticket as I know more.

### Sean Wendling, 2024-06-18

Moving these notes to the comments as they were completed and the issue status has been updated. 
--
- Additional Info required for Fuel Cell Assessment.
- Flight logs to be reviewed by Dave G and VXE Team under https://jenaero.atlassian.net/browse/VXEP-366
- Power Budget and HLB depletion will be reviewed by Sean W and Ann Arbor Team to better understand fuel cell behavior.
- Battery health assessment complete.

Cycle count was reading 28, which included multiple hot swap “cycles” in that count.  True Thermal cycle count is known to be less but the exact figure is unknown.

### Sean Wendling, 2024-06-04

@Cameron Chapman , I got more clarity on this issue in speaking with my team here. I was incorrect in my thought that the fuel cell will not charge the battery when it is not receiving signal. Fuel cell should have reverted to its default output target until the battery returned to full charge or signal was restored. 
I think it was a good call to return the fuel cell. I will add to the plan diving a bit deeper into the data on my end to try to see exactly what power target the fuel cell was after before it depleted prior to receiving it here in Ann Arbor. There are a handful of checks we can complete here to see if there is something more is going on, but at the very least we can say with significantly more confidence that this fuel cell is safe to operate.

### Cameron Chapman, 2024-06-04

@Sean Wendling what is the default power output? What would the fuel cell do if aircraft demand was higher than the default power output? Would it increase its output power based on measured output voltage?

### Sean Wendling, 2024-06-05

Default is 450W, so the fact that the battery drained is strange. Considering apPower was ~ 250W throughout the fixed wing flight something went wrong here. 
Is apPower the primary consumer during fixed wing flight or is there other variables I should be looking a?. I looked through the glossary lastnight, and there were alot of power related variables. I guess i didnt include payload power utilization, though I was suspecting that it wasnt alot.

### Sean Wendling, 2024-06-05

@Cameron Chapman It will cap out at 500W of power output. If the required power exceeds what the fuel cell is capable of outputting, then the HLB will slowly drain.

### Cameron Chapman, 2024-06-05

@Sean Wendling in fuel cell configuration, the fuel cell and HLB power both the fixed wing (apPower on the XCOM log) and VTOL system (vtPbatt), so you would need to add those for total power consumption. In fixed wing flight, it should be mostly apPower, so it does sound like something on the fuel cell side went wrong. There are a lot of fuel cell parameters on the XCOM log that could be useful to review, such as psOut                   Fuel cell output power to command. Of course, these would not mean much if the comm link to the fuel cell was not working.

### Sean Wendling, 2024-06-06

@Cameron Chapman Yeah, once I get the fuel cell back I can review whether there was a failure on the serial communication from the fuel cell. I will take a look at those metrics in particular, and evaluate the total power consumption for the vehicle throughout the flight and put together a timeline while we wait to get it back. Thanks for the info!

### Cyrus Blevins, 2024-06-11

@Sean Wendling @Cameron Chapman I am unable to test the fuel cell serial link, as there is not an accessible fuel cell here. You might want to hand this off to someone else (Raj was given this VXE plane originally so you could ask him). I was able to power the VXE through the battery and extracted some of the most recent files. They are uploaded to the Sharepoint > VXE 439 DATA.

(I will paste these details to my linked ticket for easy access in case this comment gets drowned out later https://jenaero.atlassian.net/browse/VXEP-430 )
2024/06/11 files generated: [XCL00814, XCL00815, XCL00816, FDRRECOV].csv, XCEVLOG.txt
I also grabbed some older files just in case
2024/04/15 files generated: [XCL00813, FDR00813, XCL00809, FDR00809].csv

As per advice by@Brandon Slater FDRRECOV.csv, XCEVLOG.txt, and the most recent XCL files are probably the most important.

### Sean Wendling, 2024-06-14

Hey All, the fuel cell has been received in Ann Arbor. Our team will begin to investigate and get back to you with feedback about what we find and how that might guide the investigation on the aircraft side. @Cameron Chapman , I updated the plan and Issue Status to reflect actions and included @Robert Redfield who is responsible for incoming RMA review in AA. (Let me know if you would like me to create or include VA tasks for this review). Thanks!

### Robert Redfield, 2024-06-14

It was observed that the fuel cell would not power on. No LED activity observed.
No signs of physical damage to control board. (deformation, electrical scorching, or otherwise)
Unable to pull cycle count/hours
Unable to extract calibration file
Root cause of the main control board failure indicates an electrical short of the 3.3vdc circuit. Failure of this circuit will prevent the microcontroller of the circuit board to function. There is also the potential that a failure/defect within the microcontroller could damage the 3.3vdc circuit. It is unknown at this time which failure could have happened first. (the chicken or egg scenario)
It should be mentioned that a complete control board failure mid operation could cause damage to the fuel cells within the stack due the system not being able to perform it’s cooldown operation successfully.

### Dylan Peters, 2024-06-18

Failure analysis for the PCA0120:

The PCA0120 has two 3V3 sources. The original 3V3 that is always on and goes to flight critical parts of the board (Tiva, Comm). It also has another 3V3 source, which we switch on/off (we refer to this as 3V3_SW). The 3V3_SW powers all other aspects, including current sensors, ADCs, thermistors, motor control, etc.

Initially probing, the 3V3 and 3V3_SW were shorted together. I removed the P-Channel Mosfet Q3. 3V3 was no longer shorted to GND and only 3V3_SW was shorted to GND. When removing components to find the short, I removed U13 and its coupling capacitors and the 3V3 short was gone.

Unfortunately, I can’t speak for what caused the failure. I can’t be for sure if a 3V3/3V3_SW surge caused a chip failure or if a chip failure caused the short to GND. U13 is a BLDC motor driving chip that is only used on the D450XR. It only handles signal and is primarily hall-effect driven. 

This is the only failure I’ve seen in this case and is also obsolete now. We changed our software to drive our BLDC motors using separate LIN on the D450+ (PCA0130).

### Sean Wendling, 2024-06-18

@Cameron Chapman , Update to the ticket made following physical inspection. @Robert Redfield is leading the repair along with my support in documenting and developing corrective actions. We should understand what the lead-time for return of the fuel cell sometime this week.

### Robert Redfield, 2024-06-18

I cannot, at this time, commit to a 1-week turnaround for this fuel cell.   Fuel cell failure analysis is still in progress and I do not yet know stack health for this fuel cell.   I will update ticket as I know more.

### Sean Wendling, 2024-06-18

Moving these notes to the comments as they were completed and the issue status has been updated. 
--
- Additional Info required for Fuel Cell Assessment.
- Flight logs to be reviewed by Dave G and VXE Team under https://jenaero.atlassian.net/browse/VXEP-366
- Power Budget and HLB depletion will be reviewed by Sean W and Ann Arbor Team to better understand fuel cell behavior.
- Battery health assessment complete.

Cycle count was reading 28, which included multiple hot swap “cycles” in that count.  True Thermal cycle count is known to be less but the exact figure is unknown.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V439_240318_184953_pack.zip | archive | 1980 | 2024-03-25 | listed only |
| image-20240603-165547.png | image | 36 | 2024-06-03 | listed only |
