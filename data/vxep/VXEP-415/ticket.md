# VXEP-415: VXE 538 Altitude Drop During Landing

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-05-22
- **Updated:** 2026-03-02
- **Resolved:** 2025-03-20
- **Reporter:** Pat Wells
- **Assignee:** Rajesh Budhabhatti
- **Creator:** Pat Wells
- **Labels:** TIQUILA, Weekly-incident-tracker
- **Links:** relates to ENG-3073 (538 Altitude Drop During Landing); relates to FS2-3286 (Review and update max pause duration during descent. Coordinate with software to implement. ); relates to VXEP-12 (TPTR-87 VXE 511 VTOL Connector Issues 516 CW. Contains Main connector/contact C/CAs); relates to RMA-253 (VXE-538 TIQ RMA 240524-1); relates to VXEP-553 (AS150 Plug/Pin Connector Issue Systemic Collector)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 538
- **Incident Type:** Near Miss
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Summary as reported by Lockheed FSR:
During a training flight the student pilot was practicing manual nudge during a vertical landing. With the aircraft paused they were maneuvering around when it stopped pausing and started to descend. At around 20 feet it started to behave erratically, contacted the ground, slid, and then became airborne again before landing. Damage was limited to the aft landing pad.
Here’s the student’s notes, “During a paused manual nudge, whilst correcting forward movement with the xbox controller the system seemed to override the pause at approx 20ft. Control was lost and the system began to decend in a forward motion, landing off from the LZ by approx 10m into the scrub. Motors stopped upon landing before this was selected via GCS”

AAR attached

## Corrective Action

CAs are recorded here
https://jenaero.atlassian.net/browse/VXEP-12
https://jenaero.atlassian.net/browse/VXEP-386 
The main ones that could help with this issue are:
- the automatic software aborthttps://jenaero.atlassian.net/browse/VA-93
- Contact inspection and cleaning (these contacts look pretty clean). https://jenaero.atlassian.net/browse/SMU-70

## Plan

Review recently released cleaning contacts documents. Determine if this may have prevented that. @Pat Wells 
Hardware:
- Try to reconnect to aircraft. If unable to, ask for firmware support. @Mark Squillante  - done, successful
- Cam to present options to address fleetwide options for AS150 options. Done see  https://jenaero.atlassian.net/browse/XKIT-1716
- This looks like a long pause. @Rajesh Budhabhatti based on your investigation, should this pause duration and throttle cause any issues on a normal aircraft? 9-17-24: I am looking at AAR data. I see that the pause is under 100 second, which is high; but the iBatt1 and iBatt2 currents are moderate 80A so I don’t think this could be a problem. However the VBatt falling below 18V could be an issue caused by contact resistance. The anti-spark ring on the battery connector looks a bit frayed.
- @Pat Wells I think we are ok to approve replacing the dual current sense, but we should answer the questions below before replacing any avionics or returning the aircraft.

Firmware: 
- Determine why unable to connect to aircraft via radio originally or at all now. 
- Mark was able to connect. Should we troubleshoot this further?
- @David Grosher does anything in the data indicate the cause of this behavior. “started to descend. At around 20 feet it started to behave erratically, contacted the ground, slid, and then became airborne again before landing. Damage was limited to the aft landing pad.” This seems to have occurred after the voltage returned to normal.

## Issue Status

Aircraft was invoiced 8/11/23, and built with parts before that. The improved supplier was established ~Oct 2023. It did pass our resistance check, but that could be evidence that it is batch related (all aircraft before ~Oct/23, so still a lot of aircraft)
Quick voltage drop measured ~10 seconds before the reported behavior. Need to confirm if this could be the cause or not. It looks like power contacts were inspected and passed the measurement ~10/19.
[embedded: image-20240522-172911 (a579cb85-4463-484b-b3a9-a491aa39a725).png]
 Added powerpoint summary here.

## Root Cause

