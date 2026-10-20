# ENG-3018: Low potentially interfered GPS signals, multiple repeated launch aborts

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-06-15
- **Updated:** 2026-04-17
- **Resolved:** 2026-04-17
- **Reporter:** Daniel Lloyd
- **Assignee:** Pat Wells
- **Creator:** Daniel Lloyd
- **Labels:** MARSOC, lmco
- **Links:** relates to ENG-3118 (412 428 447 Multiple Launch Aborts); relates to ENG-3201 (Source Interference Locating Equipment ); relates to VXEP-1066 (VXE 448 Multiple Aborted takeoffs)

## Description

<There are multiple occurrences of this in the same location with different tail #s. This is a consolidated investigation.>
<Link any GPS-loss aborts from sequence here.>

From the MARSOC customer.
We tried to fly AV 473 today but were unsuccessful four times in a row due to VTOL and GPS issues during launch.  The AV kept self-aborting at about 10 feet.  It’s weird because we have flown this vehicle a few weeks ago.  Two other aircraft flown today were fine. I’ve uploaded the 4x FDRs to the VXEHELP portal for analysis.   AV 473 is scheduled to pack out for deployment next week, please let me know at the soonest if you find something in the FDR that we need to address.
@Dustin Gamble

## Comments (29)

### John Clark, 2023-06-20

@Dustin Gamble any progress getting those AAR’s so we can unzip?

### Daniel Lloyd, 2023-06-21

I have tried to contact the operator to resend. Tomorrow I’ll go by there and grab them myself.

### John Clark, 2023-06-22

@Daniel Lloyd thank you. Standing by.

### Daniel Lloyd, 2023-06-22

The customer deployed both the laptop and aircraft. They were not able to locate any copies of the files today. I will check with them next week when the PIC returns to work.

### John Clark, 2023-06-23

@David Grosher this VIT is now available for dispatch. @Former user @Ryan Christino I am assigning this to your team. I think Ryan can handle it as he has been through the process with Gordon Jennings. Please, let me know if you need assistance.

### Ryan Christino, 2023-06-29

@Daniel Lloyd Any luck with communicating with the operator who obtained the flight data? We are still pending flight data that is not corrupt in order to investigate this issue.

### Daniel Lloyd, 2023-06-30

I believe they have reattempted to upload data file to the help site but I don’t have access to confirm that.

### Sam Miller, 2023-06-30

Added new file from customer on 6/30

### David Grosher, 2023-06-30

I uploaded 14 AARs as a single zip.  It is unclear if all of this data is applicable to this issue, but it is likely.

### David Grosher, 2023-06-30

Some notes I took while looking at the data. 
[embedded: Launch Abort Notes Dgrosher.pdf]

### Cody Smisek, 2023-06-30

@David Grosher Is this Jira issue relating to only 473 or all of the vehicles that were in the 14 AARs you included? In the large ZIP are vehicles 427, 436, 445, 450, 451, 473, 474, 477. 
Also possibly helpful for understanding what’s going on is adding the email / meeting notes from the conversations that were had with the customer(s). Looks like we spent a fair amount of time on this https://jenaero.atlassian.net/browse/VIT-43 only to find out that GPS interference was the likely culprit. Has that question already been raised?

### Cody Smisek, 2023-06-30

@David Grosher I pulled all the SCO data I could locate on those aircraft. It’s attached to this issue in “SCO_Data1”.

### David Grosher, 2023-07-03

@Cody Smisek It appears that the same issue is present in 12 of the included AARs and it seems the GCS location for each of these was near MARSOC HQ. 1 dataset (v436) was a full flight at a different location and didn't show this behavior, although low Cn0 was observed throughout the flight. 1 dataset (v445) wasn't a flight.
I updated my notes and I agree with Cody that this is related to https://jenaero.atlassian.net/browse/VIT-43. John T. said that the customer and LM confirmed GPS interference at the site in 9/27-28/22 and closed this issue. 
[embedded: Launch Abort Notes Dgrosher v2.pdf]
Potential work around to consider:  change the Cn0 threshold

