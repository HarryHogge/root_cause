# ENG-2047: Green AP's (0002P01G) need to have gyro/accel pass/fail criteria reviewed

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-07-10
- **Updated:** 2026-08-05
- **Resolved:** 2023-07-26
- **Reporter:** Ryan Ferguson
- **Assignee:** Maxime Jeanneau
- **Creator:** Ryan Ferguson
- **Links:** relates to VA-156 (Receiving qty 800 new processors (st10...) evaluate and test with hand soldering and small batch to Sierra); relates to VXEP-1971 (VXE 885 Erratic behavior in flight caused crash)
- **Part Number(s):** 0002P01G
- **Production Stakeholder:** Ryan Ferguson
- **Problem Type:** Production Issue

## Description

Production recently attempted to process a batch of 9 green autopilots and rejected 6 of them due to gyros and accelerometers falling out of the limits specified in the procedure.  This indicates a 66% failure rate due to accelerometer and gyro values that are falling out of spec.  This can only be detected at the last steps of processing, so it is a big sink to production when such failures happen.  
References
NCR 1220 - Green AP Failing IMU Calibration (Closed 7/21/23)
JIRA - MPU-9250 Chips have high failure rate, are obsolete, and have a high rate of counterfeits.
JIRA - Replace obsolete MPU-9250 accelerometer. 
JIRA - Red AP's have excessively tight pass/fail tolerances
IMU Calibration Procedure: Document #110640
Accelerometer 
The procedure tells techs to place the autopilot in each of the 6 orientations and record the indicated accelerometer values on the traveler.  During this phase, accelerometer values should be ~1.028.
Once values have been recorded, the tech then puts them into a spreadsheet to determine the proper calibration span and offset values.  These are then recorded in the traveler.  The quote below is the wording pulled from the procedure about the accel span and offset value acceptance criteria:
These span values should be roughly 0.96-0.98.
There is a numerical limitation of the offset value of +/-0.128; if these values are outside of that, reject the board.

After the span and offset are entered into the board and saved, the tech is to verify the calibration was correct.  The below quote discusses the acceptance criteria for the accelerometer after it has been calibrated:
Verify this is correct by rotating the jig and ensuring that one value is roughly ~1G, and the others are roughly 0 (within +/- 0.002) in the instrument panel.


In this section of the procedure, autopilots fall out because of the 0 +/- 0.002 g spec.  If we can open this to 0 +/- 0.004 g we can significantly remove the fallout due to this section. (Strike by @Greg Fryer while data is gathered.) It is common practice to reperform the accelerometer calibration multiple times if it did not fall in the acceptance range the first time around.
Common sources of error that push boards out of spec here are primarily focused around the mounting of the MAGACC2 board to the autopilot.  If it is not perfectly level and square, it will show a slight value falling out of the expected range.  The hardware to mount the MagAcc2 board to the autopilot is not capable of sufficiently doing this leveling as it involves gluing standoffs which may have slight variability in length.  Failing boards were only off by approximately 0.010” which is infeasible to ask technicians to hold without better designed hardware.
[embedded: image-20230710-181006.png]
[embedded: image-20230710-181025.png]
Gyro 
The procedure has technicians first set the gyro offset by leaving the autopilot still and copying the gyro measurements into the calibration offsets.  The following note is made about the acceptance criteria of the offset calibration:
Verify this is correct be ensuring that the corresponding values in the Vehicle State pane go to 0 (+/- 0.1).

The autopilot is then set on the rate table at 90.0 deg/s and the readings from the autopilot are noted in the traveler.  The following note is made in the procedure:
Values are typically within 1 degree of 90 degrees/second in the Vehicle State pane.

The measured gyro values are copied into the spreadsheet noted earlier.  The spreadsheet then calculates the span calibration values which are then recorded in the traveler and saved to the autopilot.  The following note is given for the acceptance criteria:
The span values should be close to 400 due to the historical scaling on the old gyros. The first two values should be negative, with the final value being positive.

When complete, the autopilot gyro calibration is verified by turning the gyro table at 90 deg/s and verifying the measured values are within an acceptable range of the expected rate of the turntable.  The following wording is the only acceptance criteria for the gyro calibration:
Verify this is correct by turning on the gyro table and ensuring that the corresponding value is ~90 degrees/second.


