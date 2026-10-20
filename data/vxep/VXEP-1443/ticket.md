# VXEP-1443: VXE 676 NAVIGATION ERROR MAGNETOMETER FAULT

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-07-22
- **Updated:** 2026-03-02
- **Resolved:** 2026-01-20
- **Reporter:** Drew Hildreth
- **Assignee:** Eric Brewer
- **Creator:** Drew Hildreth
- **Labels:** TIQUILA, Weekly-incident-tracker
- **Customer:** TIQUILA
- **Vehicle Tail Number:** VXE-676
- **Problem Type:** Discovered Issue
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround
- **Program (Marquee):** TIQUILA

## Description

Incident Description:
 
The EAGLE Det was tasked on 15/07/25 by 20X to conduct a FIND mission at 0300 on 16/07/25.
The Detachment prepared the mission on the GCS and carried out preflight inspections, including Magnetometer Calibration due to the Aircraft being new and unused. All preflight conditions were met.
At 0240 on 16/07/25 the Detachment launched the EAGLE and preceded on task.
Met was good and well within limitations. 9.8Kts on the ground and between 15 and 18Kts in the air, clear and dry conditions.
The EAGLE flew West through a series of Waypoints and Orbits. Approximately 20 minutes into the flight, the GCS displayed a warning 'NAVIGATION ERROR MAGNETOMETER FAULT'. The Det acknowledged the warning screen and continued to monitor.
After a further two minutes the Det lost footage from the Payload and Link to the Aircraft. Distance from GCS was approximately 8Km, well within range of the Short-Range Antenna.
For approximately 3 minutes the Det did not have control of the Aircraft. During that period they started the fault find procedure and followed the EP and initially raised the antenna to try regain link and line of sight.
When link was reestablished the Det discovered that the Aircraft had not followed the loss of link procedure (heading to and orbit and climbing to 1700ft). The Aircraft had continued West at 700ft, not what the commander had set in their mission plan. The Aircraft was now approximately 12Km away.
The Det under my direction commanded the Aircraft the RTB, which it preceded to do. During the flight back to our location, the Aircraft was flying erratically. Flying at excessive speeds, not maintaining on flight paths and crabbing excessively in Orbits.
Due to the excessive speeds and erratic flight, the decision was made to move the Primary Landing Zone outside the compound by 100m to ensure safety of troops on the ground.
The change was 'Sim and Sync' meaning all changes should be activated on the Aircraft. 
Just prior to recovering the Aircraft the GCS froze forcing the Commander to close and Restart the software, reconnecting, and downloading mission from the Aircraft. 
Once reconnected the Aircraft was then commanded to RTB. The Aircraft entered its landing pattern but still erratic, speeds of 60Kts and missing IP4 by approximately 300m before recovering by VTOL inside the compound, despite the Primary Landing Zone being moved.
Once recovered, the Det again tested the Magnetometer Calibration which appeared unstable. The Aircraft was stationary but the internal compass continued to deviate in its readings.
Due to the catalogue of errors, I as the Tac Commander made a decision to Isolate EAGLE 676 and complete a DASOR.

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The investigation should be split into the following sub investigations: 
- Magnetometer Performance - Likely a known issue on v6.3.4 fixed in v6.4
- Poor Flying Qualities
- Toggling between Dash and Cruise and in between values
- Flight path tracking
- Crabbed during Orbit
- Lost Comms
- Lost comms response
- Did not land at desired PLZ

See the notes for an initial investigation.

## Comments (14)

### David Grosher, 2025-07-22

The last flight appears to be in the datafiles VTL00073.csv and XCL00052.csv. And the last event logs.

### David Grosher, 2025-07-23

[embedded: Investigation 676.pdf]
Preliminary investigation.

### David Grosher, 2025-07-23

@Drew Hildreth Can you ask the customer for the Silvus radio configuration on the 2 radios.  I can see that comms were lost but they were generally in and out and seems like they might have been operating at reduced power.

### Drew Hildreth, 2025-08-04

@David Grosher Updated Pictures and additional information.

