# ENG-1070: IRAD: Battery Study Next Gen Lift

- **Issue type:** Initiative
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2023-03-31
- **Updated:** 2025-03-05
- **Resolved:** 2025-03-05
- **Reporter:** Cameron Chapman
- **Assignee:** Tom Westrich
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-640 (IRAD: B40 Battery Charger); relates to ENG-1658 (Block 35 Define Requirements and Concepts); relates to VXEP-232 (Overheating Battery/Cable (Fuel Cell Support Kit SCO Test Config) -)
- **Job Number:** J100068 - Battery_NextGenCharger [2023 Code]?

## Description

Attached related conversations. Stephen Peters speters@edgeautonomy.io seems to be leading this effort. 
SLO to charge Battery_NextGenCharger for now. Assess if it can be done within the budget, if not, a less-change approach is the fallback.
| Priority | Title | Job Number | Group/location | Project Lead | Hours | Material | Subcontract | Description |
| 4 | Battery_Study_NextGenLift |  | Ann Arbor | Mike (Interim) | 450 | $                                 - | $                                            - | Look at new battery cells for high-power (high C-rate) batteries for hybrid lift. (prefer no chinese). Consider Amprius high-power cells. |

Per Tom W-Amprius not available for production levels until ~2025.

## Comments (4)

### Cameron Chapman, 2023-03-31

Cameron – I’m sitting with Sam. Just confirmed that yes, this is what we want.
 
Assess if it can be done within the budget, if not, a less-change approach is the fallback.
 
~G
 
From: Greg Fryer <gfryer@edgeautonomy.io> 
Sent: Friday, March 31, 2023 10:20 AM
To: Cameron Chapman <cchapman@edgeautonomy.io>
Cc: Sam Miller <smiller@edgeautonomy.io>
Subject: RE: Battery_Study_NextGenLift Charge Number
 
Cameron – I believe the scope has morphed to include both. Ticket update needed.

Sam – Is this all one IRAD, now?
 
~G
 
From: Cameron Chapman <cchapman@edgeautonomy.io> 
Sent: Friday, March 31, 2023 9:28 AM
To: Greg Fryer <gfryer@edgeautonomy.io>; Carleta Arbulu <carbulu@edgeautonomy.io>
Subject: RE: Battery_Study_NextGenLift Charge Number
 
I have been charging that for the next gen charger.
 
Ann Arbor is working on the next gen battery, which I have been supporting. Should I charge the charger number or a different one?
 
Thank you,
|  | Cameron Chapman Electrical Engineering Supervisor Edge Autonomy – SLO (formerly Jennings Aeronautics) Email: cchapman@edgeautonomy.io Phone: (970)389-5904 |

 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Greg Fryer <gfryer@edgeautonomy.io> 
Sent: Friday, March 31, 2023 9:26 AM
To: Cameron Chapman <cchapman@edgeautonomy.io>; Carleta Arbulu <carbulu@edgeautonomy.io>
Subject: RE: Battery_Study_NextGenLift Charge Number
 
See
[ENG-371] IRAD: Battery Charger Upgrade to remove Chinese content - Jira (atlassian.net)
 
We want to ditch the sheet and use the Jira tag.
 
~Greg
 
From: Cameron Chapman <cchapman@edgeautonomy.io> 
Sent: Friday, March 31, 2023 9:25 AM
To: Carleta Arbulu <carbulu@edgeautonomy.io>; Greg Fryer <gfryer@edgeautonomy.io>
Subject: Battery_Study_NextGenLift Charge Number
 
Good morning Carla,
 
I have been helping Ann Arbor with this.
What should I charge? There is no J number in the sheet for it.
| Battery_Study_NextGenLift |  | Ann Arbor |

 
Thank you,
|  | Cameron Chapman Electrical Engineering Supervisor Edge Autonomy – SLO (formerly Jennings Aeronautics) Email: cchapman@edgeautonomy.io Phone: (970)389-5904 |

### Cameron Chapman, 2023-03-31

Got it, thanks.
 
-Stephen 
 
Get Outlook for iOS
From: Shaheen Hoque <shoque@edgeautonomy.io>
Sent: Monday, March 27, 2023 1:32:38 PM
To: Stephen Peters <speters@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Cc: Hayden Jeanor <hjeanor@edgeautonomy.io>; Will Harris <wharris@edgeautonomy.io>
Subject: Re: Hybrid Lift Battery contact
 
