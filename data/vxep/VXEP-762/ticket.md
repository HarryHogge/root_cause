# VXEP-762: Check if VXE30 checker SOC is accurate for Main Batteries (I suspect no). Update manuals and charger+checker firmware to instruct not to use this feature and remove it if so.

- **Issue type:** Epic
- **Status:** In Process
- **Priority:** Medium
- **Created:** 2024-11-04
- **Updated:** 2026-06-05
- **Reporter:** Cameron Chapman
- **Assignee:** Josh Burrell
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-761 (VXE 557 Smoking Smell from Fuselage after connecting main battery); relates to VXEP-1177 (VXE 808 State of Charge discrepancy)
- **Epic Status:** To Do
- **Epic Color:** ghx-label-7
- **Issue color:** purple

## Comments (8)

### Jeremy Kostel, 2024-11-06

Likely needs more testing across multiple batteries and getting lower end SoC, but from quick spot checks on charging a main battery from 60%-99% this morning SoC actually appears to track fairly well. Here is a graph showing actual, expected, and % error from a single battery tested today. We see less than a 0.5% error at each interval: 

[embedded image-20241106-212231.png]

### Christa Meck, 2026-06-01

@Cameron Chapman @Jeremy Kostel Is this still a thing?

### Cameron Chapman, 2026-06-01

@Christa Meck I think so for the checkers. Assigning to @Josh Burrell, is someone in HSV able to check the accuracy of the checker vs charger, and update documents accordingly? I suspect that the SOC will be inacurrate for main batteries.

### Josh Burrell, 2026-06-01

@Cameron Chapman will do

### Josh Burrell, 2026-06-05

@Cameron Chapman Heres what we found
[embedded checker vs charger.jpg]

### Cameron Chapman, 2026-06-05

Thanks @Josh Burrell I think the soc is accurate on the charger since it has custom fw, but not the checker. Could you update the b30 docs to say to diregard the checker soc and just refer to voltage only. We can keep this issue open to label the checkers themselves. Do you think this should get a customer notification? Lower priority since this is b30 checkers only.

### Josh Burrell, 2026-06-05

@Cameron Chapman I’ll have to get with Pat about the sending out an SB piece. We can definitely update the manuals for the 30s. All of ours showed lower than the charger so if that’s the case across the board is it really an issue?

### Cameron Chapman, 2026-06-05

@Josh Burrell It is minor, but enough of an issue for someone to write an incident (see linked issue). Could lead to confusion when preparing for air shipment, checking if enought SOC to launch, etc. A manual update may be sufficient. They have been using these checkers for years and most likely know they are not accurate.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20241106-212231.png | image | 12 | 2024-11-06 | listed only |
| checker vs charger.jpg | image | 65 | 2026-06-05 | listed only |
