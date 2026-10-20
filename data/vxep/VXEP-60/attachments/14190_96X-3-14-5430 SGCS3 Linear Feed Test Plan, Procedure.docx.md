# 96X-3-14-5430 SGCS3 Linear Feed Test Plan, Procedure.docx

Attachment 14190, docx, 12261 KB, added 2023-04-25 by Cameron Chapman.

TEST PLAN

SGCS-3 Linear Feed Test Plan

SCOPE:

This procedure defines the test plan for the proposed SGCS-3 linear antenna feed.

BILL OF MATERIALS

| ITEM # | DESCRIPTION | PART NUMBER | QTY | UNIT MEAS | Vendor | Vendor Part Number |
| 1 | Linear S-Band Feed |  | 2 |  | Epsilon |  |
| 2 | Linear C-Band Feed |  | 2 |  | Epsilon |  |
| 3 | SGCS-1 |  | 1 |  | EA |  |
| 4 | SGCS-3 |  | 1 |  | EA |  |
| 5 | VXE30 IN BATT. CONFIG |  | 1 |  | EA |  |

TOOLS REQUIRED:

SUMMARY:

Two stations need to be established, a remote station and a local station. The local station handles vehicle launch and recovery. The vehicle will orbit above the local station and ensure C2, command and control, is maintained throughout the test. The remote team needs to be setup at the maximum range possible while maintaining line of sight. On the side of a hill is optimal to avoid interference from ground clutter. At 100 km, the vehicle will need to be 3000’ AGL or higher with flat terrain between the two stations due to the horizon.

Throughout the test we will be switching the remote radio on and off to swap feeds. For safety it is important that the local station has control of the vehicle before the remote radio is switched off. Maintaining communication between the ground teams is critical.

SETUP:

Plan a mission which allows for maximum line of sight distance. Vehicle altitude should be at least 3000’ AGL to avoid ground clutter. In the example below, ground stations were established on either end of a valley.

Figure 1 Example Test Range

Station at either end of a valley, GCS on a hill, vehicle orbiting near local station

Figure 2 Remote Ground Station on Hillside

We will refer to the two ground stations as LOCAL and REMOTE.

LOCAL should be setup for vehicle launch and recovery. The vehicle will orbit above the local station and ensure C2, command and control, is maintained throughout the test.

REMOTE should be setup at the other end of the test range, preferably on the side of a hill to avoid interaction with ground clutter.

LOCAL: Setup SGCS-1 and VXE30. Power vehicle and connect to ground station.

REMOTE: Assemble SGCS3 in its standard configuration.

LOCAL: Perform a spectrum scan and tune radios to a relatively clean frequency around the center of the -, . Relay this frequency to the remote team.

REMOTE: Configure radio with new frequency.

BOTH: Select 5 bandwidth.

BOTH: Ensure beamforming is enabled.

LOCAL: Set turret to mb multicast video.

LOCAL: Open the Silvus Streamscape network manager and check radio throughput. For more information refer to the appendix at the end of this document. With both streams running it should be approximately Mbps between LOCAL and VXE30. You should leave this window open in a tab throughout the test.

REMOTE: Attempt to acquire the vehicle while it is on the ground.

LOCAL: Launch vehicle and fly to altitude.

REMOTE: Acquire vehicle and open the turret stream. Open the Silvus  network manager and check radio throughput. For more information refer to  at the end of this document. It should be approximately 4 Mbps between REMOTE and VXE30. You should leave this window open in a tab throughout the test.

REMOTE:

TEST  :

REMOTE: Power off the SGCS-3 radio, and swap the dish feeds out for the linear -Band feeds. The arrow should point up for this step of the test.

REMOTE: When the dish has been reassembled, power the radio back on and attempt to recover turret video.

REMOTE: If comms cannot be reestablished: Power down the radio, swap back the original feeds, power the radio back on, and attempt to recover the stream. If stream recovers, proceed to next test. If stream does not recover, check for interference by performing a spectrum scan and changing frequencies.

REMOTE: Fill out the contact report using the average data over an orbit.

