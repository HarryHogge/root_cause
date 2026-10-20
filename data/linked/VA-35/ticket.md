# VA-35: 511 CW Input power connector damaged

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-08-10
- **Updated:** 2025-05-28
- **Resolved:** 2025-05-28
- **Reporter:** Cameron Chapman
- **Assignee:** Jeremy Kostel
- **Creator:** Cameron Chapman
- **Labels:** Weekly-incident-tracker
- **Links:** clones VA-31 (EA Internal: 516 center wing damaged. 511 fuselage+516CW LW motor test failed. ); relates to ENG-1685 (ENG incidents should have the same fields and workflow as VIT2 incidents.  Should create corrective action and containment issues in ENG as well. ); relates to ENG-2181 (EA Internal: VXE511 Aborted Launch at 2ft, VTOL ESCs stuck in initialization loop); relates to FS2-690 (Eng 2182); relates to FS2-695 (ENG-2183 VTOL AP WDT investigation); relates to VXEP-481 (8D #24 – CW to HLB AS150 Connection Issues​ Corrective Actions); relates to VXEP-13 (TPTR-51 516 VTOL Motors failed to engage during Launch Wizard 511/516 CW damage); relates to VA-392 (511 CW Input power connector damaged Identify C/CA); causes VXEP-28 (TPTR-94 HLB reading incorrect percentage compared to measurement with checker); relates to VXEP-12 (TPTR-87 VXE 511 VTOL Connector Issues 516 CW. Contains Main connector/contact C/CAs); relates to RMA-128 (VXE 511 070523); relates to RMA-129 (VXE 516 230705 TIQ); relates to VA-1300 (TPTR-87 VXE 511 VTOL Connector Issues- Determine cause of high current/power); relates to VA-330 (TPTR-87 VXE 511 VTOL Connector Issues)
- **Part Number(s):** VXE30
- **Corrective Action:** See https://jenaero.atlassian.net/browse/VXEP-12
- **Other Stakeholder (as required):** Matt Philley

## Description

511 center wing was pulled from service due to loose object. After it was returned, we discovered a solder blob.

This issue is being used to track the 511 CW damage. See https://jenaero.atlassian.net/browse/ENG-2182 for related incident and 516 CW damage. 
See external issue for initial troubleshooting: https://jenaero.atlassian.net/browse/VIT2-322 
Please save files and plots here: https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Investigations/Old%20Docs-use%20flight%20safety%20Incident%20Reports%20-%20Shortcut%20now/VIT2-322,%20Tail%20516-Fuse%20511%20and%20516-Wing?csf=1&web=1&e=PmlXN0 
After discovering a loose object in CW 511 we switched to the wing set from 516. One flight of 511 with 516 wing set was conducted. After that flight one of the students mentioned that the HLB (S/N 2-1801) had a strong smell from around the discharge connector. The connector looked normal. During the LW for the second flight the motor check failed to spin the lift rotors more than a half turn. The VTOL Control Window indicated VTOL launch not OK and the HLB voltage was fluctuating 7-27V. The LW was canceled. At this point we were no longer going to fly this aircraft. I inspected the CW high voltage connector and it appears to have some discoloration. For troubleshooting we tried a different HLB and were able to complete the LW without issue. We also retried the original HLB and passed the LW without issue. It seemed like a good day to not crash a plane so we did not attempt a flight.

## Plan

- https://jenaero.atlassian.net/browse/VA-500  @Hayden Jeanor or @Jeremy Kostel when you have time, can you please run the 511 motors on the dyno and compare power vs thrust (torque as well) compared to a normal motor?
- Measure contact impedance with the latest method and report results.

## Issue Status

The Avionics compartments covers were removed from both of the CWs and visually inspected for markings of possible over-heated wires, components, PCB traces. There were no noticeable marks or damages. 
511-
- Have VTOL data - VTL00029 and VTL00018 attached 
- VTL00029 shows a constant high current in the takeoff phase. There is also a 190 A peak in the landing portion.
- CW input power connector showed a solder blob at the base of the contact, which indicates overheating.
- At a base current of 150A a fully mated connector has a slower increase of temperature compared to if it is not fully mated. This is also true for currents that are above 150 A.
- When the connectors are not fully mated, and knocking is applied to the connector there is a drop in current.
- on 511 there were no loose objects when removing the avionics cover
- Voltage reading for battery S/N 2-1801
- With no load - 29.1V
- With Load 28.4V
- Contact impedance measures 195uohms, which is over the newly established criteria of 180uohms. This could be due to the damage of the overcurrent, or it could have already been present and increased the resistance and temperature of this connection.

## Root Cause

- Over current - can be seen in VTL00029
- Not fully mated - the testing on 542 shows that when the connectors are not fully matted temperature increases faster than if they were fully connected.
- See https://jenaero.atlassian.net/browse/VXEP-12  and paste relevante C/CA from there.

## Comments (6)

### Cameron Chapman, 2023-08-18

@Laszlo Juhasz please see new actions in this issue.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent

### Cameron Chapman, 2023-08-29

@Laszlo Juhasz and @Adrian Garcia please update investigation status with major findings and plan with remaining steps for each of your top investigations.

### Cameron Chapman, 2023-09-03

@Laszlo Juhasz @Adrian Garcia Comments added to investigation ppt. Please review.

### Jeremy Kostel, 2024-09-19

For some reason not letting me set to “on hold” but placing on hold until we have time do this

### Christa Meck, 2025-04-17

Removed parent to prep for Incident hierarchy change.  Parent is linked as Linked issue.

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [511 and 516 charts.docx](attachments/15810_511%20and%20516%20charts.docx.md) | docx | 1796 | 2023-08-10 | converted |
| [Vehicle Investigation V516+511.pptx](attachments/15811_Vehicle%20Investigation%20V516+511.pptx.md) | pptx | 22024 | 2023-08-10 | converted |
| charts.docx | docx | 1565 | 2023-08-10 | no text found |
| 511_Power Connector.jpg | image | 356 | 2023-08-18 | listed only |
| [511 flight data plots.docx](attachments/16051_511%20flight%20data%20plots.docx.md) | docx | 1437 | 2023-08-29 | converted |
| [542 Investigation report.docx](attachments/16049_542%20Investigation%20report.docx.md) | docx | 6605 | 2023-08-29 | converted |
| [new connector Investigation report.docx](attachments/16050_new%20connector%20Investigation%20report.docx.md) | docx | 1635 | 2023-08-29 | converted |
