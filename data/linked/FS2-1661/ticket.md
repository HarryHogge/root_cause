# FS2-1661: XCOM board failures at LM Source inspection

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-04-02
- **Updated:** 2025-02-10
- **Resolved:** 2025-02-10
- **Reporter:** Scott Whitney
- **Assignee:** Jason Scherer
- **Creator:** Scott Whitney
- **Parent:** FS2-310 VXEP - SD Card file corruption (VXEP-236,237,414)
- **Links:** relates to VXEP-236 (Systemic SD card Investigation VXE-522 XCOM board failures at LM Source inspection); relates to VXEP-237 (VXE-529 XCOM board failures at LM Source inspection); relates to FS2-1754 (Implement fix to the VTOL AP - CA for corrupt SD card file); relates to VXEP-413 (CA: Firmware/GCS update to enable SDcard reformat in the field: Boot with corrupt card, Flag the degraded system and prevent flight, Inform the operator of the issue and Provide a mechanism for the operator to reformat the SD card)
- **Epic Link:** FS2-310

## Description

6/27/24 Kurt Burian
Quick update. Excerpts from my power point on share point below. This is a “in progress” document so data and conclusions may not be complete. 

FS2-1661 XCOMM SD Card.pptx

First the existing behavior of the xcomm vs planned future behavior:

[embedded: image-20240627-170834.png]
The primary fix is to boot to the web page rather then getting hung with a corrupt SD card, prevent launch, and alert the user. The remaining work is to boot in the same ‘safe’ manor ideally with also a corrupted flash, ideally allowing the XCOMM to change its tail number generated IP without a working flash chip. We want the vehicle to show up on the expected IP whenever possible to allow a user to gain access to the web page and reformat the appropriate drive via the utilities page. If the configuration cannot be read from both SD and Flash, the vehicle should boot to 10.0.0.200.

[embedded: image-20240627-171645.png]
Because flash needs to be working to save a sd config, we dont have a way of testing the combination of a valid sd config with a corrupt flash config. I’m writing a bit of code to set a flag in flash memory and disable access until cleared.

Corrupt SD Card Bugfix

[embedded: image-20240628-021324.png]


I believe I already have a method to disable launch, but its not yet documented.
The remaining work beyond wrapping up the drive level bug fix is to integrate with the GCS. This is not yet documented.
XCOM board failures at LM Source inspection
SW group
- Save existing firmware.
- Identify nature and C/CA of corruption if possible.
- Determine if reflash will correct this issue. Document process.
- Possibly allocate to a HIL for continued testing/monitoring.


Update 4/22/24
Created branch https://bitbucket.org/edgeautonomy/xcomm_202/branch/bugfix/FS2-1661_kurt_sd_card_lockup . Fixed simultaneous read issue in SD card driver code. Now can boot to web page with faulty SD Card. Added LED blinking during slow SD init to alert user device is still alive. Set bitfield in GCS reported xcommhealth and GCS+AP reported OPTIONS fault flag to prevent launch. Planning on PR release tonight.
GCS TODO
Suggest adding error flag for SD Card to:
[embedded: image-20240423-014121.png]
Shared Data Modifications
export.h
#define OPTIONS_SDERR 0x0200 // true if xcomm sd drive isnt working
#define XC_FAULT_SD 0x40000000 //xcomm sd card failure

## Sprint

FS2 Sprint 19, FS2 Sprint 20, FS2 Sprint 27, FS2 Sprint 21, FS2 Sprint 16, FS2 Sprint 28, FS2 Sprint 17, FS2 Sprint 29, FS2 Sprint 18, FS2 Sprint 24, FS2 Sprint 22, FS2 Sprint 23, FS2 Sprint 25, FS2 Sprint 26

## Comments (17)

### Scott Whitney, 2024-04-03

@Kurt Burian - look like there is another related issue https://jenaero.atlassian.net/browse/VXEP-237

### Kurt Burian, 2024-04-04

Added details to https://jenaero.atlassian.net/browse/VXEP-236. 
Flashed with 4.67 debugger. Code is stuck waiting for a SD Card read in its initialization routine. Removing the corrupted SD Card allows boot to succeed. To have this error fix itself, low level driver would need a rewrite to timeout and upper layer code would need to be modified to trigger a reformat, a significant amount of work.
Attempted SD Card reformat. No change in behavior after format. Tried reformatting disk using windows laptop. Drive was not recognized by Windows.
Placed 5-5306 back on Connors bench. 
Next Action: Needs new SD card along with production bootloader and firmware reinstalled. Suggest standard SEO checkout before returning to customer. 
[embedded: image-20240404-023330.png]

### David Grosher, 2024-04-08

@Kurt Burian @Scott Whitney FYSA
Notes from a discussion with Kurt. The application is being blocked during the initialization, the timeout in the screenshot is 10 seconds, but that may be long enough to prevent the initialization from completing in the allotted time.  We need to see if we are also blocked somewhere else. Regardless, if/when we timeout we need to set a fault bit to prevent flight but allow the system to continue to initialize.  Kurt is going to pass the error up the call chain for the timeout in the SPI driver above.  Once we are initialized with the fault identified then we have the opportunity to reformat the disk (this worked for some (most?) of the boards this was seen on). If this is doable on the XCOMM then: 
- We will need to port the fix to the VTOL AP.
- We need to send a message to the operator to explain what happened.
- We might need a workflow available on the GCS to reformat the SD card. This is currently available via the webpage.

