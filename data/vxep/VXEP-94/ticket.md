# VXEP-94: SA Camera EM18911 (100-100835) and EM19821 (100-101235) are obsolete (closed with buy)

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2022-10-20
- **Updated:** 2024-02-07
- **Resolved:** 2023-09-19
- **Due:** 2025-01-01
- **Reporter:** Victor Vandor
- **Assignee:** Greg Fryer
- **Creator:** Greg Fryer
- **Labels:** 8-28-Sprint, EE-Intern
- **Links:** relates to VA-126 (Determine if any more of the current cameras + boards can be purchased, and purchase if so. Keep run out date updated. ); relates to VA-125 (Trade study and downselect); relates to VXEP-93 (Replace SA Camera EM18911 (100-100835) and EM19821 (100-101235) are obsolete. due February 2025.)
- **Start date:** 2023-06-01
- **Production Stakeholder:** Ryan Ferguson
- **Supply Chain Stakeholder:** Victor Vandor
- **Other Stakeholder (as required):** Greg Fryer
- **Problem Type:** Part Obsolescence

## Description

See Rate Forecasts.xlsx for runout date. On 4/5/23, we calculated 03/24. 

Target requirements are essentially. https://jenaero.atlassian.net/browse/ENG-2063
- Minimize mechanical changes (fit in current spot is ideal, minimize ADP changes if not).
- Minimize software changes (discuss with John Clark and add details. May be minimized if we can stay in the same series.)
- Equal or better performance
- Same OAT and environmental requirements as the system.

 
7/14 Meeting
Actions-you should create subtasks for these. @Nadia Brown 
- Confirm with Victor have we exhausted all purchasing requirements. -in process
- What is ability to change parts or software wrt TIQUILA? Need to ask Sam+Maxime
- What is process to change parts or software wrt TIQUILA if required?Need to ask Sam+Maxime
- Scott/Nadia to evaluate fit of same interface boards? Other H264 cameras. Mechanical option is pretty rough for other options in the family
- John to scope changes to find something more modern to fit the form factor.
- Talk to John, Jai, and maybe Sam for who would know performance trades, best candidates for a replacement.


Victor 4/3/23 inventory 265 PCS in stock  = EM19821  =  ATOMAS MICRO INTERFACE BOARD
Lifetime buy made (and in progress). SA Camera and companion board.
Estimated replacement lead time is 3-4m


| Provided by Victor 3/23/23 |
| Rate 12  = 70% Airplane = 9 planes  per month (I rounded up) |
| Rate 15  = 70% Airplane = 11 planes per month (I rounded up) |
| Rate 20 =  70% Airplane = 14 planes per month ( The math worked out!) |
|  |
| 2023  Airplane demand:  132 to 153 airplanes  (this is the amount of airplanes in the budget to be delivered) |

## Comments (25)

### Cameron Chapman, 2023-04-05

@Maxime Jeanneau , I think we can keep this project assigned to you for now, but low priority until the date gets closer. If you run out of other work, you can start working on requirements and research for this project.

### Connor Peebles, 2023-04-12

Priority bumped up a little bit because of a chat with @Victor Vandor , maybe need a Jira for a re-design of the SA Cam

### Greg Fryer, 2023-05-15

AllCon, especially @Maxime Jeanneau I didn’t change anything, just moved to the ENG area. Once we start making a specific plan, we should have a brief discussion to figure out if this is as simple as drawing changes, or if it is a project that needs more structure.

### Cameron Chapman, 2023-05-16

Pretty sure it requires a new camera and board, so it should be a project. Changing to that.

### Cameron Chapman, 2023-06-19

@Nadia Brown this could be a good Summer project. You should talk to @Jaimal Hanson while you are here (he has a lot of knowledge about these), then start a requirements list in teams/electrical, then add a link to the description here. Threshold=need to have, objective=nice to have.

### Nadia Brown, 2023-06-22

@Scott Stuckey @Cameron Chapman 

Looking through the list of proposed alternatives, speaking with Jai, and the vendor, I have come across an issue. The proposed parts they have sent me are too large for the constrained space we currently have. While a redesign seemed inevitable, this will need a significant overhaul to the SA Pod Tray (107-101649) and therefore the Air Data Pod (107-101141).

