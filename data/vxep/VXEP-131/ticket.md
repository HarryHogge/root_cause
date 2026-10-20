# VXEP-131: VTOL AP acceptance criteria need specification to support automation.

- **Issue type:** Improvement
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-10-05
- **Updated:** 2025-09-25
- **Resolved:** 2025-09-25
- **Reporter:** Greg Fryer
- **Assignee:** Eric Brewer
- **Creator:** Greg Fryer
- **Labels:** Production-Priority, Rate#
- **Links:** is duplicated by ENG-2418 (Coordinate with Engineering to get clearly defined pass/fail criteria on the Red AP); is a child of ENG-2393 (Turntable Automation System (TAS)); relates to FS2-957 (Update magFit for production (DONE?)); relates to FS2-1027 (Check rotational rate precision specification for VTOL AP); relates to FS2-1028 (Identify specs for temperature and pressure of VTOL AP); relates to FS2-1029 (Update the accelerometer specification ); relates to FS2-1030 (Update the gyro specification); blocks ENG-2408 (Submit completed project to CCB for review); relates to ENG-2403 (Perform calibration verifications prior to release to production and CCB)
- **Part Number(s):** 1409P01D
- **Issue Status:** 2/8 AP waiting for SCO team to validate automated calibration.

## Description

Production is automating VTOL AP, which requires definitizaiton of the values in the process that are currently vague. 
Specifically:
- Rotational velocity is 15RPM +/- 0.5% which seem excessive. This has only been passing because the specified tool is a hand stop watch, so the actual precision is well below this anyway.
- “Reasonable values for pressure and temperature” - This is basically treated as a check for ridiculous values. My (Greg) suggestion is to integrate a weather sensor next to the setup that reports temp and pressure, and it needs to be within 5% of that.
- "Confirm that one of the axes is reading very close to 1g or -1g. Flip the jig onto the other two orthogonal faces, each time confirming the reading."   Better definition is needed for the 1g reading verification after completion.  This is effectively the final tolerance of the autopilot after calibrations are done.
- "With the rate table stopped, confirm that the roll and pitch gyro readings are within +/- 1.00 deg. Next, turn on the rate table and confirm that one of the axes is reading very close to 90deg/s or -90deg/s.  Same story as the accelerometer, the 90 deg/s reading needs to be given a tolerance.

## Comments (16)

### Greg Fryer, 2023-10-05

@David Grosher I put this in your name because it requires a check to determine what precision is actually needed, to set the looser but specific values. I think a couple hours of work is all this should take, and maybe enlist a little help to figure out how accurate the stop watch test is.

### Greg Fryer, 2023-10-05

@Trevor Gronner @Ryan Ferguson @Ryan Stafford FYI

### Greg Fryer, 2023-10-05

And, I should add - I attached a photo of the document Ryan made summarizing the testing done.

### Ryan Ferguson, 2023-10-05

The turntable rate is a point which warrants some better analysis.  Currently production isn’t using a stopwatch.  Instead they are using a stroboscope tied to the 60Hz of the power grid to get an even more precise measurement of turn rates.  If we want better than this we will likely be paying a lot to get a calibrated rate of turn sensor.

We also should determine if the temperature measurement even holds value.  The boards present a significant amount of heat which throws off the onboard temperature sensing, so I doubt it is presenting anything usable.  Our current check in production is basically verifying the temperature shows something other than 0.00 C.
I pulled some select elements from the TAS runlogs for reference when coming to this conclusion.  The temperature in the electronics shop this day was around 75 F (just an estimate, we have no sensing in the shop) which converts to approximately 24C.  The autopilots were reporting approximately 32C which is about 90 F.  It is worth noting the autopilot in position 3 is a known failure in the baro/temperature sensor.

------ Autopilot SN's in each position ------
Position 0 : Serial/Tail Number: APB-1-1207 / VC0001
Position 1 : Serial/Tail Number: APB-1-1222 / 123
Position 2 : Serial/Tail Number: APB-1-1280 / VC0001
Position 3 : Serial/Tail Number: APB-1-1217 / VC0001
Position 4 : Serial/Tail Number: APB-1-1290 / VC0001
Position 5 : Serial/Tail Number: APB-1-1228 / VC0001
Position 6 : Serial/Tail Number: APB-1-1126 / VC0001
Position 7 : Serial/Tail Number: APB-1-1162 / VC0001
Position 8 : Serial/Tail Number: APB-1-1216 / VC0001
===================================================
Uploading calinit file to autopilots...
 
