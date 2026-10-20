# VXEP-1827: Air Data Board - Failures

- **Issue type:** Problem
- **Status:** Assigned
- **Priority:** High
- **Created:** 2026-04-10
- **Updated:** 2026-08-05
- **Reporter:** Samuel Lopez
- **Assignee:** Samuel Lopez
- **Creator:** Samuel Lopez
- **Links:** relates to ENG-1750 (MPU-9250 Chips have high failure rate, are obsolete, and have a high rate of conterfeits.); relates to VXEP-1971 (VXE 885 Erratic behavior in flight caused crash)
- **Problem Type:** Production Issue
- **Severity:** 1 - Flight Critical

## Description

Files: https://jenaero.sharepoint.com/:f:/r/sites/JAI_Operations/Shared%20Documents/NCR%20Investigations/VXEP-1827%20%20%20Air%20Data%20Board%20-%20Failures?csf=1&web=1&e=nx1Ft8
As of April 2026, we have seen a string of a recent batch of boards have come in with the following issue.
- The ADBs have begun arriving in a new color - green - as opposed to their traditional color - red.
- This is due to an oversight by RW.  The Output Job files specify green.  This mistake was not captured earlier because First Articles were delivered in traditional red.
- Not a mistake, keep new boards Green. -C. Peebles
- Barometer is dead on arrival or cannot be calibrated.
- There has been a slew of bad boards due to faulty barometers.  These failures have increased significantly in April.
- Accelerometer/Magnetometer - odd values.
- The accelerometer/magnetometer readings show abnormal readings before calibration.  However, after calibration, they do read normally.
- Investigate whether all these matters are correlated.  Is the problem
- The PCBs?
- The Barometers?
- Firmware?
- Something else?
- In the middle of this investigation, we noticed that nearly fifty percent of all boards are also failing due to accelerometers with bad values pre-calibration.  This requires more investigation.

2026-05-13Description of Issue based on most recent findings
https://jenaero.sharepoint.com/:w:/r/sites/JAI_Operations/Shared%20Documents/NCR%20Investigations/VXEP-1827%20%20%20Air%20Data%20Board%20-%20Failures/Description%20of%20Issue.docx?d=wa33913076923401ba6f97f49e590a40f&csf=1&web=1&e=BpltFg
For Test Plan and Results
https://jenaero.sharepoint.com/:x:/r/sites/JAI_Operations/Shared%20Documents/NCR%20Investigations/VXEP-1827%20%20%20Air%20Data%20Board%20-%20Failures/Measurement%20Issues%20Data.xlsx?d=w2b67c656dda843ba97d4fad3f49be05e&csf=1&web=1&e=AEJElr
Accelerometers are 
MFG: MPU-9250
RW Part # 100-110018
Barometers are
MFG: MS5611-01BA || MS561101BA03-50
RW Part # 100-110017

Barometer failures have been moved to the following jira.
 [VXEP-1888] Air Data Board - Failures (Barometer) - Jira

## Plan

- Take a failed board and replace the ‘bad’ barometer with a fresh one off the shelf.  Observe whether the Air Data Board is functional.
- How feasible is this for production or board house?
- Investigate whether the barometers provided by Green Circuits are counterfeit components.  They will need to be sent out to a test lab.
- Start by contacting mfr of MS5611-01BA
- https://copilot.microsoft.com/shares/fRwYQDy4gqZmqg7Jwnh5m  but here are some potential items
- Similar checks for 9250. https://copilot.microsoft.com/shares/FRrck5CPcgSvxGPXiXGAJ
- If the problem is neither of these, ask Green Circuits about their checkout process and if they have reliability of their distributors.

Can we please do the following. 
- Make a sharepoint location for this investigation. https://jenaero.sharepoint.com/:f:/r/sites/JAI_Operations/Shared%20Documents/NCR%20Investigations/VXEP-1827%20%20%20Air%20Data%20Board%20-%20Failures?csf=1&web=1&e=nx1Ft8
- Make a sheet to get failure metrics.
- Link both in the JIRA desc https://jenaero.atlassian.net/browse/VXEP-1827
- We can also record actions hwew (ex: ensure we have enough on order to support production with expected failure rate)

## Issue Status

Root Cause Identified - Investigation Complete
https://jenaero.sharepoint.com/:p:/r/sites/JAI_Operations/Shared%20Documents/NCR%20Investigations/VXEP-1827%20%20%20Air%20Data%20Board%20-%20Failures/Air%20Data%20Board%20-%20Accelerometer%20Failures.pptx?d=w1902296ef9a4498f8633571b2dc9946e&csf=1&web=1&e=Yin8gl
The MPU9250 is an obsolete accelerometer previously manufactured by TDK. Though Redwire does not have the capability to reliably replace the components on the PCB onsite, one board did have a single accelerometer repaired and replaced upon which the board reported acceptable accelerometer limits.​
Two more boards were sent to the PCB house to have them repair and replace the accelerometer. Of the two failed boards, one of them now passes the accelerometer test that it previously failed. The other still fails - whereas before, it read around -0.850 (0.50 too high), it now reads -1.150 (0.50 too low). Interestingly, this 1 our of 2 success rates comports with the 55% success rate that we previously observed on these accelerometers.​
This confirms that root cause can be reduced to component failure.
Additionally, Advanced Component Testing has concluded that the components failed solderability tests as the solder does not adhere to the pads (see images in powerpoint).
Baro issue:
baro belongs in it's own investigation which - at the moment - we will not be pursuing.  The reason is because of the failed boards, we can expect to see a failure rate of 5% with faulty barometers, which is a failure rate we can accept.
Corrective Action
Redwire will accept the Air Data Board low yield rate.

