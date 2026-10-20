# VXEP-301: GCS Power Adapters and Kit with No ENG requirement

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2024-01-09
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Catherine Wagner
- **Creator:** Catherine Wagner
- **Issue color:** purple
- **Part Number(s):** 96X-3-09-0011, 1803C03A, 1302C22A, 1803C02A, 1302C21A, 96X-3-10-1002, 96X-3-10-1003
- **Production Stakeholder:** Emalee Johnson
- **Other Stakeholder (as required):** Brad Crampton

## Description

Kit PN: 
SGCS1
- 96X-3-09-0011 LIND DELL 7414-7424 DC POWER ADAPTER, AS150 INPUT CABLE


SGCS2
96x-3-14-1511
- GCS Power Adapter XE25 Battery - 1803C03A
- GCS Power Adapter Cigarette Lighter - 1302C22A
- GCS Power Adapter 24V Battery - 1803C02A
- GCS Power Adapter Alligator Clips - 1302C21A
- GCS POE Adapter, Dell - 96X-3-10-1002
- GCS POE AC Power Adapter - 96X-3-10-1003

No ENG drawing or requirements besides BOM. Production and inspection requirements are driven by procedure which includes measurements not defined by engineering, such as terminal depth. ENG requirements should determine build process / procedure.
REF 1803C03A Procedure REV A
[embedded file]

## Plan

- https://jenaero.atlassian.net/browse/VXEP-326  @Liam Limon can you or a production engineer start this?
- Create https://jenaero.atlassian.net/browse/VXEP-328 . 
- It is likely better to create a separate document to list this tolerance and reference it in documents, so if it ever changes, we can update in one location vs many. @Gerrit Sperling are you able to coordinate this? Please create a separate linked task for it.
- Indicate which GCS version (1-3) each of the following are in. Prioritize 1803C03A
- Add them to the GCS visio diagrams Travis created if applicable, or create another one for Misc GSE/spares kits, etc. See subtask

## Comments (22)

### Matt Philley, 2024-03-18

@Catherine Wagner @Brad Crampton FYSA pin depth requirement on 1803C03A was taken from the drawing of 107-102189. The Fuse Power Harness 107-102189-1 uses the same AS150 connector and calls out a pin depth requirement on the drawing (which is where that snapshot was taken from).
I recommend we continue the pin depth check since that was tied to a much larger Aircraft Incident Investigation where we started requiring pin depth checks for all our custom machined connectors (AS150, EC3, and EC5) since that was previously not well controlled and led to concern about connector mating, however we should put a note in the Inspection Sheet pointing to a Jira ticket like this one to eventually define it more appropriately. 

Example of older investigation about connector pin depth… which led to us defining pin depth and inspecting for it:
https://jenaero.atlassian.net/browse/VIT2-28

### Greg Fryer, 2024-03-18

@Catherine Wagner Go with what @Matt Philley said, we have several places (especially in the ground equipment) where the design control was put directly into the work instructions. It is not ideal/correct, but it is what we have for now, until we can get enough labor free to work the TDP.
@Cameron Chapman Assigned this to you, but likely on hold until we have someone free to work on drawings.

### Cameron Chapman, 2024-03-18

@Catherine Wagner @Catherine Wagner @Brad Crampton @Thomas McMillan while not ideal and drawings would be better, these procedures were generated and reviewed by engineering when initially released. They procedures engineering controlled at the time, but I agree, they are no longer. 
I also recommend we continue with the pin depth requirement to ensure the anti-spark works correctly. 
Placing this on hold until we have drafting bandwidth to create relevant drawings.

### Catherine Wagner, 2024-03-18

@Cameron Chapman @Greg Fryer Current procedure no longer includes depth requirement.
@Brad Crampton Please update inspection sheet with note referencing this Jira. My team will use it for inspection until design control is implemented. FYA @Thomas McMillan @Luis A jacinto @Sam Omiotek @Emalee Johnson 

[embedded file]

### Sam Omiotek, 2024-03-19

@Emalee Johnson @Matt Philley I removed the drawing snapshot when I revised this procedure two months ago, though I cannot remember exactly why. I added it back in with a note to verify the pin depth before sending it to inspection.
[embedded file]

### Liam Limon, 2024-04-05

