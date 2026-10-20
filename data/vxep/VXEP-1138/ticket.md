# VXEP-1138: Investigate & Resolve AHRS GPS Timestamp Intermittency

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-03-13
- **Updated:** 2025-04-17
- **Resolved:** 2025-04-17
- **Reporter:** Tobi Ogunro
- **Assignee:** Kurt Burian
- **Creator:** Tobi Ogunro
- **Parent:** VXEP-1008 Mod Payload A-Kit Gen 2 design/release/test (Long term issue resolution)
- **Leadership Stakeholder:** Greg Fryer
- **Issue Status:** Per @Kurt Burian, waiting to release v30108
- **Tech Lead:** Kurt Burian

## Description

The AHRS unit is intermittently failing to send GPS data in the required 1PPS format, preventing Bloodhound from using the data. The SBG unit does not consistently transmit in a 1PPS format, and inconsistencies have been reported.

## Plan

**Action Items:**

**1. Investigate Root Cause of GPS Timestamp Issue**

- Analyze SBG unit behavior to determine why some units work while others do not.
- Identify if the issue is due to configuration settings, software/firmware versions, or hardware inconsistencies.
- Compare the working vs. non-working SBG units to pinpoint discrepancies.

**2. Gather & Review Logs from Huntsville FLoPS Team**

- Coordinate with the FLoPS team in Huntsville to obtain logs from the faulty SBG units.
- Analyze the logs to identify patterns, errors, or deviations from expected GPS transmission.

**3. Determine Corrective Action & Implementation Plan**

- If the issue is configuration-related, define the correct settings and procedures for resolution.
- If firmware/software updates are required, identify the versioning discrepancies and necessary patches.
- Develop and test a proposed solution to validate the fix.

**4. Documentation & Communication**

- Document findings and corrective actions for future troubleshooting.
- Update relevant BOMs, manuals, and training materials if changes are required.
- Communicate resolution steps to all stakeholders, including Huntsville FLoPS Team and production teams.

**Deliverables:**

Root cause analysis of GPS timestamp intermittencyLogs from Huntsville FLoPS Team reviewed and analyzedCorrective actions defined and testedUpdates to documentation, BOMs, and manuals as needed

## Comments (7)

### Tobi Ogunro, 2025-03-13

@Alexander Alan Arnold & @Kurt Burian Here is the ticket for the AHRS GPS Timestamp Intermittency issue. We need the Huntsville team to provide logs from the bad units so we can identify the root cause.

### Tobi Ogunro, 2025-03-27

@Alexander Alan Arnold  & @Kurt Burian Did you guys take a look at this?

### Kurt Burian, 2025-03-28

@Tobi Ogunro I haven't had a chance to tackle this yet. I believe we were hoping to get the downloaded AHRS config. This would be the v30106 on the MAIM? I can try poking around a bit next week.

### Kurt Burian, 2025-04-04

Correction. I found something new.
 
The AHRS spec calls out a feature that is unsupported with the version of AHRS firmware we have been running. My AHRS initialization code sets the v2 supported PPM mode, but likely the incorrect pulse duration. The pulse duration was not specified in the spec and I assumed the original implementation was correct, which sets it to 1us rather than what I assume is correct, 500000us(50% duty).
 
- To fix the customer issue, I would connect with the control center and set the mode to PPS and the duration to 500000us. I use the latest control center, 5.0.535. Do not zero-out the GPS and IMU lever arm, the firmware reinitializes the AHRS if those are detected as (0,0,0) and your changes will be reset next power up.
- “Evt” is the estimated timestamp error. It doesn’t look like the current firmware will omit that field prior to having a fix. This is an omission on our part, we simply forward what the AHRS sends, so I don’t think it’s a good indicator of the PPS working correctly.

 
- I should immediately release a fix for the code. This will involve adding a feature to check the PPS setting and correct it if found in error.

 
- This will need to be applied to both Gen 2 and Gen 3 units, as both the old stuff getting the updated as well as what’s staged for delivery will be incorrect.

 
- I would change the production AHRS config to have the final values, lever arms included and change DIRECT_PPS to PPS, 500000us. This is optional as the way it exists currently, we overwrite reguardless.  Optional

 
- We have the imu/gps lever arms in the production config set as 0,0,0 so my firmware overwrites the config on power up as it assumes its uninitialized. This doesn’t matter for the below issue, but the value we set, DIRECT_PPS, is not supported in v2 of the AHRS firmware, which we run.

### Kurt Burian, 2025-04-05

Learned something new with the AHRS config on Friday. The initial date/time is set to Jan 2015 I believe. In the noisy GPS environment like the software QA area, the unit has a very difficult time getting a first fix. Additionally, it seems like the AHRS does not preserve the last known position/time on resets so this does not improve after the first use from the factory.
I recommend we change the initial date on the production config.

### Tobi Ogunro, 2025-04-11

@Jo Brown This software needs to be placed in egg MAIM_v30108 (SW that fixes the issue specified in this ticket)
FYSA @Kurt Burian @Alexander Alan Arnold

### Alexander Alan Arnold, 2025-04-14

@Tobi Ogunro I am just a reporter/observer on this issue. Kurt has done all the leg work investigating so if he is saying that the SW fixes the issue and its been tested and verified then I would say it has been resolved

## Attachments (0)
