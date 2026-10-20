# VXEP-497: Scour ALL plane records and figure out which ones were burned in twice. List planes they were installed into.

- **Issue type:** Sub-task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-04-26
- **Updated:** 2024-07-10
- **Resolved:** 2023-05-03
- **Reporter:** Connor Peebles
- **Assignee:** Ryan Ferguson
- **Creator:** Connor Peebles
- **Parent:** VXEP-484 0002P01G Green Autopilot Reliability Issues/Fallout Study
- **Links:** relates to VXEP-484 (0002P01G Green Autopilot Reliability Issues/Fallout Study)

## Comments (8)

### Ryan Ferguson, 2023-04-26

I’ve attached a spreadsheet of all AP’s that received two or more burn-in attempts according to the files on Dexter.  Tomorrow I plan to partner with Quality to go through the travelers in SCO to determine which planes contain an autopilot on that list.  

Additional findings of this investigation - A total of 133 autopilots had their burn-in files on Dexter.  Of these, 50 were re-burnt.  This means an average of 37% of autopilots require re-burns.  This investigation did not yet verify how many of that 37% actually passed both attempts but this will be checked tomorrow.  

@Matt Philley @Marc Richardson FYI

### Ryan Ferguson, 2023-04-27

I did more analysis and found a lot more files on Dexter.  I’ve written a Python script for the analysis of the data I pulled from Dexter and out of it I have the following information for the autopilots produced after January 1 2021.  I also have the ability to open up that time limit to significantly older autopilots, going back as far as 2005.  For now however I’ve constrained the data to keep things more relevant to VXE30.

---------- STATISTICS ----------
Total number of files analyzed: 1153 Files
Total number of SN's produced since Jan 1 2021: 197 SN's
Total number of reburned autopilots: 65 Autopilots
Percentage of autopilots reburned: 32 %

@Marc Richardson The attached txt file is the list of all affected autopilots within the date ranges mentioned above.  If I can get some help from quality tomorrow to search through SCO’s records we can try to connect the AP’s in the list with travelers.  I can also provide a significantly longer list if we want to open up the date constraints to cover block 25 as well.

[embedded: AP Reburn Analysis.py][embedded: AP Reburns 2021 thru apr 27 2023.txt]

### Ryan Ferguson, 2023-04-28

I have finished compiling the total number of aircraft which currently have autopilots that underwent multiple burn-ins attempts.  The table below contains the list of all affected aircraft affected by this risk.  I have also attached the file which associates tail numbers with autopilot SN’s.  Note that this file may look a bit messy as it was created using the files on Carson’s computer.  It also only covers aircraft going back as far as 2020.  
[embedded: Tail Number to AP Table with Reburns.xlsx]
| Planes at risk: |
| 334 |
| 336 |
| 371 |
| 425 |
| 426 |
| 430 |
| 448 |
| 449 |
| 450 |
| 454 |
| 455 |
| 463 |
| 465 |
| 467 |
| 468 |
| 470 |
| 471 |
| 472 |
| 474 |
| 486 |
| 487 |
| 508 |
| Spare 3006 |
| Spare 3011 |


The .txt file below also includes a full history of all AP SN’s that went through two or more burn-ins.  It is the same output of the script I wrote earlier but I took out the time constraints so it can show the data for all Green AP’s going back as far as 2005.  If this analysis has to be done again in the future we can easily copy the files off Dexter again and rerun the script.
[embedded: AP SNs.txt]

### Cameron Chapman, 2023-05-02

@Ryan Ferguson thanks for the great work. Should we reopen this task 2 to scrub this list for reports that were repeated, but not actual failures due to reporting software crashes as you mentioned? Reopening for answer.

### Ryan Ferguson, 2023-05-02

I’ll go through and dig on those specific tail numbers highlighted earlier to verify by hand if they were burned multiple times and update this ticket and the email chain with any updates.

### Cameron Chapman, 2023-05-03

Hello all,
 
I’ve done some more work digging into the aircraft my previous analysis highlighted to see if I could learn more about the individual failures.  Below you can see a summary of each of the aircraft tail numbers I identified and a general description of their burn-in statuses.  Note that this includes many more aircraft than the earlier report as it covers all aircraft and spares boxes going back to early 2020.
 
