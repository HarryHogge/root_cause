# ENG-2992: VXE 444 Crash in Landing Pattern

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-03-31
- **Updated:** 2025-06-02
- **Resolved:** 2023-12-21
- **Reporter:** Sam Miller
- **Assignee:** Connor Peebles
- **Creator:** Sam Miller
- **Labels:** 8-28-Sprint, FixedWingAP
- **Links:** blocks VA-184 (Tail#444 AP SN 10211 (will just link to VIT jira)); relates to VXEP-484 (0002P01G Green Autopilot Reliability Issues/Fallout Study); relates to RMA-112 (VXE-444 Avionics BOX 230404); relates to RMA-113 (VXE-444 Aircraft Rebuild 230404); relates to ENG-3054 (VXE 455 Uncommanded departure from orbit and crash into Potomac); relates to ENG-3060 (VXE 465 Cannot Connect to GCS); relates to VA-268 (VXE 444 Hands on troubleshooting. Identify cause and corrective actions.); relates to VXEP-46 (VXE-444 Crash in Landing Pattern-XCOM PCB issue); relates to VXEP-732 (VXE 628 Crash on VTOL descent)

## Description

running incident summary we will keep adding to, besides adding comments here 
\Root Cause Task Force\Flight Data Reviews\VIT2-252; VXE 444 Crash in Landing Pattern
VIT2-252_ VXE444 Crash In Landing Pattern, Investigation Details.docx
VXE444 crashed while transitioning from IP2 to IP4 in the landing pattern.  Today for a test flight after installing 6.0.12 and performing all applicable SBs, AC444 went up for approx 25 minutes before we returned to land. We used a straight in approach based on terrain and other constraints. We departed a nearby orbit at 400 ft agl to enter our 400 ft land primary land plan. To avoid the IP2 orbit  based on a nearby radio tower, we commanded straight to IP4.
 
The gcs software still highlighted the IP2 orbit and started a left turn in which it lost altitude, quickly followed by a steep climb resulting in a possible stall and rolling off to the right into a steep dive that it didn't recover from. With so little altitude to work with, there wasn't time to complete command to Orbit 2 to see if a correction could be made. Aircraft is a near complete loss.
Preliminary analysis of the XCOMM data XCL00041.xlsx indicates a loss of fixed wing autopilot power at XCOMM CPU time of 5740.169 (line 1022).  VTOL Controller also appears to have stopped recording mid-flight.

## Comments (36)

### Sam Miller, 2023-03-31

I sifted through the zip files and saved off stuff related to this flight as xlsx files.  The VTOL controller file for this flight appears to be VTL00028.  The XCOMM file is XCL00041.  Also, highlighted trouble sections.

[embedded: XC230331 (3dcaaf2d-84af-4939-bd2b-51b6f00733bc).txt][embedded: VT230330.txt][embedded: FDR00041.csv][embedded: VTL00029.xlsx][embedded: XCL00041.xlsx]

### Sam Miller, 2023-03-31

Curtis says that the SA cam had a picture until about 50ft to impact the ground, so the main battery and nose cone power was still connected until impact.  It looks like the XCOMM recorded the whole time.

### Kurt Burian, 2023-03-31

5740 is when the logging rate switches to high speed so keep that in mind as your looking at counts/time.
Serial comms to the fixed wing up is working up until the XCOMM log stops, but the data is ‘stale’ as old values are repeated which I can’t explain and this only happens with certain fields. apgpsVs is fine so is apAgl and I believe they are both computed on the fixed wing. Fixed wing IMU seems to be working.
The servo supplies go down to a volt each at this time. I don’t know if it’s because they are trying really hard or if the power is down.

I want to look for a fixed wing processor reset, watchdog or brownout from the servo supply issue. Will a AP reset cause the XCOMM servo supplies to toggle? My guess in no.

### Dustin Gamble, 2023-03-31

I think we are missing xcomm event log. I asked Curtis to do a full ftp download to make sure we get everything.
xcomm log also shows linkApRx drops to zero right before the loss.

### Sam Miller, 2023-03-31

I’m not seeing that in XCL00041.  The high speed 10Hz logging had started way earlier in the file.  
I’m pretty sure if you reset the fw autopilot, the servo power momentarily goes out.

### John Clark, 2023-03-31

From my analysis, and both Kurt and I are in complete agreement, the XComm log XCL00041.xls clearly shows the commanded altitude changing from 400' to 458'. Within 10 seconds or so the FDR for the FW AP shows one row at end of the transition 400' to 458' then the FW AP appears to reboot. This is seen at end of FDR00041.xls. The XComm data then reflects the reboot with lost data from the FW AP. Loss of control occurs shortly after. Looking now for some cause of the reboot.

### Kurt Burian, 2023-03-31

Fixed AP restart WILL cause the XCOMM servo supplies to cycle as observed in the log. I dont think anything was wrong with the servo supplies after all. Fixed wing AP reset still the best bet.

### Greg Fryer, 2023-03-31

@Cameron Chapman Reports that investigation into the NCR on 444 replaced the boom electronics and CW harness. Since the electronics are powered from the main battery, not HLB, the reverse-plug/polarity at the boom wouldn’t have impacted the APs.

### Cameron Chapman, 2023-03-31

Correction to Gregs comment. 
429 had the ESCs replaced with a reverse polarity occurence. https://jenaero.atlassian.net/browse/RMA-77 
No one ever asked about 444, or filled in the corrective action in the NCR. NCR-211227 - 106
https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/NCR%20List/DispForm.aspx?ID=106&commentId=2&e=vrdUA9o2UUK5TtbzWDiqlQ&at=15 
Either way, a reverse polarity on the boom should not affect power in the avionics box. It would likely only affect boom electronics.

### Dustin Gamble, 2023-03-31

We received the full ftp downloads of xcomm and VTOL
[embedded: AC444 .10 (fb799e50-20a7-4414-8ae0-ec00ff4c78c9).zip][embedded: AC444 .2 (2d11277e-7cad-4bed-bb09-c7d91deb88d3).zip]

### Dustin Gamble, 2023-03-31

[embedded: XCEVLOG.TXT]
This looks like the file we want and the section we are looking for:
[02:58:21.206 5310.206] GoTo m,w 4  0
[03:02:46.269 5575.270] GoTo m,w 1  1
[03:05:24.622 5733.622] ap link fault: local rx bad ap rx okay
[03:05:24.624 5733.624] ap link fault during transition/fw flight
[03:05:30.662 5739.662] ap dbg: mpu-9250 acc/gyro id (113): 113
[03:05:30.672 5739.672] ap link restored
[03:05:30.695 5739.695] ap dbg: mpu-9250 mag id (72): 72
[03:05:30.704 5739.704] ap dbg: facmag[0]: 49
[03:05:30.705 5739.705] ap dbg: facmag[1]: 50
[03:05:30.706 5739.707] ap dbg: facmag[2]: 39
[03:05:30.820 5739.820] ap dbg: GPS=NEO-M8N
[03:05:30.937 5739.937] landing detected

Note:
XC211228.TXT shows a WD BOOT 128 but that look like an old file.

### Lawton Ziedses Des Plantes, 2023-04-03

The 5V rail on the AP was only measuring 2.5V, is that confirmed?  I would also check the ribbon cable and X-com depending on where the 2.5V was measured in the circuit, could be a power supply on X-COM board as well--its weird that the Vtol Ap stopped recording halfway--two simultaneous failures of AP’s seems like a power distribution problem

### Sam Miller, 2023-04-03

There was no issue with the XCOMM board.  The 12.8V was measured at the autopilot input connector J21 on pins 30 and 32-36.  The 5V rail was measured at 2.08V between J24 Pin 10 and J21 Pin 30 (since Pin 1 was inaccessible on J24 due to the SLS mount).  This is either a power supply failure on the autopilot board or some other component pulling a bunch of current on that supply.  We have requested that the user send the avionics box back to us if possible.

### Matt Philley, 2023-04-04

Added a relation to https://jenaero.atlassian.net/browse/ENG-1086 since I didnt see one present, but there is some overlap in the investigation.

### Cameron Chapman, 2023-04-04

Thanks @Matt Philley . We’ve also been adding the FixedWingAP label to help filter related or potentially related issues. See right. I just added to this one. 
[embedded: image-20230404-210633.png]

### Kurt Burian, 2023-04-04

No WD in the XCOMM log, but we get ap link restored. Power cycle or other CPU hardware failure would avoid the WD crash message. The landed is what triggers on the xcomm when the ap comes back “not flying” after it reset.

### Matt Philley, 2023-04-12

@Sam Miller @Former user I dont think any action for this is still open with Ryan F is it? Please let me know if yall still need his support. For now I will assign it back to John T.

### Kurt Burian, 2023-04-17

Results of burn in/rerun v378. No watchdog crash in log. 
[embedded: T95_V378_230417_071537_pack.zip]

### Sean Odell, 2023-04-25

@Former user The Avionics box is now here at Edge. Who should I deliver it to to start the Evaluation?
@Greg Fryer FYI

### Sean Odell, 2023-04-25

Avionics box delivered to @Connor Peebles to start the evaluation.

### Connor Peebles, 2023-04-26

Initial findings:
[embedded: IMG_E4423.JPG]
Yesterday just confirmed Sam’s finding that it is isolated to the AP. The Xcomm board is attempting to send 12.8V to the AP as it should, but the AP isn’t seeing it.
This pic looking at the AP, no glaring defects.

No crack seen on the processor yet, but still have to pull it out to get a better angle
[embedded: IMG_0345.jpg]
LED D8 is broken. Weird failure mode if so, doubtful it was from the force of the impact
[embedded: IMG_0346.jpg]
The trace on that LED looks charred (the right half of it)

### Connor Peebles, 2023-04-26

[embedded: bevelwcc3.pdf][embedded: bevelwcc2.pdf][embedded: bevelwcc1.pdf]
Here are ~14.5X magnification zoom onto the suspect area of the chip
The arrowed and circle areas may be cracks but that would make them quite small. The lines may just be FOD trapped in the conformal coat.
Tomorrow will clean off some of the conformal coat to get a better look

### Connor Peebles, 2023-04-27

@Sam Miller Is it possible to get the full zipped FDR? It would help for automated review.

### Connor Peebles, 2023-04-27

[embedded: IMG_0354.jpg]
[embedded: IMG_0356.jpg]
[embedded: IMG_0357.jpg]
No significant cracks/holes found on processor area that usually has them (referring to main theory in [ENG-1086] 0002P01G Green Autopilot Reliability Issues/Fallout Study - Jira (atlassian.net))

Note that cracks on the processor are just a suspected symptom of a failing processor. Lack of cracks does not omit possibility of failed processor.

### Cameron Chapman, 2023-05-01

@Maxime Jeanneau or @Hayden Jeanor , can you please help with the following? 
- Create a word doc here titled with this “incident number and title - Investigation Details”. Save link to the description here.
- By reviewing this comment thread, summarize what is known from previous data review, troubleshooting, etc. Include graphs, pictures, etc as useful.
- Recommend next investigation steps.
- Review with me.
- Update fields above accordingly then proceed with investigation.


If this process works well, we may standardize. It is hard to sort important findings for long investigations just by reading through comments. 
See https://jenaero.atlassian.net/wiki/spaces/EF/pages/23363854/VIT2+Project-Incident+Troubleshooting+and+Resolution+Tracking.

### Connor Peebles, 2023-05-01

@Cameron Chapman Here is the running incident summary we will keep adding to, besides adding comments here 

\Root Cause Task Force\Flight Data Reviews\VIT2-252; VXE 444 Crash in Landing Pattern
VIT2-252_ VXE444 Crash In Landing Pattern, Investigation Details.docx

### Connor Peebles, 2023-05-02

As I am continuing my data crawl and putting it into that docx there, I noticed a crazy anomaly on SupIret, which is the analog supervisor for the payload retract current. Looks like it had a short.
[embedded: image-20230502-235959.png]
For now we will keep filling out that docx but I think this is a promising lead

### Connor Peebles, 2023-05-10

[embedded: FLIR0113.jpg]
Here is how 444’s AP looks when connected to a functional powered XCOMM. The only heat source we see is from around C18 which is where the 5V rail comes from and is only showing 0.2V. The heat on the MagAcc board is a reflection off the can shielding.

To narrow down between U14/15 and U17, I injected current controlled 5V into the 5V and GND test points. The processor turned on and heated up as it should, which until now had not happened.
[embedded: FLIR0116.jpg]

Connecting it to an XCOMM allows communication to 444’s Green AP.
[embedded: FLIR0118.jpg]
[embedded: Connected.JPG]

### Connor Peebles, 2023-05-10

From the previous comment, we see the processor isn’t destroyed, but doesn’t necessarily mean the failure wasn’t because the processor.
Some theories to look into:
- Overcurrent or overvoltage caused U14 (step-down switching regulator) that provides the 5V rail to fail or clamp shut on C20 or C18.
C20 seems to have a very small capacitance ( ) which may mean it failed or clamped.

[embedded: image-20230510-190239.png]

2. Processor messed up and shorted something … this theory needs more fleshing out

### Connor Peebles, 2023-05-10

Something else I noticed in the data is that the things to happen in chronological order: 
 at CPU Time 5720.6 APAltSet sets to 458ft from 400ft
[embedded: image-20230510-190748.png]

LinkApRx is lost at CPU Time 5730.6, 10 seconds after APAltSet is set to 458ft, or somewhere within those 10 seconds.
[embedded: image-20230510-190836.png]

VServo(s) start dropping at CPU Time 5740.2, ~10 seconds after LinkApRx is lost, or somewhere within those 10 seconds the AP reset and the slow drop off is capacitors discharging.
[embedded: image-20230510-190952.png]
[embedded: image-20230510-191002.png]
After CPU Time 5740.2, the logging rate automatically increases to 10Hz.

### Cameron Chapman, 2023-05-10

Connor will provide more detail, but here is what he just found. 
- Applied 5V manually to processor. Processor functions normally. He also determined that the regulator overcurrent capacitor is blown. This indicates failure was due to the regulator. Could be failure with regulator components or overcurrent caused by one of the attached devices (processor is one of those, but many other components are as well)

### Connor Peebles, 2023-05-10

C20 should be about 3.3nF but on 444’s AP C20 is about 0.015nF. This could be a symptom of the overcurrent with the blown C20 constantly driving to ground to shut off the regulator. U14 isn’t sending the 500KHz switching frequency it should.

### Connor Peebles, 2023-05-11

Replacing C20 with a new 3.3nF cap worked in reviving 444’s AP. I think it was so low it was driving U14 to ground constantly, which kept it from turning on. Thus, no 5V rail. Faulty C20 was measured out-of-circuit to still be 0.016nF. 
The switching frequency went back up to 500KHz for U14, or rather U14 actually turned on again.

### Cameron Chapman, 2023-05-23

@Connor Peebles please update status and plan fields.

### Cameron Chapman, 2023-07-27

Also known/potential causes corrective action implemented so far, as discussed.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent.

## Attachments (35)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AC444 .10 (fb799e50-20a7-4414-8ae0-ec00ff4c78c9).zip | archive | 19018 | 2023-03-31 | listed only |
| AC444 .10.zip | archive | 3567 | 2023-03-31 | listed only |
| AC444 .2 (2d11277e-7cad-4bed-bb09-c7d91deb88d3).zip | archive | 4799 | 2023-03-31 | listed only |
| AC444 .2.zip | archive | 557 | 2023-03-31 | listed only |
| Charts.docx | docx | 1662 | 2023-03-31 | no text found |
| [FDR00041.csv](attachments/13373_FDR00041.csv.md) | csv | 73 | 2023-03-31 | converted |
| T0_V0_230330_220820_pack.zip | archive | 33 | 2023-03-31 | listed only |
| V444 Data Extraction.jpg | image | 259 | 2023-03-31 | listed only |
| [VT230330.txt](attachments/13375_VT230330.txt.md) | text | 228 | 2023-03-31 | converted |
| [VTL00029.xlsx](attachments/13372_VTL00029.xlsx.md) | xlsx | 9862 | 2023-03-31 | converted (cut) |
| [XC230331 (3dcaaf2d-84af-4939-bd2b-51b6f00733bc).txt](attachments/13376_XC230331%20(3dcaaf2d-84af-4939-bd2b-51b6f00733bc).txt.md) | text | 64 | 2023-03-31 | converted |
| [XCEVLOG.TXT](attachments/13401_XCEVLOG.TXT.md) | text | 58 | 2023-03-31 | converted |
| [XCL00041.xlsx](attachments/13374_XCL00041.xlsx.md) | xlsx | 1482 | 2023-03-31 | converted (cut) |
| [logfile_230330_220722.csv](attachments/13367_logfile_230330_220722.csv.md) | csv | 2839 | 2023-03-31 | converted |
| image-20230404-210633.png | image | 2 | 2023-04-04 | listed only |
| T95_V378_230417_071537_pack.zip | archive | 8289 | 2023-04-17 | listed only |
| IMG_0345.jpg | image | 4403 | 2023-04-26 | listed only |
| IMG_0346.jpg | image | 4463 | 2023-04-26 | listed only |
| IMG_E4423.JPG | image | 3113 | 2023-04-26 | listed only |
| [bevelwcc1.pdf](attachments/14231_bevelwcc1.pdf.md) | pdf | 1698 | 2023-04-26 | converted |
| [bevelwcc2.pdf](attachments/14230_bevelwcc2.pdf.md) | pdf | 1507 | 2023-04-26 | converted |
| [bevelwcc3.pdf](attachments/14232_bevelwcc3.pdf.md) | pdf | 1616 | 2023-04-26 | converted |
| IMG_0354.jpg | image | 5531 | 2023-04-27 | listed only |
| IMG_0356.jpg | image | 5715 | 2023-04-27 | listed only |
| IMG_0357.jpg | image | 4687 | 2023-04-27 | listed only |
| image-20230502-235959.png | image | 94 | 2023-05-02 | listed only |
| Connected.JPG | image | 389 | 2023-05-10 | listed only |
| FLIR0113.jpg | image | 153 | 2023-05-10 | listed only |
| FLIR0116.jpg | image | 134 | 2023-05-10 | listed only |
| FLIR0118.jpg | image | 180 | 2023-05-10 | listed only |
| image-20230510-190239.png | image | 62 | 2023-05-10 | listed only |
| image-20230510-190748.png | image | 58 | 2023-05-10 | listed only |
| image-20230510-190836.png | image | 43 | 2023-05-10 | listed only |
| image-20230510-190952.png | image | 99 | 2023-05-10 | listed only |
| image-20230510-191002.png | image | 61 | 2023-05-10 | listed only |
