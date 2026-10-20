# VXEP-40: SMA Connector Torque Wrench Issue (Koaxis Vehicle Ant Cable Change)

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2022-03-25
- **Updated:** 2023-12-07
- **Resolved:** 2023-12-07
- **Reporter:** Former user
- **Assignee:** Greg Fryer
- **Creator:** Former user
- **Labels:** 8-28-Sprint, EE-Intern, Production
- **Links:** relates to ENG-1690 (No drawing for Cables from Koaxis); split to ENG-2117 (New latest revision of Fuselage RF cable drawing); relates to VA-81 (100-106271-Approve alternate vendor for SMA Male to TNC Male RA Cable (Koaxis AM10-KF141-TM20-24.00)); relates to ENG-2322 (Finalize and release RF Cable Testing Procedure 110-112764); is blocked by VA-416 (Identify correct SMA torque wrench for stainless-to-brass and brass-to-brass SMA connector mates. ); relates to VA-448 (100-101545 - SGCS2 Coax Cables No Drawing or Test Report Requirements); relates to VA-508 (Koaxis RF Cables replace 106-103824 106-103823 with 100-114532 100-114534 ); relates to VA-509 (Alternate vendor for RF cables)
- **Sprint:** VXE-2 ME Sprint Team 8-28
- **Part Number(s):** 106-103823, 106-103824
- **Production Stakeholder:** Ryan Ferguson
- **Supply Chain Stakeholder:** Victor Vandor
- **Other Stakeholder (as required):** Matt Philley
- **Severity:** 4 - Annoyance

## Description

6/1/23 Update: 
The comments morphed this ticket from the original NCR project related to the SMA connectors busting loose to the project to switch suppliers from Pasternack to Koaxis. This will now be revived to continue the project of moving to the improved Koaxis cables.

Originally announced via NCR-220208-136.  Moved here for engineering tracking.  NCR will stay open.
- Final assembly had a couple of vehicle SMA connections break on them.  Hans completed an investigation and got in touch with Pasternack and they informed us that we were over-torquing the connection.
- We currently use/supply a Pasternack click type torque wrench set to 8in-lbs.  Prior to this we used/supplied a German brand click type torque wrench also set to 8 in-lbs (since the dawn of time).
- The SMA connector on the vehicle antenna cable has a datasheet that calls out 3-5in-lbs.


Part Numbers:
106-103823 - COTS, UHF ANTENNA CABLE, LONG
106-103824 - COTS, UHF ANTENNA CABLE, SHORT

Estimated time time 8hours to revise drawing to look like mod payload drawing and coordinate with Koaxis.

## Comments (42)

### Cameron Chapman, 2022-03-25

Here are the SMA connections in the aircraft (same for XE25 and VXE30). Looking into GCS, Mod Payload, and other equipment now.
| Cable JAI PN | Location | Vendor PN | Description | Mfr | Connector 1 | Connector 1 torque value in-lbs | Connector 2 | Connector 2 torque value in-lbs |
| 106-103824 | Fuselage. Silvus to Antenna | PE3C0754/HS-11 | SMA Male Right Angle to SMA Male Straight Cable, LMR-100 Coax, 11 inches | Pasternack | PE4003 | 3-5 | PE4009. | 3-5 |
| 106-103823 | " | PE3C0754/HS-31 | SMA Male Right Angle to SMA Male Straight Cable, LMR-100 Coax, 31 inches | Pasternack | " | “ | " | “ |
| None? | 2x In Silvus box | PE3C3937-3.7 | SMA Female Bulkhead to Push-On SMP Female Right Angle Cable Using LMR-100 Coax | " | SMA Jack | NA | SMP Plug | NA |

### Cameron Chapman, 2022-03-25

Found an additional SMA connector in SGCS-3. 
|  | SGCS-3 | PE3C1491 | SMA Male to TNC Male Right Angle Cable Using LMR-240-UF Coax |  | PE44637 | 3-5 in lbs | PE44635 | NA TNC plug |  |

### Cameron Chapman, 2022-03-25

All aircraft SMA plug connections (and 1 GCS) should be listed below and all require 3-5 in-lbs. @Kyle England @Mark Frank , please list any other SMA plug connections you see or know of in any equipment (ground or flight).

### Former user, 2022-04-06

Per MRB meeting:  
- 8in-lb torque wrenches will be put back into service. (Hans)
- We will add an inspection/test to pasternack cables prior to shipment.  More details to come on this. (Hans/Matt)
- A specification will be created for replacement cables that meet 8in-lb spec.  These cables will need to be tested prior to putting them in service. (Cameron)
- Service bulletin will be generated to notify the customer. (Hans)

