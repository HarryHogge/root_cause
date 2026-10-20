# RMA-286: VXE-623 TIQ MOD 240703-1

- **Issue type:** Aircraft
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-07-02
- **Updated:** 2025-01-16
- **Resolved:** 2025-01-16
- **Reporter:** Sean Odell
- **Assignee:** Sean Odell
- **Creator:** Sean Odell
- **Labels:** Industrial_SD-Card_Installed, SD_Card
- **Links:** relates to VXEP-236 (Systemic SD card Investigation VXE-522 XCOM board failures at LM Source inspection); relates to VXEP-237 (VXE-529 XCOM board failures at LM Source inspection)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 623

## Description

LM had to downgrade the software on this aircraft per LM UK request.  Then upon getting the ok to install the latest software 6.2.9 the aircraft is refusing to take the update.  

SOW: Evaluate and install the latest software including a SCO checkout.

## Corrective Action

7/3/24 Kurt Burian
Recommended next steps are to open the avionics box and replace the SD card. I don’t know why the card failed, but it seems to be unrecoverable in its current condition. Airplane was still booting to the webpage and thought it had a working SD Card, usually a corrupt card would prevent successful boot. It could be something as simple as a pin making intermittent contact, ejecting/inserting a few times once we have the box open would let us test that. Desktop tools might allow better analysis of the cards filesystem should we want to dive further.
XCOMM needs a firmware flash once we replace the SD. I loaded a test build and forgot to roll back to the production release before returning the vehicle to the case.

## Comments (24)

### Pat Wells, 2024-07-02

@Sean Odell note this sounds very similar to the issue I was working the Textron on the LAV program last week.

### Sean Odell, 2024-07-03

Status update on initial Evaluation:
Fuselage Avionics box XCOMM SD-card showed large amount of corruption. See the attached files showing corruption. 
Attempted to Format the SD-card per standard practices and after only a couple seconds, it showed format complete, but still corruption remained. Showing signs of a hardware failure.  NOTE: Full SD-card format is between 30-60 seconds, not 5 seconds as experiences with this aircraft.
Next steps are to remove the avionics box and continue the evaluation by opening up the Avionics box.
@Pat Wells FYSA

### Sean Odell, 2024-07-03

@Steve Stack As Discussed earlier

### Sean Odell, 2024-07-03

@David Grosher@Sam Miller @Greg Fryer @Pat Wells New RMA arrived yesterday from TIQ MOD that the customer downgraded the software to the approved FAT configuration from October of last year.  Then while attempting to upgrade the aircraft to 6.2.9, it failed. They attempted to troubleshoot using LM FSR’s but was unsuccessful.   Carson and I saw the file names on the SD Card showing corruption, screen shot them, and added them to this ticket. 

Carson and I attempted to format the SD Card using the XCOMM page but the process failed both times.  The aircraft is in the RMA area in case you would like to examine the aircraft.  Then I will have the team replace the SD-card, SCO, test flight and given back to LM.

### Sean Odell, 2024-07-03

Note: Center wing did have the latest software at of 7-3-2024

### David Grosher, 2024-07-03

@Douglas Baker Should we be upgrading software, if the customer has not approved that software version?
@Kurt Burian Can you take a look at the corrupted SDcards?

### Sean Odell, 2024-07-03

@David Grosher To clarify, Edge was not upgrading the software, the customer (LM) was upgrading the software. When LM experienced failed attempts, they gave to Edge to evaluate and repair.

### Kurt Burian, 2024-07-03

@David Grosher @Sean Odell As soon as I finish my current task I will attempt a bootloader firmware program to v6.2.9. Hopefully I can then use the webpage to reformat the sd card. Will let you know when this is completed and the results.

### Kurt Burian, 2024-07-03

Attempted reformat via web page multiple times. Reported success, but could not browse or upload hex via web page after multiple attempts. Flashed 4.67->4.68 via APBL. No change in behavior. Logs show attempts to create files, but always result in failure.

