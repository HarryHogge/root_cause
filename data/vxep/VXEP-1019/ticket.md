# VXEP-1019: 107-102084 drawing clarification

- **Issue type:** Improvement
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-05-23
- **Updated:** 2025-06-13
- **Resolved:** 2025-06-13
- **Reporter:** Catherine Wagner
- **Assignee:** Catherine Wagner
- **Creator:** Catherine Wagner
- **Labels:** Electronics_Drafting
- **Links:** relates to ENG-3338 (107-102084 drawing clarification); relates to ENG-3394 (ECN - 107-102084 drawing clarification)
- **Sprint:** EE Drafting
- **Part Number(s):** 107-102084
- **Other Stakeholder (as required):** Brad Crampton

## Description

REF DWG 107-102084, REV B:
[embedded: image-20240523-200221.png]
RE: Highlighted dimensions 2.5”, 2.5”, and 4” - what to measure and where is not clear. Dimensions are not in procedure and do not align with wire cut length. Please review and update if inspection required.

## Comments (25)

### Catherine Wagner, 2024-05-23

FYA @Jingle Pina @Carrie Wentzel @Thomas McMillan @Luis A jacinto @Steve Stack @Brad Crampton

### Brad Crampton, 2024-05-23

There are no tolerances on this drawing so it cannot be inspected.

### Trevor Gronner, 2024-06-20

@Gary Angelus This task was approved as part of the sprint allocation meeting under the Production Support section. Please feel free to reach out to me if you have any questions or need any help.
@Catherine Wagner FYSA

### Gary Angelus, 2024-06-20

updated drawing for review.
Need lengths to fill in the missing dimensions, “?”.
[embedded: 107-102084-B1.pdf]

### Gary Angelus, 2024-06-20

Hi Trevor,
I posted the PDF on Jira, also attached a copy.
I have 3 dimensions I need someone to provide to me, can you provide or perhaps tell me who I need to see.
Thanks,
Gary

### Gary Angelus, 2024-06-21

[embedded: 107-102084-B1 (1512d2ea-54ed-4024-b594-7f7b043eeb17).pdf]
@Trevor Gronner @Catherine Wagner @Cameron Chapman revised drawing for review.

### Catherine Wagner, 2024-06-21

@Thomas McMillan Would you mind reviewing please?

### Thomas McMillan, 2024-06-21

@Catherine Wagner that looks good to me!  I don’t have an assembly to look at to make sure the new listed dimensions will work.  Would it be worthwhile to “inspect” a few completed assemblies in inventory to make sure the 1.10”, 1.40”, and 2.5” dimensions will work with their tolerance bands?

### Cameron Chapman, 2024-06-21

@Gary Angelus thank you for updating this.eplease review with another EE @Garrett O'Neill if available. Please use/create a editing and review checklist for each drawing updated for common issues, and checks, ensure other drafters use these, 
https://jenaero.atlassian.net/wiki/spaces/EE/pages/88014851/Common+Harness+Updates.+Please+add+these+to+EE+checklists+or+link+to+this+page. 
EE Checklists.xlsx

### Trevor Gronner, 2024-06-21

@Emalee Johnson Would you be willing to review the drawing changes?

### Emalee Johnson, 2024-06-24

@Garrett O'Neill  @Gary Angelus  Can we update to the new formatting so the BOM is included in the drawing package?

### Emalee Johnson, 2024-06-24

Feedback from production for the drawing:
- The heat shrink at the right angle does not have a tight enough tolerance, .25” will not ensure fitment in the ADP.  
- Recommend changing the tolerance for the 1.40” and 1.10” callouts to +/- .1”
- Recommend changing 1.40” to 1.3” - aligns more closely with current production measurements.
- Switch heat shrink callouts to match current standards.
- Updated drawings for 107-102094 and 107-102238 are great examples for heat shrink callouts.
- Length callout changed from 2.5” to 2.75” but we think this is a critical dimension for air data pod fitment that needs to stay at 2.75” +/- .1”.
- JST Connector pinout and orientation update to new drawing standards, example of this is in the drawing for 107-102238.
- As mentioned in my previous comment, including the BOM on the drawing is necessary.

@Gary Angelus @Garrett O'Neill @Cameron Chapman @Trevor Gronner Please see above feedback that @Liam Limon and I put together.

### Gary Angelus, 2024-06-25

[embedded: 107-102084-B1 (1f98a325-b312-4b76-85ed-06426ca2cdc0).pdf]
@Emalee Johnson, for review

### Emalee Johnson, 2024-06-25

@Gary Angelus Thanks! Did you upload the correct document? It does not look like all of the notes have been included in this new draft.

### Liam Limon, 2024-06-25

