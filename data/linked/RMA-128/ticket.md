# RMA-128: VXE 511 070523

- **Issue type:** Bug
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-07-06
- **Updated:** 2024-02-29
- **Resolved:** 2024-02-29
- **Reporter:** Sean Odell
- **Assignee:** Sean Odell
- **Creator:** Sean Odell
- **Links:** relates to ENG-2983 (511 LW motor test failed. 511 and 516 center wings damaged. ); relates to ENG-3067 (VXE511 Center Wing Loose Item); relates to VA-35 (511 CW Input power connector damaged); relates to VXEP-12 (TPTR-87 VXE 511 VTOL Connector Issues 516 CW. Contains Main connector/contact C/CAs); relates to RMA-129 (VXE 516 230705 TIQ)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 511

## Description

a.       Center Wing 511        https://jenaero.atlassian.net/browse/VIT2-321 
b.       From LM  “During the preflight inspection, the operator noted the sound of an object tumbling through the center wing when it is tilted end-over-end. Since this is not part of the wing design we chose to not fly the wing. We did not tear open the AP access panel to look for the object.”
c.       SOW:  Warranty Evaluation on Center Wing
d.       Carson’s Notes:
                 i.            NCR-230511-994 – Two anti-spark pins, the power harness was removed and replaced. Possibly zip tie bits left over in the housing.
                 ii.            NCR-230524-1046 – Wing joiner stop missing / removed. Possibly the broken stop or epoxy from the replacement is loose in the spar.

Here is what I recommend for repair.
- Replace DCSA harness. Inspect avionics tray and boom connectors for any other issues.
- Motors, ESCs, and boom harness are still being held for evaluation. They can either be replaced or wait until that evaluation is done. https://jenaero.atlassian.net/browse/VA-392
- Return to SCO.

## Comments (13)

### Sean Odell, 2023-07-26

Awaiting LM to ship this center wing back. No SCO or test flight needed for this particular repair.

### Cameron Chapman, 2023-08-09

@Sean Odell 511 center wing power connector is damaged. Can you please update this RMA accordingly?

### Sean Odell, 2023-08-09

VXE-511 Center Wing was found to have damage to the power connector. See linked issue. We are now evaluating the power connector.

### Cameron Chapman, 2023-08-09

Thoughts on what work and testing to perform on 511 before returning to service. Is RMA the best place to capture these?@Sam Miller @Carson Buckley@Greg Fryer @Matt Philley @Desiray Johnston  
- Replace dual current sense assembly.
- Inspect CW to boom and boom power connections closely for damage.
- Hover test. Inspect connectors again for any damage. Report anomalies.
- Tether test launch profile matching power and duration. Compare voltage and current measurements to a standard flight. Inspect connectors again for any damage. Report anomalies.
- SCO flight or flights. Inspect connectors again for any damage. Report anomalies.

### Sean Odell, 2023-08-09

@Greg Fryer @Sam Miller @Pat Wells @Cameron Chapman Quote for repair created and in the process of getting a Job and SO #. Final assembly replacing the  dual sense PN: 107-102264. Will update once it is at next step.

### Matt Philley, 2023-08-11

