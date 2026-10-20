# VXEP-967: VXE 465 Magnetometer issues

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2025-02-04
- **Updated:** 2026-09-09
- **Resolved:** 2025-06-24
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** Hardware, No_crash, PMA263, Weekly-incident-tracker
- **Links:** relates to RMA-535 (VXE-465 Mag Issues 250226-2); relates to AV-14 (Stalker Air Vehicle Crit 2 (Workaround) Investigations)
- **Customer:** PMA263
- **Vehicle Tail Number:** 465
- **Corrective Action:** Replace SD Card
- **Root Cause:** Faulty SD Card
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Location Webster Field, MD (KNUI)
Chris Joyce reports,
“Having lots of issues with three different birds and mag offset/errors during flight and some preventing preflight. After cals, current fw/sw, etc.”
“No payloads, VTOL 55 off, xcomm 180 out”


SharePoint Location

## Plan

Replace SD cards. Perform fixed wing mag cal and re analyze results. 
Conduct full fixed wing mag cal. Report findings.@Carson Buckley 
If no joy, have RMA replace avionics and re-test. Red tag avionics, store for long term investigation if that resolves.

## Issue Status

3/26/2025 Aircraft moved to SCO area for mag testing. Mag testing results somewhat inconclusive. Will likely perform full fixed wing mag cal to see if results improve or change. 
Aircraft left at RMA due to after hours troubleshooting/mag checking. Recommend SD card replacement as we interpret data. 
6/3/2025: RMA closed 5/28/2025. Aircraft shipped back to the customer 5/29/2025.

## Comments (47)

### Greg Fryer, 2025-02-04

@Scott Whitney Is someone available to review the attached log, see if there is anything obvious? They state no payload. 
@Pat Wells Assume they have checked for environmental factors (e.g. use the compass in the kit, change launch location)?
@Cody Smisek @David Grosher FYI.

### Alexander Alan Arnold, 2025-02-04

I have attached an AAR from a failed preflight associated with this aircraft. They said they experienced these issues with two different trillium cameras. An HD40 and an HD45. @Greg Fryer

### Scott Whitney, 2025-02-04

@Eric Brewer - can you take a look?

### Eric Brewer, 2025-02-04

@Alexander Alan Arnold @Greg Fryer can you clarify - comments above state no payloads, but comment below says they experienced issues with HD40 and HD45.  The data indicates good vtol mag but erroneous fixed-wing mag.

### Alexander Alan Arnold, 2025-02-04

I added a screenshot of the email from the customer saying they had issues while flying with gimbals. @Eric Brewer

### Cody Smisek, 2025-02-04

@Eric Brewer @Alexander Alan Arnold The texts I received were copy/pasted into the original description. Not sure why Chris' answer has now changed to indicate that a payload is being used.

### Eric Brewer, 2025-02-04

Got it - have we flown with this type of gimbal before? Both flight logs and ground test indicate significant issues with the fixed-wing mag.  Have they tried the recalibration procedures with the payload installed?
@Cody Smisek @Alexander Alan Arnold @Greg Fryer

### Alexander Alan Arnold, 2025-02-04

I will ask if they have done the cal procedure with either gimbal installed @Eric Brewer

### Alexander Alan Arnold, 2025-02-04

@Eric Brewer @Cody Smisek please review the most recent attachment tilted Chris Joyce traffic (2)

### Eric Brewer, 2025-02-04

@Alexander Alan Arnold @Cody Smisek thanks. Do we have other aircraft that fly in this configuration with the same gimbals? It’s possible there is just interference from the gimbal itself, and the ‘intermittent-ness’ of the issues they are seeing are just due to the gimbal positioning.
Before having them send the unit back - do we have anyone internally here that knows if we’ve flown this configuration before? If not, do we have those gimbals in house we can test?  If they are having the issues with two airplanes I’m inclined to believe it’s specific to those payloads rather than any hardware fault.
@Greg Fryer @David Grosher FYI.

### Cody Smisek, 2025-02-04

@Eric Brewer Based on the response from Chris, it is still unclear to me what configuration was being flown and when in the troubleshooting things were occuring. 
I can’t recall if we’ve flown preMagnss or MAGNSS with HD40 and/or HD45. Flight ops has a trillium payload.

### David Grosher, 2025-02-04

@Cody Smisek @Alexander Alan Arnold @Eric Brewer Given that they performed some calibrations it might be good to compare the new cals with some old calibrations in old AARs if available. Perhaps the new cals were performed near some source of noise.

### Eric Brewer, 2025-02-04

@David Grosher good idea.  This is the cal when it left here:

