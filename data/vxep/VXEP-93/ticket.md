# VXEP-93: Replace SA Camera EM18911 (100-100835) and EM19821 (100-101235) are obsolete. due February 2025.

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-09-19
- **Updated:** 2025-05-13
- **Resolved:** 2025-05-13
- **Due:** 2025-02-28
- **Reporter:** Greg Fryer
- **Assignee:** Grant Goodman
- **Creator:** Greg Fryer
- **Labels:** EndOfLife, GFProject, Production-Priority, Raj
- **Parent:** VXEP-266 VXE (all) ADP: Heated Pitot/New SA CAM/Remove other obsolete components
- **Links:** relates to VXEP-94 (SA Camera EM18911 (100-100835) and EM19821 (100-101235) are obsolete (closed with buy)); is blocked by VA-124 (SA Cam Replacement Define and document requirements. ); relates to VA-989 (Evaluate alternate SA cameras); relates to ENGPRJA-46 (Air data pod design improvements - heated pitot tube); relates to VXEP-266 (VXE (all) ADP: Heated Pitot/New SA CAM/Remove other obsolete components); relates to XKIT-2037 (Identify look down camera option(s))
- **Epic Status:** To Do
- **Epic Color:** ghx-label-8
- **Issue color:** dark_purple
- **Part Number(s):** 100-100835 100-101235
- **Production Stakeholder:** Emalee Johnson
- **Supply Chain Stakeholder:** Kenneth Weber
- **Problem Type:** Part Obsolescence
- **Leadership Stakeholder:** Sam Miller
- **Severity:** 2 - Degraded Performance - No Workaround
- **Job Number:** J100078 - Sustainment: VXE-30

## Description

Shared Folder:
New: 2024 Air Data Pod Updates
Old.SA Camera Replacement  Please move to new.
Block Diagram Block Diagram Heated Pitot.vsdx
Requirements and Trade Study: 2024 ADP Requirements.xlsx
Replacing components in this assembly (attached). 107-101649 SA Camera Tray Assy_B.pdf
NHA 107-101141 Air Data Pod Assy_F.pdf
Production impact has been delayed by a lifetime buy expected to support operation through 2024. However the project to replace the camera is still required as availability will drop (potentially to zero) and cost will certainly rise.

Plan:
- Requirements
- Trade study
- See if what penguin uses would be a good choice.
- Downselect.
- Design process

## Plan

SA Camera Actions 10/15
- Order ionodes to HSV and repair the one here.
- Evaluate if Ionodes meets requirements in HSV. Buy at least 2. Get the manual. Buy 3.  3 for HSV to 4.
- Identify top 3-7 cameras.
- Hide the remaining on the sheet.
- Identify an interface board that will work for each. Discard if nothing easy. Vendors and mfrs can help with this.
- Buy cameras and interface boards that could work by 10/21. Ideally sooner.
- Schedule tagup 10/21 to status order
- Downselect replacement.
- Design and integrate replacement. Ideally combine with redesign required for heated pitot. https://jenaero.atlassian.net/browse/VXEP-266

SA Camera remaining tasks-12/19:
- Integrate Omron MIPI camera- Sightline received the camera and will provide us with updated software.
- New Latency and Power measurements with Omron MIPI camera. Earlier tests used Raspberry Pi MIPI camera with 2.0 interface board.
- Image comparison: Depth of field, Viewing angel and low light operation.
- Test Boson FLIR with Sightline 1750 board and FLIR interface board. Done. Needed additional license. FLIR is working.
- ADP Harness redlines and deliver it to CAD team for drafting. Done. Will scan and have Cameron review it.
- Work with Manufacturing for Micro D-sub and Molex Clamshell connector harness wiring.  Done. Will have Cameron review it and give it to Gary for drafting.
- Fit check with new ADP housing
- Thermal analysis and measurement in new SA camera housing.
- Hand over a Sightline setup to Software team. Quick start guide here: Sightline Quick Start Guide.docx

## Issue Status

11/18 Runout status: If purchase is successful, these will fulfill demand through most of June 2025. This is with increasing June and July to 20 units each month.

## Comments (33)

### Cameron Chapman, 2024-02-16

Raj is a EE starting on Monday. Unless other projects jump in front of this one, I was planning on having him start on this project to help select a replacement.

### Cameron Chapman, 2024-02-21

