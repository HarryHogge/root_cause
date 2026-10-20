# AHRS Report.pdf

Attachment 10970, pdf, 654 KB, added 2022-09-27 by Cameron Chapman.

## Page 1

09/27/22 Edge Autonomy Proprietary Information 1  
 
 
 
 
AHRS Report 
 
 
On Differences Using New SBG Systems AHRS Firmware 
and Hardware Versions 
 
 
 
September 27, 2022 
C. Peebles

## Page 2

09/27/22 Edge Autonomy Proprietary Information 2  
0. NEW AHRS VERSIONS 
 This report is a summary of the differences between versions of the SBG-Systems AHRS 
boxes. We are now receiving new hardware versions of 3.2, while previously we had been 
receiving hardware versions around 1.2. Validation reports that highlight these differences are 
show below in Figure 1.  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
1. DIFFERENCES 
 An interesting thing to note is that the 3.2 AHRS has an older Firmware version than the 1.2.  
The next few things to note are in the settings of the AHRS that we adjust here with their 
program sbgCenter. Notably in Data Output, Port A of the settings. The 3.2 AHRS excludes the 
‘Ship Motion’ output for aircraft that is in the 1.2 AHRS. This outputs heave, surge, and sway. 
Next the 3.2 AHRS includes a new ‘GPS RAW Data’ that is not in the 1.2 AHRS, see Figure 2 
below. This log is used to store raw GPS data for post processing purposes. It stores directly 
Figure 1: The validation reports with summaries of the version of AHRS that come with the product. The old one (1.2) is on the left and the new one (3.2) 
 is on the right

## Page 3

09/27/22 Edge Autonomy Proprietary Information 3  
untouched binary messages that are relevant for post processing from the GNSS receiver. Each 
message can store up to 4096 bytes of raw GNSS data. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Figure 2: Data Output Settings for the 1.2 AHRS on the left and the 3.2 AHRS on the right.

## Page 4

09/27/22 Edge Autonomy Proprietary Information 4  
 I am contacting SBG-Systems about these differences but they really shouldn’t affect us 
until we decide to launch a stalker off a boat. 
 The last difference I noticed was that after the settings were set, the GNSS1 Position and 
Velocity soluctions were computed with ‘Single Point’ and ‘Doppler’ respectively which is 
different than what is shown in the configuration procedure here. The procedure shows the 
computations as being ‘Differential’, see Figure 3. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
I think this is because we don’t have a have ‘Known Location’ set up here at Buckley on the E-
shop Ironbird (I speculate). I’m guessing the ground control station becomes the Known 
Location once it is in a configured plane.  
 These solutions may vary in how they are computed but basically they all get the same 
job done, with varying degrees of accuracy where differential is the most accurate as it is more 
of a correction using a reference point. 
Figure 3: GNSS 1 Position and Velocity showing solutions computed. The on the left is what the procedure shows it should be and the right is 
what I was getting with the 1.2 AND 3.2 AHRS here in the E-shop at Buckley

## Page 5

09/27/22 Edge Autonomy Proprietary Information 5  
 
 
3. CHANGES 
 Because of the differences in the Data Output settings, the old .bin file we were using 
would not configure onto the 3.2 AHRS (it still would on the 1.2). So we set up a .bin 
configuration file for each 1.2 and 3.2 AHRS, as seen in Figure 2, found here: 
‘C:\JAI Vault 1\Projects\111 - MOD Payload\Electrical Design\111-104685 AHRS Resources’ 
Editing could be done to this procedure to include the part about the different configurations 
depending on the version of the AHRS as well as the differences between the types of Solution 
Computing. 
 
4. SUMMARY 
 The 3.2 AHRS and configuration tested with the MOD payload on the Iron Bird perfectly 
fine. Ofcourse more testing would be dilligent and I am not aware of how they are tested once 
installed in a plane.  
We are just waiting for SBG-Systems to get back to us on the differences.
