# RE_ Mod payload design responsibility question.msg

Attachment 10969, msg, 194 KB, added 2022-09-27 by Cameron Chapman.

From: "Curran, Matthew"
To: Cameron Chapman
Date: 2022-09-20 20:30:55-04:00
Subject: RE: Mod payload design responsibility question

I will get back to you with some clarification.

 

Matthew Curran

Lockheed Martin Aeronautics

Stalker UAS Program Manager

661-202-0193

Matthew.curran@lmco.com

 

From: Cameron Chapman <cchapman@edgeautonomy.io> 
Sent: Tuesday, September 20, 2022 1:39 PM
To: Curran, Matthew (US) <matthew.curran@lmco.com>
Cc: Justin Neel <jneel@edgeautonomy.io>; Will Harris <wharris@edgeautonomy.io>; Gamble, Dustin (US) <dustin.gamble@lmco.com>; Ryan Stafford <rstafford@edgeautonomy.io>; Kurt Burian <kburian@edgeautonomy.io>; Briana Hitchen <bhitchen@edgeautonomy.io>
Subject: EXTERNAL: RE: Mod payload design responsibility question

 

Hi Matt, 

 

Thank you for the information. Briana needs to order 10 AHRS for production orders. The V2 seems to be obsolete, but the obsolete notice says the following:

“2.2. Ellipse2-A, Ellipse2-E, Ellipse2-N impact of change

New hardware revision of box versions is 100% form, fit, and function compatible with existing Ellipse2-A, Ellipse2-E, and Ellipse2-N”

 

We have received a series 3 and are verifying if it is compatible. 

What do you recommend for these orders? Should we purchase and ship the V3 or hold for JHU approval? 

 

Thank you,



Cameron Chapman

Electrical Engineer

Edge Autonomy – SLO (formerly Jennings Aeronautics)

Mobile: +1 970-389-5904

Email: cchapman@edgeautonomy.io <mailto:cchapman@edgeautonomy.io> 

 

 

Confidentiality Notice

This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.

 

Export Control Notice

This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.

 

From: Curran, Matthew <matthew.curran@lmco.com <mailto:matthew.curran@lmco.com> > 
Sent: Tuesday, September 20, 2022 11:12 AM
To: Cameron Chapman <cchapman@edgeautonomy.io <mailto:cchapman@edgeautonomy.io> >
Cc: Justin Neel <jneel@edgeautonomy.io <mailto:jneel@edgeautonomy.io> >; Will Harris <wharris@edgeautonomy.io <mailto:wharris@edgeautonomy.io> >; Gamble, Dustin <dustin.gamble@lmco.com <mailto:dustin.gamble@lmco.com> >; Ryan Stafford <rstafford@edgeautonomy.io <mailto:rstafford@edgeautonomy.io> >; Kurt Burian <kburian@edgeautonomy.io <mailto:kburian@edgeautonomy.io> >
Subject: RE: Mod payload design responsibility question

 

JHU is working thru the approval process of getting a new IMU certified.

 

They are trying to get the Ellipse V3 certified.  We will let you know when it is certified and you will need to update your design baseline.

 

Matthew Curran

Lockheed Martin Aeronautics

Stalker UAS Program Manager

661-202-0193

Matthew.curran@lmco.com <mailto:Matthew.curran@lmco.com> 

 

From: Cameron Chapman <cchapman@edgeautonomy.io <mailto:cchapman@edgeautonomy.io> > 
Sent: Wednesday, September 14, 2022 1:38 PM
To: Justin Neel <jneel@edgeautonomy.io <mailto:jneel@edgeautonomy.io> >; Curran, Matthew (US) <matthew.curran@lmco.com <mailto:matthew.curran@lmco.com> >; Will Harris <wharris@edgeautonomy.io <mailto:wharris@edgeautonomy.io> >; Gamble, Dustin (US) <dustin.gamble@lmco.com <mailto:dustin.gamble@lmco.com> >; Ryan Stafford <rstafford@edgeautonomy.io <mailto:rstafford@edgeautonomy.io> >; Kurt Burian <kburian@edgeautonomy.io <mailto:kburian@edgeautonomy.io> >
Subject: EXTERNAL: Mod payload design responsibility question

 

