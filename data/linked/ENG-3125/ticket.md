# ENG-3125: VXE(MCM) 732 Altitude Excursions

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-11-21
- **Updated:** 2025-06-02
- **Resolved:** 2025-02-04
- **Reporter:** Garret Moose
- **Assignee:** Pat Wells
- **Creator:** Garret Moose
- **Links:** relates to VXEP-786 (VXE 732 Altitude Excursions)

## Description

We were testing landing patterns VCSi (1.0.0.dev7)/OGCS(1.0.0).  ELZ altitudes were 200 ft pattern, 300 ft IP1.  V732’s altitude increased enroute to IP1, started to descend in IP2, but released out to IP4 at 450 ft.  It then climbed in IP4 to over 900 ft AGL.  I commanded the plane to Fly to a waypoint in the route to stop the climb.

Later (I believe the final pattern and landing) altitude increased to over 600 ft in IP2 before descending to normal altitudes and landing. 

We are grounding flying VCSi/OGCS until we understand the cause.

## Comments (9)

### Pat Wells, 2024-11-22

@Garret Moose received.

### Craig Burton, 2024-11-22

I just sent an email to Dan and Garret with instructions for retrieving logs from the MCM.  Pasting here for future reference:

In MCM version 1.1, we’ve added some features that make it easier to pull individual logs from the vehicle.  But for 1.0, it’s easier to do so from the Linux command line.
- Connect to the MCM from Windows
- Open a CMD or PowerShell window
- ssh mcadmin@10.130.220.30 (and type the password)
- Change directory to where the VSM logs are located, then archive and compress them:
- cd /mnt/edge/vsm/logs
- tar cf vsm-732-logs.tar vsm-*
- gzip vsm-732-logs.tar
- Change directory to where the Onboard GCS logs are located, then archive and compress them:
- cd /mnt/edge/cucs/logs
- tar cf ogcs-732-logs.tar *
- gzip ogcs-732-logs.tar
- Exit from the ssh session with MCM
- exit
- Pull the logs from the MCM to the PC from CMD or PowerShell
- scp mcadmin@10.130.220.30:/mnt/edge/vsm/logs/vsm-732-logs.tar.gz .
- Note that there is a space between “…tar.gz” and the period (“.”) that follows.
- scp mcadmin@10.130.220.30:/mnt/edge/cucs/logs/ogcs-732-logs.tar.gz .

The compressed log files are now on your PC in the directory that was used when you opened CMD or PowerShell.
Depending on the size of the file, and how Edge’s email handles receipt of gzip files, you may have to send the logs to me via SIE (extcburt)

### Daniel Lloyd, 2024-11-22

Uploaded VSM and OGCS logs from the MCM.
@Craig Burton

### Craig Burton, 2024-11-22

Thanks for the logs @Daniel Lloyd .
While most of @Garret Moose ’s concerns in his email from yesterday evening related to altitudes in the landing patterns, one thing that struck me was the report that “Matt plotted the commanded altitude and there were two spikes up to 3000 ft.“
I’ve done a quick scan of the VSM logs which appear to show the highest altitude in all the flights is 2,982 feet, but that’s MSL.  With a reference altitude of 2,500 feet MSL, the highest flight altitude on 11/21 was 482 feet.  Could Matt’s plots have been in MSL?

### Daniel Lloyd, 2024-11-22

The altitude excursion flight was on 19 November
Dan
Get Outlook for iOS<https://aka.ms/o0ukef>

### Daniel Lloyd, 2024-11-24

In the AAR file from 19 November there is FDR file T95_V732_241119_092746_FDR00074.csv.
In that file you can see two brief instances of commanded altitudes to 2800-2900 feet. The altitude is, “Command altitude in feet, relative to sensor zero altitude”.
You can also see an occurrence of a flight altitude near 900 feet and one near 600 feet. The altitude is, “Altitude in feet, measured via barometric pressure, relative to altitude at which sensors were zeroed”.
@Craig Burton @Garret Moose @matthew.curran

### Craig Burton, 2024-11-24

Hi Dan,
Yes, I concur with your observations.  I found the same commanded altitudes a little later on Friday and published my findings to an internal ticket.  I failed to update this one thinking that no one would be looking at data over the weekend.

[embedded: altitude-set.png]
I’ve identified the root cause, but, since I found it at the end of the day Friday, no one has had the chance to review my findings.  We will hopefully have an official answer for you tomorrow.
@Daniel Lloyd @Garret Moose @matthew.curran

### Craig Burton, 2024-12-04