@Kenneth Weber @Sandra Lopez I heard we lost 15 units to scrap recently. Are you able to provide an updated run out date for the current SA Cams?

### Cameron Chapman, 2024-02-21

Can you please add any potential candidates to the columns on the right of this requirements sheet, and fill in how they compare. Adding Eric, who has helped with the Mechanical side of this, and Nadia who worked on it previously.  SA Camera SSS DRAFT.xlsx
Please comment in this JIRA project as you progress and tag people using the @ symbol who you want to notify with each comment. . https://jenaero.atlassian.net/browse/VA-124 
| SA Cam Replacement Define and document requirements. VXE_Aircraft / VA-124   Status DONE   Assigned to  Travis Storm Priority High https://jenaero.sharepoint.com/:x:/r/sites/EngineeringTeam/Shared%20Documents/Systems%20Engineering/VXE2024/VXE2024%20Requirements%20Verification%20Traceability%20Matrix%20(RVTM).xlsm?d=wfe740775ff3f44bc9517b17bc7ade1af&amp;csf=1&amp;web=1&amp;e=InaIcd  https://jenaero.atlassian.net/wiki/spaces/EF/pages/111149057/SA+Camera+SSS  Initial list (we can add more and transfer to excel format. See vault templates). here is an example VXE X-kit Requirements.xlsx Target requirements are essentially. ``` Minimize mechanical changes (fit in current spot is ideal, minimize ADP changes if not). ``` ``` Minimize software changes (discuss with John Clark and add details. May be minimized if we can stay in the same series.) ``` ``` Equal or better performance ``` ``` Same OAT and environmental requirements as the system. ``` ```   ``` ```     If we need to replace the interface board, make sure it does not overheat. ``` ```   ``` ```   ``` ``` See parent ticket for more. ```   Open in Jira |

 
 
Thank you,
|  | Cameron Chapman Electrical Engineer Edge Autonomy – SLO (formerly Jennings Aeronautics) Email: cchapman@edgeautonomy.io Phone: (970)389-5904 |

 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Raj Budhabhatti <rbudhabhatti@edgeautonomy.io> 
Sent: Wednesday, February 21, 2024 11:05 AM
To: Cameron Chapman <cchapman@edgeautonomy.io>
Subject: MA-132 camera status
 
Good morning Cameron,
I found a supplier (IVS Imaging in Texas) that may have SA-132 cameras in stock. I have reached out to them for quote and stock. Once I have this information, I will pass it to our purchasing.
I have also reached out to several suppliers for a replacement or upgrade for MA-132 with similar features and formfactor. Once I have this data, I will compare it with the MA-132 spec and make recommendations. Attached, please find the status and list of suppliers.
Thank you,
Raj

### Cameron Chapman, 2024-02-21

@Rajesh Budhabhatti please see project order in the description and plan fields.

### Rajesh Budhabhatti, 2024-02-21

Can we use SA-130? It is smaller and has autofocus. @Eric Rinell @Nadia Brown I have attached the datasheet for your reference.

### Greg Fryer, 2024-02-22

@Rajesh Budhabhatti @Cameron Chapman Based on that last email, can we put this project on hold? We would integrate effort to replace the camera into the Havoc/VXE 2024 new Air Data Pod https://jenaero.atlassian.net/browse/VXEP-266. There will be a parallel VXE30 new ADP to get just heated pitot, but we can just stick with the same camera to limit change (unless it is actually net easier to change both). Open to discussion.
If you agree, please cancel this (with 500 qty, our run out moves out past 2026 I think, so no issue).

### Emalee Johnson, 2024-02-22

@Greg Fryer Our current inventory is 85, where are you seeing qty 500 for 100-100835?

### Greg Fryer, 2024-02-22

@Emalee Johnson The vendor that took the order for qty 500 (lifetime buy) just came back this morning and said they found a source. Def not in inventory yet.

### Cameron Chapman, 2024-02-22

@Kenneth Weber can you please confirm the ETA for the order, now that the supplier can fill our demand? Can you also please provide an updated runout projection of these two components? That will set the due date for this project. 
Placing this one on hold until then. FYI @Rajesh Budhabhatti. You are still welcome to document the current options vs requirements while the information is fresh, but please hold on work past that until further notice.
[embedded file]

### Rajesh Budhabhatti, 2024-02-22

