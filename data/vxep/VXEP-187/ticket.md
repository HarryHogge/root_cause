# VXEP-187: Plan for Silvus Streamscape 5 rollout/compatibility.

- **Issue type:** Major Project
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2023-11-08
- **Updated:** 2025-06-02
- **Resolved:** 2025-06-02
- **Due:** 2024-03-18
- **Reporter:** Cameron Chapman
- **Assignee:** David Grosher
- **Creator:** Cameron Chapman
- **Labels:** GFProject, Production-Priority
- **Links:** relates to VA-1464 (965-1-01-4900 Silvus Enclosure - Label Update for SS4 vs SS5 IP Addresses); relates to VXEP-334 (Silvus SS4 Interim (4.0.4.1) Configuration File Creation Needed)
- **Production Stakeholder:** Trevor Gronner
- **Supply Chain Stakeholder:** Victor Vandor
- **Other Stakeholder (as required):** Matt Philley

## Description

Holding this in Charter/Define while we figure out the scope. If we don’t need to take immediate action, then we will just log information and then put on hold. If we are on a tighter schedule, then we need to document that and start the project.

## Plan

Questions to answer: 
- If we order radios with SS4, what IP addresses will we get? We will have to check for conflicts in our records, I suspect.
- Do they have a sunset date on SS4 radios (is there a time they will stop selling them). Supplier has run out of SGCS1 version. Our qty will last until mid march.
- Do SS4 and SS5 inter-operate. Eventually when we sell someone an SS5 airplane, will they be able to use a GCS with SS4 radios to communicate with it?

## Issue Status

Asked @Wesley Lilienthal if he plans to work on this sprint.  (sprint ends 3/1). Hard due date. We will run out ~3/18. Needs to be done before then.

## Comments (19)

### Cameron Chapman, 2023-11-08

I have a question that may have been implied, but we should answer to determine how we order and process.
Question 4.
If we radios we order arrive with SS5, can we load the 4.0.4.0 “interim firmware” on them, or would we have to order the radios and specify 4.0.4.0 “interim firmware”? This will determine if we need to fix this with procurement or processing on our end. Having silvus load 4.0.4.0 “interim firmware” seems like the most efficient method in either case.
 
I created a JIRA project to log this plan. We should move correspondence to there for tracking. https://jenaero.atlassian.net/browse/VXEP-187 
 
 
 
Thank you,
|  | Cameron Chapman Electrical Engineering Supervisor Edge Autonomy – SLO (formerly Jennings Aeronautics) Email: cchapman@edgeautonomy.io Phone: (970)389-5904 |

 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Greg Fryer <gfryer@edgeautonomy.io> 
Sent: Wednesday, November 8, 2023 1:37 PM
To: Matt Philley <mphilley@edgeautonomy.io>; Victor Vandor <vvandor@edgeautonomy.io>; Randy Schumacher <rschumacher@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>; Wesley Lilienthal <wlilienthal@edgeautonomy.io>
Cc: Marc Richardson <mrichardson@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Subject: RE: Silvus StreamScape 5 - Compatibility Issue
 
Matt, Victor, thank you. Added Wes L. since he is turning into our Silvus tech POC.
 
I think this question:
- Will “SS5 radios” with SS4 firmware still work fine with our existing radios with SS4 firmware?

- No hardware difference, so the 4.0.4.0 “interim firmware” would allow new radios to continue to function with “SS4” radios.

 
Is actually 2 questions, maybe 3?
 
- If we order radios with SS4, what IP addresses will we get? We will have to check for conflicts in our records, I suspect.
- Do they have a sunset date on SS4 radios (is there a time they will stop selling them).
- Do SS4 and SS5 inter-operate. Eventually when we sell someone an SS5 airplane, will they be able to use a GCS with SS4 radios to communicate with it?

 
~Greg
From: Matt Philley <mphilley@edgeautonomy.io> 
Sent: Wednesday, November 8, 2023 12:31 PM
To: Victor Vandor <vvandor@edgeautonomy.io>; Randy Schumacher <rschumacher@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>; Greg Fryer <gfryer@edgeautonomy.io>
Cc: Marc Richardson <mrichardson@edgeautonomy.io>
Subject: RE: Silvus StreamScape 5 - Compatibility Issue
 
@Victor Vandor @Sam Miller @Greg Fryer
 
See my “translated” notes in BLUE.
 
