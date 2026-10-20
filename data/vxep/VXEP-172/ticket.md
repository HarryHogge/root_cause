# VXEP-172: Cable Tester Documentation and Training

- **Issue type:** Major Project
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2022-12-07
- **Updated:** 2025-11-17
- **Resolved:** 2025-04-02
- **Reporter:** Cameron Chapman
- **Assignee:** Daniel Ceja
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-169 (Testing gaps for MOD Payload); relates to VA-1812 (Develop Cable Tester Cables and Procedure for MOD Payload Cables); relates to VXEP-1607 (Update cable design process to ensure planning for tooling and cable testers is complete so that they are ready when builds need to happen. )

## Description

Status 3/11/25: 
Transferring to @Daniel Ceja 
Ideas:
- Since these are ground test boards, we could optimize specs and fab house to be much cheaper than aircraft boards.
- A confluence page could be a good way to organize the various documents and related projects for cable tester boards.


Save all (non altium) draft files here: Cable Tester
365 Link: https://jennings-aeronautics-2.365.altium.com/designs/folder-2162CB87-6D0E-4FD4-BFC2-3A867107347D

Main Files
- 124-109215 Cable Tester Assembly, Adapter Harness Template, Pinout.xlsx: Instructions for making test cables.


C:\JAI Vault 1\Projects\124 - Test Equipment\Production\Electronics Shop
C:\JAI Vault 1\Projects\124 - Test Equipment\Electrical Design\PCB
Add location of current test cables. 
\\condor\Production\Cable, Wire, Harness Files\Cable Tester
See subtasks for remaining actions after the engineering to production handoff.

## Plan

7/24/24 
New proposed process. 
We think that making a new adapter PCB for each new cable designed will be the best process going forward. The harness designer is in charge of coordinating that effort. PCB should arrive before the first production harness builds (ideally before any). 
Project to make this happen:
- Clean up this project by updating or closing tasks no longer in the plan.
- Establish template for adapter PCBs. Coordinate and review with production.
- Produce example PCB (could be for MAGNSS cables or a future design effort).
- Ben N and electronics are ok auto learning and correcting once they have cables or PCBs.


Older
- FInd/make generic instructions for how to get from this cable needs testing to selecting or building test cables.
- Find or make a test cable inventory.
- Make block diagrams for how specific cables are tested. Start with visio document in sharepoint .

## Comments (14)

### Cameron Chapman, 2022-12-07

@Garrett O'Neill , can you please provide answers or recommendations to the questions listed in the description? Ok to leave blank if you don’t know. We can then call a meeting with appropriate stakeholders to outline and assign the tasks. 
FYI @Greg Fryer @Ryan Ferguson @Lawton Ziedses Des Plantes

### Garrett O'Neill, 2022-12-07

