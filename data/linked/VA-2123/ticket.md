# VA-2123: VXE-592 Purple SD corruption observed

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-10-29
- **Updated:** 2025-12-02
- **Resolved:** 2025-12-02
- **Reporter:** Cameron Chapman
- **Assignee:** Carson Buckley
- **Creator:** Cameron Chapman
- **Links:** Cannot finish until linked issue is finished. VA-2122 (Red AP replaced SD card and unable to access files after format); relates to VXEP-236 (Systemic SD card Investigation VXE-522 XCOM board failures at LM Source inspection); relates to RMA-278 (VXE-592 240701 MOLSON)

## Description

@Carson Buckley can you please fill out more info
- AC TN and history
- Was this a card replacement, new install, etc.
- Was this card corrupt after initial installation or working normally, then corrupt?
- Linked RMA?

Came up as //ROM, we rebooted and it came up //SD1, checked the Drive Status and saw this.
592 SD Corruption Webpage 1.png
 Reformatted and rebooted, came up clean after.
592 SD Formatted Webpage 1.png

## Comments (5)

### Cameron Chapman, 2024-10-29

Carson Buckley
Just had SD corruption on a replaced Purple

 What led to the corruption? 

 
Corruption can be caused by loss of power during write cycle. I don't suspect this being a card issue, just indication that yes this still happens.
 
Carson Buckley
Corruption can be caused by loss of power during write cycle. I don't suspect this being a card issue, just indication that yes this still happens.

Ryan F was not able too, this is new. Makes sense but I dont believe we were able replicate it on a bench
 
 
Yeah Ryan had tried to recreate this issue on the TAS and ran through thousands of power cycles and wasn't able to cause this to happen. Although I think we all still knew it was possible, it just appeared to be less probable than we had originally thought. 
 
I think this type of error has been observed a few times over the past few years when looking at incidents as well. 
 

Dave Grosher
I think this type of error has been observed a few times over the past few years when looking at incidents as well.

 Makes sense for those cases in which we were able to successfully reformat. 

 
This kind of corruption will cause slow loading pages, or failure to load, possibly read / write errors in the log files. Reformat has always fixed this, so it was assumed it was related to how the vehicle is accessing and writing rather than an issue with the cards themselves.
 Carson Buckley after you reformatted did you try accessing the log files? I had one with similar behavior yesterday and it would successfully reformat but after being on for a few minutes and trying to access logs or drive status it would start to hang. The main page would still say sd1 but when you watched messages you could see that it was unable to read the log file it had created at boot and was rebuilding it each time. Point being that formatting appeared to fix the card but then after subsequent reboots the files would begin failing 
It has been on for a while now and we haven't had further issues. Let me check and see how the pages are behaving before we reboot and continue.
 
Files are coming up fine, no delays.
 
No errors in the logfile.
 
It's still on if you want to come have a look, or if you have a radio you can remote in.

### Cameron Chapman, 2024-10-29

more chat history 

Cameron Chapman
Is there an NCR or JIRA incident for this? It seems like there should be

 No NCR or Jira, this was assumed to be a known issue so we just reformatted and moved on. 

 

Cameron Chapman
Would a customer know how to reformat this in the field with the current firwmare and manuals,With the FW kurt is working on and relevant manual updates?

 It might / should be in the maintenance manual on how to reformat. Anyone with access to the web interface would be capable. 

 
Checked Webmanuals, no listing for format in this context.
 
There are multiple Jira tickets on SD corruption, as far back as Nov June 2023.
 
We don't provide customers access to the web interfaces
 
That is currently the only way to reach the Utilities for SD Format, so unless someone wants that to become a GCS function then, no.
 
The FSR going to UK for the SD replacement should be aware of the process. Under normal operation it should not be required to format the storage media.
 

Carson Buckley
The FSR going to UK for the SD replacement should be aware of the process. Under normal operation it should not be required to format the storage media.

 Was this card corrupt after intial installation or working normally, then corrupt?  

 
I think Kurt's upcoming firmware may fix this automatically, but the current firmware and manuals would not

### Cameron Chapman, 2024-10-29

If I'm understanding the history of this vehicle, it was rebuilt in July and has been essentially sitting since then. The VT SD was swapped out, but otherwise it was uncalibrated. This was probably its first or second time being booted since then.
 
We have had no further issues with it since the reformat.

### Carson Buckley, 2024-10-29

@Cameron Chapman  All the relevant information, other than ‘we saw this’ is already on Jira.
Vehicle in question:
https://jenaero.atlassian.net/browse/RMA-278 

A few other cases where we have had this exact issue.
https://jenaero.atlassian.net/browse/XEO-285 
https://jenaero.atlassian.net/browse/ENG-806 
https://jenaero.atlassian.net/browse/VA-318 
https://jenaero.atlassian.net/browse/FS2-310

### Christa Meck, 2025-12-02

@Carson Buckley and/or @Cameron Chapman   Was this a part of “The SD Card Issue” ?  Has this been remediated?  Is this aircraft still in use?

## Attachments (0)
