# VXEP-1951: VXE 996 RR Motor detached from boom

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** Highest
- **Created:** 2026-07-07
- **Updated:** 2026-10-12
- **Reporter:** Jackson Riley Curvin
- **Assignee:** Sanjay Menon
- **Creator:** Jackson Riley Curvin
- **Labels:** Hardware, RCCA, Weekly-incident-tracker
- **Links:** relates to VXEP-1903 (VXE 996 Link Loss on landing); relates to VXEP-1902 (VXE 1008 Excessive wobble and vibration); relates to RMA-1051 (VXE-996 RMA 260708-2); relates to VXEP-1686 (VXE 966 Intermittent Loss of communication to Xcomm); relates to VXEP-628 (Systemic VXE30 VTOL ESC Reliability Issues )
- **Customer:** CBP
- **Vehicle Tail Number:** VXE-996
- **Vehicle Configuration:** BLK 40 4p Batt
- **Problem Type:** Discovered Issue
- **Plan:** 7/9/2026 Pull logs w/ support from @Jeremy Kostel and @Scott Whitney and inspect hardware upon arrival
- **Issue Status:** 7/9/2026 Vehicle being shipped to SLO today
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical
- **Components (EA Aircraft):** Aircraft, full assembly
- **Executive Summary:** Investigation ongoing see Powerpoint for update. Probable cause is Hardware.

## Description

Investigation PPT: https://redwireglobal.sharepoint.com/:p:/r/sites/FlightSafety/Shared%20Documents/Active%20Cases/2026_07_03_V996/V996%20Crash%20Investigation.pptx?d=w3fd7bab31fe8475096a268ad95995b97&csf=1&web=1&e=rkD24X
Sharepoint: https://jenaero.sharepoint.com/:f:/s/FlightSafety/IgDDuBywvaxpSLctLhI-F0-VAdDZo3nuC7F0Mg5mC3tRF3Y?e=qZkGi8

Customer stated that the RR Lift Motor appeared to detach from the lift boom during transition from forward flight to VTOL

Operator statement:
 took place on July 3, 2026, near Amado, Arizona.   
 
The mishap took place at approximately 1545 hours local time and about 1.2 hours into the second flight of the day. The weather during both flights was hot, with a high of 103 degrees. The highest wind speed measured by the VXE-40 was 15 miles per hour from the south. The first flight was uneventful with the exception that on both the take-off and landing the VTOL arms were vibrating in the same manner that was observed during the training that took place in Tucson the week of June 1-5. The vibrations were also observed during the take-off of the second and final flight.
 
At approximately 1542 I commanded the VXE-40 to land at the primary landing zone and it proceeded as expected to a straight on approach and once it descended to approximately 300 ft AGL it made its final approach and began to activate the VTOL motors. Once the VTOL motors sounded like the reached their prescribed speed a “pop” was heard followed a tuft of debris that was observed from the right rear motor and was immediately followed up with the three remaining motors shutting off. The VXE-40 then fell straight down with a slight rotation until it impacted the ground.  The attached images are of the undisturbed VXE-40 immediately after walking to the crash site.

## Comments (30)

### Jackson Riley Curvin, 2026-07-07

@Scott Lovett @David Grosher Still awaiting more information at this time.

### Jackson Riley Curvin, 2026-07-07

@Matt Philley

### Matt Philley, 2026-07-07

@Jackson Riley Curvin appreciate it. We are taking a look here. Extremely bizarre… We dont even know how it would be possible to break a motor free like that from the composite. 
From that pic it looks like a motor-sized hole is now present in the bottom of the boom in the RR position and the whole motor and cover are missing? At most I would think the motor would just tear out the screws like we have seen when we had an avionics box break free from a composite, but to tear out a whole circle seems very strange. 
Unfortunately the video is pretty low resolution so nothing we can really get from that.

### Jackson Riley Curvin, 2026-07-07

@Matt Philley in the video you can hear and audible pop right before the language we are curious if the prop struck the lift boom.

