# VXEP-1685: VXE 942 Lost comms after 21 minutes in flight, reestablished control but Reconnecting never went away

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2026-01-29
- **Updated:** 2026-07-13
- **Resolved:** 2026-07-13
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Michael Lindsay
- **Creator:** Alexander Alan Arnold
- **Labels:** EAASSET, Weekly-incident-tracker
- **Links:** is fixed by OGCS-526 (Websocket Auth Refresh Causes False 'Reconnecting...' Alert)
- **Customer:** EAASSET, EA_Asset, Edge_Asset
- **Vehicle Tail Number:** VXE 942
- **Vehicle Configuration:** ADV NAV w OGCS Standard Battery, E140G2Z w prototype mount, NEW ADP
- **Corrective Action:** Software fix in OGCS 1.4.0
- **Plan:** Implement a fix in the next OGCS release, 1.4.0
- **Issue Status:** Root cause identified, fix in progress.
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

While Operating VXE 942 utilizing OGCS 1.3.3 the aircraft lost connection 21 minutes into the flight but I was still receiving updates from the VXE. After approximately 4 minutes in the Lost Comms Mission, I commanded the aircraft to a waypoint, and the vehicle accepted the command. 
Gimbal and SA feed were disconnected shortly after takeoff to improve C2 with the vehicle.

After seeing the vehicle respond to commands we decided to stay in mission orbit until the airspace was clear. The vehicle descended and landed without issue but reconnecting never updated to in control. 

After landing I refreshed the web page and the control status returned. Due to the C2 issues and RF problems in flight I did not refresh the page. While in flight I attempted to log in from another GCS but never got to the log in screen. 

Attached AAR, Wireshark and OBS Capture( I will upload OBS Capture Back at hotel)

## Root Cause

Logic error in OGCS causing it to show ‘Reconnecting…’ and not send Heartbeats to the VSM despite having a good connection.

## Comments (8)

### Alexander Alan Arnold, 2026-01-29

@Craig Burton @Ted Trowbridge @Cody Smisek 
FYSA

### Cody Smisek, 2026-01-29

just to get it out of the way. in the event anyone stumbles upon “v12.8 fault” in the xcomm logs and wonders what is going on, this is related to the heated pitot and while not desired, is not unexpected at this point in time. xcomm 12v has 3A limit set in configs, we are tripping that limit when the heater kicks on at times.

### Craig Burton, 2026-01-29

