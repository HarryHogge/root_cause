# VXEP-456: Create list of issues discovered, improvement ideas, tests recommended. Prioritize the list and determine implementation plan

- **Issue type:** Epic
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2024-07-02
- **Updated:** 2025-06-02
- **Resolved:** 2025-06-02
- **Reporter:** Cameron Chapman
- **Assignee:** Abel J. Markow
- **Creator:** Cameron Chapman
- **Parent:** VXEP-183 Establish aircraft grounding, bonding, shielding, etc. status and roadmap.
- **Epic Status:** To Do
- **Epic Color:** ghx-label-1
- **Issue color:** dark_grey

## Plan

- List all issues here and record priority, test plans, and resolution plans. Let Cam know what method could work best (Ex: spreadsheet on sharepoint, Jira substasks).
- Notify Dave and Cameron of issues discovered. They can link them as potential causes for incidents and help with test and CA plans.

Idea: create a Jira subtask for each issue. Assign priority. Use plan and status fields. View and sort all of them at once with a custom search to show these fields. Add search link here. 
- Example search link https://jenaero.atlassian.net/issues/?jql=parent%3DVXEP-456 ORDER BY rank

[embedded image-20240702-213823.png]

## Comments (2)

### Cameron Chapman, 2024-07-02

Pasting email. Responding to Dave's request. The logs will be on the EE ironbird. We could likely identify the specific ones based on the time listed in the video. Garrett is pretty slammed with MAGNSS, but Liam is welcome to pull them if available. 
Thank you,
Cameron Chapman
 
From: Cameron Chapman <cchapman@edgeautonomy.io>
Sent: Tuesday, July 2, 2024 2:41 PM
To: Dave Grosher <Dgrosher@edgeautonomy.io>; Abel Markow <amarkow@edgeautonomy.io>; Garrett O'Neill <goneill@edgeautonomy.io>; Liam Shaw <lshaw@edgeautonomy.io>
Subject: Re: Test Results
 
Abel, 
I think we could benefit a lot from organizing our findings and plans. Can you please do that here? https://jenaero.atlassian.net/browse/VXEP-456 . Feel free to call or message if you want to discuss plan, list format and resolution tracking, etc. 
Plan
List all issues here and record priority, test plans, and resolution plans. Let Cam know what method could work best (Ex: spreadsheet on sharepoint, Jira substasks).
- Idea: create a Jira subtask for each issue. Assign priority. Use plan and status fields. View and sort all of them at once with a custom search to show these fields. Add search link here.
- Example search link

https://jenaero.atlassian.net/issues/?jql=parent%3DVXEP-456%20ORDER%20BY%20rank- - 
-

I responded to your items in bold below. 
Thank you,
Cameron Chapman
 
From: Dave Grosher <Dgrosher@edgeautonomy.io>
Sent: Tuesday, July 2, 2024 1:17 PM
To: Abel Markow <amarkow@edgeautonomy.io>; Garrett O'Neill <goneill@edgeautonomy.io>; Cameron Chapman <cchapman@edgeautonomy.io>; Liam Shaw <lshaw@edgeautonomy.io>
Subject: Re: Test Results
 
Thanks Abel, 
@Garrett O'Neill, @Cameron Chapman, can either of you get the event logs, data logs or AARs off of the PC and make them available via sharepoint? Or, if you could point Liam in the right direction, perhaps he could pull them for you. 
Thanks
David Grosher
Director of Flight Systems
Edge Autonomy
P: +1-760-688-6612
Email: dgrosher@edgeautonomy.io



Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Abel Markow <amarkow@edgeautonomy.io>
Sent: Tuesday, July 2, 2024 12:39 PM
To: Dave Grosher <Dgrosher@edgeautonomy.io>
Cc: Cameron Chapman <cchapman@edgeautonomy.io>; Garrett O'Neill <goneill@edgeautonomy.io>
Subject: Test Results
 
Dave,
 
Cameron and Garrett were able to see some of this in person.  I recorded the screen for the two points of interest.  I think there may be a software adjustment that may need to be made for the current bouncing, hence Gregg asked Curt come take a look. 
 
There are log files on my profile on the PC attached to the iron bird.  Windows 11 / SharePoint shows that I created the folder, but the log files didn’t transfer to this computer, I asked it to sync but it keeps showing the blue cloud without the green checkbox so I have to figure out how to get it to transfer and what I messed up.  I’m sure it was because I was rushing I missed loading the files properly.
 
 
The as run test procedure is this one:
 
2024-05-20-BondingTestCases.xlsx
 
Please note this is a rough draft of a procedure.  There are values in here that don’t make sense for this application.  I pulled MIL-SPEC and went there.
 
I recorded the hand measurements in there.  Many of the bonding measurements are out of spec for MIL spec and ok for most of the applications the AV will be used in.    
Greg and Cameron have also asked for a list of improvements to get it qualified for Carrier / DDG applications.  I’m doing the calculations now. 
 
The 100 Ohms on ground between the batteries and the odd behavior with the voltages and the offsets are a little worrisome.
 
There are 3 videos of interest from that day:
 
- This is bringing up the bench.  After they taught me, I figured a video would be nice for the next person.  Recording 2024-06-20 182216-PowerupofHotbench.mp4
- Saved here https://jenaero.atlassian.net/wiki/spaces/EE/pages/290422814/Hot+Bench+Bring+Up
- This is voltage readings / ethernet flow in the nominal configuration when I apply a 2 volt droop to simulate engine load.  Recording 2024-06-20 181819-greysintalledtransient.mp4
- Note 1:  2 volts may be a large droop for this system.  That battery is very capable.  It may be a rare case that the battery system droops that far. It also could be a common occurrence and because it recovers people don’t care.
- The dropout of the ethernet is easy to see.  It is possible the CAN bus and other devices are being knocked out too.
- The security context stays active (The credentials I passed the autopilot), so I don’t believe we had an autopilot reboot.
- The voltage in this configuration is off by several 100 millivolts and the current bounces a lot. When the grey wire is removed and a ground wire installed the values are off by a few millivolts, current is even more bouncy.
- Logging here https://jenaero.atlassian.net/browse/VXEP-460
- Grey wire removed and bonding wire between batteries (I used a banana cable @ 12 gauge).  Recording 2024-06-20 180825-NoGrey-TransientNoReboot.mp4
- This transient was a 12 volt transient into the power system no Ethernet loss.
- Voltages look great.  Currents still a bit weird.  Curt was helping me analyze this through the log files.
- Added findings to the tasks above.

 
 
Garrett is working on a defense to explain why this change is good.  Hopefully, this will help him.
 
I’m around all tomorrow and later tonight (after 7) and I’ll respond to Teams if I can.
 
Thank you,
Abel

### Cameron Chapman, 2024-07-23

Abel Visit 7/23-25, 
Agenda for the trip: FYI @David Grosher 
- Work with Wesley on the RF certification and authorization path forward

- Set up the CAN analyzer, profile the system and understand if it is vulnerable to the transients

- Profile the ethernet completely, and verify root cause.  See if I can get Kurt on board

- Get the Memory card to fail per the Dave's concerns.  (I'll bring my oscope for this)

- finalize the Grounding issues with Garrett and you.

 
Others that are still open
- Finalize a grounding and bonding schema from the current system all the way to a Aircraft carrier type ship system

- Work the BMS requirements

- Continue to hunt gremlins in the system.  (Dave's request)

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240702-213823.png | image | 46 | 2024-07-02 | listed only |