@Emalee Johnson @Catherine Wagner @Cameron Chapman This ticket has been revived due to the inspection call for 1803C03A rejecting 9 out of 10 AS150 connectors for the depth being OOT with the dimensions provided in the procedure. Previously our check was always to ensure that the connector was fully bottomed out in the threads and not remaining proud. With this most recent batch, the rejection is due to the pins being set too deep into the housing. In order to meet the requirement, the pin would have to be installed to a position where it spins freely. In order to set the pin to the appropriate depth we would either need to employ loctite on the threads and allow it to cure before sending it to quality to ensure that the depth of the wire didn’t change, or there could also be the possibility that the threads were machined too deep on this batch of connectors, and we need to have them all inspected for the thread depth. 
Currently we have a shortage for the 1803C03A parts so we will be needing a resolution ASAP that will satisfy quality to get these parts moving. Could we re-visit removing the depth requirement from this part since it is not being implemented in the other parts that are included in this Jira ticket? For example, 96x-3-09-0011 doesn’t have a depth requirement called out on the AS150 Connector.

### Cameron Chapman, 2024-04-08

@Ryan West Jimenez can you please do the following.
- Indicate which GCS version (1-3) each of the following are in. Prioritize 1803C03A
- Add them to the GCS visio diagrams Travis created if applicable, or create another one for Misc GSE/spares kits, etc.
- Add PNs to the visio diagrams and save to the vault.
- We can review each to see if the anti-spark features are required or not.
- May review the tolerance on these connectors and/or reject some of them due to the housings being out of tolerance.

Everyone else, please let us know if you have any useful information that could help with this. 
FYI @Sam Omiotek @Catherine Wagner @Liam Limon

### Cameron Chapman, 2024-04-08

@Ryan West Jimenez these documents may be helpful. 
- Search SGCS1 on the vault. Repeat for 2-3. Look for BOMs.
- I asked Travis for the current visio diagram. Will let you know,.
- SGCS Documentation Burndown.xlsx

### Cameron Chapman, 2024-04-08

@Liam Limon replying to your comment below. Unless there has a documented reason confirming the antispark feature is not required for these assemblies (inrush limiting circuitry, transient measurement, etc.) any instance of this connector should have the pin tolerance included in its design documentation and build to meet that. 
In this case, I recommend:
- https://jenaero.atlassian.net/browse/VXEP-326  @Liam Limon can you or a production engineer start this? I reco
- Create https://jenaero.atlassian.net/browse/VXEP-328 . 
- It is likely better to create a separate document to list this tolerance and reference it in documents, so if it ever changes, we can update in one location vs many. @Gerrit Sperling are you able to coordinate this? Please create a separate linked task for it.

### Emalee Johnson, 2024-04-08

@Cameron Chapman
https://jenaero.atlassian.net/browse/VA-587 I think this answers your most recent comment about the antispark feature in the GCS assemblies, “not generating enough power to be a risk”. 
@Liam Limon and I looked into your request for why the pin depths are out of spec and from what we can tell, there is a tolerance issue with the hole depth in the threaded section and the face of the connector. At the top end of the .750” length tolerance for the connector length (.755”) and the top end of the .26” hole depth callout (.27”); .755”+.27” = 1.025” the pin is .90” so the difference between the face of the connector housing and the top of the pin could be up to .125” with the max for that depth tolerance being .115”.   
I would also like to note the Anti-Spark contact measurement is from our internal drawing for (100-102571), which is a reference dimension, I was unable to locate a vendor drawing for this part.

### Cameron Chapman, 2024-04-09

@Emalee Johnson thanks for linking. There is a difference between plating issues (current capacity) and anti-spark functionality (affects transient voltages and inrush current, which can damage electronics). 
The original dimension is from 107-102189 and the XE25 drawing before that. It should not be a reference dimension anywhere. That can be fixed. 
The best way to qualify if these connectors are ok in this application would be to:
- Evaluate the connector dimensions to ensure with worst case stackup when mating the connector, the negative contact always makes contact before the positive contact passes the antispark region. 
- If not, Measure inrush current and transient voltages for each of these applications.

### Emalee Johnson, 2024-04-09

@Cameron Chapman Sorry! I was hoping you had already looked into it during the original anti-spark investigation and that is all that I found for the GCS assemblies. Will you have your team look into the anti-spark functionality requirements?
I think maybe my explanation was confusing so let me add some drawing snapshots. 
The reference dimension I am referring to is for the antispark pin (100-102571), please see the snapshot of the drawing. I used this reference dimension to identify the tolerance issue.
[embedded image-20240409-162921.png]
I used the highlighted dimensions at their max tolerance as shown in the drawing snapshot below: 
[embedded image-20240409-163447.png]
To determine that the tolerance on the other drawing, 107-102189, is not always attainable. .755” + .27” = 1.025” - .90” = .125” which is greater then the max tolerance of .115.
[embedded image-20240409-164138.png]
Please let me know if you have any questions. I think this answers https://jenaero.atlassian.net/browse/VXEP-326 But as far as determining a work around that will have to come from engineering since that will likely be under a deviation. @Greg Fryer @Liam Limon @Catherine Wagner @Kelly J Furlong FYI

