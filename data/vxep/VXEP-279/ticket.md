# VXEP-279: XE 396 Failure Nose Harness Assembly Fire

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-02-16
- **Updated:** 2025-05-20
- **Resolved:** 2025-05-20
- **Reporter:** Cameron Chapman
- **Creator:** Cameron Chapman
- **Severity:** 1 - Flight Critical

## Description

Files: VXEP-279 XE 396 Failure Nose Harness Assembly Fire
Still piecing together email and data logs. ESC meltdown. GPS spoofing. Loss of command.

## Plan

- Data Review.
- Should we also open up related issues for the inaccurate GPS and lost comms he mentioned, or is that expected behavior in a contested environment?
- Are they planning to return this vehicle? Do we have a timeline for it?
- It is hard to tell from the photos, is the damage definitely concentrated in the ESC, or could it be the originating in current sense board? We have had a few CSB failures due to hot mating without antispark contacts (using the nose connector rather than the battery connector).
- Were they connecting the nose connector with battery power applied? If unsure, they could inspect it for sparking scorches.
- Does it make sense that they could still read data from the aircraft, but not command it? Was this likely due to jamming or other degraded comms?
- How much damage did the aircraft sustain?
- It seems like they were experiencing GPS jamming and expecting other possible EW. Is there anything in the logs to indicate commands not being received? Should we open a separate issue to troubleshoot that issue? Interference could have affected the ESC, it could also be unrelated.
- I was trying to look at the data log for flight count, but it seems to be inconsistent.
Here is the last entry. It says SN 397, but the data log is titled 396. Do you know why this is? It also has different AP SNs and tail numbers in the log, which seems strange.

## Issue Status

It looks like VBatt on Xcomm drops to 18V right before the FW AP resets.  Line 999 in the XCOMM log is where it gets interesting.   ESC caught fire on this one.

## Comments (10)

### Cameron Chapman, 2024-02-16

[embedded file]
[embedded file]

### Cameron Chapman, 2024-02-16

Initial email I will review and update JIRA soon.
It is hard to tell from the picture if the damage was concentrated in the ESC or in the current sensor (where we have seen shorts lead to fires before we think due to hot mating connectors).
 
Initial questions
- Should we also open up related issues for the inaccurate GPS and lost comms he mentioned, or is that expected behavior in a contested environment?
- Are they planning to return this vehicle? Do we have a timeline for it?

 
 
 
Thank you,
|  | Cameron Chapman Electrical Engineer Edge Autonomy – SLO (formerly Jennings Aeronautics) Email: cchapman@edgeautonomy.io Phone: (970)389-5904 |

 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Dave Grosher <Dgrosher@edgeautonomy.io> 
Sent: Friday, February 16, 2024 2:57 PM
To: Cameron Chapman <cchapman@edgeautonomy.io>
Subject: Fw: FDR 12FEB
 
Hi Cameron, 
 
I'm not sure if you are tracking this one. I don't think a VXEP ticket was created for it.  It looks like VBatt on Xcomm drops to 18V right before the FW AP resets.  Line 999 in the XCOMM log is where it gets interesting.   ESC caught fire on this one. 
 
David Grosher
Director of Flight Systems
Edge Autonomy
P: +1-760-688-6612
Email: dgrosher@edgeautonomy.io



Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Pat Wells <pwells@edgeautonomy.io>
Sent: Friday, February 16, 2024 10:46 AM
To: Dave Grosher <Dgrosher@edgeautonomy.io>
Subject: Fwd: FDR 12FEB
 
 
 
Get Outlook for iOS
From: Global Support
Sent: Thursday, February 15, 2024 9:26:26 AM
To: Sam Miller <smiller@edgeautonomy.io>
Subject: FW: FDR 12FEB
 
Sam,
Can we carve out some time to go over this?  
Thanks,
Pat
 
