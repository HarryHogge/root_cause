# VXEP-1978: VXE 863 Loss of Link warning resulted in uncontrolled descent

- **Issue type:** Incident (8D)
- **Status:** D6 - Implementing Corrective Actions
- **Priority:** Highest
- **Created:** 2026-08-07
- **Updated:** 2026-10-05
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Eric Brewer
- **Creator:** Alexander Alan Arnold
- **Labels:** RCCA, Software, Weekly-incident-tracker
- **Links:** relates to VXEP-1780 (VXE 864 Crash); relates to VXEP-1775 (VXE-937 Crashed after briefly losing link.); relates to VXEP-1548 (VXE 863 VTOL motors cut during landing resulting in unintended glide landing); relates to RMA-1082 (VXE-863 RMA 260810-1); relates to FS2-5173 (V863 Stuck Semaphore Issue)
- **Customer:** CBP
- **Vehicle Tail Number:** VXE 863
- **Vehicle Configuration:** Standard VXE, Battery, 140G2Z
- **Incident Type:** Aircraft Loss
- **Severity:** 1 - Flight Critical
- **Executive Summary:** engineering conducting endurance testing on hardware to induce fault

## Description

On 8/6/2026 at approximately 21:00, VXE-30 #863 suffered a catastrophic failure, resulting in a crash.   #863 was being operated by the Tucson Sector Border Patrol VXE Team, all members of which have been trained to operate the platform by Redwire.  The crash happened near San Miguel Arizona. 
 
Approximately 1.5 hours into the flight, the primary GCS running the SUAV software reported a loss of link notification.  The situational camera on the primary GCS, as well as the payload camera on the secondary GCS never lost communication to their respective payloads and continued to provide a video feed. The operators believed that the aircraft would regain connection automatically, but that did not happen.  After a short time of loss link status, the aircraft began to veer towards the pre-programmed loss link waypoint, however that cannot be confirmed, as the loss like waypoint location was already in the general direction that the aircraft was traveling when the loss of link occurred. 
 
After the primary GCS failed to reconnect to the aircraft, the operator attempted to manually reconnect.  That also was unsuccessful.  The operator then attempted to close the SUAV software and restart it.  The operator noted after the software was restarted and clicked connect, the pre-populated tail number was 999.
 
A few seconds later the secondary operator noticed on the payload camera that the aircraft appeared to be rapidly descending towards the ground and appeared to cut out as the aircraft made impact.  The GPS coordinates from the payload camera were noted, and the operators proceeded to those GPS coordinates and located the aircraft at those exact coordinates.
 
The aircraft appeared to have struck mesquite branches just before impact into the ground.  The aircraft and payload sustained extensive damage and appear to be a total loss.  The aircraft and payload were recovered and transported to the Tucson Sector Headquarters SUAS office and will be secured for further inspection/processing by Redwire.

## Corrective Action

Software fix to add timeout and recovery logic inside CycloneTCP.
Other CA’s TBD based upon results from investigation on frequency and hardware dependence.

## Plan

Fuse and wing case in engineering SWQA area 8/27/2026 (aircraft is significantly damaged, avionics is removed from fuse)
-Determine if avionics is OK to power on. Avionics enclosure has damage and may have made contact with internal boards. 
-Verify xcomm to FWAP communication link to determine if active or inactive

## Issue Status

Software path for failure identified.  Doing further analysis and testing to determine:
- How often can/does this issue occur across the fleet?
- Is there a hardware issue with 863 that makes the software path more likely to be encountered?
- Can we recreate it on 863?  @Cody Smisek if/when able, I think it’d be a good test to turn 863 on and let it run for several days.  We can analyze the logs afterward to see if this issue reappears or not.
- Can we recreate it on any other birds/HILs?


