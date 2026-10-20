# VXEP-813: E140 Octopus/VXE30 Isolation Issues: Arcing to Fuselage, mag interference suspected

- **Issue type:** Incident (8D)
- **Status:** Waiting
- **Priority:** Highest
- **Created:** 2024-12-06
- **Updated:** 2026-02-07
- **Reporter:** Mike DeJesus
- **Assignee:** John Gober
- **Creator:** Mike DeJesus
- **Labels:** Edge_Asset
- **Parent:** ENG-3673 Link for Gimbal Payloads
- **Links:** relates to FS2-2604 (Aircraft departed plan unintentionally); relates to FS2-2605 (Aircraft indication flying opposite tracked direction); relates to FS2-2606 (Crazy landing plan behavior ); relates to VXEP-500 (VXE 674 E140ZG2 gimbals interfere with magnetometer.); relates to VXEP-897 (VXE-674 Auto abort on launch IMU failure message displayed); relates to JA-174 (Work with IT on these); relates to VXEP-1034 (VXE 734 Smoking Gimbal); relates to ENG-2816 ((Payload IPT) Field Support Kit (FSK) Development and Delivery for Octopus Gimbals); relates to ENG-3669 (Link for Gimbal Payloads)
- **Problem Type:** Discovered Issue
- **Root Cause:** Power return pins seem common with gimbal housing (not ideal, common cause of ground loops)
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround
- **LRR Desired Delivery Date:** 2025-02-01
- **LRR Required Delivery Date:** 2025-03-01
- **Product/Tech Owner:** Charles David Madewell
- **Program (Marquee):** Gimbal Payloads
- **Job Number:** J100129 - VXE Gimbal & Payload Support & Sustainment

## Description

Files: VXEP-813 E140 Octopus VXE30 mag interference suspected Mount Ground Loop
Data and Findings spreadsheet: VXEP-813 E140 Octopus VXE30 mag interference suspected Mount Ground Loop
link to the in-depth MAGNSS Mag testing Test-plan and data format: MAGNSS MAG Testing.xlsx
Summary
During several demos and customer flights the issues below have been reported from operators and customers. Upon initial investigation by the GS team it appears that a GND Loop in the VXE30 E140Z G2 mount (P/N: 017.43_C3) is contributing to the issues.

- Magnetometer interference during flight that may cause degradation of control
- Pan/Tilt Encoder Error: It appears that the GND Loop may cause an issue with the Octopus E140Z G2 on initialization that causes loss of control

Report from Sam Miller at Wolf Valkyrie (Alaska Demo)
- Unfortunately, aircraft 499 was plagued with magnetometer and gimbal issues. The first flight experienced only minor magnetometer issues with the first gimbal S/N6219, which features the prototype-grown plastic mount. However, that gimbal experienced issues in the air with lots of resets required. We suspect that the cable may be flaky due to prior damage related to inflexibility in cold weather, so we landed the aircraft to swap out the gimbal.
- After swapping to gimbal SN 6086, which features the new metal mount, we experienced significant magnetometer issues that delayed the launch by an hour. Later in the flight, the INS got very confused, leading to a loss of navigational control and very high bank angles when we RTB’d and entered the landing pattern. We considered landing immediately but had no visual but the position lights and limited comms to the PIC to attempt to guide remotely. Re-tasking the aircraft to an orbit in dash seemed to help stabilize the INS.
- Engineering should investigate root cause of the magnetometer issue: whether the gimbal with a metal mount creates a ground loop to the ground of the airframe chassis and whether there are any fuel cell to chassis-related ground loop issues. In the past, we saw similar magnetometer issues from the fuel cell shorting against the carbon airframe.

Global Support - Initial Troubleshooting and Investigation
After discussing the issues with Sam the Global Support FSRs were tasked with conducting an initial investigation to attempt to collect details on the suspected issues. 
- Initial multimeter readings without power found no voltage between chasis of VXE30 E140Z G2 mount and VXE30 chasis
- Applying power (prior to XCOMM initialization) multimeter readings of 25.55v
- After XCOMM Initialization multimeter readings of .78v
- Check the GND between the Gimbal and the Aircraft the multimeter reads .25v

## Corrective Action