Autopilot 0 responded to calinit file upload with 204
Autopilot 1 responded to calinit file upload with 204
Autopilot 2 responded to calinit file upload with 204
Autopilot 3 responded to calinit file upload with 204
Autopilot 4 responded to calinit file upload with 204
Autopilot 5 responded to calinit file upload with 204
Autopilot 6 responded to calinit file upload with 204
Autopilot 7 responded to calinit file upload with 204
Autopilot 8 responded to calinit file upload with 204
Completed boot and configuration of all APs in 109.8 seconds
Completed minimum boot delay for sensor readings.  Beginning baro checkouts...
AP 0 average baro reading: 1007.355 / ref 1013.25  Temp reading: 31.91 deg C
AP 1 average baro reading: 1008.054 / ref 1013.25  Temp reading: 32.92 deg C
AP 2 average baro reading: 1006.672 / ref 1013.25  Temp reading: 32.31 deg C
AP 3 average baro reading: 0.0 / ref 0.0  Temp reading: 0.0 deg C
AP 4 average baro reading: 1007.647 / ref 1013.25  Temp reading: 34.12 deg C
AP 5 average baro reading: 1007.36 / ref 1013.25  Temp reading: 34.08 deg C
AP 6 average baro reading: 1007.325 / ref 1013.25  Temp reading: 31.64 deg C
AP 7 average baro reading: 1007.216 / ref 1013.25  Temp reading: 32.59 deg C
AP 8 average baro reading: 1007.239 / ref 1013.25  Temp reading: 32.14 deg C

### Greg Fryer, 2023-10-06

@David Grosher Need to include the MagFit.exe work here. I was going to add it, but heard you may have had it already somewhere and didn’t want to duplicate. Can you make that task and link?

### Ryan Ferguson, 2023-10-06

I added a couple other values to the ticket which weren’t captured originally when the ticket was created but will need definition.    
@Greg Fryer Can you confirm this will be in the next sprint?

### Cameron Chapman, 2023-10-13

@David Grosher , could you please create linked tasks and estimate hours for the FW portions of these requests? We would like to consider them for the next VXE sprint.

### Ryan Ferguson, 2023-10-16

When this task gets kicked off please let me know.  There are some nuances to how the Judge Database will interpret these values which I’d like to discuss with the responsible engineer before starting work.

### Ryan Ferguson, 2023-10-20

Today I finished the turn rate sensor for the TAS.  This is a very simplistic device consisting of a microswitch and a Pi Pico programmed to measure the time between presses and convert that into a turn rate which is sent back to the TAS.  To test it, I set up the turntable at 90 deg/s (15 RPM) using the stroboscope.  I tuned it until the lines didn’t walk more than 1 degree over a 10 second period.  I left the system to run for 5 minutes, gathering the min/max/average for the whole period.  Over that period, the turn rate sensor captured the following results in RPM: 
Min: 14.9925  Avg: 14.9997  Max: 15.00375

[embedded file]

Below is a graph of the turn rate over a 1 minute period.  I am unable to provide longer durations of this graph with my current setup but it may help provide some context.
[embedded file]
Since the sensor is currently triggering on a Monster Energy Drink can, we can also see the results of that can being slightly bumped during one of the rotations:
[embedded file]

I think this shows we have a very accurate turn rate using stroboscopes alone.  The above data suggests when configured, the turntable has an accuracy of approximately -0.05%, +0.025%.

### Ryan Ferguson, 2023-12-21

Just to give a final end of the year update, the TAS is nearing completion.  The codebase for the TAS and Judge are being tested prior to release to production and are no longer receiving new features, only bug fixes prior to release.  In January when everyone is back from the holidays, I hope we can review the data collected in https://jenaero.atlassian.net/browse/ENG-2403 to set a final pass/fail criteria for the verification steps.  This combined with the magfit updates are the only remaining tasks which will require a significant time investment from other teams to prepare this project for CCB.
The autopilots that have been calibrated on the TAS will need to be calibrated again by Production to validate the results of the TAS.  This can be done after the new year if production schedules require it.  When Production is ready, they will also be building up the second batch of autopilots to be calibrated on the TAS (The 'manual method first' batch).
Once this project is released, there will be some updates and additional documentation that will need to be created.  These primarily focus on the pinout tables of the harnesses in the TAS, creation of a blast shield for safety, and ongoing support to fix any bugs Production manages to find.

### Ryan Ferguson, 2024-01-09

