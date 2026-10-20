# VXEP-576: IRAD: Cold Temp for VXE-30

- **Issue type:** Initiative
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2023-02-08
- **Updated:** 2026-02-07
- **Resolved:** 2025-04-15
- **Reporter:** Greg Fryer
- **Assignee:** Greg Fryer
- **Creator:** Greg Fryer
- **Parent:** SP-74 Cold Weather Ops
- **Links:** causes ENGPRJA-32 (Heated pitot system prototype for 2023 demo); causes ENGPRJA-46 (Air data pod design improvements - heated pitot tube); causes ENG-1511 (Create List of VXE30 Vulnerabilities to Cold); relates to ENG-1657 (INL Battery Testing)
- **Other Stakeholder (as required):** Jack Waeschle
- **Leadership Stakeholder:** Sam Miller
- **Job Number:** J100070 - VXE_ColdTemp [2023 Code?]

## Description

Files: VXE_ColdTemp
2023 Heated Pitot Prototype
Tasks
- Create Heated Pitot prototype (COMPLETE)
- Refine Heated Pitot for manufacturability (ON HOLD)
- Generate list of VXE-30 weaknesses/vulnerabilities/unknowns at -4F (-15C) and -40C (IN PROGRESS)
- Find/design/integrate cold tolerant parts & systems as driven by the list (ON HOLD)

Scope
VXE Cold Temp aims to investigate the vulnerabilities for VXE30 in cold weather conditions and expand the vehicle’s capacities in these environments. The ultimate operational temperature envelope will be driven by the findings of the initial investigation. This will help keep the project within budget and the scale of challenges manageable. 
VXE Cold Temp does not promise to expand our operations into icing conditions. This initiative will likely investigate de-icing coatings, however full deicing capabilities likely will require a complete redesign of the lift booms and forward propulsion system and extensive heater integration which is better suited for a block 35 or block 40 vehicle.

## Comments (4)

### Greg Fryer, 2023-02-08

Files attached (“Idaho Flights.docx” and two zip files) may be useful for this effort, or may not. From @Former user:
I reached ot to our CACI customer about cold weather data. They flew in November at Idaho National Labs. 
They were nice enough to send me the FDR's from those flights.  
Since they were flying at the limit of our published temperature range, I thought the data would be helpful before the artic experiment in Norway.

### Jack Waeschle, 2023-03-08

De-icing Summary
Should we want to pursue de-icing capabilities, I would recommend testing in icing wind tunnels to validate our system across a spectrum of icing conditions as these will need to be robust and reliable to avoid regular loss of vehicles.
I have found only three icing wind tunnels that can potentially be rented/used for testing.
- Icing Research Tunnel (NASA) - Cleveland, OH - Quoted $50k/day (high/conservative estimate)
- LeClerc Icing Research Laboratory (Cox and Company) - Plainview, NY - Quoted $10k/day
- Icing Research Tunnel (Iowa State) - Ames, IA @Sam Miller has a contact there but it did not sound promising when he contacted him this fall.

This testing would require 1-2 engineers and a day or two to test every component and potentially redesign systems while out there should testing results be less than satisfactory. If major system redesigns were required, a second round of testing would be required.
Another major hurdle for de-icing capabilities is our VTOL system and forward propellors. The VTOL system would likely require a full redesign of the lift booms such that blades can nest inside of a heated cavity, similar to the system on the penguin. This would also serve as an opportunity to explore abandoning single blades in favor of more vibrationally stable and traditional two bladed design. @Sam Miller is a lift system redesign within the scope of this IRAD project? This seems better fit for block 35. The forward prop would also need some creative problem solving and enginuity to avoid icing during sustained flight.
Lastly, an interesting technology I stumbled upon is Nanomyte SuperAi. This is a 20-60 thou thick clear coating that reduces ice adhesion to bare aluminum by 60-80%, which could be very useful in conjunction with heaters on our plane surface, reducing total heating capacity required, saving weight and battery energy. Obviously, this would require further research and investigation, but it seems much easier to integrate into our aircraft than alternatives like inflatable bladders/”de-icing boots” that break ice off or bleed air systems that tap hot air from turbines and direct it around flight control surfaces with a network of pipes.