There is a plan for Redwire to develop ‘self-test’ firmware which will allow our board house Green Circuits to flash/screen the boards for accelerometer/barometer failures at their own site.  However, due to limited resources and higher priorities, this plan is being shelved until further notice.  

[FS2-4855] Airdata Board - Self Test Firmware - Jira

Thus, the corrective action will be to store failed (accelerometer) boards in NCR until all boards until a large enough pile to justify sending for rework (50 or so).  Production/Quality will then send failed accelerometer boards will be re-sent to Green Circuits for one-time rework.  This will be coordinated by @Aidan Calvet @Gary Passanisi.  Upon their return, boards that pass will be processed normally.  Boards that fail will be scrapped.

Cam Discussing here with Sam I would like to resolve issues before closing. Cameron Chapman: I think a helpful step is to link individual investigati... 📷 Image

## Comments (19)

### Samuel Lopez, 2026-04-13

Dusting Limon took the barometer from a scrap VTOL board stack and replaced it into a ‘bad’ green ADB board.  After this, the board no longer returns a zero value for pressure.  However, calibration is necessary to see if this replacement fixed the issue.

### Samuel Lopez, 2026-04-16

Boards were calibrated incorrectly and must go through the oven a second time.  However, the barometers are no longer ‘dead’.

@Perry Richardson can you reach out to Green Circuits and ask/state the following.

Over the past few months, we have seen an increase in failures for the Air Data Boards not seen in the previous versions.  The barometers are dead when the board is powered on.  I bought some barometers from digikey (MS561101BA03-50).  Reflowing the barometers has not yielded positive results.  However, replacing them altogether has brought the boards to working order.

Where or what suppliers are you using to purchase the barometers from?

### Samuel Lopez, 2026-04-17

Boards have been re-calibrated.  All but one now read correctly.  This strongly indicates that either
a. the barometers that Green Circuits acquired are bad.
b. they are not being adquately soldered.
The strongest candidate is that the barometers were bad from the start.

Green Circuits has indicated that they purchased the barometers from Mouser.  Next steps are as follows.
- Take a ‘failed’ board and install resistor R10 (CAN resistor).  Though unlikely, this will eliminate the possibility that these boards are failing from the -01 to the -02 configuration.  @Gary Passanisi, can you find a ‘failed’ board?  I’ll find the resistor.
- @Natalie Lusk and @Aidan Calvet .  I’d like to take some of the dead barometers and send them to a Hi-Rel or another X Ray Lab for inspection.
- Additionally, I think it would be prudent to tell Green Circuits NOT to proceed with the next batch of 125 ADBs until we conclude our investigation.
- @Dustin Limon .  Is it too much to ask if yourself and Gary put together a list of all failed boards, which ones were reheated and still didn’t work, which had the barometers replaced and still worked, etc?
- @Perry Richardson, can you tell the board house to cease production/assembly of new boards until we conclude our investigation?

### Samuel Lopez, 2026-04-23

On 2026-04-23
Four more ADBS have barometers have come in as ‘dead’ from the board house.  
Joseph will cut out the portion of the boards from two of these ADBs to send for x ray analysis.

Aiden will then send the three dead baros and two bad boards to an x ray lab for testing.

Two will be saved to potentially send to Green Circuits.

### Samuel Lopez, 2026-04-27

April 27 Meeting
- Dustin to take 20 of the April 20 and run them through the process to see how many fail.

- Aiden to tell ACT to proceed.  Unless he finds a faster laboratory.

 
Notes
·       As of April 27, 2026.  We have 181 in stock.
o   125 from batch delivered on April 20, 2025
o   The rest from a previous batch from December 2, 2025
o   All the failures have been from the December batch.
o   The April have not gone through receiving inspection.
o   Regarding Dustin’s 20 that he will check.
§  If all 20 pass, we’re confident the lot is good, hand it back to R and I.  They’ll pass it to inventory. 
§  If we get even one failure, the lot will be rejected.  Every single one must now be screened.

### Samuel Lopez, 2026-05-06

2026-05-06
Accelerometer Failures
- Of the 20 boards that were tested of the April 20 batch, only 11 passed.  The rest had results as follows.
- 6 have accelerometer values that are out of range
- 2 have accelerometer that are fluctuating in and out of range
- 1 has accelerometer values that are out of range/also has a dead barometer
- The ADB failures have now expanded to barometer/accelerometer failures.

