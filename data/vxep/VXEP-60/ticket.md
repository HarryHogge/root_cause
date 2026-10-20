# VXEP-60: Edge conduct test of prototype units (composite)

- **Issue type:** Sub-task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2022-11-01
- **Updated:** 2025-02-28
- **Resolved:** 2023-07-24
- **Due:** 2023-03-31
- **Reporter:** Greg Fryer
- **Assignee:** Maxime Jeanneau
- **Creator:** Greg Fryer
- **Parent:** VXEP-55 Alternate (or replacement) long range SGCS-3 dish vendor (MicroAnt)
- **Links:** duplicates ENG-3219 (Test First Articles of New Antenna); is blocked by ENG-3142 (Alternate Long Range Antenna Vendor)
- **Sprint:** VXE-2 ME Sprint Team 8-28
- **Job Number:** J100082 - Sustainment: Ground Hardware

## Description

Assume 1 week of shipping time, and one week of testing in OR. Probably Precision.

## Comments (18)

### Cameron Chapman, 2023-04-25

My original card got deleted, but here is the test procedure I wrote up for the last go-around with a new dish. Probably needs a slight update, but should be 90% there. The next steps are figuring out if we are doing it, bend is doing it, or we are hiring precision.
 
https://jenaero.atlassian.net/browse/VIT2-41 
 
See attached document “96X-3-14-5430 SGCS3 Linear Feed Test Plan, Procedure.pdf”
 
I’m trying to not get involved in closing this out because of AP work, but I’m here for quick questions.
 
Thanks,
Kurt

### Cameron Chapman, 2023-04-25

@Maxime Jeanneau , please check with @Gregory Nichols if they can help us this testing. If so, when and where? See 96X-3-14-5430 SGCS3 Linear Feed Test Plan, Procedure.docx. I think Precision helped us with the testing last time. 
Range requirements.
- 3000' AGL
- Max range LOS, procedure lists 100km.

### Cody Smisek, 2023-04-27

@Cameron Chapman I don't think the requirement is 3000ft AGL. Really the requirement is that LOS is maintained and certain amount of fresnel zones are free of obstructions. The 3000ft likely assumes level ground for 100km to clear the horizon. 
We could easily set tracking antenna at a low elevation and launch from a higher elevation 100km away (like a mountain top). Part 107 restricts to 400agl but if equipment has no obstructions and maintains LOS, then I don't see how AGL impacts this testing (assuming Fresnel zone not impacted).

### Maxime Jeanneau, 2023-04-27

@Kurt Burian Given you wrote the original procedure, is it ok to fly on top of a mountain within 400ft AGL with a lower base station with good LOS on the mountain as described by Cody? To me it makes sense to do so allowing the test to be conducted in Part 107 airspace.

### Cody Smisek, 2023-04-28

@Kurt Burian @Maxime Jeanneau A few questions regarding the test plan.
- Confirming we still want to test v3.17.2.6 Silvus FW as part of this plan?
- Has this test been performed in the past for any other feeds?
- Anyone take a look at the link budget calculator Silvus provides to see what the ‘ideal’ results are for our equipment? If we’re already expecting to be above 50-60% air time for one node-to-node then 5MHz bandwidth will probably be unusable (assuming 4mbps video).

### Maxime Jeanneau, 2023-05-01

After talking with Kurt Friday: 
- We are welcome to use the new firmware as long as firmware and configuration is held consistent throughout the test
- Yes, this test was performed by precision using the original antennas, here is some information that I got forwarded (see next comment)
- The link budget should be calculated to get an idea of performance during the test, I attached the calculator here, should be pretty straightforward just need to gather information.

[embedded file]

### Maxime Jeanneau, 2023-05-01

From: Curtis Keenon <ckeenon@flyprecision.com> 
Sent: Thursday, June 9, 2022 2:43 PM
To: Sam Miller <smiller@edgeautonomy.io>
Cc: LM Dustin Gamble <dustin.gamble@lmco.com>; Chris Hofheins <chofheins@flyprecision.com>; Elias Sullwold <esullwold@edgeautonomy.io>; LM Matthew Curran <matthew.curran@lmco.com>; Kurt Burian <kburian@edgeautonomy.io>
Subject: Re: EXTERNAL: Antenna Test Results
 
Sam,
 
We tried all 3 C-band configurations and never saw greater than 5db for very short spans. We could maintain C2 for the most part, just no way to get video.
 
Best,
Curtis Keenon
Program Manager
_________________
 
Precision
 
Mobile (805) 822-2615
Office (503) 687-0108
 
