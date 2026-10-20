# VXEP-1970: VXE 525 Nose dive after transition

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** High
- **Created:** 2026-07-28
- **Updated:** 2026-09-16
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** HLB_bad_cell, Hardware, RCCA, Weekly-incident-tracker
- **Links:** relates to VXEP-1778 (VXE-512 Lost Power during transitiion resulting in crash); relates to VXEP-283 (VXE-533 Uncontrolled drift and crash after failed VTOL abort); relates to RMA-224 (VXE-525 240304-1); relates to RMA-1091 (VXE-525 RMA 260820-1)
- **Customer:** SOCOM(SUMS)
- **Vehicle Tail Number:** VXE 525
- **Vehicle Configuration:** standard vxe 30 battery configuration hd45
- **Plan:** - @David Grosher to provide further direction
- **Severity:** 1 - Flight Critical
- **Executive Summary:** Equipment Returned awaiting investingtion

## Description

Our Stalker transitioned to fixed then nosedived and is pretty much destroyed. Didn't even register that it crashed it was saying it was still in the air"
525 w 876 cw hd45 attached battery flight, silvus only no starlink . broke both batteries after impact. 

Sharepoint Data link below
https://redwireglobal.sharepoint.com/:f:/r/sites/FlightSafety/Shared%20Documents/Incident%20Reports/VXEP-1970%20VXE525?d=w149122d8c8aa4e018f14032582d6eb40&csf=1&web=1&e=sD2M0Y

## Issue Status

9/16/2026 -  Smisek 
Equipment provided to Engineering by RMA. Inspected equipment and air data system. Results recorded in SharePoint linked above within presentation. 
Confirmed pitot system is leaking significantly but unable to determine if pitot system leak led to crash or if pitot system leak resulted from the crash.  
END
___________________________________



UNKNOWN USER writes
Abnormal findings from investigation
IAS doesn’t increase while GS (GPS based does). Seems to indicate issue with pitot system (leak, electrical, pitot press, etc.)

- the xcomm logs show a ground speed of 74fps while the airspeed is only 25.7fps just before the logs cut.  What were the reported wind conditions for the flight?  
Is it possible it was transitioning into a very intense wind? If not, it could point to an issue with the pitot system (either bad shielding during cal, something in the pitot tube or sensor malfunction). 
- Will ask-winds 6 to 8 miles an hour aircraft was directed into wind for launch
- Indicated it’s reading about 20fps (13.6mph) on the ground, on the transition the airspeed just never really increased while groundspeed did.  This to me points to an issue with the pitot. If it’s still intact it’s worth inspecting it.
- may want look at the ticket for 512 and 533 as they all suffered failures during transition
- they're on 6.5.0 so unsure if the fw is missing a major update associated with transition.
- The preflight pitot push only read 55fps, which is lower than I typically see but given the test is just pushing on a pitot I can’t necessarily say if that’s an issue or not.  FWIW I did spot check another log and it only went to 66fps in preflight so i suspect that’s not related.
- this aircraft appears to have had an HLB cell failure during the issue that Eric reported as well.

## Comments (16)

### Alexander Alan Arnold, 2026-07-28

I am waiting on data from the customer at this time they were able to power on the aircraft and are conducting the FTP for xcomm and VTOL

### David Grosher, 2026-07-28

@Eric Brewer Can you take a look at this?

### Eric Brewer, 2026-07-28

@Alexander Alan Arnold can you double-check if there are any other log files on the xcomm processor? I know FTP can sometimes be flakey.  The flight appears to be sd1:/datalog/xcl00311.csv (as indicated in the xcev log), but the .csv files stop at 162.

### Alexander Alan Arnold, 2026-07-28

Ill have them long into the XCOMM page and send me a screenshot of whats availbale @Eric Brewer I also added a zip folder with some more files off the GCS

### Alexander Alan Arnold, 2026-07-28

updated ticket with the missing logs

### Eric Brewer, 2026-07-28

@Alexander Alan Arnold @David Grosher the xcomm logs show a ground speed of 74fps while the airspeed is only 25.7fps just before the logs cut.  What were the reported wind conditions for the flight?  

Is it possible it was transitioning into a very intense wind? If not, it could point to an issue with the pitot system (either bad shielding during cal, something in the pitot tube or sensor malfunction).

### Alexander Alan Arnold, 2026-07-28