From the VSM’s info log, the 1 Hz periodic heartbeat stopped entirely at 14:51:02 (22:51:02 UTC) and never resumed.  Even though the VSM continued to receive operator requests through OGCS, like the upload of waypoints and go-to’s, the absence of the heartbeats triggered the VSM’s link loss logic.
grep -ai "cucs auth" vsm-info.01.29.2026 :
14:50:56.562875:  cucs_req        0x1BEA0BAE -> 0xFFFFFFFF t=0 CUCS Authorisation Request (#1) | Req n/a
14:50:58.386564:  cucs_req        0x1BEA0BAE -> 0xFFFFFFFF t=0 CUCS Authorisation Request (#1) | Req n/a
14:51:00.216287:  cucs_req        0x1BEA0BAE -> 0xFFFFFFFF t=0 CUCS Authorisation Request (#1) | Req n/a
14:51:00.217543:  vsm_resp        0x000003AE -> 0xEAFFFFFF Multicast Cucs Authorization Report (#16319) | CUCSID:0x1BEA0BAE LOI 255
14:51:01.393322:  cucs_req        0x1BEA0BAE -> 0xFFFFFFFF t=0 CUCS Authorisation Request (#1) | Req n/a
14:51:02.416055:  cucs_req        0x1BEA0BAE -> 0xFFFFFFFF t=0 CUCS Authorisation Request (#1) | Req n/a

The CUCS logs confirm.   grep -ai heart cucs* :

cucs-0x1BEA0BAE-t942-u1-info.01.29.2026:22:50:39.344246:  auth            MulticastCucsAuthorizationReportOperation To=0xEAFFFFFF AuthorizedLoi=255 AuthorizedCucs=0x1BEA0BAE ConnectionStatus=3 LastHeartbeatTimestamp=1769727039.342776 TimeStamp=1769727039.343410
cucs-0x1BEA0BAE-t942-u1-info.01.29.2026:22:50:50.190044:  auth            MulticastCucsAuthorizationReportOperation To=0xEAFFFFFF AuthorizedLoi=255 AuthorizedCucs=0x1BEA0BAE ConnectionStatus=3 LastHeartbeatTimestamp=1769727050.188074 TimeStamp=1769727050.188688
cucs-0x1BEA0BAE-t942-u1-info.01.29.2026:22:51:00.218655:  auth            MulticastCucsAuthorizationReportOperation To=0xEAFFFFFF AuthorizedLoi=255 AuthorizedCucs=0x1BEA0BAE ConnectionStatus=3 LastHeartbeatTimestamp=1769727060.216985 TimeStamp=1769727060.217594

cucs-event.01.29.2026:23:01:00.236956:  auth            VSM is reporting 0x1BEA0BAE has not sent a heartbeat in 600.019277 seconds, forgetting and deleting state.

### Alexander Alan Arnold, 2026-01-29

If I see this issue again is best practice to refresh the webpage? @Craig Burton

### Craig Burton, 2026-01-29

@Alexander Alan Arnold , I don’t think it would help in this case; I believe we have a real issue to track down.  Did you, by chance, power up a second vehicle on the network at approximately 14:51:02?  I ask because LM is testing MUAVs and reported an issue this evening that sounds eerily similar:
| With 1 GCS 4200 radio, 6 Stalkers, and 4 additional 4200 radios on the network, all AVs showed up in VCSi, all OGCS windows opened quickly, but all OGCS windows showed "Reconnecting" and none connected.  With only one Stalker on the network, everything worked as expected.  As additional Stalkers were added one at a time things really slowed down.  With more than 3 Stalker powered up, OGCS would take a long time to connect (as much as 3 minutes).  Authorizing a Request from VCSi could take 30 seconds.  Open Launch Wizard and it could take 3 minutes for the Logs page to open, then more than 3 minutes to Reset Vehicle.  OGCS often went from You Are In Control to Reconnecting.  When Releasing control to VCSi, OGCS would sometime say No GCS Has Control while VCSi said Control.  With 6 Stalkers powered up, it took a LONG time (~10 minutes) to get to the Calibration screen and could not complete Calibration (just a spinny wheel).  Before powering up the 6th Stalker, all but one Payload was turned off.  No improvement was observed. |

FYSA @Ted Trowbridge

### Ted Trowbridge, 2026-01-30

Based on the observed behavior (telemetry was streaming, the vehicle was moving on the map, and the UI was populating), we know the vehicle was actually connected. High-rate telemetry updates are received via WebSocket, confirming that connection was active. Commands like "go to waypoint" and flight mode changes are issued as atomic REST/HTTP requests, and those were also working. The "Reconnecting..." spinner was incorrect and operators made the correct decision to ignore it and continue flight.
The logs indicate that around the time Craig noted heartbeats stopped, there were two WebSocket disconnections. The first was due to an auth token expiring, which was successfully refreshed and reconnected after ~5 seconds. One minute later, at 2026-01-29T22:51:01.796Z, there was an abnormal WebSocket disconnect which corresponds exactly to heartbeats stopping.
Analysis of the code indicates the auth refresh logic is flawed, causing two WebSocket connections to be opened rather than reusing the existing connection. When one of the two connections closes, the system incorrectly reports a full disconnection despite the other remaining open and receiving telemetry. This is a logic error and synchronization issue.  I’ve created https://jenaero.atlassian.net/browse/OGCS-526 to reproduce and fix the issue.
Refreshing the page would likely have resolved the issue, but it’s understandable why that was avoided because it could’ve exacerbated comms issue - and we specifically warn not to via an OGCS dialog.
@Alexander Alan Arnold @Craig Burton @Cody Smisek @David Grosher

### Ted Trowbridge, 2026-01-30

@Alexander Alan Arnold for this exact issue – where it says ‘Reconnecting…’ despite the vehicle moving on the map and UI updating – yes, a page refresh should resolve it.

### Jackson Riley Curvin, 2026-07-13

Issue resolved in 1.4.0

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 2026-01-29 15-03-02.mkv | video | 118056 | 2026-01-29 | listed only |
| AAR_V942_20260129T231620Z.zip | archive | 16422 | 2026-01-29 | listed only |
| VXE942_NewSilvus_Config_OGCS_Reconnecting_Issue.pcapng | other | 54775 | 2026-01-29 | listed only |
