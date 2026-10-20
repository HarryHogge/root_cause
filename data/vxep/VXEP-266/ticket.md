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
- **Project Tier:** Tier 2
- **Planned Milestone(s):** Preliminary Design Review (PDR), Detailed Design/Critical Design Review (CDR), Production Readiness Review (PRR)
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

### Cameron Chapman, 2023-01-05

Jack estimates 12.5W required.
In either case, I think we should integrate a thermal shutoff board, like the one we use for the SA cam. If we used that exact board, we should be able to solder wires to the thermistor pads, then locate the thermistor wherever needed. Need to check board current ratings. 
It seems like there are two main options.
- Power heaters internally from custom ADP harness, likely splicing into the SA CAM lines.
- Seems like the best option.
- Can only switch on and off by also switching SA CAM on/off. (unless we added additional circuitry).
- Looks best, no external wiring.
- I calculate up to 42W available on those wires, so we should have plenty (limited by the XCOM converter temp, so we should aim for much less. 12.5W should be ok. We will test).
- Add external harness from mod payload port to ADP.
- Easiest.
- Uglier, having to tape cable to the fuselage and wing after connection both.
- Can be switched on and off.
- More power available.

@Jack Waeschle @Greg Fryer @Connor Peebles @Former user @Kurt Burian @Sam Miller 
[embedded: 1910P01.PDF]

### Former user, 2023-01-05

@Cameron Chapman thanks for summarizing.  i believe we can run the wiring through the channel in the wing so it doesn’t have to be entirely external if we want to use the aux port.  we will have some sections that need to be external/taped, however.
I like the idea of splicing into the ADP lines if possible 🙂

### Kurt Burian, 2023-01-05

@Cameron Chapman There is no way to switch the sa cam on and off. SA-CAM would just provide ethernet. There is CAN available up there for the air data pod. Automatic solution makes more sense then autopilot/xcomm control thus avoiding communication.

### Kurt Burian, 2023-01-05

@Cameron Chapman Also make sure we power from the camera power supply not the airdata. Sounds like that's the plan if I’m reading right since you need 12V, but just want to be sure. We can afford to loose camera, but not airdata if the heater shorts.

### Cameron Chapman, 2023-01-05

@Kurt Burian , yes. The plan/calculations below were to splice into the camera power lines. I think the Q5 SA CAM FET on the XCOM port can be switched off from a webpage. Maybe not, but in any case, we would not want anyone doing this during a flight. 
Yes, for the rapid prototype automating seems much more feasible than adding control communication (only need power wires).

### Cameron Chapman, 2023-01-05

@Jack Waeschle If we use thermal shutoff board, we will be right on the edge of the current rating. DF13 contacts and NTR1P02T1G rated to 1A. 12.8V*1A=12.8W. Est 12.5W required. May be ok. Need to test. Less power would be better. 
@Laszlo Juhasz , can you please do the following. This should be top priority given the due date. We can meet to discuss.
- Measure SA cam current at 12.8V in.
- Run 1A 12.8V through thermal shutoff board. Record IR image of both sides.
- Coordinate heater on and off setpoints with Jack.
- Build prototype 1910P01B board with wires from RT1 pads to remote RT1. Start with ~6” wires. Kapton tape over RT1 acceptable for prototype. Verify shutoff points calculated in 3.
- We should identify another way to cover RT1 conductors that is more thermally conductive than kapton and can bond to desired location.

### Laszlo Juhasz, 2023-01-06

Since the recently used P-CH MosFet (NTR1P02T1G) is rated only for 1A, I’ve ordered overnight 50pcs of the https://www.digikey.com/en/products/detail/BSH205G2R/1727-2247-1-ND/5395549?curr=usd 20V 2A P-CH MosFets (package/pin compatible) needed to switch the heating resistor ON/OFF. 
[embedded: Heating Pad.jpg]

### Laszlo Juhasz, 2023-01-06

[embedded: image-20230106-233527.png]
Three low currents rated PTC fuses are requested by overnight order.

### Cameron Chapman, 2023-01-09