@Greg Fryer @David Grosher @Trevor Gronner I have done some work to define an acceptance criteria for the gyro and accelerometer verifications.  Design Engineering/flight dynamics will have to approve the proposed results before they get rolled in to the TAS project.  If these standards are acceptable from Design Engineering, I will add them to the AP Judge to be applied against all autopilots that come out of the TAS.
Data collection methods
I have developed two SQL scripts (attached to this message) to calculate a 2 standard deviation value for all of the values in the gyroverification and accelverification tables of the TAS database.  These scripts can be rerun again in the future as well to update the acceptance criteria as needed.  The calculations exclude any results which are significantly off from the target values (greater than 0.5 from target for accelerometers and greater than 10 deg/s off from target for gyros).
Over time as the database gains more data, these scripts will likely have to be run again to generate a new acceptance criteria.  Since this data has never been used to reject an autopilot before, I will set the AP Judge to use the most permissive criteria of the dataset until more data can be collected for better informed numbers.  This will be what I present to CCB but can tighten the criteria more over time.
Current process
I spoke with @Ben Norris to ask what they have been using for their criteria in electronics using the manual methods.  In the accelerometer, he has been using “roughly +/-0.05 for the accelerometer and +/-1.0 for the gyro”.  
This lines up with the accelerometer statistics of the current data as the 2 standard deviations difference (two sigma upper - two sigma lower) is approximately +/- 0.040 g.  The gyro data is a bit more challenging with 9 of the 42 values having standard deviations difference which significantly exceed the +/- 1.0 criteria.  The largest of these is the ypos_gyro_1_z data which hints at an acceptance criteria of +/- 2.74 ((two sigma upper - two sigma lower) / 2).  For this reason I will be requesting the acceptance criteria as such:

Proposed acceptance criteria for gyro and accelerometer verifications
Accelerometer
Target value for axis +/- 0.050 g
Rationale: This is what production has used to pass autopilots this far without direction from Engineering.  As it is wider than the statistically derived results, this wider criteria will be kept until sufficient data is collected to tighten the criteria further in the future.  Current data from the TAS shows that an acceptance criteria of +/- 0.020 g of target would be acceptable, however more data would be beneficial before unnecessarily tightening the criteria.
[embedded file]
Current statistics results for the accelerometer SQL query

Gyro
target value for axis +/- 2.74 deg/s
Rationale: Production has been operating with an unofficial criteria of +/- 1.0 deg/s which has been excessive.  It is common for techs to recalibrate autopilots many times over to get results to match the data.  The statistics from the gyro script below (num samples = 332 from 17 autopilots) show that this criteria may be excessive and can be opened to +/- 2.74 deg/s to avoid unnecessary fallout.  This acceptance criteria would guarantee an accuracy within approximately 3.04% of the target 90 deg/s.  
[embedded file]
Current statistics results for the gyro SQL query

[embedded file][embedded file]

### Ryan Ferguson, 2024-02-13

@Eric Brewer Please let me know if there is any additional work required for the acceptance criteria prior to release.  The Judge Database has been updated with the 2.74 deg/s acceptance criteria as shown below.  If all is good, we can release the database in the Vault to ensure we keep traceability on the criteria.

### Ryan Ferguson, 2024-02-13

Worth noting, the acceptance criteria are stored in the Judge Database in the Vault.  To read it, download the SQLite DB Browser or similar.  The database can be found in the following directory:
C:\JAI Vault 1\Projects\107 - Stalker XE, VTOL Gen 2\Production\Electronics Shop\Acceptance Criteria

Once released, I’ll copy the database into the Condor read-only directory everyone executes from so we can ensure it’s up to date.

### Eric Brewer, 2024-02-19

@Ryan Ferguson This looks reasonable to me.

### Ryan Ferguson, 2024-02-22

Given the response below and the passing of the TAS through CCB today, I am closing this ticket and considering the matter complete.  There will be periodic reviews of the data from the TAS to be completed at later dates.

### Christa Meck, 2025-09-25

Closed per previous comment.

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Photo 2023-10-05 11_10_07.jpg | image | 2557 | 2023-10-05 | listed only |
| MicrosoftTeams-image (9).png | image | 244 | 2023-10-20 | listed only |
| image-20231020-224613.png | image | 75 | 2023-10-20 | listed only |
| image-20231020-224953.png | image | 57 | 2023-10-20 | listed only |
| [accel std deviations.sql](attachments/18284_accel%20std%20deviations.sql.md) | text | 9 | 2024-01-09 | converted |
| [gyro std deviations.sql](attachments/18282_gyro%20std%20deviations.sql.md) | text | 10 | 2024-01-09 | converted |
| image-20240109-200245.png | image | 376 | 2024-01-09 | listed only |
| image-20240109-200346.png | image | 448 | 2024-01-09 | listed only |