Currently, the suggested Camera is a 12MP model that we have yet to receive further info on as the contact with InterTest is waiting to hear back from one of their own. All other cameras I have researched are slightly bigger and not quite what we want. I have also reached out to SONY in hopes of hearing back from them regarding a replacement, but have not received follow up yet.

The biggest move for concern however comes with the encoder board. The current size we use is a 2.16” x 0.9” board. The one they suggested to me appears to be IONODES ATOMAS-IOT-DUAL which is a 2.3” x 2.3” board. This is far too large. However, while at lunch, I heard back from InterTest about another board, IONODES ATOMAS-IOT, that measures in at 2.16” x 1.5”. This is smaller and would be of similar functionality, but the size is still far too large. I have added IONODES ATOMAS-IOT-DUAL into the vault under: IONODES ATOMAS-IOT-DUAL InterTest in the CAD folder and will attach it here.

Here is the ATOMAS-IOT-DUAL (in blue/white) overlaid in the current SA model.
[embedded file]
Here is the outline (Highlighted yellow with the black lines) of the ATOMAS-IOT-MICRO. I was not given a STEP file for this, but wanted to convey the sheer size of it.
[embedded file]
While the part could be moved back and we could shift the walls and holes of the SA Pod Tray back as seen in the picture below (circled in red), it would still encroach upon the space of the camera which currently looks like will need to be replaced by a larger size camera, unless the vaguely suggested camera they offer us is of similar size to the current model we are using.
[embedded file]
After speaking with Scott about this, we are planning to raise the level of priority of this to highest as this can greatly affect the TEQUILA project due to a redesign until we have a better understanding on how to best approach this.
[embedded file]

### Nadia Brown, 2023-07-05

Here is a suggested Camera Sensor from InterTest that they claim is compatible with the new board: https://www.ovt.com/products/ov12a/

### Cameron Chapman, 2023-07-26

Hi Victor,
 
Thanks for your patience on this as we conducted a thorough survey of all of our global partners for any remaining cameras and boards.
 
So here is where we’re at.
At a minimum, we can scrape together QTY 23 total cameras and boards without much hassle. The biggest constraint is the Atomas Micro board – more specifically, the NXP chip used for the board that was discontinued a while ago. This has always been the primary limiting factor for the board’s availability. I understand that QTY 23 falls well short of your preference for QTY 300.
 
So here is another option based on a very significant development in our search. The good news is that we found a source for a large quantity of NXP chips and equally important, IONODES is willing to do a final production run with these available chips. An obstacle is that we will have to pay a premium for the chips along with an MoQ for procurement and initiation of the build. But the bottom line is that this is a viable option and frankly speaking, very unexpected given the circumstances.
 
On the other hand, the Sony cameras are not easily sourced either, but we do believe we can obtain enough cameras through our network and reserve stash.
 
In short, we would need an MoQ of QTY 500 boards and cameras to get everyone on board and move forward with this option.
 
Please let me know if you are open to this volume. As these situations tend to be fluid, once I hear back from you, I will firm up details on our end so that I can provide pricing.
 
Best regards,
 
Eddie Park
Sales Engineer

InterTest, Inc. I 303 Route 94 I Columbia, NJ  07832   Headquarters
InterTest, Inc. I 445 South Figueroa Street, Suite 3100 I Los Angeles, CA  90071  Remote
Cell: +1 (213) 215-5838
www.intertest.com
ISO 9001:2015 Certified
 
From: Victor Vandor <vandor@jenaero.com> 
Sent: Monday, July 24, 2023 8:04 AM
To: Ryan Phraner <rphraner@intertest.com>; Eddie Park <epark@intertest.com>
Cc: Eddie Park <epark@intertest.com>; Nadia Brown <nbrown@edgeautonomy.io>
Subject: RE: Sony FCB-MA132
 
Eddie,
 
Please confirm if you were able to source these items for us.
 
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
 
 
From: Ryan Phraner <rphraner@intertest.com> 
Sent: Monday, July 17, 2023 2:01 PM
To: Victor Vandor <vandor@jenaero.com>
Cc: Eddie Park <epark@intertest.com>
Subject: RE: Sony FCB-MA132
 
Hi Victor,
 
Indeed!  Yes Eddie has already quoted you.  Apologies I did not recognize your email. 
 
The website you found for the MA132, Goldfinchway, is our legacy & used equipment site. 
 
Regards,
 
Ryan Phraner
Account Coordinator
 

