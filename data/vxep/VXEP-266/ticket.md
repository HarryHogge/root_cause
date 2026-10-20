# VXEP-266: VXE (all) ADP: Heated Pitot/New SA CAM/Remove other obsolete components

- **Issue type:** Major Project
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-01-05
- **Updated:** 2026-07-30
- **Resolved:** 2025-11-14
- **Due:** 2025-05-01
- **Reporter:** Cameron Chapman
- **Assignee:** Grant Goodman
- **Creator:** Cameron Chapman
- **Labels:** Heated-Pitot, valid
- **Parent:** VXEP-902 LRR March Delivery
- **Links:** relates to ENGPRJA-32 (Heated pitot system prototype for 2023 demo); relates to VXEP-93 (Replace SA Camera EM18911 (100-100835) and EM19821 (100-101235) are obsolete. due February 2025.); is a parent of VA-1316 (Define requirements for heated pitot versions); is a parent of VA-1315 (Heated pitot-Define schedule, create JIRA tasks, and assign. ); relates to VA-1342 (Heated Pitot V1 Mechanical Design); relates to VA-1343 (Heated Pitot V1 Electrical Design); relates to VXEP-581 (Seal Air Data Pod Assembly PN 107-101141); relates to XKIT-2781 (MAGNSS Productization); blocks LRRSUAS-455 (Final 3 Systems Delivered); fixes VXEP-976 (VXE 500 Reports large negative AGL after landing ); relates to VXEP-1511 (Updates for Dual SA Camera BOM (2121923-01 and -02))
- **Issue Status:** Deadline from Sam that we need a PDR and the balance of the plan by 3/29.
- **Is this ticket a Design Project?:** Yes
- **Project Tier:** Tier 2
- **Planned Milestone(s):** Preliminary Design Review (PDR), Detailed Design/Critical Design Review (CDR), Production Readiness Review (PRR)
- **Current Sprint Priority:** 15.0
- **LRR Desired Delivery Date:** 2025-08-01
- **LRR Required Delivery Date:** 2025-08-01
- **Contract/Customer First Need:** June 02, 2025 Production Cut In
- **Product/Tech Owner:** Greg Fryer
- **Program (Marquee):** VXE30 Aircraft Sustainment
- **Job Number:** J100078 - Sustainment: VXE-30

## Description

Confluence: https://jenaero.atlassian.net/wiki/spaces/PDAO/pages/163643414/Air+Data+Pod+Updates+Heated+Pitot+Initial+and+Havoc 
Files: Heated Pitot
Shared Folder: 2024 Air Data Pod Updates
Subsystem files: https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Electrical/SA%20Camera%20Replacement?csf=1&web=1&e=c6XIc6 Heated Pitot
Requirements and Trade Study: 2024 ADP Requirements.xlsx
2023 Heated Pitot Prototype
Vault (do not post WIP electrical files here, just post when ready for order/production)C:\JAI Vault 1\Projects\107 - Stalker XE, VTOL Gen 2\Electrical Design\Heated Pitot

Electrical design related to the heated pitot/heated Air Data Pod prototype & productionized/refined version. 
See here for SA Camera replacement requirements and info. It is likely most efficient to integrate both updates at once. https://jenaero.atlassian.net/browse/VXEP-93

## Comments (44)

### Greg Fryer, 2024-02-02

Linked in the SA Camera project, which likely should be changed to a problem, content incorporated, and then closed as duplicate. However, that can only happen if we have enough SA cameras left to keep production going until we have a whole new ADP.
@Eric Rinell looked at the proposed replacement from the company we tried to by Qty 500 (“lifetime buy”), and it does not remotely fit.

### Greg Fryer, 2024-02-25