Hi @Laszlo Juhasz , there seems to have been a misunderstanding. We want the fuses to trip based on temperature, not current. One of the heaters requires 12.5W ~1A at 12.8V in, so a fuse 1A or less is too low. 
I think you want something more like a thermostat or thermal switch. Something small so it can be located on the probe. Please order ASAP to meet project schedule. 
https://www.digikey.com/en/products/filter/temperature-sensors-thermostats-mechanical/516?s=N4IgTCBcDaIC4AsCmAnAtgQwDYAIDOA7gJZwDGCIAugL5A

### Cameron Chapman, 2023-01-09

@Laszlo Juhasz , [2:45 PM] Jack Waeschle
 
The adhesive fails at 120C

[2:45 PM] Cameron Chapman
What is target temp?

[2:48 PM] Jack Waeschle
We don't actually know what temp is required to melt the mass flow rate of snow. My flowsim predicts that 12.5W would have a steady state temp of 80F, I'm skeptical of that number until it is validated by experimental testing.

[2:48 PM] Jack Waeschle
We could target 130F

### Cameron Chapman, 2023-01-09

@Jack Waeschle would any of these fit in the desired locations? We’d like to order ASAP if so. 
SMD -may need 2 in parallel for the pitot. 66L070-0516
Screw mount B12A07505AEDA0GE
[embedded: image-20230109-235357.png]
https://www.digikey.com/en/products/detail/cantherm/B12A07505AEDA0GE/1840429
https://www.digikey.com/en/products/detail/sensata-airpax/66L070-0516/5081896

### Cameron Chapman, 2023-01-09

SMD below is 100 MOQ. This would work better 66L075-0349

### Cameron Chapman, 2023-01-09

Planning to order 10x of these 66L075-0349  8x of these B12A07505AEDA0GE

### Jack Waeschle, 2023-01-10

@Cameron Chapman, since we’re out of the office today I’m just using the CAD assembly for reference that doesn’t model the wiring. Within the CAD model there is plenty of room for those. We will have to verify once they arrive.

### Jack Waeschle, 2023-01-10

[embedded: CAD electronics width.PNG]
[embedded: CAD electronics height.PNG]
[embedded: CAD electronics space.PNG]
[embedded: Potential space for heated pitot electronics.PNG]
@Cameron Chapman I took a look at the procedure and it appears the ADP doesn’t have any wires in the area immediately behind the static probe, and this should be sufficient space.

### Cameron Chapman, 2023-01-10

@Jack Waeschle thanks for the fit check. Those sensor types would have to be placed where we want to sense the heat. Could they fit in those spots?

### Jack Waeschle, 2023-01-10

@Cameron Chapman which part of the sensor needs to be in contact with the surface of interest? If it's the yellow highlighted part, that could easily be slipped under the heater at the base of the pitot, and under the donut. If the entire unit/flat face needs to be in contact, that would be possible to shove under the heater but it would cause a big air gap and degrade the performance of the heater. Additionally, only part of the flat face would contact the curved surface of the pitot.
[embedded: Temp sensors.PNG]
For reference, the OD of the pitot tube is 1/2 inch or 12.7 mm.

### Laszlo Juhasz, 2023-01-10