See attached more info from Silvus on the change. I am going to focus on getting the radios we know are good in the hands of Production, but it looks like any new radios will still need different firmware from what we had due to the IP address issue… which is not ideal, but does not kill backwards compatibility.
 
 
|  | Matt Philley Quality Engineer Edge Autonomy – SLO Phone: +1-805-592-1178 Email: mphilley@edgeautonomy.io |

 
 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
 
From: Matt Philley <mphilley@edgeautonomy.io> 
Sent: Wednesday, November 8, 2023 10:23 AM
To: Victor Vandor <vvandor@edgeautonomy.io>; Randy Schumacher <rschumacher@edgeautonomy.io>
Cc: Sam Miller <smiller@edgeautonomy.io>; Marc Richardson <mrichardson@edgeautonomy.io>
Subject: RE: Silvus StreamScape 5 – Compatibility Issue
 
@Victor Vandor @Randy Schumacher
 
We have the following questions then. We can ask them at the 12 o clock call or else we need answers ASAP:
 
- Is there a hardware difference between an existing SS4 radios (SC4240EP-235467-BB & SC4240P-235467-O) and “SS5 radios”? If they are not backwards compatible that sounds like a PN change. Has there been a Part Number roll on the Silvus side?

- No hardware difference and no change to Silvus Part Numbers. The issue is they ran out of IP Addresses for the 172.20.XXX.XXX subnet(?), so part of the “SS5” change is to expand IP’s to 172.16.XXX.XXX thru 172.31.XXX.XXX.
- We can tell if they are SS4 or SS5 by the IP address. Anything still 172.20.XXX.XXX is SS4

 
- Since we do not have the infrastructure in place to transition to “SS5 radios” with SS5 firmware can we still order “SS4 radios” with SS4 firmware? Or “SS5 radios” with SS4 firmware?
- If we can still order radios with SS4 firmware, can we also get some note on the PO or Packing List to specify which SW/FW is being loaded that way we don’t have to power on every radio at receipt (which is going to be a pain)

- They have an “interim firmware” to allow the continued use of “SS4” firmware which is 4.0.4.0, which is based off their 4.0.3.15 firmware (newer than the 4.0.3.14 firmware we currently use), however there might be duplicate IPs…?

 
- Will “SS5 radios” with SS4 firmware still work fine with our existing radios with SS4 firmware?

- No hardware difference, so the 4.0.4.0 “interim firmware” would allow new radios to continue to function with “SS4” radios.

 
- For all the RMA radios we are sending are you updating them to SS5 firmware? Hopefully not…

- RMA radios did not get any new firmware. We can verify because IP stayed the same

 
I am sure there will be more questions, but these are the major ones.
 
 
 
 
|  | Matt Philley Quality Engineer Edge Autonomy – SLO Phone: +1-805-592-1178 Email: mphilley@edgeautonomy.io |

 
 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
 
From: Sam Miller <smiller@edgeautonomy.io> 
Sent: Wednesday, November 8, 2023 7:57 AM
To: Matt Philley <mphilley@edgeautonomy.io>; Victor Vandor <vvandor@edgeautonomy.io>; Randy Schumacher <rschumacher@edgeautonomy.io>; Marc Richardson <mrichardson@edgeautonomy.io>
Subject: RE: Silvus StreamScape 5 - Compatibility Issue
 
Our customers are not moving to Version 5 anytime soon.  There is a huge pile of testing and CCBs that will have to be done over the next few months.  We MUST continue to deliver 4.0.3.14 so that the customer's systems are compatible with new systems coming from the factory. 
 
Thanks,
Sam
 
From: Matt Philley <mphilley@edgeautonomy.io> 
Sent: Wednesday, November 8, 2023 7:06 AM
To: Victor Vandor <vvandor@edgeautonomy.io>; Randy Schumacher <rschumacher@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>; Marc Richardson <mrichardson@edgeautonomy.io>
Subject: RE: Silvus StreamScape 5 - Compatibility Issue
 
@Victor Vandor
 
We will need instructions on how to do that. We can hold them in QA until that happens though.
 
Does this mean older ground station radios will not be able to communicate to radios with this newer firmware? That seems like a really big deal for things in service… will this change the way we configure or checkout radios?
 
@Sam Miller This also sounds like a change to the CIL and ABL for TIQUILA?
 
@Marc Richardson FYSA
 

 
 
|  | Matt Philley Quality Engineer Edge Autonomy – SLO Phone: +1-805-592-1178 Email: mphilley@edgeautonomy.io |

 
 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
 
From: Victor Vandor <vvandor@edgeautonomy.io> 
Sent: Tuesday, November 7, 2023 4:55 PM
To: Matt Philley <mphilley@edgeautonomy.io>; Randy Schumacher <rschumacher@edgeautonomy.io>
Cc: Sam Miller <smiller@edgeautonomy.io>
Subject: FW: Silvus StreamScape 5 - Compatibility Issue
Importance: High
 