### Matt Philley, 2026-07-07

@Jackson Riley Curvin maybe… if the prop struck the boom though I would suspect damage to the boom somewhere around here, which I dont see at least in this picture. 
Either way super strange and we will need to follow all the normal steps to get the AC somewhere we can get access to it so we can assign folks to step thru the investigation. 
[embedded: image-20260707-154920.png]

### Jackson Riley Curvin, 2026-07-07

@Ted Trowbridge

### Ruysser Gabler, 2026-07-07

@Matt Philley The statement also notes vibration on take off and landings of previous flights as well as the TO of this one. Is there a potential that the excessive vibrations they were seeing weakened the composite and it finally broke on this landing?

### Greg Fryer, 2026-07-08

@Ruysser Gabler I’m going to put this in the bucket of “not guessing at failure mode in chat, because then it becomes true” 🙂  We’ve got half a dozen theories, but need to see the composite in detail to actually narrow down.

### Pat Wells, 2026-07-08

@Jackson Riley Curvin @Matt Philley  @Greg Fryer 
This is being overnighted to SLO today.  Who needs it in their hands in SLO tomorrow to investigate the composites?

@Drew Hildreth @Alexander Alan Arnold 

@Lauren Velasquez please add tracking numbers to this ticket and link to RMA ticket.

### Alexander Alan Arnold, 2026-07-08

fedex 874117045670

customer notified me that equipment has been dropped off at Fedex

### Matt Philley, 2026-07-08

@Pat Wells I just spoke with Greg and @Sanjay Menon will be the focal and I will support him with the admin stuff. If both he and I are notified we can jump on it.

### Sanjay Menon, 2026-07-08

@Matt Philley @Greg Fryer Initial review of the video: a clear "pop" sound followed by a puff of dust and an object travelling away from the vehicle (looks to be a broken piece of propeller).
[embedded: image-20260708-193707.png]
[embedded: image-20260708-193727.png]
[embedded: image-20260708-193757.png]

Afterwards the right rear prop seems to be missing its blade (and/or counterweight? not totally clear in the video) and still rotating. The blade is broken off after impact, and all six screws mounting the motor remain and look like they’re tightened down:
[embedded: image-20260708-193824.png]
[embedded: image-20260708-193903.png]

Motor imbalance/dynamic behavior caused by the broken prop could have then led to the composite fracture. Blade strike seems possible, although as Matt pointed out there isn't a clear mark in the expected location on the boom.
Same result would be possible if instead the counterweight section of the prop broke first during flight. 
Next steps are to investigate hardware and vehicle logs to find the root cause of the right rear propeller breaking.

### Sanjay Menon, 2026-07-08

@Jackson Riley Curvin Was the brass counterweight or the blade of the RR prop found near the vehicle? If one was found next to the plane and the other lost/found far away, that would point to which one broke first

### Jackson Riley Curvin, 2026-07-09

@Sanjay Menon I am not sure the aircraft is on its way back to SLO now

### Pat Wells, 2026-07-09

@Matt Philley @Sanjay Menon The wing case has arrived. The RMA section has it for you to pick up and investigate.  Note we have a meeting with the customer tomorrow morning so anything you can share with us today will be valuable. 
@Alexander Alan Arnold @Scott Lovett  FYSA

### Alexander Alan Arnold, 2026-07-09

we are still waiting on the fuselage case for some reason they got split up

### Matt Philley, 2026-07-09

@Pat Wells @Alexander Alan Arnold @Greg Fryer
@Sanjay Menon  and I took a look already. We have some notes to digest, but ya Fuse Case is not here so we cant go thru everything nor attempt to pull XCOMM logs.
@Jeremy Kostel will pull ESC logs from the booms and attempt to pull VTOL logs from the CW. 
We will keep the case in RMA until the Fuse arrives to prevent stuff from wandering, but we will need to borrow the CW to power it safely over in Engineering. Jeremy will coordinate with Zack when he grabs it. It should only in Engineering less than an hour and he will comment on this ticket to track it.