@Sean Odell @Pat Wells we have since also replaced the full 107-101161 Avionics Board Assy for this Aircraft based on our Conformal Coat Investigation (Ref. 8D #21 - VTOL Avionics Board Assy Conformal Coat Intrusion).
To re-cap that investigation we found conformal coat in undesirable locations in the Avionics Board Assy that was already installed in AC511. We pulled all WIP and we found an Autopilot Board and Interface Board pair with no conformal coat in undesirable locations. 
Serial # APB-1-1364 was installed on 8/10/23 by Final Assy Supervisor Kyle E and Inspected by Chris E. AC 511 is now going thru SCO calibration and checkout this morning with intent to deliver it back to SMR ASAP for flight testing and Customer handoff(?).

### Cameron Chapman, 2023-09-19

@Sean Odell @Pat Wells Reopening this RMA. The equipment has not been returned right? 
@Greg Fryer @Former user since this is TIQUILA FAT related, are we approved to repair this equipment, or do we want to keep it until the incident is signed off by LM or customer? 
Here is what I recommend for repair. 
- Inspect the 511 ESCs for signs of overcurrent (open up, smell, visually inspect top).
- Reassemble booms. Hover test then tether test 511 with normal takeoff profile. Ensure no issues.
- Return to SCO.

### Cameron Chapman, 2023-09-19

@Sean Odell please hold on this repair for a bit. I want to make sure this related issue is also ready to close before we return related equipment.  https://jenaero.atlassian.net/browse/VXEP-12

### Cameron Chapman, 2023-11-08

@Sean Odell this was marked as done, but no comments on what was done. It is not authorized for return. Do you know why it was marked as done?

### Sean Odell, 2023-11-08

@Cameron Chapman Moved it back to evaluate as you are correct this scope has been expanded. This ticket was originally for the loose item which was complete. Since we still are evaluating this aircraft, I will leave it on that until your team tells me otherwise.

### Cameron Chapman, 2024-01-05

@Sean Odell I updated the disposition. I think most of this aircraft should be ok to return. Can you please update the description to state the history of the 511 fuselage and other parts? Any issues with those? I only see the CW mentioned. 
Here is what I recommend for repair.
- Replace DCSA harness. Inspect avionics tray and boom connectors for any other issues.
- Motors, ESCs, and boom harness are still being held for evaluation. They can either be replaced or wait until that evaluation is done. https://jenaero.atlassian.net/browse/VA-392
- Return to SCO.

### Sean Odell, 2024-01-05

Closing this ticket as the RMA was repaired and delivered to LM early 10/23. The investigation of cause was still open, but the purpose of this ticket has been complete. Any future request for this aircraft will be on a new RMA ticket.
@Pat Wells FYI

### Cameron Chapman, 2024-01-08

Hi Cameron,
 
As far as the parts are concerned, you can repurpose them for engineering purposes or scrap accordingly.
 
The information in this email can be placed in the closed RMA ticket.
 
Very Respectfully,
 
|  | Sean Odell After Market Project Manager Edge Autonomy – San Luis Obispo Office: +1 805-592-1959 Email: sodell@edgeautonomy.io |

 
 
From: Cameron Chapman <cchapman@edgeautonomy.io> 
Sent: Friday, January 5, 2024 3:11 PM
To: Sean Odell <sodell@edgeautonomy.io>
Cc: Pat Wells <pwells@edgeautonomy.io>
Subject: RE: Information on VXE-511 and any questions?
 
Thanks Sean. In that case, are we ok to scrap/repurpose the 511 parts we have that we don’t need for investigation or would you like to?
Ok if I attach this email to the RMA for context?
 
Thank you,
|  | Cameron Chapman Electrical Engineering Supervisor Edge Autonomy – SLO (formerly Jennings Aeronautics) Email: cchapman@edgeautonomy.io Phone: (970)389-5904 |

 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Sean Odell <sodell@edgeautonomy.io> 
Sent: Friday, January 5, 2024 1:52 PM
To: Cameron Chapman <cchapman@edgeautonomy.io>
Cc: Pat Wells <pwells@edgeautonomy.io>
Subject: Information on VXE-511 and any questions?
 
Good day Cameron,
 
I wanted to give you the full story on VXE-511.  Now I recall why my RMA ticket was closed many months ago.  
While engineering was evaluating the aircraft, the choice to repair it with new parts was made. Edge repaired the aircraft, and I closed the ticket.
 
The amount of information I entered into Jira was very little at that time, but Pat and I have changed are tactic to enter everything we can into our Tickets now that LM does not poke around Jira much anymore. Sorry for the confusion caused by lack of communication in Jira about 511.
 
Further background… LM, in an emergency request from the UK, had them ship 3 aircraft for some type of requirement. LM did a quick source and shipped this aircraft to the UK along with 2 others.  There was FUSE damage from TIQ FAT that never got told to Jeff (LM) or I. So, it got delivered to UK by LM with Fuse damage. Edge did send Sam Miller in an emergency to help support repairs, but it fell on LM in the end.
 
All that said Cameron, I am going to close my RMA ticket and you/Engineering can close your tickets whenever your cleared to do so. It sounds like VXE-511 might come back in a couple months for an RMA and I will need a new ticket for that work.
 
If you have any questions please let me know, but I will be closing the original ticket since the aircraft is closed on LM’s side. Thank you and your team for the hard work!
 
Very Respectfully,

## Attachments (34)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 20230706_111545.jpg | image | 7363 | 2023-07-06 | listed only |
| 20230706_111556.jpg | image | 2927 | 2023-07-06 | listed only |
| 20230706_111627.jpg | image | 6933 | 2023-07-06 | listed only |
| 20230706_111708.jpg | image | 903 | 2023-07-06 | listed only |
| 20230706_111714.jpg | image | 865 | 2023-07-06 | listed only |
| 20230706_111727.jpg | image | 1002 | 2023-07-06 | listed only |
| 20230706_111733.jpg | image | 2625 | 2023-07-06 | listed only |
| 20230706_111752.jpg | image | 2586 | 2023-07-06 | listed only |
| 20230706_111757.jpg | image | 3601 | 2023-07-06 | listed only |
| 20230706_111825.jpg | image | 2166 | 2023-07-06 | listed only |
| 20230706_111843.jpg | image | 7937 | 2023-07-06 | listed only |
| 20230706_111911.jpg | image | 6866 | 2023-07-06 | listed only |
| 20230706_111916.jpg | image | 2218 | 2023-07-06 | listed only |
| 20230706_111921.jpg | image | 3535 | 2023-07-06 | listed only |
| 20230706_111924.jpg | image | 2595 | 2023-07-06 | listed only |
| 20230706_111959.jpg | image | 6810 | 2023-07-06 | listed only |
| 20230706_112004.jpg | image | 6873 | 2023-07-06 | listed only |
| 20230706_112009.jpg | image | 4180 | 2023-07-06 | listed only |
| 20230706_112014.jpg | image | 3748 | 2023-07-06 | listed only |
| 20230706_112135.jpg | image | 5049 | 2023-07-06 | listed only |
| 20230706_112141.jpg | image | 5621 | 2023-07-06 | listed only |
| 20230706_112153.jpg | image | 5400 | 2023-07-06 | listed only |
| 20230706_112209.jpg | image | 6658 | 2023-07-06 | listed only |
| 20230706_112503.jpg | image | 6716 | 2023-07-06 | listed only |
| 20230706_112507.jpg | image | 6877 | 2023-07-06 | listed only |
| 20230706_112511.jpg | image | 7167 | 2023-07-06 | listed only |
| 20230706_112519.jpg | image | 1530 | 2023-07-06 | listed only |
| 20230706_112523.jpg | image | 2054 | 2023-07-06 | listed only |
| 20230706_112755.jpg | image | 6788 | 2023-07-06 | listed only |
| 20230706_112800.jpg | image | 5942 | 2023-07-06 | listed only |
| 20230706_112810.jpg | image | 5848 | 2023-07-06 | listed only |
| 20230706_112824.jpg | image | 7076 | 2023-07-06 | listed only |
| 20230706_114634.jpg | image | 5760 | 2023-07-06 | listed only |
| [VXE 511 7-6-2023.pdf](attachments/15344_VXE%20511%207-6-2023.pdf.md) | pdf | 3271 | 2023-07-06 | converted |