|  | Pat Wells Director of Global Support Edge Autonomy – Huntsville, AL Cell: 256-836-4443 Email: pwells@edgeautonomy.io |

 
 
From: GV <gabev14@gmail.com> 
Sent: Monday, February 12, 2024 8:00 AM
To: Global Support <globalsupport@edgeautonomy.io>
Subject: FDR 12FEB
 
|  | You don't often get email from gabev14@gmail.com. Learn why this is important |  |

All, 
 
Attached is the FDR that we were able to pull from our A/C. During our preflight we had zero warnings with full GPS and no ESC warnings or malfunctions . We recognized spoofing on the z-axis at roughly ~2000' and AV began to report -1400+ AGL. At this time we could not send CMDs to the AV but could monitor flight and AV did attempt to RTB to the original waypoint prior to TDP. We attempted to swap to another GCS hoping for a system glitch but still had cmds ghosted. 
 
We have a few question that we hope you can help us with:
- When/Why would flight CMDS ghost, is this attributed to ESC failure?
- Is there an ESC shelf life or potentially bad batch. We do not fly these AVs and are there indicators prior to inflight EPs?
- Should we test other components prior to flying the same AV?
- What hardware is connected and is the ESC affected by GPS anomalies?
- What are known EW effects or known susceptibilities to ESCs?
- Is there AV logics built into the program that we can interpret and expect to do when certain conditions are met?
- If we turn on GPS prior to flight at what ALT will AV begin to accept CMDs/Inputs from the operator?
- Can we turn off GPS in flight post LAU in Gains menu?
- How long did AV continue to climb and why did AV flight path veer from input waypoint?

If there additional procedures to getting this AV back and operational? 
 
As we move closer to flying again we are hoping to get some


 
V/R, 
 
Gabe Varela
+1 5204880658

### Pat Wells, 2024-02-17

@Cameron Chapman & @David Grosher thanks for looking into this.  I didn’t initially open a VXEP Jira ticket as this is a Block 25 aircraft. 
Wanted to make sure everyone was tracking that.

### Cameron Chapman, 2024-02-17

Thanks @Pat Wells for the information. I updated the title to XE. We don’t have a separate project for XE.

### Pat Wells, 2024-02-19

Thanks @Cameron Chapman

### Cameron Chapman, 2024-02-19

@David Grosher @Pat Wells It definitely seems like the failure in the ESC assembly caused the issue. Additional questions
- It is hard to tell from the photos, is the damage definitely concentrated in the ESC, or could it be the originating in current sense board? We have had a few CSB failures due to hot mating without antispark contacts (using the nose connector rather than the battery connector). 
- Were they connecting the nose connector with battery power applied? If unsure, they could inspect it for sparking scorches.
- Does it make sense that they could still read data from the aircraft, but not command it? Was this likely due to jamming or other degraded comms?
- How much damage did the aircraft sustain?

Answers to his questions  
- When/Why would flight CMDS ghost, is this attributed to ESC failure?
- No. Unless the short in the ESC brought the bus voltage low enough so the XCOM did not operate normally. Unlikely since it was still sending data.
- Is there an ESC shelf life or potentially bad batch. We do not fly these AVs and are there indicators prior to inflight EPs?
- Not that I am aware of. They are repurposed hobby Castle ESCs, so we do not have much quality control on them. That being said, B25 ESC failures have been rare (I have not heard of many, but they didn’t have a problem tracking system). @Carson Buckley or @Sam Miller may have more knowledge of B25 ESC issues
- Should we test other components prior to flying the same AV?
- I do not have a good idea of how much damage it encountered.
- What hardware is connected and is the ESC affected by GPS anomalies?
- It should not be. Not sure what he meant by the first part of the question.
- What are known EW effects or known susceptibilities to ESCs? 
- None, but B25 has not undergone any EMI/EMC testing as far as I know. I would not be surprised if it had susceptibilities. It has lots of unshielded harnesses and assemblies.
- Is there AV logics built into the program that we can interpret and expect to do when certain conditions are met?
- Not sure what this means. Yes, the AV has logic for various circumstances.
- If we turn on GPS prior to flight at what ALT will AV begin to accept CMDs/Inputs from the operator?
- Can we turn off GPS in flight post LAU in Gains menu?
- How long did AV continue to climb and why did AV flight path veer from input waypoint?

