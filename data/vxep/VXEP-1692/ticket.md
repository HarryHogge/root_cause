# VXEP-1692: B40/30 XCOM WDT resets

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** High
- **Created:** 2026-02-04
- **Updated:** 2026-10-02
- **Reporter:** Cameron Chapman
- **Assignee:** David Grosher
- **Creator:** Cameron Chapman
- **Links:** relates to FS2-3875 (B40 Investigations ); relates to FS2-4141 (B40 WDT reset during RC fwd power check); relates to FS2-4207 (XCOMM: 4.75_rc3 reset investigation); relates to FS2-4175 (B40 Endurance Test - Capture WD boots); relates to FS2-4292 (Corrupt SD Card data  (B40 WD Investigation)); relates to VXEP-1701 (Evaluate XCOM acceptance tests, document issues, and implement fixes.); relates to VXEP-1548 (VXE 863 VTOL motors cut during landing resulting in unintended glide landing); relates to RMA-864 (VXE-646 RMA 251216-1); relates to FS2-4316 (Characterize error signature from an induced stack overflow in an ISR); relates to XKIT-5113 (B40 Non Flight-blocker flight test issue collector/Squawk List); relates to VXEP-1775 (VXE-937 Crashed after briefly losing link.); relates to ENG-346 (1607P01A Improvements. XCOM / XE240 PWR COMMS BD)
- **Corrective Action:** C/CA Improvements to production burn in procedures: https://jenaero.atlassian.net/browse/VXEP-1701
- **Severity:** 1 - Flight Critical

## Description

Main incident https://jenaero.atlassian.net/browse/VXEP-1692 

Investigation summary: https://redwireglobal.sharepoint.com/:p:/r/sites/EngineeringTeam/Shared%20Documents/200%20-%20Software/B40%20Investigation%20Data/WD%20Investigation/WDT%20Hardware%20Investigation.pptx?d=we9038b85f178402b9f4464a25bcf03cb&csf=1&web=1&e=kwaFoo
Sharepoint https://jenaero.sharepoint.com/:f:/s/EngineeringTeam/IgCmHcFgdXPeRbdcqQHWgJ8-AaTn-G522CHwO_3ML45Rhj0?e=i3TwV7 
Investigation sheet.: https://jenaero.sharepoint.com/:f:/s/EngineeringTeam/IgCmHcFgdXPeRbdcqQHWgJ8-AaTn-G522CHwO_3ML45Rhj0?e=i3TwV7 
XCOM Containment Sheet: https://jenaero.sharepoint.com/:x:/s/QualityTeam/IQDVhgQtYiwSRriZ1fSyyMCmAUDLZan64jyCYA16wh7YR2Y?e=eaFVK3
Chat:
Cameron Chapman: Updated table  Box PN Box SN XCOM SN Curr... | v913 B40 Avionics Investigation | Microsoft Teams
WD Shared Notes: Watch Dog Timer (WDT) Shared Notes - VXE Aircraft - Confluence 

Stress testing https://jenaero.atlassian.net/browse/FS2-4233

## Plan

See comments below for day to day status and plan.
Main inquiry paths and findings updated 2026-04-15. Ranked in rough order of investigation priority. 
Specific investigation details and tests here https://jenaero.sharepoint.com/:f:/s/EngineeringTeam/IgCmHcFgdXPeRbdcqQHWgJ8-AaTn-G522CHwO_3ML45Rhj0?e=i3TwV7 
- Sandeep’s latest FW is reducing WDs significantly. Continue running on multiple boards. Diagnose each.
- Build based on old FW showing much less Wds.
- Plan to make a build based on more recent FW. Test results.
- Based on above, figure out when/what increased WD frequency.
- Latest B40 RC8 significantly reduces WD from B30 latest (6V power supplies off, maybe other changes). Testing that on a larger number of XCOMs that previously failed for WD. 
- Working on new builds and testing each on 5 XCOMs. https://jenaero.sharepoint.com/:f:/s/EngineeringTeam/IgBVXcXj31sqQIGOtAVmQo_EAaJSC30dgJ4dqxvZlvKpS78?e=MMiBlP
- Laszlo has test equipment that can induce EMI to precise parts of the circuit. Plan to use that to identify vulnerable areas that can induce WDs and see if they can be improved. 
- Observed WDs seem to be more common, possibly induced by phone calls on both XCOM 5-6356 and 5-6159
- Injecting noise into certain parts of the circuit (ex: serial lines at the ribbon cable) seemed to reduce frequency. He is investigating potential improvements from these findings (ex: filtering serial lines).
- Tested disabling all power supplies and supplying 5-6356 XCOM with external power. Significantly increased WDs. Investigating what this indicates.
- Discovered XCOMs have 2 varieties of power converters. Evaluate if WDs are more common on one than the other (especially with latest FW). @Lawrence Nichols @Logan Wright