- This project aims to add isolation that helps prevent this issue. https://jenaero.atlassian.net/wiki/spaces/SEIT/pages/edit-v2/863830129?
- Non-conductive mounting plates (link to that project or list when it was implemented and containment status).

## Plan

1/10
- John to transfer findings to excel sheet and maybe fishbone. Discuss with Cam.
- Plan for additional aircraft tests to recreate and test resolutions.
- Evaluate options for breaking conductive path to gimbal housing.
- Create subtasks for other problems encountered.


- Engineering should investigate root cause of the magnetometer issue: whether the gimbal with a metal mount creates a ground loop to the ground of the airframe chassis and whether there are any fuel cell to chassis-related ground loop issues. In the past, we saw similar magnetometer issues from the fuel cell shorting against the carbon airframe.

- @John Gober Gather data to quantify is this issue is systemic or worse with specific gimbals and aircraft.
- For setups where the issue exists, measure resistance between gimbal and aircraft structure, or other relevant points (with harness connected and not).
- testing combinations of the following and quantifying mag interference.
- gimbal powered vs unpowered
- Connected or not
- Mounted vs unmounted and adjacent.
- Rotating vs stationary vs Stalled
- Manually grounding gimbal to fuselage with a jumper wire.
- Summarize findings and recommended next steps.
- Potential improvements:
- Ensure path from gimbal housing to aircraft is not conductive (Ex: different plate, mount, mounting hardware, etc.)

## Issue Status

25 FEB 25 Further testing on hold until an aircraft is made available.  GS / FLOPS currently TDY with all HSV assets for five weeks.
Latest findings. 
| Test # | Aircraft | Gimbal | Mount | Plate | Mount Conducts | Notes |
| 1 | 734 | 6172 | Aluminum | Carbon | Yes | Confirmed GS observations from their initial testing Tilt encoder fault, stray voltage between gimbal and aircraft |
| 2 | 734 | 6172 | Aluminum | Carbon | Yes | More stray voltages; detected 32 mA current flowing from gimbal to plane |
| 3 | 734 | 6086 | Aluminum | Carbon | Yes | Gimbal passed BIT; reported no errors; does not respond to operator |
| 4 | None | 6172 | Aluminum | Carbon | Yes | Not probative - SSR in payload harness blocking ground through Alden See tests repeated without harness in Tests 6 and 8 |
| 5 | 674 | 6172 | 3D Printed | G10 | No | Successful BIT on gimbal, Mag Check Good |
| 6 | None | 6172 | None | None | N/A | Resistance from ground pin to gimbal base is 3.5 to 4 Ohms |
| 7 | 734 | None | None | None | N/A | Posible return (ground) path through Silvus |
| 8 | None | 6182 | 3D Printed | None | N/A | Confirmed gimbal GND is tied to housing |
| 9 | 734 | 6182 | 3D Printed | Carbon | No | Successful BIT on gimbal, Mag Check Good |

Testing Details: Testing
Spreadsheet Summary: VXEP-813 + 1034 E140 Octopus VXE30 mag interference suspected Mount Ground Loop.xlsx

 Power return pins seem common with gimbal housing (not ideal, common cause of ground loops)_

Incident Reports > VXEP-813 > Testing
Mike DeJesus worked the investigation from the Global Support perspective.  He has had multiple units report this issue.  His initial thought is that the paint is coming off the mount plate and making an electrical ground to the vehicle.  This is due to the mount being fabricated from a metal.  His initial report is above under the Global Support heading.

## Comments (16)

### David Grosher, 2024-12-06

@Eric Brewer FYSA

### Greg Fryer, 2024-12-06

@Charles David Madewell I don’t think we’ve discussed the incident tracking/routing/updates yet, but this is how we record our RCCA findings (in reportable-to-the-customer form). I think you are already working this, so we just need to status appropriately to support customer feedback.

### Mike DeJesus, 2024-12-09

@Aleksandrs Checking to see if Aleksandrs Guks has access.

### Greg Fryer, 2024-12-10

For the record, Aleksandrs does not because this issue is set to Edge US. We’d need to move it out of that (click the padlock icon at the upper right). I asked @Christa Meck to verify all our other settings are right before we let Riga back in (hasn’t been a priority is all). Would need the owner to scrub and make sure nothing export controlled slips in via photo or comment. Shouldn’t be an issue, since there’s no relationship to the various export controlled topics.