OK, will do.
From: Cameron Chapman (Jira) <jira@jenaero.atlassian.net>
Sent: Thursday, February 22, 2024 10:23 AM
To: Raj Budhabhatti <rbudhabhatti@edgeautonomy.io>
Subject: [JIRA] Cameron Chapman mentioned you on https://jenaero.atlassian.net/browse/VXEP-93#icft=VXEP-93
You don't often get email from jira@jenaero.atlassian.net. Learn why this is important<https://aka.ms/LearnAboutSenderIdentification>
Cameron Chapman mentioned you on an issue
VXE Problems/https://jenaero.atlassian.net/browse/VXEP-93#icft=VXEP-93 SA Camera EM18911 (100-100835) and EM19821 (100-101235) are obsolete  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌
Cameron Chapman mentioned you on an issue
VXE Problems<https://jenaero.atlassian.net/browse/VXEP?atlOrigin=eyJpIjoiOGYwY2VkMjJhNjdmNDNhNzhhMTAxMzQ4ZTg1NDA0ZTciLCJwIjoiaiJ9>
/
VXEP-93<https://jenaero.atlassian.net/browse/VXEP-93?atlOrigin=eyJpIjoiOGYwY2VkMjJhNjdmNDNhNzhhMTAxMzQ4ZTg1NDA0ZTciLCJwIjoiaiJ9>
SA Camera EM18911 (100-100835) and EM19821 (100-101235) are obsolete <https://jenaero.atlassian.net/browse/VXEP-93?atlOrigin=eyJpIjoiOGYwY2VkMjJhNjdmNDNhNzhhMTAxMzQ4ZTg1NDA0ZTciLCJwIjoiaiJ9>
[Image removed by sender.]
Cameron Chapman 10:23 AM PST
@Kenneth Weber can you please confirm the ETA for the order, now that the supplier can fill our demand? Can you also please provide an updated runout projection of these two components? That will set the due date for this project.
Placing this one on hold until then. FYI @Rajesh Budhabhatti. You are still welcome to document the current options vs requirements while the information is fresh, but please hold on work past that until further notice.
[cid:image001.png@01DA6579.60D9B6E0]
[View issue]
Get Jira notifications on your phone! Download the Jira Cloud app for Android<https://play.google.com/store/apps/details?id=com.atlassian.android.jira.core&referrer=utm_source%3DNotificationLink%26utm_medium%3DEmail> or iOS<https://itunes.apple.com/app/apple-store/id1006972087?pt=696495&ct=EmailNotificationLink&mt=8>.
Manage notifications<https://jenaero.atlassian.net/jira/settings/personal/notifications?emailPreferences=true&atlOrigin=eyJpIjoiOGYwY2VkMjJhNjdmNDNhNzhhMTAxMzQ4ZTg1NDA0ZTciLCJwIjoiaiJ9#emailpreferences>  •  Give feedback<https://surveys.atlassian.com/jfe/form/SV_9X3zi1X4q1gKsqF>  •  Privacy policy<https://www.atlassian.com/legal/privacy-policy>
[cid:image003.png@01DA6579.60D9B6E0]
[cid:image003.png@01DA6579.60D9B6E0]
- - WARNING: This email originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe. **

### Cameron Chapman, 2024-02-22

Hi Emalee,
 
David is reaching out to the vendor and will give us an update tomorrow. This is for PO 230824-05.
 
My understanding is that it is still open.
 
Regards,
 
|  | Ken Weber Supply Chain Manager Edge Autonomy – San Luis Obispo, CA Phone: +1-832-326-0866 (mobile) Email: kweber@edgeautonomy.io 831 Buckley Road, San Luis Obispo, CA 93401 |

 
Confidentiality Notice 
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments. 
 
Export Control Notice 
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government. 
 
From: Emalee Johnson <ejohnson@edgeautonomy.io> 
Sent: Thursday, February 22, 2024 2:16 PM
To: Ken Weber <kweber@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Cc: David Johantgen <djohantgen@edgeautonomy.io>; Greg Fryer <gfryer@edgeautonomy.io>
Subject: RE: [JIRA] Cameron Chapman mentioned you on VXEP-93
 
Hey Ken,
 
It looks like Cameron and Greg weren’t on that original email.
 
According to the Jira ticket Greg is saying we have 500 additional Cameras on order. I see in this attachment that there was a cancelled PO, PO 230824-05.
 
Is there a new PO of qty of 500 for 100-100835? If so, what is our ETA?
 
