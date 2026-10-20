# FS2-4473: Investigate and Implement Detection and Handling of Stale Air Data in FW AP

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2026-04-09
- **Updated:** 2026-08-24
- **Resolved:** 2026-08-24
- **Reporter:** Scott Whitney
- **Assignee:** Ben Triplett
- **Creator:** Scott Whitney
- **Fix versions:** Release 6.7.1
- **Parent:** FS2-752 Vehicle Incident Investigation Support
- **Links:** relates to VXEP-1780 (VXE 864 Crash)
- **Epic Link:** FS2-752
- **Sprint:** FS2 Sprint 37, FS2 Sprint 38

## Description

Currently in progress: Investigation CA to detect stale air data and handle it appropriately in the Fixed Wing Autopilot (FW AP) firmware. This task involves analyzing the stale air data issue, developing detection mechanisms, and implementing handling strategies to improve system reliability and performance.

## Plan

Difficult to repro exactly. Currently in SG HIL sim setting airspeed to 52kt to match incident then soft reset XComm and log the results. Fixes in XComm and FW AP improve performance compared to baseline but are not definitive because I can’t repro the conditions that lead to the WDT reset, which is more problematic for the system than a simple soft reset. Had to modify the baseline code so that a soft reset acts more like a WDT reset when the soft reset is invoked in flight. Otherwise the system re-zeros the airspeed and baro alt data to match current in-flight conditions which guarantees a crash.
Results show approximately 300 foot drop in altitude with the baseline code and a 100 foot drop for the update.
Copilot summary of changes - XComm:
The XComm changes were concentrated in xcomm_202/can.c and a small supporting cleanup in xcomm_202/CrashState.c.
- The main functional fix was to stop re-establishing the remote-air autozero baseline on watchdog or software resets. In xcomm_202/can.c, airmagdataaz is now preserved across those reset types, which avoids a mid-flight step change in reported baro/q after XComm restarts.
- The CAN airdata path was hardened so version acquisition does not depend on the blocking config-request path. Instead of calling remoteConfigRequest() from the airdata receive handler, xcomm_202/can.c now sends a lightweight non-blocking version request at a low retry rate until can_ver is learned, and logs the learned version once when it first arrives.
- We removed dead XComm code by deleting the unused remoteConfigDump helper from xcomm_202/can.c, and updated the warning comment so it points specifically at remoteConfigRequest() as the blocking path to avoid in CAN dispatch.
- We cleaned up reviewability issues in the XComm changes: added braces around the conditional code we introduced, replaced the introduced magic numbers with named constants in xcomm_202/can.c, and braced the reset-cause helpers in xcomm_202/CrashState.c.

Copilot summary of changes - FW AP:
- In FW AP, the main functional changes were in fixed-wing-ap-6.7/Autopilot/hostintf.cpp and fixed-wing-ap-6.7/Autopilot/oloop.cpp. We also removed dead debug scaffolding from fixed-wing-ap-6.7/Autopilot/target.h and fixed-wing-ap-6.7/Autopilot/Vtol.cpp.
- In fixed-wing-ap-6.7/Autopilot/hostintf.cpp, the AP now only accepts remote-air packets when AIR_DATA_UPDATE is set. That means after an XComm reset, packets that do not yet contain a fresh air sample no longer overwrite the AP’s last-good remote airdata.
- In fixed-wing-ap-6.7/Autopilot/hostintf.cpp, remoteAirTime is now only refreshed when a truly fresh airdata sample arrives. This makes the stale-air timeout mean “no new airdata has arrived,” instead of “some packet came in.”
- In fixed-wing-ap-6.7/Autopilot/oloop.cpp, when remote airdata goes stale, the AP now raises an airspeed fault and supplies a bounded fallback estimated airspeed. That estimate comes from current airspeed if usable, otherwise GPS groundspeed, with a minimum floor of about 75% of cruise speed so the estimate does not collapse toward zero.
- Also in fixed-wing-ap-6.7/Autopilot/oloop.cpp, when fresh remote airdata resumes, the AP clears the airspeed fault and stops using the fallback estimate. So the AP can recover automatically once the remote-air stream is healthy again.
- The dead-code cleanup on the AP side removed old LAND_DEBUG and LAUNCH_DEBUG scaffolding from fixed-wing-ap-6.7/Autopilot/target.h and fixed-wing-ap-6.7/Autopilot/Vtol.cpp, plus a small cleanup of the related conditional logic in fixed-wing-ap-6.7/Autopilot/hostintf.cpp. That part was cleanup only, not a behavior change.
- The XComm and FW AP changes are designed to work together. XComm now avoids creating bad post-reset airdata by preserving the airdata zero baseline across watchdog/software resets and by reacquiring version/config without blocking CAN dispatch.
- The FW AP side then adds protection if XComm still resets or the remote-air stream drops out anyway. The AP ignores packets that are not marked as fresh airdata, detects when real airdata updates stop, falls back to a safer bounded airspeed estimate, and clears the fault once fresh samples resume. So XComm reduces the chance of bad data being produced, and FW AP reduces the chance of bad behavior if the data stream is interrupted or temporarily invalid.


Simulation results:
The current 6.7 code shows a substantial drop in altitude of over 300 ft on setting of the airspeed measurement to 52 ft/s and then soft-reset of the xcomm. The airspeed also spikes in response to the dive which is expected. Ignore the drop to the ground at the end - that is a result of permanently fixing the measured airspeed at 52 ft/s and is expected. 

[embedded: image-20260409-174313.png]
With the updates in place the air vehicle loses much less altitude and recovers more quickly:
[embedded: image-20260409-174500.png]
I had copilot examine the data logs from the incident and look for evidence that some of the more severe possible issues may have occurred during that flight (stale data leading to latched bad air data - especially due to old blocking call to get the airdata version), this is the summary: 

There is some evidence for it in the incident flight, but not enough to call it proven.
What supports it:
- After the WDT restart, the incident log shows CAN air data detected in xcomm_202/logs/T95_V937_260320_171552_pack_flightincident/T95_V937_260320_171552_xcevlog.txt.
- I do not see a corresponding AirData version: message in that restart window, and current code logs that when the version response is actually processed in xcomm_202/can.c.
- In your newer test logs, the healthy pattern is CAN air data detected followed almost immediately by AirData version: 0x3002, for example in xcomm_202/logs/T95_V101_260408_143620_pack_codeupdate/T95_V101_260408_143620_xc240816.t02.

What weakens it:
- The incident pack is old 4.72 logging, so it does not directly log can_ver stuck at 0.
- I also do not see repeated Failed to get AirData Version. Retrying... messages in the incident restart window, which would have made the case much stronger.

So the best answer is: yes, the incident flight has circumstantial evidence consistent with that happening, mainly “airdata detected but no visible version-learn event.” But it is not a smoking gun from the available logs.

## Comments (1)

### Pat Wells, 2026-08-11

@Ben Triplett  have there been any updates on this?  Is there a path forward with resources allocated?

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20260409-174313.png | image | 134 | 2026-04-09 | listed only |
| image-20260409-174500.png | image | 162 | 2026-04-09 | listed only |