```
[23:29:27.265 4.265] sd free space target (GB*0.1) 100
[23:29:38.215 15.217] level 1 login allowed 10.0.0.2
[23:29:39.931 16.931] initial sd free space (GB*0.1) 593
[23:29:39.946 16.947] creating burn file list sd1:/datalog/burnlist.txt
[23:29:40.003 17.003] open file fail sd1:/datalog/xcl00000.csv
[23:29:40.008 17.008] Next log file: sd1:/datalog/xcl00000.csv
[23:29:40.009 17.009] filestream open 1
[23:29:40.047 17.048] open file fail sd1:/datalog/burnlist.txt
[23:29:40.049 17.049] Filestream opened, starting datalogger task
[23:29:40.071 17.071] event FLT_EVENT_ON
[23:29:40.093 17.093] save fdr: sd1:/datalog/fdrrecov.csv
[23:29:40.114 17.114] add flight file sd1:/datalog/fdrrecov.csv
[23:29:40.148 17.148] open file fail sd1:/datalog/fltfiles.txt
[23:29:40.171 17.171] DebugMsg SLA reset start
[23:29:40.172 17.172] sla discovery start
[23:29:40.175 17.175] fc rate 115200
[23:29:40.275 17.275] fc tx:  
```

### Kurt Burian, 2024-07-03

Tried formatting flash in addition to SD card, no change. Seems like the file table is corrupted in a way that cant be fixed by reformatting, likely something physical with the SD Card. Brandon has seem similar behavior in the past on the HIL, their fix was to replace the SD Card.
Occasionally we get a garbage “Log Files” page, usually has been loading a blank page. “Drive Status->SD” always shows a empty page rather then the sd card file system:

[embedded: image-20240703-234723.png]

[embedded: image-20240703-235111.png]

[embedded: image-20240703-235139.png]

[embedded: image-20240703-235003.png]

### Sean Odell, 2024-07-11

@Kurt Burian Has taken the aircrafts fuselage case to continue the investigation in Engineering.
@Pat Wells FYSA

### Sean Odell, 2024-07-26

FYSA@Pat Wells- @Kurt Burian  has requested another week with this aircraft to complete investigation. Once I am back from PTO, I will work on quote and completing this RMA.

### Sean Odell, 2024-08-23

@Kurt Burian Please add a comment to this ticket of what you would like me to do to this aircraft now that your evaluation is complete.  Example: replace SD-card, SCO and Test fly 1 time.  Thank you in advance.

### Kurt Burian, 2024-08-23

Hey sorry, I think my email 8/6/24 must have gotten lost in the either. Same procedure with this asset.
At the moment I’m out of ideas. I think I’ve held onto your assets long enough to glean any useful information. I think we can move forward and process the RMAs for:
- V632 Fuse:         Partition fix reports success, but drive remains corrupted on subsequent reboot. Unique failure mode, not observer on other vehicles.

The recommended course of action is to replace the SD Card, reprogram with the correct firmware, and reload the original gains/config in case the calibrations have been corrupted through my tampering. I’m hoping we can retain the bad SD cards for further analysis.
I assume the vehicle will get the standard SCO checkout.

### Sean Odell, 2024-08-26

Equipment back in RMA Area and now working on getting the quote, travelers, and people lined up to perform the work. I also will need to get the avionics box removed and prepared for electronics to rework.
@Pat Wells FYI

### Sean Odell, 2024-08-30

Engineering Eval complete and needs a Quote generated for a new SD-card. ETA 9-5

### Sean Odell, 2024-09-09

Quote completed and submitted to finance for SO/Job creation on 9-9-24

### Sean Odell, 2024-09-19

In electronics getting SD-card replaced in the Avionics Box.

### Pat Wells, 2024-11-13

@Sean Odell @Jackson Riley Curvin Last update 19 September.  What is current status?

