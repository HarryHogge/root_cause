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
[embedded: image-20231222-151149.png]
[embedded: image-20231222-151156.png]

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

### Cameron Chapman, 2023-12-21

Tagged up with Kurt and Hayden. They weren't aware of anything obvious that would impact other than some short. Kurt stated further schematic review would be required (did not task him with that).
 
Cody
From: Cody Smisek
Sent: Thursday, December 21, 2023 3:19 PM
To: Tom Westrich <twestrich@edgeautonomy.io>; Sean Wendling <swendling@edgeautonomy.io>
Cc: Cameron Chapman <cchapman@edgeautonomy.io>
Subject: RE: Overheating Battery/Cable (Fuel Cell Support Kit SCO Test Config) - Third Party Proprietary Information
 
Tom
 
Adding Cameron as I don’t know the heated HLB wiring.
 
Yes, installs into the odu that is used for battery charging and opens the solenoid. Constantly powering, so if they left it on for extended period of time (many hours?) then I suppose it could drain the battery. The heater odu is 4 pin and not used for the solenoid tester.
 
Cody Smisek
 
From: Tom Westrich <twestrich@edgeautonomy.io> 
Sent: Thursday, December 21, 2023 2:50 PM
To: Cody Smisek <csmisek@edgeautonomy.io>; Sean Wendling <swendling@edgeautonomy.io>
Subject: Fwd: Overheating Battery/Cable (Fuel Cell Support Kit SCO Test Config) - Third Party Proprietary Information
 
Cody,
 
I have to admit, I am unaware of how the solenoid test cable is used to actuate the valve on the fuel cel propane regulator during regulator calibration. This was something LMCO managed and I was fairly removed.  
 
Where does one install the ODU end of the solenoid test cable?  Into the battery? Or into a different connector?  
 
Thanks,
 
Tom
From: Matt Philley <mphilley@edgeautonomy.io>
Sent: Thursday, December 21, 2023 3:54:24 PM
To: Sam Miller <smiller@edgeautonomy.io>; Greg Fryer <gfryer@edgeautonomy.io>; Steve Adlich <sadlich@edgeautonomy.io>; Drew Cunnien <dcunnien@edgeautonomy.io>; Tom Westrich <twestrich@edgeautonomy.io>
Cc: Marc Richardson <mrichardson@edgeautonomy.io>
Subject: FW: Overheating Battery/Cable (Fuel Cell Support Kit SCO Test Config) - Third Party Proprietary Information
 
Fuel Cell Type Engineering Peeps!
 
We have an odd situation and not sure how to proceed or who would be the technical focal to help investigate.
 
Lockheed Source Inspection was performing a checkout of the Regulator Calibration Test Assembly inside a Fuel Cell Support Kit and we had a Hybrid Lift Battery that was used for testing overheat which appears to have killed the battery.
 
We are unsure if the issue may have been with the test setup, perhaps with a test component (i.e. a bad solenoid with a short) or if there is some issue running this test using a modern Heated Hybrid Lift Battery or if this test should only be run with a legacy “non-heated” hybrid lift battery.
 
 
Who in our company is familiar with this test and can help with some troubleshooting?
 
 
<image001.png>
 
<image002.png>
 
 
 
| <image003.png> | Matt Philley Quality Engineer Edge Autonomy – SLO Phone: +1-805-592-1178 Email: mphilley@edgeautonomy.io |

 
 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
 
From: jun.1.park@lmco.com <jun.1.park@lmco.com> 
Sent: Thursday, December 21, 2023 11:50 AM
To: Matt Philley <mphilley@edgeautonomy.io>; Ben Norris <bnorris@edgeautonomy.io>
Cc: Marc Richardson <mrichardson@edgeautonomy.io>; Hartsell, Jeff (US) <jeff.hartsell@lmco.com>; jose.g.sandoval@lmco.com; doulan.j.reis@lmco.com; matthew.curran@lmco.com
Subject: Overheating Battery/Cable (Fuel Cell Support Kit SCO Test Config) - Third Party Proprietary Information
 
Third Party Proprietary Information
 
Hi Matt, Ben,
 
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

### Cameron Chapman, 2023-12-21

