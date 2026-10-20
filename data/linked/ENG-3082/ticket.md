# ENG-3082: VXE-492 Fly away Camp Lejune

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-08-16
- **Updated:** 2025-06-02
- **Resolved:** 2023-08-31
- **Reporter:** Pat Wells
- **Assignee:** John Clark
- **Creator:** Pat Wells
- **Labels:** PMA_263
- **Links:** relates to FS2-725 (VIT2-343 VXE-492 Fly away Camp Lejune); relates to VXEP-43 (VXE-492 Flyaway Camp Lejune); relates to RMA-185 (VXE-492 231107 Full Aircraft "Fly Away")

## Description

From the customer:
1AUG2023
The Aircraft took off and climbed to its commanded altitude of 700ft as soon as it did, the AV lost connection over ETA-2. Sgt XX immediately checked the connections from the radio to the aircraft. When everything looked normal he tried to get a visual of the aircraft. He didn’t see it over ETA-2 and then checked the path of its recovery to see if it was attempting to land. When he didn't see it recovering the contractors with TALSA-E started pulling the logs and Sgt XX went to the aircraft's last known location and searched the woods to see if it decided to land immediately.
After the loss, Sgt XX set up a mobile GCS to attempt to get connection with the AV and drove on the roads around ETA-2, LZ Canary and the training areas north of Courthouse Bay with three other instructors. They drove around all of the ranges in and around the AV's last known direction of flight for approximately 5 hours. Meanwhile, the students got on line to search further on foot near the last known location of the AV. The next day (2 Aug), Sgt XX drove around Verona Loop for 2 hours, searching along each of the roads throughout the entirety of the training area without success locating the SUAS.

## Comments (15)

### Pat Wells, 2023-08-16

@Greg Fryer  please assign to an engineer or group

### Pat Wells, 2023-08-16

@David Grosher @Sam Miller

### Greg Fryer, 2023-08-16

@John Clark Please review (or have reviewed) the attached record ASAP.

### John Clark, 2023-08-16

| T95_V492_230801_071912_pack.zip |

If the above file is available it would be helpful. In C:\Users\Public\Documents\My GCS\After Action Reports
Also, gcs.ini would be helpful in C:\ProgramData\GCS\XEVTOLGCS\gcs.ini
@Pat Wells

### Pat Wells, 2023-08-18

@John Clark  I have requested the files from the customer.

### Pat Wells, 2023-08-21

[embedded: T95_V492_230801_071912_pack.zip][embedded: gcs.ini]
@John Clark attached additional files received from customer. @Michael Berger can you determine the lost comms configuration of this aircraft as discussed, from the gcs.ini and add it to this ticket, please?

### Daniel Lloyd, 2023-08-21

Just before the data from the aircraft stops the main battery drops by 3 volts.

### John Clark, 2023-08-22

@Michael Berger the gcs.ini for the flight is a part of T95_V492_230801_071912_pack.zip as well.

### Michael Berger, 2023-08-22

@John Clark Based on the GCS.ini file the vehicle was initially set to automatically execute its LOS mission.

[SETTINGS]
InitialLosRtbOverride=0

It is unlikely, but this could have been changed after GCS startup, the gcs.ini file only specifies the initial state.
If it was changed there would be a message in the EventLog.
```
EventLog("LOS RTB Override: ", m_LosRtbOverride ? "Enabled" : "Disabled");
```
note
m_LosRtbOverride=-0 means execute the LOS mission
m_LosRtbOverRide=1 means continue on the mission (don’t RTB).

### Daniel Lloyd, 2023-08-22

In any case the aircraft will return to land at the active landing pattern. The only difference is the path it takes to get there.

### John Clark, 2023-08-23

The aircraft reaches launch state 16 LCH_WAITSAFE and no more communications transpire. This may be a critical boundary that could be HIL tested.
Failed Flight:
[07:19:54.873] lch state: 16 LCH_WAITSAFE wait for command, end the launch
[07:19:54.882] lch timeout: 2
[07:19:54.952] vt ack safe or timeout, lch complete
[07:19:54.952] LaunchShouldFWLaunch now: 0
[07:19:54.953] LaunchShouldPitchAngle now: 0
[07:19:54.953] LaunchShouldFWPower now: 0
[07:19:54.960] VTOL MSG: Fixed wing flight
[07:19:56.929] false SAFE
[07:20:07.386] MissionRepaint
[07:20:07.386] TrackingLayerRepaint
[07:21:50.839] Show Caution(): Master Caution
[07:21:50.839] MessageBoxTop(): LOSS OF DOWNLINK WARNING
[07:21:52.789] Show Caution(): Master Caution
[07:22:35.950] Show Caution(): Master Caution
[07:22:35.950] MessageBoxTop(): LOSS OF DOWNLINK
Normal Flight:
[10:25:13.490] lch state: 16
[10:25:13.491] lch timeout: 2
[10:25:13.506] vt ack safe or timeout, lch complete
[10:25:13.506] LaunchShouldFWLaunch now: 0
[10:25:13.507] LaunchShouldPitchAngle now: 0
[10:25:13.507] LaunchShouldFWPower now: 0
[10:25:13.819] VTOL MSG: Fixed wing flight
[10:25:19.103] roll fault: 4071
[10:25:28.557] Changing active waypoint
[10:25:30.547] Refresh
[10:26:23.632] mci stopped receiving replies, reconnect required
[10:27:20.953] RefreshMap
[10:27:20.968] Refresh
[10:27:26.387] qsim:  reality   vtype95
[10:27:26.419] connections added
[10:27:26.489] power mode was, is: -1.000000, 1.000000
[10:27:26.490] power mode was, is: 1.000000, 4.000000
[10:27:26.490] Sim created
[10:27:26.491] sim set ref: 35400333, -120615929, 365, 297
[10:27:26.508] sim goto: 4, 0, 0, 0
[10:27:26.508] lch done: 345.000000, 300.000000
[10:27:26.512] power mode was, is: 4.000000, 1.000000
[10:27:26.652] power mode was, is: 1.000000, 5.000000
[10:27:28.166] TrackingLayerRepaint
[10:27:30.401] TrackingLayerRepaint
[10:27:30.445] Refresh
[10:27:36.901] Verify mission...
[10:27:36.901] Mission DB in vehicle verified

### John Clark, 2023-08-23

https://jenaero.sharepoint.com/:p:/r/sites/EngineeringTeam/Shared%20Documents/General/Vehicle%20Incidents/VIT2-343/VXE492%20Investigation.pptx?d=w2f0293a576b7427185d7009846324f0f&csf=1&web=1&e=bsHGUD 
Report included here.

### Cameron Chapman, 2023-08-24

linking subtasks to parent test

### Cameron Chapman, 2023-08-24

Linking subtasks to parent.

### Greg Fryer, 2023-08-31

Closed, no further action possible. Problem ticket moving to Bermuda Triangle.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [1AUG23 AV 492 Loss of Link Incident.docx](attachments/15882_1AUG23%20AV%20492%20Loss%20of%20Link%20Incident.docx.md) | docx | 3593 | 2023-08-16 | converted |
| VXE492.zip | archive | 258 | 2023-08-16 | listed only |
| T95_V492_230801_071912_pack.zip | archive | 142 | 2023-08-21 | listed only |
| gcs.ini | other | 55 | 2023-08-21 | listed only |