Some Open Questions: 
- Can we put SDCards into a corrupted state to enable testing?
- Can we reformat corrupted disks via the webpage?

### Kurt Burian, 2024-04-09

New discovery. The SD Card SPI tx/rx driver timeout is too long. There is a 1ms task polling the SD Card which calls the “xchg_spi” function. If the timeout is longer then 800 counts(default 10000), the requests seem to stack up and lockup the processor. 
[embedded: image-20240409-070159.png]

### Kurt Burian, 2024-04-09

SD Card initializes at a low data rate. SPI tx/rx method is called hundreds of times during SD card init. Shorter timeout needed during this period or processor would  watchdog(disabling WDT made the lights stops blinking in the all on/all off ~1sec period). When data rate changes to 16Mhz, timeout changes to a 4 byte delay.
Using a unresponsive card, I was able to login to the XCOMM web page and run SD Card format and performance test utilities with messages open in parallel. Next will try with a functioning SD Card both inserted and removed.

[embedded: image-20240410-030636.png]

### Kurt Burian, 2024-04-11

Need a few more days on this. I tried performing a format with a known good SD Card and my changes cause it to fail. Working on a solution that functions normally and doesnt lock up with a bad card.

### Kurt Burian, 2024-04-22

Added xcomm sd card fault to vtol fault bitfield
#define XC_FAULT_SD 0x40000000 //xcomm sd card failure
Will need GCS to interpret and prompt user. Recommend error prompt on starting launch wizard. Need to find a way to prevent FW AP from launching next.

### Kurt Burian, 2024-04-23

@Michael Berger I’m looking to prevent the vehicle from progressing through launch wizard if the SD card is bad. I was wondering if I can hijack one of the XC_PWR_FAULT_* or VT_FAULT_* parameters set on the XCOMM to cause a error that would prevent launch? Id rather create a new fault parameter is the work load isnt too bad, but I assume that any changes to the launch wizard would be substantial. All fault parameters shown below:

[embedded: image-20240423-171940.png]

### David Grosher, 2024-07-03

@Douglas Baker This is the ticket in my group there is information all over here so it can be hard to extract out. But a few minute conversation with Kurt and myself and we can explain in more detail the solution being implemented. Simply put it is:
- Boot the processor with the corrupted SD card.
- Fail a health bit to prevent launch.
- Inform the operator
- Provide a mechanism for the operator to reformat the SD card (Also provide an operational supplement so they can follow a procedure). This step could also be automated in the future given more time and scope.

Any other potential corrective action requires a recall of birds to replace hardware, either the XCOMM board and VTOL board (most likely) and/or the SD cards on those boards.  
Note: All potential causes will result in the same corrupted SD card (voltage leakage (bit rot), or non-graceful power down during a write). The cause could also be some combination of the two. Counterfeit hardware could be a complicating factor that leads to the two other causes happening more frequently.

### Kurt Burian, 2024-07-08

https://bitbucket.org/edgeautonomy/xcomm_202/pull-requests/59

### Kurt Burian, 2024-07-08

Released a patch for the next release that will boot to webpage with a corrupted SD card. Currently this would result in a failed boot on the respective xcomm or vtol board. Will follow up with a second patch to solve the issue with a corrupted filesystem on a card that otherwise mounts correctly.

### Kurt Burian, 2024-07-10

I have a bugfix candidate to test tomorrow. 
- added a fdisk button that recreates a partition table
- modified sd driver init call to leave CS held low throughout the initialization process. This allowed cards to init that were otherwise failing.

### Kurt Burian, 2024-09-24

[embedded: SD Card Boot Failure.pptx]

### Scott Whitney, 2024-12-05

Reassigning to @Jason Scherer for review and reference

### David Grosher, 2025-02-05

@Scott Whitney @Jason Scherer I think this ticket is done with the current 6.4 delivery, correct? If not we should split that work from whatever we still want to do.

### Scott Whitney, 2025-02-05

@David Grosher  - all the planned tasks except for “currupt flash, SD” are complete. We have captured that work https://jenaero.atlassian.net/browse/FS2-2644 
@Jason Scherer please confirm that above is correct and close this task

### Jason Scherer, 2025-02-10

@Scott Whitney That is correct. Ticket closed.

## Attachments (9)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| f8321c51-4195-47f6-a3c0-f75c154b71f5#media-blob-url=true&id=dbd2a488-6a52-450b-9ac5-1211b017484b&collection=&contextId=19419&height=907&width=1077&alt=image-20240404-023330.png | image | 248 | 2024-04-08 | listed only |
| image-20240409-070159.png | image | 23 | 2024-04-09 | listed only |
| image-20240410-030636.png | image | 113 | 2024-04-09 | listed only |
| image-20240423-014121.png | image | 17 | 2024-04-22 | listed only |
| image-20240423-171940.png | image | 67 | 2024-04-23 | listed only |
| image-20240627-170834.png | image | 62 | 2024-06-27 | listed only |
| image-20240627-171645.png | image | 115 | 2024-06-27 | listed only |
| image-20240628-021324.png | image | 122 | 2024-06-27 | listed only |
| [SD Card Boot Failure.pptx](attachments/23362_SD%20Card%20Boot%20Failure.pptx.md) | pptx | 297 | 2024-09-24 | converted |
