# VA-400: TPTR-94 HLB reading incorrect -Summarize C/CA

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2023-08-29
- **Updated:** 2025-06-09
- **Resolved:** 2025-06-09
- **Reporter:** Cameron Chapman
- **Assignee:** Cameron Chapman
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-28 (TPTR-94 HLB reading incorrect percentage compared to measurement with checker)

## Description

TPTR-94 HLB reading incorrect - Investigation .pptx
@Nadia Brown I added some comments to the ppt and changed the name. Please do the following top pri. 
- Plot the section of the log where the flights dip to 80% SOC ~28V. (Done)
- For the same time period, plot the total cell voltage from the same section of the XCOM log. (Done)
- The times won’t line up, so you’ll have to line up something like UTC or Ibatt. Ask Adrian if unsure how. Create a new column time since Launch wizard start or something.
- If the cell voltages look good, and the vbatt from the flight log drops, that proves a connection issue. (Done)
- Attach discharge test plot that was performed on that battery after the incident. That will show that the connection issue is not with the battery, but instead the damaged 511 CW. (Is the discharge test included in the AAR or is there someplace else I can hunt this information down from?) HLB 2-1803. Probably here  \\condor\Production\Battery Information\Battery Production Data List\VXE30 HL Battery Info. Contact Ben N if not.  (Done)
-

## Sprint

VXE-1 Cameron's Team 9-17, VXE-1 Electrical-8, VXE-2 Everything Else 2024-03, VXE-1 Electrical 10/29, VXE-1 Electrical 11-20-12/10, VXE-1 EE Team Sprint 8/28-9/17, VXE Product Dev & Sup 2024-07, VXE-1 Electrical 10/9, VXE Product Dev & Sup 2024-05, VXE-1 Electrical-7, VXE Prod Dev & Sup 2024-08

## Comments (11)

### Nadia Brown, 2023-09-25

@Cameron Chapman Thank you for the patience. I did take a bit longer to go through this so that I could read through all the terms and make sure I was comparing the right things. I added the logs I used to this ticket and graphed them around what I thought may be key points in the data we wished to see.

I went ahead and added my graphs and conjectures to the PowerPoint. Please let me know if I missed anything or misunderstood the assignment. The only thing I did not add in the excel sheets is the column indicating time since launch wizard started as I was a bit uncertain on the meaning and reached out to @Adrian Garcia for some clarifications, but waiting at the moment.

### Nadia Brown, 2023-09-26

Added the column and updated the charts.

### Cameron Chapman, 2023-10-03

@Nadia Brown 
- HLB 2-1803. Probably here  \\condor\Production\Battery Information\Battery Production Data List\VXE30 HL Battery Info. Contact Ben N if not.

### Nadia Brown, 2023-10-05

@Cameron Chapman I think this is ready for review

### Cameron Chapman, 2023-10-06

@Nadia Brown Please see notes in ppt, complete those updates, and let me know when done. 
[embedded: image-20231006-155728.png]

### Nadia Brown, 2023-11-02

@Cameron Chapman I addressed newest comments about adding time and date and flight on slides. Sent back to you.

### Cameron Chapman, 2023-12-15

@Nadia Brown please make the following changes to the ppt. 
- Cody thinks “HLB 1803 was likely installed on 8/7 for flight #2 (this was only verified through a flight data log on a future flight as the actual AAR is unavailable at this time)”. Your ppt says 7/8. Can you please make sure the logs line up with Cody’s statement? See parent ticket. 
- Since we are working with a UK customer, I recommend saying August 7 to avoid confusion.
- The drop in voltage looks more like battery disconnected vs the description saying 80% SOC. I think we need to look for a different log/time period. Can you please look for anywhere the battery reports 80% SOC ~28V? To help narrow it down, one of the logs should report the battery SN.

### Nadia Brown, 2023-12-18

@Cameron Chapman So after looking into this a bit, it is agreed this did occur on August 7th. The reason it appears on the ppt as 07/08 is because the template for the ppt listed it as day/month. This is super confusing since the standard here in the US is month/day, but I had assumed we were using day/month because this may be related to Tequila? I can go ahead and swap it to be 08/07 so it is month day instead of day/month. That’s no problem, just want to clarify and offer an explanation to that date.

