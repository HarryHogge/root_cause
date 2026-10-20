# VXEP-1775: VXE-937 Crashed after briefly losing link.

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2026-03-17
- **Updated:** 2026-08-21
- **Resolved:** 2026-08-21
- **Reporter:** Michael Mohr
- **Assignee:** David Grosher
- **Creator:** Michael Mohr
- **Labels:** GS_Closed, Lithuanian_BG, RCCA, Software, Weekly-incident-tracker
- **Links:** relates to RMA-951 (VXE-937  RMA 260320-1); relates to RMA-953 (D4501012 RMA 260320-3); relates to VXEP-1780 (VXE 864 Crash); relates to VXEP-1692 (B40/30 XCOM WDT resets ); relates to VXEP-1978 (VXE 863 Loss of Link warning resulted in uncontrolled descent )
- **Customer:** Lithuania-Border-Guard
- **Vehicle Tail Number:** VXE-937
- **Root Cause:** xcomm WDT led to stale FWAP data
- **Incident Type:** Aircraft Loss
- **Severity:** 1 - Flight Critical
- **Executive Summary:** CA implementation in progress
- **RMA Disposition:** RMA was completed before this Section was added to Jira. Aircraft was rebuilt.

## Description

Operator statement post crash: 
I would like to inform you about an incident involving the unmanned aircraft VXE 30 Stalker No. 937. The incident occurred on March 16, 2026, at approximately 12:10. 
A planned familiarization and training flight was being conducted near the Medininkai Border Guard School using an unmanned aircraft powered by a fuel cell. 
We took off from the Border Guard School premises at 11:15. We flew approximately 2.5 km in a southwesterly direction over meadows and forests. I set the flight plan in a “stadium pattern,” climbed to 600 feet above ground level, and we circled in that area. 
After confirming that the system was operating smoothly and that the flight parameters were stable, we gradually increased altitude without changing location. At the time of the incident, we had climbed to 1,600 feet above ground level. Approximately one hour after takeoff, the camera operator warned that the video transmission had been lost. At that same moment, I briefly lost communication with the unmanned aircraft. When the connection was briefly restored, the aircraft’s position on the map in the control computer window was no longer changing. The fuel cell indication showed that its status was unclear. According to the telemetry data, the aircraft was still in fixed-wing mode, but it was not moving. 
After realizing that the aircraft had most likely crashed, the colleagues who were with me went toward the last displayed coordinates. Upon arriving at the location, they confirmed that the unmanned aircraft was lying on the ground and had crashed.
Operator also reports that communication was lost at 1600 FT for about 15 - 20 seconds and after that com was reestablished. After that UAV didn't move so operators suspected it crashed.  
Camera operator post crash: 
I was operating gimbal, my POV - it was flying normally, suddenly video lost and we found it exactly where it was showing on the map.

## Vehicle Configuration

Standard VXE30
Fuel Cell

## Corrective Action

https://jenaero.atlassian.net/browse/FS2-4473 engineering currently working implementation detection and handling of stale air data in FWAP

## Issue Status

Investigation powerpoint here:
https://jenaero.sharepoint.com/:p:/r/sites/FlightSafety/_layouts/15/Doc.aspx?sourcedoc=%7B1A5E851F-0AFC-43F2-8645-250B8824B274%7D&file=VXE937Crash_VXEP1775.pptx&action=edit&mobileredirect=true

## Comments (12)

### Michael Mohr, 2026-03-17

@David Grosher Working with Riga (Rudolfs Ribkinskis) to get the avionics and center wing RMA’d to SLO for data pull.

### Alexander Alan Arnold, 2026-03-23

@David Grosher @Scott Lovett Data has been uploaded to ticket. Sam M pulled all the logs from the Xcomm and VTOL as well as generated an FDR by the looks of it.

### Alexander Alan Arnold, 2026-03-23

@David Grosher Cody looked through some of the logs earlier and said he saw a couple Watch Dog resets and wanted me to relay that to you. Is there a way we could also tell that there are watch dog resets so we can build rules for scotts tool that is going to assist us in investigations? @Scott Lovett

### David Grosher, 2026-03-23

@Alexander Alan Arnold Yes, there was a XCOMM reset when the airspeed was below the setpoint. We believe that with the stale data the FW AP nose down to gain speed but since the data was stale it kept nosing down.

### Scott Lovett, 2026-04-07

Currently working on containment/corrective action

### Lauren Velasquez, 2026-04-10

@David Grosher This AC and FC are in the RMA Area ready for Engineering evaluation. Intake Procedure and photos have  been completed and uploaded to the linked RMA tickets.
@Drew Hildreth @Ronnie Baker  FYSA

### Eric Brewer, 2026-04-27