The problem with the above portions of the procedure is that techs do not have hard acceptance criteria.  The decision to pass or fail a board based on gyro calibration is entirely left up to the technician to decide what is acceptable.  Hard limits need to be specified for production to properly screen boards.
Of note is that when a gyro is slightly off level, the calibrated gyro will show nonzero values on the axies that are not turning when set on a turn table.  For example, when turning on the pitch axis, the pitch might show 90 deg/s while roll shows 1.2 deg/s and yaw shows 0.0 deg/s.  This would indicate a slightly misleveled IMU as the

## Comments (23)

### Greg Fryer, 2023-07-10

@Cameron Chapman @Former user @John Clark @David Grosher Please review ASAP, so we can determine which area is most impacted, or if this is going to be equivalent to the red AP activity. Might be interesting to look at an old green AP, see if the mounting is the same (I wager it is) and this is another spot where things were known to be ignored.

### John Clark, 2023-07-11

@Greg Fryer I have reviewed. Whom ever wrote this up (Ryan Ferguson?) did a fine summary, IMO. For the ACC the problem seems to be the mounting. For the Gyro, the mount for the test? “when a gyro is slightly off level, the calibrated gyro will show nonzero values on the axies that are not turning when set on a turn table.” I would suggest a different procedure and perhaps a test fixture could be developed. Or as suggested, accept wider margins. If wider margins are to be accepted, then possible software impact would be difficult to assess because there is no formal data related to any of the IMU’s I have ever seen. That seems hugely problematic.

### Ryan Ferguson, 2023-07-11

The problem with this situation is that such a test fixture would be very difficult to develop.  The alignment here isn’t in the range of 10’ths of an inch, it’s approximately 10 thousandths of an inch.  We do not have an easy way to ensure this using standard removable 3D printed jigs.  Additionally, the MPU9250 may be soldered to the MagAcc2 board slightly off angle which would further increase error during checkouts.  This is a failure mode we cannot control in house as it is soldered by Sierra.  
If we wish to mechanically remove failure modes, I believe the best method would be to redesign the MagAcc2 module so it uses a 3D printed mount that covers far more surface area than the standoffs.  This would in theory move all of the alignment and mechanical support to the 3D printed mount rather than relying on the headers and standoffs to keep consistent lengths.  The downside to this method is increased weight and engineering time spent designing the support.

### Cameron Chapman, 2023-07-11

I agree this is an issue. Thanks Ryan for the detailed write up. @Maxime Jeanneau has worked on it, maybe @Garrett O'Neill as well. @Maxime Jeanneau can you please work with @Ryan Ferguson to determine and summarize recommendations for how to address this issue (I suggest a separate Investigation Plan section in the description). Leaving in new state in case we want to discuss in the next meeting.

### Maxime Jeanneau, 2023-07-17

So far worked with @Ryan Ferguson to go through the calibration procedure and have definitely seen failed results working with one board, APB-10494. One observation made pretty early on was that the accelerometer board (shown as silver with a B2B connection in the images) moves slightly when pushed. It appears to be mounted with RTV and plastic fasteners which is different from the last picture shown above.
Leading theory here is that the accelerometer board is moving slightly during calibration and which throws off  the results.
I tried securing the accelerometer board better using rubber bands during the calibration but so far have had the same failing result. I just bonded the standoffs with dp270 by making a fillet around the standoffs to add support. Will try this tomorrow once it cures. I will also try to track down a passing board to compare results and see if the same play in the RTV is present.
[embedded: IMG-6161.jpg]

### Maxime Jeanneau, 2023-07-17

One interesting observation is when checking the calibration, I’m able to get passing cal values by applying downward pressure on the accelerometer board (the RTV feels a bit spongy/springy)

### Maxime Jeanneau, 2023-07-18

@Ryan Ferguson brought up a good point on the datasheet of the accelerometer sensor MPU-9250 (see linked)
[embedded: PS-MPU-9250A-01-v1.1.pdf]
Manufacturer specification for “Zero-G Initial Callibration Tolerance” is listed as: 
 +/-.06g for x and y axis
and +/-.08g for z axis 
This would make our .002g callout in the procedure way overly specified compared to what the manufacturer would expect for this product.

### Greg Fryer, 2023-07-19

@Maxime Jeanneau @Ryan Ferguson I don’t think the 0.06/8g chip tolerance is super relevant, in that we are calibrating it out and then doing a check. There is probably another tolerance that is relevant, but it appears tighter if 0.004g (which is still an order of magnitude tighter) still works.
I’m going to authorize the change (talk to production/leadership this AM), and have sent a question to Gordon to confirm. It really comes down to the AP sensitivity in code, and the variability after calibration.