### Pat Wells, 2024-12-17

@Greg Fryer @Cameron Chapman is there nothing we can do from the VXE30 side to look into this issue?  I don’t believe RIga can add much until we determine what’s happening with the aircraft.

FYSA @Mike DeJesus

### Cameron Chapman, 2024-12-17

@Pat Wells @Greg Fryer @John Gober @Charles David Madewell @Mike DeJesus yes, we were initially hoping Riga could do it, since I think they had an aircraft in the familiarity and ability to disassemble the gimbal. For testing in Huntsville or Slo I would recommend testing combinations of the following and quantifying  mag interference. 
- gimbal powered vs unpowered
- Connected or not
- Mounted vs unmounted and adjacent.
- Rotating vs stationary vs Stalled
- Manually grounding gimbal to fuselage with a jumper wire.

### Mike DeJesus, 2024-12-17

@Greg Fryer It doesnt look like I can change the padlock settings, not sure why.

### Cameron Chapman, 2024-12-18

Related conversation: 
rom: Abel Markow amarkow@edgeautonomy.io
Sent: Wednesday, December 18, 2024 11:31 AM
To: Wesley Lilienthal wlilienthal@edgeautonomy.io; Dmitrijs Palamarčuks dpalamarcuks@edgeautonomy.eu; Cameron Chapman cchapman@edgeautonomy.io; Connor Peebles cpeebles@edgeautonomy.io
Cc: Žilvinas Vinskas zvinskas@edgeautonomy.eu; Aleksandrs Guks aguks@edgeautonomy.eu; Herberts Stāmers hstamers@edgeautonomy.eu
Subject: Re: About EMI
Howdy again Dmitrijs,
It was nice meeting you. 
Some notes from the conversation, and a few other ideas.
The noise appears inductive in nature.  
You have common ground planes due to the VIAS
The 1ohm resistor is isolating the AGRND of the CHIP from the GND of the rest of the circuit which makes the HBRIDGE work.
The PWM output in the diagram of the datasheet never shows two channels high at the same time, and the o-scope capture shows both signals high at the same time.   
The noise lift on channel (2) being tied to the peaks of the current channel (3) appear to show that another feedback device is jumping.   This implies the ground plane is lifting
The UART is a 5v UART
The UART fails when the motor is brought online.
The UART is 5V tolerant (See note on page 13 of hardware integration manual).  They say to buffer the system if you are using a 5v system because it is only putting out 2.6 volts.  That coupled with the ground lifting may make it like 2.4 volts which might not be enough for the controller to see the UART signal.
Some ideas of test cases to help weed out the issue:
Try a level shifter on the UART to move it to 5V.
In the data sheet tech notes there is equation (1).  Make sure we have the correct value for the inductors.
In the data sheet for PVDD they show a 1000uF cap on the power input.  It was not shown on the detailed schematic, may want to find out what that capacitor is, and temporarily add one on the tantalum cap directly above the chip towards the power source.
For the Vecotrnav chip, it appears you have two decoupling / cleanup capacitors.  Their documentation didn't have an implementation circuit.  Recommend reaching out to them for any recommended decoupling capacitors or cleanup caps.
Use a differential probe on the ground plane vs VCC into the Vector NAV chip when the motor is running and see if the VCC moves.
Monitor the enable and reset voltage pins out of the vector nav chip and see if they fall off when the motor spins.  If you see the noise on those pins, you know its coming into the chip, likely through the low side power.  They are pulled to the internal 3v rail on a pull up resistor.  
Try splitting the return path for the motor system away from the grounds of the rest of the board all the way back to the input of the system.  May even put a small resistor in line to force the other ground plane away form the motors
Happy to help more after the new year.   Merry Christmas and Happy New Year.
Abel
From: Wesley Lilienthal wlilienthal@edgeautonomy.io
Sent: Tuesday, December 17, 2024 10:53 PM
To: Dmitrijs Palamarčuks dpalamarcuks@edgeautonomy.eu; Abel Markow amarkow@edgeautonomy.io; Cameron Chapman cchapman@edgeautonomy.io; Connor Peebles cpeebles@edgeautonomy.io
Cc: Žilvinas Vinskas zvinskas@edgeautonomy.eu; Aleksandrs Guks aguks@edgeautonomy.eu; Herberts Stāmers hstamers@edgeautonomy.eu
Subject: Re: About EMI
Hi Dmitrijs,
Thank you for the very comprehensive overview below of the issues you are experiencing and for the visual walkthrough of the PCB design in question just now. Sorry I could not be of more immediate and direct help, but I hope to at least put you in touch with those who might be able to better assist. 
In addition to Abel, allow me to direct you to Cameron Chapman, Electrical Engineering lead, as well as Connor Peebles, Electrical Engineer, both located here in SLO and on Cc in this email. Both Cameron and Connor have significant backgrounds in power and baseband PCB design and may be able to provide you direction on best practices and the most lucrative places to begin looking for root cause. 
Once you are able to get the design in front of Abel, I am hoping he too will be able to devote an expert eye in review of your existing design and advise on potential means to resolve the coexistence issues. 
Cameron and Connor - Would you please review Dmitrijs's description of his coexistence issue below and let him know if you might be able to assist?
Thank you,
- Wes