### Greg Fryer, 2026-07-09

@Matt Philley @Sanjay Menon Can we start a mechanical review of the damage to the boom?

### Jeremy Kostel, 2026-07-09

CW and ESC logs have been pulled, everything is returned to RMA. Logs all located in the sharepoint folder. 
For anyone looking at data I believe VTL00135 is the incident VTOL log
[embedded: image-20260709-223454.png]

### Alexander Alan Arnold, 2026-07-10

we are on clock to provide a preliminary report to CBP by the 17th, understand we still do not have the fuse for the xcomm data but primary concern for customer is removing operator error from their own investigation. @Matt Philley @Sanjay Menon @Jeremy Kostel

### Matt Philley, 2026-07-10

@Alexander Alan Arnold is that need an output from the meeting with them today? 
Who is the RDT focal for that so Sanjay can align on what content and format is expected for that preliminary report?

### Alexander Alan Arnold, 2026-07-10

@Matt Philley yes, they were pretty adamant about today in the meeting, @Jeremy White @William Doupis are the customer facing PMs. The other FSRs and I can also be pinged on format and content when there is something to go over. Root cause would be incredible but understand what would probably not happen. major concern is just alleviating operator error as contributing factor.

### Jeremy White, 2026-07-10

@Matt Philley Format is whatever is standard for the group.

### Jackson Riley Curvin, 2026-07-10

@Matt Philley @Greg Fryer @Sanjay Menon The Fuselage just arrived in the RMA area.

### Eric Brewer, 2026-07-10

[embedded: image-20260710-185856.png]
@Alexander Alan Arnold reviewed the flight log, there was definitely a good bit of vibe in the pitch and roll axes on the transition out.  The climb looked on the high side of normal (our abort limits are above 1 for Axyz and 30 for rpy for more than a second, so it was below that during the climbout).  It’s hard to know if the vibe was due to the hardware failure or if the vibe caused the hardware failure.  hopefully physical inspection would yield some clues here.

### Alexander Alan Arnold, 2026-08-12

@Sanjay Menon Has there been any major discoveries found or anything revealed for this investigation?

### Sanjay Menon, 2026-08-17

@Alexander Alan Arnold Narrowed down list of possible root causes currently being investigated is in the powerpoint. Currently the main threads of investigation are focused on prop testing and material analysis

### Jackson Riley Curvin, 2026-10-12

@Sanjay Menon  has there been any updates to this also I do not have access to the PowerPoint any more.

### Sanjay Menon, 2026-10-12

@Jackson Riley Curvin Added new link to the post-migration PPT, testing is still underway to try and recreate the failure

### Jackson Riley Curvin, 2026-10-12

@Sanjay Menon thank you!

## Attachments (14)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 996 possible prop strike.png | image | 30 | 2026-07-07 | listed only |
| Image (1).jpg | image | 1012 | 2026-07-07 | listed only |
| MicrosoftTeams-video.mp4 | video | 3144 | 2026-07-07 | listed only |
| VXE mishap front.jpg | image | 252 | 2026-07-07 | listed only |
| close-up of motor arm.jpg | image | 2831 | 2026-07-07 | listed only |
| image-20260707-154920.png | image | 889 | 2026-07-07 | listed only |
| Screen Recording 2026-07-07 181202.mp4 | video | 18157 | 2026-07-08 | listed only |
| image-20260708-193707.png | image | 27 | 2026-07-08 | listed only |
| image-20260708-193727.png | image | 60 | 2026-07-08 | listed only |
| image-20260708-193757.png | image | 89 | 2026-07-08 | listed only |
| image-20260708-193824.png | image | 35 | 2026-07-08 | listed only |
| image-20260708-193903.png | image | 2933 | 2026-07-08 | listed only |
| image-20260709-223454.png | image | 124 | 2026-07-09 | listed only |
| image-20260710-185856.png | image | 248 | 2026-07-10 | listed only |