i can ask, not sure what time it is where they are. Also they're on 6.5.0 so unsure if the fw is missing a major update associated with transition. You may want look at the ticket for 512 and 533 as they all suffered failures during transition. @Eric Brewer adding winds 6 to 8 miles an hour aircraft was directed into wind for launch

### Eric Brewer, 2026-07-28

@Alexander Alan Arnold thanks.  Indicated it’s reading about 20fps (13.6mph) on the ground, on the transition the airspeed just never really increased while groundspeed did.  This to me points to an issue with the pitot. If it’s still intact it’s worth inspecting it.


[embedded image-20260728-184134.png]
The preflight pitot push only read 55fps, which is lower than I typically see but given the test is just pushing on a pitot I can’t necessarily say if that’s an issue or not.  FWIW I did spot check another log and it only went to 66fps in preflight so i suspect that’s not related.
[embedded image-20260728-184240.png]

### Alexander Alan Arnold, 2026-07-29

added pics of ADP and AAR from ground testing they were able to do this morning. they are saying there is no 272 VTOL log in the webpage. Is there another method of getting that file off the aircraft? @Eric Brewer @David Grosher

### Cody Smisek, 2026-08-03

Coincidentally, this aircraft appears to have had an HLB cell failure during the issue that Eric reported as well.
@Stephen Peters FYI
[embedded image-20260803-151236.png]

### Alexander Alan Arnold, 2026-08-04

@Eric Brewer Do you think a root cause can be determined without the equipment returned?

### Eric Brewer, 2026-08-04

@Alexander Alan Arnold I’m not sure if one can be reached definitively assuming it was a pitot system malfunction.  Given the damage that occurred on the crash we can’t conclusively rule if the pitot system malfunctioned or if there was some other issue.  Do you think it’s an acceptable conclusion that pitot malfunction was more probable than not to be the root cause? @David Grosher @Cody Smisek .

### Cody Smisek, 2026-08-04

@Eric Brewer Not sure if you’re asking me or not. But given the current location of the equipment and the data we were provided, it seems like a reasonable conclusion to suspect the airspeed as root cause. Agreed, I don’t think we’d be able to conclude anything for or against the theory if we had the equipment due to damage caused during the ground contact. 
I’d still like a photo of the data card for the HLB so AA can add to their list. @Alexander Alan Arnold

### Cameron Chapman, 2026-08-05

@Alexander Alan Arnold is there an incident recorded for this battery. Was it grounded?

### Cameron Chapman, 2026-08-05

@Cody Smisek @Eric Brewer @Alexander Alan Arnold I think if we did have the equipment and could replicate similar issues, it would be good evidence that the same issue was present here (yes not proof since it could have been impact damage). Some faults are unlikely to happen from crashes (ex: if we could identify an issue with potted PCB ICs)

### Cody Smisek, 2026-09-16

@David Grosher I have added a sharepoint link with additional logs pulled from aircraft (VTOL and Xcomm). Screenshots of webpages also added.
Inspected air data pod, added observations and photos to draft presentation included in the sharepoint link at top of ticket. 
Confirmed pitot system is leaking significantly but unable to reasonably conclude if issue occurred pre or post incident.

## Attachments (12)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| GCS-20260728T145642Z-1-001.zip | archive | 67806 | 2026-07-28 | listed only |
| Image (55).jpg | image | 1330 | 2026-07-28 | listed only |
| VTOL-20260728T164106Z-1-001.zip | archive | 15548 | 2026-07-28 | listed only |
| VTOL_876-20260728T143956Z-1-001.zip | archive | 50500 | 2026-07-28 | listed only |
| XCOMM-20260728T164108Z-1-001.zip | archive | 295 | 2026-07-28 | listed only |
| XCOMM_XE525-20260728T143830Z-1-001.zip | archive | 29426 | 2026-07-28 | listed only |
| image-20260728-184134.png | image | 36 | 2026-07-28 | listed only |
| image-20260728-184240.png | image | 30 | 2026-07-28 | listed only |
| AAR-20260729T142001Z-1-001.zip | archive | 177 | 2026-07-29 | listed only |
| Image (56).jpg | image | 921 | 2026-07-29 | listed only |
| Image (57).jpg | image | 842 | 2026-07-29 | listed only |
| image-20260803-151236.png | image | 90 | 2026-08-03 | listed only |
