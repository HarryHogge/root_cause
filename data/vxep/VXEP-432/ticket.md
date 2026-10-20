# VXEP-432: Define Lifetime Fail Criteria for AS150 Anti spark connector resistance

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2024-06-11
- **Updated:** 2026-09-30
- **Resolved:** 2026-09-30
- **Reporter:** Hayden Jeanor
- **Creator:** Hayden Jeanor
- **Links:** relates to VA-573 (Poor Quality/higher impedance plating on AS150 power contacts - Containment and Corrective Action); relates to VXEP-539 (Main battery (s/n: 3-1976) connector heated up while plugged into V692)
- **Issue Status:** Determined fail criteria based off of best estimate - biasing towards sparking within passing criteria

## Description

Problem reported by A. Bertulis: 
So recently a few of our asset vehicles had dead resistors in the battery connectors. One of them was a visually sparking main battery connector on the fuselage side, and another one was a center wing AS150 connector that just measured really low resistance compared to other vehicles and we assume that might cause sparking too.
 
Anyway, we want to add a check for our 50 (or 100) cycle inspections, to measure the resistance of both battery connectors to determine if they’re good or not and we’d like to know the “acceptable” range so we can start using that info internally and potentially put it in the manuals for customers in the future.
We can measure the connectors of the new vehicles and get a range from that, but I’d like to get the correct acceptable range from engineering. Please let us know if you can help with this.

Nominal Anti Spark Ressitance = 6 Ohms

2 Ohms - 10 Ohms can be classified as acceptable for that connector. Any resistance outside of that range should be flagged for replacement.

## Plan

- Determine Fail criteria - ENG
- Implement changes in SCO - FLOPS
- Document any failures of criteria - FLOPS
- sparking within passing criteria
- no sparking within failing criteria
- Makes adjustments to criteria - ENG
- Push changes to customer documentation - FLOPS

## Comments (14)

### Artis Bertulis, 2024-06-11

@Hayden Jeanor I only have a recent example (see below), the top picture is a brand-new cable from stock (5.9 Ohms), and the bottom one (0.7 Ohms) is the one that got replaced.

[embedded: image-20240611-165317.png]

### Hayden Jeanor, 2024-06-11

@Artis Bertulis That data is very helpful. The failure actually measured 0.7 kOhms = 700Ohms. This still results in sparking, just at a different location on the connector, but it is helpful to better characterize how they are failing

### Hayden Jeanor, 2024-06-11

ran through the shop and dyno area to get a rough data set of AS150’s throughout its lifecycle. 
V481 CW = 8.4
V481Fuse = 5.9
V371 fuse= 6
V371 CW = 6.1
V376 CW = 6.3
V604 CW = OC
Known sparking fuse contact on V376 = 500k
Random connector in shop = OC
Rest of connectors in shop/dyno(~qty 20)= ~5.8-6.3

The interesting about this was that the failed contacts didnt seem to have very many matting cycles on it - i plan on pulling 100 contacts from inventory to see if there are any non-conforming contacts straight from the supplier @Catherine Wagner please let me know if quality already does a check like this upon receipt

### Hayden Jeanor, 2024-06-11

@Cyrus Blevins did you find any connectors outside the range of 5.5-6.5 Ohms from the inventory pull?

### Cyrus Blevins, 2024-06-11

@Hayden Jeanor All of the ones in the bag you gave me fell between ~5.8-6.2 Ohms

### Catherine Wagner, 2024-06-12

@Hayden Jeanor No testing is performed on contacts at receipt. We do visual inspection and source verification (ensuring they’re from AMASS). Looping in @Matt Philley to potentially add to inspection sheet if deemed necessary.

### Matt Philley, 2024-06-12

@Catherine Wagner @Hayden Jeanor yep no receiving testing was determined to be necessary during that big 8D because we were testing the Dual Current Sense assemblies and we use those AS150 contacts elsewhere where it was determined there was no concern.
The current receiving inspection process is outlined in the Inspection Sheet available by the PN

### Hayden Jeanor, 2024-06-14

@Cyrus Blevins  i have devised a testing ckt that will help us determine a fail criteria. Can you please perform test with my assistance.  