Investigation ppt in work, not yet completed as of 8/28/2026.
https://redwireglobal.sharepoint.com/:f:/r/sites/FlightSafety/Shared%20Documents/Active%20Cases/2026_08_VXE863Investigation?d=w3091e095ce2d488ea3d0ee5028dc7fd4&csf=1&web=1&e=EIvvtb

## Root Cause

Software tasks on xcomm locked due to infinite block inside CycloneTCP.  Unclear if hardware made this software failure mode more likely to happen.

## Comments (31)

### Alexander Alan Arnold, 2026-08-13

@David Grosher ive added some gcs logs. not sure if they have anything of value, the aircraft should be shipping today

### Mathew Papaleo, 2026-08-17

@Alexander Alan Arnold ive added aar and maint log, and screenshot of basic silvus page. let me know if there is anything else youd like to see

### Drew Hildreth, 2026-08-17

@David Grosher Mat was able to pull some data from 863

### David Grosher, 2026-08-17

@Drew Hildreth The board was not swapped during the RMA as requested. 

XComm startup 2026/08/17 20:00:50.602
version: 4.74
git commit hash: 2ae959d
build: 2025/12/11 16:55:53
code checksum: DD2DCD89
cyclone version: 2.0.2
Vehicle name: Stalker B30
Vehicle Class: VXE  95
XC SN: 5-6227

SCO in May 2025
[19:31:55.844] XComm startup 2025/05/13 19:31:55.844
[19:31:55.844] version: 4.71
[19:31:55.844] git commit hash: b0aebe6
[19:31:55.844] build: 2025/03/03 09:44:32
[19:31:55.844] code checksum: 5D1AAF76
[19:31:55.844] cyclone version: 2.0.2
[19:31:55.844] Vehicle name: VXE30
[19:31:55.844] Vehicle Class: VXE  95
[19:31:55.844] Tail number: 863
[19:31:55.844] XC SN: 5-6227

### Drew Hildreth, 2026-08-17

@David Grosher Thanks
@Lauren Velasquez Per our discussion, we have to verify that everything is captured. Assumptions are not good enough. This is why we have to use the Material Dispo Form and our Quote Requests are reviewed prior to going to Q&P.

### David Grosher, 2026-08-17

@Drew Hildreth @Lauren Velasquez Also, I couldn’t find any SCO data following the RMA. I’m a bit concerned that it was shipped without proper testing, regardless of the fact that the requested work was not performed.

### Mathew Papaleo, 2026-08-18

@David Grosher there is a vxe30 pre-delivery sco form  dated from january 2026. ill attach it fya @Lauren Velasquez

### David Grosher, 2026-08-18

@Drew Hildreth Can we also pull all of the SD card data as well?

### David Grosher, 2026-08-18

@Eric Brewer In the last AAR there is data from the day of the incident. It seems that the XCOMM event log simply stops while it is flying,  I don’t see any indication of anything happeneing. Can you look into the data to see if you find anything?

### Drew Hildreth, 2026-08-18

@Mathew Papaleo can you work on getting the data from the SD Card? I know the aircraft is in rough shape. If Scott W is in the office today he may be able to assist if we just have to pull SD Cards.

### Mathew Papaleo, 2026-08-18

@Drew Hildreth @Scott Whitney after talking to scott, ive identified the files requested, threw them in a zip folder, and added to attachments on this Jira page.

### Drew Hildreth, 2026-08-18

@David Grosher Mat was able to pull the SD Card Files.

### Drew Hildreth, 2026-08-18

@Alexander Alan Arnold @Jackson Riley Curvin Mat added a zip file above of the SD Card Files

### Eric Brewer, 2026-08-18

@David Grosher  I'm seeing that all the telemetry from the fwap on xcomm seems to freeze at time 5335.  I see the bms voltages continue to update/change after that, but all fwap telemetry is frozen.  
VTOL shows that the vehicle entered a steep pitch down with roll below 10 degrees. 
radalt on xcomm continues updating and agrees with what VTOL sees - rapid descent. 