### Maxime Jeanneau, 2023-07-19

I’ve been taking data on a few autopilots tested so far: the same autopilot, one with just RTV bonding the standoffs one with RTV with DP270 supporting. I got slightly better results with the DP 270.


[embedded: Accelerometer Error by Orientation.xlsx]
[embedded: Capture.PNG]
I think we should continue recording this data in a similar manner on future autopilot calibrations, especially until this issue is resolved. 
It appears like the three main sources of error that I suspect are affecting our results: 
- Motion of the autopilot board mounted with the accelerometer board relative to the Jig (motion within the rails of the 3d printed jig)
- Motion of the autopilot board relative to the accelerometer board (Standoffs/RTV)
- Non parralelism of the jig (if each orientation is not exactly parallel, trapezoidal).


From what I understand the mounting of the accelerometer relative to the autopilot board should be corrected for during the calibration. 
To be tested today is:
- Epoxy only mounting the standoffs (board preped by Liam overnight)
- Epoxy potting the entire board
- Special attention will be made to seeing any motion of the autopilot within the fixture

### Desiray Johnston, 2023-07-19

@Greg Fryer 
Current process
The Forward Flight autopilot first goes through the build and flash procedure, document 110115.  This step has techs solder some components to the board and load firmware.  The next procedure, document 110354, continues to load config files to the AP and set it up for burn-in which happens in document 110065.  After all of this is done, the board is now ready for the IMU calibration process.  In all, this likely takes approximately 2 hours of tech time per board and an overnight burn-in to get to this point.
 
The IMU calibration procedure, Document 110640, and the calibration sheet (document 107786) discuss how to calibrate both the gyros and accelerometers in the Green AP.  Techs start by setting up the gyro rate table for 90 deg/s and loading some configuration files to the AP.  The initial gyro offsets are set in the configuration by letting the autopilot sit still and adjusting the offset to zero out the gyro.  Techs then test the magnetometer before setting up for the accelerometer calibration.
 
Calibrating the accelerometer is a much more manual process than that of the Red AP.  The tech leaves the IMU on the leveled calibration table and notes the measured maximum value for the axis being tested.  The jig is rotated to each of its 6 faces to get a min/max value for the accelerometer on each face.  Once done, the data is copied into a spreadsheet which then calculates the span and offset values for the accelerometer.  The data at this point will show something like this:

 
At this point is the first acceptance range specified for the accelerometer.  The procedure states that the span values should be “roughly 0.96 – 0.98.  There is a numerical limitation of the offset value of +/-0.128; if these values are outside of that, reject the board.”  Production has not seen an autopilot fail this test yet.
 
The span and offset values are then copied into the autopilot configuration and saved.  This is where the second acceptance range is specified.  “Verify this is correct by rotating the jig and ensuring that one value is roughly ~1G, and the others are roughly 0 (within +/- 0.002) in the instrument panel.”
 
Once the accelerometers are calibrated, techs proceed to the gyro calibration which has a much lower fallout rate and is not part of this discussion.
 
 
The problem
The second accelerometer acceptance range is the one which is causing production stoppages and a high fallout rate.  The majority of our autopilots do not fall in the very narrow range specified and are rejected at this step.  Approximately 2.5 hours have been put into the autopilot by the time this failure is found.  It is also common practice to reperform the calibration if it does not pass the first time.
 
Risk to aircraft
This topic was brought up with Carson and he mentioned the GCS doesn’t even report accelerometer values beyond one decimal place (1.1 G for example).  An autopilot would need to have a failure in the offset of at least 0.050 to even register in the GCS as more than a rounding error.  The autopilot may be able to see this error if VXE were operating in dead reckoning modes but I suspect this would be a non-issue for current VXE operations considering we do not currently support that capability.  An autopilot with significantly erroneous IMUs would be rejected by the span values specification in the previous step. 
 