The highlighted ear is a slot for screw.  This particular shaped designed to install on a flat surface by a screw but for testing that can be removed and use a tape.
________________________________
From: Jack Waeschle (Jira) <jira@jenaero.atlassian.net>
Sent: Tuesday, January 10, 2023 4:35 PM
To: Laszlo Juhasz <ljuhasz@edgeautonomy.io>
Subject: [JIRA] (https://jira-prod-us-18-4.prod.atl-paas.net/browse/ENGPRJ-319#icft=ENGPRJ-319) Electrical design
Jack Waeschle added 1 new comment and edited 1 comment. Eng. Projects (New or Simple)/https://jira-prod-us-18-4.prod.atl-paas.net/browse/ENGPRJ-319#icft=ENGPRJ-319 Electrical design  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌
Jack Waeschle added 1 new comment and edited 1 comment.
Eng. Projects (New or Simple)<https://jenaero.atlassian.net/browse/ENGPRJ?atlOrigin=eyJpIjoiYWM3MjVkMjAyNmM2NDRiOWI4MjI4NDIzNzRjMDRlYTIiLCJwIjoiaiJ9>
/
ENGPRJ-319<https://jenaero.atlassian.net/browse/ENGPRJ-319?atlOrigin=eyJpIjoiYWM3MjVkMjAyNmM2NDRiOWI4MjI4NDIzNzRjMDRlYTIiLCJwIjoiaiJ9>
Electrical design <https://jenaero.atlassian.net/browse/ENGPRJ-319?atlOrigin=eyJpIjoiYWM3MjVkMjAyNmM2NDRiOWI4MjI4NDIzNzRjMDRlYTIiLCJwIjoiaiJ9>
https://secure.gravatar.com/avatar/95d9a0bbf8744ee9598a9d75b796e73e?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FJW-4.png       Jack Waeschle 4:30 PM PST
@Cameron Chapman which part of the sensor needs to be in contact with the surface of interest? If it's the yellow highlighted part, that could easily be slipped under the heater at the base of the pitot, and under the donut. If the entire unit/flat face needs to be in contact, that would be possible to shove under the heater but it would cause a big air gap and degrade the performance of the heater. Additionally, only part of the flat face would contact the curved surface of the pitot.
[cid:cc0f2fd6-9dbc-48dd-842d-d6cbca2e65da]
https://secure.gravatar.com/avatar/95d9a0bbf8744ee9598a9d75b796e73e?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FJW-4.png       Jack Waeschle 4:32 PM PST edited
@Cameron Chapman which part of the sensor needs to be in contact with the surface of interest? If it's the yellow highlighted part, that could easily be slipped under the heater at the base of the pitot, and under the donut. If the entire unit/flat face needs to be in contact, that would be possible to shove under the heater but it would cause a big air gap and degrade the performance of the heater. Additionally, only part of the flat face would contact the curved surface of the pitot.
[cid:cc0f2fd6-9dbc-48dd-842d-d6cbca2e65da]
For reference, the OD of the pitot tube is 1/2 inch or 12.7 mm.
View issue<https://jenaero.atlassian.net/browse/ENGPRJ-319?atlOrigin=eyJpIjoiYWM3MjVkMjAyNmM2NDRiOWI4MjI4NDIzNzRjMDRlYTIiLCJwIjoiaiJ9>
Get Jira notifications on your phone! Download the Jira Cloud app for Android<https://play.google.com/store/apps/details?id=com.atlassian.android.jira.core&referrer=utm_source%3DNotificationLink%26utm_medium%3DEmail> or iOS<https://itunes.apple.com/app/apple-store/id1006972087?pt=696495&ct=EmailNotificationLink&mt=8>.
Manage notifications<https://jenaero.atlassian.net/secure/ViewPersonalSettings.jspa#emailpreferences>  •  Give feedback<https://surveys.atlassian.com/jfe/form/SV_9X3zi1X4q1gKsqF>  •  Privacy policy<https://www.atlassian.com/legal/privacy-policy>
[cid:atl-generated-5eee53ce-0890-4c07-b90c-91825c41928a]
[cid:atl-generated-5eee53ce-0890-4c07-b90c-91825c41928a]
- - WARNING: This email originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe. **

### Cameron Chapman, 2023-01-11

@Jack Waeschle , could the sensor bond to the outside of the heater, or would that risk getting too hot on the inside? We can test/order lower temp cutoffs if needed.

### Jack Waeschle, 2023-01-11

It should work on the outside, as long as it has adequate contact. Since it is a flat sensor, my main concern would be part of the sensor being exposed to the cold air rushing by and convective cooling making the reading from the sensor lower than the temperature of the heater.

### Laszlo Juhasz, 2023-01-11

I was searching for a possible environment chamber for testing, and this is something would be helpful: https://www.ebay.com/itm/334459630745?_trkparms=amclksrc%3DITM%26aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D245022%26meid%3De04ec15a0483497f90eaa5d03b23dad9%26pid%3D101195%26rk%3D5%26rkt%3D12%26sd%3D125406633692%26itm%3D334459630745%26pmt%3D1%26noa%3D0%26pg%3D2047675%26algv%3DSimplAMLv11WebTrimmedV3MskuWithRevOptLambda90KnnRecallV1&_trksid=p2047675.c101195.m1851&amdata=cksum%3A334459630745e04ec15a0483497f90eaa5d03b23dad9%7Cenc%3AAQAHAAABEPZqctS1aW2Gn1fMafrLrPa7%252BqLD2Pgo5GTgCDTJgIpBMBHaBHcFvdVGNBWeIytK8U7x8RargP9Bv5VZgW5ZIFM%252BxhVgQC3Veb7RyrrkICAJSs%252BM%252F2KjFJS5R%252F1ROIKKthCN65chtifdhiS%252B06N5kKIpL1ZC0uQVldJcUhvMDKBgPgFKzt%252FevUuLtnUPAzCdKf6nc3aRBgpQYMgbcNl7LqCfPXa0kCvtf%252FM9am2FloC74sciX7VlSCtHMA2x8gp%252Bg6RWgQxUKuWOIp%252ByQST12KBcJy5Ud71KwJMGbiFDQSDRJumz6HDPR87LgIkfjJcOIRwxwdyoFEryrMe1zTjoCnqZUboaSQbyx%252BYYJhj7214U%7Campid%3APL_CLK%7Cclp%3A2047675

### Laszlo Juhasz, 2023-01-17

@Cameron Chapman @Jack Waeschle The test for the proof of concept was conducted and the results are promising. The pitot tube and the drain plate heating were tested @-10C° ambient and @ 20C° room for reference. The results are attached:
[embedded: Chamber_DrainPlate_Referenced.jpg]
[embedded: Tube_ends_referenced.jpg]
[embedded: Drain_Plate_Install.jpg]
[embedded: Heater Installation.jpg]
[embedded: Tube Install.jpg]
 
[embedded: SCH.jpg]
The amount of the current drawn by the camera is 165mA, two small round heaters series 560mA, pitot tube heater pad 1560mA @ 12.5V

### Cameron Chapman, 2023-01-23

Here is the current limiting circuit. 
[embedded: image-20230123-225338.png]

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

[embedded: image-20240226-182513.png]

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
[embedded: Thermostat_vs_PTC.docx]

### Rajesh Budhabhatti, 2024-03-06

Eric has a machined pitot tube ready for testing. He will deliver it to us when the heater element arrives so we can conduct power and temperature testing.

### Cameron Chapman, 2024-03-07

@Eric Rinell @Rajesh Budhabhatti @Jack Waeschle There is a large risk that we will not be able to provide that much power to the heated pitot without cutting into the 12V payload budget (required for Trillium payloads). This is why the power capacity test is high priority. We should also evaluate options for if we do not have that much power available (purchase higher resistance/lower power heaters)

### Rajesh Budhabhatti, 2024-03-08

Agreed. That is why I am thinking of making a mathematical model for pitot tube and correlate our findings from the testing Mark and I did on Wednesday. For our testing yesterday, we used a 12 Ohm heater and limited current to 1 amp. I will have more data and strategy to share by end of day today.

### Laszlo Juhasz, 2024-03-15

After running multiple tests using a PTC fuse for constant temperature control of the PITOT tube I’ve came to the following conclusion. The PTC fuse will have a few milliOhms resistance at the beginning of the operation. If there is a proper and very tied thermal tie to the heated tube then the tube has to reach about 100C to trip the PTC and it will increase it’s own resistance to limit the current flow to the heater. As the heated pipe cools off from that high temperature it will stabilize and goes into a self-regulated temperature control about 60C( that is highly depends of the location of the PTC and also thermal conduction between the heated tube and the PTC). The PTC will remain in a tripped state while changing the internal resistance and maintain a steady temperature keeping it’s own temperature around 90C. According to the PTC datasheet it’s not recommended to operate these fuses at this state due to quicker degradation of these components. I’ve noticed that if there is a sudden “stressful” cooling temperature change occurs on the PTC it might suffer permanent damage and became shorted. Therefore, I’m proposing a more controlled and better rated temperature control and also make it more energy efficient for production. The attached sketch is the proposed solution using a thermistor, a buck converter and possibly heat pipes. 
[embedded: Buck Converter Used.jpg]

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