Outlook-A picture .png
Wesley Lilienthal
Senior Staff RF Engineer
Edge Autonomy – SLO (formerly Jennings Aeronautics)
Email: wlilienthal@edgeautonomy.io
Mobile: (805) 704-5344
From: Dmitrijs Palamarčuks dpalamarcuks@edgeautonomy.eu
Sent: Tuesday, December 17, 2024 4:54 AM
To: Wesley Lilienthal wlilienthal@edgeautonomy.io; Abel Markow amarkow@edgeautonomy.io; Herberts Stāmers hstamers@edgeautonomy.eu
Cc: Žilvinas Vinskas zvinskas@edgeautonomy.eu; Aleksandrs Guks aguks@edgeautonomy.eu
Subject: Re: About EMI
Hi Wesley and Abel,
Early in the morning works for me, but I rely on public transportation, so I suggest 8:15am Latvian time.
Let me introduce you to the problem. We have a gimbal with several PCBs in a daisy chain connection. The first two have a BLDC driver circuit on them. The first driver board has many issues in terms of noise performance. The second driver does not have such problems. The EMI problem is so severe that the internal circuits do not work properly. I'm sharing the Altium 365 links, so you should have access to these designs by now. You can view the designs online or you can download them if you have Altium Designer. If you are having trouble accessing them, I have attached them to this email as well.
E0089A12V16 - Base PCB (older version)
E0089A12V17 - Base PCB (newer version)
E0089A14V06 - Pan PCB
E0067A28V13 - Tilt PCB
E140G3 Designs.zip
Outlook-vpnlqcbl.png
Our BLDC motor control circuit on the Base PCB introduces a lot of noise into the system, which does not allow us to accurately measure the current despite the current sense amplifier's claim of common-mode noise rejection. I don't know how to separate the noisy circuits from the sensitive analog, since I need to measure the currents. We can also realistically separate them by the Z-axis, given how small the area we have. So, the noisy power circuits are at the top and the sensitive analog are at the bottom. We were not able to fully follow the Henry Ott book's guidelines because I had to stick with six layers of copper, and I still have the digital signals on the bottom and no power separation. I also have no idea how to make the Kelvin connection, so I've made a guess that the phases should go to the bottom and then to the top. You will see. The design may be updated in the future with other features such as an Ethernet to UART converter/switch circuit for the Vector Nav module, so we will probably have to go to at least 8 layers.
The Channel 3 is the current measurement.
Outlook-qewreqkf.png
But the bigger problem is that for some reason the Vector Nav module stops working when the H-bridge is in operation. More specifically the UART no longer responds. In my opinion this has something to do not only with the Base PCB motor drivers but also with the fact that it is daisy chain connection, and I have to move the Molex headers that connect the board to the next one close to the main D-Sub connector. The problem goes away when we mount the board to the chassis, and our mounting holes are GND. So, RF bonding helps. But this shouldn't happen in the first place, and relying on the screw connection impedance isn't a good idea either. In any case, my guess is that both problems are of the same nature, and there is something seriously wrong with the grounding/return paths.
There are other unrelated things that I cannot figure out on my own, but I cannot miss a chance to ask someone. For example, the Ethernet transformer eliminates the need for GND, and it is usually suggested to remove it from the underneath. However, this is not possible in this daisy chain connection. What can you suggest to do? Also, the Ethernet transformer on the Tilt PCB is very small and doesn't have a common mode choke, so I'm placing it on the Base PCB. Is this okay to do so?
I recently read the Henry Ott book, but I haven't been able to put the pieces together when designing the three-phase motor driver. So, I'm fairly new to the EMC field and we haven't done any actual testing in terms of common mode noise measurement using LISN or H and E field probe measurements. So we may have to discuss first steps to identify the problem.
Thanks,
Outlook-A picture .png
Dmitrijs Palamarčuks
Electronics Engineer
Edge Autonomy – Riga
Email: dpalamarcuks@edgeautonomy.eu
From: Wesley Lilienthal wlilienthal@edgeautonomy.io
Sent: Monday, December 16, 2024 10:55 PM
To: Abel Markow amarkow@edgeautonomy.io; Herberts Stāmers hstamers@edgeautonomy.eu
Cc: Dmitrijs Palamarčuks dpalamarcuks@edgeautonomy.eu
Subject: Re: About EMI
You don't often get email from wlilienthal@edgeautonomy.io. Learn why this is important
Great, 10:00pm on December 17th PST works for me as well. 
Herberts - How is 8:00am on December 18th Latvia time? 
- Wes