Aircraft 334 VXE – AP 10005 – 3 burn-in attempts – Failed first burn-in, passed second and 3rd attempt.
Aircraft 336 VXE – AP 10028 – 4 burn-in attempts – Failed first two burn-ins, passed 3rd and 4th attempt.
Aircraft 371 XE25 – AP 10189 – 2 burn-in attempts – First burn-in never triggered, passed second attempt.
Aircraft 371 VXE – AP 10152 – 2 burn-in attempts – First burn-in never triggered, passed second attempt.
Aircraft 425 VXE – AP 10302 – 2 burn-in attempts – Failed first burn-in, passed second attempt.
Aircraft 426 VXE – AP 10286 – 2 burn-in attempts – Failed first burn-in, passed second attempt.
Aircraft 430 VXE – AP 10210 – 2 burn-in attempts – Failed first burn-in, passed second attempt.
Aircraft 448 VXE – AP 10131 – 3 burn-in attempts – Failed first burn-in, passed 2nd and 3rd attempt.
Aircraft 449 VXE – AP 10235 – 2 burn-in attempts – Failed first burn-in, passed second attempt.
Aircraft 450 VXE – AP 10195 – 2 burn-in attempts – Passed both burn-ins 6 months apart.  No risk posed to this aircraft by double burn-ins.
Aircraft 454 VXE – AP 10244 – 2 burn-in attempts – Appears to be a duplicate AP SN with tail 467.  Probably had only one burn-in but unable to verify for sure.
Aircraft 455 VXE – AP 10362 – 2 burn-in attempts – Failed first burn-in, passed second attempt.
Aircraft 463 XE25 – AP 10236 – 3 burn-in attempts – Failed first burn-in, passed second attempt, failed 3rd attempt.
Aircraft 465 VXE – AP 10242 – 2 burn-in attempts – Passed first time, then failed burn-in two months later.
Aircraft 467 VXE – AP 10244 – 2 burn-in attempts – Appears to be a duplicate AP SN with tail 454.  Probably had only one burn-in but unable to verify for sure.
Aircraft 468 VXE – AP 10246 – 2 burn-in attempts – Passed both burn-ins 6 months apart.  No risk posed to this aircraft by double burn-ins.
Aircraft 470 VXE – AP 10242 – 2 burn-in attempts – Passed first time, then failed burn-in two months later.
Aircraft 471 XE25 – AP 10253 – 2 burn-in attempts – Failed first burn-in, passed second attempt.
Aircraft 472 XE25 – AP 10230 – 3 burn-in attempts – First burn-in failed and subsequent burn-in attempts never properly completed.  Burn-in appears to have consistently failed on this autopilot.
Aircraft 474 XE25 – AP 10258 – 2 burn-in attempts – Failed first burn-in, passed second attempt.
Aircraft 486 VXE – AP 10289 – 2 burn-in attempts – First burn-in never triggered, passed second attempt.
Aircraft 487 VXE – AP 10298 – 2 burn-in attempts – Failed first burn-in, passed second attempt.
Aircraft 508 VXE – AP 10375 – 2 burn-in attempts – Failed first burn-in, passed second attempt.
Spare 3006 XE25 – AP 10151 – 3 burn-in attempts – Burn-in never triggered first two attempts, passed 3rd attempt.
Spare 3011 XE25 – AP 10390 – 2 burn-in attempts – Failed first burn-in, passed second attempt.
 
 
Overall, the data seems to show that we had quite a few autopilots which had burn-in issues that passed in subsequent burn-ins.  It was also found that we had a loss of traceability on the autopilots for aircraft 454 and 467 where they both ended up getting assigned the same AP SN several months apart.  The cause of this is not clear but could explain some issues where the AP’s would be burned in successfully the first time then fail burn-in a few months later and end up in a plane.  In those circumstances it is likely the failing second burn-in graph was caused by a separate autopilot receiving the same SN as the original one.  These losses of traceability all seemed to happen within a 2-month time span which indicates a potential issue with the SN lists not being updated or saved.  The first board to show this issue (AP SN 10244) was processed on 5/27/2022 and the last (AP SN 10242) was processed on 7/12/2022.
 
Another failure mode was also discovered while reviewing the data.  In some autopilots the burn-in would fail to trigger and the board would simply refuse to record any burn-in data.  This is likely caused by inconsistencies in the oven, but more research should probably be done on these outliers.
 
The major outlier however is aircraft 472.  No passing burn-in attempts were able to be found for the autopilot installed in it.  This included an exhaustive look through SCO’s digital files and traveler records.  It is possible this was caused by another loss in traceability but without being able to open the plane we cannot verify this.
 
 
Please let me know if there are any questions.  I’ll be happy to explain my methods in more detail or do some more detailed research.
 
 
|  | Ryan Ferguson Production Engineer Edge Autonomy – SLO Phone: +1-765-437-2057 Email: rferguson@edgeautonomy.io |

 
 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: John Tucker <jtucker@edgeautonomy.io> 
Sent: Monday, May 1, 2023 2:59 PM
To: Ryan Ferguson <rferguson@edgeautonomy.io>; Ryan Stafford <rstafford@edgeautonomy.io>; Desiray Johnston <djohnston@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>; Greg Fryer <gfryer@edgeautonomy.io>; Connor Peebles <cpeebles@edgeautonomy.io>; Kyle DeBernardi <kdebernardi@edgeautonomy.io>; Marc Richardson <mrichardson@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>
Cc: Dave Grosher <dgrosher@edgeautonomy.io>; Kelly Furlong <kfurlong@edgeautonomy.io>; Matt Philley <mphilley@edgeautonomy.io>; Lawton Ziedses Des Plantes <lzdp@edgeautonomy.io>
Subject: RE: Discuss holes found on most of our fixed wing AP processors, and approve if we are ok to use them
 
Hi Ryan,
 