The data seems to indicate fixed-wing became unresponsive and likely cut all the actuators which led to a nose dive.  It’s unclear if it’s due to power failure or something else.

 @Alexander Alan Arnold @Drew Hildreth @Jackson Riley Curvin FYSA.

### Eric Brewer, 2026-08-19

@David Grosher @Alexander Alan Arnold @Drew Hildreth @Jackson Riley Curvin some new evidence, the logs in the FDR (from fixed-wing ap) cut a little bit after the dive begins.  This indicates that the telemetry stopped going to xcomm before the dive began, but at least some parts of the fwap were still logging data during the beginning of the dive.  @John Clark can you see if there’s any way this might have happened within fwap where the link back to xcomm dropped but the logger was still working?

### Drew Hildreth, 2026-08-20

@Eric Brewer Really appreciate the continued work on this. 

@John Clark The aircraft (or what is left of it) is down in RMA if you need anything.

### John Clark, 2026-08-20

@Eric Brewer I am not aware of anything that would prevent logging continuation on link loss between  XComm  and FW-AP in the logs the FW-AP keeps in it’s local serial flash. Recall those appear as FDRxxx. Those logs also appear in the XComm. But in some cases there may be logging that was recorded exclusively in FW, I think. If you have an AAR I’d be happy to look and see what I can find.

### Eric Brewer, 2026-08-20

@John Clark AAR is attached. The xcomm log of interest is T95_V863_260817_130122_xcl00188.csv, FDR is T95_V863_260817_130122_fdrrecov

### John Clark, 2026-08-21

@Eric Brewer There are a total of seven frames recorded in the fdrrecov provided once the Uplink is lost.
[embedded: image-20260821-151952.png]
I note some losses in those frames: VertSpd, RCUpdate, PwrInt. After those frames the log ends. PwrInt is an integral term for Power PID. RCUpdate are Remote Cmds (Tagged Pkts). That would be consistant with the Link Loss. VertSpeed is logged ultimately from UpdateVertSpeed in the outer loop. Controlled here:
[embedded: image-20260821-153541.png]
I did not see a full Debug Log. I cant be certain the FW-AP did not watchdog.
*One final comment the actual computation of the Uplink State is complex. I did fully decode it.

### Cody Smisek, 2026-08-27

@Eric Brewer For some reason this aircraft ended up in engineering area. Was there anything we needed from it? I don’t see any updates to issue status or plan field so not sure why it’s in engineering. From the comments it seems like we have the data off of it?
@Scott Whitney @John Clark @David Grosher @Alexander Alan Arnold

### David Grosher, 2026-08-27

@Cody Smisek This is in an active investigation that will likely require some testing of the hardware.

### Eric Brewer, 2026-08-27

@Cody Smisek @David Grosher @Scott Whitney @John Clark @Alexander Alan Arnold sorry Cody the issue status isn’t up to date with what we’re currently investigating, but what we saw is that xcomm appeared to lose communication with a few other subsytems including FWAP.  As a troubleshooting step it’d be good to see if the hardware is currently functioning and communicating with xcomm<->fwap or if that is broken.  IF it’s still broken that points to a hardware failure, if it’s working fine now it would be unclear if we had a software failure in flight or some sort of intermittent hardware issue.

Working on some more investigation today and will update status and next steps above based upon what I find.

### Cody Smisek, 2026-08-27

@Eric Brewer I will take a look at the aircraft and see if it’s in a state to be powered on and check xcomm-fwap

### Cody Smisek, 2026-08-27

Fuselage Avionics was powered via power supply and breakout harness. No other aircraft components connected. FWAP sensors populate and respond to avionics movement. FWAP versions populate on xcomm throughput. 
Seems to indicate FWAP is communicating with xcomm. 
Avionics enclosure shows signs of significant impact. Any hardware defects discovered internally should take into consideration high velocity impact with terrain. 
@Eric Brewer FYI