Outlook-A picture .png
Wesley Lilienthal
Senior Staff RF Engineer
Edge Autonomy – SLO (formerly Jennings Aeronautics)
Email: wlilienthal@edgeautonomy.io
Mobile: (805) 704-5344
From: Abel Markow amarkow@edgeautonomy.io
Sent: Friday, December 13, 2024 4:59 PM
To: Wesley Lilienthal wlilienthal@edgeautonomy.io
Cc: Herberts Stāmers hstamers@edgeautonomy.eu; Dmitrijs Palamarčuks dpalamarcuks@edgeautonomy.eu
Subject: Re: About EMI
Tuesday 10 pm is awesome.
Sent from my iPhone
On Dec 13, 2024, at 4:07 PM, Wesley Lilienthal wlilienthal@edgeautonomy.io wrote:
﻿
Abel - They are on Latvia time, which is 10 hours ahead. Perhaps either early morning before 8:00 am PST or in the evening after 10:00 pm PST?
- Wes

Outlook-A picture .png	
Wesley Lilienthal
Senior Staff RF Engineer
Edge Autonomy – SLO (formerly Jennings Aeronautics)
Email: wlilienthal@edgeautonomy.io
Mobile: (805) 704-5344
From: Abel Markow amarkow@edgeautonomy.io
Sent: Friday, December 13, 2024 4:03 PM
To: Wesley Lilienthal wlilienthal@edgeautonomy.io
Cc: Herberts Stāmers hstamers@edgeautonomy.eu; Dmitrijs Palamarčuks dpalamarcuks@edgeautonomy.eu
Subject: Re: About EMI
I’m in Vegas on Monday.  Maybe Tuesday at 10?
Sent from my iPhone
On Dec 13, 2024, at 2:38 PM, Wesley Lilienthal wlilienthal@edgeautonomy.io wrote:
﻿
- Abel

Hi Herberts,
I can certainly discuss and would be happy to help. I would suggest we include our contractor, Abel Markow (added on Cc) as he has been driving our recent grounding, bonding, and shielding efforts and has the most acutely-applicable skillset and experience. 
Perhaps sometime next week? Abel - When are you available?
Thank you, 
- Wes