|  | Emalee Johnson Production Engineer Edge Autonomy – SLO https://edgeautonomy.io/ Email: ejohnson@edgeautonomy.io |

### Cameron Chapman, 2024-02-23

Emalee,
 
I spoke with the supplier today and they will be able to support the PO after all. They said they would give me a schedule on when they plan to ship cameras.
 
 
|  | David Johantgen Procurement Specialist III Edge Autonomy 831 Buckley Road, SLO, CA 93401 Office: +1 805.868-0201 Email: djohantgen@edgeautonomy.io |

### Cameron Chapman, 2024-02-23

Greg,
 
Good news. 280 cameras are shipping out next week. That will bring them up to schedule. They will ship per PO : April1, May 1 and June 1.
 
I’ll reload the PO 230824-05
 
 
|  | David Johantgen Procurement Specialist III Edge Autonomy 831 Buckley Road, SLO, CA 93401 Office: +1 805.868-0201 Email: djohantgen@edgeautonomy.io |

### Cameron Chapman, 2024-07-09

Latest projections per Perry are that we’ll run out in December-January. @Perry Richardson @Greg Fryer does our development plan match this?

### Greg Fryer, 2024-07-09

@Cameron Chapman Let’s see if any of the project engineers have bandwidth to pick this up. I do not know if we need two solutions (or two implementations of hte same solution) one with heated pitot and one without. Probably depends on the burden (any power in normal conditions, any weight)?
Not sure I’m answering your question.
@Carl Graf @Scott Whitney @Grant Goodman @Ryan Babigian

### Greg Fryer, 2024-07-10

I asked @Grant Goodman to start building/tracking the plan for this. Covering the linked set of issues:
- Obsolete SA Camera for VXE30 STD ADP
- Integrate into Heated Pitot for VXE30 STD ADP
- Integrate into VXE30 Havoc ADP
- (Hopefully) also act as a look-down camera for VXE30 Havoc (perhaps different config, certainly different mounting). Also optional (e.g. only if that is selected as needed for exotic landings, or if it has other value.)

### Rajesh Budhabhatti, 2024-08-26

Meeting scheduled 9/10 at 9:00 am with Brian Harrison and Eddie Park from Intertest to identify potential replacements for current SA cameras. We may be needing two cameras per vehicle.

### Perry Richardson, 2024-09-10

Just an Update on the SA Camera and stock runout.  A current demand today we have stock to cover until end of February 2025.

### Cameron Chapman, 2024-12-02

@Perry Richardson @Grant Goodman did you complete the Czech purchase? Can you please update a new runout date when complete?

### Perry Richardson, 2024-12-02

Cameron
Will have an answer to you in the morning. Still trying to get documents in place to send the $$$$$.
[A picture containing icon  Description automatically generated]
Perry Richardson
Procurement Specialist
Edge Autonomy – San Luis Obispo, CA
Phone: +1-805-592-1163 x123
Email : prichardson@edgeautonomy.io
831 Buckley Road, San Luis Obispo, CA 93401

### Greg Fryer, 2024-02-22

@Emalee Johnson The vendor that took the order for qty 500 (lifetime buy) just came back this morning and said they found a source. Def not in inventory yet.

### Cameron Chapman, 2024-02-22

@Kenneth Weber can you please confirm the ETA for the order, now that the supplier can fill our demand? Can you also please provide an updated runout projection of these two components? That will set the due date for this project. 
Placing this one on hold until then. FYI @Rajesh Budhabhatti. You are still welcome to document the current options vs requirements while the information is fresh, but please hold on work past that until further notice.
[embedded file]

### Rajesh Budhabhatti, 2024-02-22