Three altitude excursions were analyzed.  The times of the events were 11:12:13, 12:00:26 and 12:20:00.  The first two were inadvertently commanded due to a software defect and the last one is suspected as being environmental in nature.
Commanded Excursions
The root cause for the two commanded excursions has been identified as a defect in the 1.0 release of the VSM, in which Landing Patterns could be Previewed prior to AP reference altitude establishment which occurs during the Calibrate step in the Launch Wizard.  The times noted above, 11:12:13 and 12:00:26, are associated with the first times at which the landing patterns were executed. At 11:12:13, the Primary pattern was automatically entered after the autopilot completed its single waypoint primary mission, and at 12:00:26 was the first time that the Emergency LP was commanded by the operator. This suggests that the rapid climbs observed had to do with the altitudes loaded into the landing patterns themselves.
Reconciling the calibration time of the vehicle with the time at which the landing patterns were Previewed reveals the root cause of this incident: the landing patterns were previewed prior to the vehicle having been calibrated. This was a vulnerability in the 1.0 release prior to the extra validation to guard against this scenario (fixed in 1.1):
The landing patterns were Previewed (Purpose == 0) at 10:06:34 and 10:07:04:
10:06:34.708835: cucs_req a010133 Landing Pattern Request (#17000) ff000000 Type Alt
10:06:34.729324: vsm_resp ffffffff Landing Pattern (#17001) ff000000 Pur 0, Type Alt
10:07:04.530041: cucs_req a010133 Landing Pattern Request (#17000) ff000000 Type Pri
10:07:04.550516: vsm_resp ffffffff Landing Pattern (#17001) ff000000 Pur 0, Type Pri
But the vehicle wasn’t calibrated until 10:09:21:
10:09:13.092584: oper Vehicle reference altitude has been set to 2502 ft MSL.
10:09:21.741257: oper Vehicle reporting reference altitude of 2502 ft MSL.
10:09:43.560259: oper 0x0a010133 uploaded waypoints 1, 2, 3, 4
10:09:43.737884: ap_ack Primary route upload has been acknowledged by the AP
10:09:52.804133: ap_ack Emergency Landing route upload has been acknowledged by the AP
10:09:58.544470: ap_ack Primary Landing route upload has been acknowledged by the AP
Due to the lack of calibration, the landing pattern altitude encodings would not have subtracted the reference elevation of roughly 2,500 feet. The commanded altitudes of 2,863 and 2,873 feet represent the DTED elevation under IP1 plus the requested AGL value of 300 feet.  Because the landing patterns were re-uploaded in flight, the proper calibration was encoded into the landing pattern waypoints, allowing a safe landing.
Non-commanded Excursion
In addition to the two previously discussed (unintentionally) commanded climbs (circled in blue), there was a third near the end of the flight (yellow highlight). During this climb, the vehicle was flying a Primary landing approach. The VSM’s logs indicate that the Operating Mode was RTB throughout the climb, from 12:20 to 12:21, with a rapid descent from 12:21 to 12:22. The RTB operating mode results in the VSM commanding the landing, but inhibiting any further commands until a new mode is entered (i.e. all subsequent VCSi commands are filtered until changed). Thus, this climb was not commanded by the VSM.
[embedded: v732-19-Nov-2024-annotated.png]
Looking at the AP logs, specifically the reading OLPwrCom from T95_V732_241119_092746_FDR00074.csv, we can see that during this time interval of 12:20 to 12:22, the commanded power shows a marked reduction in throttle, dropping from 40% to under 10% (and approaching 1%) for the duration of the rapid climb and descent.
 
[embedded: OLPwrCom.png]
Garret’s notes indicated that there were strong thermals encountered during their tests; I suspect that this un-commanded climb was the result of encountering one of these shortly before landing.
@Daniel Lloyd @Garret Moose @matthew.curran

### Pat Wells, 2024-12-10

@Garret Moose see below for report on this issue.

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V732_241119_092746_pack.zip.allow | other | 9839 | 2024-11-21 | listed only |
| ogcs-732-logs.tar.gz | archive | 16719 | 2024-11-22 | listed only |
| vsm-732-logs.tar.gz | archive | 24499 | 2024-11-22 | listed only |
| 732 Altitude Excursion 10 Nov 24.jpg | image | 85 | 2024-11-24 | listed only |
| altitude-set.png | image | 116 | 2024-11-24 | listed only |
| OLPwrCom.png | image | 124 | 2024-12-04 | listed only |
| v732-19-Nov-2024-annotated.png | image | 275 | 2024-12-04 | listed only |