## Issue Status

See comments below for day to day status and plan. 
2026-09-16 update:
Latest WD status: 6.7.1 mitigation. 
When air data is stale due to XCOM reset, FWAP handles the problem by flying a proxy to airspeed during that interval. 
Tail number comment. Seems more tied to new boards since  850 until corrective actions were implemented. 

Major findings
- Turning off all 12V and 6V converters on a XCOM with a lot of WDs (Rate ~6/hr before) eliminated them over a 3 day period. 
- This seems to prove on this board and (likely others) WDs are related to power converters on XCOM.
- May be reduced or eliminated with redesign or moving these converters off the board. Need more data and to make a roadmap/plan.

- Improved XCOM burn in procedure and extended duration 6 to 24 hours.
- 7/96 XCOMs failed burn in running the 6.6.1 release (XCOMM v4.74).
- B40: We have not run into any WD in B40 endurance runs for Release Candidates. Our endurance test is 24 hours minimum on each RC before ready for flight. RC4-8 have all passed
- https://jenaero.sharepoint.com/:x:/s/QualityTeam/IQDVhgQtYiwSRriZ1fSyyMCmAUDLZan64jyCYA16wh7YR2Y?e=eaFVK3
- Since implemented related CAs to burn in and FW, 0 WDs in all B40 flight and ground testing since 4/1/20206.
- Asked @Scott Whitney if we can and should run a similar script for B30 flights since then.

## Comments (7)

### Cameron Chapman, 2026-04-17

With an AI assist - 
 Moving from plan to comments not valid timestamps:
- Lawrence identified XCOM 5-6159 seems to have a WD boot 1.6 seconds after every power up. Will confirm if interpreting the logs correctly. We have been unable to predict when WDs will happen until now, so this could be a good opportunity to perform specific measurements when the WD is anticipated. 
- Working on test plan to test this.
-

When the XComm firmware encounters an exception — such as a null pointer dereference or an illegal instruction — the processor immediately stops what it was doing, saves diagnostic information (what was running and where), disables all interrupts, and enters an infinite loop doing nothing. It cannot recover on its own. After approximately 8 seconds, the hardware watchdog timer expires and forces a full processor reset, just as if power had been cycled.
 
On the next boot cycle, the firmware recognizes that the reset was caused by the watchdog (not a normal power-on or intentional software restart) and flags it as a "WD BOOT" in the event log. This message always appears at roughly 1.3 seconds after power-on, not because that is when the fault occurred, but because the firmware intentionally waits 1 second during startup before writing anything to the event log. That delay is by design — it gives the system time to stabilize before accessing the SD card. The timing of "WD BOOT" in the log is therefore consistent and expected, regardless of when during the previous flight the fault actually happened.
 

I've attached a bash script, crashSearch.sh, we keep under version control that searches a directory tree for event logs with "WD BOOT 16" then captures a summary of the resets to a .csv file. The 2nd script deduplicate_crashes.py cleans up the .csv file to eliminate duplicates theat end up in our logs. Among the information crashSearch.sh captures is our closest estimate of when the actual crash occurred, the timestamp of the last event log entry before the watchdog reset.
 