### Cameron Chapman, 2023-05-04

Pasting email chain: + @Hayden Jeanor 
Thanks Kevin for asking. Always nice to get unexpected engineering help.
 
Jack is in leading our project to define and expand the cold weather limitations of our aircraft, which this effort certainly fits into. He would be the best person to tag up with for current efforts. See https://jenaero.atlassian.net/browse/ENG-374 .
Kurt also did a lot of great experimentation and reporting when he developed the HLB heater system. See docs in this folder  VXE_ColdTemp
 
Some of the experimentation has likely been done by Kurt, but here are some additional tests I could think of that would be useful.
- Main battery:
- Better define operational limits in various flight conditions. different cold, wind, humidity, etc.
- Evaluate how much this range could be expanded by adding heaters like the HLB. The battery heats itself somewhat during fixed wing operation due to internal resistance.
- HLB:
- Additional testing to verify limitations in different cold, wind, humidity, etc. conditions.
- Evaluation how we could increase the cold temperature range with higher power heaters/better insulation (without compromising max tem)

 
Are they interested in hot weather limits as well, or just cold for now?
 
Thank you,
|  | Cameron Chapman Electrical Engineering Supervisor Edge Autonomy – SLO (formerly Jennings Aeronautics) Email: cchapman@edgeautonomy.io Phone: (970)389-5904 |

 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Kevin Sivertson - Bend <ksivertson@edgeautonomy.io> 
Sent: Thursday, May 4, 2023 10:53 AM
To: Greg Fryer <gfryer@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Cc: Gregory Nichols <gnichols@edgeautonomy.io>
Subject: Re: INL battery testing
 
Ok, great. Thanks!
 
 
|  | Kevin Sivertson   Training Manager  Edge Autonomy |

 
 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments. 
 
From: Greg Fryer <gfryer@edgeautonomy.io>
Sent: Thursday, May 4, 2023 10:50 AM
To: Kevin Sivertson - Bend <ksivertson@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Cc: Gregory Nichols <gnichols@edgeautonomy.io>
Subject: RE: INL battery testing
 
Kevin – That’ll be a question to Cameron, added.
 
~Greg
 
From: Kevin Sivertson - Bend <ksivertson@edgeautonomy.io> 
Sent: Thursday, May 4, 2023 10:47 AM
To: Greg Fryer <gfryer@edgeautonomy.io>
Cc: Gregory Nichols <gnichols@edgeautonomy.io>
Subject: INL battery testing
 
Good morning Greg,
Idaho National Labs, would like to do some environmental testing on our batteries, and has funding to do so.  
POC on our side is Allen Gardner.  I am just the messenger. 
 
 
I just got off the phone with the lead engineer at INL doing the testing asked if we have any tests or experiments, we would like to see accomplished for cold weather exposure and or operational temperature testing.  Do we have a running list of questions or tests we would like to have run concerning battery operation?  
 
The lead engineer is Matthew Sirk from Idaho National Labs.
Matthew G. Shirk :matthew.shirk@inl.gov
 
|  | Kevin Sivertson   Training Manager  Edge Autonomy   Mobile: +1(503) 913-7102  Email: ksivertson@edgeautonomy.io |

 
 
Confidentiality Notice 
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments. 
 
Export Control Notice 
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.

### Christa Meck, 2025-03-04

@Greg Fryer Does this work from 2023 still need to be completed?

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| INLColdFlights_01.zip | archive | 15454 | 2023-02-08 | listed only |
| INLColdFlights_02.zip | archive | 15758 | 2023-02-08 | listed only |
| [Idaho Flights.docx](attachments/12461_Idaho%20Flights.docx.md) | docx | 18 | 2023-02-08 | converted |
| [Re_ INL battery testing.msg](attachments/14365_Re_%20INL%20battery%20testing.msg.md) | msg | 138 | 2023-05-04 | converted |
| [US Army 11th Airborne Alaska Wolf Valkyrie II Day 1 SITREP - 2024-11-13.pdf](attachments/24490_US%20Army%2011th%20Airborne%20Alaska%20Wolf%20Valkyrie%20II%20Day%201%20SITREP%20-%202024-11-13.pdf.md) | pdf | 2001 | 2024-11-14 | converted |