Outlook-A picture .png	
Wesley Lilienthal
Senior Staff RF Engineer
Edge Autonomy – SLO (formerly Jennings Aeronautics)
Email: wlilienthal@edgeautonomy.io
Mobile: (805) 704-5344
From: Herberts Stāmers hstamers@edgeautonomy.eu
Sent: Thursday, December 12, 2024 11:10 PM
To: Wesley Lilienthal wlilienthal@edgeautonomy.io; Dmitrijs Palamarčuks dpalamarcuks@edgeautonomy.eu
Subject: About EMI
You don't often get email from hstamers@edgeautonomy.eu. Learn why this is important
Hi Wes,
Sam mentioned you and your expertise, and I wanted to reach out.
We’re dealing with some ground loop issues in our circuit board designs and would appreciate your input. Dmitrijs can provide more technical insights on the challenges.
Would you be open to a quick call to see if this is within your field?
Regards
Outlook-A picture .png	
Herberts Stāmers
Project Manager
Edge Autonomy – Riga
Mobile: +371 25576537
Email: hstamers@edgeautonomy.eu

### Charles David Madewell, 2024-12-24

John Gober was able to do some initial testing on Dec 18, 2024.  His initial report is attached “E140Z G2 Ground Loop Testing December 18.doc”.  More testing is planned after the holidays.

### Charles David Madewell, 2025-01-03

John Gober did some testing on Tuesday (12/31/2024) with EPS6172 on the stand with the ground harness. He didn't see any misbehavior of the gimbal or any stray current or voltages. From what John has gathered, this was not a problem until someone decided to use a conductive mount for the gimbal. John thinks the short-term solution may be Sam's suggestion to change our mounting plate from painted aluminum to a non-conductive plastic.  John thinks we will need an IB to trace the problem much further. On that front, Gio shipped a box of parts Tuesday - which he think contains 2/3 of the parts needed. Ryan F. and John also ordered a 10-foot table for the work area.

### Christa Meck, 2025-01-22

FYI Only:  I linked https://jenaero.atlassian.net/browse/JA-174 to show that we are tracking the access issues/permissions/Riga situation.

### Pat Wells, 2025-01-23

@Cameron Chapman @John Gober @Charles David Madewell I’ve added two AAR’s from flights on 18January25 that utilized non-conductive mounts on they payload.
Zero MAG issues or anomalies were experienced during these flights.

### Charles David Madewell, 2025-01-23

Ref the attachments that Pat Wells pasted above:   T95_V674_250118_153701_pack.zip and T95_V574_250118_130728_pack.zip

### Jackson Riley Curvin, 2025-02-18

@Greg Fryer  734 Zip file is attached the date of the incident was 14 FEB. Student noticed gimbal mounting plate was warm upon investigation noticed that the gimbal mounting plate was arching between the fuselage. Photos are attached as well.

### Greg Fryer, 2025-02-20

@John Gober Please make sure the status of this ticket, and it’s subtasks, get updated so we know it’s advancing. Please also make sure the root cause/investigation file is in sharepoint: Incident Reports

### Christa Meck, 2025-04-17

Removed parent to prep for Incident hierarchy change.  Parent is linked as Linked issue.

## Attachments (14)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 1.jpg | image | 1727 | 2024-12-09 | listed only |
| 2.jpg | image | 2354 | 2024-12-09 | listed only |
| 3.jpg | image | 1519 | 2024-12-09 | listed only |
| 4.jpg | image | 2944 | 2024-12-09 | listed only |
| 5.jpg | image | 2141 | 2024-12-09 | listed only |
| [E140Z G2 Ground Loop Testing December 18.docx](attachments/25143_E140Z%20G2%20Ground%20Loop%20Testing%20December%2018.docx.md) | docx | 15 | 2024-12-24 | converted |
| T95_V674_250118_130728_pack.zip | archive | 911 | 2025-01-23 | listed only |
| T95_V674_250118_153701_pack.zip | archive | 7007 | 2025-01-23 | listed only |
| 9b2523f1-3e81-4644-a41d-364ad5aedb2f.jpg | image | 56 | 2025-02-18 | listed only |
| VXE-734 VTOL.zip | archive | 82848 | 2025-02-18 | listed only |
| VXE-734 XCOMM.zip | archive | 20220 | 2025-02-18 | listed only |
| a7f83c82-8d93-4121-b3d1-60c732ecce2f.jpg | image | 83 | 2025-02-18 | listed only |
| bb0e851b-ea76-4c1b-9153-998c6b315c3a.jpg | image | 84 | 2025-02-18 | listed only |
| f4d14c07-5526-4b61-8d72-856c662c8010.jpg | image | 63 | 2025-02-18 | listed only |