[embedded: image-20250205-001512.png]
And here is the cal in their latest logs:
[embedded: image-20250205-001541.png]
That’s a huge delta in the offsets and the z span.  It’s possible it’s related to the payloads they have installed or could be specific to their site or the way they are calibrating the birds.  It may make sense to have a quick call with Chris if he’s available as we can talk through his setup.

### David Grosher, 2025-02-04

@Alexander Alan Arnold @Pat Wells See below, you might try to set up a call between Chris and Eric.

### David Grosher, 2025-02-14

@Alexander Alan Arnold I just wanted to follow up on this. Have we discussed the calibration procedure with Chris Joyce?

### Alexander Alan Arnold, 2025-02-18

@Eric Brewer Are you available tomorrow at 1230 EST. Chris can jump on a call and have the aircraft set up so we can have him conduct  a mag cal and pull the logs for us.

FYSA @Pat Wells @David Grosher

### Eric Brewer, 2025-02-18

@Alexander Alan Arnold yes I can be available at that time.  
@David Grosher FYI that will be during standup but I can send an update ahead of time.
@Pat Wells FYI.

### Alexander Alan Arnold, 2025-02-19

Meeting with Chris is scheduled on teams @Eric Brewer

### Alexander Alan Arnold, 2025-02-19

Added the files from 465 and 464 from the testing done today @Eric Brewer

### Eric Brewer, 2025-02-25

@Alexander Alan Arnold, Carson and I met with Chris and Kendal today.  465 has a bad SD card and is being sent back to Huntsville for warranty repairs.  We will check out the magnetometers when it returns. 
@David Grosher @Pat Wells FYI.

### Cody Smisek, 2025-03-26

I see 465 in engineering. Are we supposed to be doing something with it? 
@Eric Brewer @Alexander Alan Arnold

### Alexander Alan Arnold, 2025-03-26

There is an issue with the VTOL magnetometer that needs to be addressed, none of the MAG cals we did could fix the issue. @Eric Brewer @Cody Smisek

### Eric Brewer, 2025-03-26

@Alexander Alan Arnold @Cody Smisek has the SD card been replaced in Huntsville? If so then we just want to do a mag check here (both fixed-wing and vtol).

### Alexander Alan Arnold, 2025-03-26

@Eric Brewer Negative, when we received it, the ROM status was not there. It read like normal.

### Cody Smisek, 2025-03-26

@Eric Brewer For the time being I’ve placed this aircraft with the numerous others in the engineering area. If an updated plan is created for next steps, let me know if there further assistance I can provide onsite with the hardware.

### Eric Brewer, 2025-03-26

@David Grosher are we advising that cards are replaced if they are suspected regardless of actual symptoms observed? 

@Cody Smisek if so I’d recommend card swap and then rerun mag checks for fixed-wing and vtol as next steps. This customer doesn’t have a lot of assets so I assume they want to get it back relatively quickly.
@Alexander Alan Arnold FYI.

### David Grosher, 2025-03-26

@Eric Brewer @Pat Wells I think if we are doing RMA work, then we should do an SD card swap.

### Pat Wells, 2025-03-26

@David Grosher correct. Standard procedure is to always replace on RMA’s if it hasn’t already been done.  Regardless of if its corrupt or not.

### Alexander Alan Arnold, 2025-03-26

“received A/C in HSV on 3/10/25,
tried doing a MAG CAL multiple times every time it was done it seemed to make it worse and kept failing stabilization. Enroute to SLO for further evaluation”

added Jacksons comments from RMA ticket @Eric Brewer @Cody Smisek

### Pat Wells, 2025-03-27

@Cody Smisek @Eric Brewer aircraft is back in RMA as I understand now.  What are the next steps please?

@Drew Hildreth

### Cody Smisek, 2025-03-27

Replace SD cards. @Pat Wells

### Eric Brewer, 2025-03-27

@Alexander Alan Arnold the fixed-wing mag calibration looks like it’s back to a very similar value to what it was when it left here:

[embedded: image-20250327-154352.png]
Vs when it left:
[embedded: image-20250327-154416.png]
When we tested it in the lab here Carson thought the mag cal was good compared to what it normally leaves the factory with, although we did see some drift in the fixed-wing mag.  Are you able to share any logs from your failed stabilization tests?

### Alexander Alan Arnold, 2025-03-27

@Eric Brewer We did the testing on March 11th if you would like to pull the logs from the fuselage. I don’t see the logs on my machine here.

### Eric Brewer, 2025-03-27

@Alexander Alan Arnold thanks.  @Pat Wells @Drew Hildreth are you able to pull off the flight logs before the SD cards are replaced? @Cody Smisek FYI.

### Alexander Alan Arnold, 2025-03-27

