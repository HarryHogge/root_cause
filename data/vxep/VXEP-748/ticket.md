# VXEP-748: VXE 674 734 main battery percentage reporting incorrectly S/N's 2101 & 2088

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-10-29
- **Updated:** 2024-10-31
- **Resolved:** 2024-10-31
- **Reporter:** Pat Wells
- **Assignee:** Hayden Jeanor
- **Creator:** Pat Wells
- **Labels:** Edge_Asset, Weekly-incident-tracker
- **Links:** relates to VXEP-720 (VXE 490 main battery percentage reporting incorrectly during flight with MB's (S/N's 1967 and 1737)); relates to VA-2115 (2 MB's (S/N's 1967 and 1737) do not seem fly intended 4 hrs on V490 ); relates to FS2-2495 (Document Battery Voltage/Current Software Design); relates to VXEP-759 (Simulation Overestimating Power Consumption)
- **Incident Type:** Other (Record"Event Type: XXXXXX" in the description)
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Statement from Edge FLOPS team:
We had another issue of the main batteries reading higher percentages on the software than the actual percentage of the battery after checking them post flight. We ran multiple flights on both batteries in two different aircraft. After the last flight of the day, while disassembling both aircraft, we checked the batteries and both read percentages of more than 20% of what the software was reading. For example, my flight specifically was reading 62% before recovery and read 37% on the battery checker post flight. Both of these batteries are brand new and were a part of a kit that we just received in HSV last week.

AAR’s attached

## Root Cause

The issue comes down to the use of COTS battery checkers and the Li-ion model included in the battery checkers to assess the state of charge of our Amicell battery. The cell chemistry of our Amicell batteries have a different SoC discharge curve compared to that of which the cell checkers are programmed to.
[embedded: image-20241030-204746.png]
Li-ion discharge curve
[embedded: image-20241030-212419.png]
Measured Amicell discharge curve

## Comments (8)

### David Grosher, 2024-10-30

@Jason Scherer Can you lay out the data path from voltage measurements to battery reporting on the GCS for this investigation. You can work with @Eric Brewer to see if there is a bug in the calculation.
Then, I think we should do a data collection with FLOPS to get a larger set of data across a population of batteries. Manufacturing variance could be an issue here.

### David Grosher, 2024-10-30

@Everett Werner

### Hayden Jeanor, 2024-10-30

@Gregory Nichols can you point me in the direction of the operator for this flight? or confirm that instead of “After the last flight of the day, while disassembling both aircraft, we checked the batteries and both read percentages of more than 20% of what the software was reading. For example, my flight specifically was reading 62% before recovery and read 37% on the battery checker post flight.” they meant “After the last flight of the day, while disassembling both aircraft, we checked the batteries and both read percentages of more than 20% less of what the software was reading. For example, my flight specifically was reading 62% before recovery and read 37% on the battery checker post flight.” Thanks!

### Calvin Rogers, 2024-10-30

@Hayden JeanorI was the Instructor/PIC for that specific flight. Your second quoted statement was correct. The battery checker was reading more than 20% less than the software was reading. Software = 62%, battery checker = 37%. I was not sure the exact numbers for the other flight which I gave the estimate of 20% for both. Let me know if this is what you were asking for or if I need to provide more clarification.

### Everett Werner, 2024-10-30

@David Grosher @Pat Wells @Hayden Jeanor @Cameron Chapman @Scott Whitney 
Worked with Cameron and Hayden: The issue appears to come down to the use of COTS battery checkers and the Li-ion model included in the battery checkers to assess the state of charge of our Amicell battery. The cell chemistry of our Amicell batteries are not the same as those used in Li-ion batteries. 

The simulation inaccuracy is a separate issue, its estimating that the vehicle will drain its entire battery capacity in a 20 minute flight, to do this it would need to consume roughly 4500W for the entire 20 minutes which is 3x more than the vehicle can output at 100% throttle.

[embedded: image-20241030-204746.png]
Li-ion discharge curve


[embedded: image-20241030-212419.png]
Measured Amicell discharge curve

### Cameron Chapman, 2024-10-30

@Hayden Jeanor @Everett Werner can you please open up linked issues for the sim inaccuracy (if not already documented), training and manual updates of sim inaccuracies, corrective actions for this issue (training and manual updates of not using the checker SOC, eventually removing SOC if inaccurate from the checker, etc). 
@Tom Westrich @Stephen Peters we should plan to replace this hobby Chinese checker at some point. potential requirement for the new charger, do you think we should add the ability for it to check battery and cell voltages without a power supply (powered by the battery?)?

### Cameron Chapman, 2024-10-30

Please also confirm these are the C/CA for the linked issues and update those as well (can just link to this one in those fields if the same)

### Hayden Jeanor, 2024-10-31

Corrective action for this is being tracked in https://jenaero.atlassian.net/browse/VXEP-720 . Closing this ticket

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V674_241025_111821_pack.zip | archive | 2125 | 2024-10-29 | listed only |
| T95_V734_241025_110050_pack.zip | archive | 2484 | 2024-10-29 | listed only |
| image-20241030-204746.png | image | 117 | 2024-10-30 | listed only |
| image-20241030-212419.png | image | 8 | 2024-10-30 | listed only |
