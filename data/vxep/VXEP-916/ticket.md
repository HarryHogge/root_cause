# VXEP-916: VTOL Controller stopped talking during EMC emission ground tests (aircraft not radiated)

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-01-28
- **Updated:** 2026-03-02
- **Resolved:** 2025-05-19
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** TIQUILA, Weekly-incident-tracker
- **Links:** relates to ENG-3072 (VTOL Controller stopped talking during EMC emission ground tests (aircraft not radiated)); relates to FS2-2854 (Jason's Open Investigations)
- **Customer:** TIQUILA
- **Plan:** - Data review
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

From LM:
During EMC emissions testing, all 3 VTOL Controller froze. Motor Test and Instrument Panel went solid white; Sensors froze. Refreshed webpages to try to restore and got white screens. Did not get VTOL Controller page or login screen. Cycled power to VTOL Controller by disconnecting and reconnecting umbilical cord. Refreshed web pages and got VTOL Controller login screen in all 3 window. AAR T95_V478_20250122_140014 with FDR downloaded. AAR has lots of data because plane had been powered up for 20+ hours since last Reset. FDR took approximately 1 hours to download with 64 dB radio link, <2 dB interference, <10 Queue size, and <30% airtime.
Note: This test was not radiating the aircraft. They were measuring EMI from the aircraft. 
Initial Observations: 
- Multiple resets are in the file but no crash dumps. There was only ~6 hours in the longest run.
- Number of tasks created is , 346 due to a huge number of actuator overrides generated.
- Many Tasks inheriting priority that shouldn’t be:
- UTC Tick
- Energy
- HTTP Conn 1/2/3/4
- AGL Capture
- GPS Parse
- LL Detect
- CAN RX
- IMU Cycle
- Mavlink
- Datalogger
- Two Ethernet Phy interrupts in the last minute, which was unusual as there were only 25 total.

## Comments (11)

### David Grosher, 2025-01-28

@Pat Wells I assume that there should be 3 AARs for this incident, one from each vehicle.

### Pat Wells, 2025-01-28

@David Grosher only one was provided as per Garret’s comments on the 20 hours of run time.  
Would you like me to request the other two?

### David Grosher, 2025-01-28

@Pat Wells Unfortunately, since they power cycled the VTOL there is no crash dump. I’m not sure there will be much information there. Let me go through what we have for now.

### David Grosher, 2025-01-28

@Jason Scherer Interesting issue during testing with a lot of actuator overrides. Per the statement in sounds like there would have been a VTOL AP WDT but it isn’t in the data. They would have had the webpage open for quite a while.

### Jason Scherer, 2025-01-28

@David Grosher This initially made me think it could be SD card failure. I found this is the log “[04:40:52.267 21361.267] uri not found POST  /outtest.stm” which means the web file was not found. The 'outtest.stm file is the web page file for motor tests.
[embedded: image-20250128-222239.png]
However, given that this occurred on three separate VTOLs at the same time makes me think it’s not the hw. I noticed a lot of “Act Ovr” tasks have been run, and I’m thinking this may be more of a running out of system resources issue which would explain why the system didn’t crash. It simply lacked resources to respond to web requests (just a hunch).
Tagging @Scott Hunter for Trace expertise. He and I both found this set of data very interesting. I think we want to try recreating the steps that caused this behavior so we can better understand it. @Pat Wells would it be possible to get the procedure that was used for motor test? I assume it was as simple as using the webpages, but I don’t want to make bad assumptions.

### Pat Wells, 2025-01-28

@Jason Scherer request sent for details on motor test.

### Pat Wells, 2025-01-29

@Jason Scherer @David Grosher 
Here’s what came back from LM on the AAR’s and motor tests:

What other two AARs? When the VTOL Controller webpage windows froze, I produced one AAR.
I don’t remember exactly what tests we were doing when the VTOL Controller webpages froze, but immediately before my notes about the pages freezing is a note about completing the vertical and horizontal polarization RF measurements of the forward motor running at 50% throttle (with propeller blades, using Propulsion Test in the Jennings GCS software). After that, we measured at various receiver antenna positions while running the forward motor at 50% throttle (no blades, Jennings GCS Propulsion Test) and running the three working lift motors at 15% (1150 microseconds) (no blades, using the VTOL Controller/Motor Test webpage).

### Pat Wells, 2025-02-03

@David Grosher @Jason Scherer  Received the following clarification from LM:

During EMC testing, we were simultaneously monitoring three separate VTOL controller webpages: Instrument Panel, Motor Test, and Sensors. During one test we observed that all three VTOL controller windows were frozen. The Instrument Panel and Motor Test pages went all white. The Sensors page still showed data, but was not updating.

### David Grosher, 2025-05-19

@Pat Wells Is the customer tracking this? There is a massive electrical redesign that is part of the blk 35/40 design effort that will address some of this. I don’t think it makes sense to track here.

### Pat Wells, 2025-05-19

@David Grosher I agree tracking it here is no longer needed.

### David Grosher, 2025-05-19

These concerns are being addressed in electrical redesign that is part of the Blk 35/40 effort.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V748_250122_140014_pack.zip | archive | 35564 | 2025-01-28 | listed only |
| image-20250128-222239.png | image | 2 | 2025-01-28 | listed only |