REMOTE: Power off the SGCS-3 radio and rotate the  45 degrees.he arrow should point up and right for this step of the test.

REMOTE: When the dish has been reassembled, power the radio back on and attempt to reconnect to the vehicle.

REMOTE: If comms cannot be reestablished: Power down the radio, rotate the feeds back to the arrow up configuration, power the radio back on, and attempt to recover the stream. If stream recovers, proceed to next test. If stream does not recover, check for interference by performing a spectrum scan and changing frequencies.

REMOTE: Fill out the contact report using the average data over an orbit.

REMOTE: Power off the SGCS-3 radio, and swap the dish feeds out for the linear -Band feeds. The arrow should point up for this step of the test.

REMOTE: When the dish has been reassembled, power the radio back on and attempt to reconnect to the vehicle.

REMOTE: If comms cannot be reestablished: Power down the radio, swap back the original -Band feeds, power the radio back on, and attempt to reconnect with the vehicle. If stream recovers, proceed to next test. If stream does not recover, check for interference by performing a spectrum scan and changing frequencies.

REMOTE: Fill out the contact report using the average data over an orbit.

:

REMOTE: Power off the SGCS3 radio and rotate the dish feeds 45 degrees. The arrow should point up and right for this step of the test.

REMOTE: When the dish has been reassembled, power the radio back on and attempt to reconnect to the vehicle.

REMOTE: If comms cannot be reestablished: Power down the radio, rotate the feeds so the arrow points up, power the radio back on, and attempt to reconnect with the vehicle. If this fails restore dish in standard SGCS-3 -Band configuration. If stream does not recover, check for interference by performing a spectrum scan and changing frequencies.

REMOTE: Fill out the contact report using the average data over an orbit.

APPENDIX A – USING SILVUS STREAM SCAPE NETWORK MANAGER:

Login to the web page of the radio under test. The IP address can be found on the front of the radio mounted to SGCS-3.

Once the web page opens, click the StreamScape Network Manager tab.

The network manager provides a graphic representation of the radio’s status and peers. Each dot or ‘node’ is a radio in our network. The lines between represent the connection quality with the labels showing the signal to noise ratio, SNR. The higher the SNR, the better the quality of the signal.

Node labels can be changed to make things easier to read. Click on the label to rename. Press enter to save.

To get more information on a radio, double click on the node. A new window will open with metrics specific to that station.

For our data collection, we are interested in data sent from the VXE30 node. Double click on the VXE30 node to open a popup window.

As an example, below we compare the data rate with the SA camera feed open and closed. With MediaClient connected to the stream, the data rate increase to approximately 1 Mbps.

Fill out the “Contact Report” using the data from the popup window. Relevant fields are shown below. We only want the data transmitting from the VXE30 and received by the SGCS-3 ground station. Make sure you record data from the correct pop-up window and row.

If video isn’t playing smoothly and the air-time is around 100%, too much data is being pushed over the link at the current settings. You can try switching to 10 bandwidth and see if video quality improves, however, this will only work if the signal strength is above a minimum threshold and is no guarantee.

APPENDEX B – PERFORMING SILVUS SPECTRUM SCAN

Login to the web page of the radio under test. The IP address can be found on the front of the radio mounted to SGCS-3.

Click the “Spectrum Scan” menu tab.

When the page loads, click the settings hamburger menu icon (three stacked, horizontal lines) highlighted in red below.

Settings Icon

Choose your scan settings. In this example we will evaluate 2400-2500

Check the box with the name of the vehicle’s radio

Enter the center of the scanning range, in this example, 2400

Enter the span of the scan, in this example, take 2500 - 2400 which gives = 100

Choose all antennas.

Set the resolution bandwidth to 625 kHz.

Set the threshold to 5 dB, any interference above this level will have its duty cycle reported on the threshold plot.

Leave the duration set to 1s

Scan Settings

A report resembling the plots below should render after a few minutes.

Scan Results

If  is emitting in the radio spectrum, peaking will be visible in the “Peak” plot. In the spectrum scan above, interference can be seen both in the “Average” plot and the “Peak” plot above 2400 . Any frequency below this should be adequately free of interference.
