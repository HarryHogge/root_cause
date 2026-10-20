# VXEP-1907: Add RF loads to all SLO and HSV ironbirds. Add to IB diagrams

- **Issue type:** Epic
- **Status:** In Process
- **Priority:** Low
- **Created:** 2026-06-05
- **Updated:** 2026-07-17
- **Reporter:** Cameron Chapman
- **Assignee:** Matthew Aguirre
- **Creator:** Cameron Chapman
- **Parent:** VXEP-1673 Build and document EE ironbirds

## Issue Status

See email history in comments. 
(6/11) due to last working day will be assigning to @Cameron Chapman to decide what to do with this ticket next

## Comments (4)

### Cameron Chapman, 2026-06-22

From: Wesley Lilienthal <wlilienthal@edgeautonomy.io>
Sent: Thursday, June 4, 2026 4:42 PM
To: Cody Smisek <csmisek@edgeautonomy.io>
Cc: Greg Fryer <gfryer@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Subject: Re: Iron Bird Radio Loads
Copy. PR01301 submitted for the qty 6 terminators you need plus qty 4 for general R&D use. 
- Wes

| Wesley Lilienthal Senior Staff RF Engineer Mobile: 805.704.5344 wesley.lilienthal@rdw.com [embedded: Redwire] |
| [embedded: linkedin icon] [embedded: X icon] [embedded: youtube icon] [embedded: facebook icon] [embedded: instagram icon] |

NOTICE: This message, and any attachments, contain(s) information that may be confidential, proprietary and/or protected by privilege from disclosure and is intended only for the individual or entity named above. No one else may disclose, copy, distribute or use the contents of this message for any purpose. Its unauthorized use, dissemination or duplication is strictly prohibited and may be unlawful. If you receive this message in error or you otherwise are not an authorized recipient, please immediately delete the message and any attachments and notify the sender.
From: Cody Smisek <csmisek@edgeautonomy.io>
Sent: Thursday, June 4, 2026 4:02 PM
To: Wesley Lilienthal <wlilienthal@edgeautonomy.io>
Subject: Re: Iron Bird Radio Loads
 
No need for in-line.
Thanks
Cody
From: Wesley Lilienthal <wlilienthal@edgeautonomy.io>
Sent: Thursday, June 4, 2026 3:35 PM
To: Cody Smisek <csmisek@edgeautonomy.io>
Cc: Greg Fryer <gfryer@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Subject: Re: Iron Bird Radio Loads
Yes, will procure. 
In addition to full termination of all transmissions, is there also separately any need to have the iron birds communicate with an external Silvus radio / GCS? If so, in-line attenuators can be utilized in a conducted (RF cabled only, not radiated) run between IB radio and bench radio. This allows for comms between only the conductively-cabled radios, with no free space transmissions occurring that could leak to any antenna-equipped radio in the building. If so, I can procure hardware for such a setup as well. 
- Wes

| Wesley Lilienthal Senior Staff RF Engineer Mobile: 805.704.5344 wesley.lilienthal@rdw.com [embedded: Redwire] |
| [embedded: linkedin icon] [embedded: X icon] [embedded: youtube icon] [embedded: facebook icon] [embedded: instagram icon] |

NOTICE: This message, and any attachments, contain(s) information that may be confidential, proprietary and/or protected by privilege from disclosure and is intended only for the individual or entity named above. No one else may disclose, copy, distribute or use the contents of this message for any purpose. Its unauthorized use, dissemination or duplication is strictly prohibited and may be unlawful. If you receive this message in error or you otherwise are not an authorized recipient, please immediately delete the message and any attachments and notify the sender.
From: Cody Smisek <csmisek@edgeautonomy.io>
Sent: Thursday, June 4, 2026 3:05 PM
To: Wesley Lilienthal <wlilienthal@edgeautonomy.io>
Cc: Greg Fryer <gfryer@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Subject: Re: Iron Bird Radio Loads
If you're able to procure, that would be great. 
We've got 3x engineering IBs that need them. 
From: Wesley Lilienthal <wlilienthal@edgeautonomy.io>
Sent: Thursday, June 4, 2026 2:55 PM
To: Cody Smisek <csmisek@edgeautonomy.io>
Cc: Greg Fryer <gfryer@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Subject: Re: Iron Bird Radio Loads
Hi Cody,
Yes, see the Mini-Circuits TERM-5W-183S+. Qty 2 required per (iron) bird. These are adequate to properly terminate each chain of the Silvus radio, with all transmit energy being converted to thermal. 
Would you like me to procure or do you plan to?
- Wes

| Wesley Lilienthal Senior Staff RF Engineer Mobile: 805.704.5344 wesley.lilienthal@rdw.com [embedded: Redwire] |
| [embedded: linkedin icon] [embedded: X icon] [embedded: youtube icon] [embedded: facebook icon] [embedded: instagram icon] |

NOTICE: This message, and any attachments, contain(s) information that may be confidential, proprietary and/or protected by privilege from disclosure and is intended only for the individual or entity named above. No one else may disclose, copy, distribute or use the contents of this message for any purpose. Its unauthorized use, dissemination or duplication is strictly prohibited and may be unlawful. If you receive this message in error or you otherwise are not an authorized recipient, please immediately delete the message and any attachments and notify the sender.
From: Cody Smisek <csmisek@edgeautonomy.io>
Sent: Thursday, June 4, 2026 1:08 PM
To: Wesley Lilienthal <wlilienthal@edgeautonomy.io>
Cc: Greg Fryer <gfryer@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Subject: Iron Bird Radio Loads
 
Hey Wes
Would you be able to point out an appropriate RF load(s) to purchase for the silvus aircraft radios that we have connected to the IBs? I don't want these radios accidentally connecting to anything else in the building, so I figure best way to do this is put a load on the end.
Thanks
| Cody Smisek Flight Test cody.smisek@rdw.com [embedded: Redwire] |
| [embedded: linkedin icon] [embedded: twitter icon] [embedded: facebook icon] [embedded: youtube icon] [embedded: instagram icon] |

### Matthew Aguirre, 2026-07-14

Ordered 8x right angle sma-f to sma-m adapters to fit 5W loads. Need for this was not enough clearance to be able to easily demate/mate power to Silvus radio without bending cables. Waiting for arrival on order before installing on Iron Birds. PR01526.

### Matthew Aguirre, 2026-07-14

B40 UAP was fitted with 2x swept right angle sma-f to sma-m adapters (macaroni shaped) and 5W loads were installed. Only need 6x right angle adapters to for B30, B30 UAP, and B40 iron birds.

### Matthew Aguirre, 2026-07-17

B40 and B30 iron birds were fitted with the right angle sma-f to sma-m adapters, and 5W loads were installed. Need to install on the B30 UAP at a later date/time, due to ongoing test.

## Attachments (0)
