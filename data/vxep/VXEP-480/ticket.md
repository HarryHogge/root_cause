# VXEP-480: Create Master Document for Quality: IPC-A-610, IPC-A-620 Conformances and Engineering Deferrals/ Deviations

- **Issue type:** Major Project
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2023-07-05
- **Updated:** 2025-05-21
- **Resolved:** 2025-05-21
- **Reporter:** Connor Peebles
- **Assignee:** Cameron Chapman
- **Creator:** Connor Peebles
- **Labels:** IPC-Deviation, Production
- **Links:** is caused by ENG-1623 (26g and 28g C-Grid Connectors and Crimps Do Not Conform to IPC); is caused by ENG-1803 (DF13 Contacts - Insulation tabs are piercing PTFE insulation); is caused by ENG-1808 (Using heat shrink on top of wire insulation in crimp contacts (JST contacts)); relates to VA-34 (VXE 509 - Connection to vehicle lost while idle on the ground); relates to ENG-2350 (Determine and document electronics IPC and other requirements we will use for assembly and inspection.  ); relates to VXEP-68 (Evaluate standardizing soldering iron temperatures and other build processes. ); relates to TQT-3 (IPC 610 Clarification); is duplicated by VA-492 (VXE450 Implement CA: Quality to create inspection document per Eng input.); is blocked by VA-641 (Outline steps, assignees, and hours to create QA inspection document. ); is caused by VXEP-51 (Internal - Aircraft 450 VTOL Landing Crash - ESC soft start)
- **Production Stakeholder:** Matt Philley

## Description

As suggested by Thomas McMillan :

Problem statement: 
We have recently been adding inspection criteria to PCBA drawings, specifying IPC-A-610 Class 2 among others. However, when inspectors look at older assembly drawings they are mainly using tribal knowledge to fill in for the lack of inspection criteria listed on the drawings, or creating NCRs and Jiras to call out a disposition.
Solution: 
Create a Master Document that details inspection criteria of electrical assemblies to default to if there is no appropriate inspection criteria on the assembly drawing.
This would also include engineering deferrals of known deviations from our class of IPC, some examples of which are in the Caused By related Jira tickets here.

Please add comments here for further deferrals we should add to this master document (tribal knowledge that we have been passing through inspection)
(@ relevant people here, once approved, to accumulate these tribal knowledge points)

Draft Document Link: WI-910-003 General Electronics Inspection Requirements.docx
Things to add:
- Standard solder temps and techniques.

## Comments (11)

### Connor Peebles, 2023-07-05

@Cameron Chapman @Greg Fryer Let me know what you think of this minor project and if approved.
FYI @Matt Philley for QA say

### Cameron Chapman, 2023-07-07

Approved, but this seems like a document and process production or quality could manage, rather than engineering. Engineering would just provide the initial guidance and approve deviations. 
I suggest you discuss with them before starting.

### Matt Philley, 2023-07-10

@Cameron Chapman @Connor Peebles  WI-910-003 General Electronics Inspection Requirements has been drafted and is meant to help fill this gap to provide more clear written direction for inspectors. I have been working on it slowly with the Inspection team. Now that I am back in the office I am hoping to get the first draft ready for review in the next week or so. I am not familiar with PCB stuff so thats where I kinda stalled before I left on PTO.

### Connor Peebles, 2023-07-10

@Matt Philley Great! Feel free to ask us anything when you get there. 
Will that include engineering deferrals from IPC? Such as could resolve these linked issues? 
Will cancel this task.

### Matt Philley, 2023-07-10

@Connor Peebles not totally sure yet… I have some open sections to add notes that could be used for that. Keep everything open for now though until I can get my feet back under me and we can touch base.

### Matt Philley, 2023-07-11

@Brad Crampton @Marc Richardson @Catherine Wagner FYSA

### Catherine Wagner, 2023-09-22

IPC Deviation/Deferral: 
IPC-A-610H, Sect. 5.2.17, states “Inclusions that penetrate or project from the solder fillet” are a Defect for Class 1, 2, 3.
Engineering Guidance is that “solder inclusions pass per IPC-A-610 8.3.5.4: If the solder filet and surface is still equal to or greater than 75% the length of the lead.” REF NCR 1347

### Connor Peebles, 2023-09-26

@Greg Fryer These could go into production improvements backlog:
- plus here is a semi-duplicate created as a result of AC509 debacle [ENG-2350] Determine and document electronics IPC and other requirements we will use for assembly and inspection. - Jira (atlassian.net)

### Connor Peebles, 2023-12-05

@Liam Limon

### Liam Limon, 2023-12-06

@Connor Peebles We’ve been approaching this by writing specs for the termination type and then defining the applicable IPC Class 2 standards using language and pictures that defines a Target, Acceptable, and Unacceptable criteria. This can then be referenced on every drawing that uses that type of termination.

### Catherine Wagner, 2024-01-08

@Thomas McMillan noted that 96X-3-09-0002 current crimp process is defective per IPC-620. May need review for deviation. REF: JOSE C

## Attachments (0)
