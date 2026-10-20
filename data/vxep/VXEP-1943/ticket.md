# VXEP-1943: VXE-1022 auto aborted VTOL launch at the pause. No XCOMM logs in the AAR.

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** Highest
- **Created:** 2026-06-25
- **Updated:** 2026-10-07
- **Reporter:** Zachary Mann
- **Assignee:** David Grosher
- **Creator:** Michael Mohr
- **Labels:** Hardware, LRR, RCCA, Weekly-incident-tracker
- **Links:** relates to FS2-4887 (VXE-1040 XCOMM SD Card Corrupted); relates to RMA-1072 (VXE-1022 AVIONICS BOX RMA 260730-1)
- **Customer:** Redwire
- **Vehicle Tail Number:** VXE-1022
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround
- **Program (Marquee):** LRR
- **Executive Summary:** Sending Avionics to SLO for investigation. Probable cause Hardware.

## Description

LRR internal asset
VXE-1022 aborted at the pause during launch. Believed to be a GNSS drop. After downloading the AAR from the flight, it was discovered that the XCOMM logs were missing from the AAR. Conducted an FTP and attached the files below.
Also, operator had no indication (popup) on why the aircraft aborted on OGCS.

## Vehicle Configuration

Block 35
Standard Main Battery
140ZG2

## Plan

Field Check - confirm SD Card is not corrupted
- connect to Jennings GCS and see if you are prompted to reformat SD Card
- Going to XCOMM webpage and confirming the SD1 card is mounted or if you are in ROM mode

[embedded: image-20260630-172430.png]

## Comments (11)

### Alexander Alan Arnold, 2026-06-25

@David Grosher @Cody Smisek XCOMM logs have been added that were not captured in the AAR from this morning 
@Eric Brewer

### Alexander Alan Arnold, 2026-07-02

@Scott Whitney AAR uploaded. We had to run the python script probably 20 times and power cycle the aircraft 3 times to get into the XCOMM page.
I connected in OGCS with no issues upon power up then disconnected from AP and swapped to SUAV and connected with no issue
we had the script on engineering/admin laptop, and we could not connect after the script displayed success in command prompt after ten attempts we power cycled the aircraft and swapped to an internal LRR gcs and tired again after about 8 trys with script displaying success we power cycled again and used the same gcs and then it worked. 
we had no problems connecting to the other available webpages.

### Alexander Alan Arnold, 2026-07-07

@Scott Whitney Was anything discovered after the testing and AAR we uploaded? What else can we do to troubleshoot this issue?

### Scott Whitney, 2026-07-09

@Alexander Alan Arnold  - the xcomm logs only part of the flight on jun 26. There is no evidence in the AAR from July 2 of a Launch abort. 

Can you provide a timeline of events? Was the SD card ever reformatted? 

XCOMM Logs:
```
2026/06/26
Line 2618: Launch Complete

Line 4657: [18:10:37.926 3877.926] GoTo m,w 5  0 (go to waypoing)

Line 4763: XCOMM Logging ends (no data around landing)



No more XCOMM data until 2026/07/02
```
[embedded: image-20260708-231643.png]

VTOL Logs:
- Capture entire flight on 2026-06-26

- no data from a launch abort

[embedded: image-20260708-231707.png]

### Alexander Alan Arnold, 2026-07-09

Operator states no issue during launch wizard, at 20ft check aircraft aborted launch. the date of the abort was 2026-06-25

we did the testing recommended in the team's chat Addison, Anthony, +2

testing write up is in my comment from july 2, the SD card was not reformatted as when connecting in SUAV there was no indication it needed to be in the SD card format section. It also displayed SD1:/www/ in the xcomm webpage @Scott Whitney @Addison Osborn

### Matt Philley, 2026-07-09

This AC is still under investigation, but is also part of the JST Crimp Process Containment https://jenaero.atlassian.net/browse/XKIT-5525 
Per Scott W the work on the Containment should not interfere with this investigation.
Not sure when that will take place, but wanted to link in case that becomes relevant.

### Scott Whitney, 2026-07-15

@Alexander Alan Arnold  -  at this time it is unclear why the data stopped on the xcomm. is it possible to set up the avionics to run a endurance of the avionics? 
Avionics Endurance Test — Attempt to Reproduce Data Dropout
- Choose a test setup:
- Preferred: Run avionics installed in the fuselage
- Alternative: Run avionics standalone (if vehicle is in JST Containment)
- Provide full 28V power to the avionics
- Position a desk fan on the avionics to prevent overheating
- Let the system run continuously for 24 hours
- Pull the logs after the 24-hour period

Goal: Determine if the data dropout can be reproduced under sustained operation. 
If there isn’t time to do a proper investigation, I would recommend replacing the XCOMM. 
 
@David Grosher is back tomorrow, he may have additional test recommendations

### Alexander Alan Arnold, 2026-07-17

@Scott Whitney @David Grosher could we run two separate 10-12 hour test so we do not have to leave the aircraft unattended? we are still working to source a BLK 35-power adapter so it would be battery only.

### Scott Whitney, 2026-07-17

@Alexander Alan Arnold - yes, if it is on battery, you shouldn’t leave it running overnight unattended.

### Jackson Riley Curvin, 2026-07-22

@Scott Whitney @David Grosher  the AARs are uploaded from the endurance test

### Scott Whitney, 2026-07-24

@Jackson Riley Curvin  - there is likely an issue with the XCOMM or XCOMM SD. That avionics should be RMA’d to replace XCOMM and checked out by the eshop.

## Attachments (11)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V1022_B35_20260625T152636Z.zip | archive | 77911 | 2026-06-25 | listed only |
| VTOL_VXE1022.zip | archive | 41198 | 2026-06-25 | listed only |
| XCOMM_VXE1022.zip | archive | 16416 | 2026-06-25 | listed only |
| frontend-native-0039-2026-06-25.bin | other | 3162 | 2026-06-25 | listed only |
| [frontend-native-0039-2026-06-25.jsonl](attachments/63136_frontend-native-0039-2026-06-25.jsonl.md) | text | 2 | 2026-06-25 | converted |
| image-20260630-172430.png | image | 583 | 2026-06-30 | listed only |
| AAR_V1022_B35_20260702T203104Z.zip | archive | 44750 | 2026-07-02 | listed only |
| image-20260708-231643.png | image | 172 | 2026-07-09 | listed only |
| image-20260708-231707.png | image | 177 | 2026-07-09 | listed only |
| AAR_V1022_B35_20260720T215235Z (1).zip | archive | 80577 | 2026-07-22 | listed only |
| AAR_V1022_B35_20260721T221118Z.zip | archive | 161926 | 2026-07-22 | listed only |