Hi Stephen,
 
For a VTOL aircraft, the vertical thrust to weight ratio should be between 1.1 to 1.3.
1.3 should be preferable.
 
Thanks
Shaheen Hoque
 
Get Outlook for iOS
From: Stephen Peters <speters@edgeautonomy.io>
Sent: Monday, March 27, 2023 10:21:54 AM
To: Cameron Chapman <cchapman@edgeautonomy.io>; Shaheen Hoque <shoque@edgeautonomy.io>
Cc: Hayden Jeanor <hjeanor@edgeautonomy.io>; Will Harris <wharris@edgeautonomy.io>
Subject: RE: Hybrid Lift Battery contact
 
Awesome, thank you! It will be important to understand from Allen and Sam the weight on backwards (or overall) compatibility. This study is exploratory in nature and in the end will report to leadership what the prospective battery supplier outlook is, and to accomplish that a concrete understanding of what we do now is pertinent for meaningful discussion. So, thank you again!
 
Shaheen, would you be able to comment on the lift power vs. weight relationship? Are there methods we use internally to estimate how much energy the VTOL function demands? If possible, it would be nice to understand the impact additional payload mass (taking group rating for granted), incurred, e.g., via incremented fuel capacity or perhaps a larger fuel cell system, might have on the VXE30 air-frame’s VTOL power needs.
 
I could imagine a route here might be to collect aggregate flight data and produce some VXE30 statistics with a processing tool like MATLAB or python, but only if something like that hasn’t already been done.. I imagine it could have been, given the derived 1.3 power safety factor.
 
-Stephen
 
 
From: Cameron Chapman <cchapman@edgeautonomy.io> 
Sent: Monday, March 27, 2023 12:04 PM
To: Stephen Peters <speters@edgeautonomy.io>
Cc: Hayden Jeanor <hjeanor@edgeautonomy.io>; Shaheen Hoque <shoque@edgeautonomy.io>; Will Harris <wharris@edgeautonomy.io>
Subject: RE: Hybrid Lift Battery contact
 
+Will
 
Thank you,
|  | Cameron Chapman Electrical Engineering Supervisor Edge Autonomy – SLO (formerly Jennings Aeronautics) Email: cchapman@edgeautonomy.io Phone: (970)389-5904 |

 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Cameron Chapman <cchapman@edgeautonomy.io> 
Sent: Monday, March 27, 2023 9:04 AM
To: Stephen Peters <speters@edgeautonomy.io>
Cc: Hayden Jeanor <hjeanor@edgeautonomy.io>; Shaheen Hoque <shoque@edgeautonomy.io>
Subject: RE: Hybrid Lift Battery contact
 
Hi Stephen,
 
It seems like we would be best to start off with design targets/requirements for this project and VXE>30.
Shaheen (Aero supervisor) would likely be the best one to provide a lift power vs weight requirement, and may have some insight to max weights we are planning to support. Also CCd Will (Mech E Lead).
 
Depending on the scope of the change for the next generation and the voltages supported by the fuel cell, you could get more efficiency and less wire weight from higher cell count batteries, but those would not be compatible with VXE30.
 
I recommend also meeting with Allen and Sam to define the requirements of this project, max weight we want to support, and a targeted timeline.
 
Thank you,
|  | Cameron Chapman Electrical Engineering Supervisor Edge Autonomy – SLO (formerly Jennings Aeronautics) Email: cchapman@edgeautonomy.io Phone: (970)389-5904 |

 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Stephen Peters <speters@edgeautonomy.io> 
Sent: Monday, March 27, 2023 5:53 AM
To: Cameron Chapman <cchapman@edgeautonomy.io>
Cc: Hayden Jeanor <hjeanor@edgeautonomy.io>
Subject: RE: Hybrid Lift Battery contact
 
Hi Cameron, I think this would be great if we were searching for a (semi-) direct replacement. What makes this level of specificity challenging in this context is that mass specific performance metrics are to take precedence over external factors – it could be that for the benefit of reducing the HLB mass by 0.x we will purchase individual cells and pack them in house; in such an instance, factors, i.e. thermal performance, are subject to our own design and processes.
 
To further explicate the scope, the “next gen.” HLB should fulfill the requirements of the future VXE35, which although should still be group 2, is intended to be over designed such that it informally could transcend the 55lb boundary with an extra fuel tank or two.
 