Suspected: This seems to be the difficult and predicted case of contacts that passed initial testing, but then failed later due to increased resistance (possibly due to plating issues or faulty parts).
AS150 Pin test Results (<235uOhm is pass):
- First test: 435uOhm - FAIL
- 2nd Test after cleaning: 317uOhm - Fail
- 3rd Test after cleaning again: 232uOhm - Pass (Barely)

Aircraft was invoiced 8/11/23, and built with parts before that. The improved supplier was established ~Oct 2023. It did pass our resistance check, but that could be evidence that it is batch related (all aircraft before ~Oct/23, so still a lot of aircraft)

## Comments (28)

### Pat Wells, 2024-05-22

@Douglas Baker FYSA issue during TIQ training event.

### David Grosher, 2024-05-22

@Cameron Chapman This looks like an electrical issue given the dip in the HLB to 18 volts. 
[embedded: image-20240522-172911.png]

### Douglas Baker, 2024-05-22

@Pat Wells Do we think they will ask for a containment plan on this issue?

### Pat Wells, 2024-05-22

@Cameron Chapman pictures of connector added. 
Comments from LM FSR: The center wing power connector exhibits signs of distress. The HLB for that flight showed no signs. The resistor on the center wing connector was measured at 5.7 ohms.

### Pat Wells, 2024-05-23

@Cameron Chapman FYSA this aircraft is on it’s way back to SLO on an RMA due to the power connector issues.  
Does your team need the hardware to continue investigating?
@Sean Odell FYSA

### Cameron Chapman, 2024-05-23

@Pat Wells and @Sean Wendling, yes, we will test when it arrives. This seems to be the difficult and predicted case of contacts that passed initial testing, but then failed later due to increased resistance (possibly due to plating issues or faulty parts). CAs are recorded here 
https://jenaero.atlassian.net/browse/VXEP-12 
The main ones that could help with this issue are:
- the automatic software aborthttps://jenaero.atlassian.net/browse/VA-93
- Contact inspection and cleaning (these contacts look pretty clean). https://jenaero.atlassian.net/browse/SMU-70

### Sean Wendling, 2024-05-23

Hey @Cameron Chapman, did you mean to ping @Sean Odell ? If there is any support I can provide lmk 🙂

### Cameron Chapman, 2024-05-23

I did. Thanks @Sean Wendling

### Sean Odell, 2024-05-30

@Cameron Chapman @Pat Wells Aircraft incoming evaluation complete. Photos on RMA ticket including initial report. I am bringing over the aircraft as soon as I tag with RMA tags.

Preliminary findings: Aircraft could only be connected Hardwired and ARR unable to be generated by GCS. All software was latest released version and radio was correct also. Upon power cycling the aircraft I have lost ALL connection both wired and wireless. 
AS150 Pin test Results (<235uOhm is pass):
- First test: 435uOhm - FAIL
- 2nd Test after cleaning: 317uOhm - Fail
- 3rd Test after cleaning again: 232uOhm - Pass (Barely)

### Cameron Chapman, 2024-06-03

@Mark Squillante are you available to power up this aircraft and see if you can connect to it? See plan field above.

### Mark Squillante, 2024-06-03

@Cameron Chapman I should be able to help with that.

### Mark Squillante, 2024-06-05

@Cameron Chapman I am able to connect to the vehicle via GCS software as well as through webpage.

### Pat Wells, 2024-06-18

@Sean Odell this is cleared by the engineering team for repair. Please proceed. 6/18/24

### Sean Odell, 2024-07-01

@Cameron Chapman I see notes that a possibly Dual current sense assembly is needed on this centerwing. Is there any other assembly that needs to be replaced from the teams investigation? I was told to finish my repair quote but no one told me if anything needs to be replaced. Thank you for any help you can provide.

### Cameron Chapman, 2024-07-01

@Sean Odell that part appears to be the cause of this issue and the only electrical damaged part. The description also mentions a damaged aft landing pad.

### Sean Odell, 2024-07-01