Hi Matt,
We build that adapter cable in SLO. I created this incident to track the issue. We can follow up there. I wasn’t on the original email. Can you please attach those files to a reply or in the JIRA incident?
 
A standard heated HLB wiring is the same pinout as the original HLB without heaters. The new connections are on a different connector.
 
Can we test the equipment involved tomorrow? Based on the description, I am guessing it was a fault in one of the involved parts or the wrong solenoid PN was used (Ex: a 5V solenoid would pull too much current with a 12V input).

### Matt Philley, 2023-12-22

Copied from Email chain:

@Cameron Chapman I don’t believe we make that cable in SLO. There are no procedures, inspection sheets, kit lists, inventory location, etc. Perhaps we did at one time but it does not look like we have lately…? I will check with Eshop. It looks like the BOM we have in vault has not been updated since 2020.
 
The equipment involved is with LM in their cage and I am not sure if they will be here today or not. They will also be on vacation until Jan 2 so if troubleshooting is needed can I get a point of contact and either Myself or Steve S will help coordinate that with LM.
 
 
@Tom Westrich does AA have a drawing package for these components? That would help if it turns out one of these components has a problem. And can yall confirm if AA is making or purchasing this cable that goes into the Fuel Cell Support Kits?
- Regulator and Solenoid Assy (PN FCS1000-ACC-805)
- VXE30 Solenoid Test Cable (PN FCS1000-ACC-807)

### Ben Norris, 2023-12-22

@Cameron Chapman This test cable routes through the heater control board since it center taps from the ground pin to the 3rd cell which goes from the charge cable through the heater board to the sense cable to the battery taps instead of the original design which was just the charge odu to the battery taps.

### Matt Philley, 2023-12-22

AA confirmed they have been making the cable.
AA drawings attached from Tom W

### Matt Philley, 2023-12-22

@Steve Stack FYSA

### Cameron Chapman, 2023-12-25

@Ben Norris good point. The voltages are the same as before, but it does connect through the PCB.  The current to the solenoid is low (8mA), but the issue could be due to a fault on the PCB, unexpected interaction with the solenoid, harness, or solenoid issue.  We will see when we can test the equipment. 
[embedded: image-20231226-041207.png]

### Matt Philley, 2024-01-03

FYI folks LM is asking for status on this investigation. I have deferred to Program Management to workout priority with Engineering. 
Steve A and Doug B for the TIQUILA program.

### Matt Philley, 2024-01-04

(Duplicate from email chain)
I worked with Jeff to pull back Fuel Cell Support Kit FCS1043 & FCS1056 which were involved in the failure. They are now red tagged with NCR# AA-20 in the RMA area. Let me know who will be involved in the investigation and I can show them where its at.
 
HLB 2-1619 which was damaged during the testing is in the LM Battery cabinet also in the RMA area.

### Cameron Chapman, 2024-01-04

Tracking investigation here. @Laszlo Juhasz can you please investigate this tomorrow? Please ensure testing is not destructive. See attached for adapter harness pinout. 
FYI @Douglas Baker @Matt Philley @Pat Wells

### Laszlo Juhasz, 2024-01-04

@Cameron Chapman Yes, I’ll investigate first in the morning. keeping in mind not to destroy anything during the  test.

### Matt Philley, 2024-01-05

@Laszlo Juhasz let me know if you need any help locating the equipment

### Pat Wells, 2024-01-11

@Cameron Chapman @Laszlo Juhasz do we have a good path forward to continue investigating this or do we need to pass off to Ann Arbor team?  LM is pressing hard for status of investigation.
@Douglas Baker

### Tom Westrich, 2024-01-12

From Laszlo on 1/11/24:

Hi,
 
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
 
Best,
 
|  | Laszlo Juhasz Electrical Engineer III Edge Autonomy – SLO (formerly Jennings Aeronautics) Mobile: +1 720-244-6291 Email: ljuhasz@edgeautonomy.io |

### Tom Westrich, 2024-01-12

@Laszlo Juhasz , it sounds like your analysis showed the Solenoid Test Cable (WIR0248) to have the correct pinout, and that the Solenoid used had no short (although potential room for improvement in future designs).  Is this correct?
@Matt Philley, based on Laszlo’s work, it sounds like we can release the FCSKs from this issue and focus future root cause investigation on the HLB. @Cameron Chapman , do you agree?