InterTest, Inc. | 303 Route 94 | Columbia, NJ 07832
Office: (908)496-8008 | Fax: (908)496-8004
www.intertest.com
This e-mail message is confidential, may be privileged and is intended for the exclusive use of the addressee. If the reader of this message is not the intended recipient, or an employee or agent responsible for delivering this message to the intended recipient, you are hereby notified that any disclosure, distribution or reproduction of this e-mail message is strictly prohibited. If the addressee cannot be reached or is unknown to you, please inform the sender by return e-mail immediately and delete this e-mail message and destroy all copies. 
ISO 9001:2015 Certified
From: Victor Vandor <vandor@jenaero.com> 
Sent: Monday, July 17, 2023 4:56 PM
To: Ryan Phraner <rphraner@intertest.com>
Subject: RE: Sony FCB-MA132 
Importance: High
 
Hello Ryan,
 
We are the end user – it goes on our platform. 
 
I believe Eddie Park has been involved with our account.
 
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
 
 
From: Ryan Phraner <rphraner@intertest.com> 
Sent: Monday, July 17, 2023 12:53 PM
To: Victor Vandor <vandor@jenaero.com>
Subject: Sony FCB-MA132
 
Hello Victor,
 
Thank you for your inquiry.  We have fielded similar requests recently on the MA-132.  Who is the end user?
 
Regards,
 
Ryan Phraner
Account Coordinator
 

InterTest, Inc. | 303 Route 94 | Columbia, NJ 07832
Office: (908)496-8008 | Fax: (908)496-8004
www.intertest.com
This e-mail message is confidential, may be privileged and is intended for the exclusive use of the addressee. If the reader of this message is not the intended recipient, or an employee or agent responsible for delivering this message to the intended recipient, you are hereby notified that any disclosure, distribution or reproduction of this e-mail message is strictly prohibited. If the addressee cannot be reached or is unknown to you, please inform the sender by return e-mail immediately and delete this e-mail message and destroy all copies. 
ISO 9001:2015 Certified
 
 
From: Goldfinch Way (Shopify) <mailer@shopify.com> 
Sent: Friday, July 14, 2023 4:39 PM
To: info@goldfinchway.com
Subject: New customer message on July 14, 2023 at 4:39 pm
 
|  | You received a new message from your online store's contact form.   Country Code: ``` US ``` Name: ``` VICTOR PHELIPPE  VANDOR ``` Email: ``` vandor@jenaero.com ``` Phone Number: ``` 12522149153 ``` Comment: ``` PLEASE CONFIRM STOCK AVAILABILITY FOR THE Sony FCB-MA132 94º HFOV Micro HD Camera ``` ``` https://goldfinchway.com/products/sony-fcb-ma132-94%C2%BA-hfov-micro-hd-camera ``` ```   ``` ``` We are looking for 300 pcs ``` |  |

 
** WARNING: This email originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe. **
 
** WARNING: This email originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe. **
 
** WARNING: This email originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe. **

### Cameron Chapman, 2023-07-26

Hi @Victor Vandor ,
 
It sounds like they could produce 500 sets of current SA camera+boards, at a possibly high price. Given our lack of engineering bandwidth to develop a replacement soon, I think we should quote these 500 sets, or whatever price breaks they could reasonably produce.

### Greg Fryer, 2023-08-04

I approved the 2 year (at rate30) order, if nothing else to support TIQUILA without a change board. Will bring up with Scott K.

### Cameron Chapman, 2023-08-22

Hi Victor,
 
Did we execute this purchase? Can you please provide order details? https://jenaero.atlassian.net/browse/ENG-1735 
 
Thank you,
|  | Cameron Chapman Electrical Engineering Supervisor Edge Autonomy – SLO (formerly Jennings Aeronautics) Email: cchapman@edgeautonomy.io Phone: (970)389-5904 |

 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Victor Vandor <vvandor@edgeautonomy.io> 
Sent: Friday, August 4, 2023 1:33 PM
To: Greg Fryer <gfryer@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>; Nadia Brown <nbrown@edgeautonomy.io>; Scott Kirk <skirk@edgeautonomy.io>
Cc: Matt Philley <mphilley@edgeautonomy.io>; Ryan Stafford <rstafford@edgeautonomy.io>
Subject: RE: SA Camera Obsolete Parts: Purchase More (IMPORTANT!) 
Importance: High
 
We are aligned!  We will move forward with the purchase.
 