@David Grosher created a powerpoint for the investigation (attached above) with a brief log analysis.

### Eric Brewer, 2026-05-05

@David Grosher is this one good to move to ‘implenting corrective action’?

### David Grosher, 2026-05-05

@Eric Brewer Yes, I will move it along. We aren’t going to investigate this hardware anymore. There is a continuing investigation into hardware resets that is related. I linked to this ticket. @Michael Mohr

### Drew Hildreth, 2026-05-27

@Alexander Alan Arnold get somebody to create a report of this one as well. should be similar to 864. Once that is complete we can move this to D5. There is a start here already… move information to the new slide deck.

### Pat Wells, 2026-08-11

Reqested status update on CA 8/11/2026

### Drew Hildreth, 2026-08-21

@David Grosher do you want to keep this open for any reason? Aircraft has been rebuilt. Report has been sent. Corrective actions have been taken. Also there is a ticket for just the XComm Resets.

## Attachments (37)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Explanation video of flight p1.mp4 | video | 10011 | 2026-03-17 | listed only |
| Explanation video of flight p2.mp4 | video | 4630 | 2026-03-17 | listed only |
| IMG_8739.jpg | image | 672 | 2026-03-17 | listed only |
| IMG_8740.jpg | image | 532 | 2026-03-17 | listed only |
| IMG_8741.jpg | image | 547 | 2026-03-17 | listed only |
| IMG_8742.jpg | image | 499 | 2026-03-17 | listed only |
| IMG_8743.jpg | image | 956 | 2026-03-17 | listed only |
| IMG_8744.jpg | image | 293 | 2026-03-17 | listed only |
| Post Crash photo.jpg | image | 401 | 2026-03-17 | listed only |
| Post crash telemetry photo from soft.jpeg | image | 318 | 2026-03-17 | listed only |
| signal-2026-03-16-133109.jpeg | image | 546 | 2026-03-17 | listed only |
| signal-2026-03-16-133311.jpeg | image | 416 | 2026-03-17 | listed only |
| signal-2026-03-16-133317.jpeg | image | 116 | 2026-03-17 | listed only |
| signal-2026-03-16-133427.jpeg | image | 126 | 2026-03-17 | listed only |
| signal-2026-03-16-133504.mp4 | video | 4186 | 2026-03-17 | listed only |
| signal-2026-03-16-133504_002.jpeg | image | 501 | 2026-03-17 | listed only |
| signal-2026-03-16-133504_003.jpeg | image | 501 | 2026-03-17 | listed only |
| signal-2026-03-16-133504_004.jpeg | image | 463 | 2026-03-17 | listed only |
| signal-2026-03-16-133504_005.jpeg | image | 458 | 2026-03-17 | listed only |
| signal-2026-03-16-133504_006.jpeg | image | 401 | 2026-03-17 | listed only |
| signal-2026-03-16-133504_007.jpeg | image | 453 | 2026-03-17 | listed only |
| signal-2026-03-16-133504_008.jpeg | image | 484 | 2026-03-17 | listed only |
| signal-2026-03-16-133504_009.jpeg | image | 434 | 2026-03-17 | listed only |
| signal-2026-03-16-133504_010.jpeg | image | 398 | 2026-03-17 | listed only |
| signal-2026-03-16-133504_011.jpeg | image | 490 | 2026-03-17 | listed only |
| signal-2026-03-16-133504_012.jpeg | image | 498 | 2026-03-17 | listed only |
| signal-2026-03-16-133504_013.jpeg | image | 522 | 2026-03-17 | listed only |
| signal-2026-03-16-133504_014.jpeg | image | 542 | 2026-03-17 | listed only |
| signal-2026-03-16-133504_015.mp4 | video | 7279 | 2026-03-17 | listed only |
| signal-2026-03-16-133504_016.mp4 | video | 2460 | 2026-03-17 | listed only |
| signal-2026-03-16-133504_017.mp4 | video | 2079 | 2026-03-17 | listed only |
| signal-2026-03-16-133617.mp4 | video | 22962 | 2026-03-17 | listed only |
| signal-2026-03-16-133631.jpeg | image | 104 | 2026-03-17 | listed only |
| T95_V937_260320_171552_pack.zip | archive | 3228 | 2026-03-23 | listed only |
| VTOL_VXE937.zip | archive | 165633 | 2026-03-23 | listed only |
| XCOMM_VXE937.zip | archive | 85698 | 2026-03-23 | listed only |
| [VXEP-1775_VXE-937_Vehicle Investigation Report_20260626.pdf](attachments/63949_VXEP-1775_VXE-937_Vehicle%20Investigation%20Report_20260626.pdf.md) | pdf | 637 | 2026-08-07 | converted |
