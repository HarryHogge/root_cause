# VXEP-1066: VXE 448 Multiple Aborted takeoffs

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-03-04
- **Updated:** 2026-08-18
- **Resolved:** 2025-04-15
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Greg Fryer
- **Creator:** Alexander Alan Arnold
- **Labels:** MARSOC, Software, Weekly-incident-tracker
- **Links:** relates to ENG-3018 (Low potentially interfered GPS signals, multiple repeated launch aborts); relates to VXEP-527 (VXE 469 Uncommanded aborted VTOL launch at 100ft AGL); relates to VXEP-102 (VXE-380 Launch abort)
- **Customer:** MARSOC
- **Vehicle Tail Number:** VXE 448
- **Vehicle Configuration:** Standard VXE 30 Battery config
- **Corrective Action:** No CAs, aircraft performed as designed and aborted launch due to exceeding limits.
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Operator Statement
On Saturday 1st we had a drill and had two unsuccessful launches with our stalker system. The first launch our pre flight inspections were completed and pre flight launch was conducted with now issues on the GCS. It VTOLed about 20-30ft AGL before returning to land. We then switched the hybrid battery ran through pre flight inspection and pre flight launch on the GCS with no issues. After launched it VTOLed to its transition height 300ft AGL and as the main prop started it turned off and begun descending back to land. We then switched to our secondary VXE30 and had no issues. Today Monday the 3rd we took stalker 448 our primary VXE30 inspected all motors and props, inside and out and did not see any issues. We did our pre flight inspections and pre flight launch with no issues on the GCS and had a successful launch and recovery. Attached is the files for both failed launches and the successful launch today. Files 071724 and 072626 were the failed. File 010044 was the successful launch. We are using our other stalker, until we find out if this one has an issue we need to fix. Please let me know as soon as you guys can if there is anything I need to do to make this bird operational. We only have the one for now and even with the successful launch today I don't feel comfortable flying 448 for any ops until I know what is going on.

SharePoint Link VXEP-1066 VXE448 Aborted Takeoffs
Presentation Vehicle Investigation VXEP-1066.pptx

## Issue Status

Creating presentation with analysis of data. Appears there might have been 3 launch aborts on the same day with this aircraft. Not the originally reported 2, as noted by the GCS log notes below….
[embedded image-20250321-174244.png]

## Root Cause

Probable RF Signal interference led to U-Blox receiver performance / accuracy estimate indicators exceeding limits and causing launch abort.

## Comments (20)

### David Grosher, 2025-03-04

@Alexander Alan Arnold There is no XCOMM, VTOL, or FDR data in the logs.

### Alexander Alan Arnold, 2025-03-04

Tracking, I asked them to just preform a full download of data from xcomm and vtol ip since they cant do the AAR the right way. forgot to add it was incomplete. 

I will add it once they deliver it. @David Grosher

### Michael Mohr, 2025-03-10

@David Grosher Just received the AAR from the deployed unit and attached. It is a full download of all aircraft files.

### David Grosher, 2025-03-10

@Michael Mohr @Alexander Alan Arnold This would be a good first issue to try and tackle. Take a look at the xcomm event logs to see if you can identify the causes of the aborts. I find a text search for abort usually will get you there. I also have a section towards the bottom of my Grafana Dash board that will show a set of plots related to common things that could result in launch aborts, such as mismatches between the FW and VTOL APs, Cn0 or other sensor issues. Once we know what threshold was triggerred then we can decide on the next steps in the investigation. If the systems shows Link losses or communication errors then Jason can help with next steps, otherwise if it is sensor related then Eric can support next steps.

### Jackson Riley Curvin, 2025-03-10

@David Grosher looking at XC250303.txt file at 15.26.47.717 there was a  vtol fault during climb, RTLdebugMsg Climb abort, VTOL controller fault followed by a sensor: GPS fault followed by a sensor: laser range finder fault. At 15.27:29.127 ap dbg: vt 1ch abort request from gcs

### Michael Mohr, 2025-03-20

@David Grosher We did an initial look but can’t tie anything together. Has Jason had a chance to look at this? The customer has grounded this asset until we tell him something.

### Cody Smisek, 2025-03-20

@Michael Mohr is this vehicle CONUS?

### Michael Mohr, 2025-03-20

@Cody Smisek No, they are deployed.

### Cody Smisek, 2025-03-20

@Michael Mohr Suspect GPS interference. Will update with some plots this afternoon or tomorrow. Exceeded some accuracy checks during VTOL climb

### Cody Smisek, 2025-03-20

@Michael Mohr 
creating some slides and have linked the presentation in description field. Here’s quick look at what I’ve found so far that leads me to believe GPS interference. LRF fault might be a symptom of the GPS vertical accuracy being degraded. Need to confirm with code review. 
[embedded image-20250320-225059.png]

### Cody Smisek, 2025-03-21

@Michael Mohr Questions for MARSOC. What payload are they operating during these flights? Is there any special RF equipment in the area of their operations that is being utilized?

### Michael Mohr, 2025-03-21

@Cody Smisek I’ll ask.

### Michael Mohr, 2025-03-21

From customer:
“We were using the HD55 for day/night capabilities. No jammers that I know of. RF all over the place it’s very noisy in this area”

### Cody Smisek, 2025-03-21

@Michael Mohr if they've got AARs from other aircraft flights in the area I can take a look and compare those as well.
Data review suggests RF interference.

### Cody Smisek, 2025-03-26

@David Grosher @Greg Fryer 
More time could be spent to clean up presentation and add more code review of how a GPS fault occurs but it seems like the slides with graphical data provide the necessary explanation to the launch aborts observed. 
@Jason Scherer and I browsed through the code to try and understand the LRF fault more yesterday, it seems likely the LRF fault is going to occur anytime we’re outside of it’s operational range and one of the other faults trips. This can also be seen in the linked ticket for https://jenaero.atlassian.net/issues/VXEP-102?jql=textfields%20~%20%22launch%20abort%2A%22. I don’t think I’ll be able to fully digest the code to understand how that occurs and break it down in a slide. 
If we want to spend more time cleaning up the presentation, can do, otherwise ready to close out this ticket and provide follow up to customer if @Michael Mohr hasn’t already.

### David Grosher, 2025-03-26

@Pat Wells It might be good to have the FSR team update the report so that they understand the analysis.

### Pat Wells, 2025-03-26

@Jackson Riley Curvin @Alexander Alan Arnold @Michael Mohr 
Please reveiw and update the report. This will help you get a better understanding as Dave mention’s below.

@Drew Hildreth FYSA

### Pat Wells, 2025-04-01

@Jackson Riley Curvin @Michael Mohr

### Alexander Alan Arnold, 2025-04-15

@Michael Mohr @Jackson Riley Curvin Seems like GPS/RF interference was the culprit, we may potentially be able to close this one and let customer know there's nothing wrong internally. 
@Drew Hildreth FYSA

### Michael Mohr, 2025-04-15

@Jackson Riley Curvin @Alexander Alan Arnold Agree on closing. I already informed the customer that we were leaning toward GPS interference, and it is safe to fly.

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V448_240305_010044_pack.zip | archive | 107 | 2025-03-04 | listed only |
| T95_V448_250301_071724_pack.zip | archive | 98 | 2025-03-04 | listed only |
| T95_V448_250301_072626_pack.zip | archive | 128 | 2025-03-04 | listed only |
| VXE448AArs.zip | archive | 339836 | 2025-03-10 | listed only |
| image-20250320-225059.png | image | 282 | 2025-03-20 | listed only |
| image-20250321-174244.png | image | 2 | 2025-03-21 | listed only |