I got a small price discount just now, so I will counter and get this thing going!
 
Victor Vandor
Supply Chain Manager
Edge Autonomy
Previously Jennings Aeronautics
P: +1-805-544-0932
Email: vvandor@edgeautonomy.io

### Victor Vandor, 2023-08-22

We are discussing better price opportuities and last call will happen on 08/23 among Intertest and Edge to finalize what can be done.  We were able to improve the price  but still 5% off the target  (target price is the same price we paid last time)

### Cameron Chapman, 2023-08-24

Linking subtasks to parent

### Nadia Brown, 2023-08-28

From: Sam Miller <smiller@edgeautonomy.io>
Date: August 25, 2023 at 2:18:59 PM PDT
To: Allen Gardner <agardner@edgeautonomy.io>
Cc: Greg Fryer <gfryer@edgeautonomy.io>, Cameron Chapman <cchapman@edgeautonomy.io>
Subject: RE: SA camera
Allen,
We ordered 500 more Sony FCB-MA132 94 Deg HFOV cameras and ATOMAS Micro encoder boards yesterday, so we should be covered for a while.  Swapping in a new camera will be a significant effort requiring mechanical, electrical, and software resources.  When we kick that effort off, I would recommend that we take the opportunity to integrate a new Lowlight/NIR EO camera and an LWIR like a FLIR Lepton or Boson.  An articulated or separate downward-facing camera set might also come in handy for landing on boats.  I’m not sure what the NIIRS rating or frame rate for an Apriltag-based landing system would be – something to look into as part of requirements development.
For reference, the costs for our existing camera and boards are:
Sony FCB-MA132: $150
ATOMAS Micro encoder: $634
Thanks,
Sam
From: Allen Gardner <agardner@edgeautonomy.io> 
Sent: Friday, August 25, 2023 12:49 PM
To: Sam Miller <smiller@edgeautonomy.io>
Cc: Greg Fryer <gfryer@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Subject: SA camera
I saw this spam email below and remembered that we need a new SA camera on our bird. Who is looking into that for us?
From: Qimeng Zhao <qimeng.zhao@immervision.com> 
Sent: Friday, August 25, 2023 8:25 AM
To: Allen Gardner <agardner@edgeautonomy.io>
Subject: Remarkable features and benefits offered by Immervision low-light navigation camera module
Dear Allen,
I'm emailing because I would love your feedback about our low-light navigation camera module.
Do you know the remarkable features and benefits offered by the Immervision low-light navigation camera module?
- Wide-Angle: 190° Field of view for extended coverage

The 190 degrees field of view captures more information than most cameras available for such applications and allows manufacturers to reduce the number of sensors required to monitor the 360 degrees surroundings of the drone.
2. Low-Light: High performance in low-light conditions
Its sensitivity to low light improves the performance of navigation algorithms, allows for secure navigation from dawn-to-dusk and can eliminate the need to have to have additional illuminator source
3. Off-the-shelf: Solution ready for implementation with possibility of customization
The Immervision camera module is supported out-of-the-box by industry leading robotics platforms such as the Qualcomm® Robotics RB5, Qualcomm® Flight RB5 5G, and ModalAI® VOXL® 2. Drivers are available to facilitate the evaluation and minimize the integration effort by the drone providers.
4. Ruggedized
IP67 and first element in glass for usage in various environments, outdoors and indoors
5. Lightweight
Small footprint and lightweight for low impact on battery consumption, the Module Weight is under 5g.
You can find more information about the Immervision low-light navigation camera following this link: https://www.immervision.com/drone-uas-uav/docs/Brochure-Immervision-Drone-Camera-Module.pdf
Should you have any questions/requirements or would like to purchase a demonstration kit, please contact me directly.
Best regards,
Simon(Qimeng) Zhao
Sales and Business Development
T: +1 (514) 985-4007
C: +1 (514) 867-7986
qimeng.zhao@immervision.com
 
|  |  | Immervision Inc 2020 Robert-Bourassa Blvd., Suite 2320, Montreal (QC)  H3A 2A5 Canada immervision.com |

### Cameron Chapman, 2023-08-28

The PO has been sent.
 
Thanks,
 
Mike Jercich
Procurement Specialist
Edge Autonomy
Previously Jennings Aeronautics
P: +1-805-592-1163
Email: mjercich@edgeautonomy.io
 

 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Victor Vandor <vvandor@edgeautonomy.io> 