Learn more about how we enjoy the mission at flyprecision.com »
_________________
 
NOTICE: This e-mail message is the property of Precision, LLC and affiliates. The contents of this message and any attachments are proprietary, confidential and potentially trade secret and protected by law from release or disclosure. If you are not the intended recipient of this message, please forward a copy to ckeenon@flyprecision.com including your email address and delete the message and its attachments from your computer. Thank you.
 
 
On Thu, Jun 9, 2022 at 2:06 PM Sam Miller <smiller@edgeautonomy.io> wrote:
Strange, we did not observe this behavior at AEWE when switching from 3.17.2.6 to 4.0.2.8. 
 
Also, did the baseline C-band circular polarized antennas work at 100km?  I would be very surprised. 
 
From: Curtis Keenon <ckeenon@flyprecision.com> 
Sent: Thursday, June 9, 2022 2:02 PM
To: LM Dustin Gamble <dustin.gamble@lmco.com>
Cc: Chris Hofheins <chofheins@flyprecision.com>; Elias Sullwold <esullwold@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>; LM Matthew Curran <matthew.curran@lmco.com>; Kurt Burian <kburian@edgeautonomy.io>
Subject: Re: EXTERNAL: Antenna Test Results
 
Dustin,
 
You are correct with your observations and yes C-band was unusable at 100km.
 
Best,
Curtis Keenon
Program Manager
_________________
 
Precision
 
Mobile (805) 822-2615
Office (503) 687-0108
 
Learn more about how we enjoy the mission at flyprecision.com »
_________________
 
NOTICE: This e-mail message is the property of Precision, LLC and affiliates. The contents of this message and any attachments are proprietary, confidential and potentially trade secret and protected by law from release or disclosure. If you are not the intended recipient of this message, please forward a copy to ckeenon@flyprecision.com including your email address and delete the message and its attachments from your computer. Thank you.
 
 
On Thu, Jun 9, 2022 at 1:34 PM Gamble, Dustin <dustin.gamble@lmco.com> wrote:
I’m trying to put all the data collected into one table. Chris/Curtis can you review this table for our call this afternoon.
 
When I see the TCP data, it looks like the newer firmware, 4.x, is way slower, drops from 17Mbps to ~3 Mbps but the video still looks good. Is that what you observed?
 
Also looks like C-band just doesn’t work at that range.
 
Standard antenna (CW,CCW) looks like identical results for both Slant and Up (horizontal and vertical) polarization. Slant might be a tiny bit better.
 
 
|  |  | Mhz |  | 1 to 10 |  | % | Mbit/s | Mbit/s | Mbit/s | Mbit/s |
| Antenna | Band | Bandwidth | Version | Video Quality | SNR | Air Time | User Thru | Data Rate | TCP 1 | TCP 2 |
| Standard | S | 20 | 3.17.2.6 | 10 | 11 | 40 | 28.06 | 5.5 | 17.9 | 12.3 |
| Standard | S | 20 | 4.0.2.8 | 10 | 11 | 28 | 28.06 | 5.1 | 1.7 | 3.16 |
| Slant | S | 20 | 4.0.2.8 | 10 | 11 | 42 | 28.06 | 6.3 | 1.28 | 2.34 |
| Up | S | 20 | 4.0.2.8 | 10 | 11 | 32 | 11.68 | 5.2 | 2.11 | 1.82 |
| Slant | C | 10 | 4.0.2.8 | 1 | 3 | 56 | 2 to 4 | 5 to 6 |  |  |
| Up | C | 10 | 4.0.2.8 | 1 | 3 | 55 | 2.3 | 5 |  |  |
| Slant | C | 2 | 4.0.2.8 | 2 | 4 | 70 | 4.6 | 3.5 |  |  |

 
 
 
From: Chris Hofheins <chofheins@flyprecision.com> 
Sent: Thursday, June 9, 2022 9:04 AM
To: Curtis Keenon <ckeenon@flyprecision.com>; Elias Sullwold <esullwold@edgeautonomy.io>; Sam Miller <smiller@edgeautonomy.io>; Gamble, Dustin (US) <dustin.gamble@lmco.com>; Curran, Matthew (US) <matthew.curran@lmco.com>; Kurt Burian <kburian@edgeautonomy.io>
Subject: EXTERNAL: Antenna Test Results
 
Antenna Test Results
Thu, Jun 9, 2022 3:30 PM - 4:30 PM (PDT)
Please join my meeting from your computer, tablet or smartphone.
https://meet.goto.com/717429021 
You can also dial in using your phone.
(For supported devices, tap a one-touch number below to join instantly.)
United States: +1 (224) 501-3412
- One-touch:

