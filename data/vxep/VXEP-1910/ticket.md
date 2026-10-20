# VXEP-1910: VXE 954 is an Adv Nav aircraft but gains show (95), we changed the gains page to 115 and set to AP but when we power cycle the aircraft goes back to 95 in the gains.

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2026-06-11
- **Updated:** 2026-07-06
- **Resolved:** 2026-07-06
- **Reporter:** Michael Lindsay
- **Assignee:** Eric Brewer
- **Creator:** Michael Lindsay
- **Labels:** GS_Closed, MOLSON, RCCA, Weekly-incident-tracker
- **Links:** relates to VXEP-1914 (VXE 931 FW AP not set to Adv Nav vehicle type)
- **Customer:** MOLSON
- **Vehicle Tail Number:** 954
- **Vehicle Configuration:** VXE30 Adv Nav, Battery Config
- **Problem Type:** Production Issue
- **Severity:** 1 - Flight Critical

## Description

While doing the maintenance portion of the course it was discovered that the firmware was showing the correct firmware for and adv nav but was asking for updates back to the standard blk 30.  We updated the gains to 115 and sent to AP, but when we power cycle the aircraft the gains go back to 95 and will not stay as 115.

## Comments (10)

### Carson Buckley, 2026-06-11

@Michael Lindsay  This will need to be returned under RMA, assigned to @Lauren Velasquez for intake.

### Michael Lindsay, 2026-06-17

Following MOLSON 7 this aircraft will have the FW AP uploaded with the 115 build provided by @Eric Brewer .  following updating I will provide a XCOMM full pull for review.

### Michael Lindsay, 2026-06-18

@Eric Brewer @David GrosherI have completed the XCOMM AP Firmware updated with the HEX file provided.  The throughput page in XCOMM is showing vehicle type 115.  I have completed an LW with not further issues.  I have uploaded the XCOMM full pull for 954 for your review.  @Carson Buckley FYSA

### Eric Brewer, 2026-06-18

@Michael Lindsay thanks. Looks like it was connected to the same SGCS as 931.  Same 3 build times also.  Will be good to review those logs once we get them.
[embedded image-20260618-153418.png]

### Eric Brewer, 2026-06-18

@David Grosher @Ted Trowbridge FYI.

### Drew Hildreth, 2026-06-23

@Michael Lindsay Have you had a chance to get the additional logs that Eric is talking about below?

### Michael Lindsay, 2026-06-23

@Eric Brewer @Drew Hildreth Are the logs that you are referring to from SGCS-253 that was used to update the aircraft?  Or are you requesting different logs.

### Eric Brewer, 2026-06-23

@Drew Hildreth, @Ted Trowbridge should be able to provide details of the logs we’re looking for.
It’s also worth asking if they ever did a manual update of the vehicle type in the gains panel.   I could see a scenario where they got the error that the GCS they had wouldn’t connect (if it’s a VXE30-only GCS it won’t connect to an advanced nav bird), and then maybe they updated the vehicle type manually.

### Drew Hildreth, 2026-06-23

@David Grosher @Ted Trowbridge @Scott Whitney is there any CA for this? Is there anything I can relay to MOLSON on how this is being addressed? Eric provided a fix which worked, but will that be the norm should this present itself again?

### Scott Lovett, 2026-07-06

Updated XCOMM firmware.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| XCOMM_VXE954.zip | archive | 2957 | 2026-06-18 | listed only |
| image-20260618-153418.png | image | 156 | 2026-06-18 | listed only |