### Matt Philley, 2022-04-18

Initial Containment Inspection has been Completed as of 4/18/22. A physical identifier is on the bins in Inventory to flag any future orders to be inspected as well.
4/18 MP - Qty 9 of PN 106-103823 (long) were rejected out of Qty 35 tested in Inventory and the Right-angle connector failed to meet torque requirement. These are removed from Inventory and moved to NCR Cage. All Qty 4 of PN 100-106271 were acceptable in Inventory.
4/12 MP - Qty 11 of PN 106-103824 (Short) were rejected out of Qty 35 from Inventory and the Right-angle connector failed to meet torque requirement. These are removed from Inventory and moved to NCR Cage.

### Engineering Monitor, 2022-09-20

Coaxis cables received.  Need to coordinate ground range test and then flight test.

### Matt Philley, 2023-05-31

@Marc Richardson NCR references added

### Greg Fryer, 2023-06-01

@Cameron Chapman These are getting moved into the First Article process and could use attention. The work required to finish that is unclear. Can you please define here, and see if it’s something that can be completed in someone’s discretionary time?

### Cameron Chapman, 2023-06-01

Need to coordinate ground range test and then flight test before approving. @Matt Philley do you have any updates for urgency vs other projects, failure rate, etc. 

@Hayden Jeanor or @Maxime Jeanneau , are you available to work on this?
Here is what I was thinking for testing last year.

Questions and answers from Carson
- What do we do for current tests? Does it work. Check SNR ~65 received signal ~25 in shop. Has 1 and 2 antenna.
- Test signal strength over long distance in high bay. Same positions. And orientation. Spin around 45 deg and see if it changes.
- Test at various points over the frequency range.
- Repeat during flight test (single frequency or both ends in two flights). Guessing we don’t want to switch mid flight.
- Other tests recommended? Vibration?

### Matt Philley, 2023-06-01

@Cameron Chapman Not terribly urgent, but we just had a recent batch of cables that failed (linked NCRs) and the Inventory sweep caught additional ones.
It looks like we will need to place another order from Pasternack to keep up with rate, which sparked the convo about wanting to finish the project and move to the improved cables when we can.
So… not terribly urgent, but would be better to move to the new cables sometime in the next month or two in order to avoid putting more money and inspection into Pasternack we know are not what we want. 
I updated the title to be more accurate with what this ticket morphed into.

### Hayden Jeanor, 2023-06-02

Will coordinate with @Maxime Jeanneau on Monday. He's more familiar with with silvus radio functionality, and im more familiar with testing requirements of RF cabling.

### Matt Philley, 2023-06-02

@Hayden Jeanor @Maxime Jeanneau not sure if its been communicated with, but the Koaxis cables are physically sitting on the “First Article” rack in Inspection with a red tag and note on them regarding this effort.

### Matt Philley, 2023-06-20

Added reference to a new NCR 1164 where Carson found a defect internal to the wire that appears to be a manufacturing defect where they apply their part marking label causing a short when pressure is applied
@Desiray Johnston FYI

### Matt Philley, 2023-06-20

@Maxime Jeanneau @Nina Menon I also recommend yall touch base on these cables to perform a test installation with Kyle E. I think we made a length adjustment or two so we wanna make sure we are all on the same page with routing.

### Greg Fryer, 2023-06-20

@Maxime Jeanneau Desiray asked me what the plan is to get this implemented, as cables are in-house. Can you please update if there are any steps remaining? (Note, I’m assuming you and Cameron have you working on this currently - if not, please put it On Hold so everyone knows it’s not being worked on.)

### Matt Philley, 2023-06-21

@Maxime Jeanneau based on the cause of the shorted cables from Pasternack (NCR 1164 linked above) I think it would be worth pulling the jacket off a cable or two to inspect the condition of the core and dielectric insulator especially around any heat shrink labels.

### Maxime Jeanneau, 2023-06-22

@Laszlo Juhasz @Hayden Jeanor and I have figured out how to test the cables for RF loss and reflections which Pasternack does and ships us the quality information. We plan on documenting a test procedure and qualifying the first article Koaxis cables. 
In the future we’d like Koaxis to test the cables prior to shipping and ship with test documentation like Pasternack (the first articles do not have test documentation). If Koaxis is unable to test the cables to our specification, we could design a test procedure similar to the antenna test procedure for Quality to evaluate cables. 
@Noah Richardson started a new SolidWorks drawing to capture the short and long cable for Koaxis, and we’ll add the electrical specifications once determined, this would be released as a revision to the current EA part number.

