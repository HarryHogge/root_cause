# ENG-2983: 511 LW motor test failed. 511 and 516 center wings damaged.

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-06-28
- **Updated:** 2025-06-02
- **Resolved:** 2025-05-21
- **Reporter:** Daniel Lloyd
- **Assignee:** Laszlo Juhasz
- **Creator:** Daniel Lloyd
- **Labels:** 8-28-Sprint, TIQUILA, TIQUILA-Blocker
- **Links:** relates to RMA-128 (VXE 511 070523); relates to RMA-129 (VXE 516 230705 TIQ); relates to ENG-1810 (Is there a way to pull the previous flight log, or all flight logs using the GCS or another automated tool? ); relates to ENG-3160 (Determine overcurrent abort limit, then implement auto-abort when present. Update manuals accordingly. ); relates to VA-33 (VXE511 Aborted Launch at 2ft, VTOL ESCs stuck in initialization loop); is caused by VXEP-385 (New Connectors and Contacts, Overall Requirements Review); relates to VA-276 (VIT2-322 Implement corrective actions); relates to VA-275 (VIT2-322 Hands on trobleshooting. Identify cause and corrective actions.); relates to VA-277 (VIT2-322 Review C/CA); relates to VXEP-12 (TPTR-87 VXE 511 VTOL Connector Issues 516 CW. Contains Main connector/contact C/CAs); relates to VXEP-13 (TPTR-51 516 VTOL Motors failed to engage during Launch Wizard 511/516 CW damage); relates to FS2-952 (Do any of the flight logs list what equipment was connected? If not, could we add this feature?); causes SP-206 (Improve Power Connector, Contacts, and Signal Connectors); relates to TQT-470 (Inform Customer of Airworthiness Directive (No: Airworthiness Directive (AD)_Mating Connection_2023-10-12 _A) )

## Description

Please save files and plots here: https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Investigations/VIT2-322,%20Tail%20516-Fuse%20511%20and%20516-Wing?csf=1&web=1&e=0CI18P 
After discovering a loose object in CW 511 we switched to the wing set from 516. One flight of 511 with 516 wing set was conducted. After that flight one of the students mentioned that the HLB (S/N 2-1801) had a strong smell from around the discharge connector. The connector looked normal. During the LW for the second flight the motor check failed to spin the lift rotors more than a half turn. The VTOL Control Window indicated VTOL launch not OK and the HLB voltage was fluctuating 7-27V. The LW was canceled. At this point we were no longer going to fly this aircraft. I inspected the CW high voltage connector and it appears to have some discoloration. For troubleshooting we tried a different HLB and were able to complete the LW without issue. We also retried the original HLB and passed the LW without issue. It seemed like a good day to not crash a plane so we did not attempt a flight.

## Comments (33)

### Daniel Lloyd, 2023-06-29

Resistance across the resistor measured at 96.9 ohms

### Sean Odell, 2023-07-06

@Scott Stuckey @Cameron Chapman @Greg Fryer  This aircraft arrived late last night. Who is going to be the engineer to start the evaluation?

### Sean Odell, 2023-07-06

Should there be another VIT2 opened for VXE-516 CW specifically @Daniel Lloyd ?

### Daniel Lloyd, 2023-07-06

The resister on the power cable appears to be bad causing this issue. I you like you can change this ticket from aircraft 511 to CW 516.

### Sean Odell, 2023-07-06

@Scott Stuckey @Cameron Chapman @Daniel Lloyd @Carson Buckley The center wing does show some signs of electrical arc/burnt.  That said, Carson and I quickly checked the resistance on the AS150 connector. It should be around 6 ohms and it registered 110 Ohms. 
Who would like to do the electrical evaluation on this Center wing to confirm?

### Cameron Chapman, 2023-07-07

Thanks @Daniel Lloyd for the detailed incident report. It sounds like HLB (S/N 2-1801) was loosing connection to CW 516. To make sure we have the right logs, was 516 CW flying with the 511 fuselage? I added that to configuration field. 
@Sean Odell please deliver to engineering. @Laszlo Juhasz, can you please take a look at this, and work with other EEs to review the VTOL current in the attached FDR zip. This could be a good training opportunity for Maddie and other interns arriving Monday.

