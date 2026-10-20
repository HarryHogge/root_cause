# VXEP-232: Overheating Battery/Cable (Fuel Cell Support Kit SCO Test Config) -

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-12-21
- **Updated:** 2024-03-05
- **Resolved:** 2024-03-05
- **Reporter:** Cameron Chapman
- **Assignee:** Mark Squillante
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-640 (IRAD: B40 Battery Charger); relates to SP-206 (Improve Power Connector, Contacts, and Signal Connectors); relates to VXEP-389 (Develop Replacement for Troublesome/Non Mil-Stnd Board Mount/PCB Connectors); relates to ENG-1070 (IRAD: Battery Study Next Gen Lift)
- **Production Stakeholder:** Ben Norris
- **Other Stakeholder (as required):** Laszlo Juhasz
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

During SCO for a fuel cell support kit yesterday, the hybrid lift battery used to power(?) the regulators began to overheat, along with the connected test cable. Ben did a quick courtesy check on the affected battery (SN 2-1619) and found the board inside has been fried (see attached). I’ve also provided a transcript of our test set-up as described in our SCO document (see attached).
 
We are not 100% sure what is causing the issue or when it started, but we suspect that this particular test set-up is not intended to be used with the latest all-weather version of lift batteries.
 
Below is the list of all suspect hardware that will need to be re-validated. Note that all the hardware DID pass the SCO testing requirements, but the overheating may have negatively affected the hardware in other ways.
 
Suspect Hardware
- FCS1056 (PN FCS1000-801)

- 3EA Regulator and Solenoid Assy (PN FCS1000-ACC-805)

- SN 9715
- SN 6061
- SN 6062

- 1EA VXE30 Solenoid Test Cable (PN FCS1000-ACC-807)

- FCS1043 (PN FCS1000-801)

- 3EA Regulator and Solenoid Assy (PN FCS1000-ACC-805)

- SN 9702
- SN 9717
- SN 9721

- 1EA VXE30 Solenoid Test Cable (PN FCS1000-ACC-807)

 
For now, LM will stand-down from any further testing for the FCSK’s until an agreed path-forward has been deliberated. Note that Ben suggested that we could potentially circumvent the issue and continue SCO by using an older model of the lift battery. However, if the core issue is related to the test cable being incompatible with the new batteries, we would still need to resolve how the cable would be utilized out in the field.
 
Thanks,
Jun Park
Lockheed Martin Aeronautics Company
Supplier Quality Engineer
P:  408-203-1985

Test Setup:
[embedded file]
[embedded file]

## Corrective Action

- Open linked Jira issues for these. See linked issues below.
- Switching from a solder cup to a crimp style connector would likely mitigate the issue. https://jenaero.atlassian.net/browse/VA-1004

Improvements
- Using an economizer could reduce heat dissipation (see thermal image was taken after about 1minute at 19C ambient).
- Using a different wire securing instead of that sharp bracket and wire tie.
- Improve PCB signal connectors to reduce the chances of damage and shorts. https://jenaero.atlassian.net/browse/VA-1046

## Plan

- Likely cause identified. Determine CAs.
- Did we have electronics QC at the time this battery was made? 
- We did not have electronics QC at the time (October 2022)
- Determine reporting and customer comms requirements.

## Issue Status

Investigation complete. 
No faults discovered with solenoid or solenoid harness. Improvement suggestions in CAs.  
Investigation report: https://jenaero.sharepoint.com/:p:/r/sites/EngineeringTeam/_layouts/15/Doc.aspx?sourcedoc=%7BE4590243-4432-4156-A200-2C4B2D016671%7D&file=Investigation%20Report.pptx&action=edit&mobileredirect=true

## Root Cause

Intermittent short in 16 pin ODU wiring inside the battery, pins 8 and 9. This would short out cell 2. Most likely a broken wire strand causing intermittent short. 
- This intermittent nature could explain why the battery was operating nominally for a while, then shorted due to agitation when the operator was connecting the harness for the solenoid test. This short also can explain the heat observed, bad voltage readings, and damage to the PCB.

