# VXEP-555: VXE 530 Anomalies on Launch and in flight

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2024-08-22
- **Updated:** 2026-03-02
- **Resolved:** 2025-06-18
- **Reporter:** Pat Wells
- **Assignee:** Jason Scherer
- **Creator:** Pat Wells
- **Labels:** FlightSystems, GCS, TIQUILA, Weekly-incident-tracker
- **Links:** relates to ENG-3047 (530 Anomalies on Launch and In Flight); relates to FS2-2336 (Mission Failed to Sync (VXEP-555)); relates to FS2-2337 (Unexpected pause during takeoff (VXEP-555)); relates to FS2-2338 (Investigation into GCS taking over 1 min to reconnect to vehicle when GCS IP address changed due to switching ethernet ports while connected.); relates to GCSS-366 (GCS froze during RTB command); relates to FS2-2339 (Investigate Delay in GCS accuracy during landing (VXEP-555)); relates to RMA-457 (VXE-530 RMA  250108-1 (SD Card Swap & Expansion) ); relates to FS2-2854 (Jason's Open Investigations); relates to VXEP-1069 (Multiple RMA Aircraft Unable to Connect to Xcomm); relates to FS2-3092 (VXEP-555 20-30 second lag in vehicle position on GCS); relates to VXEP-1311 (VXE 530 GCS Lag)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 530
- **Plan:** Review new xcomm logs
- **Incident Type:** Near Miss
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Received from LM:
Multiple anomalies were observed during the third and fourth flights of V530 during the Reiver Look 2 T&E in the UK.  On 22 August 2024:
- During V530 1st flight of the day, 4th flight of the T&E, during a mission sync, the sim took a LONG time, then the mission upload failed and timed out.  This happened a few times before the mission was successfully sync’d.  Mission was fairly large/long, but still took an unexpectedly long time (and multiple failures) to sync.  Comms indicator was green and comms (per the Silvus GUI) were excellent (SNR=34, Airtime <60%). @Jason Scherer Looking at new data
- On the 2nd flight of the day, the aircraft paused briefly (throttle reduced) before lifting out of the stand, then paused for ~5 seconds at 10 feet before continuing to climb.  See attached video with sound up to hear throttle pause in stand. @Eric Brewer Conclusion in Report
- During flight, radio Ethernet cable was moved from one Ethernet port to the other to eliminate multiple SA camera video feeds in the downlink.  Cable was reconnected within 2-3 seconds.  GCS software took 60+ seconds to reconnect to aircraft.  Comms (per Silvus GUI) were great. @Ted Trowbridge - Data is not in the logs.
- When RTB was commanded, GCS screen froze with hourglass for 90+ seconds.  When the sim (or whatever it was doing) finished, a window popped up for 1 or 2 seconds stating that the aircraft was executing the Lost Comms Mission.  when the window closed, the aircraft entered the active landing pattern with no user input.  Comms indicator remained green throughout and comms (per Silvus GUI) were great. @Ted Trowbridge Data is not in the logs.
- During the landing pattern, it was observed that the aircraft position and telemetry on the GCS was 20-30 seconds behind the actual aircraft position.  This could have been an issue if the gap had been longer and the aircraft had landed before the operator was given the option to Enable User Landing Control.  See attached video of GCS showing aircraft on approach to landing while the aircraft was already on the ground.  @Ted Trowbridge @Jason Scherer Relook at this

AAR data has to go through formal MOD channels which will take a few days.
For consistency, the MOD plans to fly the same aircraft with the same GCS tomorrow.  Please advise Garret Moose asap if the recommendation is to NOT fly V530 until the fight data is reviewed.

## Issue Status

Originally unable to connect to xcomm. Removed SD card, no change. Re-flashed xcomm firmware and now can access. 
Pulled relevant xcomm logs and stored on sharepoint. 
Placed report here.
SharePoint: Here

## Comments (29)

### Jason Scherer, 2024-11-08

@Pat Wells I have been re-tasked to work on the SD Card investigation. I will need to put this investigation back in my to do list for now.

### David Grosher, 2024-11-15

@Ted Trowbridge Can you look into the GCS freezing issue in item 4 and the delay on the GCS in item 5. It is unclear if we have enough diagnostics in place to look into this. 
@Eric Brewer Pull together a report (Some data in the comments below for item 3). And, look into item 2. 
@Jason Scherer spend some time on item 1.

### Jason Scherer, 2024-11-18

@Pat Wells Would it be possible to get the previous AAR T95_V530_240822_133603_pack.zip. I’m working on item #1 and I don’t see any mission upload/download timeouts in the debug of the AAR currently attached (T95_V530_240822_151625_pack) to this ticket. However, I do see timeouts in the event log for the previous AAR, which should be for the same day according to the event log we do have.

### Pat Wells, 2024-11-18

@Jason Scherer I’ll request the AAR.

### Eric Brewer, 2024-11-19

@David Grosher @Pat Wells @Ted Trowbridge @Jason Scherer I linked a report above.  I put Mike’s text in the report for the IP issue, and I created a writeup for the launch throttle issue.  The launch throttle issue looks like a race condition/hole in our initialization logic that can allow the motors to try to spool to full for 1s before xcomm has actually commanded a launch.  Then when the launch is commanded it returns to soft start so the end result is that the motors spool up then back down before launch.  Based upon how the vehicle responded it seems like it should be ok but I suppose it’s conceivable that in some case it could lift off the tray before we intend for it to.  
If they have the previous AAR’s that Jason requested below I may be able to tell what caused the altitude command to be high and propose a workaround short term, long term we’ll need to address this software defect.

### Eric Brewer, 2024-11-19

@David Grosher @Pat Wells @Ted Trowbridge @Jason Scherer After reviewing another unrelated log, it occurred to me that this one did not use VTOL on landing, and it is still using an older software version (VTOL 1.53).  If this is the case, the mcAlt cmd is never reset after the flight, so this explains why the altitude command is high.  In this case we’d need to recommend either power cycling the vehicle between flights or updating to the latest software.  Is there a reason they are not on 1.55.03?

### Pat Wells, 2024-11-19

@Eric Brewer this is the TIQUILA customer and their approval process for software updates is lengthy. At the time of this event they had not yet approved an update.

### David Grosher, 2024-11-26

@Pat Wells We are waiting on the 2nd AAR for this to move forward.

### Alexander Alan Arnold, 2025-01-10

@Pat Wells Did we ever receive the second AAR?

### Pat Wells, 2025-01-10

@Alexander Alan Arnold @David Grosher @Rodney Linch 
Aircraft is inbound to SLO for SD card rework.  
Will pass over to engineering team to investigate when it arrives.

### Rodney Linch, 2025-01-14

@David Grosher - AC cases delivered to Engineering drop-off area.

### Pat Wells, 2025-03-04

@Jason Scherer is this complete?

### Jason Scherer, 2025-03-04

@Pat Wells Quick answer is no. This still needs work.
I have not worked on this since my last update (Nov 18 where I was blocked pending more log data). Reading through the comments it looks like the vehicle is now here (since Jan14), so the logs need to be pulled and analyzed. 
I’m now tracking all my investigation related work in the attached ticket (FS2-2854 “Jason’s Open Investigations). I frequently update status/priority as I work down investigations, so if you ever want to know what I’m active on, or if you think I might be missing an investigation, this is a good place to look.
This ticket (VXEP-555) is currently lumped in the “Other High Priority Incidents” category which is #8 on the list of things for me to look at. I’m blocked on the first few which are NCRs that are going through rework and an RMA that needs EE support, so I’m currently active on investigations https://jenaero.atlassian.net/browse/VXEP-600 and https://jenaero.atlassian.net/browse/VXEP-1054 (Pri 3 & 4). After these investigations (1-2 days), Dave has me queued up to get back to some critical development work (UAP) before going after the other incidents. 
@David Grosher FYSA

### Cody Smisek, 2025-03-04

@Jason Scherer has asked for help on this. I will find vehicle and pull aircraft logs and take a look.

### Cody Smisek, 2025-03-04

Unable to access xcomm. VTOL webpage shows no connection with xcomm. Looking into issue. Uploaded VTOL data.

### Cody Smisek, 2025-03-10

xcomm logs uploaded. status updated

### Michael Mohr, 2025-04-22

@Cody Smisek @Jason Scherer Has there been any update to these anomalies investigations? Is the swapping of the ethernet ports the cause of the delays in commanded RTB and GCS accuracy during landing?

### Pat Wells, 2025-06-16

@David Grosher @Jason Scherer can we bump this up in priority.  Customer is asking questions.. @Drew Hildreth

### David Grosher, 2025-06-16

@Drew Hildreth Please split this into the 5 different issues that it represents. The three closed conclusions can be provided to the customer. The remaining two we can address as we have time. Currently we can’t provide any bandwidth from Jason. @Pat Wells FYSA

### Drew Hildreth, 2025-06-18

4/5 issues have been resolved on this ticket or can’t be reproduced. Final issue is https://jenaero.atlassian.net/browse/VXEP-1311.

### Pat Wells, 2025-03-04

@Jason Scherer is this complete?

### Jason Scherer, 2025-03-04

@Pat Wells Quick answer is no. This still needs work.
I have not worked on this since my last update (Nov 18 where I was blocked pending more log data). Reading through the comments it looks like the vehicle is now here (since Jan14), so the logs need to be pulled and analyzed. 
I’m now tracking all my investigation related work in the attached ticket (FS2-2854 “Jason’s Open Investigations). I frequently update status/priority as I work down investigations, so if you ever want to know what I’m active on, or if you think I might be missing an investigation, this is a good place to look.
This ticket (VXEP-555) is currently lumped in the “Other High Priority Incidents” category which is #8 on the list of things for me to look at. I’m blocked on the first few which are NCRs that are going through rework and an RMA that needs EE support, so I’m currently active on investigations https://jenaero.atlassian.net/browse/VXEP-600 and https://jenaero.atlassian.net/browse/VXEP-1054 (Pri 3 & 4). After these investigations (1-2 days), Dave has me queued up to get back to some critical development work (UAP) before going after the other incidents. 
@David Grosher FYSA

### Cody Smisek, 2025-03-04

@Jason Scherer has asked for help on this. I will find vehicle and pull aircraft logs and take a look.

### Cody Smisek, 2025-03-04

Unable to access xcomm. VTOL webpage shows no connection with xcomm. Looking into issue. Uploaded VTOL data.

### Cody Smisek, 2025-03-10

xcomm logs uploaded. status updated

### Michael Mohr, 2025-04-22

@Cody Smisek @Jason Scherer Has there been any update to these anomalies investigations? Is the swapping of the ethernet ports the cause of the delays in commanded RTB and GCS accuracy during landing?

### Pat Wells, 2025-06-16

@David Grosher @Jason Scherer can we bump this up in priority.  Customer is asking questions.. @Drew Hildreth

### David Grosher, 2025-06-16

@Drew Hildreth Please split this into the 5 different issues that it represents. The three closed conclusions can be provided to the customer. The remaining two we can address as we have time. Currently we can’t provide any bandwidth from Jason. @Pat Wells FYSA

### Drew Hildreth, 2025-06-18

4/5 issues have been resolved on this ticket or can’t be reproduced. Final issue is https://jenaero.atlassian.net/browse/VXEP-1311.

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| V530 Landing While On the Ground.MOV | video | 23094 | 2024-08-22 | listed only |
| V530 Pauses on Launch.mp4 | video | 10911 | 2024-08-22 | listed only |
| V530 RTB Commanded (1).MOV | video | 66276 | 2024-08-22 | listed only |
| V530 RTB Commanded.MOV | video | 66276 | 2024-08-22 | listed only |
| T95_V530_240822_151625_pack.zip | archive | 1849 | 2024-08-23 | listed only |
| [VXE-530 Anomalies.pdf](attachments/30002_VXE-530%20Anomalies.pdf.md) | pdf | 524 | 2025-06-18 | converted |