@Cameron Chapman @Rajesh Budhabhatti I took the liberty of re-assigning this to Raj. I just found an email in my vacation backlog indicating that LM is trying to drive heated pitot into the baseline TIQUILA scope. I am working with them to negotiate the exact cut-in (ideally to a future phase), but it does indicate that we should shift the focus from the SA Camera (now resolved - or postponed to at least 2025) and instead drive to a revision to the VXE-30 Air Data Pod to incorporate the heated pitot. Note that @Eric Rinell has done initial mechanical design, so has a heater element we can electrically evaluate.
Please be sure this goes through our design process, and we will need a project plan for it (schedule). We should also evaluate obsolescence, but err strongly towards lifetime buys vs. actual design out (if possible). Given that our business plan is to move to Havoc, which will have a new ADP, that is where full de-obsolescence should reside. (And additional improvements, such as CAN and more robust software/microcontroller design. And EMI.

### Rajesh Budhabhatti, 2024-02-26

I believe Lazlo has done some preliminary testing with pitot tube heating using both 5V and 12V. I will work with Eric to see if there is any mechanical issues to be considered. I also believe Lazlo is out until Friday so I will get on this issue.

### Cameron Chapman, 2024-02-26

@Rajesh Budhabhatti please tag up with me for a kickoff. We will start with requirements and evaluating the trade offs of different options. 
@Greg Fryer let me know when you have a better idea of due date.

### Cameron Chapman, 2024-02-26

[embedded file]

### Rajesh Budhabhatti, 2024-02-26

Will do. Thanks

### Greg Fryer, 2024-02-27

@Cameron Chapman @Rajesh Budhabhatti Apologies for us getting jerked around. Just got a deadline from Sam that we need a PDR and the balance of the plan by 3/29. This is VXE30 only, and so we should limit the scope strictly to heated pitot since the SA cam is addressed by the lifetime buy.
Guess at due date remains the same (late Jun/Jul with MCMAGNSS updates).
Please invite me to the kickoff, so I can answer any context shortages. Also add @Eric Rinell since he already crafted some mechanical design and the actual metal pitot and a notional heating element - obviously needs to get through concept review to make sure it’s all coherent.

### Eric Rinell, 2024-02-27

@Greg Fryer Need requirement definition on heating the static side. Is it included in this scope of work, or will pitot heat be sufficient?

### Cameron Chapman, 2024-02-27

@Eric Rinell Greg said yes, need heated static as well.

### Cameron Chapman, 2024-03-04

Moving old project order to comments. See epics now. 
Heated pitot project order.
- Define and capture requirements.
- Do we have a temperature, humidity, snowfall, or other related requirement?
- Is the requirement just to add a reasonable amount of heating with limited scope?
- Do we want/need switchable, or could switching on automatically based on temperature be acceptable?
- Outline schedule in confluence. https://jenaero.atlassian.net/wiki/spaces/PDAO/pages/163643414/Air+Data+Pod+Updates+Heated+Pitot+Initial+and+Havoc
- Evaluate main options. Will they provide enough power and not add unacceptable risk to the aircraft? 
- Share power with SA CAM. SW limit is ~0.85A with SA cam taking ~0.15A. Have not quantified max current available if SW limit was disabled. Power supply is limited to 5A, but does not have enough heat sinking to support that. 
- Previous testing indicated <3.5A continuous among all 12V supply. (we do not want to limit power available to 12V payloads with this design). Trillium already uses a lot of the capacity.
- See attached POWER TREE, B25+VTOL2.SchDoc
- Share power with ADP and VTOL AP (this seems like a bad idea).
- New harness to connect more power to ADP (does not seem in scope).

### Laszlo Juhasz, 2024-03-06

As a reminder from the prototype development, using a thermostat resulted very dynamic ripple effect on the power source and over current was detected by the SW. I’ve had conducted a proof-of-concept test using a PTC fuse replacing the thermostat and avoiding such problem. I’m sharing a document explaining the result and comparing the two-temperature controlling technics.
[embedded file]

### Rajesh Budhabhatti, 2024-03-06

Eric has a machined pitot tube ready for testing. He will deliver it to us when the heater element arrives so we can conduct power and temperature testing.

### Cameron Chapman, 2024-03-07

@Eric Rinell @Rajesh Budhabhatti @Jack Waeschle There is a large risk that we will not be able to provide that much power to the heated pitot without cutting into the 12V payload budget (required for Trillium payloads). This is why the power capacity test is high priority. We should also evaluate options for if we do not have that much power available (purchase higher resistance/lower power heaters)

### Rajesh Budhabhatti, 2024-03-08

Agreed. That is why I am thinking of making a mathematical model for pitot tube and correlate our findings from the testing Mark and I did on Wednesday. For our testing yesterday, we used a 12 Ohm heater and limited current to 1 amp. I will have more data and strategy to share by end of day today.

### Laszlo Juhasz, 2024-03-15

After running multiple tests using a PTC fuse for constant temperature control of the PITOT tube I’ve came to the following conclusion. The PTC fuse will have a few milliOhms resistance at the beginning of the operation. If there is a proper and very tied thermal tie to the heated tube then the tube has to reach about 100C to trip the PTC and it will increase it’s own resistance to limit the current flow to the heater. As the heated pipe cools off from that high temperature it will stabilize and goes into a self-regulated temperature control about 60C( that is highly depends of the location of the PTC and also thermal conduction between the heated tube and the PTC). The PTC will remain in a tripped state while changing the internal resistance and maintain a steady temperature keeping it’s own temperature around 90C. According to the PTC datasheet it’s not recommended to operate these fuses at this state due to quicker degradation of these components. I’ve noticed that if there is a sudden “stressful” cooling temperature change occurs on the PTC it might suffer permanent damage and became shorted. Therefore, I’m proposing a more controlled and better rated temperature control and also make it more energy efficient for production. The attached sketch is the proposed solution using a thermistor, a buck converter and possibly heat pipes. 
[embedded file]

### Greg Fryer, 2024-08-29

@Ryan Babigian Here’s the project that has most of the info on the ADP. Per discussion, we need to meet with @Grant Goodman and figure out if he has the BW to handle.

### Greg Fryer, 2024-08-29

@Grant Goodman is going to pick this up. He’s going to start with the charter (scope) and requirements so everything we need is to folks. That includes the couple up front “big decisions” on aproach.

### Rajesh Budhabhatti, 2024-10-01

Schematics redline done. Scott S, Greg to decide on connectors. Per Scott, the enclosure is best handled in-house rather than have the vendor (tree town) make it. Once the connector is decided upon, we will have new harnesses drawings to match.

### Christa Meck, 2025-04-08

@Grant Goodman Can we get an updated Due Date and a review on children + linked tickets?  If this is needed for March LRR there is an incredible amount of work here that I don’t know is being tracked.

### Trevor Gronner, 2025-09-11

@Grant Goodman Can we close out this ticket? Or at least some of the subtasks?

### Laszlo Juhasz, 2023-01-11

I was searching for a possible environment chamber for testing, and this is something would be helpful: https://www.ebay.com/itm/334459630745?_trkparms=amclksrc%3DITM%26aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D245022%26meid%3De04ec15a0483497f90eaa5d03b23dad9%26pid%3D101195%26rk%3D5%26rkt%3D12%26sd%3D125406633692%26itm%3D334459630745%26pmt%3D1%26noa%3D0%26pg%3D2047675%26algv%3DSimplAMLv11WebTrimmedV3MskuWithRevOptLambda90KnnRecallV1&_trksid=p2047675.c101195.m1851&amdata=cksum%3A334459630745e04ec15a0483497f90eaa5d03b23dad9%7Cenc%3AAQAHAAABEPZqctS1aW2Gn1fMafrLrPa7%252BqLD2Pgo5GTgCDTJgIpBMBHaBHcFvdVGNBWeIytK8U7x8RargP9Bv5VZgW5ZIFM%252BxhVgQC3Veb7RyrrkICAJSs%252BM%252F2KjFJS5R%252F1ROIKKthCN65chtifdhiS%252B06N5kKIpL1ZC0uQVldJcUhvMDKBgPgFKzt%252FevUuLtnUPAzCdKf6nc3aRBgpQYMgbcNl7LqCfPXa0kCvtf%252FM9am2FloC74sciX7VlSCtHMA2x8gp%252Bg6RWgQxUKuWOIp%252ByQST12KBcJy5Ud71KwJMGbiFDQSDRJumz6HDPR87LgIkfjJcOIRwxwdyoFEryrMe1zTjoCnqZUboaSQbyx%252BYYJhj7214U%7Campid%3APL_CLK%7Cclp%3A2047675

### Laszlo Juhasz, 2023-01-17

@Cameron Chapman @Jack Waeschle The test for the proof of concept was conducted and the results are promising. The pitot tube and the drain plate heating were tested @-10C° ambient and @ 20C° room for reference. The results are attached:
[embedded file]
[embedded file]
[embedded file]
[embedded file]
[embedded file]
 
[embedded file]
The amount of the current drawn by the camera is 165mA, two small round heaters series 560mA, pitot tube heater pad 1560mA @ 12.5V

### Cameron Chapman, 2023-01-23

Here is the current limiting circuit. 
[embedded file]

### Cameron Chapman, 2023-01-23

Lawton to check ironbird avionics box for any signs of damage/overloading U5 converter.

### Greg Fryer, 2024-02-02

Linked in the SA Camera project, which likely should be changed to a problem, content incorporated, and then closed as duplicate. However, that can only happen if we have enough SA cameras left to keep production going until we have a whole new ADP.
@Eric Rinell looked at the proposed replacement from the company we tried to by Qty 500 (“lifetime buy”), and it does not remotely fit.

### Greg Fryer, 2024-02-25

@Cameron Chapman @Rajesh Budhabhatti I took the liberty of re-assigning this to Raj. I just found an email in my vacation backlog indicating that LM is trying to drive heated pitot into the baseline TIQUILA scope. I am working with them to negotiate the exact cut-in (ideally to a future phase), but it does indicate that we should shift the focus from the SA Camera (now resolved - or postponed to at least 2025) and instead drive to a revision to the VXE-30 Air Data Pod to incorporate the heated pitot. Note that @Eric Rinell has done initial mechanical design, so has a heater element we can electrically evaluate.
Please be sure this goes through our design process, and we will need a project plan for it (schedule). We should also evaluate obsolescence, but err strongly towards lifetime buys vs. actual design out (if possible). Given that our business plan is to move to Havoc, which will have a new ADP, that is where full de-obsolescence should reside. (And additional improvements, such as CAN and more robust software/microcontroller design. And EMI.

### Rajesh Budhabhatti, 2024-02-26

I believe Lazlo has done some preliminary testing with pitot tube heating using both 5V and 12V. I will work with Eric to see if there is any mechanical issues to be considered. I also believe Lazlo is out until Friday so I will get on this issue.

### Cameron Chapman, 2024-02-26

@Rajesh Budhabhatti please tag up with me for a kickoff. We will start with requirements and evaluating the trade offs of different options. 
@Greg Fryer let me know when you have a better idea of due date.

### Cameron Chapman, 2024-02-26

[embedded file]

### Rajesh Budhabhatti, 2024-02-26

Will do. Thanks

### Greg Fryer, 2024-02-27

@Cameron Chapman @Rajesh Budhabhatti Apologies for us getting jerked around. Just got a deadline from Sam that we need a PDR and the balance of the plan by 3/29. This is VXE30 only, and so we should limit the scope strictly to heated pitot since the SA cam is addressed by the lifetime buy.
Guess at due date remains the same (late Jun/Jul with MCMAGNSS updates).
Please invite me to the kickoff, so I can answer any context shortages. Also add @Eric Rinell since he already crafted some mechanical design and the actual metal pitot and a notional heating element - obviously needs to get through concept review to make sure it’s all coherent.

### Eric Rinell, 2024-02-27

@Greg Fryer Need requirement definition on heating the static side. Is it included in this scope of work, or will pitot heat be sufficient?

### Cameron Chapman, 2024-02-27

@Eric Rinell Greg said yes, need heated static as well.

### Cameron Chapman, 2024-03-04

Moving old project order to comments. See epics now. 
Heated pitot project order.
- Define and capture requirements.
- Do we have a temperature, humidity, snowfall, or other related requirement?
- Is the requirement just to add a reasonable amount of heating with limited scope?
- Do we want/need switchable, or could switching on automatically based on temperature be acceptable?
- Outline schedule in confluence. https://jenaero.atlassian.net/wiki/spaces/PDAO/pages/163643414/Air+Data+Pod+Updates+Heated+Pitot+Initial+and+Havoc
- Evaluate main options. Will they provide enough power and not add unacceptable risk to the aircraft? 
- Share power with SA CAM. SW limit is ~0.85A with SA cam taking ~0.15A. Have not quantified max current available if SW limit was disabled. Power supply is limited to 5A, but does not have enough heat sinking to support that. 
- Previous testing indicated <3.5A continuous among all 12V supply. (we do not want to limit power available to 12V payloads with this design). Trillium already uses a lot of the capacity.
- See attached POWER TREE, B25+VTOL2.SchDoc
- Share power with ADP and VTOL AP (this seems like a bad idea).
- New harness to connect more power to ADP (does not seem in scope).

### Laszlo Juhasz, 2024-03-06

As a reminder from the prototype development, using a thermostat resulted very dynamic ripple effect on the power source and over current was detected by the SW. I’ve had conducted a proof-of-concept test using a PTC fuse replacing the thermostat and avoiding such problem. I’m sharing a document explaining the result and comparing the two-temperature controlling technics.
[embedded file]

### Rajesh Budhabhatti, 2024-03-06

Eric has a machined pitot tube ready for testing. He will deliver it to us when the heater element arrives so we can conduct power and temperature testing.

### Cameron Chapman, 2024-03-07

@Eric Rinell @Rajesh Budhabhatti @Jack Waeschle There is a large risk that we will not be able to provide that much power to the heated pitot without cutting into the 12V payload budget (required for Trillium payloads). This is why the power capacity test is high priority. We should also evaluate options for if we do not have that much power available (purchase higher resistance/lower power heaters)

### Rajesh Budhabhatti, 2024-03-08

Agreed. That is why I am thinking of making a mathematical model for pitot tube and correlate our findings from the testing Mark and I did on Wednesday. For our testing yesterday, we used a 12 Ohm heater and limited current to 1 amp. I will have more data and strategy to share by end of day today.

### Laszlo Juhasz, 2024-03-15

After running multiple tests using a PTC fuse for constant temperature control of the PITOT tube I’ve came to the following conclusion. The PTC fuse will have a few milliOhms resistance at the beginning of the operation. If there is a proper and very tied thermal tie to the heated tube then the tube has to reach about 100C to trip the PTC and it will increase it’s own resistance to limit the current flow to the heater. As the heated pipe cools off from that high temperature it will stabilize and goes into a self-regulated temperature control about 60C( that is highly depends of the location of the PTC and also thermal conduction between the heated tube and the PTC). The PTC will remain in a tripped state while changing the internal resistance and maintain a steady temperature keeping it’s own temperature around 90C. According to the PTC datasheet it’s not recommended to operate these fuses at this state due to quicker degradation of these components. I’ve noticed that if there is a sudden “stressful” cooling temperature change occurs on the PTC it might suffer permanent damage and became shorted. Therefore, I’m proposing a more controlled and better rated temperature control and also make it more energy efficient for production. The attached sketch is the proposed solution using a thermistor, a buck converter and possibly heat pipes. 
[embedded file]

### Greg Fryer, 2024-08-29

@Ryan Babigian Here’s the project that has most of the info on the ADP. Per discussion, we need to meet with @Grant Goodman and figure out if he has the BW to handle.

### Greg Fryer, 2024-08-29

@Grant Goodman is going to pick this up. He’s going to start with the charter (scope) and requirements so everything we need is to folks. That includes the couple up front “big decisions” on aproach.

### Rajesh Budhabhatti, 2024-10-01

Schematics redline done. Scott S, Greg to decide on connectors. Per Scott, the enclosure is best handled in-house rather than have the vendor (tree town) make it. Once the connector is decided upon, we will have new harnesses drawings to match.

### Christa Meck, 2025-04-08

@Grant Goodman Can we get an updated Due Date and a review on children + linked tickets?  If this is needed for March LRR there is an incredible amount of work here that I don’t know is being tracked.

### Trevor Gronner, 2025-09-11

@Grant Goodman Can we close out this ticket? Or at least some of the subtasks?

## Attachments (21)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [1910P01.PDF](attachments/11862_1910P01.PDF.md) | pdf | 316 | 2023-01-05 | converted |
| Heating Pad.jpg | image | 192 | 2023-01-06 | listed only |
| image-20230106-233527.png | image | 28 | 2023-01-06 | listed only |
| image-20230109-235357.png | image | 53 | 2023-01-09 | listed only |
| CAD electronics height.PNG | image | 349 | 2023-01-10 | listed only |
| CAD electronics space.PNG | image | 303 | 2023-01-10 | listed only |
| CAD electronics width.PNG | image | 215 | 2023-01-10 | listed only |
| Potential space for heated pitot electronics.PNG | image | 486 | 2023-01-10 | listed only |
| Temp sensors.PNG | image | 176 | 2023-01-10 | listed only |
| cc0f2fd6-9dbc-48dd-842d-d6cbca2e65da | other | 80 | 2023-01-10 | listed only |
| Chamber_DrainPlate_Referenced.jpg | image | 2042 | 2023-01-17 | listed only |
| Drain_Plate_Install.jpg | image | 618 | 2023-01-17 | listed only |
| Heater Installation.jpg | image | 387 | 2023-01-17 | listed only |
| SCH.jpg | image | 288 | 2023-01-17 | listed only |
| Tube Install.jpg | image | 1166 | 2023-01-17 | listed only |
| Tube_ends_referenced.jpg | image | 2191 | 2023-01-17 | listed only |
| image-20230123-225338.png | image | 123 | 2023-01-23 | listed only |
| image-20240226-182513.png | image | 129 | 2024-02-26 | listed only |
| [Heated Pitot Tube Review process.docx](attachments/18993_Heated%20Pitot%20Tube%20Review%20process.docx.md) | docx | 18 | 2024-02-27 | converted |
| [Thermostat_vs_PTC.docx](attachments/19260_Thermostat_vs_PTC.docx.md) | docx | 2258 | 2024-03-06 | converted |
| Buck Converter Used.jpg | image | 2784 | 2024-03-15 | listed only |