## Comments (43)

### Laszlo Juhasz, 2024-01-17

A brief update, the battery was dismantled, and the investigation is in progress.

### Cameron Chapman, 2024-01-21

@Mark Squillante, Laszlo will be out for a while. Are you available to investigate this tomorrow? 
Here were the next steps we planned. 
- Inspect battery and adapter harnesses for shorts. We suspect there may be a short on the unused pins of the adapter harness. Laszlo received a harness from Ben to test that,
- Create investigation report and attach photos of PCB damage, damaged pins, etc. List what pin number shows damage and what signal that corresponds to.
- Inspect for other items that could have caused the PCB damage.

Thank you

### Mark Squillante, 2024-01-22

Looks like the ODU pins 8 and 9 are shorted together, which would short out cell 2. Battery pack itself appears to have no shorts and ~540mV was measured across cell 2. I would likely have to cut the wires from the ODU to the 8 pin DF13 to determine which side has the short.
Here are pictures of battery control board and DF13 mating connectors for P5 and P6.
[embedded file]
[embedded file]
[embedded file]

### Mark Squillante, 2024-01-22

I tested the solenoid test cable using the cable tester and no shorts were found.
I tried to separate the 8 pin DF13 connector from its mate and they were melted together. I ended up breaking both sides of the connector but the short is now gone, so it looks like the short was in the DF13.
[embedded file]
[embedded file]
[embedded file]

### Mark Squillante, 2024-01-23

I did a more aggressive wiggle test this morning and found no shorts between pins 8 and 9 on the ODU. These are unused pins and the connector is pretty well potted, so it is likely this is not the root cause. 
[embedded file]
[embedded file]

### Mark Squillante, 2024-01-23

I was able to replicate the short by slightly wiggling the wires just behind the 16 pin ODU on the battery. Short is intermittent but very easy to recreate with a small amount of wire wiggling.

### Mark Squillante, 2024-01-23

I removed most of the potting on the ODU connector. The gray and violet wires were the shorted connection but unfortunately it seems I removed the short when removing the potting. Here are pictures before and after removing the potting. 
[embedded file]
[embedded file]
[embedded file]
[embedded file]
[embedded file]

### Mark Squillante, 2024-01-23

I asked @Thomas McMillan to look at the battery and he said that while inconclusive, there is high probability that a wire strand was outside the solder cup on the ODU and caused the intermittent short

### Mark Squillante, 2024-01-24

@Marc Richardson is this issue worth tracking for your team?

### Cameron Chapman, 2024-01-24

old info from status field 
I’ve done some investigation about this incident.
The connecting wire (ODU to Solenoid) has no defect and all checks out good.
As far as the solenoid goes, I have two concerns.
The connecting wires are tied to the body of the solenoid by a wire-tie.
There is a small aluminum bracket with sharp corner edges and that cuts into the insulation.
That is a potential candidate for causing short.
The involved solenoids were investigated, but no direct evidence of such short.
The second concern and that might relate to a short is that the solenoid constantly driven from about 12V(three cells)
and that causing close to one Watt of dissipation heating up the winding of it.
For a future improvement, I’m highly recommending using an Economizer to reduce that dissipation.
As of today, I’ve not found any direct evidence or sign of cause of that incident.
Next step would be to investigate the battery, especially the ODU connection.
-
As of today: January 12, 2023 
The battery was located and verified for cell reading. (see attached 200153.png)
At this point, I’m requesting an approval for dismantle the battery and investigate deeper the cause of the anomality of such reading.
-

### Mark Squillante, 2024-01-24

Investigation report located here: https://jenaero.sharepoint.com/:p:/r/sites/EngineeringTeam/Shared%20Documents/Investigations/LM%20Overheating%20HLB,%20Solenoid%20Test%20Cable/Investigation%20Report.pptx?d=we459024344324156a2002c4b2d016671&csf=1&web=1&e=YFmdVN