### Matt Philley, 2023-06-26

@Nina Menon @Kyle England can yall please coordinate with @Maxime Jeanneau to install a set of the Koaxis cables into a fuselage? Maxime has brought up the point that these cables do have a minimum bend radius requirement and can be damaged during install. Maxime has the cables with him. 
Purpose of the test assembly is to checkout the following things:
- Verify the lengths of the cables makes sense for final routing and assembly process
- Check if the installation process requires any concerning wire bending, twisting, pinching, etc.
- Verify the final routing as we have defined does not violate any bend radius requirements
- Note any other observations from Maxime based on his current knowledge of these cables that may become follow-on opportunities for improvement (hopefully nothing alarming)

@Desiray Johnston FYSA

### Maxime Jeanneau, 2023-06-26

From the new cable’s specifications, a minimum bend radius of .25'' must be maintained to prevent permanent damage to the cable.

### Maxime Jeanneau, 2023-06-28

Test install occurred yesterday 6/27, both cables fit nicely and conformed to the minimum bend radius. Fit nicer than the pasternack cables due to no use of heat shrink (especially on the back of the SMA connectors).

### Maxime Jeanneau, 2023-06-28

Current Koaxis order did not come with testing printed out in the box, reached out to KOAXIS but no luck. 
We are screening 3 of each cable in engineering and going to gather data on RF loss and reflections compared to Pasternack. This procedure is getting documented for future use by QA, decision should be made whether we want to test a sample or test all cables in new KOAXIS order. @Matt Philley

### Cameron Chapman, 2023-06-30

@Maxime Jeanneau it seems like these cables meet RF requirements. Here is what I recommend for mechanical verification. 
- Install on engineering asset. Compare signal strength with another aircraft during ground testing (aircraft and antennas in the same location).
- Flight test engineering asset. Monitor signal strength during flight and compare to normal. 
- Ok to approve for production after this.
- Leave Koaxis cables in engineering asset. This way, if an issue arose, we would hopefully find it before customers.
- Things that would help, but are not required.
- Vibration testing of cables/connectors. One of the interns could maybe do this.
- Koaxis reporting if any other aircraft use these connectors. Bonus points for being manned or large vibration environments (helicopter).

### Cameron Chapman, 2023-07-11

Pasting from duplicate ticket.
@Maxime Jeanneau I think this is a GCS cable. Would you like to track in this ticket or separate? 

@Cameron Chapman 100-106271 does not appear to be addressed in https://jenaero.atlassian.net/browse/ENG-1847. Should I open a separate ticket for it? Vault does not show an approved KOAXIS part number but that’s what is currently in inventory:
[embedded: image-20230710-164719.png]
@Matt Philley FYI

### Matt Philley, 2023-07-11

@Cameron Chapman PN 100-106271 are called out on the following assemblies:
96X-3-14-5410 SGCS3 Kit
107-106385-1 TCI and Consumables Kit 1
107-103277 VXE30 Spares Package

### Matt Philley, 2023-07-11

I just pulled Qty 50 of PN 100-106271 from Koaxis from Inventory since they are not yet approved, missing test reports, and lack part marking.
I will send a notification email to Purchasing and Production since we only have Qty 10 left in Inventory now.

### Maxime Jeanneau, 2023-07-13

We’ll track the GCS RF cables as a separate ticket see: [ENG-2062] 100-106271-Approve alternate vendor for SMA Male to TNC Male RA Cable (Koaxis AM10-KF141-TM20-24.00) - Jira (atlassian.net)

### Maxime Jeanneau, 2023-07-13

Flight testing with new Koaxis cables on installed on the 491 SCO asset aircraft was successful today. I collected a data set comparing 491 with no payload, 491 with payload, and 528 (production aircraft with Pasternack still installed). Results show performance was indistinguishable between pasternack and Koaxis therefore moving forward with production.

Find data and summary here: Engineering Team - RF Cable Testing - All Documents (sharepoint.com)

### Maxime Jeanneau, 2023-07-13

Conclusion : Engineering approves Koaxis vendor for: 
106-103823 - COTS, UHF ANTENNA CABLE, LONG
106-103824 - COTS, UHF ANTENNA CABLE, SHORT

### Matt Philley, 2023-07-14