With that in mind, do we have an internal method to calculating VTOL lift power based on payload mass? Also, is the 1.3 safety factor derived as a bound from aggregate VTOL flight data?
 
Thanks,
Stephen
 
 
From: Cameron Chapman <cchapman@edgeautonomy.io> 
Sent: Thursday, March 23, 2023 11:48 AM
To: Stephen Peters <speters@edgeautonomy.io>
Cc: Hayden Jeanor <hjeanor@edgeautonomy.io>; Will Harris <wharris@edgeautonomy.io>; Shaheen Hoque <shoque@edgeautonomy.io>; Ryan Christino <rchristino@edgeautonomy.io>
Subject: RE: Hybrid Lift Battery contact
 
Hi Stephen,
 
I recommend you compile a list of derived requirements, then schedule a requirements review for the project with me, Shaheen (aero), Sam M, and Will H(Mech).
 
Here are the main ones:
- Correct, the pack capacity needs to have enough capacity for a worst case takeoff and immediate landing+margin at the end of its lifecycle (accounting for the reduced capacity due~ to wear). I attached flight data for an actual flight, which is then scaled to 1.3x as an estimate of worst case (high altitude and heavy aircraft)
- More energy than needed for 1 will not help. We are limited to 55lbs to stay in class 2. Will would know best, but I think our current baseline is ~49 not including payloads. Depending on the payload, we typically weigh ~54lbs I think. Will can verify. A lighter pack that meets requirements is better than the same weight with more capacity.
- I meant to attach the NHA last time (attached now).
- The connector location, type, and form factor will need to stay approximately the same to be compatible with our aircraft. We can provide models when helpful.
- The attached pack has integrated heaters and a heater control and cell monitor board. A replacement would need those installed as well.
- The enclosure is waterproof when the connectors are mated.

 
Thank you,
|  | Cameron Chapman Electrical Engineering Supervisor Edge Autonomy – SLO (formerly Jennings Aeronautics) Email: cchapman@edgeautonomy.io Phone: (970)389-5904 |

 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Stephen Peters <speters@edgeautonomy.io> 
Sent: Thursday, March 23, 2023 7:04 AM
To: Cameron Chapman <cchapman@edgeautonomy.io>
Cc: Hayden Jeanor <hjeanor@edgeautonomy.io>
Subject: Re: Hybrid Lift Battery contact
 
Cameron, it seems like the HLB performance requirements are relatively simple. There are some nuances in pack integration and the temperature environment the UAV operates, but at its core, the battery needs to be able to output >200A @ 26.4-26.9V for >30s.
 
I think this is sufficient information to gauge battery suppliers that may be ahead in specific energy, with follow-up thought that looks at cycle life, environmental, and integration style trade-offs, if any. I’m not sure what we would think about a HLB with 2x the specific energy but 0.5x the cycle life.
 
One thing that is unclear to me is whether the duration requirement is only half of what is needed. I presume this ~30s is specific for take-off, what about landing?
 
Thanks for taking the time to collect this information for me. Let me know if I am over-simplifying and if you think I should consider some finer grain detail.
 
-Stephen
 
 
From: Cameron Chapman <cchapman@edgeautonomy.io>
Sent: Monday, March 20, 2023 6:55:23 PM
To: Stephen Peters <speters@edgeautonomy.io>
Cc: Hayden Jeanor <hjeanor@edgeautonomy.io>
Subject: RE: Hybrid Lift Battery contact
 
Hi Stephen,
Sorry for the delay in responding. Very busy times. I’ll respond with some information now, and more soon. I CC Hayden, who has also been working on some battery projects.
 
Questions
- Do you have access to our server or vault? Ex “\\condor\Production\Battery Information\Battery Production Data List”

- I recommend requesting that access from the helpdesk email, but we can share info other ways until then. Email for now, then we can establish a MS teams team.
- We can give you access to confluence too (a wiki we are building) https://jenaero.atlassian.net/wiki/spaces/EE/pages/11272193/Power+and+Temperature+Profiles

 
Info.
- Amicell makes our main 60Ah battery for fixed wing flight. Thunder power makes our 6.6Ah HLB for VTOL.
- I attached the following

- Datasheet-record of all HLBs tested and their specs.
- Test procedure
- Drawing
- UN cert

 
Quick Answers
- What performance metrics are most pertinent to the HLB, or more generally, what are the specific HLB functions that drive its requirements? Further, assuming the numbers quoted in the table above are correct, do they reflect accurately the needs of the VXE30 or are the VXE30 requirements nicely packed inside of the Amicell HLB capabilities?

