# VXEP-429: SW Release 6.3.0 Asset 481 Takeoff Failure

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-06-07
- **Updated:** 2024-12-24
- **Resolved:** 2024-08-23
- **Reporter:** Carl Graf
- **Assignee:** David Grosher
- **Creator:** Carl Graf
- **Labels:** Stalker-Standard, VXE30_only
- **Links:** relates to FS2-1950 (v481 - Investigate launch abort); relates to FS2-1960 (v481 Investigation - Software Regression Flight test incident); relates to VXEP-514 (VXE 696 - Software release 6.3.2 Asset 696 Takeoff Failure); relates to VXEP-846 (Remove and tag hardware from 481 incident)
- **Start date:** 2024-06-07
- **Sprint:** XKIT 5/29-6/18
- **Vehicle Tail Number:** 481
- **Vehicle Configuration:** Stalker-Standard (VXE30)
- **Corrective Action:** See https://jenaero.atlassian.net/browse/VXEP-514
- **Production Stakeholder:** David Grosher
- **Other Stakeholder (as required):** Greg Fryer
- **Problem Type:** Other (explain in description)
- **Issue Status:** Same issue as v696. Closed
- **Root Cause:** See https://jenaero.atlassian.net/browse/VXEP-514
- **Incident Type:** Aircraft Loss
- **Monitor Type:** Flight Test (Engineering)
- **Severity:** 1 - Flight Critical
- **Components (EA Aircraft):** Aircraft, full assembly, Firmware, Software, General

## Description

Ref: VXEP-429 SW 6.3.0 Asset 481 Takeoff Failure 20240607.pptx
Fishbone: VXEP-429 Fishbone.vsdx
Photos & Video: 06.07.2024 Regression testing launch crash

## Plan

EE evaluation to determine if powering up to download the AAR will not cause further damage. If deemed safe, power up and download data files.

## Comments (10)

### Carl Graf, 2024-06-07

[2:02 PM] Ruysser Gabler
1f373_cooking 1 surprised 1
[2:02 PM] Artis Bertulis
Flight #4 during take-off all the motors just stopped at around 50-100ft and it just dropped down on its nose
[2:03 PM] Artis Bertulis
Don’t have the AAR as the GCS shows lost link, not sure if we should attempt to power it on to get it
[2:04 PM] Scott Whitney
 What are the risks to powering it on to retrieve the ARR?
[2:05 PM] Artis Bertulis
I don’t know what’s damaged and don’t want to damage it more by connecting battery to a crashed vehicle
[2:06 PM] Artis Bertulis
We will pack it up and deliver it to engineering ASAP, no more flights today
[2:06 PM] Michael Berger
Is there an advantage to getting the AAR now, vs bringing it  back to the office and checking it as we try to power it up? I think waiting is the better choice.
[2:09 PM] Scott Whitney
 
Artis Bertulis
We will pack it up and deliver it to engineering ASAP, no more flights today

Sounds good
 
[2:11 PM] Artis Bertulis

Debug during launch 
[2:12 PM] Artis Bertulis
VTOL window did not register any issue
[2:12 PM] Artis Bertulis

### Carl Graf, 2024-06-07

@David Grosher @Kurt Burian @Jason Scherer, @Hayden Jeanor is going to take a look at the asset when it gets here and upload any data. Please review and start going over the data ASAP.

### Carl Graf, 2024-06-07

[2:36 PM] Michael Berger
VTOL widow says Starring descent, it should not say that unless there was a problem.
[2:38 PM] Michael Berger
debuglog says says launch is aborting. Another indication that something went wrong on launch.

### Hayden Jeanor, 2024-06-10

Logs were recovered and distributed on 6/7 by removing avionics box and connecting to the IB.

### Jason Scherer, 2024-06-10

Was a launch abort commanded?

[embedded: image-20240610-162708.png]

### Artis Bertulis, 2024-06-10

Added a picture of HLB connector after the crash
[embedded: Image.jpg]

### Artis Bertulis, 2024-06-10

Also here are the pictures and videos 06.07.2024 Regression testing launch crash

### Cody Smisek, 2024-10-07

@Greg Fryer I see this issue is closed. Are we clear to disposition/dispose of the hardware? Currently stored under the engineering stairwell area.

### Greg Fryer, 2024-10-08

@David Grosher To answer @Cody Smisek this looks done, and it looks like you closed it. Any issue with the team dispositioning the HW? Save what we can, scrap the rest (generally).

### David Grosher, 2024-10-08

@Greg Fryer @Cody Smisek All of the hardware should be red tagged.  The only valid use at this point is in a HIL or iron bird if it is functional.

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Asset 481 01.jpg | image | 111 | 2024-06-07 | listed only |
| Asset 481 02.jpg | image | 70 | 2024-06-07 | listed only |
| Asset 481 03.jpg | image | 65 | 2024-06-07 | listed only |
| T95_V481_240607_155445_01_pack.zip | archive | 2892 | 2024-06-07 | listed only |
| Image.jpg | image | 171 | 2024-06-10 | listed only |
| image-20240610-162708.png | image | 14 | 2024-06-10 | listed only |
| MISB-06072024-155151-0.mpg | video | 23888 | 2024-06-12 | listed only |
