# VXEP-1914: VXE 931 FW AP not set to Adv Nav vehicle type

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Medium
- **Created:** 2026-06-16
- **Updated:** 2026-08-12
- **Resolved:** 2026-08-12
- **Reporter:** Michael Lindsay
- **Assignee:** Alexander Alan Arnold
- **Creator:** Michael Lindsay
- **Labels:** GS_Closed, MOLSON, RCCA, Software, Weekly-incident-tracker
- **Links:** relates to VXEP-1910 (VXE 954 is an Adv Nav aircraft but gains show (95), we changed the gains page to 115 and set to AP but when we power cycle the aircraft goes back to 95 in the gains.)
- **Customer:** MOLSON
- **Vehicle Tail Number:** 931
- **Vehicle Configuration:** VXE30 Adv Nav - Battery config
- **Problem Type:** Discovered Issue
- **Severity:** 3 - Degraded Performance - With Workaround
- **Executive Summary:** Unable to re-create issue. Waiting on engineering guidance

## Description

While completing the launch wizard after the AP resets we get a warning that the firmware needs to be updated.  We have discovered that the FW AP is set to the standard Blk 30 (95).  We attempted to change the vehicle type to 115 in the gains but it would revert back to 95 following any power cycle or rest of the AP during the launch wizard.

## Comments (20)

### Michael Lindsay, 2026-06-16

@Eric Brewer I have completed the FW AP software update in the XCOMM, this has corrected the issue and it is showing as an Adv Nav (115) in both the XCOMM and GCS software.  I have completed a XCOMM dump and that added to this ticket for you to review.

### Eric Brewer, 2026-06-16

@Michael Lindsay thank you.  Based upon the logs, the vehicle was loaded with version 6.5.1 advanced nav (probably when it left the factory)?  There aren’t many event logs on here, and it looks like other than just today when we loaded the right software it hasn’t had a GPS fix (or time) since September of last year - does that seem right? At some point after September it was somehow flashed with the non-advanced nav version of 6.6.1 software (i can’t see the date that happened because after that flashing it doesn’t have GPS).

From the testing I’ve done on the GCS i cannot make this happen when the vehicle type is set correctly.  The 6.6.0 GCS (which supports only VXE30) will not connect or allow software updates with an advanced nav (T115) vehicle.  Is it worth asking them if they remember what was done during the upgrade/flashing process? Alternatively if they have any AAR’s they produced between September 11th of last year and now we can analyze them.  The xcomm event logs show a few logs on 9/11, then a bunch without dates (from not having gps), and then the logs we got today with the correct 6.6.1 advanced nav build loaded on.

@David Grosher @Scott Whitney FYI.

### David Grosher, 2026-06-16

@Michael Lindsay I think the GCS that flashed the bird was one of these two IP addresses: 
XC000101.TXT:[20:51:25.136 4771.136] ftp login attempt from:  10.0.11.51
XC000101.TXT:[00:02:04.516 116.516] ftp login attempt from:  10.0.253.51
 
If you can pull logs from them then you might be able to figure out the config that allowed it to happen

FYSA: @Eric Brewer @Ted Trowbridge

### David Grosher, 2026-06-16

@Eric Brewer @Michael Lindsay I think the incident occurred in XC000101.T01 with the GCS at IP address: 10.0.253.51. This is the first time I see a reference to the ublox receiver in the log right after the image is flashed. 

[00:21:12.697 563.697] ftp login attempt from:  10.0.253.51
[00:21:21.944 572.944] flasher version: BSL AP FLASHER 1.0
[00:22:22.756 633.756] ap dbg: NEO-M8N Config

### David Grosher, 2026-06-16

@Eric Brewer @Michael Lindsay Courtesy of @Jo Brown the 10.0.253.51 IP address is SGCS1-253. Let’s pull the logs from there.

### Michael Lindsay, 2026-06-17

@Eric Brewer @David Grosher I have attached all the GCS logs from SGCS-253.  Please let me know if there are the logs that you are requesting.

