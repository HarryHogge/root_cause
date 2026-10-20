# VXEP-241: Epsilon E140Z G2 Payload Productionize

- **Issue type:** Improvement
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2022-11-17
- **Updated:** 2025-03-04
- **Resolved:** 2024-03-15
- **Due:** 2023-07-28
- **Reporter:** Hans Hershberger
- **Assignee:** Tim Muchmore
- **Creator:** Hans Hershberger
- **Labels:** Engineering, Fuselage
- **Links:** relates to ENGPRJA-61 (E140 G2 MWIR integration and test for AEWE); relates to ENG-904 (Epsilon E140Z G2 VXE Vehicle Productionize); relates to ENGPRJA-33 (Epsilon 95 Triclops Prototype); relates to ENG-3126 (140G2 Wiring harness housing seperated); relates to ENG-878 (Epslion 140Z G2 Transit Case design); relates to ENG-579 (Embedded disable/power cycle feature for epsilon payloads); relates to ENG-580 (Epsilon Improvements); blocks ENG-1072 (Branch Cable improvement for VXE-30 for the Epsilon Gimbal); blocks VXEP-438 (IRAD: VXE-30 Support/Create Octopus Gimbal kits into production)
- **Start date:** 2022-11-30
- **Job Number:** J100072 - VXE Integrate 140 MWIR

## Description

Determine the project scope of how to make the current prototype Epsilon 140Z G2 payload for VXE30 work as a production model.  Start with discussion of short term scope and long term scope.  More children added as result of discussions
Details from Sam and Aidas. 12/1
- Two EPS140 + one EPS140.MWIR, both with the expanded voltage range planned to ship in February.
- Goal is for fuselage changes to be compatible with all payloads. (Including Trillium LD-has Jira project)
- TIQUILA will eventually want LD. Need timeline.
- Goal is to have these payloads (especially MWIR, but may not be ready in time) ready for AEWE (March 14).
- Any other epsilon sales planned before or after feb. Not aware of any other than potential  CANSOF (Spring/Summer 2023). Romania trying to figure out a purchase. Probably wont be able to deliver until May-June based on backlog.

## Comments (21)

### Cameron Chapman, 2022-11-29

Additional items to discuss in the meeting tomorrow. 
- What documentation level and personnel are required to produce short term option?
- Short and long term updates needed to operator documentation
- What issues/difficulties exist in producing or using the current equipment?
- See short term subtask items.
- What are time limits, due dates, acceptable end users, etc. of short term and long term solutions?
- How can we align priorities and schedules of VXE and E140 development between sites?
- Do we want to stagger long term design improvements? Some are less scope and bigger gain than others. Start with creating subtasks to make decision, then another to do the work if decided.
- Long term improvements.
- Expand E140 voltage range (remove prototype regulator)
- Move connectors to the side of the payload (enables smaller landing gear, better FOV, possible retract/extend).
- VXE30 landing pad alternatives.
- List others.

### Cameron Chapman, 2022-11-30

Creating a subtask for E140MWIR design and integration. Hopefully much of it can be common with E140Z G2, if not, we should break it out as a separate project.

### Cameron Chapman, 2022-11-30

Hi, Cameron,
 
In mid-December, Aleksandrs team will make the first tests of PCBs with upgraded electronic components (capacitors).
 
If everything goes well, two EPS140 + one EPS140.MWIR will be delivered to the US with upgraded components.
 
Best regards,
 
|  | Aidas Kučys VP/General Manager Edge Autonomy - Riga Phone: +371-2-668-7665 Email: akucys@edgeautonomy.io Address: 1 Jaunbridagi, LV-2167, Mārupe, Latvia |

 
From: Cameron Chapman <cchapman@edgeautonomy.io> 
Sent: Tuesday, 29 November 2022 6:47 PM
To: Aidas Kucys <akucys@edgeautonomy.io>
Subject: RE: Epsilon modifications for Stalker VXE
 
Thanks Aidas. From my electrical VXE perspective, the expanded voltage range seems like a more important, and hopefully quicker improvement to make the payload integration more rugged and professional. We do not need them to be tied together. The expanded voltage range would enable us to get rid of the prototype and large regulator we have in the harness.
 
The benefits of moving the connectors would primarily be to enable more retraction, which could result in smaller landing gear and a better FOV for the payload.
 
|  | Cameron Chapman Electrical Engineer Edge Autonomy – SLO (formerly Jennings Aeronautics) Mobile: +1 970-389-5904 Email: cchapman@edgeautonomy.io |

 
 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Aidas Kucys <akucys@edgeautonomy.io> 