### Laszlo Juhasz, 2024-01-30

Additionally, to the previous findings it’s very important to mention that the ODU connector hosting the wires from the battery cells installed in a tilted position and that results the wires being pressed to the inner wall of the enclosure bottom shell. The wires from that ODU connector are pressing that wall in such way it can be felt from the outside just touching that area. See attached image (Tilted ODU Assembly).

### Greg Fryer, 2024-02-28

@Mark Squillante To get this one closed out, I made some minor edits to the report. I separated the two CAs into an “Immediate” and a “Long Term/Future Development”. We won’t track the Long Term as part of the incident, just log it (done) and go forth. So the only action remaining is to meet with Electronics/Quality and verify that the procedures/inspections in place now would prevent this issue.
(If somehow not, then we’ll need to work on an improvement there.)
Edit: Advanced to Verifying Corrective Actions, since we do believe they are complete.

### Mark Squillante, 2024-02-29

@Matt Philley we determined the root cause was an intermittent short on the 16-pin ODU connector at the solder cups. Likely a wire strand was making intermittent contact with an adjacent pin. This battery was built before inspection would have caught this. Can you verify that the current process would catch this issue?

### Matt Philley, 2024-03-01

@Mark Squillante @Greg Fryer 
This 16-pin ODU is part of the 114-105901 Battery Heater Charge Cable. 
The current process involves Production soldering the inner ring, then submitting it for inspection, then soldering outer ring, then submitting to inspection again. Inspection is inspecting to “IPC/WHMA-A-620C, JAN 2017, Sec. 4.8.6.1”. This process has been in place since ~July 2023. Snapshots of procedure, traveler, and inspection sheet below. Additionally, these cables are also functionally tested as part of the traveler with a test procedure. 
SLO is no longer manufacturing this harness, but HSV should be building to the same process and inspection. 
@Sloan Payne can you verify if HSV is following the same procedure, traveler, inspection, etc. during the inspection of this harness and if there was a solder issue we should be able to detect it? I can talk you through the background of this issue before you respond if you would like. 

If there were a solder issue then the current process should detect it during this visual inspection and associated cable tester check. 

Traveler originally released ~6/21/23 (moved to peer review and available in vault on this date. Actual release not till Aug 2023)
[embedded file]
[embedded file]

Procedure originally released ~ 6/21/23 (moved to peer review and available in vault on this date. Actual release not till Oct 2023)
[embedded file]
[embedded file]
Inspection Sheet dated Nov 2023
[embedded file]

### Sloan Payne, 2024-03-05

@Matt Philley and @Greg Fryer Huntsville follows the same procedure, traveler, and inspection sheet during the inspection of these cables. We check thoroughly for solder bridges, loose stands, and FOD. One suggestion from my inspection is that a test step be added after potting. We have found that the handling during the breakaway cables being pulled apart could affect wires as well as handling while potting. To ensure these cables are good after potting, it might be good to add an additional test after potting to ensure no wires or joints were damaged during handling.

### Matt Philley, 2024-03-05

@Greg Fryer I think we are good to close this issue since the current process should detect if something like this would happen again. 
@Sloan Payne  sounds like that could be an improvement. I think yall have control over that process now to make that kind of change if desired right?

### Sloan Payne, 2024-03-05

@Matt Philley We do not have authority to change travelers and procedures yet as no Engineer sits in house here so we would need SLO to do this.

### Greg Fryer, 2024-03-05

@Sloan Payne We don’t want you to be waiting for us at all, regardless of where we are. Our biggest limitation is bandwidth, so there are lots of improvements that we aren’t doing because they aren’t actually causing a fire or directed development from “on high”. If there’s something you have the time for amongst a team, we are happy to hear the pitch, let you know if there’s design reasons not to do it, and if that works out, sign off at the end.
(Also still trying to carve out time and refresh our HSV Eng Lead posting, speaking of no bandwidth.)

