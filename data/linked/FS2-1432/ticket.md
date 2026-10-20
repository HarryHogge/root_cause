# FS2-1432: v604 Crash investigation

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-02-08
- **Updated:** 2024-03-19
- **Resolved:** 2024-03-19
- **Reporter:** Scott Hunter
- **Assignee:** Scott Hunter
- **Creator:** Scott Hunter
- **Fix versions:** Release 6.3.4
- **Parent:** FS2-752 Vehicle Incident Investigation Support
- **Links:** relates to VXEP-263 (VXE-604 crash during SCO/ Flight test); relates to FS2-1406 (v604 Crash investigation); relates to FS2-1419 (Test operation of RTOS to rule in or out processor loading issues for AV604 mishap.); relates to FS2-1568 (v604 fix implementation - Priority 3 inheritance by datalogger)
- **Epic Link:** FS2-752
- **Sprint:** FS2 Sprint 13, FS2 Sprint 14, FS2 Sprint 15

## Comments (3)

### Scott Hunter, 2024-02-08

Raw notes - 
Questions:
- Why doesn't imuSrc seem to work?
- Doesn't match what's in the configuration file.
- Where is the mag declared bad?
- Where is this fallback?
- Is there any AddMessage for swapping mag?
- Is there any AddMessage for mag at startup?

 
For some reason the "case SOURCE_QUERY" isn't being called but "case HEALTH/SENSOR_INIT/SENSOR_POLL" are.
 
None of the mpu9250 stuff is called when external mag is enabled, but is called when external mag is 0 in the config
Do we see any dropouts in the data indicating trouble with the interface or CPU?
I don't see anybody using IsExternalMagFallback() for any kind of fallback. Info about the health of the external mag may be sent to XCOMM in the mavlink "control_sensors_health". That may be the health flag that's logged by XCOMM but we don't know for sure. We should do a better job of logging when something has a fault and what the fault is. XCOMM logs a better fault but only if the VT has failed during climb. It's level triggered so it would get logged if the fault exists before climbing.  Seems important to log any time the fault goes high. (ApmParser.cpp:2963)
The data doesn't seem to be skipping or stuck in the csv file. We might have a clue in the new diagnostics if this is the CPU climbing because the sensor is in trouble. I2C?
I don't see any evidence of a fallback on the mag sensor. You get what you get from config - this is testable though

### Scott Hunter, 2024-02-13

See https://jenaero.atlassian.net/browse/FS2-1420 for some info regarding cpu load testing. Bottom line is there doesn’t appear to be a problem where extra CPU load causes trouble with the mag sensors. It seems more likely trouble with the mag sensor caused the extra cpu load

### Scott Hunter, 2024-02-22

@Eric Brewer - FYI
Findings 2/21/24: 
- The code the system uses to track which mag sensor is in use doesn't appear to work. My testing with an Iron Bird configured HIL indicates the function GetMagSource() which calls GetSource(mag_server) always returns "0" because sptEntry() returns a null pointer whether sensor->privider is a 0 or 1. I was able to see sensor->provider change between 0 and 1 while debugging but the pointer was always reported as NULL. GetMagSource() is used to build up the imuSrc field in the log file. If the system were working the mag source would be a "3" (MAG_EXTERN) or "F" (MAG_HILSRC) rather than "0'.  “0” in those imuSrc bits indicates the value has not been set.
- The code that fails-over seemed to work in my testing when I hacked the raw sensor data to be out of range. The values required to cause a fail-over of the mag sensor look extreme.
- Recommendations so far
- Clean up the code mess 
- The flag that goes to XCOMM is a different calculation vs the code that's used to switch over in the VTOL. The internal switch-over code may be too lenient. We should use compatible logic.
- The XCOMM flag is based on the mags measurement compared to expected magnetic field for the area
- The internal flag is based on the raw sensor data being stuck or individual axes reading ~4 gauss (+/-2K counts) before being transposed, filtered and scaled
- Note:  
- Bx/By/Bz is the sensed magnetic field being used by the system. There's no data in the log file indicating which sensor that is.
- imuBx/By/Bz is the normalized Bx/By/Bz being used by the system.
- Evaluate the need (requirement) for logging better sensor health data
- Set up a lab test with a large magnet 
- Monitor flags
- Monitor data
- I suspect the internal sensor did NOT switch over in 604, I need to look at 406 
- Look at 406 data
- Look at other SCO flights.

## Attachments (0)
