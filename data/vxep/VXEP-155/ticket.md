# VXEP-155: VXE-455 all lift motors turned off during vertical ascent on launch

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Medium
- **Created:** 2023-10-20
- **Updated:** 2026-09-03
- **Resolved:** 2025-05-28
- **Reporter:** Pat Wells
- **Assignee:** Cameron Chapman
- **Creator:** Pat Wells
- **Labels:** MCWL, PMA263, Weekly-incident-tracker
- **Links:** relates to RMA-184 (VXE-455 231102); relates to FS2-1181 (v455 Crash during launch investigation); relates to VA-1036 (VXE-455 all lift motors turned off during vertical ascent on launch- Electrical inspection. Identify C/CA)
- **Customer:** MCWL, PMA263
- **Vehicle Tail Number:** 455
- **Problem Type:** Other (explain in description)
- **Root Cause:** Inconclusive due to missing log data. Logs indicate a failed lift system during climb. The failure occurred ~81' AGL.
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

On launch during vertical ascent all four lift motors turned off at 50-75ft AGL.  Aircraft nosed over and crashed into ground.  Lift booms destroyed, nose cone destroyed, tail boom damaged, horizontal and vertical stabs detached from tail boom. 
Aircraft Logs Uploaded Here: Flight Safety - VXE-455 all lift motors turned off during vertical ascent on launch - All Documents (sharepoint.com)
Relevant Logs for this flight:
- Fixed Wing Autopilot: FDRRECOV.csv
- XComm: XCEVLOG.txt, XCL00081.csv
- VTOL Autopilot: VTEVLOG.txt, VTL00042.xls

## Vehicle Configuration

FW AP: V6.05m
XComm: V4.67
VTOL: V1.52

## Plan

- I think we should try to identify C/CA of why we are missing VTOL logs for 24 seconds before the crash.
- Up to 5 seconds of missing data could be explained by unlucky timing on software commits to the file (“save”). However, 24 seconds is extreme. Another possibility is a failing SD card which we have seen a lot of.
- Same action for why the FWAP only starts between 28-29 sec.
- FDRs are pulled from XComm at the end of the flight. If the GCS detected a false landing then it would have started the FDR retrieval process. Likely this would have not completed before impact. We do not have GCS logs to confirm if this was the case, but it would explain why the FDR was not fully recovered.
- Do the logs indicate SA cam traffic when the vehicle starts to fall? That would indicate if the VTOL AP int board had power or not.
- Insufficient log data to determine SA cam traffic during the initial fall.
- XComm data shows working network and CAN bus until the end of the log.
- Plot commanded power vs expected power for each motor. Jason working
- We do not have sufficient log data. This requires VTOL data as the ibat1 and ibat2 data is not logged on XComm. Additionally, XComm has a lower sample rate of the current and voltage data. Best we can get is a low sample rate overall system power comparison before the event occurred.
- @Connor Peebles 
- Put each (XCOMM, VTOL AP & Interface) through production testing.
- Power up boards individually and look for abnormal hot spots.
- @Jason Scherer Look at FW AP log data supposedly after incident (conversation we had w/ Kurt)
- I re-attempted to download the FDR data which resulted in the same data contained in the previous FDR recover file. Unfortunately, we still don’t have critical flight data during the failed climb. @Cameron Chapman Did we ever get the GCS log for this flight?
- @Jason Scherer Look for XCOMM Watchdog (conversation we had w/ Kurt)
- No Watch Dog Events are reported in the XComm debug message log file (XCEVLOG.txt). As previously noted the reset to the XComm processor occured due to a “POWER RESET” and logs indicate that. -JS 2-29-24

## Issue Status

Cause Inconclusive: Aircraft 455 launched and climbed to an altitude of ~82’ before it fell to the ground. Log analysis indicates a lift system failure. The aircraft started descending from 80’ rapidly (~1.1 seconds). The aircraft initially pitches down which matches the observed behavior. The XComm processor interpreted the altitude decrease as a failed climb. The XComm processor issued an RTL command right before the aircraft crashed. Both XComm and VTOL processors show a power reset occurred after the fall.​
There are no easily identifiable hardware issues so far, will look more into.
Latest Report: Vehicle Investigation Report VXEP-155.pptx

