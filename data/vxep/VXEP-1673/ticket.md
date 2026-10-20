# VXEP-1673: Build and document EE ironbirds

- **Issue type:** Major Project
- **Status:** In Process
- **Priority:** Medium
- **Created:** 2023-09-02
- **Updated:** 2026-07-09
- **Reporter:** Cameron Chapman
- **Assignee:** Matthew Aguirre
- **Creator:** Cameron Chapman
- **Links:** relates to ENG-2210 (Build an IronBird for Engineering); relates to VXEP-1669 (Build and Document Ironbirds for UAP )
- **Other Stakeholder (as required):** John Gober

## Description

Sharepoint: Iron birds and HILs

Planned structure to reorganize info into
- https://jenaero.atlassian.net/browse/VXEP-1673
- B40 improvements
- B30 improvements
- B40 and UAP IBs are linked to this project, but stay in UAP project.   https://jenaero.atlassian.net/browse/VXEP-1669
- HSV Ironbird(s)

Add this to visio drawings for B40 BK precision 1685B 1-60VDC 5A


- Organize relevant files into this folder and parent folders (unless a better one exists, then link here) B40 UAP Iron Bird (Better one linked below, created by adrian)
- Relevant Files: Iron Bird
- Move this file to parent folder if latest Engineering Ironbird - BOM & inventory list.xlsx
- Review Jira issues linked to this and in search related to ironbirds.
- https://jenaero.atlassian.net/browse/ENGINF-377
- https://jenaero.atlassian.net/browse/ENGINF-12
- Organize into remaining projects.
- Close and merge duplicates
- Move files to one locations.
- Find Adrian scrapped/spare parts BOM if around. If not make one to start inventorying parts we could use for IBs. 
- Talk to RMA and electronics/quality and see what they do with NFF parts. Document that process and ask if engineering could be consulted before scrapping.
- Sort engineering cabinets.
- Update dispo for what we should keep.
- Want to troubleshoot in the future.
- Update dispos and scraps.
- 





Old, need to update/merge
Build and document  engineering ironbirds. 
- VXE30 config. 
- 1 baseline, not changed.
- 1 for testing changes.
- 1 for HSV
- Current Havoc config
- GSE. Whatever equipment we can duplicate from NFF parts from GCS1-3.

Helpful Ironbird Documents. \\CONDOR\Production\Procedures\VXE30
Relevant files/sharepoint folder: Iron Bird 

Need to organize inventory list. These files are relevant. 
- Engineering Ironbird - BOM & inventory list.xlsx

## Plan

- Resolve peer review items. Ironbird review   (Web view)

TODO:
- Cutouts for all components
- create 2D stencils?
- labels for all assys
- System for only one person using the IB at a time
- Single user Status sign 
- sign where someone can put their name down that they are using it
- only be used when its “available”, otherwise hunt down the person using it
- signage/instructions
- configuration management
- Red tags/labeling to identify history of each component
- add network switch
- add “avionics transponder test cable” - iron bird has one: allows for ethernet from transponder port

## Issue Status

status update 3/8: 
Fuselage box is completed but needs to be tested. Centering box needs a few more components to be complete then is read to test but have not been able to work on it. 
Build one more Iron Bird for VXE 30 and Havoc 
Checklist built for VXE 30 Iron Bird: IRON BIRD CHECKLIST.xlsx
Currently asking around for scrap parts 

(6/11) due to last working day will be reassigning to @Matthew Aguirre upon request

## Comments (17)

### Connor Peebles, 2023-09-05

@Madeleine Masiello Please add hours to ‘time tracking’, that have already been worked and continue doing so (like once a day if spending multiple hours a day)

### Connor Peebles, 2023-09-06

@Madeleine Masiello  Please put these on a pink inventory request form from inventory. We’ll talk to Kyle D. before submitting it
- QTY 1 107-104993 - Fuselage Payload Harness
- QTY 1 1911P01A - Ground Iso Board
- QTY 1 2002P01A - CCA, Magnetometer
- QTY 4 107-101850 - Pegasus Servos

### Madeleine Masiello, 2023-09-06

@Connor Peebles I made the pink slip. Ready to talk to Kyle whenever.

### Cameron Chapman, 2023-09-13

Let me know who would like to take this on. Could be a good training project for @Wesley Lilienthal to start. @Adrian Garcia @Jeremy Kostel 
@Connor Peebles or @Maxime Jeanneau do you have a recommendation?

### Wesley Lilienthal, 2023-09-22

@Cameron Chapman Per discussion with @Connor Peebles, forgoing in favor of tasks included in the current sprint. Please advise if I should pick this up.

### Connor Peebles, 2024-01-12

assigning to @Adrian Garcia for when he has spare time

### Cameron Chapman, 2024-05-28

@Adrian Garcia this seems to duplicate https://jenaero.atlassian.net/browse/ENG-2210 . Can you please consolidate the latest info then close one of them? Can you please create a tracker for parts and tasks complete vs remaining, then link it in the JIRA description?

### Cameron Chapman, 2024-05-28

@Adrian Garcia 
Please list specific steps in the plan field. Ex: 
- Ready for basic functional test. Need support to verify.
- I need to build the LED indicators and find the motor/esc for the center wing
- Havoc status (I think this would be better as a separate linked task for Havoc). I think it would be easier to list via a linked excel sheet. That way you could list all parts required and the status of each

### Cameron Chapman, 2024-05-29

@Cyrus Blevins

### Cyrus Blevins, 2024-06-06

@Cameron Chapman ESD Mat came in and is set up, with the completion of the foam cutouts (for all the parts currently plugged in) the VXE30 Iron Bird should be fully ready for anybody to test on/use. Everybody is free to move around the setup as they see fit.

### Cameron Chapman, 2024-06-06

Thanks @Cyrus Blevins . Does the mat have a wrist strap connection point? Is the mat connected to ground? 
Next step is build and document the xkit version

### Cyrus Blevins, 2024-06-06

@Cameron Chapman I just followed the instructions on confluence, but it would definitely be worth a quick check from whoever passes by it next

### Cameron Chapman, 2024-06-07

@Cyrus Blevins sounds good. Please have any EE peer review it.

### Adrian Garcia, 2024-07-18

@Cameron Chapman @Jeremy Kostel @Giovanni Gonzalez @Cyrus Blevins Workbenches for both VXE30 and Havoc have been ordered and will approximately ship 7/25. They probably will not come until after I am back from PTO 
[embedded: image-20240718-161922.png]

### Hayden Jeanor, 2024-09-09

@Adrian Garcia see updated TODO

### Christa Meck, 2025-09-02

@Adrian Garcia @Cameron Chapman
This one’s been hanging around a while and some of the Sub Tasks have been In Progress for over a year.  Are we past this now that we’re on the 40 or is some of this work still valid?

### Cameron Chapman, 2026-07-09

@Christa Meck still valid

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240718-161922.png | image | 99 | 2024-07-18 | listed only |