[embedded: image-20260827-180659.png]
[embedded: image-20260827-180715.png]
[embedded: image-20260827-180727.png]

### Eric Brewer, 2026-08-28

@Cody Smisek @David Grosher @Scott Whitney @John Clark @Scott Hunter @Alexander Alan Arnold I linked an investigation ppt above with the findings so far.  With some help from John and Scott we were able to identify that few software tasks were blocked due to an infinite wait time and the innards of our communication software being locked up.  We don’t know yet if this was more likely to happen with 863’s hardware or if it was just unlucky. We can run the additional testing recommended above and see what we find.  Will also continue analysis and testing to see how we can recover from such a situation in the future.

### Cody Smisek, 2026-08-31

@Eric Brewer can you update the link as it links to the old server and I cannot find the folder in incident reports folder.

### Eric Brewer, 2026-09-04

@Alexander Alan Arnold @David Grosher @Cody Smisek @Scott Whitney quick update on this.  We have been leaving the 863 avionics powered on during this entire week.  We have not observed the same stuck semaphore issue, though we did see an unrelated WDT reset on the xcomm processor. We will continue testing to see if the issue surfaces, but at this point it’s looking like just a really infrequent corner case of the software that can cause this vs. something inherently wrong with 863’s hardware.

### Cody Smisek, 2026-09-08

system was left running over the long weekend. uptime for both webpages shows 123hrs. already previously reported difficulty pulling larger files from the avionics. xcomm event log is now 30mb, file downloading stops during all attempts. unless further direction / instruction on how to pull these larger logs is provided, I’ve discontinued the testing and returned equipment to their respective cases.

### Lauren Velasquez, 2026-09-08

@Drew Hildreth  Let me know how you would like RMA to proceed @Zack Garcia  @Alexander Alan Arnold  FYA

### Drew Hildreth, 2026-09-10

@Lauren Velasquez Hold on any movement with Quotes and such. Most important is to identify Root Cause and have CAs in place. Then we get the report compelted and sent to the customer.

@Alexander Alan Arnold were we able to get anywhere Cody’s inquiry above in regards to the large files?

### Zachary Mann, 2026-10-05

Team is currently working on the software and should be completed on 6.8.1.

## Attachments (18)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 5364.jpg | image | 339 | 2026-08-07 | listed only |
| 5365.jpg | image | 341 | 2026-08-07 | listed only |
| 5369.jpg | image | 362 | 2026-08-07 | listed only |
| 5372.jpg | image | 308 | 2026-08-07 | listed only |
| 5375.jpg | image | 352 | 2026-08-07 | listed only |
| 5376.jpg | image | 380 | 2026-08-07 | listed only |
| 5378.jpg | image | 288 | 2026-08-07 | listed only |
| [Customer Mishap  Issue Reporting Form Aircraft 863.docx](attachments/63957_Customer%20Mishap%20%20Issue%20Reporting%20Form%20Aircraft%20863.docx.md) | docx | 123 | 2026-08-07 | converted |
| GCS_LOGS.zip | archive | 419 | 2026-08-13 | listed only |
| Screenshot 2026-08-17 132143.png | image | 338 | 2026-08-17 | listed only |
| T95_V863_260817_130122_pack.zip | archive | 1890 | 2026-08-17 | listed only |
| [vxemaintenancelog.txt](attachments/64094_vxemaintenancelog.txt.md) | text | 2 | 2026-08-17 | converted |
| sd card files from log files.zip | archive | 6236 | 2026-08-18 | listed only |
| image-20260821-151952.png | image | 3 | 2026-08-21 | listed only |
| image-20260821-153541.png | image | 75 | 2026-08-21 | listed only |
| image-20260827-180659.png | image | 90 | 2026-08-27 | listed only |
| image-20260827-180715.png | image | 85 | 2026-08-27 | listed only |
| image-20260827-180727.png | image | 109 | 2026-08-27 | listed only |