Next Steps
- We must determine if these are board failures, component failures, or assembly failures.
- To eliminate board failures, we will re-solder fresh accelerometers to two (2) of the six bad accelerometer boards.
- Recommend sending an additional three or four accelerometer boards to x ray lab and/or to component test lab.

### Samuel Lopez, 2026-05-07

2026-05-07 - CAN Termination
- It was discovered that the hilbox only has one CAN termination.  Though it’s unlikely, this may lead to false errors.  A 121 Ω resistor is being added to the Air Data Board side of the harness to comport with proper CAN practices.
- The barometer/accelerometer failed board was re-tested with an added CAN resistor.  The result was the same.  @Gary Passanisi please remove the added resistor from the board.
- @Gary Passanisi will test the additional 19 boards once the 121 Ω resistor is added to the CAN line on the ADB side.
- Once all failures are confirmed, a procedure will be set up to send failed boards back to boardhouse for barometer/accelerometer reworks.

### Samuel Lopez, 2026-05-11

- The ADB Hilbox has been modified to have two CAN terminations - the one on the XCOMM that has always been there, and one on the harness near the ADB.  All 20 boards from the April 20 lot have been re-tested with identical results.  We can conclude that root cause is NOT the testing setup due to CAN terminations.

Next Steps are still
- Determine if these are board failures, component failures, or assembly failures.
- To eliminate component failures, we will re-solder fresh accelerometers to two (2) of the six bad accelerometer boards.
- Recommend sending an additional three or four accelerometer boards to x ray lab and/or to component test lab.

### Samuel Lopez, 2026-05-11

Boardhouse will be contacted to discuss the following.


- Ask the boardhouse why there has been a change in the color of the boards?  Even though we don't expect this to be a root cause issue, we'd be remiss in not asking.
- Inform the boardhouse that in addition to the barometer failures, we now also have accelerometer failures on both old and new batches.
- Ask them if we can send them some of these failed boards and have them remove and replace the components in question - accelerometer/barometer.

Additionally, I spoke to Ben Norris last week.  Even though we are expecting to have historically low output of these batches - 11/20 = 55% - we may want to nonetheless increase output.  This is because we are also expecting to ramp up production here in SLO potentially to 40 builds per month.  I'll call a meeting between two or three of us to finalize this.

### Samuel Lopez, 2026-05-13

@Nigel Goodison  @Aidan Calvet 

Kurt took 1 of the 9 boards that had a failed accelerometer and replaced the component itself - MPU 9250.  After doing so, the accelerometer has a passing value!!!
This confirms that, as we suspected, these board failed due to a bad component batch.

### Samuel Lopez, 2026-05-13

May 13, 2026 Plan
Aiden will send
- Four complete to the test house for x-ray to check if component is compromised AND board solder job are compromised.
- Two will be sent to Green Circuits for replacement.
- Three fresh MPU 9250 will be sent to test house for x ray to compare versus bad components.

### Samuel Lopez, 2026-05-18

2026-05-15
Inspection of three MPU 9250 solder jobs of three failed boards has been completed.  No irregularities detected.  Firmware has been re-flashed on same three boards - no change.  

Please see Fishbone and Microscope Videos in SharePoint for details.

VXEP-1827   Air Data Board - Failures

### Samuel Lopez, 2026-05-18

2026-05-18
Continue Production?
Three boards are being sent to Green Circuits for x ray of accelerometer assembly (Only 11 of the 24 pins are actually used in the ADB).  If:
- No irregularities are revealed by x ray - then it’s not an assembly issue, tell Green Circuits to continue production immediately.
- There is an irregularity revealed by x ray AND it’s one of the 11 pins - Green Circuits will update their pick and place procedure and continue production.

### Samuel Lopez, 2026-06-19

Root Cause Identified
- Board failure due to component failures.  Please see PowerPoint above for details.

### Cameron Chapman, 2026-07-10

@Samuel Lopez can you please give more info on C/CA and can I review before closing? I do not see it in the ppt. Can you please summarize here?

### Samuel Lopez, 2026-07-10

@Cameron Chapman 
Corrective action will be to store failed boards in NCR until all boards in a single batch have been processed.  Production/Quality will then send failed accelerometer boards will be re-sent to Green Circuits for one-time rework.  This will be coordinated by @Aidan Calvet @Gary Passanisi.  Upon their return, boards that pass will be processed normally.  Boards that fail will be scrapped.

### Samuel Lopez, 2026-07-13

@Cameron Chapman 
I have updated the C/CA in the ‘Issue Status’ and would like to close this out.

### Cameron Chapman, 2026-07-13

@Samuel Lopez thanks for updating the ADB investigation. Did anyone evaluate testing MPU9250s before board installation? Could board houses do that, or not worth it?

### Cameron Chapman, 2026-07-13

@Samuel Lopez Also, the problem description lists issues with the baro and accel, but the C/CA only seems to address the accel. How many had baro failures? Is the investigation of that tracked anywhere?

## Attachments (0)
