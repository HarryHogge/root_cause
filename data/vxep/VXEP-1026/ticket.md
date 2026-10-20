# VXEP-1026: 107-104091 VXE30 VTOL HIL Flight Simulator Box updates

- **Issue type:** Engineering Change
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-07-09
- **Updated:** 2025-02-14
- **Resolved:** 2024-10-23
- **Reporter:** Emalee Johnson
- **Assignee:** Trevor Gronner
- **Creator:** Emalee Johnson
- **Labels:** Electronics_Drafting
- **Parent:** VA-1935 HIL Box Updates 
- **Links:** relates to VA-2397 (BOM Change: 107-107735 GPS Board)
- **Epic Link:** VA-1935
- **Target start:** 2024-07-09
- **Production Stakeholder:** Desiray Johnston
- **Other Stakeholder (as required):** Ben Hansen

## Description

- Replace tough seal 23 (100-102225) on 107-104091 VXE30 VTOL HIL Flight Simulator Box. [CAD] [Drawing]
- Replace item 4 (107-102077-1) and item 14 (1807P01C) with VTOL GPS Assembly 107-107735 [CAD] [Drawing]
- Remove item 28 (107-103101), item 5 (107-102078) already captures that board in the assembly. [CAD]  [Drawing]

TS is used to bond the ADP cable collar (107-102798) to the HIL box, production recommends using the same replacement implemented for the center wing, DP 604NS (100-111583)

## Comments (18)

### Emalee Johnson, 2024-07-09

@Cameron Chapman @Trevor Gronner @Desiray Johnston

### Cameron Chapman, 2024-07-09

DP 604NS (100-111583) is approved. Please report if it bonds well after curing. If it does, please assign to @Gerrit Sperling to update the drawing. @Emalee Johnson

### Emalee Johnson, 2024-07-10

Kit list is updated to show DP604NS and the link to the Jira ticket is on there as well. 
@Ben Hansen I think this will be part of the HIL box that you are working on so when you get to this part of the build please provide feedback.

### Emalee Johnson, 2024-07-25

@Cameron Chapman I have a couple more drawing updates for 107-104091, do you want me to add it to this ticket or create a separate one for each issue? 
Also Dan completed this build today and said that the DP604NS worked just fine as a replacement for TS so that's good news! Mark also supported with a brief inspection to make sure it all looked good based on the previous HIL boxes he has built.

### Cameron Chapman, 2024-07-25

@Emalee Johnson 1 issue per PN release sounds good (so you could change the title of this to say  107-104091 VXE30 VTOL HIL Flight Simulator Box updates. If they were released at separate times, they should be different tasks. 
Please assign to Gerrit to update once problems are listed

### Emalee Johnson, 2024-07-25

@Cameron Chapman  Thanks for the feedback, this ticket is updated. @Gerrit Sperling  Assigning to you, please let me know if you have any questions.

### Gerrit Sperling, 2024-07-31

107-104091 is now in Engineering Change Request state on the vault. @Cameron Chapman do you have permissions to push through to ME EDIT so I can begin these changes?

[embedded: image-20240731-173821.png]
Here is the file state workflow, I just dont have permissions to push out of ECR or into production release.

### Cameron Chapman, 2024-07-31

@Gerrit Sperling Please check with CM group @David R. Martin II for documentation and training of this process. I do not know/remember who can issue the ECO.

### David R. Martin II, 2024-08-01

@Cameron Chapman Engineering owns the Vault and its release process. The Configuration Management team does not have documentation or training for this process. I do have limited Vault permissions, which fortunately do include transitioning objects from ECR to ME - EDIT. I have done so for 107-104091 assembly and drawing. I do not have permissions to release objects.
@Gerrit Sperling You should be able to work on the objects now.

### Gerrit Sperling, 2024-08-01

@David R. Martin II Thank you for pushing it through. I will be able to get these to CCB now once the changes are made.

### Gerrit Sperling, 2024-08-01

[embedded: REVB DRAFT1 107-104091 XE VTOL HIL Box Assembly.pdf]
@Cameron Chapman @Emalee Johnson Are either of you able to review and approve the changes made here? Then I can push it through.

### Cameron Chapman, 2024-08-01

@Barry Mendez is anyone documenting the changes Scott is making to workflows? I think we should (example, who should perform what functions). 
[embedded: image-20240731-173821 (8fed58c3-1267-4f2a-9d32-9dc861678d29).png]

### Emalee Johnson, 2024-08-01

@Gerrit Sperling  For 107-107735 Can you change the description to VTOL GPS Assembly, I don’t see any other issues with the BOM. It is up to you guys but the actual drawing is missing quite a few features in terms of the harnesses and wire routing but we have done our best to make a work instructions that captures all of those details so up to you guys.

### Gerrit Sperling, 2024-08-01

@Emalee Johnson Updated description. I will have to leave that other decision you mention to @Cameron Chapman. I am fine with it being in a work instruction. I can do the CAD based off of the work instruction but it will take a bit of time.

### Cameron Chapman, 2024-08-01

@Gerrit Sperling approved to change to 107-107735 VTOL GPS Assembly. @Gerrit Sperling are you able to complete this related task in parallel? https://jenaero.atlassian.net/browse/ENG-567

### Gerrit Sperling, 2024-08-02

107-104091 Is ready for CCB release @Greg Fryer @Cameron Chapman @Emalee Johnson

### Barry Mendez, 2024-08-02

@Cameron Chapman - Not that I’m aware of. Would that be a Configuration Management function?

### Greg Fryer, 2024-09-11

Hey @Gerrit Sperling and others, be sure to change things to an Engineering Change when it’s a drawing revision - otherwise there’s no flag to make sure CCB actually sees it. See me sometime and I can show you a couple clicks to do it.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240731-173821.png | image | 43 | 2024-07-31 | listed only |
| [REVB DRAFT1 107-104091 XE VTOL HIL Box Assembly.pdf](attachments/22238_REVB%20DRAFT1%20107-104091%20XE%20VTOL%20HIL%20Box%20Assembly.pdf.md) | pdf | 337 | 2024-08-01 | converted |
| image-20240731-173821 (8fed58c3-1267-4f2a-9d32-9dc861678d29).png | image | 43 | 2024-08-01 | listed only |