Sent: Monday, November 28, 2022 9:13 PM
To: Cameron Chapman <cchapman@edgeautonomy.io>
Cc: Steven Wilson <swilson@edgeautonomy.io>; Cody Smisek <csmisek@edgeautonomy.io>; Herberts Stamers <hstamers@edgeautonomy.io>; John Tucker <jtucker@edgeautonomy.io>; Aleksandrs Guks <aguks@edgeautonomy.io>; Justin Neel <jneel@edgeautonomy.io>; Hans Hershberger <hhershberger@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>; Ryan Stafford <rstafford@edgeautonomy.io>; Greg Fryer <gfryer@edgeautonomy.io>; Josh Brungardt <JBrungardt@edgeautonomy.io>; Kyle DeBernardi <kdebernardi@edgeautonomy.io>
Subject: RE: Epsilon modifications for Stalker VXE
 
Hi, Cameron,
 
Let me double-check with the team on the current status.
 
Herberts was redesigning a connector from top to side. However, this requires a new PCB, and implementation is subject to electronic component availability.
 
Aleksandrs’ team is working on expanding the voltage range.
 
Will update you tomorrow.
 
Best regards,
 
|  | Aidas Kučys VP/General Manager Edge Autonomy - Riga Phone: +371-2-668-7665 Email: akucys@edgeautonomy.io Address: 1 Jaunbridagi, LV-2167, Mārupe, Latvia |

 
From: Josh Brungardt <jbrungardt@edgeautonomy.io> 
Sent: Monday, 28 November 2022 10:30 PM
To: Kyle DeBernardi <kdebernardi@edgeautonomy.io>
Cc: Cameron Chapman <cchapman@edgeautonomy.io>; Aidas Kucys <akucys@edgeautonomy.io>; Steven Wilson <swilson@edgeautonomy.io>; Cody Smisek <csmisek@edgeautonomy.io>; Herberts Stamers <hstamers@edgeautonomy.io>; John Tucker <jtucker@edgeautonomy.io>; Aleksandrs Guks <aguks@edgeautonomy.io>; Justin Neel <jneel@edgeautonomy.io>; Hans Hershberger <hhershberger@edgeautonomy.io>; Aleksandrs Kipluks <akipluks@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>; Ryan Stafford <rstafford@edgeautonomy.io>; Greg Fryer <gfryer@edgeautonomy.io>
Subject: Re: Epsilon modifications for Stalker VXE
 
Cameron’s request is valid as these internal assets will be mostly flown with E140’s on them.
 
V/r,
 
Josh Brungardt
COO
Edge Autonomy
P: +1-541-602-1842
Email: jbrungardt@edgeautonomy.io



Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
On Nov 28, 2022, at 12:23, Kyle DeBernardi <kdebernardi@edgeautonomy.io> wrote:
 
All, 
 
To be clear, the 3 aircraft we are building in December are internal assets. 
 
I still think Cameron’s request is valid, as we are quoting VXE30’s in this configuration.  But the aircraft in December are only for internal use.
 
| <image002.png> | Kyle DeBernardi, P.E. Production Manager Edge Autonomy – SLO Phone: +1-510-685-9062 Email: debernardi@edgeautonomy.io |

 
 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Cameron Chapman <cchapman@edgeautonomy.io> 
Sent: Monday, November 28, 2022 12:01 PM
To: Aidas Kucys <akucys@edgeautonomy.io>; Steven Wilson <swilson@edgeautonomy.io>; Josh Brungardt <JBrungardt@edgeautonomy.io>
Cc: Cody Smisek <csmisek@edgeautonomy.io>; Herberts Stamers <hstamers@edgeautonomy.io>; John Tucker <jtucker@edgeautonomy.io>; Aleksandrs Guks <aguks@edgeautonomy.io>; Justin Neel <jneel@edgeautonomy.io>; Hans Hershberger <hhershberger@edgeautonomy.io>; Aleksandrs Kipluks <akipluks@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>; Kyle DeBernardi <kdebernardi@edgeautonomy.io>; Ryan Stafford <rstafford@edgeautonomy.io>; Greg Fryer <gfryer@edgeautonomy.io>
Subject: RE: Epsilon modifications for Stalker VXE
 
Hello Aidas,
 