Sources of error
Engineering has been primarily focused on finding the source of the error as previous batches appear to have never had issues with this specification.  Some error can be attributed to the mounting of the MagAcc2 to the autopilot as a non-parallel mounting can cause the accelerometer to fall out of spec.  Attempts to measure the amount of non-parallelism needed to create a failing result have been mixed, but initial measurements suggest having a side as little as 0.006” off of parallel will cause an autopilot to fall out of the +/-0.002 accelerometer spec.  This is approximately the thickness of 5 pieces of human hair.  This is such a narrow tolerance that production would not be able to meet it consistently without redesigning the MagAcc2 or using expensive custom fixturing which would introduce a number of other issues. 
 
An additional source of error which Engineering has been concerned with is the fixturing of the autopilot in the calibration jig.  This has not been an issue in the several years we have used the same jig.  I am in the process of designing a new one anyway to further remove this source of error. 
 
It is worth noting that simply pushing on the MagAcc while doing calibration can sometimes be enough to bring the results into a passing spec.  This indicates that the flex of the board may be enough to cause a board to be rejected.
 
Manufacturers datasheet
Looking at the datasheet for the MPU9250, the sensor in the MagAcc2, it seems we are also specifying a tighter acceptance criteria than the chip manufacturer can guarantee.  TDK specifies a tolerance of +/- 0.060 on the X and Y axis and +/- 0.080 on the Z axis.
Proposed solutions
There are several possible solutions to this issue.  The first is to invest significant engineering time around redesigning the MagAcc2 to be more parallel with the autopilot.  This however would likely result in us continuing to fail to hit rate goals while the board is redesigned and may not successfully solve the root cause.
Option 2 is to redesign the test fixture.  This already has unclear benefits as the current jig has worked for years without issue and still shows little sign of wear.  I am already redesigning it anyway so we can eliminate this possible cause.
The 3rd and most preferred option is to evaluate opening the tolerances in our procedures.  This has the biggest payoff to production as it could drop our fallout rates down to 20% or lower by specifying a tolerance of +/- 0.050

### Matt Philley, 2023-07-19

@Greg Fryer to be clear what is the acceptable range that Engineering is approving? Your comment below states “0.004”
[embedded: image-20230719-173701.png]
@Ryan Ferguson your proposed update to the procedure looks like “0.05”. We need to make sure these values align especially if we may update it again in the near future. 
[embedded: image-20230719-173745.png]
Procedure: Doc# 110640 (Where requirement is captured)
Traveler: Doc# 107786

### Matt Philley, 2023-07-19

