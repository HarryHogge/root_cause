# VXEP-221: VXE 398 Heading Data Appears Delayed Compared to Other Aircraft

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2023-12-13
- **Updated:** 2026-03-02
- **Resolved:** 2024-12-06
- **Reporter:** Cameron Chapman
- **Assignee:** David Grosher
- **Creator:** Cameron Chapman
- **Labels:** INL
- **Links:** relates to ENG-1750 (MPU-9250 Chips have high failure rate, are obsolete, and have a high rate of conterfeits.)
- **Issue color:** dark_yellow
- **Customer:** INL
- **Vehicle Tail Number:** 398
- **Other Stakeholder (as required):** Connor Peebles
- **Incident Type:** Squawk
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

We are doing some ViDAR testing and we have looked at the aircraft heading data we are getting from XCOMM and there seems to be some delay with one of our aircraft (398) compared to the other aircraft (464,462). 398 was a blk 25 originally, and 464/462 were organic blk 30 birds.

## Plan

- Sam requesting flight data from the 464,462, and 398 to compare.
- May be due to conterfeit MPU-9250 see linked issue.

## Comments (8)

### Cameron Chapman, 2023-12-13

Adding Connor, who may is more familiar with these, but there were no component changes between XE25 and 30 to the FWAP, XCOM, or Magacc board that I am aware of. I think we should start by requesting flight data from the 464,462, and 398 to compare.
I created this incident to track. https://jenaero.atlassian.net/browse/VXEP-221 
 
 
@Sam Miller, do you agree with this plan? Would you like to ask them, or have one of us or @Pat Wells ask?
 
Thank you,
|  | Cameron Chapman Electrical Engineering Supervisor Edge Autonomy – SLO (formerly Jennings Aeronautics) Email: cchapman@edgeautonomy.io Phone: (970)389-5904 |

 
Confidentiality Notice
This e-mail message, including any attachments, may contain confidential information which is intended only for the use of the intended recipient(s). Any unauthorized review, use, disclosure, distribution, dissemination or action taken in reliance upon this information by persons or entities other than the intended recipient is prohibited. If you are not the intended recipient and this message has been addressed to you in error, please promptly notify the sender by email reply and destroy all copies of the message and any attachments.
 
Export Control Notice
This document and attachments may contain technical data as defined in the International Traffic In Arms Regulations (ITAR) 22 CFR 120.10 or the Export Administration Regulations (EAR) 15 CFR Parts 730 – 780. Export of this material may be controlled by these regulations and may not be exported or transferred to non-U.S. persons without prior written approval from the U.S. government.
 
From: Sam Miller <smiller@edgeautonomy.io> 
Sent: Wednesday, December 13, 2023 9:17 AM
To: Dave Grosher <Dgrosher@edgeautonomy.io>
Cc: Cameron Chapman <cchapman@edgeautonomy.io>
Subject: RE: AHRS
 
Thanks Dave!
 
Cameron,  please see below.  Would there be any difference in older XE25 vs new VXE30 Mag/Acc boards for the fixed wing AP?   Have we refreshed that board with newer components since XE25?
 
From: Dave Grosher <Dgrosher@edgeautonomy.io> 
Sent: Wednesday, December 13, 2023 9:10 AM
To: Sam Miller <smiller@edgeautonomy.io>
Subject: Re: AHRS
 
Sorry, I missed this yesterday. 
 
I think you are correct, but I don't think that would matter.  Both configurations would be pulling the VTOL data in that case.  The only thing that I can think of is one of the boards was respun with newer components. Cameron would be the one to ask in that case. 
 
Also, I think both the FW AP data and the VTOL data would be available on the XCOMM. I assume whichever field they are looking at would be consistent across all birds. 
 
From: Sam Miller <smiller@edgeautonomy.io>
Sent: Tuesday, December 12, 2023 8:05 AM
To: Dave Grosher <Dgrosher@edgeautonomy.io>
Subject: FW: AHRS
 
Hi Dave,
 
Got this email from the INL guys…they’re testing the VIDAR stuff.  Any ideas here?  I vaguely recall that we might be using the VTOL mag/acc board in the wing to provide better-quality sensor data to the fixed-wing autopilot, but I’m not sure. 
 
Thanks,
Sam
 
From: Chris Joyce <chris@trinitybend.com> 
Sent: Sunday, December 10, 2023 1:35 PM
To: Sam Miller <smiller@edgeautonomy.io>; Ryan Christino <rchristino@edgeautonomy.io>
Subject: AHRS
 
Gents,
 
We are doing some ViDAR testing and we have looked at the aircraft heading data we are getting from XCOMM and there seems to be some delay with one of our aircraft (398) compared to the other aircraft (464,462). 398 was a blk 25 originally, and 464/462 were organic blk 30 birds. Was there a different version AHRS or other hardware between the blk25 and 30 that could lead to this?
 
 
Thanks
Chris

### Cameron Chapman, 2023-12-13

Hi Guys,
 
As far as I know, there have been no major component changes for Magacc2, besides the ever present approval of alternative components that usually only apply to passives. We have past BOMs and approved alternatives recorded.
 
I would, however, like to remind people of Ryan F.’s concern that he brought up awhile ago where he pointed out that the market is flooded with MPU-9250 counterfeits, after the MPU-9250 stopped being produced in 2017. The MPU-9250 was a popular hobbyist IMU. It is still on the Magacc2 board.
 
Best,
|  | Connor Peebles Electrical Engineer Edge Autonomy – SLO Email: cpeebles@edgeautonomy.io |

### David Grosher, 2024-02-19

@Sam Miller @Pat Wells Did we ever get data for this incident?

### Pat Wells, 2024-02-19

@David Grosher I did not receive any data on this.  Was not even tracking it until now.

### David Grosher, 2024-05-22

@Pat Wells Independent of this ticket, it was discovered that all of the calibrations from v398 had been deleted at some point. Given that and we don’t have any data, I propose we close this ticket.

### David Grosher, 2024-12-05

@Pat Wells Can we close this? There is no data, it has been lingering for some time.

### Pat Wells, 2024-12-06

@David Grosher yes close it out.

### David Grosher, 2024-12-06

No data

## Attachments (0)