Thank you very much for leading this project – this is exactly what we needed to determine the correlation between multiple AP Chip burn-ins and recent VXE30 AP issues/failures, as well as to isolate the Avionics Boxes we have in production.
 
I think we have what we need at the moment as we determine fleet risk and effectivity from this, and of course we’ll know more after sending chips out for decapsulation.
 
To the group – please continue using this thread to add any additional thoughts or findings on the Green AP topic.
 
Best,
John
 
From: Ryan Ferguson <rferguson@edgeautonomy.io> 
Sent: Friday, April 28, 2023 1:15 PM
To: Ryan Stafford <rstafford@edgeautonomy.io>; Desiray Johnston <djohnston@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>; Greg Fryer <gfryer@edgeautonomy.io>; Connor Peebles <cpeebles@edgeautonomy.io>; Kyle DeBernardi <kdebernardi@edgeautonomy.io>; Marc Richardson <mrichardson@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>; John Tucker <jtucker@edgeautonomy.io>
Cc: Dave Grosher <dgrosher@edgeautonomy.io>; Kelly Furlong <kfurlong@edgeautonomy.io>; Matt Philley <mphilley@edgeautonomy.io>; Lawton Ziedses Des Plantes <lzdp@edgeautonomy.io>
Subject: RE: Discuss holes found on most of our fixed wing AP processors, and approve if we are ok to use them
 
Hello all,
I’ve completed the project to create a list of aircraft which had autopilots with more than one burn-in.  The details can be found in ENG-1592.
 
My first task was to create a list of all autopilots which experienced more than one burn-in.  This involved writing a python script to parse all 1,153 log files on Dexter.  The output of this script can be seen in the attached text file which includes autopilots as old as 2005.  If I limit the timeline to only autopilots produced since Jan 1, 2021 I end up with the following statistics:
 
---------- STATISTICS FOR AP’s AFTER 2021 ----------
Total number of files analyzed: 1153 Files
Total number of SN's produced since Jan 1 2021: 197 SN's
Total number of reburned autopilots: 65 Autopilots
Percentage of autopilots reburned: 32 %
 
 
Running the script to look at all autopilots produced since 2005, we can see some lifetime statistics as below:
 
---------- STATISTICS FOR ALL GREEN AP’s ----------
Total number of files analyzed: 1153 Files
Total number of individual SN's produced: 690 SN's
Total number of reburned autopilots: 299 Autopilots
Percentage of autopilots reburned: 43 %
 
 
 
I was able to take the outputs of these scripts and compare them against the records in SCO to determine what autopilot SN was installed in which plane.  I can then reference that SN against the re-burn sheet to tell if it was affected by the re-burn risk.  The full spreadsheet for this can also be found in the attachments, but to summarize it we come out with the following aircraft which have a risk posed to them by the re-burn.  I’ve taken the data out of that sheet and put it in the one Desiray requested.
 
 
| Tail # | Production Status | Type | Avionics Box | # Burn In |
| 378 | LM Cage (ready to ship) | FBI XE25 Upgrade | Reused | 1 |
| 379 | Ready for flight test | FBI XE25 Upgrade | Reused | 1 |
| 380 | Ready for source | FBI XE25 Upgrade | Reused | 1 |
| 381 | In source inspection | FBI XE25 Upgrade | Reused | 1 |
| 455 | NCR CW during flight test | RMA | New | 2 |
| 333 | In source inspection | FBI XE25 Upgrade | Reused | 1 |
| 508 | Failed flight test | FBI Goodwill | New | 2 |
| 334 | Ready for source | FBI XE25 Upgrade | Reused | 3 |
| 375 | Ready for flight test | FBI XE25 Upgrade | Reused | 1 |
| 501 | LM Cage (ready to ship) | New (PMA) | New | 1 |
| 507 | LM Cage (ready to ship) | New (PMA) | New | 1 |

 
 
Please let me know if any further data analysis is needed on this dataset.  I can easily manipulate the script to change the data format if needed.

### Ryan Ferguson, 2023-05-03

Since the data has been collected and compiled as requested I’m going to close this ticket.

### Cameron Chapman, 2023-05-04

@Maxime Jeanneau , useful data to look for correlation or a lack of it.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Green AP Double Burn-ins.xlsx](attachments/14222_Green%20AP%20Double%20Burn-ins.xlsx.md) | xlsx | 13 | 2023-04-26 | converted |
| [AP Reburn Analysis.py](attachments/14257_AP%20Reburn%20Analysis.py.md) | text | 2 | 2023-04-27 | converted |
| [AP Reburns 2021 thru apr 27 2023.txt](attachments/14258_AP%20Reburns%202021%20thru%20apr%2027%202023.txt.md) | text | 1 | 2023-04-27 | converted |
| [AP SNs.txt](attachments/14276_AP%20SNs.txt.md) | text | 3 | 2023-04-28 | converted |
| [Tail Number to AP Table with Reburns.xlsx](attachments/14275_Tail%20Number%20to%20AP%20Table%20with%20Reburns.xlsx.md) | xlsx | 16 | 2023-04-28 | converted |
