# May2023BendLongRangeTestingAntennaReport.docx

Attachment 15161, docx, 4480 KB, added 2023-06-22 by Maxime Jeanneau.

VXE30 Long Range SGCS3 Testing Report Spring 2023

Conducted: 5/31/2023

Location: Bend Oregon

Test Engineers: Cody Smisek, Maxime Jeanneau

Pilot in Command: Donald Allen, Kevin Sivertson

Test Procedure: 96X-3-14-5430 and Flight Test Request - 005 VXE30 Mid Range Testing

Overview:

This report contains information on the VXE30 long range testing event performed in Bend, Oregon on May 31, 2023.

The primary test objective was to characterize the first article builds from a new vendor of SGCS3 feeds and dishes (Micro Ant) for use in SGCS3 production units. The secondary objective was to collect detailed data on radio link performance of the VXE30 system near the limits of the supported operational range.

Both S Band and C-Band frequencies were tested. Radio link quality was assessed both by using metrics from the Silvus radio interface, and by streaming live Octopus E140Z G2 EO/IR video from the gimbal mounted within the aircraft. In all configurations tested, radio link was established, and video was streamed successfully.

Methodology:

Test procedures 96X-3-14-5430 and FTR 005 VXE30 Mid Range Testing were followed. A remote and local station was established. The local station using SGCS1 performed vehicle launch and recovery. The vehicle orbited above the local station which maintained command and control throughout the test.

Figure 1 Local Station Location Responsible for Aircraft Command and Control

The remote station was setup first at 48.5 km then at 98.5km from the local station. Both locations provided line of site throughout the flight orbit of the aircraft. Remote radio link performance metrics were collected from the Silvus web interface, Silvus speed tests were performed, and live video was streamed from the Octopus (formerly known as Epsilon) payload.

Figure 2: Remote Site (~48.5km C Band Left ~98.5km S Band Right) for Data Collection

Summary:

Weather:

Sky Clear, Visibility 10+ (some smoke in the area). Temps 50-70deg F.

Flights

| Flight | Takeoff (Local) | Duration (hours) | Trials |
| 1 | 0954 | 1.33 | SGCS2, S-band Production Antennas |
| 2 | 1148 | 1.54 | SGCS3, S-Band Production and First Article Antennas |
| 3 | 1454 | 1.9 | SGCS3, S-Band Production and First Article Antennas |

Controlled Variables:

Silvus Firmware: 4.0.3.14

Payload Software and Firmware: 3.5.1.1

Vehicle Altitude: 6781 MSL

Orbit Direction: Left

Equipment Used

VXE481 – AP FW 6.05m C4D9, Xcomm 4.67XEVT

Octopus (Formerly Epsilon) E140Z G2 EO/IR

SGCS1 – JAI1 (Radio JAI1-2 with antenna PNAOV2D230515G-TM Polarity V)

SGCS2-29

SGCS3-28

Micro Ant first article dishes and Feeds

Chronological Summary:

Preflight briefing commenced at 0600L on May 31, 2023 in the Bend office (2789NW Lolo Drive Bend, Oregon 97703). At 0630L the test team completed packing/loading of equipment and proceeded to the remote and local sites. At 0800L, the remote team began setup of SGCS2-S Band for FTR-005 at the 50km site. For electrical power, a small gas generator was intended to be utilized at the remote sites. However, due to unknown reasons, the generator was inoperative for the first portion of the testing (would not start). Power was provided to the midrange antenna via vehicle battery utilizing the alligator clips from the SGCS2 kit.

At 0813L a spectrum scan was performed. During this time at both sites, it was determined that the screen recording software (OBS Studio) appeared to be degrading the performance of the GCS laptops. As such, native screen recording was not available during testing, however, mobile devices were utilized to record applicable screen videos.

During the local sites first attempt of aircraft launch, IMU match errors were observed during launch wizard checks. These were subsequently cleared by unknown methods. Additionally, during initial connection, link distance on Silvus was mismatched between SGCS1 radio and VXE481 radio (5000m vs 50000m). This resulted in delays due to radio issues which were corrected prior to launch.

After launching the aircraft, at 1040L, an initial non-required test was performed for SGCS3 S-Band with Epsilon feeds and dishes. The intentions were to determine a baseline and verify appropriate connections with the system. It was noted that the gimbal was not accepting commands for movement and later it was identified that the connector harness was interfering with movement inside of the payload area. This did not impact testing and was corrected after the first landing.

At 1054L, SGCS2 FTR005 was completed for S band. This was followed by a landing to reconfigure equipment for C band testing.

At 1116L SGCS3 was reconfigured for C band with standard epsilon equipment. A issue was observed where commanding 1 selection of up through the GCS software tracking antenna dialogue resulted in full movement to the max up position. This was corrected by disconnecting and reconnecting to the antenna. Silvus communications were initially attempted, but it was observed that the radio was ‘browning’ out due to the power setup. At 1239L, additional attempts to restart the generator were successful and all remaining testing was done using a Craftsman 2500W generator for power.

At ~1314L testing was completed at the 50km site and a landing was performed at the local site.

At 1440L the remote team arrived at the 100km site. Equipment setup was completed at 1500L.

Flight crew reported that the aircraft ascended significantly above the commanded altitude at 1630L.

At 1700L testing was completed and site pack up performed. At 1830L a flight debrief was completed in the Bend office.

Results:

Video:

Both antenna configurations for SGCS-3 C-band (50km) resulted in excellent 4Mbps video streaming. This was done with the bandwidth of the Silvus radio set at 10 Mhz. Both antenna setups were not noticeably distinguishable between production and Micro Ant first article as they were both judged as a 10.

When 4 Mbps video was attempted on SGCS-3 S Band (100km), in both antenna configurations, the video started freezing and jumping and Silvus Airtime was near 100%. By reducing the video to 2Mbps and increasing the bandwidth of the Silvus radio to 20 MHz smooth video with limited to no freezing/jumping was achieved although the resolution was slightly lower than 4 Mbps video. Antenna setups were not noticeably distinguishable between production and Micro Ant first article as they were both judged as a 9.

Figure 3: Summary of Operator Judged Video Quality and Video Size Settings/Silvus Bandwidth Settings

Figure 4: Video Screen Shots (Top Left: C-Band Production, Top Right: C-Band-Band First Article, Bottom Left: S-Band Production, Bottom Right: S-Band First Article)

Silvus Web Page Statistics:

During each trial while video was streaming, the Silvus webpage metrics below were recorded. As this data was varying slightly during measurement, care was made to approximate the average for each data point.

Figure 5: Silvus Webpage statistics while streaming video

Silvus Speed Tests:

During each trial, the video payload was turned off and a Silvus speed test was performed to quantify how much data could be sent through the radio connection. The results are shown in the figures below.

Figure 6: Speed Test Comparison of 50km C Band Production and First Article Antennas

Figure 7: Speed Test Comparison of 100km S Band Production and First Article Antennas

Conclusion:

Radio connection was established for all trials.

Good video was successfully streamed for all trials.

Evidence to move forward with Micro Ant for SGCS 3 Feeds and Dishes

Limitations of Testing/Improvements:

Increase speed test duration for 1 entire orbit

Point video in same direction for each trial to better judge video quality

Method for collection Silvus Radio metrics from webpage as an average without having to judge average by looking

Appendix:

Location of video files

Scans of contact reports

Location of data files