I have heard that we are planning to deliver a few more VXE30+ E140 payloads in December. Have you had any chance to work on the expanded voltage range for the E140? The units we have delivered so far have included a rather hacked together prototype regulator harness that ideally should not be sold to customers. Increasing the voltage range to be compatible with out battery would be a much more rugged, lighter, and more professional solution.
 
If that effort has not yet started, could it start soon so that future customers could order and receive the significantly improved option?
 
Thank you, 
| <image003.png> | Cameron Chapman Electrical Engineer Edge Autonomy – SLO (formerly Jennings Aeronautics) Mobile: +1 970-389-5904 Email: cchapman@edgeautonomy.io |

 
 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Aidas Kucys <akucys@edgeautonomy.io> 
Sent: Tuesday, September 27, 2022 11:58 AM
To: Cameron Chapman <cchapman@edgeautonomy.io>; Steven Wilson <swilson@edgeautonomy.io>; Josh Brungardt <JBrungardt@edgeautonomy.io>
Cc: Cody Smisek <csmisek@edgeautonomy.io>; Herberts Stamers <hstamers@edgeautonomy.io>; John Tucker <jtucker@edgeautonomy.io>; Aleksandrs Guks <aguks@edgeautonomy.io>; Justin Neel <jneel@edgeautonomy.io>; Hans Hershberger <hhershberger@edgeautonomy.io>; Enoch Nicholson <enicholson@edgeautonomy.io>; Aleksandrs Kipluks <akipluks@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>; Kyle DeBernardi <kdebernardi@edgeautonomy.io>; Ryan Stafford <rstafford@edgeautonomy.io>
Subject: RE: Epsilon modifications for Stalker VXE
 
Hi, Cameron,
 
I assure you that the implementation of voltage range expansion is on Aleks' to-do list, "medium" priority.
 
Next few weeks, most of the R&D resources are tied up in finalizing PNC VTOL Mk2.5 avionics.
 
We will review engineering priorities in CW42.
 
Best regards,

### Cameron Chapman, 2022-12-05

From Guks
E140 Electrical
- Our batteries range from 30.1V-~20V steady state (transients may exceed this range for short durations depending on equipment switching on and off, impedance, etc.) Is the plan to support this range? A larger range would also be acceptable.
We plan to replace all 30V capacitors to 50V but we still have a motor driver limit of 42V. So I think this should work for you.
- Can you integrate a 12V enable Open=disable signal into the PCB, at some point? Ideally for these first deliveries, but if not, in the future would also be great. It would allow us to build a more streamlined and easier to build harness without bulky/fragile relay in the middle.
We are looking into it. Perhaps we can integrate a simple mosfet. I will let you know details.
a.	In the short term, we can develop an inline relay option if needed.
- Because SLO does not know and cannot test the power requirements in detail until the equipment arrives, can Latvia select and test an inline relay during your development for us to use?
a.	We would want 12V enable Open=disable. We can discuss requirements and potential options if so.
Overlaps with the previous item.
- Do you have any power requirements for the EPS140 + EPS140.MWIR available? We would like to verify that the wiring and relay can support these requirements and determine if we will need any heat sinking of the relay.
a.	Previous testing of the EPS140 showed much larger startup current required than the specs indicated, which required us to spend more time selecting and testing a new regulator.
Average current for 140G2 is around 1.5Amps on (24V). Short peaks can go up to 3Amps. We don’t have a spec for 140MWIR yet. Basically the main difference is cooled IR sensor which requires additionally 15W of power.

### Cameron Chapman, 2023-01-03

Sent 1/3
Hello Aidas and Team,
I hope your holidays went well. I would like to check in on our various payload projects.
- When does most of the Riga facility return to work?
- Are the planned payload deliveries still on schedule for a February delivery date for two EPS140 + one EPS140.MWIR?
- Do you have an estimated delivery date for the E95s that will be required for the Triclops project? (Targeting AEWE demo March 14).
- Was Aleksandrs or anyone else able to determine if an onboard relay/FET would be feasible? If not, were you able to identify an inline one that could work?
- Did you create the Teams Team mentioned below for schedule, file sharing, and communication? Would you like me to if not?
- Greg, any updates on connecting Riga to JIRA?

### Cameron Chapman, 2023-01-17

Hello everyone,
Here is the summary and actions from the call this morning. Please feel free to add or modify any.
 
Summary
E95s should be ready to send ~1/24. Sam will be in Latvia until 2/4. May hand carry to SLO then.
- Need to expand voltage range or integrate converters.
- We discussed in SLO. We are planning on all 3 E95s to point the standard direction (down). Please hold on 90 deg evaluation.