[embedded: Image-20240614-162225.jfif]
Rough procedure:
- Build harnesses required for test
- Safety: there will be sparking in this test. Wear safety glasses and gloves.
- set PS to 29.4V w/ a current limit of 1A but turn the output off.
- connect all AS150 connectors as shown in circuit except for the AS150 positive pair that has Ras in parallel. Connect it to the FW propulsion system on the IB.
- Set Ras to 6Ohms.
- With the positive AS150 pair still disconnected, turn PS output on.
- Slowly bring the positive AS150 pair to mate and observe if any sparking occurs. None should occur with the pot set at 6Ohms.
- Repeat steps 5-7 but with Ras swept across a range of 0-50 Ohms @ one ohm increments. Do not start @ 0 ohms, instead start at 6 ohms and increase/decrease in 1ohm increments/decrements.
- repeat steps 4-8 for the lift propulsion system on the IB.

### Hayden Jeanor, 2024-06-21

Found a flaw in the test circuit, so not doing it the official way. Going the quick and dirty route. @Artis Bertulis  2 Ohms - 50 Ohms can be classified as acceptable for that connector. Any resistance outside of that range should be flagged for replacement.

### Cameron Chapman, 2024-07-01

@Hayden Jeanor reopening. This task is not done until the check has been implemented and documented. 
Pasting email chain. 
Good morning, 
I am catching up after a week off. A few follow up questions? 
- Do we have any wording in any document about reporting battery connections that spark when mating? We should add that along with any periodic test we determine.
- Do operators have a multimeter and leads in any of their flight kits?
- We are planning to replace these contacts, but it is a large project. https://jenaero.atlassian.net/browse/VA-573

Thank you,
Cameron Chapman
 
From: Hayden Jeanor <hjeanor@edgeautonomy.io>
Sent: Friday, June 28, 2024 2:21 PM
To: Dana Holley <dholley@edgeautonomy.io>; Artis Bertulis <abertulis@edgeautonomy.io>; Grace Burgess <gburgess@edgeautonomy.io>; Greg Nichols <gnichols@edgeautonomy.io>; Catherine Wagner <cwagner@edgeautonomy.io>
Cc: Ruysser Gabler <rgabler@edgeautonomy.io>; Laszlo Juhasz <ljuhasz@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Subject: RE: Battery connector resistance check
 
No this does not require an AD. As far as I’m aware, the customer is aware that the EC5s should not be mated while power applied to the aircraft due to them not having any functional anti-sparking measures.
 
As for how many flight cycles recommended between inspection, I would say 50 just because it’s such a quick and easy measurement on two points of the aircraft.
 
Thanks,
 
|  | Hayden Jeanor Electrical Engineer I Edge Autonomy – SLO (formerly Jennings Aeronautics) Phone: +1 805-592-1660 ext. 150 Email: hjeanor@edgeautonomy.io |

 
 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Dana Holley <dholley@edgeautonomy.io>
Sent: Friday, June 28, 2024 12:23 PM
To: Hayden Jeanor <hjeanor@edgeautonomy.io>; Artis Bertulis <abertulis@edgeautonomy.io>; Grace Burgess <gburgess@edgeautonomy.io>; Greg Nichols <gnichols@edgeautonomy.io>; Catherine Wagner <cwagner@edgeautonomy.io>
Cc: Ruysser Gabler <rgabler@edgeautonomy.io>; Laszlo Juhasz <ljuhasz@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Subject: RE: Battery connector resistance check
 
Thanks for the update on the nomenclature. I’m trying to expand this in all areas of our documentation as it is lacking. I’m surprised this didn’t get noticed in our review period with our Mating Connection AD. I’ll start adding you to those, where applicable. Do we have any procedures/other tolerances for checking the EC5 connectors to prevent the issue of sparking?
 
Just to confirm, it doesn’t sound like this issue needs to be reflected to a customer immediately through an AD. We are comfortable with an inspection only? Will it be a 50 or 100 flight cycles?
 
VR,
 
Dana
 
From: Hayden Jeanor <hjeanor@edgeautonomy.io>
Sent: Friday, June 28, 2024 9:37 AM
To: Dana Holley <dholley@edgeautonomy.io>; Artis Bertulis <abertulis@edgeautonomy.io>; Grace Burgess <gburgess@edgeautonomy.io>; Greg Nichols <gnichols@edgeautonomy.io>; Catherine Wagner <cwagner@edgeautonomy.io>
Cc: Ruysser Gabler <rgabler@edgeautonomy.io>; Laszlo Juhasz <ljuhasz@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Subject: RE: Battery connector resistance check
 