### Sloan Payne, 2024-03-05

@Greg Fryer I understand. Just was explaining as to why we cannot update the vault items currently.

### Douglas Baker, 2024-01-16

@Laszlo Juhasz @Cameron Chapman I have sent a follow up to LM requesting permission to dismantle the battery.   This is the second attempt.  I will continue to follow up.

### Douglas Baker, 2024-01-16

@Pat Wells @Cameron Chapman @Laszlo Juhasz  We have approval to dismantle the battery.
From Subject Received Size Categories
trevor.w.lee@lmco.com RE: QA finding 2:08 PM 109 KB

### Laszlo Juhasz, 2024-01-16

@Douglas Baker Awesome. Thank you, I’m proceeding with the dismantle.

### Laszlo Juhasz, 2024-01-17

A brief update, the battery was dismantled, and the investigation is in progress.

### Cameron Chapman, 2024-01-21

@Mark Squillante, Laszlo will be out for a while. Are you available to investigate this tomorrow? 
Here were the next steps we planned. 
- Inspect battery and adapter harnesses for shorts. We suspect there may be a short on the unused pins of the adapter harness. Laszlo received a harness from Ben to test that,
- Create investigation report and attach photos of PCB damage, damaged pins, etc. List what pin number shows damage and what signal that corresponds to.
- Inspect for other items that could have caused the PCB damage.

Thank you

### Mark Squillante, 2024-01-22

Looks like the ODU pins 8 and 9 are shorted together, which would short out cell 2. Battery pack itself appears to have no shorts and ~540mV was measured across cell 2. I would likely have to cut the wires from the ODU to the 8 pin DF13 to determine which side has the short.
Here are pictures of battery control board and DF13 mating connectors for P5 and P6.
[embedded file]
[embedded file]
[embedded file]

### Mark Squillante, 2024-01-22

I tested the solenoid test cable using the cable tester and no shorts were found.
I tried to separate the 8 pin DF13 connector from its mate and they were melted together. I ended up breaking both sides of the connector but the short is now gone, so it looks like the short was in the DF13.
[embedded file]
[embedded file]
[embedded file]

### Mark Squillante, 2024-01-23

I did a more aggressive wiggle test this morning and found no shorts between pins 8 and 9 on the ODU. These are unused pins and the connector is pretty well potted, so it is likely this is not the root cause. 
[embedded file]
[embedded file]

### Mark Squillante, 2024-01-23

I was able to replicate the short by slightly wiggling the wires just behind the 16 pin ODU on the battery. Short is intermittent but very easy to recreate with a small amount of wire wiggling.

### Mark Squillante, 2024-01-23

I removed most of the potting on the ODU connector. The gray and violet wires were the shorted connection but unfortunately it seems I removed the short when removing the potting. Here are pictures before and after removing the potting. 
[embedded file]
[embedded file]
[embedded file]
[embedded file]
[embedded file]

### Mark Squillante, 2024-01-23

I asked @Thomas McMillan to look at the battery and he said that while inconclusive, there is high probability that a wire strand was outside the solder cup on the ODU and caused the intermittent short

### Mark Squillante, 2024-01-24

@Marc Richardson is this issue worth tracking for your team?

### Cameron Chapman, 2024-01-24

old info from status field 
I’ve done some investigation about this incident.
The connecting wire (ODU to Solenoid) has no defect and all checks out good.
As far as the solenoid goes, I have two concerns.
The connecting wires are tied to the body of the solenoid by a wire-tie.
There is a small aluminum bracket with sharp corner edges and that cuts into the insulation.
That is a potential candidate for causing short.
The involved solenoids were investigated, but no direct evidence of such short.
The second concern and that might relate to a short is that the solenoid constantly driven from about 12V(three cells)
and that causing close to one Watt of dissipation heating up the winding of it.
For a future improvement, I’m highly recommending using an Economizer to reduce that dissipation.
As of today, I’ve not found any direct evidence or sign of cause of that incident.
Next step would be to investigate the battery, especially the ODU connection.
-
As of today: January 12, 2023 
The battery was located and verified for cell reading. (see attached 200153.png)
At this point, I’m requesting an approval for dismantle the battery and investigate deeper the cause of the anomality of such reading.
-

