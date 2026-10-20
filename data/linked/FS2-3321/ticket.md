# FS2-3321: VXE-541 Investigation: Failed to perform proper landing sequence actions

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-06-02
- **Updated:** 2025-10-20
- **Resolved:** 2025-08-12
- **Reporter:** Scott Whitney
- **Assignee:** Logan Wright
- **Creator:** Scott Whitney
- **Links:** relates to VXEP-1278 (VXE-541 Failed to perform proper landing sequence actions, resulting in the aircraft crashing into the ground.)
- **Sprint:** FS2 Sprint 33, FS2 Sprint 34

## Description

VXE-541 Failed to perform proper landing sequence actions, resulting in the aircraft crashing into the ground.
Investigate artifacts in https://jenaero.atlassian.net/browse/VXEP-1278

## Comments (16)

### Logan Wright, 2025-06-03

@Scott Whitney - Here is what I’ve compiled from the original 541 crash report!
Log files zip folder:
- [embedded: CrashLogs541.zip]

Sensor plots:
[embedded: crash_data_541.png]
Voltage and current plots are as reported by VTOL AP while most other sensor readings are from FWAP. I also included yaw/pitch/roll diagrams to demonstrate discrepancy between FWAP and VTOL AP measurements, though you can see that in their limits, the plots approach the same values (albeit the scaling is different). Altitude climbs continuously and never falls which is actually agreed on by all altitude measurements reported by both VTOL AP and FWAP (not shown). GPS satellite count is shown in the bottom right and that fluctuates quite a bit.
Discrepancy for Y/P/R out:
- It seems plausible that if the IMU were flipped over one of its axes by 180 degrees, we would see exactly two euler angles each scaled by a factor of -1. Depending on how the attitude is computed, relative accelerometer readings (if reversed) may show opposite rates of euler angles.

### Logan Wright, 2025-06-03