Hey Dana,
 
Please see my response to the engineering-oriented questions:
 
- Are we able to tell from AAR’s if VTOL failures are occurring because of contacts being outside said criteria? If yes, how many crashes have occurred? VTOL failure due to AS150 contacts are a consequence of a separate issue regarding the conductivity of the AS150 contact. This criterion is only to address the issue of sparking while mating/de-mating the connector.
- Can the Ohm resistance check for AS150 contacts be applied to all AS150 connections including the ones for the left and right VTOL booms? I think you might be confused by which power contacts are used between the CW and boom. We use AS150’s contacts on our battery connections. For our CW to Boom contacts, we use EC5 contacts.

 
 
|  | Hayden Jeanor Electrical Engineer I Edge Autonomy – SLO (formerly Jennings Aeronautics) Phone: +1 805-592-1660 ext. 150 Email: hjeanor@edgeautonomy.io |

 
 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Dana Holley <dholley@edgeautonomy.io>
Sent: Friday, June 28, 2024 8:26 AM
To: Hayden Jeanor <hjeanor@edgeautonomy.io>; Artis Bertulis <abertulis@edgeautonomy.io>; Grace Burgess <gburgess@edgeautonomy.io>; Greg Nichols <gnichols@edgeautonomy.io>; Catherine Wagner <cwagner@edgeautonomy.io>
Cc: Ruysser Gabler <rgabler@edgeautonomy.io>; Laszlo Juhasz <ljuhasz@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Subject: RE: Battery connector resistance check
 
I think I’m on board with making this an inspection and possibly an AD depending on the response(s) to a couple questions.
 
- Are we able to tell from AAR’s if VTOL failures are occurring because of contacts being outside said criteria? If yes, how many crashes have occurred?
- Can the Ohm resistance check for AS150 contacts be applied to all AS150 connections including the ones for the left and right VTOL booms?

 
For the inspection being included into the inspection schedule. I will need the following.
 
- A determination on whether this will be 50 or 100 flight cycle inspection.
- A rough draft procedure detailing how to perform the inspection. It seems straight forward; I just don’t have enough time/ equipment right now to write it for the next month.
- What does the customer do if the inspection fails?

 
As we all know there are a lot of issues with our connections. It would be great to have a procedure in place to remove and replace this part in the field. In Theater, we cannot simply just RMA the aircraft. I’m hoping we start pushing for MX procedures that will cover most parts/components to include all aircraft structural damage.
 
VR,
 
Dana
 
 
From: Hayden Jeanor <hjeanor@edgeautonomy.io>
Sent: Thursday, June 27, 2024 12:03 PM
To: Artis Bertulis <abertulis@edgeautonomy.io>; Grace Burgess <gburgess@edgeautonomy.io>; Greg Nichols <gnichols@edgeautonomy.io>; Dana Holley <dholley@edgeautonomy.io>; Catherine Wagner <cwagner@edgeautonomy.io>
Cc: Ruysser Gabler <rgabler@edgeautonomy.io>; Laszlo Juhasz <ljuhasz@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Subject: RE: Battery connector resistance check
 
Yes, this criteria can be applied to both anti-spark AS150 contacts on the aircraft – HLB and MB.
 
|  | Hayden Jeanor Electrical Engineer I Edge Autonomy – SLO (formerly Jennings Aeronautics) Phone: +1 805-592-1660 ext. 150 Email: hjeanor@edgeautonomy.io |

 
 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Artis Bertulis <abertulis@edgeautonomy.io>
Sent: Thursday, June 27, 2024 10:56 AM
To: Hayden Jeanor <hjeanor@edgeautonomy.io>; Grace Burgess <gburgess@edgeautonomy.io>; Greg Nichols <gnichols@edgeautonomy.io>; Dana Holley <dholley@edgeautonomy.io>; Catherine Wagner <cwagner@edgeautonomy.io>
Cc: Ruysser Gabler <rgabler@edgeautonomy.io>; Laszlo Juhasz <ljuhasz@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Subject: RE: Battery connector resistance check
 