### Mark Squillante, 2024-01-24

Investigation report located here: https://jenaero.sharepoint.com/:p:/r/sites/EngineeringTeam/Shared%20Documents/Investigations/LM%20Overheating%20HLB,%20Solenoid%20Test%20Cable/Investigation%20Report.pptx?d=we459024344324156a2002c4b2d016671&csf=1&web=1&e=YFmdVN

### Laszlo Juhasz, 2024-01-30

Additionally, to the previous findings it’s very important to mention that the ODU connector hosting the wires from the battery cells installed in a tilted position and that results the wires being pressed to the inner wall of the enclosure bottom shell. The wires from that ODU connector are pressing that wall in such way it can be felt from the outside just touching that area. See attached image (Tilted ODU Assembly).

### Greg Fryer, 2024-02-28

@Mark Squillante To get this one closed out, I made some minor edits to the report. I separated the two CAs into an “Immediate” and a “Long Term/Future Development”. We won’t track the Long Term as part of the incident, just log it (done) and go forth. So the only action remaining is to meet with Electronics/Quality and verify that the procedures/inspections in place now would prevent this issue.
(If somehow not, then we’ll need to work on an improvement there.)
Edit: Advanced to Verifying Corrective Actions, since we do believe they are complete.

### Mark Squillante, 2024-02-29

@Matt Philley we determined the root cause was an intermittent short on the 16-pin ODU connector at the solder cups. Likely a wire strand was making intermittent contact with an adjacent pin. This battery was built before inspection would have caught this. Can you verify that the current process would catch this issue?

### Matt Philley, 2024-03-01

@Mark Squillante @Greg Fryer 
This 16-pin ODU is part of the 114-105901 Battery Heater Charge Cable. 
The current process involves Production soldering the inner ring, then submitting it for inspection, then soldering outer ring, then submitting to inspection again. Inspection is inspecting to “IPC/WHMA-A-620C, JAN 2017, Sec. 4.8.6.1”. This process has been in place since ~July 2023. Snapshots of procedure, traveler, and inspection sheet below. Additionally, these cables are also functionally tested as part of the traveler with a test procedure. 
SLO is no longer manufacturing this harness, but HSV should be building to the same process and inspection. 
@Sloan Payne can you verify if HSV is following the same procedure, traveler, inspection, etc. during the inspection of this harness and if there was a solder issue we should be able to detect it? I can talk you through the background of this issue before you respond if you would like. 

If there were a solder issue then the current process should detect it during this visual inspection and associated cable tester check. 

Traveler originally released ~6/21/23 (moved to peer review and available in vault on this date. Actual release not till Aug 2023)
[embedded file]
[embedded file]

Procedure originally released ~ 6/21/23 (moved to peer review and available in vault on this date. Actual release not till Oct 2023)
[embedded file]
[embedded file]
Inspection Sheet dated Nov 2023
[embedded file]

### Sloan Payne, 2024-03-05

@Matt Philley and @Greg Fryer Huntsville follows the same procedure, traveler, and inspection sheet during the inspection of these cables. We check thoroughly for solder bridges, loose stands, and FOD. One suggestion from my inspection is that a test step be added after potting. We have found that the handling during the breakaway cables being pulled apart could affect wires as well as handling while potting. To ensure these cables are good after potting, it might be good to add an additional test after potting to ensure no wires or joints were damaged during handling.

### Matt Philley, 2024-03-05

@Greg Fryer I think we are good to close this issue since the current process should detect if something like this would happen again. 
@Sloan Payne  sounds like that could be an improvement. I think yall have control over that process now to make that kind of change if desired right?