Basic Configuration:
Frequency (MHz): 2235
Bandwidth: 5 Mhz
Network ID: StalkerXE
Link Distance (meters): 20000
Total Transmit Power (requested): 38dBm/3.981 W
Routing Mode: Large Network


UA radio confiig
Frequency: 2205 Hz
Bandwidth: 5MHz
Network ID: StalkerXE
Link Distance: 20000
Total Transmit Power (requested): 38dBm/3.981 W
Routing Mode: Large Network

### Drew Hildreth, 2025-08-12

@David Grosher @Eric Brewer Good morning, Gents. I know we have a million things going on. This is the last I had on this Investiagtion. Dhruti has asked me to join her for a meeting in about hour and a half to discuss incident updates. has anything changed from the below?

1.The flying qualities with respect to both tracking and speed were the result of gusty wind conditions. 
- The mag warning is likely the result of issues that were fixed in v6.4 that make the Mag driver more robust in terms of rejecting bad data.
- The vehicle landed where its last received mission told it to. I’m not sure why the updated mission was not sent/received. Still looking into the GCS logs.
- It is unclear why comms were dropped at that range. the FSR team is trying to understand Silvus setup with the customer.

### Eric Brewer, 2025-08-12

@Drew Hildreth I don’t have anything formally written up on this but based upon the brief look at the logs I took a few weeks ago it appeared to me that the seemingly ‘erratic’ flying was due in large part to high winds.  The winds were close to the opreational limit, so that will lead to a few things:
- Airspeed command increasing/decreasing as the aircraft goes around an orbit - this logic designed to keep the ground speed above a certain threshold
- Aircraft heading changing during an orbit - this will happen naturally as the aircraft faces headwind/crosswind/tailwind around an orbit.

I won’t be able to get you something more formal until next week.

### Drew Hildreth, 2025-08-12

@Eric Brewer This helps. Thank you.

### David Grosher, 2025-08-12

@Drew Hildreth In addition to Eric’s comment, they need to upgrade to v6.4 for the best Magnetometer performance.

### David Grosher, 2025-08-12

Downgraded severity, there is no indication that any of the observed behaviors were flight critical. Still at 2 due to the potential unexpected LoS behavior.

### David Grosher, 2025-11-12

@Drew Hildreth This incident is very hard to close because of all of the different issues that the ticket has in it. My understanding is that at least a few of the issues in the list can be closed. I would suggest we split this and then deliver the report for closed issues and then pass the other issues to the relevant parties for further investigation. It is very hard to manage tickets with multiple different issues.

### David Grosher, 2026-01-14

@Eric Brewer Can you look at the mag portion of this incident? Thanks.

### Eric Brewer, 2026-01-15

@David Grosher I see two instances in the xcomm logs where the mag status goes invalid, about 10 and 15 minutes into flight.  There is not indication of this in the VTOL logs, but the log rates of both xcomm and vtol are low.  The mag bit here is what is tied to the stanag alert about mag fault.  The mag performance overall looks good (attitude/heading from the fw and vtol match relatively well as expected), so this is likely the momentary blip that was a known issue with this version of software.

Let me know if you need anything else.


[embedded: image-20260115-145714.png]

### Eric Brewer, 2026-01-15

@David Grosher quick correction to above - I do see two blips on the vtol data as well (I had accidentally plotted the wrong file before).
It seems a pretty good bet this is related to the known software issue with that version.

### David Grosher, 2026-01-15

@Drew Hildreth We believe this an instance of the mag issue resolved in v6.4 where invalid mag data wouldn’t be filtered out.  https://jenaero.atlassian.net/browse/FS2-2699

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 676_AAR_DATA.zip | archive | 59319 | 2025-07-22 | listed only |
| FW_ AAR Files 676.zip | archive | 1227 | 2025-07-23 | listed only |
| [Investigation 676.pdf](attachments/30908_Investigation%20676.pdf.md) | pdf | 388 | 2025-07-23 | converted |
| thumbnail_image001.png | image | 554 | 2025-08-04 | listed only |
| thumbnail_image003.jpg | image | 92 | 2025-08-04 | listed only |
| image-20260115-145714.png | image | 222 | 2026-01-15 | listed only |