### Daniel Lloyd, 2023-07-07

511 did that one flight with the 516 wing set.

### Sean Odell, 2023-07-10

@Cameron Chapman Both 511 and 516 delivered to Engineering. Please assign to the correct person. Thank you!

### John Clark, 2023-07-25

@Kurt Burian I took this one back so you can help @Connor Peebles . I know what Laszlo needs.

### John Clark, 2023-07-25

@Laszlo Juhasz @Daniel Lloyd I do not see any launch or land in any of the below as provided by the AAR. Please tell me if I am missing something.
[embedded: image-20230725-223313.png]

### Daniel Lloyd, 2023-07-26

CW 516 performed one flight on aircraft 511 without issue. It was during the LW for the second flight that we experienced HLB voltage issues. we cancelled the LW and collected an AAR with FDR. If you want data from the previous flight you may have to dig around in the CW.
@John Clark

### John Clark, 2023-07-26

@Laszlo Juhasz please let me know if I can help you find the logs that are needed.

### Laszlo Juhasz, 2023-07-26

@John Clark  The data from 511 and 516 recovered (attached),
[embedded: 511_516Data.zip]
 but unfortunately, the 516 VTOL is corrupted a bit or two. 
[embedded: 511_Power Connector.jpg]
[embedded: Residue.jpg]

### John Clark, 2023-07-27

@Laszlo Juhasz looking at your data now. @Connor Peebles can you detail the corruption you encountered gathering this data. Face to face might be easiest?

### John Clark, 2023-08-03

@Laszlo Juhasz I was able to identify 4 flights on 516 CW. Two of those might be of interest. Please let me know anything else you might need.
[embedded: Vehicle Investigation V516.pptx]

### Cameron Chapman, 2023-08-04

Thanks @John Clark
- Do you have excel files for those plots? Can you please post them to a shared location like this one? I think saving plots and summaries to shared locations helps the efficiency of troubleshootinghttps://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Investigations/VXE%20Wing%20516%20Fuselage%20511%20VTOL%20Power%20Issue?csf=1&web=1&e=RlYDz5
- On separate plots, can you please plot the currents, voltages, and throttles of VTOL00029 vs an earlier flight? 
- A higher current could have caused this damage.
- A higher resistance connections could have also (which would be visible in the logs by a lower measured voltage and higher throttles).
- Possible cause.
- If the connector was not fully mated, it could increase resistance and lead to this issue. The connectors are known to be difficult to mate and not super clear when fully mated. -check voltage readings during flight.
- Manufacturing defect. -Measure contact resistance vs normal. inspect/dissassemble connectors. Would be great to locate and inspect the battery
- Weak battery leading to higher current. -check voltage readings.
- Heavy aircraft-no reports of abnormal configuration.

@Daniel Lloyd do you know where the battery for this flight is located? I think HLB (S/N 2-1801)

### Laszlo Juhasz, 2023-08-04

@John Clark @Daniel Lloyd @Sean Odell  Based on the awesome report from John, there is an indication of high current flow during the flights. For reference, I’m sharing the result of our benchtop thermal testing for similar power connector and wires at 150/200A. The red terminal heats up the most due to the single 8AWG wire temperature rise and the reduced surface area. Even if there is no manufacturing error that terminal heats up almost twice as fast as the return terminal having 2x10AWG wires connected to it.  
[embedded: Lift_Battery Connector_Thermal_Test.jpg]

### Cameron Chapman, 2023-08-07

@Laszlo Juhasz those plots show 150 A for 2 min is still a lot lower than the melting point of solder. The worst profile in the plots shows ~170A for 30 seconds. This does seem high, but possibly not high enough to melt solder with a standard connector. 
Please see investigation plan for recommended next steps.

### Greg Fryer, 2023-08-08

