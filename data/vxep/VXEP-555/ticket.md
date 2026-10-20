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

### Pat Wells, 2024-08-23

@David Grosher AAR file has been added.

### Pat Wells, 2024-09-16

@David Grosher checking in for any updates ahead of the Air Worthiness brief with TIQ on Wed 9/18

### David Grosher, 2024-09-16

@Pat Wells No progress to date. There are other issues being worked.

### David Grosher, 2024-09-27

@Scott Whitney

### Scott Whitney, 2024-09-30

@David Grosher - I created https://jenaero.atlassian.net/browse/FS2-2335 to capture all the tasks/bugs in this issue. All issues are also linked to here

### Jason Scherer, 2024-10-09

@David Grosher @Scott Whitney @Pat Wells Quick look at the XComm log. GCS switched IPs during flight (I’m guessing that they switched Ethernet ports during flight to resolve the SA Cam issue Item#3 above). This changed the active IP for the GCS. The vehicle was already locked into the other IP which caused a delay, of about 50 seconds in connectivity, until the vehicle connection timeout occurred and allowed the new IP to connect.
Initial Connection: (GCS Connects with IP 10.0.108.51)
XComm Log: [14:16:41.856 9479.856] config paired with: 10.0.108.51:50201
XComm Log: [14:16:41.858 9479.858] link paired with: 10.0.108.51:50012
During Flight, the GCS secondary IP (10.0.108.50) attempts to connect, and is rebuked by the vehicle
XComm Log: [14:44:05.132 11123.132] ping attempt rebuked: 10.0.108.50:50020
XComm Log: [14:44:05.352 11123.352] ping mismatch ping 10.0.108.51
XComm Log: [14:44:05.353 11123.353] ping mismatch sip 10.0.108.50
Edit: Looking at the GCS Debug log (debug.txt) I can see the GCS gets a new IP after the launch and activation of the primary mission 
GCS Debug Log: [15:42:41.808] Mission DB in vehicle verified
GCS Debug Log: [15:42:53.766] new local ip: 127.0.0.1
GCS Debug Log: [15:42:58.796] new local ip: 10.0.108.50
GCS Debug Log: [15:43:07.856] Show Caution(): Master Caution
GCS Debug Log: [15:43:07.857] MessageBoxTop(): LOSS OF DOWNLINK WARNING
GCS Debug Log: [15:43:11.030] Show Caution(): Master Caution
GCS Debug Log: [15:43:52.894] Show Caution(): Master Caution
GCS Debug Log: [15:43:52.894] MessageBoxTop(): LOSS OF DOWNLINK
rebuke messages continue for the next  14 seconds.
The GCS tries to connect on the secondary IP (10.0.108.50) and is rebuked
XComm Log: [14:44:19.799 11137.799] connect attempt rebuked: 10.0.108.50:50204
XComm Log: [14:44:19.883 11137.883] ip mismatch cfg 10.0.108.51
XComm Log: [14:44:19.885 11137.886] ip mismatch sip 10.0.108.50
XComm Log: [14:44:19.887 11137.887] connect attempt rebuked: 10.0.108.50:50204
XComm Log: [14:44:19.897 11137.897] ip mismatch cfg 10.0.108.51
XComm Log: [14:44:19.898 11137.898] ip mismatch sip 10.0.108.50
XComm Log: [14:44:19.899 11137.899] connect attempt rebuked: 10.0.108.50:50204
XComm Log: [14:44:19.910 11137.910] ip mismatch cfg 10.0.108.51
XComm Log: [14:44:19.911 11137.911] ip mismatch sip 10.0.108.50
XComm Log: [14:44:19.912 11137.912] connect attempt rebuked: 10.0.108.50:50203
XComm Log: [14:44:19.923 11137.923] ip mismatch cfg 10.0.108.51
XComm Log: [14:44:19.924 11137.924] ip mismatch sip 10.0.108.50
XComm Log: [14:44:19.925 11137.926] connect attempt rebuked: 10.0.108.50:50203
XComm Log: [14:44:19.936 11137.936] ip mismatch cfg 10.0.108.51
XComm Log: [14:44:19.937 11137.937] ip mismatch sip 10.0.108.50
XComm Log: [14:44:19.938 11137.938] connect attempt rebuked: 10.0.108.50:50203
XComm Log: [14:44:19.949 11137.949] ip mismatch cfg 10.0.108.51
XComm Log: [14:44:19.950 11137.950] ip mismatch sip 10.0.108.50
XComm Log: [14:44:19.951 11137.951] connect attempt rebuked: 10.0.108.50:50203
Then ping rebuke messages (along with more connection attempts) continue
XComm Log: [14:44:58.945 11176.945] ping attempt rebuked: 10.0.108.50:50020
XComm Log: [14:44:59.056 11177.056] ping mismatch ping 10.0.108.51
XComm Log: [14:44:59.057 11177.057] ping mismatch sip 10.0.108.50
Vehicle connection timeout occurs, and the GCS is allowed to connect on the new IP Address (10.0.108.50)
XComm Log: [14:44:59.179 11177.179] link timeout
XComm Log: [14:44:59.180 11177.180] uplink state was/is: ACTIVE TIMEOUT
XComm Log: [14:44:59.181 11177.182] muav release
XComm Log: [14:44:59.182 11177.183] ping paired with: 10.0.108.50:50020
XComm Log: [14:45:04.113 11182.114] config paired with: 10.0.108.50:50201
XComm Log: [14:45:04.115 11182.115] link paired with: 10.0.108.50:50012
XComm Log: [14:45:04.215 11182.215] uplink state was/is: TIMEOUT ACTIVE
Then another timeout occurs on the same IP (10.0.108.50) leading to what I believe is the ELZ mission (“GoTo m,w 2  0“)
Edit: After looking at the GCS event log (event.txt) I believe the alternate landing zone was selected by the operator. (Time: 017:56.547  LZ Selection: : Alternate)
XComm Log: [14:51:25.760 11563.760] ap link fault: local rx okay ap rx bad
XComm Log: [14:51:25.761 11563.762] ap link fault during transition/fw flight
XComm Log: [14:52:18.572 11616.572] link timeout
XComm Log: [14:52:18.573 11616.573] uplink state was/is: ACTIVE TIMEOUT
XComm Log: [14:53:25.372 11683.372] ap dbg: LOS!
XComm Log: [14:53:28.674 11686.674] ping paired with: 10.0.108.50:50020
XComm Log: [14:53:30.025 11688.025] config paired with: 10.0.108.50:50201
XComm Log: [14:53:30.026 11688.026] link paired with: 10.0.108.50:50012
XComm Log: [14:53:30.107 11688.107] uplink state was/is: TIMEOUT ACTIVE
XComm Log: [14:53:30.108 11688.109] connect forced sla reset
XComm Log: [14:53:31.109 11689.109] DebugMsg video reinit
XComm Log: [14:53:31.110 11689.110] DebugMsg video 0 -> video any
XComm Log: [14:53:31.111 11689.111] DebugMsg video 2 -> video 1
XComm Log: [14:53:31.112 11689.112] event FLT_EVENT_CONNECT
XComm Log: [14:53:32.166 11690.166] ap link restored
XComm Log: [14:53:44.054 11702.054] GoTo m,w 2  0
XComm Log: [14:53:44.570 11702.570] GoTo m,w 2  0
XComm Log: [14:53:45.485 11703.485] GoTo m,w 2  0
XComm Log: [14:53:46.134 11704.134] GoTo m,w 2  0
XComm Log: [14:53:46.690 11704.690] GoTo m,w 2  0
XComm Log: [14:53:47.055 11705.055] GoTo m,w 2  0
XComm Log: [14:53:47.397 11705.397] GoTo m,w 2  0
XComm Log: [14:53:47.793 11705.793] GoTo m,w 2  0
XComm Log: [14:53:48.158 11706.158] GoTo m,w 2  0
XComm Log: [14:53:48.543 11706.543] GoTo m,w 2  0
XComm Log: [14:53:48.886 11706.886] GoTo m,w 2  0
XComm Log: [14:58:23.815 11981.815] landing pattern detected

### Pat Wells, 2024-10-14

@David Grosher & @Jason Scherer any updates on this since Jason’s last comment?

### Scott Whitney, 2024-11-01

@Pat Wells @David Grosher - regarding item #3 above this delay is an expected behavior. 

From Mike:
Each ethernet port has a unique IP address. Suppose the IP for port 1 is 10.10.10.1 and port 2 is 10.10.10.2.
When the cable was disconnected, the vehicle detected that it lost link with the GCS at IP address 10.10.10.1. It then started waiting for the GCS at IP address 10.10.10.1 to reconnect. During this time the vehicle would not allow connections from other GCSs (specifically the one at IP address 10.10.10.2).
When the vehcile eventually. timed out on the connection, it then allow the GCS at IP address 10.10.10.2 to connect.,
The vehicle could not tell that it was the same GCS trying to reconnect. It thought it was another GCS trying to take control.
In a handoff, which is what this was, the GCS must manually disconnect from the vehicle, and then reconnect.,
Switching Ethernet ports while connected to a vehicle is not a supported operation.

### Pat Wells, 2024-11-07

@Scott Whitney @David Grosher @Jason Scherer 
Can we move this forward and close out with a customer report?

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

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| V530 Landing While On the Ground.MOV | video | 23094 | 2024-08-22 | listed only |
| V530 Pauses on Launch.mp4 | video | 10911 | 2024-08-22 | listed only |
| V530 RTB Commanded (1).MOV | video | 66276 | 2024-08-22 | listed only |
| V530 RTB Commanded.MOV | video | 66276 | 2024-08-22 | listed only |
| T95_V530_240822_151625_pack.zip | archive | 1849 | 2024-08-23 | listed only |
| [VXE-530 Anomalies.pdf](attachments/30002_VXE-530%20Anomalies.pdf.md) | pdf | 524 | 2025-06-18 | converted |