### David Grosher, 2026-06-17

@Ted Trowbridge Are the previous event logs still available on the GCS?

### Ted Trowbridge, 2026-06-17

@David Grosher @Michael Lindsay I don’t see any GCS logs attached, are you referencing the flightdatalog.csv?  I would be looking for the debuglog.txt and eventlog.txt that normally get packaged up with the AAR.

### Michael Lindsay, 2026-06-18

@Ted Trowbridge I have uploaded the files from SGCS-253 under program data / GCS.

### Ted Trowbridge, 2026-06-18

@Michael Lindsay nothing of note in the uploaded files.  The logs don’t provide any indication of why the vehicle type switched.

### Michael Lindsay, 2026-06-18

@Ted Trowbridge ack, is there anything else you need from this GCS.

### Michael Lindsay, 2026-06-18

@Eric Brewer I uploaded an AAR from yesterday we had to reset the aircraft after a HLB swap as we seem to have lost all Sats.  They did come back after power cycling and we flow several flights after with no issues.  Can you have a review of the attached AAR to ensure there is no issues with GPS.  Thanks

### Drew Hildreth, 2026-06-23

@Eric Brewer Have you had a chance to take a look at the latest AAR that Mike Uploaded?

@Scott Lovett @Stephan Johnson Please take a look at this as well and let me know what you all think. I want to start verifying that we are able to identify and analyze the AARs as if we were the Eric, or Dave, or Scott W. or Cody… the list goes on.

### Eric Brewer, 2026-06-23

@Drew Hildreth yes - sorry I responded to Michael directly and didn’t update the ticket.  The AAR contains one good flight (wiht GPS) and a short log before that (~15s) where the aircraft doesn’t have GPS.  15s is around the normal startup time so it wouldn’t be unexpected to not have GPS for that short a time period.  If you can get some logs that are earlier than these ones (assuming that’s when they had the issue?) i can take a look. 
[embedded: image-20260623-134950.png]

### Michael Lindsay, 2026-06-23

@Eric Brewer @Drew Hildreth I can get additional AARs 931, but we didn’t have any GPS issues after we updated the FW AP to the correct build thus I didn’t open a separate ticket for this issue.  We flow 7 plus flights without any GPS errors.

### Michael Lindsay, 2026-06-29

@Alexander Alan Arnold @Eric Brewer The FW AP firmware has been updated in the XCOMM webpage to the correct build for adv nav (115).  Ted Trowbridge could not find anything in the SGCS-253 logs to provide an indication as to why the vehicle type switched (see comment below). The aircraft has flown serviceable.  If there is no further logs to help determine the root cause of this issue I  recommend that we close this ticket.

### Eric Brewer, 2026-07-06

@Michael Lindsay @Alexander Alan Arnold OK agreed.  We will track this issue and let you know if it pops up anywhere else.  To our knowledge these were the only two vehicles in the fleet to have this issue, and we have not been able to recreate it in the lab.

### Alexander Alan Arnold, 2026-08-12

@Eric Brewer Is this going to stay open for a while or is just a one off bug?

### Eric Brewer, 2026-08-12

@Alexander Alan Arnold we could not come up with any reproduction steps and did not get any additional information from this customer.  This is the only time this has happened across the fleet that we’re aware of, so I think we keep an eye out if it would pop up again, but I don’t know of any corrective actions.  The GCS correctly blocks uploading the wrong software so it feels like something was manually done with the gains, but obviously we can’t know for certain.

### Alexander Alan Arnold, 2026-08-12

unable to recreate. correct fimrware loaded aircraft flew without issue. original reported issue not seen again

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| XCOMM_VXE931.zip | archive | 8974 | 2026-06-16 | listed only |
| GCS-253 Files.zip | archive | 31264 | 2026-06-18 | listed only |
| T115_V931_260617_081856_pack.zip | archive | 1813 | 2026-06-18 | listed only |
| image-20260623-134950.png | image | 30 | 2026-06-23 | listed only |