### David Grosher, 2023-07-03

I went through the data Cody provided for all of the SCO flights with the same tail numbers and I didn’t see any indication of CNo issues during those flights.

### David Grosher, 2023-07-06

MARSOC sent data for two aborted launches with v482 and one successful launch with v484 at roughly the same time.

### David Grosher, 2023-07-06

@Cody Smisek I think the aborted launch was v484.

### Cody Smisek, 2023-07-06

@David Grosher deleted my comment. Thanks for catching. Debug log for 482 appears to show first a connection to 484 (with 2x failed launches) then a successful flight of 482. I think….

### Cody Smisek, 2023-07-06

https://www.faasafety.gov/files/notices/2023/May/PAXRVR_23-02_GPS_Flight_Advisory.pdf 
looks like only 436 would have been impacted by this notice (based on dates)

### Sam Miller, 2023-07-06

Excellent find @Cody Smisek!  @Pat Wells can you please gently inform MARSOC about this and see if they’re tracking?

### Pat Wells, 2023-07-07

@Sam Miller I will gently bring this to MARSOC’s attention today.

### Greg Fryer, 2023-07-20

Per @Sam Miller We are getting a spectrum analyzer and hopefully a SME who can use it track interference to source.

### Cody Smisek, 2023-07-20

@Greg Fryer Clarification. We have a spectrum analyzer, I’m working on getting quotes for additional hardware and licenses for that in house hardware to support location finding / direction finding.

### Pat Wells, 2023-07-27

Will be conducting on site GPS spectrum survey with BAE and equipment 1-3 August.

### Pat Wells, 2023-08-03

On 1 Aug 2023 the source of GPS interference was located in the area of operations.  We were not able to access the building where the source is being emitted from.  Customer will work the on-site issue going forward with the tenant of the building.
[embedded file, not matched to an attachment]

### Cameron Chapman, 2023-08-03

Pat to update fields above and move to review investigation

### Cameron Chapman, 2023-08-24

Linking subtasks to parent.

### Maxime Jeanneau, 2023-09-15

@Wesley Lilienthal may be interested in this as well

### Christa Meck, 2026-04-17

@Pat Wells @Cameron Chapman 
Is this still an item that needs investigation or are we beyond this at this point?

### Pat Wells, 2026-04-17

@Christa Meck this was resolved. No further action needed.

## Attachments (12)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V473_230615_074754_pack.zip | archive | 431 | 2023-06-15 | listed only |
| T95_V473_230615_080129_pack.zip | archive | 466 | 2023-06-15 | listed only |
| T95_V473_230615_082602_pack.zip | archive | 716 | 2023-06-15 | listed only |
| AARs.zip | archive | 18850 | 2023-06-30 | listed only |
| [Launch Abort Notes Dgrosher.pdf](attachments/15278_Launch%20Abort%20Notes%20Dgrosher.pdf.md) | pdf | 486 | 2023-06-30 | converted |
| SCO_Data1.zip | archive | 71935 | 2023-06-30 | listed only |
| T95_V473_230512_120106_pack.zip | archive | 212 | 2023-06-30 | listed only |
| [Launch Abort Notes Dgrosher v2.pdf](attachments/15282_Launch%20Abort%20Notes%20Dgrosher%20v2.pdf.md) | pdf | 577 | 2023-07-03 | converted |
| T95_V482_230706_144623_pack.zip | archive | 1846 | 2023-07-06 | listed only |
| T95_V484_230706_141551_pack.zip | archive | 1059 | 2023-07-06 | listed only |
| T95_V484_230706_143444_pack.zip | archive | 1173 | 2023-07-06 | listed only |
| [VIT2-316 Vehicle Incident Report.pptx](attachments/15371_VIT2-316%20Vehicle%20Incident%20Report.pptx.md) | pptx | 883 | 2023-07-06 | converted |