@Cameron Chapman @Laszlo Juhasz  Please generate a complete report (John’s ends at the data) that lines up the incident report with the conclusion, and store here: VIT2-322, Tail 516-Fuse 511-Wing (folder also linked in description). Root cause needs to address the reason for high amperage, or at least the not-disproved reasons.
Assuming remaining possible causes do not indicate an issue with the aircraft, please also send a disposition to @Sean Odell so he can get the aircraft repaired and released.

### Matt Philley, 2023-08-09

Linking NCR related to a similar issue happening in SCO of AC 538 on 6/28/23 (NCR 1318) where we found a defect in the AS150 connector of the 107-102264 Dual Current Sense Assy which required excessive force to fully mate the connector, which caused the connector to not be fully mated and left loose.

### Daniel Lloyd, 2023-08-14

@Cameron Chapman that HLB 1801 is somewhere in the Edge building. I would ask Jeff.

### Cameron Chapman, 2023-08-14

Thanks Dan! @Jeff Hartsell , do you know where S/N 2-1801 is? Could we have it to test for potential connection or build issues?

### Jeff Hartsell, 2023-08-14

@Cameron Chapman Yes, I have 2-1801.  I’ll set it aside tomorrow with the Shipping Team.

### Cameron Chapman, 2023-08-15

Thanks Jeff. @Adrian Garcia can you please pick this battery up today and red tag it with this incident number?

### Matt Philley, 2023-08-15

Confirmed Battery SN 2-1801 is in SLO, has been tagged with a red NCR tag and Orange RMA tag. Currently on the investigation workbench in Engineering.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent.

### Noah Chavez, 2023-09-08

Another issue related to this happened on Wednesday (9/7/2023). This can be seen in NCR-1481. Picture of the solder in the connector can be seen below.
[embedded: image-20230908-132004.png]

### Cameron Chapman, 2023-09-08

@Daniel Lloyd do you know the configuration/weight of these flights? 511 VTOL logs are showing consistently high power levels, which would indicate a heavy aircraft, extra inefficient propulsion system, and/or very low air density. @Ryan Christino or @Former user , can you help us investigate this? 511 VTL plots.xlsx
[embedded: image-20230908-215915.png]

### Daniel Lloyd, 2023-09-12

@Cameron Chapman these aircraft were being used during training. They would have been configured with a Trillium payload, at most the heavier HD55. They did not have any additional payloads.

### Daniel Lloyd, 2023-09-12

@Cameron Chapman I don’t have the DA reading for these flights. The field elevation was near 2500 ft, temp was near 88 deg and low humidity. That’s going to put the DA above 2500 ft. Not high but more than you’re going to see from SMR.

### Cameron Chapman, 2023-09-13

Thanks @Daniel Lloyd, this is very useful information. We will investigate.

### Mark Squillante, 2023-10-25

Tested 516’s AS150 contact, measured 313 uOhms (>235 uOhms is failure). Anti-spark now measuring ~178 ohms.

### Mark Squillante, 2023-10-26

AS150 anti-spark contact was cleaned with isopropyl alcohol and remeasured, now measures 188 uOhms.

## Attachments (11)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| HLB Voltage.JPG | image | 136 | 2023-06-28 | listed only |
| IMG_1559[1].JPG | image | 2692 | 2023-06-28 | listed only |
| T95_V511_230627_103013_01_pack.zip | archive | 2047 | 2023-06-28 | listed only |
| image-20230725-223313.png | image | 11 | 2023-07-25 | listed only |
| 511_516Data.zip | archive | 75133 | 2023-07-26 | listed only |
| 511_Power Connector.jpg | image | 356 | 2023-07-26 | listed only |
| Residue.jpg | image | 352 | 2023-07-26 | listed only |
| [Vehicle Investigation V516.pptx](attachments/15684_Vehicle%20Investigation%20V516.pptx.md) | pptx | 22021 | 2023-08-03 | converted |
| Lift_Battery Connector_Thermal_Test.jpg | image | 1637 | 2023-08-04 | listed only |
| image-20230908-132004.png | image | 2127 | 2023-09-08 | listed only |
| image-20230908-215915.png | image | 12 | 2023-09-08 | listed only |