@Gary Angelus If you’d like to see how the LRF installs in the Air Data Pod I can show you on our IronBird version in Electronics if you’d like. Garrett O’Neil in Electrical Engineering is also pretty familiar with this assembly. Thanks!

### Gary Angelus, 2024-06-25

Hi Liam, always like to see where items are installed in the unit, any time  @Liam Limon

### Gary Angelus, 2024-06-25

@Emalee Johnson @Liam Limon @Garrett O'Neill [embedded: 107-102084[B1].pdf] 
Let me know if I missed anything.

### Emalee Johnson, 2024-06-25

@Gary Angelus Awesome, thank you! It looks good so far, I will work on reviewing this today and tomorrow morning and let you know if we have anymore feedback.

### Garrett O'Neill, 2024-06-26

@Gary Angelus Can you fill in these missing title block fields on both pages:
Next Higher Assembly: 107-101141
Drawn By: C. CHAPMAN
Drawn By Date: 3/23/2020
Approved By: J. O’CONNELL
Approved By Date: 3/23/2020

### Emalee Johnson, 2024-06-26

@Gary Angelus Thank you for adding the BOM to the drawing, can you format it like this and then remove the blank lines? 
This is the example from drawing 107-102094. 
[embedded: image-20240626-205038.png]
- Additionally, the balloons for items 3, 5, 6 should say AR on the lower half, they currently say 1.

### Emalee Johnson, 2024-06-26

@Gary Angelus  Ok I think the last comment is to just change the 1.3” dimension to be 1.300” please. Thank you so much, this drawing looks way better.

### Garrett O'Neill, 2024-06-27

@Emalee Johnson I had Gary remove the title block info and export notice from the BOM before copying it over, as it’s already present on the drawing sheet.

### Gary Angelus, 2024-06-28

@Garrett O'Neill @Emalee Johnson add PDF for one more review.

### Emalee Johnson, 2024-06-28

@Gary Angelus  Looks good to me, thank you for implementing all the feedback. 
@Liam Limon Can you glance at this one more time please?

### Cameron Chapman, 2024-07-08

@Gary Angelus thanks for making this update. Please coordinate review with @Garrett O'Neill or another EE when available. Things I can see from a quick review. 
- Please do not create a new altium file for each drawing. You should update the existing one. “107-102084 Laser Range Finder.SchDoc” The vault will keep the history. Please save over that file and delete the duplicate. 
[embedded: image-20240708-225256.png]
- This should become rev C. B1 would historically indicate a redline (going away). In Scotts new process, B1 would indicate an engineering release (not for production).
- CM should transition old revs to obsolete once this is released. @Angela Porto
- The new format should include the BOM and drawing in one pdf, and delete the excel BOM when released.
- Please coordinate a template with @Garrett O'Neill and record here. https://jenaero.atlassian.net/wiki/spaces/EE/pages/22183937/EE+Drawing+Templates+Documentation+Information+and+Examples  Please update all relevant confluence pages as the process is finalized. 
- Examples (mfr pn should be removed from BOM).
- Please use and add to the harness checklist tab here.  EE Checklists.xlsx

## Attachments (12)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240523-200221.png | image | 173 | 2024-05-23 | listed only |
| [107-102084-B1.pdf](attachments/21155_107-102084-B1.pdf.md) | pdf | 1547 | 2024-06-20 | converted |
| [107-102084-B1.pdf](attachments/21151_107-102084-B1.pdf.md) | pdf | 1547 | 2024-06-20 | converted |
| image001.png | image | 1 | 2024-06-20 | listed only |
| image002.png | image | 0 | 2024-06-20 | listed only |
| image003.png | image | 4 | 2024-06-20 | listed only |
| [107-102084-B1 (1512d2ea-54ed-4024-b594-7f7b043eeb17).pdf](attachments/21159_107-102084-B1%20(1512d2ea-54ed-4024-b594-7f7b043eeb17).pdf.md) | pdf | 2173 | 2024-06-21 | converted |
| [107-102084-B1 (1f98a325-b312-4b76-85ed-06426ca2cdc0).pdf](attachments/21197_107-102084-B1%20(1f98a325-b312-4b76-85ed-06426ca2cdc0).pdf.md) | pdf | 2515 | 2024-06-25 | converted |
| [107-102084[B1].pdf](attachments/21250_107-102084[B1].pdf.md) | pdf | 2691 | 2024-06-25 | converted |
| image-20240626-205038.png | image | 103 | 2024-06-26 | listed only |
| [107-102084-B1 (1859f870-f9ad-4a98-bca7-8d8010ee602c).pdf](attachments/21306_107-102084-B1%20(1859f870-f9ad-4a98-bca7-8d8010ee602c).pdf.md) | pdf | 2731 | 2024-06-28 | converted |
| image-20240708-225256.png | image | 45 | 2024-07-08 | listed only |