Sent: Thursday, August 24, 2023 9:42 AM
To: Cameron Chapman <cchapman@edgeautonomy.io>; Greg Fryer <gfryer@edgeautonomy.io>; Nadia Brown <nbrown@edgeautonomy.io>; Scott Kirk <skirk@edgeautonomy.io>; Michael Jercich <mjercich@edgeautonomy.io>
Cc: Matt Philley <mphilley@edgeautonomy.io>; Ryan Stafford <rstafford@edgeautonomy.io>
Subject: RE: SA Camera Obsolete Parts: Purchase More (IMPORTANT!) 
Importance: High
 
Good news! 
 
We got the prices down to a level we can survive! Total spend went from $462,000 to $391,000 = $71k savings
 
Michael, please issue a PO to Intertest :  monthly deliveries between December and June of 2024 -  500 pcs/7 months = around 70 boards a month
 
Thank You

### Greg Fryer, 2023-09-19

ALCON (@Victor Vandor @Mike Jercich @Cameron Chapman @Nadia Brown ) I closed this ticket as it was completed by the procurement. I created a separate problem to show the new run out date (asked Mike and Randy to comment if I was correct, and to update if not). Plan to address that starting Jan 2024. See the https://jenaero.atlassian.net/browse/VXEP-93 for further action.

### Matt Philley, 2024-02-07

@Kelly J Furlong @Ryan Ferguson @Brad Crampton @Ben Norris FYSA looks like we did a lifetime buy for these obsolete boards for the SA Camera.
We have 100-101235 ATOMAS-MICRO-CNCT boards in QA. Is there any particular testing we want to do before these go into inventory? Anyone from Production want to review them first…? It looks like they did not come with any specific paperwork for us to review. 
If not we can just do standard PCB incoming and call it good…? 
@Catherine Wagner FYSA

### Catherine Wagner, 2024-02-07

@Matt Philley Note that we do not have inspection requirements for these boards currently. We could inspect workmanship.

### Ryan Ferguson, 2024-02-07

@Matt Philley@Catherine Wagner These boards are tested nominally during the buildup and checkouts of the SA cams and air data pod.  I haven’t heard much about high failure rates of this board, so a standard PCB receiving inspection will probably be sufficient.

### Matt Philley, 2024-02-07

@Catherine Wagner I also spoke with Ben N and Kelly F they agreed standard PCB workmanship inspection and then inventory. No additional inspection or testing needed from Production.

### Greg Fryer, 2023-09-19

ALCON (@Victor Vandor @Mike Jercich @Cameron Chapman @Nadia Brown ) I closed this ticket as it was completed by the procurement. I created a separate problem to show the new run out date (asked Mike and Randy to comment if I was correct, and to update if not). Plan to address that starting Jan 2024. See the https://jenaero.atlassian.net/browse/VXEP-93 for further action.

### Matt Philley, 2024-02-07

@Kelly J Furlong @Ryan Ferguson @Brad Crampton @Ben Norris FYSA looks like we did a lifetime buy for these obsolete boards for the SA Camera.
We have 100-101235 ATOMAS-MICRO-CNCT boards in QA. Is there any particular testing we want to do before these go into inventory? Anyone from Production want to review them first…? It looks like they did not come with any specific paperwork for us to review. 
If not we can just do standard PCB incoming and call it good…? 
@Catherine Wagner FYSA

### Catherine Wagner, 2024-02-07

@Matt Philley Note that we do not have inspection requirements for these boards currently. We could inspect workmanship.

### Ryan Ferguson, 2024-02-07

@Matt Philley@Catherine Wagner These boards are tested nominally during the buildup and checkouts of the SA cams and air data pod.  I haven’t heard much about high failure rates of this board, so a standard PCB receiving inspection will probably be sufficient.

### Matt Philley, 2024-02-07

@Catherine Wagner I also spoke with Ben N and Kelly F they agreed standard PCB workmanship inspection and then inventory. No additional inspection or testing needed from Production.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IONODES ATOMAS-IOT-DUAL INTERTEST.sldasm | other | 27869 | 2023-06-22 | listed only |
| image-20230622-231513.png | image | 123 | 2023-06-22 | listed only |
| image-20230622-231848.png | image | 105 | 2023-06-22 | listed only |
| image-20230622-232159.png | image | 132 | 2023-06-22 | listed only |