## Comments (31)

### Pat Wells, 2023-10-20

@Greg Fryer do not expect to receive any AAR files or RMA of hardware before the end of Oct 2023. Customer is currently participating in an active training event and unable to send at this time.

### Greg Fryer, 2023-10-25

Status note, as expected still have not received AAR or aircraft back. Putting On Hold (should have done that first).

### Greg Fryer, 2023-11-08

@Pat Wells Any update on if this will be shipped, or if any data can be available?

### Cameron Chapman, 2023-11-08

**Sean Odell:**

Aircraft arrived late 11-8-2023. Will be doing initial evaluation and deliver to engineering tomorrow morning.
@John Clark are you available to review these logs? FYI@Greg Fryer

### Sean Odell, 2023-11-09

@Greg Fryer @Cameron Chapman  Aircraft intake complete and aircraft delivered to Engineering for your continued evaluation. Photos are on the RMA ticket linked.

### Pat Wells, 2023-11-13

@Cameron Chapman customer did not download logs prior to returning the aircraft on RMA.  Our team will need to pull those now that we have the aircraft in house.

### Cameron Chapman, 2023-11-13

@John Clark or @David Grosher do you have anyone available to pull and analyze this data? Will any of the aircraft logs contain a cut and safe command if it was pressed, or would that be stored on the GCS laptop (which we do not have)?

### David Grosher, 2023-11-14

@Jason Scherer Can you pull the logs from this AV and send them to me? I will review them and then assign the investigation further.

### Jason Scherer, 2023-11-14

@David Grosher Flight Logs uploaded to SharePoint (Flight Safety - VXE-455 all lift motors turned off during vertical ascent on launch - All Documents (sharepoint.com))

### David Grosher, 2023-11-14

@Cameron Chapman @Greg Fryer I don’t see any indication that a SAFE command was issued. The data is not conclusive, but if I had to guess, I would say it was a task lock scenario that would have resulted in a WDT but it crashed and power cycled too fast to log any related data.  The log ends rather abruptly on the VTOL and does not log any data as it falls.

### Cameron Chapman, 2023-11-14

Thanks @David Grosher and @Jason Scherer. 
Would such a command be logged on any GCS logs? Could we request it from the customer? I would hope that the GCS would continue to log even when the aircraft connection is logged, but that may have not been captured if they didn’t generate an AAR.

### David Grosher, 2023-11-14

@Craig Burton (see question below) 
I believe the answer is yes. I also think I have seen it in the VTOL/XCOMM logs in the past when it was issued.

### Jason Scherer, 2023-11-14

@Cameron Chapman Yes, the GCS Debug Log (and perhaps the aircraft logs as well) would indicate if the safe command was issued by the user. For example, on another AAR I found the following message logged in the GCS Debug Log. “[07:17:09.607] VTOL MSG: User Command: VTOL SAFE”

### Cameron Chapman, 2023-11-14

@Jason Scherer how would we get those logs for this flight? Are they stored on the aircraft, or would we need to request them from the customer laptop?

### Jason Scherer, 2023-11-14

@Cameron Chapman The GCS Debug log would be included in the AAR which would be generated from the customer laptop. As far as I know we have not received an AAR from the customer for this incident.

### Cameron Chapman, 2023-11-14

@Michael Berger if a customer did not generate an AAR after this flight, could we still have them send the GCS debug log from their laptop? Where would it be located if so?

### Michael Berger, 2023-11-14

It should in C:\ProgramData\GCS\XEVTOLGCS. 
Note that C:\ProgramData is a hidden folder. 
Assuming SUAV VTOL.

### Cameron Chapman, 2023-11-15

@Jason Scherer, @David Grosher mentioned that we have evidence that the abort button was not pushed. Can one of you please update the fields above?

### Jason Scherer, 2023-11-15

