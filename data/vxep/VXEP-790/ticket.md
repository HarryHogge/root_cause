# VXEP-790: VXE 645 and 646 GCS Software freezing up during flight

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2024-11-22
- **Updated:** 2026-03-02
- **Resolved:** 2025-01-10
- **Reporter:** Pat Wells
- **Assignee:** Ted Trowbridge
- **Creator:** Pat Wells
- **Labels:** TIQUILA, Weekly-incident-tracker
- **Customer:** TIQUILA
- **Plan:** More logs requested
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

The Operator’s statement for both of these problems is quite lengthy so I’ve attached them as 2 Word documents. Both issues essentially present the same which is why I’ve combined them into one Jira ticket.

I’ve already asked the customer to check for logs in the GCS crash dump folder.  None were present.

AAR’s attached.

## Comments (12)

### David Grosher, 2024-11-22

@Ted Trowbridge FYSA

### Ted Trowbridge, 2024-11-26

@David Grosher @Pat Wells 
Although the SSD and telemetry were still functioning and the UA GUI carrot was still moving as
expected, the pan zoom and go to functionalities were unavailable.

I’m reading this as the map overlays and instrument panel were still updating, but all inputs to the GCS were frozen.  Is that your understanding of what happened?
Dave mentioned something about significant map data being loaded for these missions, any info on that?

### Pat Wells, 2024-11-26

@Ted Trowbridge yes I that is my understanding as well of how the GCS was behaving.

Today the customer mentioned that there was a large amount of map data indexed at the time these freezes occurred.  They noted a noticeable slow down in the responsiveness of the GCS software with this large about of map data loaded.  Since then they have started limiting the amount of map data they are loading and have noted that it doesn’t slow the GCS software down.

### Ted Trowbridge, 2024-11-26

@David Grosher @Pat Wells 
Looking at the GCS logs I can identify 4 times in the 241118_104601 flight where there was a large gap suggesting a UI freeze.  Each pause was after mission verification and upload and was followed by a master caution for loss of downlink:
```
[11:17:40.377] Verify mission...
[11:17:40.377] Mission DB in vehicle verified
[11:18:11.642] Show Caution(): Master Caution
[11:18:11.647] MessageBoxTop(): LOSS OF DOWNLINK WARNING
```
Immediately after Mission DB in vehicle verified the mission is FTP’ed to the vehicle.  I believe the FTP transfer may have hung and/or timed out causing the UI to freeze.  That’s further supported by the FDR download failure when pulling AARs which would also use FTP.
It’s not possible to disable the mission FTP to the vehicle.
It would be valuable to get the XCOMM logs, but I suppose that’s not possible at this time?  Can we ask them to try again?

### Pat Wells, 2024-11-27

@Ted Trowbridge I’m going to work with the customer to potentially obtain the XCOMM logs.
In the meantime is there anything the customer should be concerned about in regards to safety of flight related issues?  They’ve currently grounded their fleet pending our response to this issue.

### Ted Trowbridge, 2024-11-27

@Pat Wells I would agree with the customer that consistent long freezes of the GCS would present a risk to safety of flight, there’s nothing I can provide yet that will allow them to un-ground the fleet.  I am hoping to learn more from additional logs in order to reproduce the issue and provide them a resolution or workaround.
It’s possible to pull logs with just and FTP client rather than generating AARs.  I’m not sure if we ever suggest customers do that, but it might help uncover further issues with FTP.  I think it would also be possible to pull from the XCOMM and VTOL web pages?  Is that a standard procedure?

### Pat Wells, 2024-11-27

@Ted Trowbridge my plan was to ask them to FTP the logs.  That’s what I initially asked and they didn’t do it. 
More to follow.

### Pat Wells, 2024-12-02

@Ted Trowbridge @David Grosher Additional data attached from aircraft 646 for your review.

### Pat Wells, 2024-12-03

@Ted Trowbridge @David Grosher additional data attached for aircraft 645.

### David Grosher, 2025-01-07

@Pat Wells We can’t analyze this issue with the provided data. There is no data regarding GCS performance and there are no steps to reproduce. I suggest we close this, Bermuda triangle

### Alexander Alan Arnold, 2025-01-10

@David Grosher If you are fine with this, I will move it to D8 Bermuda triangle.

@Pat Wells FYSA

### David Grosher, 2025-01-10

We can’t reproduce the issue and there is no data in the current set of logs that would help us figure this out. We have received a few reports of issues with the GCS freezing on occasion and it is usually when large amounts of map data are loaded or when many other applications (such a software to support payload operation) are running concurrently. As systems move to the OGCS on this program this is expected to be addressed.

## Attachments (11)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [645 operator statement.docx](attachments/24665_645%20operator%20statement.docx.md) | docx | 15 | 2024-11-22 | converted |
| [646 operator statement.docx](attachments/24664_646%20operator%20statement.docx.md) | docx | 18 | 2024-11-22 | converted |
| Picture 1.png | image | 440 | 2024-11-22 | listed only |
| Picture 2.png | image | 10424 | 2024-11-22 | listed only |
| Picture 3.png | image | 346 | 2024-11-22 | listed only |
| Picture 4.png | image | 489 | 2024-11-22 | listed only |
| Picture 5.png | image | 504 | 2024-11-22 | listed only |
| T95_V645_241030_024020_pack.zip | archive | 679 | 2024-11-22 | listed only |
| T95_V646_241118_104601_pack.zip | archive | 340 | 2024-11-22 | listed only |
| 646_AAR-Data_Direct-from-AV.zip | archive | 48433 | 2024-12-02 | listed only |
| 645 - AAR Data - From AV (1).zip | archive | 44120 | 2024-12-03 | listed only |