### Sloan Payne, 2024-03-05

@Matt Philley We do not have authority to change travelers and procedures yet as no Engineer sits in house here so we would need SLO to do this.

### Greg Fryer, 2024-03-05

@Sloan Payne We don’t want you to be waiting for us at all, regardless of where we are. Our biggest limitation is bandwidth, so there are lots of improvements that we aren’t doing because they aren’t actually causing a fire or directed development from “on high”. If there’s something you have the time for amongst a team, we are happy to hear the pitch, let you know if there’s design reasons not to do it, and if that works out, sign off at the end.
(Also still trying to carve out time and refresh our HSV Eng Lead posting, speaking of no bandwidth.)

### Sloan Payne, 2024-03-05

@Greg Fryer I understand. Just was explaining as to why we cannot update the vault items currently.

## Attachments (30)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [107-103807 SOLENOID TEST CABLE, PINOUT.xlsx](attachments/18019_107-103807%20SOLENOID%20TEST%20CABLE,%20PINOUT.xlsx.md) | xlsx | 2570 | 2023-12-22 | converted |
| [FCS1000-ACC-805_REV B.PDF](attachments/18024_FCS1000-ACC-805_REV%20B.PDF.md) | pdf | 130 | 2023-12-22 | converted |
| [FCS1000-ACC-807_REV B.PDF](attachments/18025_FCS1000-ACC-807_REV%20B.PDF.md) | pdf | 100 | 2023-12-22 | converted |
| [FW 2-1619 .msg](attachments/18021_FW%202-1619%20.msg.md) | msg | 136 | 2023-12-22 | converted |
| Test Config.PNG | image | 52 | 2023-12-22 | listed only |
| [WIR0248_REV E.PDF](attachments/18026_WIR0248_REV%20E.PDF.md) | pdf | 166 | 2023-12-22 | converted |
| image-20231222-151149.png | image | 588 | 2023-12-22 | listed only |
| image-20231222-151156.png | image | 658 | 2023-12-22 | listed only |
| image-20231226-041207.png | image | 79 | 2023-12-25 | listed only |
| Screenshot_2024-01-05_180940.jpg | image | 474 | 2024-01-12 | listed only |
| image-20240112-200153.png | image | 760 | 2024-01-12 | listed only |
| IMG_0002.jpg | image | 6906 | 2024-01-22 | listed only |
| IMG_0003.jpg | image | 6918 | 2024-01-22 | listed only |
| IMG_0004.jpg | image | 6952 | 2024-01-22 | listed only |
| IMG_0594.jpg | image | 7555 | 2024-01-22 | listed only |
| IMG_0595.jpg | image | 7107 | 2024-01-22 | listed only |
| IMG_0596.jpg | image | 6723 | 2024-01-22 | listed only |
| IMG_0599.jpg | image | 9004 | 2024-01-23 | listed only |
| IMG_0600.jpg | image | 7133 | 2024-01-23 | listed only |
| IMG_0601.jpg | image | 7131 | 2024-01-23 | listed only |
| IMG_20240123_095300794.jpg | image | 1907 | 2024-01-23 | listed only |
| IMG_20240123_095310666.jpg | image | 404 | 2024-01-23 | listed only |
| IMG_20240123_105035559_HDR.jpg | image | 793 | 2024-01-23 | listed only |
| IMG_20240123_105116604_HDR.jpg | image | 697 | 2024-01-23 | listed only |
| Tilted ODU Connector.jpg | image | 1462 | 2024-01-30 | listed only |
| image-20240301-153109.png | image | 73 | 2024-03-01 | listed only |
| image-20240301-153146.png | image | 201 | 2024-03-01 | listed only |
| image-20240301-153157.png | image | 394 | 2024-03-01 | listed only |
| image-20240301-154136.png | image | 110 | 2024-03-01 | listed only |
| image-20240301-154327.png | image | 25 | 2024-03-01 | listed only |