For the second point, this has been a reoccurring issue with this particular log set--but they did not record the battery serial number in the log I was given. I checked the GCS and xtls, and vtls but saw no mention anywhere. I am also a bit confused and require some clarification, but for:
”Can you please look for anywhere the battery reports 80% SOC ~28V?”

Is that not what we did with the graphs in the powerpoint already?

### Cameron Chapman, 2023-12-18

@Nadia Brown
“August 7” (spelling out the month) is tedious, but avoids any confusion. 
 I was looking at slide 6 and somehow missed slide 7. I think it would be useful to recreate this plot, but with the power cycle before and after this data. If you could show that before and after the voltages were equal, and this power cycle they were not, that could prove the issue was with this battery. If that is not available, the same plot from the 511 logs before the linked incident could prove the power connection was the issue. https://jenaero.atlassian.net/browse/VA-35  
The dip to 0 is likely the battery being unplugged, but the 28V VtVbatt seems to be what we are looking for. 
[embedded: image-20231219-000452.png]

### Nadia Brown, 2023-12-18

@Cameron Chapman Thank you. I appreciate the reply. I do agree August 7th is a lot clearer and will go ahead and move to that. I’ll go ahead and try to get you those plots--going to reassign for myself again.

### Nadia Brown, 2023-12-21

@Cameron Chapman I updated the dates to be more clear, and added another graph on page 7 with the power overlaid on the voltages from the current sense and battery itself. The power does go to zero on the dip, and then appears to have an almost equal spike but in the negative direction after.

## Attachments (11)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [TPTR-94 HLB reading incorrect VTL.xlsx](attachments/16715_TPTR-94%20HLB%20reading%20incorrect%20VTL.xlsx.md) | xlsx | 9894 | 2023-09-26 | converted (cut) |
| [TPTR-94 HLB reading incorrect XCOMM.xlsx](attachments/16716_TPTR-94%20HLB%20reading%20incorrect%20XCOMM.xlsx.md) | xlsx | 6749 | 2023-09-26 | converted (cut) |
| [107-101191 Hybrid Lift Test.pptx](attachments/16855_107-101191%20Hybrid%20Lift%20Test.pptx.md) | pptx | 9459 | 2023-10-05 | converted |
| [2-1803 Data Comparison.xlsx](attachments/16856_2-1803%20Data%20Comparison.xlsx.md) | xlsx | 665 | 2023-10-05 | converted (cut) |
| Battery Inc 2-1803.PNG | image | 23 | 2023-10-05 | listed only |
| [VXE30 HLB 2-1803 230809 B1.csv](attachments/16849_VXE30%20HLB%202-1803%20230809%20B1.csv.md) | csv | 35 | 2023-10-05 | converted |
| [VXE30 HLB 2-1803 Charger Data 230809.xlsx](attachments/16861_VXE30%20HLB%202-1803%20Charger%20Data%20230809.xlsx.md) | xlsx | 44 | 2023-10-05 | converted |
| image-20231006-155728.png | image | 8 | 2023-10-06 | listed only |
| [TPTR-94 HLB reading incorrect VTL (f0ab7081-4ff1-47ff-8c27-db3fae7662b4).xlsx](attachments/17517_TPTR-94%20HLB%20reading%20incorrect%20VTL%20(f0ab7081-4ff1-47ff-8c27-db3fae7662b4).xlsx.md) | xlsx | 10308 | 2023-11-09 | converted (cut) |
| [TPTR-94 HLB reading incorrect XCOMM (27d96feb-1373-4189-8a22-df1576774fb4).xlsx](attachments/17516_TPTR-94%20HLB%20reading%20incorrect%20XCOMM%20(27d96feb-1373-4189-8a22-df1576774fb4).xlsx.md) | xlsx | 7307 | 2023-11-09 | converted (cut) |
| image-20231219-000452.png | image | 41 | 2023-12-18 | listed only |