- See flight profile below. Needs to survive the worst case with margin for as many flight cycles as feasible.

- What role would an over-designed HLB fill? Would it assist in increased payload capacity, VTOL maneuverability, VTOL/overall endurance, etc.?

- SWAP trade off. For now, not much. Higher altitude/heavier vehicle takeoffs, but we are still limited to 55lbs including payload to stay in group 2. We typically want as light weight as gets the job done.

- Are there peripheral energy subsystems that effect the HLB’s performance, or does the HLB act independently aside from, perhaps, in-flight charging?

- Minor in flight recharging. I thing ~0.75A to ensure the battery doesn’t drain from ESC electronics. Can check later on the VTOL AP schematic.

 

 
Thank you,
|  | Cameron Chapman Electrical Engineering Supervisor Edge Autonomy – SLO (formerly Jennings Aeronautics) Email: cchapman@edgeautonomy.io Phone: (970)389-5904 |

 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Stephen Peters <speters@edgeautonomy.io> 
Sent: Wednesday, March 15, 2023 12:30 PM
To: Cameron Chapman <cchapman@edgeautonomy.io>
Subject: RE: Hybrid Lift Battery contact
 
Hi Cameron, I’m Stephen from the Ann Arbor Edge office. I am the project lead for the hybrid lift battery IRAD study that motivated the email introduction Theo had sent last week.
 
The hard goal for this project is to evaluate battery suppliers with the aim to maximize specific energy/power for application in 1-2 years. E.g., from information I have been able to collect (see table below), the current VXE30 Amicell battery has a specific energy of ~284 Wh/kg while Amprius advertises, with their Si nanowire anode tech, up to 500 Wh/kg.
 

 
I am wondering if you might be able to answer a couple of questions for me.
- What performance metrics are most pertinent to the HLB, or more generally, what are the specific HLB functions that drive its requirements? Further, assuming the numbers quoted in the table above are correct, do they reflect accurately the needs of the VXE30 or are the VXE30 requirements nicely packed inside of the Amicell HLB capabilities?
- What role would an over-designed HLB fill? Would it assist in increased payload capacity, VTOL maneuverability, VTOL/overall endurance, etc.?
- Are there peripheral energy subsystems that effect the HLB’s performance, or does the HLB act independently aside from, perhaps, in-flight charging?

 
I look forward to hearing from you and would be open to setting up a meeting if you think that would be helpful.
 
Thanks,
-Stephen
 
 
 
 
 
From: Theo Coetzee <tcoetzee@edgeautonomy.io> 
Sent: Monday, March 6, 2023 1:51 PM
To: Tom Westrich <twestrich@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>; Will Harris <wharris@edgeautonomy.io>
Cc: Stephen Peters <speters@edgeautonomy.io>; Michael Edison <medison@edgeautonomy.io>
Subject: RE: Hybrid Lift Battery contact
 
Hi Stephen,
 
For questions about the electrical components / battery cells:
Cameron Chapman would be the best person to contact.
 
For mechanical design:
Will Harris would be the best person.
 
I’m also available if needed.
 
Thanks
-Theo
 
From: Tom Westrich <twestrich@edgeautonomy.io> 
Sent: Wednesday, February 15, 2023 12:09 PM
To: Theo Coetzee <tcoetzee@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>
Cc: Stephen Peters <speters@edgeautonomy.io>; Michael Edison <medison@edgeautonomy.io>
Subject: Hybrid Lift Battery contact
 
Hi Sam & Theo,
 
Stephen Peters will be working on the Energy Systems IRAD program to evaluate alternate battery suppliers for the existing Hybrid Lift Battery.  One of his first tasks is to get as much information as possible on the current HLB.  Can you please connect him with the appropriate person at Edge for this effort?
 
Thanks!
 
Tom
 
|  | Tom Westrich VP Technology Edge Autonomy Phone: 734.302.7632x475 Cell: 505.228.5427 Email: twestrich@edgeautonomy.io |

### Cameron Chapman, 2023-03-31

Assigning to @Tom Westrich  and inviting Stephen to JIRA.

### Christa Meck, 2025-03-04

@Cameron Chapman and/or @Tom Westrich Does this work from 2023 need to be completed?

## Attachments (0)