Matt, Randy
 
We just received a new batch from Silvus that is currently in QA for inspection.
 
We will need to double check to ensure that these radios are equipped with StreamScape 4 software.  Ideally, they would ship radios to us with 4.0.3.14
 
Based on the message attached, starting November 01st,  the radios would arrive with  StreamScape 5 software and this is a problem
 
Can we investigate the latest batch received to ensure these do not have to be returned?
 
Victor Vandor
Supply Chain Manager
Edge Autonomy
Previously Jennings Aeronautics
P: +1-805-544-0932
Email: vvandor@edgeautonomy.io

Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
 
From: Sam Miller <miller@jenaero.com> 
Sent: Tuesday, November 7, 2023 4:06 PM
To: Victor Vandor <vvandor@edgeautonomy.io>
Cc: Greg Fryer <gfryer@edgeautonomy.io>; Wesley Lilienthal <wlilienthal@edgeautonomy.io>
Subject: Silvus StreamScape 5 - Compatibility Issue
Importance: High
 
Hi Victor,
 
Reviewing this document, I just realized that we cannot downgrade radios shipped to us! 
 
We must ensure that all Edge Autonomy radios are shipped with StreamScape 4 software.  Ideally, they would ship radios to us with 4.0.3.14. 
 
Thanks,
Sam
 
From: Silvus Technologies <info@silvustechnologies.com> 
Sent: Friday, September 29, 2023 9:44 AM
To: Sam Miller <miller@jenaero.com>
Subject: Introducing StreamScape 5 - Next Gen Firmware & Functionality; Backwards Compatibility Alert – Please Read
 
| Can't read or see images? View this email in a browser |

 
|  | Dear Silvus Customer,   Silvus is excited to announce that StreamScape 5 is here with a wide range of upgraded performance, security and scalability improvements, in addition to Spectrum Dominance BETA enhancements that deliver secure & protected comms in congested and contested environments.   The notification letter linked below includes additional information on these expanded improvements and features, along with important details on StreamCaster radio & firmware compatibility, and how to update your StreamCaster fleet to ensure full interoperability.     Please reach out to your Silvus Sales Representative or info@silvustechnologies.comany with any questions.   Best Regards,   The Silvus Team     StreamScape 5 Release Announcement and Backwards Compatibility Alert |  |

### Matt Philley, 2023-11-08

@Cameron Chapman @Wesley Lilienthal @Greg Fryer I added all the info we have gotten from Silvus to this JIRA. There is a pretty good breakdown which may answer some more questions. 
Historically we have been updating/changing the FW on every radio after it arrives either in Electronics or in SCO to make sure it aligns with our baseline, so that process already exists. 
Their “comparison matrix” states that any shipped radio can load the Interim 4.0.4.0 firmware, so that gives us options.

### Cameron Chapman, 2023-11-08

Thanks Matt. @Victor Vandor, can we request Silvus ship us radio with 4.0.4.0 firmware loaded? That seems like it will save production some work. Any objections @Wesley Lilienthal. We should update the vault datacards and ordering sharepoint if we proceed with that plan.

### Cameron Chapman, 2023-11-09

From: Sam Miller <smiller@edgeautonomy.io> 
Sent: Wednesday, November 8, 2023 3:57 PM
To: Cameron Chapman <cchapman@edgeautonomy.io>; Greg Fryer <gfryer@edgeautonomy.io>; Matt Philley <mphilley@edgeautonomy.io>; Victor Vandor <vvandor@edgeautonomy.io>; Randy Schumacher <rschumacher@edgeautonomy.io>; Wesley Lilienthal <wlilienthal@edgeautonomy.io>
Cc: Marc Richardson <mrichardson@edgeautonomy.io>
Subject: RE: Silvus StreamScape 5 - Compatibility Issue
 
Ideally, the radios would come loaded with 4.0.3.14 so we don’t have to reprogram them.  😉

### Matt Philley, 2023-11-13

Victor has requested and Silvus responded that they will send radios configured with SS4 4.0.4 in the future.
This is still a new firmware for us. 
[embedded: image-20231113-184508.png]

### Sam Miller, 2023-11-13

I’m working with LM to determine which flavor (4.0.4.X or SS5) we roll out on the TIQUILA program.  This is all incredibly helpful…thanks very much team!

### Matt Philley, 2023-11-15

Sam’s notes on decisions made for path forward:
[embedded: image-20231115-152200.png]

