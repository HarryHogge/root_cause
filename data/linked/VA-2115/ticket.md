# VA-2115: 2 MB's (S/N's 1967 and 1737) do not seem fly intended 4 hrs on V490

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-10-28
- **Updated:** 2024-10-30
- **Resolved:** 2024-10-30
- **Reporter:** Hayden Jeanor
- **Creator:** Hayden Jeanor
- **Links:** relates to VXEP-748 (VXE 674 734 main battery percentage reporting incorrectly S/N's 2101 & 2088); relates to VXEP-720 (VXE 490 main battery percentage reporting incorrectly during flight with MB's (S/N's 1967 and 1737))

## Description

From Flops:
“2 MB's do not seem fly intended 4 hrs, allegedly lasted for only 2-3h of flight time
S/N's 1967 and 1737”

## Plan

- we should also get more info from the operator "do not seem fly intended 4 hrs" according to what indicator/data point (guessing GCS). @Brian Casey
- Perform discharge profiles on Batteries to determine if their life has degraded to only last < 3hrs (~900Whr)'
- Flight operations battery cabinet, they are marked with a big blue tape saying Hawaii demo
- give material disposition on batteries
- close monitoring of cell voltages periodically during test
- if batteries have plenty of capcaity (~1000Whr +) we need to investigate V490 further

## Comments (10)

### Hayden Jeanor, 2024-10-28

the logs show that there was plenty of battery left acc. to apVlife 
[embedded: image-20241028-163051.png]
to complicate it further, on one of the flights, we had super erratic Vlife log data. Almost like it wasnt compensating for the amount of load on the battery
[embedded: image-20241028-163103.png]

### Hayden Jeanor, 2024-10-28

For reference, here is from a full 3.5hr flight cody performed this week:
[embedded: image-20241028-163229.png]

### Hayden Jeanor, 2024-10-28

@Ben Norris  would you or someone else in production be able to perform our production capacity test on these two MBs?[embedded: 107-101047 - Electronics - Amicell Cell Pack Test - Work Instruction.pptx]

### Hayden Jeanor, 2024-10-28

Baseline production capacities:
- 3-1967 = 1408Whr
- 3-1737 = 1393Whr

### Ben Norris, 2024-10-28

@Hayden Jeanor I’ll run the test for capacity comparison.

### Cameron Chapman, 2024-10-28

@Ben Norris @Hayden Jeanor 
where are the batteries now? What charge state are they in? 
Recommend close monitoring of cell voltages periodically during test
we should also get more info from the operator "do not seem fly intended 4 hrs" according to what indicator/data point (guessing GCS)

### Hayden Jeanor, 2024-10-28

@Cameron Chapman my fault for not measuring SoC before charging the packs. Ben reported that the batteries appeared to be at storage charge. @Brian Casey @Artis Bertulis can you confirm if the batteries were charged/discharged anytime between the flights and this morning?

### Artis Bertulis, 2024-10-28

@Hayden Jeanor , I’m pretty certain that they are, because they got shipped here after the demo and haven’t been used since, and I’d like to think that they got discharged to “storage” for the shipment, but @Brian Casey should be able to confirm.

### Hayden Jeanor, 2024-10-30

Pull test results (production fail criteria = 34lbs)
3-1967:
- pull 1 = 57.2 lbs
- pull 2 = 58.9 lbs
- pull 3 = 56.1lbs
- Avg = 57.4 lbs

3-1737:
- pull 1 = 36 lbs
- pull 3 = 37.1 lbs
- pull 3 = 34.3 lbs
- avg = 35.8 lbs

### Hayden Jeanor, 2024-10-30

duplicate of https://jenaero.atlassian.net/browse/VXEP-720 . Closing

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [107-101047 - Electronics - Amicell Cell Pack Test - Work Instruction.pptx](attachments/24242_107-101047%20-%20Electronics%20-%20Amicell%20Cell%20Pack%20Test%20-%20Work%20Instruction.pptx.md) | pptx | 21370 | 2024-10-28 | converted |
| image-20241028-163051.png | image | 149 | 2024-10-28 | listed only |
| image-20241028-163103.png | image | 261 | 2024-10-28 | listed only |
| image-20241028-163229.png | image | 157 | 2024-10-28 | listed only |