@David Grosher @Cameron Chapman I updated the fields, and I posted a link to the investigation report on SharePoint. It looks like it may have been a hardware (boom power) failure. It’s hard to tell because we are missing so much data at the critical moment. What I know is that the HLB voltage looks ok. the initial climb looks ok. The XComm logs a climb fault as the aircraft is falling from the sky. Based on the observed forward motors giving out first, plus the FW AP showing a downward pitch as it starts to fall, is it possible a connector or harness failed?

### Cameron Chapman, 2023-11-16

@Jason Scherer the investigation plan field does not seem updated (you can delete steps that have been done). See this comment below. “@David Grosher mentioned that we have evidence that the abort button was not pushed. Can one of you please update the fields above?”
Investigation status should include a summary of the fishbone (or just paste the fishbone slide)
- XCOM log should have vtol battery voltage and current (Ibatt 1 and 2). Can you please plot that after the VTOL log stops? That would help indicate a VTOL fault.
- Can you please plot commanded power vs expected power for each motor (John should know how to do this, if not, I can dig up the calculation).

### Jason Scherer, 2023-12-05

@Cameron Chapman XComm CSV does not have ibat 1 & 2 broken out. It simply has vtVbatt and vtIbatt. If you look at slide 7 of the Vehicle Investigation Report it shows those values plotted. They are normal until the end of the XComm log. I’ll update to add the commanded power versus expected power. I updated the timeline slide that Greg added to be more accurate. I removed the history on the investigation plan field. I copied the investigation status from the report and put it in the field on this ticket.

### Jason Scherer, 2023-12-05

Also, I wanted to make a distinction about the abort button. I don’t have any evidence it was or wasn’t pressed. I simply didn’t find anything to say it was. Since we don’t have the GCS logs, I can’t say for sure.

### Cameron Chapman, 2023-12-12

@Cameron Chapman

### Cameron Chapman, 2023-12-13

@Jason Scherer. Great work. The ppt is very helpful.  can you please do the following? 
- I think we should try to identify C/CA of why we are missing VTOL logs for 24 seconds before the crash. 
- Same action for why the FWAP only starts between 28-29 sec.
- Do the logs indicate SA cam traffic when the vehicle starts to fall? That would indicate if the VTOL AP int board had power or not.
- @Connor Peebles can you or someone you assign please investigate the functionality of the lift system (XCOM, VTOL AP, ESCs)? It was involved in a significant crash, so please inspect, resistance measurement, and power up carefully.

### Connor Peebles, 2023-12-14

@Cameron Chapman @Sean Odell Is 455 incident hardware back in RMA?

### Sean Odell, 2023-12-14

@Connor Peebles The physical hardware is in RMA. The repair quote is complete on my end. If your team needs the hardware back, it is available.

@Cameron Chapman @Pat Wells FYSA

### Connor Peebles, 2023-12-14

There are no easily identifiable hardware issues so far, will look more into. (https://jenaero.atlassian.net/browse/VA-1036 )
@Jason Scherer I added some to the investigation plan, paraphrasing from our conversation w/ Kurt (you may have to fill in more details for me).

### Cameron Chapman, 2024-03-11

@Jason Scherer Thank you for the updates. Are you available to give any information or linked issues for items 1-3 in the plan above?

### Jason Scherer, 2025-03-22

@Cameron Chapman I don’t believe we have sufficient data to make any more conclusions. I have added statements to steps 1-3 in the plan. Regarding the missing log data, my best guess is a failing SD card. If we still have the SD card we could try some tests, but we already know the old SD cards are not rated for this purpose and prone to error.

@David Grosher @Pat Wells How should we proceed on this investigation? Since we are missing critical log data during the incident, I don’t expect to come to any further conclusions.

### Pat Wells, 2025-03-24

@David Grosher @Jason Scherer this was closed out a year ago with the customer by replacing their aircraft under goodwill.

### David Grosher, 2025-03-24

@Jason Scherer This sounds like task lock, likely resolved in a more recent firmware update. If we don’t have data then let’s close this as Bermuda Triangle. The customer is no longer tracking it. @Pat Wells FYSA.

## Attachments (0)