Copied from email this morning:
The test requirements and requirement for a printed report should be specified on the drawing for Supply Chain to communicate the requirement to the vendor and for QA to know to check for the test report upon receipt. It looks like there are draft drawings for these cables, but not released ones.
 
The existing JIRA (https://jenaero.atlassian.net/browse/ENG-1847 ) should either be converted to an Engineering Change or a new Engineering Change should be created so we can track the new release through the CCB process, then we can include the sub-tasks for things like communicating to the vendor, production cut-in, etc.
 
@Desiray Johnston We can explore using the Koaxis cables on deviation until those tasks are resolved, but we have a couple months worth of Pasternack cables in Inventory I would rather focus on implementing these in properly and not on cutting corners to start installing them if we can avoid it. This is a good CCB topic though.

### Matt Philley, 2023-07-24

@Greg Fryer @Cameron Chapman I brought this up in CCB, but Maxime gave the new Koaxis cables the thumbs-up for the aircraft, but now we need actual drawings for these cables.
The MOD Payload RF Cables are a good example to use. https://jenaero.atlassian.net/browse/ENG-1643

### Cameron Chapman, 2023-07-24

Sounds good. Would a drawings from Koaxis suffice?

### Matt Philley, 2023-07-24

@Cameron Chapman we could probably use that to get by assuming it has whatever test requirements we have on it. That isnt consistent with elsewhere though so not ideal long term.

### Maxime Jeanneau, 2023-07-24

Worked with @Noah Richardson and @Scott Stuckey to create and release a solidworks drawing to capture the koaxis test requirements. We released these in the vault today: 
106-103823-B
106-103824-B
Should be ready to order using the new drawings

### Cameron Chapman, 2023-07-24

Thank you everyone. @Maxime Jeanneau please either change this problem to engineering change and process into CCB, or link engineering change to implement those documents.

### Cameron Chapman, 2023-07-25

@Maxime Jeanneau moving back in in process. Please see comment below. It should be CCBd before closing. Also fill out fields like resolution description, stakeholders, etc.

### Maxime Jeanneau, 2023-08-23

See https://jenaero.atlassian.net/browse/ENG-2117 for CCB ticket

### Cameron Chapman, 2023-08-24

Linking subtasks to parent

### Maxime Jeanneau, 2023-09-01

A 5in/lb option we already have in the shop: Fixed Break-Over Torque Wrench With 5/16 Bit For SMA Connectors Pre-set to 5 in-lbs (pasternack.com) (Vendor Part Number: PE5019-19A). Expensive though, ~$300

### Maxime Jeanneau, 2023-09-05

Alternative to Pasternack, not yet in house: SMA Fixed Torque Wrench in Click Type 5/16 inch Bit that is Pre-set to 5 in-lbs (fairviewmicrowave.com)

### Maxime Jeanneau, 2023-09-15

@Wesley Lilienthal This ticket covers change to the fuselage RF cables from pasternack to koaxis. Last step is to rev the fuselage drawing with the new part numbers to close ticket captured by [VA-508] Update Higher Level Drawings for Part number change for Long and Short Koaxis Cables - Jira (atlassian.net) which @Nadia Brown could help with. (Drawing needs to be brought up to current standards and re-released with modification)

### Nadia Brown, 2023-09-25

@Maxime Jeanneau Has this been addressed yet and is my assistance still required for the higher level drawing update?

### Greg Fryer, 2023-12-07

I’m calling this one done, we can create a separate problem on any outstanding RF related items. And be more specific with the actions.

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [SMA Cable Lengths - 22.04.26.pdf](attachments/14895_SMA%20Cable%20Lengths%20-%2022.04.26.pdf.md) | pdf | 990 | 2023-05-26 | converted |
| [SMA Connector MRB Meeting - 22.04.18.pdf](attachments/14896_SMA%20Connector%20MRB%20Meeting%20-%2022.04.18.pdf.md) | pdf | 1531 | 2023-05-26 | converted |
| [Antenna Cable Mfg Defect Investigation - June 2023.pdf](attachments/15134_Antenna%20Cable%20Mfg%20Defect%20Investigation%20-%20June%202023.pdf.md) | pdf | 728 | 2023-06-21 | converted |
| [1-12 Photos Trials.docx](attachments/15376_1-12%20Photos%20Trials.docx.md) | docx | 9003 | 2023-07-07 | converted |
| [Trial Data 6-29-23.xlsx](attachments/15375_Trial%20Data%206-29-23.xlsx.md) | xlsx | 30 | 2023-07-07 | converted |
| image-20230710-164719.png | image | 37 | 2023-07-11 | listed only |