If there additional procedures to getting this AV back and operational?

### David Grosher, 2024-02-19

@Cameron Chapman 
“2. Does it make sense that they could still read data from the aircraft, but not command it? Was this likely due to jamming or other degraded comms?”  The FW AP reset after the voltage drop, data was still being sent to the XCOMM following reset. The control modes didn’t appear to change after the reset and given the aircraft was recovered it seems that it kept flying. But given the event it is possible that the commands couldn’t be received. Unfortunately, I don’t think we will be able to test this in the HIL.

### Cameron Chapman, 2024-02-19

Thanks @David Grosher. I was referring to these sections of the email.
- We recognized spoofing on the z-axis at roughly ~2000' and AV began to report -1400+ AGL. At this time we could not send CMDs to the AV but could monitor flight and AV did attempt to RTB to the original waypoint prior to TDP. We attempted to swap to another GCS hoping for a system glitch but still had cmds ghosted.
- What hardware is connected and is the ESC affected by GPS anomalies?
- What are known EW effects or known susceptibilities to ESCs?

It seems like they were experiencing GPS jamming and expecting other possible EW. Is there anything in the logs to indicate commands not being received? Should we open a separate issue to troubleshoot that issue? Interference could have affected the ESC, it could also be unrelated. 
I was trying to look at the data log for flight count, but it seems to be inconsistent. 
Here is the last entry. It says SN 397, but the data log is titled 396. Do you know why this is? It also has different AP SNs and tail numbers in the log, which seems strange. 
| Flight Date | Flight Date UTC | Flight Number | Pilot | Ground Crew | Instructor | A/C Type | A/C Mod | A/C S/N | A/C Comms | AP Firmware | Gains | XCOMM Firmware | Weight | AP S/N | Total Launches | Total Flight Hours | LW | CW | RW |
| 12/4/2023 | 12/4/2023 |  |  |  |  | XE25 |  | 397 | Silvus S Band | 6.05j | A382 | 4.60.XEVT | 26.5 | 10114 | 56 | 48.7 | 397 | 397 | 397 |

### David Grosher, 2024-02-20

@Cameron Chapman 
- It appears that the FW AP reset and then the altitude possibly was re-calibrated in the process because there is a rapid jump down to a negative value after it initialized. But I don’t see the -1400 number that they referenced.
- ESC throttle does control altitude so if the altitude was incorrectly below the commanded altitude then it is feasible that we would see a higher than expected throttle command for an extended period of time. However, we don’t see any unusual throttle commands.  One thing to note in the plot here is there is a significant power draw that is uncommanded after the AP reset.  This could also be an artifact of the error state of the AP. 
[embedded file]
- Limited EMI testing has been performed on XE25 that I am aware of. There were documented issues with Navy testing at 200 V/m (on deck environmental specification) with VXE30.  The ESCs are driven by PWM, it is possible that noise on that bus could lead to non-deterministic behavior on the ESC. But the current pulled wasn’t significantly higher or for longer duration than the earlier portion of the flight.

### David Grosher, 2025-05-19

@Pat Wells Is there any pending action on this XE25 vehicle? I’m not sure we really have the capability to effectively support XE25 at this point.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T91_V396_240212_085643_pack.zip | archive | 440 | 2024-02-16 | listed only |
| image-20240217-054529.png | image | 4549 | 2024-02-16 | listed only |
| image-20240217-054556.png | image | 267 | 2024-02-16 | listed only |
| image-20240221-042511.png | image | 85 | 2024-02-20 | listed only |