OK, will do.
From: Cameron Chapman (Jira) <jira@jenaero.atlassian.net>
Sent: Thursday, February 22, 2024 10:23 AM
To: Raj Budhabhatti <rbudhabhatti@edgeautonomy.io>
Subject: [JIRA] Cameron Chapman mentioned you on https://jenaero.atlassian.net/browse/VXEP-93#icft=VXEP-93
You don't often get email from jira@jenaero.atlassian.net. Learn why this is important<https://aka.ms/LearnAboutSenderIdentification>
Cameron Chapman mentioned you on an issue
VXE Problems/https://jenaero.atlassian.net/browse/VXEP-93#icft=VXEP-93 SA Camera EM18911 (100-100835) and EM19821 (100-101235) are obsolete  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌
Cameron Chapman mentioned you on an issue
VXE Problems<https://jenaero.atlassian.net/browse/VXEP?atlOrigin=eyJpIjoiOGYwY2VkMjJhNjdmNDNhNzhhMTAxMzQ4ZTg1NDA0ZTciLCJwIjoiaiJ9>
/
VXEP-93<https://jenaero.atlassian.net/browse/VXEP-93?atlOrigin=eyJpIjoiOGYwY2VkMjJhNjdmNDNhNzhhMTAxMzQ4ZTg1NDA0ZTciLCJwIjoiaiJ9>
SA Camera EM18911 (100-100835) and EM19821 (100-101235) are obsolete <https://jenaero.atlassian.net/browse/VXEP-93?atlOrigin=eyJpIjoiOGYwY2VkMjJhNjdmNDNhNzhhMTAxMzQ4ZTg1NDA0ZTciLCJwIjoiaiJ9>
[Image removed by sender.]
Cameron Chapman 10:23 AM PST
@Kenneth Weber can you please confirm the ETA for the order, now that the supplier can fill our demand? Can you also please provide an updated runout projection of these two components? That will set the due date for this project.
Placing this one on hold until then. FYI @Rajesh Budhabhatti. You are still welcome to document the current options vs requirements while the information is fresh, but please hold on work past that until further notice.
[cid:image001.png@01DA6579.60D9B6E0]
[View issue]
Get Jira notifications on your phone! Download the Jira Cloud app for Android<https://play.google.com/store/apps/details?id=com.atlassian.android.jira.core&referrer=utm_source%3DNotificationLink%26utm_medium%3DEmail> or iOS<https://itunes.apple.com/app/apple-store/id1006972087?pt=696495&ct=EmailNotificationLink&mt=8>.
Manage notifications<https://jenaero.atlassian.net/jira/settings/personal/notifications?emailPreferences=true&atlOrigin=eyJpIjoiOGYwY2VkMjJhNjdmNDNhNzhhMTAxMzQ4ZTg1NDA0ZTciLCJwIjoiaiJ9#emailpreferences>  •  Give feedback<https://surveys.atlassian.com/jfe/form/SV_9X3zi1X4q1gKsqF>  •  Privacy policy<https://www.atlassian.com/legal/privacy-policy>
[cid:image003.png@01DA6579.60D9B6E0]
[cid:image003.png@01DA6579.60D9B6E0]
- - WARNING: This email originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe. **

### Cameron Chapman, 2024-02-22

Hi Emalee,
 
David is reaching out to the vendor and will give us an update tomorrow. This is for PO 230824-05.
 
My understanding is that it is still open.
 
Regards,
 
|  | Ken Weber Supply Chain Manager Edge Autonomy – San Luis Obispo, CA Phone: +1-832-326-0866 (mobile) Email: kweber@edgeautonomy.io 831 Buckley Road, San Luis Obispo, CA 93401 |

 
Confidentiality Notice 
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments. 
 
Export Control Notice 
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government. 
 
From: Emalee Johnson <ejohnson@edgeautonomy.io> 
Sent: Thursday, February 22, 2024 2:16 PM
To: Ken Weber <kweber@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Cc: David Johantgen <djohantgen@edgeautonomy.io>; Greg Fryer <gfryer@edgeautonomy.io>
Subject: RE: [JIRA] Cameron Chapman mentioned you on VXEP-93
 
Hey Ken,
 
It looks like Cameron and Greg weren’t on that original email.
 
According to the Jira ticket Greg is saying we have 500 additional Cameras on order. I see in this attachment that there was a cancelled PO, PO 230824-05.
 
Is there a new PO of qty of 500 for 100-100835? If so, what is our ETA?
 
|  | Emalee Johnson Production Engineer Edge Autonomy – SLO https://edgeautonomy.io/ Email: ejohnson@edgeautonomy.io |

### Cameron Chapman, 2024-02-23

Emalee,
 
I spoke with the supplier today and they will be able to support the PO after all. They said they would give me a schedule on when they plan to ship cameras.
 
 
|  | David Johantgen Procurement Specialist III Edge Autonomy 831 Buckley Road, SLO, CA 93401 Office: +1 805.868-0201 Email: djohantgen@edgeautonomy.io |

### Cameron Chapman, 2024-02-23

Greg,
 
Good news. 280 cameras are shipping out next week. That will bring them up to schedule. They will ship per PO : April1, May 1 and June 1.
 
