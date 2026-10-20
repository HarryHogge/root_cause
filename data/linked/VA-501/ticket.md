# VA-501: TPTR-87 VXE 511 VTOL Connector Issues - Prepare and submit data package for customer.

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2023-09-12
- **Updated:** 2025-06-09
- **Resolved:** 2025-06-09
- **Reporter:** Cameron Chapman
- **Assignee:** Cameron Chapman
- **Creator:** Cameron Chapman
- **Links:** blocks VXEP-12 (TPTR-87 VXE 511 VTOL Connector Issues 516 CW. Contains Main connector/contact C/CAs)

## Description

Updated request:
Template for format located here: TIQUILA Team OneNote
Briefing stored to: Briefings



Initial Request:
To support closure on this action, Trevor asked for a data package that recommends closure and includes the following:
- Description of Fix
- Testing Results
- Documentation (specifically documentation to support field-fix efforts, but potentially we should be transparent enough to show them our changed production and QA instructions)
- RCCA 8D charts (may only need in backup)

## Sprint

VXE-2 Mech-Prod 2024-01, VXE Product Dev & Sup 2024-07, VXE-2 Mechanical+Prod 09-Oct, VXE-2 Production, VXE-2 Mech-Prod 2024-6, VXE Product Dev & Sup 2024-05, VXE Prod Dev & Sup 2024-08, VXE-2 Mech-Prod 2024-5

## Comments (5)

### Cameron Chapman, 2023-09-12

Yeah, Cameron said the same thing. So everybody knows but me. 😊
 
From: Matt Philley <mphilley@edgeautonomy.io> 
Sent: Tuesday, September 12, 2023 2:55 PM
To: Greg Fryer <gfryer@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Subject: RE: TPTR-87 - Connector Issue (8D aside)
 
@Greg Fryer@Cameron Chapman
 
Don’t forget the existing 8D is already linked in the TPTR Jira Ticket in the description https://jenaero.atlassian.net/browse/VXEP-12. It should cover all the major points already except details on the engineering corrective action(s).
 
 
|  | Matt Philley Quality Engineer Edge Autonomy – SLO Phone: +1-805-592-1178 Email: mphilley@edgeautonomy.io |

 
 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
 
From: Greg Fryer <gfryer@edgeautonomy.io> 
Sent: Tuesday, September 12, 2023 2:16 PM
To: Matt Philley <mphilley@edgeautonomy.io>; Glen Francis <gfrancis@edgeautonomy.io>
Cc: Jeran Heistermann <jheistermann@edgeautonomy.io>; Ryan Stafford <rstafford@edgeautonomy.io>; Hans Hershberger <hhershberger@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>; Trevor Gronner <tgronner@edgeautonomy.io>
Subject: RE: TPTR-87 - Connector Issue
 
Glen – We’re bouncing of the process rails here on approach, but we can do what was requested. I also dropped a bunch of folks off to save email.
 
From a straight-up engineering perspective this was a low level change, meaning the amount of review is not high. What your email just turned it into (under the “important to the customer” clause in the process, yes it’s actually there) is a L4. (Maybe it should have been all along, but we were going for “faster”)
 
I just warned Hans, and will get Cameron or a EE designee involved to make up that content and conduct a formal design review. Design review will include production (swapped in Trevor) and Quality (Matt). Specific content will be the design (one sheet drawing), testing results (including additional test action), and 8D (which is never light weight). 8D to come from Cameron’s team (largely) – mostly using existing gathered data.
 
~Greg
 
From: Matt Philley <mphilley@edgeautonomy.io> 
Sent: Tuesday, September 12, 2023 1:37 PM
To: Glen Francis <gfrancis@edgeautonomy.io>; Greg Fryer <gfryer@edgeautonomy.io>
Cc: Kyle DeBernardi <kdebernardi@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>; Jeran Heistermann <jheistermann@edgeautonomy.io>; Steve Adlich <sadlich@edgeautonomy.io>; Pat Wells <pwells@edgeautonomy.io>; Ryan Stafford <rstafford@edgeautonomy.io>; Marc Richardson <mrichardson@edgeautonomy.io>
Subject: RE: TPTR-87 - Connector Issue
 
To clarify… the Engineering change is still in process for the connector. Production and QA are NOT ready to start producing material to any new modification to the AS150 connector on the Aircraft centerwing.
 
I don’t think anyone in Production or QA has even gotten hands-on to that label yet, so we have not even been able to start modifying any procedures or inspection points.
 
The change is flagged for discussion at CCB this week: https://jenaero.atlassian.net/browse/VA-456
 
 
|  | Matt Philley Quality Engineer Edge Autonomy – SLO Phone: +1-805-592-1178 Email: mphilley@edgeautonomy.io |

 
 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
 
From: Glen Francis <gfrancis@edgeautonomy.io> 
Sent: Tuesday, September 12, 2023 12:11 PM
To: Greg Fryer <gfryer@edgeautonomy.io>
Cc: Kyle DeBernardi <kdebernardi@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>; Jeran Heistermann <jheistermann@edgeautonomy.io>; Matt Philley <mphilley@edgeautonomy.io>; Steve Adlich <sadlich@edgeautonomy.io>; Pat Wells <pwells@edgeautonomy.io>; Ryan Stafford <rstafford@edgeautonomy.io>
Subject: TPTR-87 - Connector Issue
 
Greg
 
LM was asking about the connector issue during our weekly Tag-Up for Hardware Deliveries.  It’s one of the blocking issues to restart deliveries.
 
I told them we have the fix identified and we’re doing some final testing and generating the documentation to support both the field fix and the cut-in to production. 
 
Kyle was also on the call and confirmed that we will be producing material following modified production and QA instructions.
 
To support closure on this action, Trevor asked for a data package that recommends closure and includes the following:
- Description of Fix
- Testing Results
- Documentation (specifically documentation to support field-fix efforts, but potentially we should be transparent enough to show them our changed production and QA instructions)
- RCCA 8D charts (may only need in backup)

 
Recommend we keep this simple and possibly iterate a time or two with Matt Curran and/or Jeff Hartsell.
 
Thanks,
 
Glen
 
|  | Glen Francis Director of Program Management Edge Autonomy Office:  256.715.5734 Office:  805.544.0932 ext 204 Mobile:  +1 256.337.9725 Email:  GFrancis@edgeautonomy.io Address: 170 Jetplex Blvd SW, Suite E, Huntsville AL 35824 |

### Matt Philley, 2023-09-13

Asking Glen if we can use the new LM 4-blocker template instead of a full 8D for this topic, which would be much more simple to complete.

### Matt Philley, 2023-09-13

@Cameron Chapman Assigning to me for now. We are still trying to figure out where ownership lies for Customer Communication, but I am familiar enough with this topic to help with this one.

### Cameron Chapman, 2023-09-13

Sounds good. Thanks Matt.

### Matt Philley, 2023-09-13

OK according to @Marc Richardson Quality is not on the hook for this one, so I am standing down on putting a summary together. Not sure who is the owner though.

## Attachments (0)
