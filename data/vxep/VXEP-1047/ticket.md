# VXEP-1047: VXE-729 Aborted launch

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2025-02-24
- **Updated:** 2026-09-09
- **Resolved:** 2025-06-04
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** No_crash, PMA263, Software, Weekly-incident-tracker
- **Links:** relates to FS2-2332 (Investigate AP Link Loss issues on FW AP); relates to VXEP-1179 (498 Aborted Launch); relates to FS2-3145 (Investigate VXEP-1047); relates to VXEP-1057 (VXE 398 Aborted Takeoff after 10 feet)
- **Customer:** PMA263
- **Part Number(s):** VXE 30 standard config
- **Issue Status:** Customer continues to be non-responsive on our requests.
- **Root Cause:** Believed to be software related
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

SOI-E are experiencing system commanded launch aborts after 200-250 feet AGL on multiple aircraft without warning.

SharePoint: VXEP-1047 Launch Abort

## Comments (23)

### Alexander Alan Arnold, 2025-02-25

After speaking with the operator that experienced the issues, he explained 507 was fine and that it is 498 with I believe the 497 CW and 494 with 503 CW that are having the abort issue. Deleted 507 data from ticket. 

I will upload the other data once it is provided. @David Grosher

### Alexander Alan Arnold, 2025-03-07

For VXE 729, which will be added to this ticket, this data is from the march 3rd AAR file in the xcevlog associated with the flight., 
[20:19:40.376 1101.376] ap link fault: local rx okay ap rx bad
[20:19:40.379 1101.379] ap link fault during climb/transition, RTL
In the xcl00019 file for march 3rd in the linkApTx and Rx columns there are still numerical values present 

From March 4th xcevlog
[13:48:49.114 6438.114] ap dbg: vt lost link during lch, aborting

All of these flights are from the same customer at the same site. @David Grosher 

The issue Jackson and I are running into are what exactly the lost link is in reference too. Is it Silvus link or internal link from the aircraft or a combination of both?

### Alexander Alan Arnold, 2025-03-07

https://jenaero.atlassian.net/browse/VIT2-275 

@Jackson Riley Curvin Dug this one up are these related and still a bug in 6.3.4?

@David Grosher

### David Grosher, 2025-03-07

@Alexander Alan Arnold There was no change that resulted from that previous investigation. It never looked into the reason that comms dropped out. However, Jason has been looking into a few tickets where comms have been lost with the GCS and has found a few interesting issues that will likely need to be addressed. This could be related to those.

### David Grosher, 2025-03-11

@Jason Scherer This may be related to your other investigation into communication issues.

### Jason Scherer, 2025-03-11

@Alexander Alan Arnold Quick answer. The “vt lost link during lch, aborting” message occurs when the fixed wing autopilot does not receive messages from the GCS for more than 5 seconds during launch. 

When a GCS message is received on the fixed wing ap, a function called “MaintainLink()” is called which essentially resets a timeout timer. The fixed wing is checking 10 times per second to see if the timeout timer has expired (5 second timeout). So the launch abort would be commanded 5 seconds after the last message received from the GCS. It’s hard to say specifically which part of the link failed without digging further into the data. The link between fixed wing and GCS looks like this:
Fixed Wing AP<-serial connection->XComm<-Ethernet->XComm Network Switch<-Ethernet->IP Comm Network Switch<-Ethernet->Radio<-RF->Ground Radio<-Ethernet->GCS
I documented this launch abort message in more detail for a really old NCR, but the slides might be helpful here for reference. [embedded file] This was the very first investigation I was assigned, but it seems like we didn’t have a conclusive reason for the abort. We did conclude that it was a general software issue and not a vehicle specific issue, so the NCR was dispositioned with use as is.
Additionally, I have an ongoing general software investigation into issues like this [FS2-2332] Investigate AP Link Loss issues on FW AP - Jira with more information. I’ll link this ticket to that one, to keep track.

### Pat Wells, 2025-03-17

@Jason Scherer any updates or work arounds for this?  Customer is unable to fly their aircraft.

### Jackson Riley Curvin, 2025-03-31

[embedded image-20250331-203509.png]

### Jackson Riley Curvin, 2025-03-31

[embedded image-20250331-203605.png]

### Jackson Riley Curvin, 2025-03-31

[embedded image-20250331-203702.png]

### Jackson Riley Curvin, 2025-03-31

[embedded image-20250331-203834.png]

### Jackson Riley Curvin, 2025-03-31

[13:48:49.114 6438.114] ap dbg: vt lost link during lch, aborting
[13:48:49.116 6438.116] ap dbg: vt lch abort triggered
[13:48:49.117 6438.117] ap dbg: vt status: 10647

### Jackson Riley Curvin, 2025-03-31

[13:48:51.953 6440.953] ap link fault during landing
13:48:55.205 6444.205] vtol launch detected

### David Grosher, 2025-04-01

@Pat Wells @Alexander Alan Arnold @Jackson Riley Curvin Could you request an export of the radio configurations from the GCS and the birds (729 and 498)?  I want to rule out actual real link issues.

### Jackson Riley Curvin, 2025-04-02

@David Grosher I reached out to the customer yesterday doesn't seem likely that we will get that information.

### David Grosher, 2025-04-04

@Pat Wells @Jackson Riley Curvin It was mentioned in the incident meeting that other PMA-263 operators were having issues with un-commanded aborted launches but were not formally reporting those incidents. Is that happening with the same group or at the same location or with the same ground radio? Given that FLOPS is not experiencing this type of behavior and that we aren’t receiving incidents from other fleets or customers I think these potential links need to be explored further.

### Pat Wells, 2025-04-07

@Jackson Riley Curvin @Alexander Alan Arnold See Dave’s comment below. 
Can we track this down with SOIE?

### Alexander Alan Arnold, 2025-04-07

Jackson already asked the customer for this I believe, it might be worth asking Joe Brown what config PMA263 runs off of and load it onto a gcs in SLO to potentially recreate it. @Pat Wells

### Drew Hildreth, 2025-06-04

Closing due to lack of response from the customer.

### Drew Hildreth, 2025-06-04

Closed due to lack of customer response.

### Alexander Alan Arnold, 2025-04-07

Jackson already asked the customer for this I believe, it might be worth asking Joe Brown what config PMA263 runs off of and load it onto a gcs in SLO to potentially recreate it. @Pat Wells

### Drew Hildreth, 2025-06-04

Closing due to lack of response from the customer.

### Drew Hildreth, 2025-06-04

Closed due to lack of customer response.

## Attachments (9)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V498_250214_133747_pack.zip | archive | 1523 | 2025-02-25 | listed only |
| [flightdataloggcs-6.3.4-0.csv](attachments/26491_flightdataloggcs-6.3.4-0.csv.md) | csv | 72 | 2025-02-25 | converted |
| T95_V729_250303_121756_pack.zip | archive | 1630 | 2025-03-07 | listed only |
| T95_V729_250304_054701_pack.zip | archive | 1543 | 2025-03-07 | listed only |
| [AC 533-NCR-240617 Aborted TO after start of transition-Initial-Analysis.pptx](attachments/27069_AC%20533-NCR-240617%20Aborted%20TO%20after%20start%20of%20transition-Initial-Analysis.pptx.md) | pptx | 695 | 2025-03-11 | converted |
| image-20250331-203509.png | image | 36 | 2025-03-31 | listed only |
| image-20250331-203605.png | image | 17 | 2025-03-31 | listed only |
| image-20250331-203702.png | image | 24 | 2025-03-31 | listed only |
| image-20250331-203834.png | image | 22 | 2025-03-31 | listed only |