tel:+12245013412,,717429021#
Access Code: 717-429-021

Get the app now and be ready when your first meeting starts: https://meet.goto.com/install 
Chris Hofheins
VP of Operations
_________________
 
PRECISION
 
MOBILE (909) 967-6097
OFFICE (503) 687-0108
 
See our transformation in action at flyprecision.com »
_________________
 
NOTICE: This e-mail message is the property of Precision, LLC and affiliates. The contents of this message and any attachments are proprietary, confidential and potentially trade secret and protected by law from release or disclosure. If you are not the intended recipient of this message, please forward a copy to name@flyprecision.com including your email address and delete the message and its attachments from your computer. Thank you.
   
** WARNING: This email originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe. **
 
** WARNING: This email originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe. **

### Cody Smisek, 2023-05-01

Regarding FW, I should clarify, do we still want to compare v3 to v4 for both feeds or we only need v4 for both feeds?
And do we have the geographic location they used for tracking antenna & aircraft? Assuming aircraft was at their site. @Maxime Jeanneau looks like we have a test report template in a higher level Jira. Did Precision provide a report after they completed testing previously? 
Knowing the previous answer will help understand the next question. What is our tolerance for range. Does it need to be exactly 100km? I’ve identified locations that are rather optimal for ease of use and altitude but are only 95km straight line.  (I’ve found an alternate site that is ~99km but still want to know tolerance).

### Maxime Jeanneau, 2023-05-03

- @Carson Buckley is the current SGCS3 configuration shipping with v4 silvus firmware? If not we could look into increasing the scope of this test to validate the performance of the upgrade. If so seems out of scope as the primary objective is to validate the performance of the new antennae's.
- @Kurt Burian , did precision provide a report beyond the forwarded email chain below? (Possibly containing coordinates of testing location).
- It would be best to test at 100km or slightly more, but I’ve heard testing was done at less in the past. From what I understand is it would be best to shoot for 100km or slightly over but can reduced if unreasonably challenging.

### Maxime Jeanneau, 2023-05-03

Will look into gathering the information for the link budget unless someone has one filled out already (or if different from the one already linked)

### Cody Smisek, 2023-05-04

@Maxime Jeanneau Kurt already provided the data he used for the link budget to spec out this project so that’s covered.

### Carson Buckley, 2023-05-04

@Maxime Jeanneau All SGCS unit are shiping with 4.0.3.14 and customers are being advised to update their equipment as well, since 4.0 is not backwards compatible.

### Carson Buckley, 2023-05-04

C:\JAI Vault 1\Projects\107 - Stalker XE, VTOL Gen 2\Electrical Design\Firmware and Hex Files\965-1-01-4900 Silvus Radio

### Maxime Jeanneau, 2023-05-18

Modified test plan ready for review found at C:\JAI Vault 1\projects\105 - sgcs 1, 2, and 3\electrical design
Changes made to limit scope of test to just comparing antenna performance

### Maxime Jeanneau, 2023-05-18

Modified contact report ready for review found at C:\JAI Vault 1\projects\105 - sgcs 1, 2, and 3\electrical design
Changes made to limit scope of test to just comparing antenna performance

### Cody Smisek, 2023-05-25

@Maxime Jeanneau I received 6 feeds from Precision. 4 are white. 2 appear to be a white version of our current S band feeds. 2 look like a mini version of the current S bands and 2 might be the C bands?
[embedded file]
[embedded file]
[embedded file]

### Maxime Jeanneau, 2023-05-25

I’m 90% sure based off of Carson’s description the C band antennas are the cylindrical ones. @Carson Buckley is this correct?

### Cody Smisek, 2023-05-25

he agreed that this is correct.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [96X-3-14-5430 SGCS3 Linear Feed Test Plan, Procedure.docx](attachments/14190_96X-3-14-5430%20SGCS3%20Linear%20Feed%20Test%20Plan,%20Procedure.docx.md) | docx | 12261 | 2023-04-25 | converted |
| [MN-MIMO Link Budget Calculator-SGCS3.xlsx](attachments/14292_MN-MIMO%20Link%20Budget%20Calculator-SGCS3.xlsx.md) | xlsx | 61 | 2023-05-01 | converted |
| MicrosoftTeams-image (4).png | image | 254 | 2023-05-25 | listed only |
| MicrosoftTeams-image (5) (2).png | image | 327 | 2023-05-25 | listed only |
| MicrosoftTeams-image (5).png | image | 193 | 2023-05-25 | listed only |