@Cameron Chapman @Greg Fryer @Ryan Ferguson @Lawton Ziedses Des Plantes 
- How can we best document the process so that inexperienced users can run tests? Need to document the following and determine who will create each of these documents: We have a work-in-progress reference manual on the vault detailing all required knowledge of using the tester (creating projects, running tests, interpreting results, etc.).
- Using a cable PN to test, how does someone find out:
- what cables to connect? The plan is to create an excel document, similar to a pinout, detailing what test PCBs, adapter harnesses, etc. are needed to test a given assembly, along with other information such test program name and how to make the connections. The filename follows the convention “Part Number Description, Test Setup”. This way the document will automatically appear along with the drawing, procedure, etc. when searching that assembly’s part number on the vault.
- how to connect them? See 1.a.i.
- what program do they run? See 1.a.i.
- How do they find and run a program, and how can they tell if it passed or failed? See 1.
- How are new programs created? See 1. Who will them? Anyone can create one. Electronics can decide if they want to restrict this to certain people.
- How do people know how to build adapter cables? Build documents for adapter harnesses are already created. The reference manual will have a section giving a quick explanation on how to read them, but it’s a very simple process.
- Process for designing and building for adapter cables needed to test new cable designs (or other equipment (Ex: PCBs)? The test harness design is common across all adapter harnesses. The design follows a template that does not require additional design work for new harnesses. As for testing PCBs, I don’t think the cable tester is a good tool for that.
- How do operators know if a new adapter board is required? Create Jira task for EEs if so. The test setup document (see 1.a.i.) calls out the part number of the required adapter board for a given test. If a test does not exist for a given assembly, they will have to try and create one using a combination of existing adapter PCBs and adapter harnesses. If it is not possible do so with existing harnesses/PCBs, they can either try and create a special adapter harness (easiest solution), or request a new PCB be designed (more time consuming). We already have 2 types of adapter PCBs that should cover ~80% of all harnesses that we currently make. I have preliminary designs for 3 additional boards that will cover the rest and have already stocked up the parts. We can design/order them as time in the schedule allows.
- What is the status of each of these documents? (List doc titles and functions). I can’t link files from the vault, but here are the filenames and functions:
- WK 260 MU Cable Tester, Quick Reference Manual
- Reference manual explained at the top. Summarizes all basic knowledge that is required to use the tester.
- WK 260 MU Cable Tester, Test Setup Template
- Template document for documenting new test setups.
- WK 260 MU Cable Tester, Adapter Harness Kit, Pinout
- Build document for new adapter harnesses. Includes how to give a unique name/label to each harness.
- WK 260 MU Cable Tester, Adapter PCB, Connector List
- This document is used to plan out what connectors will go on different adapter PCBs.
- 107-104993 Fuselage Payload Harness, Test Setup.xlsx
- An example of a test setup that has already been documented and is ready for use.
- WK 260 MU Cable Tester, Hardware Manual
- Extensive hardware manual provided by the manufacturer. Go here if quick reference manual does not have what you’re looking for.

3. Additional questions or suggestions? As discussed with Ben and Lawton, we’ll need to set aside a space to neatly organize the adapter harnesses. It might be easiest to put the cable tester on its own bench and use the shelf above it for storing harnesses/PCBs. The names of each harness were picked to be easily human readable, so organizing them and then finding the one you need should be very straightforward.

### Cameron Chapman, 2022-12-08

@Garrett O'Neill. Thank you for the information. Please assign these docs PNs. Always helpful to list PNs when referencing documents.
C:\JAI Vault 1\projects\124 - test equipment\production\electronics shop
The proposed documents look good and useful. I think we should schedule a meeting with stakeholders to review the proposed process and collect feedback before spending a lot of time updating the documents. 
Changes for the procedure.
- Add a reference documents section after TOC listing the related documents and descriptions.
- Combine scope sections onto the same page.
- Change old projects slides to test setup excel format and remove from this procedure.
- In testing process, step 1 should detail to open test setup file that matches cable under test PN, and connect according to that document. 
- In this step, reference a section for what to do if a test setup file does not exist (Who to contact, which files to open, how to use them if not obvious. We should meet to determine who will make new ones)
- Project names on the tester should start with the cable PN. PN only may be acceptable.

Changes to test setup
- “Fuselage Payload Harness Connector”

Add a label to the cable tester to reference the ref manual, include manual PN.

### Cameron Chapman, 2022-12-08

Meeting scheduled 12/12 at 3pm.
I think we should meet to discuss the current status of the cable tester, its documentation, planned tasks their assignees. Hopefully we can define the best formats and content for planned documents to help people use the tester. The meeting should be more efficient if is familiar with the existing documents. Please quickly review them before the meeting if you can. You are also welcome to send feedback ahead of the meeting to consider or discuss.
 
C:\JAI Vault 1\projects\124 - test equipment\production\electronics shop
 
Agenda:
- Review existing documentation formats. Discuss any recommended changes to templates.
- Determine which groups and individuals will update which documentation.
- Discuss planned tasks, add those tasks to JIRA, and assign.

### Garrett O'Neill, 2022-12-09

All cable tester documents have been renamed “124-109215 Cable Tester Assembly, <Document Description>”
[embedded: image-20221209-181508.png]

### Cameron Chapman, 2022-12-15

Completed engineering handoff to production meeting.Here are the actions. I created and assigned them as subtasks for this project.  
- Try heat shrink labels. Electronics
- Peg board to organize harnesses using column/row location indicators? Electronics to sort out. -Ryan
- Record custom cables as separate line in adapter harness template. -Ben
- Who will update test procedure documents? Update describing how to use documents. Electronics/Ben
- Document how to order and build ribbon cable. -dwg + BOM + work instruction for not obvious steps-Garrett
- Add to pinout table a column saying how many we have built. -Ben.
- Ben to write helpdesk so prod engineers and techs can access folders like this C:\JAI Vault 1\Projects\124 - Test Equipment\Production\

### Cameron Chapman, 2023-01-03

@Garrett O'Neill , can you please move these PCB files to the vault for each of the boards you created?
\condor\Users\GarrettO\Altium
@Ben Norris , please see those folders and let us know if creating a netlist spreadsheet would be helpful. You are looking for this file 2201P01A Cable Tester, Adapter PCB, JST.PDF

### Garrett O'Neill, 2023-01-04

@Cameron Chapman @Ben Norris Project folders moved to the vault:
C:\JAI Vault 1\Projects\124 - Test Equipment\Electrical Design\PCB

### Greg Fryer, 2023-02-02

@Cameron Chapman Need to see if this is done, going, or what.

### Cameron Chapman, 2023-03-30

@Greg Fryer not done, but handed off to production. Assigning to Ryan, who will be working with Belcan (see attached email).

### Cameron Chapman, 2023-03-30

Hi Folks!
 
Our support from Belcan for the scope of work of Cable Tester Setup and Implementation is finally coming soon! This email is meant to be an overview and I will schedule a sitdown with a smaller crew (or larger if it is requested) on more of the details.
 
Scope:
- Belcan will provide 1 Engineer for the purpose of setup, documentation, and implementation of Cable Tester for Production in the Electronics Shop for the attached Qty 26 cable PN’s for the VXE30 aircraft.

 
Who Involved:
- Ryan F – Production Engineering
- Ben N?? – Production
- TBD?? – Electrical Engineering

 
Paople/Timeline:
- Michael (Chase) Ezell will be onsite for 2 weeks from 4/10 through 4/21

- Additional Belcan folks will be onsite 4/10 & 4/11 to help(?) still figuring this one out

 
Questions to be hashed out in short meeting I will schedule soon:
- Is it OK to borrow Ben N(?) or anyone else from Production who is knowledgeable on Cable Tester for a day or two to get Chase up to speed?

- What do we want to define as “good enough” documentation for cable tester? Excel BOM/Pinout or solidworks/Altium drawings…?

- Procedures should be able to drafted by Chase with help from Sam O and Richard (Elect Documentation Belcan Support)

 
 
 
|  | Matt Philley Production Engineering Supervisor Edge Autonomy – SLO Phone: +1-805-592-1178 Email: mphilley@edgeautonomy.io [embedded: VXE30 Top Level, Harnesses to be Cable Tested - RF 23.03.30.xlsx] |

### Matt Philley, 2023-04-20

Chase from Belcan has draft a few procedures with some troubleshooting documentation in the following folder:
C:\JAI Vault 1\Projects\124 - Test Equipment\Production\Electronics Shop
List of cables we are targeting for Belcan and in-process documentation is located in the following folder
10 - Belcan Cable Tester Documentation

### Christa Meck, 2025-04-01

@Daniel Ceja and/or @Cameron Chapman Does this work from 2022 still need to be completed?

### Daniel Ceja, 2025-04-02

@Christa Meck I believe all of those tickets from 2022 have been completed

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20221209-181508.png | image | 40 | 2022-12-09 | listed only |
| [VXE30 Top Level, Harnesses to be Cable Tested - RF 23.03.30.xlsx](attachments/13354_VXE30%20Top%20Level,%20Harnesses%20to%20be%20Cable%20Tested%20-%20RF%2023.03.30.xlsx.md) | xlsx | 13 | 2023-03-30 | converted |