Yes, you can pull logs before the card is replaced. Just connect to the aircraft then access the Xcomm file explorer page via <ftp://stalker:[password removed]@<YOUR_XCOMM_IP @Eric Brewer 

Pat and Drew are in Huntsville with me. So, they can't pull data. The fuselage is in SLO.

### Eric Brewer, 2025-03-27

@Alexander Alan Arnold Got it - didn’t realize Pat and Drew were in Huntsville also.  Cody is out at flight testing so we’d need to find someone else to pull the logs.

### Greg Fryer, 2025-04-01

@Eric Brewer There’s a comment in the linked RMA ticket calling for “mag repair”, but I don’t see us concluding that. Was that just an assumption, based on bad mag data? Should we consider just directing avionics replacement for the RMA, we can investigate the logs separately rather than keep the plane in work? (I may be too optomistic)

### Eric Brewer, 2025-04-01

@Greg Fryer the fixed-wing mag was recalibrated in Huntsville but they still reported issues with heading mismatch.  The mags passed Carson’s checkout in SLO but looked off in the informal testing that Cody did.  At this point since we have to swap SD cards it may not be a bad idea to swap out avionics while we’re at it. @David Grosher FYI.

### Greg Fryer, 2025-04-02

@Cody Smisek I think you left the last comment about re-doing full calibration, did that happen and no joy? I have put in replacing avionics if that doesn’t pass, in an effort to get the plane to closure.

### Cody Smisek, 2025-04-02

Last instructions to everyone was to replace SD cards then conduct mag cals. Mag cals have not been completed to my knowledge and I'm unsure and not tracking status of SD card replacements

### Alexander Alan Arnold, 2025-04-08

@David Grosher Is this still in D2, or can we potentially have this moved to D4/6?

### Christa Meck, 2025-04-17

Removed parent to prep for Incident hierarchy change.  Parent is linked as Linked issue.

### Rodney Linch, 2025-05-27

@Greg Fryer - Carson verified mag issue is resolved.  Can we close this out?  Carson’s notes: It seems the issue with GCS communication was solved by the standard SD swap process. Magnetometer has been verified, and it doesn't require a flight. Wing has been sealed, so I think we just need to push it to CofC (need NCR closed before we can) and it should be good.

### Greg Fryer, 2025-05-28

@Rodney Linch Seems like the RMA can move forward. I’ll reassign the investigation to Dave, see if he has enough info to agree we got to root cause and close.

### Greg Fryer, 2025-05-28

@David Grosher This one looks done, assuming we sorted out the SD card questions/issues. If not, can you pass to whoever has the ball there?

### Drew Hildreth, 2025-06-03

@Greg Fryer Per Carsons notes this seemed to have been resolved by the SD Card swap. Unless somebody disagrees with me, I would like to close this one. I will update the plan above.

Shipping has already been requested for the RMA.

### Greg Fryer, 2025-06-03

@Drew Hildreth It’s fine for the RMA to complete, even if the investigation is still open. Need to get Dave G. to agree/approve the root cause is sufficient before closing the incident.

## Attachments (15)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Chris joyce traffic(2).pdf](attachments/25889_Chris%20joyce%20traffic(2).pdf.md) | pdf | 136 | 2025-02-04 | converted |
| Media (35).jpg | image | 461 | 2025-02-04 | listed only |
| [Message from Chris joyce.pdf](attachments/25888_Message%20from%20Chris%20joyce.pdf.md) | pdf | 134 | 2025-02-04 | converted |
| T95_V465_250203_125447_pack-20250204T161834Z-001.zip | archive | 3842 | 2025-02-04 | listed only |
| T95_V465_250204_112908_pack.zip | archive | 725 | 2025-02-04 | listed only |
| image-20250205-001512.png | image | 9 | 2025-02-04 | listed only |
| image-20250205-001541.png | image | 7 | 2025-02-04 | listed only |
| [wierd mag issues .msg](attachments/25883_wierd%20mag%20issues%20.msg.md) | msg | 7366 | 2025-02-04 | converted |
| 464 data | other | 128 | 2025-02-19 | listed only |
| 465 data | other | 125 | 2025-02-19 | listed only |
| [RE Chris Joyce Mag Issues (with eric data and comments).msg](attachments/26387_RE%20Chris%20Joyce%20Mag%20Issues%20(with%20eric%20data%20and%20comments).msg.md) | msg | 515 | 2025-02-19 | converted |
| T95_V464_250219_112828_pack.changetozip | archive | 5314 | 2025-02-19 | listed only |
| T95_V465_250219_112828_pack.changetozip | archive | 2923 | 2025-02-19 | listed only |
| image-20250327-154352.png | image | 15 | 2025-03-27 | listed only |
| image-20250327-154416.png | image | 21 | 2025-03-27 | listed only |
