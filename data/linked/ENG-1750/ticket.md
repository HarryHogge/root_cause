# ENG-1750: MPU-9250 Chips have high failure rate, are obsolete, and have a high rate of conterfeits.

- **Issue type:** Engineering Change
- **Status:** Moved to SolidWorks Manage
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2023-05-17
- **Updated:** 2026-08-05
- **Resolved:** 2026-08-03
- **Reporter:** Ryan Ferguson
- **Assignee:** Cameron Chapman
- **Creator:** Ryan Ferguson
- **Labels:** EndOfLife
- **Links:** relates to ENG-1752 (1409P01D VTOL AP improvements); causes ENG-1774 (Replace obsolete MPU-9250 accelerometer (FW AP and ADP). ); relates to VXEP-221 (VXE 398 Heading Data Appears Delayed Compared to Other Aircraft); relates to VXEP-1827 (Air Data Board - Failures); relates to VXEP-1971 (VXE 885 Erratic behavior in flight caused crash)
- **Part Number(s):** MPU-9250
- **Supply Chain Stakeholder:** Perry Richardson
- **Problem Type:** Production Issue

## Description

Recent batches of red autopilots (PN 1409P01D) have had a high failure rate.  Lawton has estimated these failure rates to be as high as 70%.  While digging into the causes of these failures, the MPU-9250 seems to be a common cause of roughly 2/3 of those failures.
Looking at a project which relies on IMUs and their reliability, SlimeVR is a project which uses IMUs in VR.  Hundreds of people have built their own trackers, all of which require anywhere from 6 to 10 IMU’s.  As a result, they have a pretty good comparison of different IMUs available on the market driven by large amounts of experience.  This page of their documentation lists the MPU-9250 with the following comment:
“Finding legitimate MPU9250s has become exceedingly difficult due to counterfeits and DOA IMUs. Buy at your own risk."

Winsource also lists this chip with a very high counterfeit rate.  They estimate 78% of these chips available in the open market are counterfeit.  The MPU-9250 is also obsolete, with online sources pointing to an EOL date sometime in 2018.

Based on the unreliability of the MPU-9250 in this related project and our current issues in production, it may be a good idea in the short term to send some of our IMU’s to be decapsulated to determine if they are counterfeit chips.  It may also be a good practice to send a subset of any future MPU-9250 chips purchased to be decapsulated as well to determine authenticity.

This issue affects the MagAcc2 board on the Green AP, the VTOL AP, and the Air Data Board.

Part Number Summary:
100-110018 - IMU ACCEL/GYRO/MAG I2C/SPI 24QFN (Vendor PN: MPU-9250)
Where-Used:
- 107-107307 - Processed 1409P01D, VXE Autopilot [Centerwing]
- 1409P01D - VXE Autopilot (Unprocessed)
- 107-103560 - Processed Air Data Board Assy [Air Data Pod Assy]
- 1502P01D - Air Data Board (Unprocessed)
- 107-103101 - Processed Mag Accel 2 Board [Avionics Enclosure Assy]
- 1710P01A - Mag Accel 2 Board (Unprocessed)


Proposed replacement IMU, the BNO085. https://www.adafruit.com/product/4754

In Progress: MPU-9250 IMU Replacement

## Comments (3)

### Ryan Ferguson, 2023-05-19

I have done some testing and investigation on this front.  My first goal was to figure out if the failure modes were replicable.  I’ve gone through the batch of 8 that Lawton had fall out during this batch and powered them on to see if I could replicate the issues Lawton noted.  Below are the SN’s of these autopilots.
1259 - No Sensors, Lost Connectivity 
- I was unable to log into this autopilot.  Further testing is needed to see if it may have changed IP addresses or if the filesystem was corrupted.

1294 - Mag Fail 
- I was unable to log into this autopilot.  Further testing is needed to see if it may have changed IP addresses or if the filesystem was corrupted.

1297 - Mag Fail
- The board appeared to work normally with functioning outputs on the MPU9250.  Since there’s a possibility of intermittent failure, this board was kept out of production under NCR-1021.
- Additional details about this board are below.  It was chosen to have its MPU removed to see how the autopilot responds when no IMU is present.

1303 - No 192 Network
- I was unable to log into this autopilot.  Further testing is needed to see if it may have changed IP addresses or if the filesystem was corrupted.

1305 - Tried New SD Card - Board Will Not Format Any Card
- I was unable to log into this autopilot.  Further testing is needed to see if it may have changed IP addresses or if the filesystem was corrupted.
- Lawton noted he swapped multiple SD cards and was unable to get it to format properly.

1305 - Mag Doesn’t Work - MPU 9250
- The MPU-9250 shows values of 0.0000 and will not change even when exposed to a magnet.

[embedded: APC-1-1305.PNG]
1309 - No Bootloader - Red LED Broken? 
- This board does in fact seem to have bootloader issues.  More testing required to see if it can be fixed by reflashing

1310 - 9250 Mag Fail
- This board seems to have defaulted to the external mag for some reason.  The config page has the external mag value set to “Off” just like the other boards, yet it somehow is showing the external mag rather than the MPU-9250.
- The sensor priorities are also consistent with the other boards.  No other changes have been made between this board and APB-1-1297.
[embedded: APC-1-1310.PNG]
[embedded: image-20230519-185245.png]



MPU-9250 Removal
Board 1297 was chosen to have its MPU removed to see how an autopilot responds to a nonexistent MPU.  Personal experience has shown that counterfeit MPUs will sometimes not respond to any data, so we needed to see how the autopilot would respond to this failure.  Linda was able to remove this chip without disturbing any nearby components.
Before removing the chip, the MPU values were seen to be operating like normal.  See the below image for an example of this functioning state.
[embedded: Magnetometer Page Pre-Removal-20230519-163301.PNG]

The MPU-9250 was removed and all solder pads cleaned using acetone.  
[embedded: image-20230519-184303.png]

After removal, the board was once again loaded up to see how the webpage now responded.  The webpage now shows 0.0015 values for all of the Bxyz values.  
[embedded: Magnetometer Page Post-Removal.PNG]
After doing a few reboots of the autopilot, the Bxyz values now show 0.0000.  The LSM9DSx still shows values that respond to differing magnetic environments.  This is consistent with some of the previously seen failures.  

Findings 
If an autopilot responds with all 0.0000 or 0.0015 values, it can be assumed the MPU-9250 is non-responsive and is not sending data to the autopilot.  This could also be due to other component failures but has not been verified.
More investigation needs to be done on the external mag priorities in 1310.

### Cameron Chapman, 2023-05-22

Ideas discussed with Ryan. Will create subtasks
- Separate inventory based on source. Investigate if failure rate differs between the sources.
- Develop screening tests to identify counterfeit chips.
- Evaluate methods to safely remove and replace chips once installed. Send back to Sierra? (pads under component are hard to solder and inspect).
- Ryan reports that a disconnected magnetometer may lock up the FWAP. Need to test to verify .

### Christa Meck, 2026-08-03

RDW-ECR0095

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| APC-1-1305.PNG | image | 44 | 2023-05-19 | listed only |
| APC-1-1310.PNG | image | 43 | 2023-05-19 | listed only |
| Magnetometer Page Post-Removal.PNG | image | 44 | 2023-05-19 | listed only |
| Magnetometer Page Pre-Removal-20230519-163301.PNG | image | 44 | 2023-05-19 | listed only |
| image-20230519-184303.png | image | 2135 | 2023-05-19 | listed only |
| image-20230519-185245.png | image | 78 | 2023-05-19 | listed only |