@Ryan Ferguson Can we update the IMU Calibration Traveler (Doc#107786) to include capturing this acceptance value? That way we have a record of what acceptance value we used moving forward? That way we can collect some data as this investigation continues… even just a “Verified Axyz values remained with acceptable +/- 0.XXX range” check box

### Ryan Ferguson, 2023-07-19

I can update the traveler as well.  I can add a field for the maximum deviation from zero seen so we can record that for later use.  I know @Maxime Jeanneau is also partnering with Liam to gether the values of a small batch to get more information.
I put the 0.050 value in there per a management decision but can change it again if we determine another value is necessary.

### Ryan Ferguson, 2023-07-19

The calibration traveler and SN spreadsheet have been updated to capture the maximum and minimum deviation from zero when doing checkouts.  This will help do time series studies on this issue should it arise again in the future.

### Maxime Jeanneau, 2023-07-19

Path forward, we are running through all the autopilots that have not passed the accelerometer calibration test and recording the pass/fail values in a spreadsheet approximately looking like: 
[embedded: faafa.PNG]
We will then evaluate based off of the data how much we need to expand the tolerance from +/-.002 noted on the procedure.

### Greg Fryer, 2023-07-19

I’ve got the math from Gordon, and found the typical and limits that Carson implements in SCO (this same value gets calibrated in the plane during attitude calibration). The typical max there is about 1.5 degrees (which would be 0.026g), but he has seen as high as 3 and 4 and had it work. (higher values than that, and things don’t work).
So we need to try and hold it “about there”. I will look at the data from the existing rejects, and see  how it lines up with the above and give a new value. And will also document the rationale and math in Confluence for future reference.

### Ryan Ferguson, 2023-07-19

I have finished the initial prototype of the new style of calibration jig.  Below are the associated PN’s.
124-113211 - Top level assembly
124-113212 - Calibration fixture
124-113213 - Calibration clamping plate
[embedded: image-20230719-205302.png]
It does use 4 #4-40 x .172” brass inserts in the main fixture and 4 #4-40 x 5/8” thumbscrews to secure the clamping plate which holds down the autopilot.
I also intentionally designed the fixture to be very large to maximize contact area with the turn table, making an off-square condition less likely.  We are now trying to coordinate with the individuals responsible for the printers across the company to see who can print it first.

### Maxime Jeanneau, 2023-07-19

Data from 7 accelerometer calibrations came in, here is a chart of where we are currently at: 
[embedded: Accerlerometer Error by Autopilot Serial Number.PNG]
(Data in spreadsheet here): 
[embedded: 07192023accelerometerErrorData.xlsx]
@Greg Fryer got numbers/formulas from Gordon equating .001G error in this step equates to .057 degree error during SCO roll/pitch/yaw check. @Carson Buckley Cmentioned he can calibrate with up to 3-4 degree error however this is after the avionics box is installed in the vehicle (installation can increase error). A .035 discrepancy in this step would equate to 2 degree error seen in the vehicle (more after installed).  We will move forward with installing the passing autopilots to this new tolerance (all of them) and monitor/record their performance during Carson’s SCO checkout.

### Ryan Ferguson, 2023-07-19

The procedure has now been updated to indicate +/- 0.035 as the new acceptance criteria.  I will also make some updates to the traveler and SN list in Condor to better capture the values Engineering wishes to record.

### Ryan Ferguson, 2023-07-19

The traveler has been revised to include a check box for recording the accelerometer data in the SN list on Condor for later review.  I also moved the spreadsheet made by @Maxime Jeanneau and @Liam Limon into a separate sheet in the SN list so we can record all of the data in one location.  

 @Maxime Jeanneau  Would it be possible to have you review the procedure and traveler and push them through the release process if acceptable?  They are in the Vault in documents 110640 and 107786 respectively.   I did also remove the checkboxes in the traveler for MagAcc vs MagAcc2 as the obsolete MagAcc has been out of production for over a year now.  Leaving the question in at this point would only cause confusion to those who are unfamiliar with the autopilots.

### Carson Buckley, 2023-07-20

@Maxime Jeanneau SN 10472 looks to be the outlier of this dataset, so I will focus on the calibration of that AP when it arrives. If 10472 checks out fine, then 0.035 should be satisfactory.

### Ryan Ferguson, 2023-07-24

I have finished off the print of the new autopilot calibration jig this morning.  I checked it against the granite table for squareness and it seems one side is slightly off square.  I have @Liam Limon doing a side by side comparison of the new jig against the original to see if we get a different set of results between the jigs.  If the MPU is able to measure the amount of error present in the jigs I’ll see if we can sand down the new jig to be square.

### Maxime Jeanneau, 2023-07-26

@Carson Buckley has processed 4 autopilots that we passed with the expanded accelerometer calibration tolerance, including the AP that scored the worst (10472) see: \\condor\Production\Lists\SN Lists\965-1-01-2004 XE25 Autopilot 0002P01, SN List. 
So far the largest offset was 1.0 degree, for the AP serial number that calibrated the worst 10472 (max .031g error). Carson mentioned this is in bounds and did not hold up system checkout. 
This is evidence that the new +-.035 tolerance for this calibration step is appropriate.

## Attachments (12)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20230710-181006.png | image | 2624 | 2023-07-10 | listed only |
| image-20230710-181025.png | image | 3031 | 2023-07-10 | listed only |
| IMG-6161.jpg | image | 1810 | 2023-07-17 | listed only |
| [PS-MPU-9250A-01-v1.1.pdf](attachments/15495_PS-MPU-9250A-01-v1.1.pdf.md) | pdf | 940 | 2023-07-18 | converted |
| [07192023accelerometerErrorData.xlsx](attachments/15516_07192023accelerometerErrorData.xlsx.md) | xlsx | 19 | 2023-07-19 | converted |
| [Accelerometer Error by Orientation.xlsx](attachments/15507_Accelerometer%20Error%20by%20Orientation.xlsx.md) | xlsx | 16 | 2023-07-19 | converted |
| Accerlerometer Error by Autopilot Serial Number.PNG | image | 48 | 2023-07-19 | listed only |
| Capture.PNG | image | 34 | 2023-07-19 | listed only |
| faafa.PNG | image | 25 | 2023-07-19 | listed only |
| image-20230719-173701.png | image | 16 | 2023-07-19 | listed only |
| image-20230719-173745.png | image | 17 | 2023-07-19 | listed only |
| image-20230719-205302.png | image | 130 | 2023-07-19 | listed only |