@Cameron Chapman I am tracking the physical damage like the landing pad, but now you confirmed the electrical side of things. I can now work on completing this quote for repair. Appreciate the assistance!

### Pat Wells, 2024-09-16

@Cameron Chapman are we ready to close this out with the customer. I believe the last discussion we had the plan was to link the connector issue to our previously released Mating Connection Air Worhiness Directive.

### Rajesh Budhabhatti, 2024-09-16

@Pat Wells @Cameron Chapman Hi Patrick, I am looking at AAR data. I see that the pause is under 100 second, which is high; but the iBatt1 and iBatt2 currents are moderate 80A so I don’t think this could be a problem. However the VBatt falling below 18V could be an issue caused by contact resistance. The anti-spark ring on the battery connector looks a bit frayed.

### Cameron Chapman, 2024-09-17

Thanks @Rajesh Budhabhatti agreed. The main cause seems to be failed contacts. I was asking about the pause and current loading to see if that could have caused the damage to the contacts. So that profile should not overheat anything based on your analysis? It seems closer to 150A on the second half, not 80.  

[embedded: image-20240917-220054.png]

### Rajesh Budhabhatti, 2024-09-17

Yes, I see, 150A with a peak to almost 180A peak for two motors.
I see the power connector with black plastic peeled and frayed. This makes me think that the power connector was the issue.
Raj

### Pat Wells, 2024-11-05

@Cameron Chapman can we work on closing this out and getting the aircraft back to RMA for repair?

### Cameron Chapman, 2024-11-06

@Pat Wells electrically, we are ready for RMA. 
@Eric Brewer , do you think we should investigate these more, or do you recommend sending to RMA? 
Firmware:
- Determine why unable to connect to aircraft via radio originally or at all now.
- Mark was able to connect. Should we troubleshoot this further?
- does anything in the data indicate the cause of this behavior. “started to descend. At around 20 feet it started to behave erratically, contacted the ground, slid, and then became airborne again before landing. Damage was limited to the aft landing pad.” This seems to have occurred after the voltage returned to normal.

### Pat Wells, 2024-11-06

@Sean Odell FYSA

### Eric Brewer, 2024-11-06

@Cameron Chapman , I took a quick look at the logs and uploaded a summary here.  The rapid descent definitely looks related to the battery issue.  I am less clear on why the pause command was cancelled.  It seems hard to believe it would be coincidental to the voltage drop but I can’t seem to find the logic in the code that might trigger it.  @Ted Trowbridge do you have any ideas on what might have triggered that in the GCS code?

### Alexander Alan Arnold, 2024-12-10

@Rajesh Budhabhatti Is D4 an accurate status for this investigation?

### Alexander Alan Arnold, 2025-01-10

@Rajesh Budhabhatti Any updates?

### Pat Wells, 2025-03-17

@Cameron Chapman what is left to close this out?  We’ve already repaired and returned the aircraft to the customer.

### Cameron Chapman, 2025-03-19

@Pat Wells  I think this is ready to close. CA: replace AS150 contacts in B35.

## Attachments (9)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IMG_2447[1].JPG | image | 2535 | 2024-05-22 | listed only |
| IMG_2448[1].JPG | image | 2907 | 2024-05-22 | listed only |
| IMG_2449[1].JPG | image | 2766 | 2024-05-22 | listed only |
| IMG_2450[1].JPG | image | 2740 | 2024-05-22 | listed only |
| T95_V538_240521_105006_pack.zip | archive | 4019 | 2024-05-22 | listed only |
| image-20240522-172911 (a579cb85-4463-484b-b3a9-a491aa39a725).png | image | 151 | 2024-05-22 | listed only |
| image-20240522-172911.png | image | 151 | 2024-05-22 | listed only |
| csg-icon-genericAttachment | other | 0 | 2024-09-17 | listed only |
| image-20240917-220054.png | image | 135 | 2024-09-17 | listed only |