### Matt Philley, 2024-01-12

@Tom Westrich We can clear the FCSK, but LM will need a root cause and clear direction about this testing procedure before they resume source inspection and testing of this product. 
We are also a bit sensitive here in SLO about battery overheating due to the fire we had… so I would not want them performing this test again either until we can definitely say why that battery overheated and that the test as written is safe to perform. 
The battery involved is still in the LM Battery cage in the RMA area next to the LM Cage, so that is available to test.

### Cameron Chapman, 2024-01-12

I agree with @Matt Philley . We should identify the cause (hopefully today) before proceeding. @Laszlo Juhasz will prioritize today. @Tom Westrich can you please create a linked tasks to evaluate Laszlo’s recommendations, then paste the links in the corrective action field. 
@Laszlo Juhasz please update investigation status and plan as you proceed. 
FYI @Mark Squillante @Garrett O'Neill

### Sean Odell, 2024-01-12

HLB (2-1619) involved in this investigation is now with @Laszlo Juhasz in engineering to continue investigation. No longer in RMA area.
@Cameron Chapman @Pat Wells @Greg Fryer FYSA

### Cameron Chapman, 2024-01-12

@Douglas Baker we have identified an issue with the battery, but it may have been caused by transients from the solenoid actuation. We will know better when we open the battery. Can you please request permission from LM to open up the battery for further inspection? We will likely have to provide a replacement. 
[embedded: image-20240112-200153.png]
@Tom Westrich , do you perform functional testing of these harnesses and solenoids with a battery in AA?
Do we have any history of how many of these harnesses we have shipped and tested (or that LM has tested) since we added the BMS?
FYI @Laszlo Juhasz 
@Pat Wells in regards to “LM is pressing hard for status of investigation.” LM is also pressing hard for the AGNSS development, and we are internally pushing hard for xkit. Adding more EE resources would directly delay one of those other efforts, but Laszlo and Mark are working this issue.

### Laszlo Juhasz, 2024-01-16

@Douglas Baker @Sean Odell @Matt Philley @Cameron Chapman Good morning, just a “Monday” morning reminder. - Continuing the investigation, we’ll need the permission to dismantle the battery. Thank you.

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
[embedded: IMG_0004.jpg]
[embedded: IMG_0002.jpg]
[embedded: IMG_0003.jpg]

### Mark Squillante, 2024-01-22

I tested the solenoid test cable using the cable tester and no shorts were found.
I tried to separate the 8 pin DF13 connector from its mate and they were melted together. I ended up breaking both sides of the connector but the short is now gone, so it looks like the short was in the DF13.
[embedded: IMG_0595.jpg]
[embedded: IMG_0594.jpg]
[embedded: IMG_0596.jpg]

### Mark Squillante, 2024-01-23

I did a more aggressive wiggle test this morning and found no shorts between pins 8 and 9 on the ODU. These are unused pins and the connector is pretty well potted, so it is likely this is not the root cause. 
[embedded: IMG_20240123_095310666.jpg]
[embedded: IMG_20240123_095300794.jpg]

### Mark Squillante, 2024-01-23

I was able to replicate the short by slightly wiggling the wires just behind the 16 pin ODU on the battery. Short is intermittent but very easy to recreate with a small amount of wire wiggling.

### Mark Squillante, 2024-01-23

I removed most of the potting on the ODU connector. The gray and violet wires were the shorted connection but unfortunately it seems I removed the short when removing the potting. Here are pictures before and after removing the potting. 
[embedded: IMG_0599.jpg]
[embedded: IMG_0600.jpg]
[embedded: IMG_20240123_105116604_HDR.jpg]
[embedded: IMG_20240123_105035559_HDR.jpg]
[embedded: IMG_0601.jpg]

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
[embedded: image-20240301-153109.png]
[embedded: image-20240301-154327.png]

Procedure originally released ~ 6/21/23 (moved to peer review and available in vault on this date. Actual release not till Oct 2023)
[embedded: image-20240301-153146.png]
[embedded: image-20240301-153157.png]
Inspection Sheet dated Nov 2023
[embedded: image-20240301-154136.png]

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