### Sean Odell, 2024-11-13

@Pat Wells This was awaiting source inspection when the SD-Card issue came up. It is now in the queue for SD-Card replacement as well as getting the wing case from LM.@Jackson Riley Curvin

### Jackson Riley Curvin, 2025-01-02

@Rodney Linch Production Orders list says this is complete is this accurate?

### Jackson Riley Curvin, 2025-01-10

@Rodney Linch we need to see if this aircraft got the Payload Modification it appears to already have the industrial cards installed if the Mod is done then we can close this one out. @Pat Wells FYSA

### Pat Wells, 2025-01-10

@Rodney Linch additionally this fuselage may have been the latest production version that does not require payload bay mods.  Need to run all this down and get this back to LM/ TIQ as we’ve had it since July 24

@Jackson Riley Curvin  FYSA

### Rodney Linch, 2025-01-16

Sent to finished goods on 1-16-2025

## Attachments (28)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 623 SD Corruption.png | image | 159 | 2024-07-03 | listed only |
| SD Corruption Messages.png | image | 179 | 2024-07-03 | listed only |
| image-20240703-234723.png | image | 45 | 2024-07-03 | listed only |
| image-20240703-235003.png | image | 36 | 2024-07-03 | listed only |
| image-20240703-235111.png | image | 29 | 2024-07-03 | listed only |
| image-20240703-235139.png | image | 13 | 2024-07-03 | listed only |
| [RMA Repair Quote for AC 623 SD Card Warranty LM UK MOD 9-9-2024.pdf](attachments/23027_RMA%20Repair%20Quote%20for%20AC%20623%20SD%20Card%20Warranty%20LM%20UK%20MOD%209-9-2024.pdf.md) | pdf | 183 | 2024-09-09 | converted |
| [01032025.pdf](attachments/25279_01032025.pdf.md) | pdf | 2274 | 2025-01-03 | converted |
| 20250103_190621000_iOS.jpg | image | 2537 | 2025-01-03 | listed only |
| 20250103_190634000_iOS.jpg | image | 1780 | 2025-01-03 | listed only |
| 20250103_190703000_iOS.jpg | image | 2083 | 2025-01-03 | listed only |
| 20250103_190730000_iOS.jpg | image | 1710 | 2025-01-03 | listed only |
| 20250103_190755000_iOS.jpg | image | 1764 | 2025-01-03 | listed only |
| 20250103_190839000_iOS.jpg | image | 2230 | 2025-01-03 | listed only |
| 20250103_190847000_iOS.jpg | image | 1968 | 2025-01-03 | listed only |
| 20250103_190939000_iOS.jpg | image | 1954 | 2025-01-03 | listed only |
| 20250103_191022000_iOS.jpg | image | 2523 | 2025-01-03 | listed only |
| 20250103_191127000_iOS.jpg | image | 3529 | 2025-01-03 | listed only |
| 20250103_192108000_iOS.jpg | image | 2780 | 2025-01-03 | listed only |
| 20250103_192121000_iOS.jpg | image | 2110 | 2025-01-03 | listed only |
| 20250103_192438000_iOS.jpg | image | 1670 | 2025-01-03 | listed only |
| 20250103_192447000_iOS.jpg | image | 2013 | 2025-01-03 | listed only |
| 20250103_192539000_iOS.jpg | image | 1937 | 2025-01-03 | listed only |
| 20250103_192623000_iOS.jpg | image | 1652 | 2025-01-03 | listed only |
| 20250103_194647000_iOS.jpg | image | 3466 | 2025-01-03 | listed only |
| 20250103_194705000_iOS.jpg | image | 2111 | 2025-01-03 | listed only |
| 20250103_194716000_iOS.jpg | image | 2401 | 2025-01-03 | listed only |
| 20250103_205357000_iOS.jpg | image | 2201 | 2025-01-03 | listed only |