If you want even more detail about the exceptions, this Jira ticket has some working documents Sandeep and I are working towards better understanding of the exceptions. https://jenaero.atlassian.net/browse/FS2-4316?atlOrigin=eyJpIjoiMTczMjNiMjM3MGE3NDBiOThlYmIzOGNmYzB…
crashSearch 1.sh
deduplicate_crashes.py

### Cameron Chapman, 2026-05-07

Moving to comments. Does not seem like shielding had much of an effect on frequency 
- Shielding bare XCOM/filtering power input may have an effect on WD frequency. @Laszlo Juhasz @Lawrence Nichols testing with and without shielding. Report rate. 
- Result in larger box w AP attached. 18Wds overnight.
- Running without AP attached, but connector window to AP still open. WDs still happening, but seems to be less.
- Fully closing this opening seems to eliminate them in a few hours of testing. Plan to run this config on 2 boards overnight to see if truly 0. 
- Potential future tests, shielded tape, EMI spray, etc
- looks like we use two different Cu/Ni shielding tapes one from 3M 100-110765 and one from TitanRF 2125920 but TItanRF also sells bags as well as film by the roll so we could easily make our own custom precut shield

### Cameron Chapman, 2026-05-07

Notes from the call today, 
5/7 New build loaded yesterday. No WDS yet on the 3 working boards, which may be interesting. Much less that prior.
- SW wants WDs to evaluate. Turn on 6V to maximize WD chances.

 
Some boards get stuck in boot loops when updating to B40 FW.
- Check for SD card corruption.
- Focus on getting new boards working with latest FW trying to get WDs with the boards. Turn on all converters to maximize WDs.
- Can troubleshoot why that is, see if flashing back to B30FW works later, but lower priority. See if master reset button laszlo mentioned helps with that.

### Cameron Chapman, 2026-06-23

6/23 Call What is current status of investigation and plan? 
Doing more testing to confirm what is getting us into WD situations. If ISR related, fix would reorder priorities, round robin, etc. Relatively quick to fix once known. 
Current status: 
Hardware: Laszlo testing XCOM on old FW with LDO for lower voltage.  LDO replaced FET on 2 boards identified in log. Matt to coordinate with Laszlo assigning PN and documenting pictures and schematic
FW: Other XCOMs. Running newer Sandeep FW. Tracking ISRs. Have mechanism which will log if nesting is happening, how we are consuming ISR stack. Will also check if not returning from ISRs. Having in latest build. Trying to update XCOMs with that.

### Cameron Chapman, 2026-06-25

6/25 Meeting
- Laszlo: Want to see if processor brown out detection gets triggered by 3.3V line at any time. Planning to run on an original configuration board. Ideally once with frequent WDs. Can you and/or Matt please take some pictures of the modification, record PN consumed, add this doc to the vault, then relabel these boards?
- @Matthew Aguirre to populate WD count in tracker sheet. Find an unmodified board that has WDs occuring for laszlos test. May have to roll back firmware. 6375 looks like a potential one.
- Sandeep: new set of logs from this morning are interesting. Some exceptions seen. Trigger for those is most likely memory corruption. Difference from previous is that we now have a trace to go through.

### Cameron Chapman, 2026-06-25

@Perry Richardson are you able to help us with an inquiry. Are the PIC32 @Connor Peebles  are you aware of any subs ever approved? @Sandeep Dharmadhikari  mentioned some known issues with older versions. 
Current PN on B40 schematic/BOM is PIC32MZ2048EFM144-I/PH. I am not aware of it ever changing or subs approved since 2018 at least.

### Cameron Chapman, 2026-06-25

@Connor Peebles @Perry Richardson  disregard: 
“Sorry i misspoke in the meeting, the part number gives us a ton of information abou the chip but does not give us the silicon revision, the only way to ensure it is asking the distributor the a particular silicon revision or higher. For us, the only way to do it is to read the associated register in firmware. I have added the register read to our firmware, going forward, we will know what revision is running on the xcomm from the logs.
 
Makes sense. It may or not be possible, but would take a lot of work to run that down with distributors if they and we had tracking. Pulling from that register sounds best”

## Attachments (0)
