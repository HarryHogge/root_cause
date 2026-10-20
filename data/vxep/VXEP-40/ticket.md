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

### Cameron Chapman, 2023-07-11

Pasting from duplicate ticket.
@Maxime Jeanneau I think this is a GCS cable. Would you like to track in this ticket or separate? 

@Cameron Chapman 100-106271 does not appear to be addressed in https://jenaero.atlassian.net/browse/ENG-1847. Should I open a separate ticket for it? Vault does not show an approved KOAXIS part number but that’s what is currently in inventory:
[embedded file]
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
[embedded file]
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
