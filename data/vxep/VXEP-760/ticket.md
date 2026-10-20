# VXEP-760: VXE 485 Crash on VTOL landing

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2024-10-31
- **Updated:** 2026-08-14
- **Resolved:** 2025-02-28
- **Reporter:** Pat Wells
- **Assignee:** Pat Wells
- **Creator:** Pat Wells
- **Labels:** MARSOC, Software, Weekly-incident-tracker
- **Links:** relates to RMA-386 (VXE-485 241107-1); relates to VXEP-565 (Send out customer notification of the guidance to ensure pause/nudge duration is an emergency procedure only and is limited ); relates to VXEP-791 (VXE 409 turned away from wind during recovery then crashed)
- **Customer:** MARSOC
- **Vehicle Tail Number:** 485
- **Corrective Action:** https://jenaero.atlassian.net/browse/VXEP-565
- **Plan:** - @Jason Scherer working on pulling VTOL logs 1/14/2025 -Not Possible. Logs corrupted.
- **Root Cause:** There is not enough information to properly conclude a root cause
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

From MARSOC Kona
Did not receive a witness statement from operator.  Did receive a video which shows everything that happened.  Attached. 

AAR attached.  I’m aware that it’s missing data, I’ve reached out to customer to work on getting the remaining data from the aircraft.

## Issue Status

VTOL AP Log Files are corrupted but XCOMM files were attained. [embedded file] 

@Eric Brewer @David Grosher

## Comments (29)

### Cameron Chapman, 2024-11-08

@Eric Brewer I do not know what triggers the log rate to slow down, the cause or effect of these faults. FW group would know best. 
Random guess (maybe the logs slow down when the operator enables pause/nudge).

### Eric Brewer, 2024-11-08

@Scott Hunter , @David Grosher mentioned you might have seen this low logging rate issue before, does this incident match the signature you saw previously? FYI @Cameron Chapman 
@David Grosher let me know who might best be able to assist with understanding the cause/effect of the vaux fault.

### Sean Odell, 2024-11-19

@David Grosher @Cameron Chapman @Pat Wells @Rodney Linch Aircraft delivered to Engineering pending evaluation. Photos and intake documentation is stored in the RMA ticket.

### Adrian Garcia, 2024-11-21

@Cameron Chapman @David Grosher @Eric Brewer VTOL AP data logs are corrupted but I was able to get the XCOMM Files.

### Jason Scherer, 2024-12-03

@Adrian Garcia I’ve been able to manually decrypt data from some SD cards now. I’d like to take the SD Card out of CW485 and attempt to recover the logs manually. I’ve notice it’s not opened up yet. Let me know if it’s a good time to open the CW and remove the SD card.

### Adrian Garcia, 2024-12-04

@Jason Scherer the wing case is near my workbench whenever you need it.

### Rodney Linch, 2024-12-11

@Jackson Riley Curvin - wing and fuse cases are still with engineering.

### Rodney Linch, 2024-12-11

@Emalee Johnson - RMA will require material dispostion.

### Pat Wells, 2024-12-18

@Rodney Linch what disposition are you asking for?  The investigation is still ongoing.

### Rodney Linch, 2024-12-18

@Pat Wells  Material disposition for all material contents returned to validate whether or not any / some / none parts are salvageable.  And parts being salvaged would possibly lower our cost, or that of the customer.

### Eric Brewer, 2024-12-20

@Jason Scherer @Adrian Garcia were we able to extract VTOL logs from this flight?

### Alexander Alan Arnold, 2025-01-10

@Eric Brewer Any updates on this?

### Eric Brewer, 2025-01-10

@Alexander Alan Arnold unfortunately without VTOL logs I don’t know that there is much more we can determine for this flight.
@Jason Scherer @Adrian Garcia @David Grosher FYI.

### Pat Wells, 2025-01-14

@Jason Scherer @Eric Brewer @David Grosher did we ever have success retreiving or decrypting the VTOL logs?

### Jason Scherer, 2025-01-21

After pulling the image and decrypting the data, the image is not mountable. This means that there is some level of data corruption in the SD card image. It is unlikely that we will be able to get any logs from this image, but I am going to do a little more analysis to see if it’s something recoverable.

### Pat Wells, 2025-01-27

@Jason Scherer checking in for any updates.

### David Grosher, 2025-01-28

@Pat Wells We weren’t able to recover data from this aircraft. At this point we won’t be able to provide any additional information on the root cause.

### Jason Scherer, 2025-02-12

I was unable to get any further logs on this vehicle.

### Pat Wells, 2025-02-27

@David Grosher  does this need to go to the Bermuda triangle?

### David Grosher, 2025-02-27

@Pat Wells Yes, we unfortunately can’t resolve the investigation. The data rate on the XCOMM was unexpectedly low and there was no recoverable VTOL data.

### Alexander Alan Arnold, 2025-01-10

@Eric Brewer Any updates on this?

### Eric Brewer, 2025-01-10

@Alexander Alan Arnold unfortunately without VTOL logs I don’t know that there is much more we can determine for this flight.
@Jason Scherer @Adrian Garcia @David Grosher FYI.

### Pat Wells, 2025-01-14

@Jason Scherer @Eric Brewer @David Grosher did we ever have success retreiving or decrypting the VTOL logs?

### Jason Scherer, 2025-01-21

After pulling the image and decrypting the data, the image is not mountable. This means that there is some level of data corruption in the SD card image. It is unlikely that we will be able to get any logs from this image, but I am going to do a little more analysis to see if it’s something recoverable.

### Pat Wells, 2025-01-27

@Jason Scherer checking in for any updates.

### David Grosher, 2025-01-28

@Pat Wells We weren’t able to recover data from this aircraft. At this point we won’t be able to provide any additional information on the root cause.

### Jason Scherer, 2025-02-12

I was unable to get any further logs on this vehicle.

### Pat Wells, 2025-02-27

@David Grosher  does this need to go to the Bermuda triangle?

### David Grosher, 2025-02-27

@Pat Wells Yes, we unfortunately can’t resolve the investigation. The data rate on the XCOMM was unexpectedly low and there was no recoverable VTOL data.

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IMG_7006.MOV | video | 8893 | 2024-10-31 | listed only |
| T95_V485_241029_142416_01_pack.zip | archive | 247 | 2024-10-31 | listed only |
| Update 485.zip | archive | 22890 | 2024-11-06 | listed only |
| image-20241107-193321.png | image | 23 | 2024-11-07 | listed only |
| image-20241107-193445.png | image | 9 | 2024-11-07 | listed only |
| V485 XCOMM Logs.zip | archive | 6463 | 2024-11-21 | listed only |