### Matt Philley, 2023-11-29

@Desiray Johnston @Sandra Lopez @Victor Vandor 
It looks like this task is still in “Charter/Define” I think yall might need to come up with a drop-dead date for Engineering so we can properly prioritize this? The next batch of radios will be delivered with the interim SS4 config which has not yet been tested/approved by Engineering. So they will be held in QA. 
I am not sure when we will run out of our current inventory of radios… but it looks like the soonest might be the 100-107929 used in SGCS2&3 early Jan…? 

Current Inventory Counts as of 11/29 from Sharepoint and Packing Slip in QA:
| Edge PN | Vendor PN | Inv Count | Count in QA | Where Used | Qty Used Per |
| 96X-3-14-1014 | SC4240EP-235467-BB | 31 | 15 | SGCS1 | 2 |
| 100-107929 | SC4480E-235467-SBST | 4 | 8 | SGCS2 & SGCS3 | 1 |
| 100-100879 | SC4240P-235467-O | 10 | 20 | Aircraft | 1 |

### Matt Philley, 2024-01-03

1/17/24 - Silvus replied and there is no issue with rolling these back to v4.0.3.14, so radios were approved and moved to Inventory
December Delivery arrived with v5.0.0.0 firmware, but still have 172.20 IP addresses. So it looks like we can roll them back to v4.0.3.14 without issue…. but on hold in QA until Silvus replies
[embedded: image-20240103-204839.png]

### Matt Philley, 2024-01-17

@Wesley Lilienthal is there an update for this or an estimated complete for this action? We look to be in good shape for January for Production, but I think you said it was pretty close back in Dec so I don't wanna lose track of it.

### Matt Philley, 2024-01-18

@Greg Fryer @Sam Miller @Steve Stack @Douglas Baker @Marc Richardson 
Just a reminder that this Silvus Firmware is included (I think indirectly) on TIQUILA CIL and ABL, so have we determined if a change notification to TIQUILA is required? I am mentioning this as part of our Airworthiness discussion about change notification with them. There was a draft prepared by Sam on 11/14/23, but it also seems like it might be linked to the FIPS discussion, so not sure if that was completed and delivered or not. 
We will run out of radios with the existing firmware sometime in the next couple months I believe. 

Aircraft:
[embedded: image-20240118-200756.png]
SGCS1:
[embedded: image-20240118-200820.png]
SGCS2:
[embedded: image-20240118-200847.png]
SGCS3 not in scope of TIQUILA yet, but also impacted

### Matt Philley, 2024-02-01

@David R. Martin II @Greg Fryer @Wesley Lilienthal @Sam Miller @Marc Richardson @Victor Vandor @Kyle DeBernardi @Douglas Baker 
January Silvus delivery arrived. Most are still 172.20, IPs, but the first radio that is 172.17 and NO LONGER COMPATIBLE WITH APPROVED SILVUS FIRMWARE has arrived. I will be holding that radio in QA until we have approval for the latest firmware both internally and from our Customers. 
Now that we have a final Qty of approved radios I think it would be wise for Production and Supply Chain to align on when they will run out, so Engineering and Program Management are aware the due-date for approvals before we start having product on hold for this approval. 
There has been no status update since November on this topic……
[embedded: image-20240201-185446.png]

### Greg Fryer, 2024-02-01

@Matt Philley Thank you for reminding me. I created an Epic of tasks and asked @Wesley Lilienthal to brief @David Grosher and someone from SW to get the test and deployment sorted out, along with the notices to Programs (especially TIQ which will require SDRL updates).

### Matt Philley, 2024-02-02

@Trevor Gronner FYSA here is the Jira ticket we need a Production Need Date. 
I have updated how many are in QA as well. Let me know if you have any questions.
| Edge PN | Vendor PN | Inv Count | Count in QA (2/2/24) | Where Used | Qty Used Per |
| 96X-3-14-1014 | SC4240EP-235467-BB |  | 14 OK 1 Not OK | SGCS1 | 2 |
| 100-107929 | SC4480E-235467-SBST |  | 12 OK | SGCS2 & SGCS3 | 1 |
| 100-100879 | SC4240P-235467-O |  | 20 OK | Aircraft | 1 |

### Trevor Gronner, 2024-02-02