Hi Matt,

 

What is the current status of mod payload design requirements. I know other companies previously selected and designed the main electronics. Are they responsible for selecting and qualifying new electronics, or is Edge/LM now? 

 

For this specific case, the original AHRS is obsolete. The new one should be 100% form, fit, and function compatible, but I don’t know if we are responsible for verifying that, if someone else is, or if anyone else has already tested the new one. 

 

Thank you,



Cameron Chapman

Electrical Engineer

Edge Autonomy – SLO (formerly Jennings Aeronautics)

Mobile: +1 970-389-5904

Email: cchapman@edgeautonomy.io <mailto:cchapman@edgeautonomy.io> 

 

 

Confidentiality Notice

This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.

 

Export Control Notice

This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.

 

From: Cameron Chapman 
Sent: Wednesday, September 14, 2022 1:33 PM
To: Briana Hitchen <bhitchen@edgeautonomy.io <mailto:bhitchen@edgeautonomy.io> >
Cc: Eileen Hongo <ehongo@edgeautonomy.io <mailto:ehongo@edgeautonomy.io> >; Kelly Furlong <kfurlong@edgeautonomy.io <mailto:kfurlong@edgeautonomy.io> >; Kyle DeBernardi <kdebernardi@edgeautonomy.io <mailto:kdebernardi@edgeautonomy.io> >; Victor Vandor <vvandor@edgeautonomy.io <mailto:vvandor@edgeautonomy.io> >
Subject: RE: MFG Change on SBG Ellipse-N

 

The requirements and designers for mod payload have always been vague to me, since another company selected and designed all of the electronics, but I think we are responsible for it now.

 

It looks like the new part should be an acceptable substitute. I would reorder one ASAP for testing to verify it works in our system. Depending on lead times, you may want to order enough to cover the 10/15 date + engineering test units as well. 

 

2.2. Ellipse2-A, Ellipse2-E, Ellipse2-N impact of change

New hardware revision of box versions is 100% form, fit, and function compatible with existing Ellipse2-A, Ellipse2-E, and Ellipse2-N

 



Cameron Chapman

Electrical Engineer

Edge Autonomy – SLO (formerly Jennings Aeronautics)

Mobile: +1 970-389-5904

Email: cchapman@edgeautonomy.io <mailto:cchapman@edgeautonomy.io> 

 

 

Confidentiality Notice

This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.

 

Export Control Notice

This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.

 

From: Briana Hitchen <bhitchen@edgeautonomy.io <mailto:bhitchen@edgeautonomy.io> > 
Sent: Wednesday, September 14, 2022 11:25 AM
To: Cameron Chapman <cchapman@edgeautonomy.io <mailto:cchapman@edgeautonomy.io> >
Cc: Eileen Hongo <ehongo@edgeautonomy.io <mailto:ehongo@edgeautonomy.io> >; Kelly Furlong <kfurlong@edgeautonomy.io <mailto:kfurlong@edgeautonomy.io> >; Kyle DeBernardi <kdebernardi@edgeautonomy.io <mailto:kdebernardi@edgeautonomy.io> >; Victor Vandor <vvandor@edgeautonomy.io <mailto:vvandor@edgeautonomy.io> >
Subject: MFG Change on SBG Ellipse-N
Importance: High

 

Hi Cameron,

 

I went to reorder part # 111-104685 / Vendor part # 100-1474 and they have had a change to part #100-2504. Can you please review and advise if the new part # is acceptable for the Mod Payload? Production is trying to ship these out by 10/15, so I need to get these on order ASAP. 

 

Link to new specs:

https://files.sbg-systems.com/s/groC80um5XTjR0G

 

Briana Hitchen

Procurement Specialist

Edge Autonomy 

Previously Jennings Aeronautics

P: +1-805-592-1190



Confidentiality Notice

This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.

 

Export Control Notice

This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.

 

** WARNING: This email originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe. **

 

** WARNING: This email originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe. **

Attached to this email (not converted): image001.png, image002.jpg