I’ll reload the PO 230824-05
 
 
|  | David Johantgen Procurement Specialist III Edge Autonomy 831 Buckley Road, SLO, CA 93401 Office: +1 805.868-0201 Email: djohantgen@edgeautonomy.io |

### Cameron Chapman, 2024-07-09

Latest projections per Perry are that we’ll run out in December-January. @Perry Richardson @Greg Fryer does our development plan match this?

### Greg Fryer, 2024-07-09

@Cameron Chapman Let’s see if any of the project engineers have bandwidth to pick this up. I do not know if we need two solutions (or two implementations of hte same solution) one with heated pitot and one without. Probably depends on the burden (any power in normal conditions, any weight)?
Not sure I’m answering your question.
@Carl Graf @Scott Whitney @Grant Goodman @Ryan Babigian

### Greg Fryer, 2024-07-10

I asked @Grant Goodman to start building/tracking the plan for this. Covering the linked set of issues:
- Obsolete SA Camera for VXE30 STD ADP
- Integrate into Heated Pitot for VXE30 STD ADP
- Integrate into VXE30 Havoc ADP
- (Hopefully) also act as a look-down camera for VXE30 Havoc (perhaps different config, certainly different mounting). Also optional (e.g. only if that is selected as needed for exotic landings, or if it has other value.)

### Rajesh Budhabhatti, 2024-08-26

Meeting scheduled 9/10 at 9:00 am with Brian Harrison and Eddie Park from Intertest to identify potential replacements for current SA cameras. We may be needing two cameras per vehicle.

### Perry Richardson, 2024-09-10

Just an Update on the SA Camera and stock runout.  A current demand today we have stock to cover until end of February 2025.

### Cameron Chapman, 2024-12-02

@Perry Richardson @Grant Goodman did you complete the Czech purchase? Can you please update a new runout date when complete?

### Perry Richardson, 2024-12-02

Cameron
Will have an answer to you in the morning. Still trying to get documents in place to send the $$$$$.
[A picture containing icon  Description automatically generated]
Perry Richardson
Procurement Specialist
Edge Autonomy – San Luis Obispo, CA
Phone: +1-805-592-1163 x123
Email : prichardson@edgeautonomy.io
831 Buckley Road, San Luis Obispo, CA 93401

## Attachments (18)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [28mm Board Camera.pdf](attachments/18571_28mm%20Board%20Camera.pdf.md) | pdf | 344 | 2024-01-31 | converted |
| image-20240201-005303.png | image | 392 | 2024-01-31 | listed only |
| image-20240202-185013.png | image | 196 | 2024-02-02 | listed only |
| side by side (002)-20240202-072116.jpg | image | 2536 | 2024-02-02 | listed only |
| [RE_ 100-100835 (SA Camera) - estimated run-out date_.msg](attachments/18610_RE_%20100-100835%20(SA%20Camera)%20-%20estimated%20run-out%20date_.msg.md) | msg | 226 | 2024-02-05 | converted |
| [107-101141 Air Data Pod Assy_F.pdf](attachments/18916_107-101141%20Air%20Data%20Pod%20Assy_F.pdf.md) | pdf | 341 | 2024-02-21 | converted |
| [107-101649 SA Camera Tray Assy_B.pdf](attachments/18907_107-101649%20SA%20Camera%20Tray%20Assy_B.pdf.md) | pdf | 195 | 2024-02-21 | converted |
| [FCB-Micro-print-ready-brochure.pdf](attachments/18914_FCB-Micro-print-ready-brochure.pdf.md) | pdf | 824 | 2024-02-21 | converted |
| [RE_ Atomos Micro order.msg](attachments/18915_RE_%20Atomos%20Micro%20order.msg.md) | msg | 268 | 2024-02-21 | converted |
| image-20240222-182058.png | image | 5 | 2024-02-22 | listed only |
| image001.png | image | 4 | 2024-02-22 | listed only |
| image003.png | image | 4 | 2024-02-22 | listed only |
| image004.png | image | 1 | 2024-02-22 | listed only |
| ~WRD0458.jpg | image | 1 | 2024-02-22 | listed only |
| image001.png | image | 9 | 2024-12-02 | listed only |
| image003.png | image | 0 | 2024-12-02 | listed only |
| image004.png | image | 4 | 2024-12-02 | listed only |
| image005.png | image | 1 | 2024-12-02 | listed only |