@Douglas Baker @Greg Fryer @Sam Miller @David R. Martin II @Wesley Lilienthal @David Grosher I put together an estimate of when the Silvus inventory that is compatible with our old firmware would run out below. I included a production need date to give production enough time to process the parts so they could still ship on time. I also included an estimated ship date to customers in the hopes that our program management and business development teams would reach out to customers and give them a warning. The SGCS1 (96X-3-14-1014) looks like it will be our critical date since we already have received one that cannot use our current firmware version and we will run out of inventory of that item first based on our current production schedule.
| Edge PN | Vendor PN | Where Used | Production Need Date | Estimated Ship Date to Customers |
| 96X-3-14-1014 | SC4240EP-235467-BB | SGCS1 | March 15th | End of March/Early April |
| 100-107929 | SC4480E-235467-SBST | SGCS2 & SGCS3 | April 1 | Mid April |
| 100-100879 | SC4240P-235467-O | Aircraft | April 1 | Mid April |

@Kyle DeBernardi @Matt Philley @Marc Richardson @Sandra Lopez FYSA

### Trevor Gronner, 2024-02-08

@Cameron Chapman I added the due date to this Jira ticket based on the information from my comment below. Please let me know if you want the date to be placed under Due date or Target end (or another field?)

### Matt Philley, 2024-03-18

@David Grosher @Wesley Lilienthal @Cameron Chapman @Greg Fryer
 [embedded: StreamScape v4 and v5 Comparison Matrix and Transition Notes v2 (1).pdf] 
See updated notification from Silvus to clarify the IP range and compatibility with SS4, SS4 Interim, and SS5. This is meant to provide clarification to their original comparison matrix from October 2023.

The primary difference is that it clarifies that SS4 Interim does NOT use the expanded IP range.
Instead Silvus is shipping radios with 2 IP addresses labeled “SS4” and “SS5” (see image). When the radio is configured to SS4 Interim the radio will operate and report the “SS4” 172.20 IP address, which is a “Duplicate IP” matching something else Silvus has already shipped. 
Carson and I ran some situations and we did confirm that even with different virtual IPs if two radios have the same 172.20 IP they will still have a network conflict. It did not crash the network, which is good… but the radios did not operate properly. 
When the radio is updated to SS5 firmware the radio will recognize and use the “SS5” IP address automatically, which is nice. The radio does retain the virtual IP through the update if it was configured on SS4 Interim and then updated to SS5 (like if we shipped it SS4 interim and then a Customer updates it to SS5).
[embedded: image-20240318-195320.png]
[embedded: image-20240318-195345.png]

### David Grosher, 2024-03-18

@Wesley Reynolds FYI

### Matt Philley, 2024-06-12

@Trevor Gronner FYSA for matrix on SS version and FIPS

## Attachments (14)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [SS5 Transition Release Notes.pdf](attachments/17504_SS5%20Transition%20Release%20Notes.pdf.md) | pdf | 77 | 2023-11-08 | converted |
| [StreamScape v4 and v5 Comparison Matrix and Transition Notes.pdf](attachments/17505_StreamScape%20v4%20and%20v5%20Comparison%20Matrix%20and%20Transition%20Notes.pdf.md) | pdf | 146 | 2023-11-08 | converted |
| [Streamscape_5_Customer_Notification_FINAL_09.28.23.pdf](attachments/17506_Streamscape_5_Customer_Notification_FINAL_09.28.23.pdf.md) | pdf | 128 | 2023-11-08 | converted |
| [SS5 Transition Release Notes (84bb2015-f14c-40d5-8ad1-7ea55be5f85b).pdf](attachments/17514_SS5%20Transition%20Release%20Notes%20(84bb2015-f14c-40d5-8ad1-7ea55be5f85b).pdf.md) | pdf | 77 | 2023-11-09 | converted |
| image-20231113-184508.png | image | 59 | 2023-11-13 | listed only |
| image-20231115-152200.png | image | 44 | 2023-11-15 | listed only |
| image-20240103-204839.png | image | 914 | 2024-01-03 | listed only |
| image-20240118-200756.png | image | 27 | 2024-01-18 | listed only |
| image-20240118-200820.png | image | 25 | 2024-01-18 | listed only |
| image-20240118-200847.png | image | 25 | 2024-01-18 | listed only |
| image-20240201-185446.png | image | 3666 | 2024-02-01 | listed only |
| [StreamScape v4 and v5 Comparison Matrix and Transition Notes v2 (1).pdf](attachments/19587_StreamScape%20v4%20and%20v5%20Comparison%20Matrix%20and%20Transition%20Notes%20v2%20(1).pdf.md) | pdf | 153 | 2024-03-18 | converted |
| image-20240318-195320.png | image | 88 | 2024-03-18 | listed only |
| image-20240318-195345.png | image | 260 | 2024-03-18 | listed only |