Hi all,
 
Just to get back to this:
 
@Dana Holley @Grace Burgess see https://jenaero.atlassian.net/browse/VXEP-432, Hayden provided that for the AS150 (the HLB connector) the resistance should be anywhere between 2 – 50 Ohms.
@Hayden Jeanor would this also apply to the main battery connector?
 
|  | Artis Bertulis Flight Operations Manager SLO Edge Autonomy – San Luis Obispo, CA Phone: +1-805-215-3844 Email: abertulis@edgeautonomy.io |

 
 
From: Hayden Jeanor <hjeanor@edgeautonomy.io>
Sent: Tuesday, June 11, 2024 9:29 AM
To: Artis Bertulis <abertulis@edgeautonomy.io>; Grace Burgess <gburgess@edgeautonomy.io>; Greg Nichols <gnichols@edgeautonomy.io>; Dana Holley <dholley@edgeautonomy.io>; Catherine Wagner <cwagner@edgeautonomy.io>
Cc: Ruysser Gabler <rgabler@edgeautonomy.io>; Laszlo Juhasz <ljuhasz@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>
Subject: RE: Battery connector resistance check
 
Mornin Artis,
 
Yup, Laszlo and I typically deal with issues such as this.
 
The cheap characteristics of those connectors will be the EE’s departments demise. I agree, adding this service interval would probably be beneficial if we are seeing sparking upon mating.
 
Of the top of my head, those Anti Spark terminals have a nominal resistance of 6 Ohms. To develop a quick fail criteria for a service interval, we would want the measured resistance across a multitude of failures so we can try to determine at what resistance sparking occurs.
 
- Do you have the measured resistances of the failures?
- Can you point to any NCR/RMA’ed connectors that we can analyze?
- @Catherine Wagner im curious, do you know if we perform any quality checks on the anti-spark terminal in batches of AS150s?

 
Jira: https://jenaero.atlassian.net/browse/VXEP-432
 
Thanks,
 
|  | Hayden Jeanor Electrical Engineer I Edge Autonomy – SLO (formerly Jennings Aeronautics) Phone: +1 805-592-1660 ext. 150 Email: hjeanor@edgeautonomy.io |

 
 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Artis Bertulis <abertulis@edgeautonomy.io>
Sent: Tuesday, June 11, 2024 8:37 AM
To: Hayden Jeanor <hjeanor@edgeautonomy.io>; Grace Burgess <gburgess@edgeautonomy.io>; Greg Nichols <gnichols@edgeautonomy.io>; Dana Holley <dholley@edgeautonomy.io>
Cc: Ruysser Gabler <rgabler@edgeautonomy.io>
Subject: Battery connector resistance check
 
Hi Hayden,
 
Feel like you’d be the guy to ask, but if not, please forward it to the right person.
 
So recently a few of our asset vehicles had dead resistors in the battery connectors. One of them was a visually sparking main battery connector on the fuselage side, and another one was a center wing AS150 connector that just measured really low resistance compared to other vehicles and we assume that might cause sparking too.
 
Anyway, we want to add a check for our 50 (or 100) cycle inspections, to measure the resistance of both battery connectors to determine if they’re good or not and we’d like to know the “acceptable” range so we can start using that info internally and potentially put it in the manuals for customers in the future.
We can measure the connectors of the new vehicles and get a range from that, but I’d like to get the correct acceptable range from engineering. Please let us know if you can help with this.
 
Thanks!

### Hayden Jeanor, 2024-07-01

@Cameron Chapman sorry, ive been trying to limit the scope of Jira tickets recently. This was only to encompass the definition of criterion. Expanding ticket scope ot include implementation

### Hayden Jeanor, 2024-08-15

@Artis Bertulis from recent findings in https://jenaero.atlassian.net/browse/VXEP-539. I am updating the acceptance criteria to 2 Ohms - 10 Ohms

### Artis Bertulis, 2024-08-15

@Dana Holley @Grace Burgess see below

### Christa Meck, 2026-09-30

No work done in almost a year.  Canceling.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240611-165317.png | image | 4657 | 2024-06-11 | listed only |
| Image-20240614-162225.jfif | image | 210 | 2024-06-14 | listed only |