### Catherine Wagner, 2024-04-09

@Emalee Johnson @Cameron Chapman The vendor specification is included in the inspection sheet. I do not see a tolerance but it’s not aligned with the drawing reference dimension at 23.70mm (.933 in).
[embedded image-20240409-174358.png]

### Ben Norris, 2024-04-10

From looking into this I think I have found a workaround until proper Design Engineering Drawings can be drafted up. It seems like the two critical dimensions for placement inside the housing are the closest distance from the face of the connector housing and the face of the pins (because if the pins are too close or even worse proud to the connector face then they could potentially short to the female terminals in the wrong orientation.) The second measurement being the difference between the faces of the two pins (because if the negative pin is lower than .1in from the top of the positive pin then the antispark feature will be negated.) So we just need to add to the procedure and inspection sheets for all GCS assemblies with this housing, a callout for more than 0.085 in gap from the face of the housing and no more than .100 in difference in height between the pins. And we can leave the 0.115 in measurement in as reference if desired. This would be implemented by production engineering and quality with approval from design engineering until design engineering has sufficient bandwidth to draft proper drawings which can apply this deviation from the callout for the Fuse Power Harness which has different power requirements compared to the adapters included in the GCS into the GCS adapters. @Emalee Johnson @Cameron Chapman @Catherine Wagner @Matt Philley @Brad Crampton

### Cameron Chapman, 2024-04-11

Thank you @Ben Norris great analysis. Are you or production engineering able to mark up a drawing with the recommended changes? That would expedite our availability to review and update the drawings.

### Brad Crampton, 2024-04-11

@Cameron Chapman  @Ben Norris Attached is the proposed inspection sheet for 96X-3-09-0011. It shows the proposed pin depth requirements for the AS150 terminals. @Sam Omiotek The procedure and traveler will need to be modified and I have left some notes on your desk we may need to discuss.

### Liam Limon, 2024-04-12

@Cameron Chapman @Brad Crampton Inspection Call - center wing (sharepoint.com) Another build that is waiting for an update to this depth requirement that is being held up in quality.

### Cameron Chapman, 2024-04-14

@Brad Crampton @Liam Limon the inspection sheet brad attached looks good. Approved on my end.

### Emalee Johnson, 2024-08-16

Hot NCR related to this same pin depth issue. 107-102189-1/-2 Issues related to potting and Pin Depth
These power harnesses are an active shortage for Pre-MAGNSS @Cameron Chapman @Garrett O'Neill 
FYI @Kelly J Furlong

### Cameron Chapman, 2024-08-19

Reopening this. It should not be closed until the fields above are updated (plan should be complete, status should say what was done). Assigning to Gary now that Ryan left.

### Emalee Johnson, 2024-08-16

Hot NCR related to this same pin depth issue. 107-102189-1/-2 Issues related to potting and Pin Depth
These power harnesses are an active shortage for Pre-MAGNSS @Cameron Chapman @Garrett O'Neill 
FYI @Kelly J Furlong

### Cameron Chapman, 2024-08-19

Reopening this. It should not be closed until the fields above are updated (plan should be complete, status should say what was done). Assigning to Gary now that Ryan left.

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240109-184044.png | image | 267 | 2024-01-09 | listed only |
| image-20240318-204447.png | image | 410 | 2024-03-18 | listed only |
| image-20240319-164416.png | image | 843 | 2024-03-19 | listed only |
| image-20240409-162921.png | image | 5 | 2024-04-09 | listed only |
| image-20240409-163447.png | image | 52 | 2024-04-09 | listed only |
| image-20240409-164138.png | image | 22 | 2024-04-09 | listed only |
| image-20240409-174358.png | image | 382 | 2024-04-09 | listed only |
| [96X-3-09-0011 Lind Dell 7414-7424 DC Power Adapter, AS150 Input Cable Inspection Sheet.xlsx](attachments/20004_96X-3-09-0011%20Lind%20Dell%207414-7424%20DC%20Power%20Adapter,%20AS150%20Input%20Cable%20Inspection%20Sheet.xlsx.md) | xlsx | 433 | 2024-04-11 | converted |