MWIR not available until end of February. Sam may be able to hand carry then.
Need to identify which 140 G2 will be used for demo and any other upcoming builds.
 
Actions
- Aleksandrs: See if E95 deliveries can be modified to support Stalker voltage range (30.1V-~20V). This is a highly desired feature for Stalker, as it would lead to a much more professional, lightweight, and rugged integration.
- If this is not feasible, would Riga be able to select, test, and mount a compatible voltage converter? This would lead to a much less rushed integration and test in SLO.
- Aleksandrs?: Test 3 E95s or similar bandwidth over Silivus radios.
- Can you please send ideal and minimum bandwidth requirements for E95?
- Aleksandrs: Please do not proceed with any 90 deg work. Planning on standard orientation currently.
- Aidas: Clarify E140 orders and deliveries. Which are we planning to send to AEWE? Does SLO have any incoming we should plan to build VXE integration hardware?
- Hans: Develop options to ensure maximum ground clearance of wing gimbals and minimize view obstruction of wing landing gear.
- Hans: Evaluate drag and weight impacts of E95 triclops configuration. Ensure no risk to flight stability.
- Cameron: Inquire/document bandwidth limitations of VXE and GCS equipment (excluding radio-tested above) in planned connection configuration.

### Cameron Chapman, 2023-02-07

@Hayden Jeanor, this should ship soon.  Can you please prepare a wiring diagram and information for a concept review, and to plan the upcoming builds. Please kit the parts needed for our planned builds. Each E140 should ship with a ground test harness for testing as well. See the manual for details. 
| Item | Qty | Ship Date Estimate | Delivery to SLO |
| 140 G2 expanded voltage range | 1 | 8-Feb | 17-Feb |
| 140 G3 (MWIR) expanded voltage range | 1 | 20-Feb | 1-Mar |
| E95 expanded voltage range | 3 | 8-Feb | 17-Feb |

Epsilon Delivery Dates.xlsx

### Hayden Jeanor, 2023-02-14

@Cameron Chapman long term, are we considering an inline switching device (relay or transistor) in the harness?

### Cameron Chapman, 2023-02-21

@Hayden Jeanor , long term, the plan is to evaluate adding a FET to the PCB in the epsilon. We should ask if they have a timeline for that. We will likely have lots of questions during testing, so we can add that to the list.

### Hans Hershberger, 2023-04-17

We are getting an Epsilon 140Z G2 sent down from Bend for this effort.

### Hans Hershberger, 2023-05-23

A slight snag on this as the E140 asset we have in house is one that needs a voltage regulator so it is not quite reflective of current technology.  The mechanical side seems fairly buttoned up, but there may be more work that comes with integrating the electrical harness.

### Hans Hershberger, 2023-06-09

Model added to VXE35 Demonstrator CAD

### Hans Hershberger, 2023-06-12

@Sam Miller Next time we get in a payload to SLO with an integrated voltage regulator, I would like to swap it for our current asset (that does need a voltage regulator) so we can button up this project.

### Hans Hershberger, 2023-06-12

Pushing back due date a month to reflect our current lack of a payload that reflects our production capabilities.

### Hans Hershberger, 2023-06-21

This may be integrated first on MWIR as that is what we have in house now.  But if we integrate one, we integrate the other.

### Hans Hershberger, 2023-09-13

I’ve got two tickets to paradise two mounts on order from Protolabs that hold the relay in various positions.

### Greg Fryer, 2024-01-22

This ticket and it’s sub-tasks has just been overtaken by events. We are working with Latvia to move the definition of the kit over there, though likely the documentation still needs to come from FLOPS.

### Greg Fryer, 2024-01-22

@Tim Muchmore I don’t think we’ve dragged you into this, but it’s mostly out of our hands in SLO, but we are trying to support Latvia in implementation. Might also be a spot @Rodney Linch can help with, but not sure he’s plugged into Jira yet either.

### Greg Fryer, 2024-01-22

@David R. Martin II You should probably ping me on most of these, most folks will have forgotten what it was for. i just re-crafted this whole project, to try and match reality.

### Tim Muchmore, 2024-01-23

@Greg Fryer Team Latvia has questions about the GSC-03-84820-00 and M27500-26SC2T23 cables sent separately via chat 
They also need 10x connectors shipped to their facility from the US in order to meet the timeline.

### Greg Fryer, 2024-03-15

Completed by the Riga team!

## Attachments (0)