@Logan Wright According to the logs from XCOMM which Dave G found to show the attitude fault by the VTOL system, we should see this failure at 1 hour, 3 mins, and 40 seconds from bootup time (CpuTime in xcomm logs), so the red dashed bars represent that instant when we should be seeing something odd (from the sensors' end of the system).

### Scott Whitney, 2025-06-04

Thanks @Logan Wright 
FYSA: @David Grosher

### David Grosher, 2025-06-04

@Logan Wright The attitude fault is the last thing that happens and is almost certainly the result of a previous failure. I think the link fault that occurs earlier highlights some form of communication error that might expose a weakness in the landing sequence state machine resulting in the Lift system failing to start and the fixed wing system to stop exerting control on the system (hypothesized based on the error description). I think we need to look into the different comms buses when the link fails and then evaluate next steps. 

Also, the lack of satellites seems like another potential issue. Was this system exposed to jamming, if so, could there have been communications jamming or directed energy.

Also, it seems like there were a number of low power and differential power errors, we need to track this down. Is it an electrical issue or is it driven by the lack of fix in the GNSS system. Also, we should look at the update rate of the GNSS system, we have seen this cause issues in the past if it is at an unexpected rate.

### Logan Wright, 2025-06-04

@David Grosher I will attempt to address those points. To get GNSS update rates, can I refer to our current builds for that info? Or have we intro’d GNSS rate changes in the code base since then? If we have access to 541, I think it’d be helpful to directly extract configs and additional AARs to see if this has been happening behind the scenes without flagging us/the user.

### David Grosher, 2025-06-04

@Logan Wright The posRate and VelRate from the VTOL datalog will indicate received updates from the receiver. There was an issue in 6.2.9 that led to some issues here. 


[embedded: image-20250605-002352.png]

### Logan Wright, 2025-06-05

@David Grosher Based on the plots, looks like our rates were ok within the interval between the first and last ap link faults in the xcomm logs (between the red bars). I will continue exploring alternate paths.
- The first ap link fault was logged at ~42 mins and 35 seconds with the last one at ~1 hr 4 mins and 40 seconds in xcomm logs.

[embedded: crash_plots_541.png]

### David Grosher, 2025-06-05

@Logan Wright I would look into the GPS issues and the Low power issues during VTOL transition.  It seems like there was possibly an issue properly aborting.

### David Grosher, 2025-06-10

@Logan Wright @Scott Whitney We will need a report for this incident. I also don’t think we have found the root cause. 

The following in the VTOL Event log looks as though an abort was triggered by the FW AP but did not succeed. 
[10:38:24.470 3874.470] host vtol state was, is: APVTOL_LANDPREP APVTOL_TRANSITION
[10:38:45.971 3895.971] MC safe 1
[10:38:47.982 3897.982] host vtol state was, is: APVTOL_TRANSITION APVTOL_FWFLIGHT
Based on the XCOMM log it seems that there were a number of power faults. 

We should look at the airspeed calibration, the lack of GPS satellites, whether the attitudes from each AP match during transition, the power system and whether the power draw is in line with the throttle commands.

### Logan Wright, 2025-06-10

I worked a couple hours on this today. Will continue tomorrow. Need guidance on where to find commanded/executed throttle levels in order to match up the plot with current draw. Lat/lon seems to have been either erased and set to zeros in the xcomm datalogs or they just weren’t receiving data from the gps. I found that there was a period of ~80 seconds with nSats=0 which is when the fault occurred (according to the reported time stamps from the xcomm and vtol event logs). This period of 0 sats may also be an artifact of the low logging rate during flight (0.1 Hz) as the vehicle may have had comms in between samples, but I don’t know of any way to confirm this. I find it odd how stable the euler angles are at the red line which is where the attitude faults caused a vtol transition abort. I’ll include what I’ve been looking at below.
[embedded: 541_investigation_data.png]

### Jason Scherer, 2025-06-19

@Connor Peebles Not sure if you are working this one or not, but we need some HW team input regarding HLB voltage/current levels during landing.
Graphs below are from XCL00123.csv, I’ll take a look at VTOL data next.
Lift system did not pull expected power during landing. Current levels remain under 5 amps until the end. Could be a loose power connection to the HLB? Based on the lower power consumption (500W threshold) and big difference in throttle values (diff .5 I believe) the landing abort was activated as expected. The abort was a reaction to the faulty lift system.
[embedded: image-20250619-202318.png]
zooming out on the current graph you can see that the expected current levels (180A) did occur at the end (too late?).
[embedded: image-20250619-202707.png]
@Logan Wright @David Grosher FYSA

### Jason Scherer, 2025-06-19

VTOL data matches XComm data. 
VTOL Log: VTL00137.csv
[embedded: image-20250619-210110.png]

### Connor Peebles, 2025-06-20

@Jason Scherer It does seem like a lift ESC problem in my experience

### Logan Wright, 2025-06-25

Worked with Jason S to create some more plots for the investigation. I included a slide in his investigation report to address concerns given in the original task. Seems like Jason has rooted out that the cause is most likely related to hardware - @Scott Whitney

### Logan Wright, 2025-08-12

Thanks to Jason Scherer, wrapped up efforts on this awhile ago. Just updating now

### Steve Gonzales, 2025-10-20

@Logan Wright Hi, do you know where the center wing is for this one?  it is missing in the case?

## Attachments (9)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| CrashLogs541.zip | archive | 1309 | 2025-06-03 | listed only |
| crash_data_541.png | image | 184 | 2025-06-03 | listed only |
| image-20250605-002352.png | image | 47 | 2025-06-04 | listed only |
| crash_plots_541.png | image | 134 | 2025-06-05 | listed only |
| 541_investigation_data (d51251f3-0a54-45cc-86d8-7dba7708dcc4).png | image | 148 | 2025-06-10 | listed only |
| 557cb241-34a1-45f0-8c57-81ab6941bbab.png | image | 99 | 2025-06-19 | listed only |
| image-20250619-202318.png | image | 124 | 2025-06-19 | listed only |
| image-20250619-202707.png | image | 116 | 2025-06-19 | listed only |
| image-20250619-210110.png | image | 152 | 2025-06-19 | listed only |
