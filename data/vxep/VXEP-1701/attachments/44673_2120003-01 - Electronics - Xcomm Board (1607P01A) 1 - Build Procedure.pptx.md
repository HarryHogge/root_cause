# 2120003-01 - Electronics - Xcomm Board (1607P01A) 1 - Build Procedure.pptx

Attachment 44673, pptx, 114377 KB, added 2026-02-19 by Ben Norris.

## Slide 1

ProcedurePart Number:		2120003-01Assembly Revision:	DDescription:		XCOMM Board
Procedure Revision: F
09 February 2026
[picture]
UNCONTROLLED WHEN PRINTED

DATE PRINTED:__2/13/2026__

PRINTED COPIES ARE ONLY VALID FOR 24 HOURS FROM THE PRINT DATE UNLESS MARKED “CONTROLLED COPY” IN RED INK.
COPIES OF THESE CONTROLLED DOCUMENTS ARE NOT AUTHORIZED.
[picture]
2026-02-09
Redwire Proprietary Information
1

## Slide 2

Revision History:
| Rev | Description | Date |
| A | Original Release. | 2022-11-01 |
| B | Updated step 4 to account for resistor variations between Sierra and SPM Xcomms. | 2024-03-18 |
| C | SD card updates, new PN per ENG-2735 | 2024-10-22 |
| D | Industrial SD Card w/ UV Cure Adhesive | 2025-01-03 |
| E | Updated SD card part number, no UV cure required | 2025-08-25 |
| F | Combined all 3 procedures into one and updated to current process | 2026-02-09 |
2026-02-09
Redwire Proprietary Information
2

## Slide 3

[picture]
Tools and Supplies:
Tools: 
Soldering Station
Multi-meter
Supplies: 
Black RTV
Conformal Coat
[picture]
2120003-01
[picture]
2119959-01
[picture]
107-111718
[picture]
= This Procedure
[picture]
107-103798
Family Tree:
2026-02-09
Redwire Proprietary Information
3

## Slide 4

Safety Information: 
Personal Protective Equipment (PPE): 
General – Wear disposable gloves.​

Safety Guidelines:
General – Do not ingest small parts due to choking hazards. Stay alert to sharp edges and corners of assembly materials.
Heat Gun ​ – Keep flammable materials away from the heat gun. Keep the heat gun away from skin.
Epoxy and Adhesives – Do not ingest, inhale, or touch epoxy and adhesive materials.

In Case of Emergency: 
Seek immediate medical attention and inform supervisors of work-related injuries.
[picture]
2026-02-09
Redwire Proprietary Information
4
i
Intro:
This procedure is for new boards, that haven’t had anything loaded onto them. If you are troubleshooting a bricked board, work with someone who has experience troubleshooting them. 
This procedure covers installing the bootloader and firmware, as well as setting the configuration and formatting the on-board storage for the Power Comms (also know as the Xcomm2) board. 
When the software is initially loaded, the IP address of the Power Comms (XComm2) board is 192.168.10.70, so only computers configured as 192.168.10.XXX (standard for our office network) can talk to the board.  After the initialization configuration is loaded (and power is cycled), the board IP address will be 10.128.123.2, so only computers configured as 10.XXX.XXX.XXX (standard network configuration for vehicle components) will be able to talk to the board.
This procedure is to be done after the initial buildup.  Once complete, perform the Xcomm burn in procedure.

## Slide 5

Reference Documentation
BOM
C:\JAI Vault 1\projects\106 - stalker xe, block 25\electrical design\pcb\1607a01, xe240 block 25 power comms\2120003 Processed 1607P01A, X-Comm, BOM.xlsx

File Path References for Firmware and Config Software: Slide 17  Slide 24  Slide 25
C:\JAI Vault 1\Projects\107 - Stalker XE, VTOL Gen 2\Electrical Design\Firmware and Hex Files\965-1-01-2004 (1607P01A) X-comm Firmware and Configs\1607P01A X-Comm Current Production Firmware Version.txt

Label
C:\JAI Vault 1\production eng\4 - electronics\5 - labels\1 - serial labels\2120003-01 - Electronics - XCOMM Board - SN Label.lbx

Standard Operating Procedures						Document 2125238
C:\JAI Vault 1\Production eng\4 - Electronics\4 - Other Files\Standard Operating Procedures (SOP).docx
5
Redwire Proprietary Information
2026-02-09
Links will not work the first time, follow the computer path to find the file and open it, then the links will work
[picture]

## Slide 6

10
Paperwork and Kit Check
Pull the latest release documentation from the Vault:
	Document 2120003	BOM
	Document 2120008	Label

Verify contents of the Kit match the Drawing Requirements and are free of damage

✎ Record the As-Built Rev. in the Traveler.
2026-02-09
Redwire Proprietary Information
6
Build Procedure

## Slide 7

20
Apply a small dot of RTV to the XCOMM board where the battery will be attached
Do not allow the RTV to flow over the solder pads while placing the battery on the PCB
Solder the battery into place and clean residual flux from the PCB
Do not allow the battery to short while handling
✎ Measure the battery voltage and note it in the traveler. Battery shall be greater than 2.7V
Note: If the voltage is less than the 2.7V, try powering up the XCOMM through the Ironbird for a few minutes to recharge the battery. If the voltage of the battery is zero, this indicates a dead battery, and it should be replaced.
✎ Record the material lot number and expiration date in the Traveler.
✎ Record the tool asset number and calibration due date in the Traveler.
2026-02-09
Redwire Proprietary Information
7
[picture]
[picture]
[picture]

## Slide 8

20
Install the Industrial SD card (2120068-01) fully into the slot
✎ Record the SD card SN/lot number in the Traveler.
Apply a small amount of RTV to the top of the industrial SD card and use a plastic spreader to smooth out the material as shown above
Flip the board over and apply a long bead of RTV on the capacitor resting position as shown
Bend the legs of the capacitor and solder into place, ensuring the negative lead (shorter of the two, side with the grey stripe) faces toward the edge of the board  
Solder a 1.5” long piece of 22AWG bus wire over the capacitor as shown to secure it to the board
✘ DO NOT install capacitor backwards as this poses a risk to hardware and safety
2026-02-09
Redwire Proprietary Information
8
[picture]
[picture]
[picture]
[picture]
[picture]

## Slide 9

20
Verify that R162 is installed across pins 2 and 3 of Q13
Resistor should read either “101” or “1000” and have good solder joints
Clean all joints of flux using IPA and swabs
Apply a black 9mm label with part number and serial number on the board as shown above
✎ Record the XCOMM Board SN/lot number in the Traveler.
2026-02-09
Redwire Proprietary Information
9
[picture]
[picture]
[picture]
[picture]

## Slide 10

25
QUALITY INSPECTION
Inspect battery and capacitor solder joints.
[picture]
[picture]
2026-02-09
Redwire Proprietary Information
10

## Slide 11

30
Use a cotton swab to cover the battery and capacitor with conformal coat.
✎ Record the material lot number and expiration date in the Traveler.
[picture]
[picture]
2026-02-09
Redwire Proprietary Information
11

## Slide 12

[picture]
[picture]
Finished board
[picture]
[picture]
30
2026-02-09
Redwire Proprietary Information
12

## Slide 13

2026-02-09
Redwire Proprietary Information
13
Initialization Procedure

## Slide 14

40
Connect the board to be tested to the power connection and network connections on the Ironbird
Ensure the power supply is set to 28V and 3A
Connect the Pickit connector to the board at the J10 connector (near the SD)
Note: If the Pickit isn’t available see appendix A
2026-02-09
Redwire Proprietary Information
14
[picture]
[picture]
[picture]

## Slide 15

40
Press the button on the Pickit, the Pickit will start flashing purple, once it starts flashing green then the programming is done
Unplug the Pickit from the XCOMM
2026-02-09
Redwire Proprietary Information
15
[picture]
[picture]
Press Here
[picture]
[picture]

## Slide 16

40
Run the JAI AP bootloader interface software: apbl.exe
In the ethernet box, change the last octet of the IP address to 72 (the default is 71, which is the autopilot)
Note: Do not press the Enter key when finished, as it will close the program. Just change the number and click out of the IP settings window.
Press the “Connect” button and wait for the connection
Verify that the dialog reads “Device connected” and shows the bootloader version uploaded in the previous step
Note: You should see a green light by the XCOMM2 board ICSP connector
Note: If you are not working on a new board ( a board without software loaded), hit the reset button on the board by the J10 connector right before you press “Connect”
2026-02-09
Redwire Proprietary Information
16
[picture]
[picture]
[picture]

## Slide 17

40
Select “Load Hex File” button and browse for the Current Production Firmware Hex File referenced in the text file. Slide 5
Copy and paste, or follow, the path outlined in the text file to navigate the vault to the correct hex file
2026-02-09
Redwire Proprietary Information
17
[picture]
[picture]
[picture]

## Slide 18

40
Select “Erase-program-verify” and wait for the programming to complete.
Note: it takes about 100 seconds to complete the programming. You will see the blue light next to the J10 connector blinking during the programming process. 
When completed, the dialog will read “Programming completed, Verification successful” and the blue light will go off
Click “Disconnect” 
✎ Check off and record the bootloader firmware version on the traveler.
2026-02-09
Redwire Proprietary Information
18
[picture]
[picture]

## Slide 19

40
Reset the board using the reset button located near the J10 connector or by cycling the power to the board.
Wait 10 seconds, until you see blinking lights (red, blue, and green)
Using a web browser, navigate to the XCOMM2 page: 10.0.0.200
Note: if you cannot connect, try this address: 192.168.10.70
Login to the webpage using the standard credentials:
Username: stalker
Password: $talkerXE240
2026-02-09
Redwire Proprietary Information
19
[picture]
[picture]
10.0.0.200

## Slide 20

40
Verify on the webpage that the correct firmware is listed in the row labeled “Board” under the blue “System Information” section. 
Reference the text file for details on what the expected firmware version is
✎ Record the Main Firmware Version in the Traveler 
Note: On the “Document source” row, which is under the green “HTTP Connection” section, you will see “ROM”
2026-02-09
Redwire Proprietary Information
20
[picture]

## Slide 21

40
Click on the “Utilities” link at the bottom of the page
Click “Enter Utilities”
Open another browser tab and navigate to the XCOMM2 main page
Select “Messages” at the bottom to view the log
Note: having the two windows outlined in green side by side will make checking the status of the subsequent steps a bit easier
2026-02-09
Redwire Proprietary Information
21
[picture]
[picture]
[picture]
[picture]
[picture]
19
20
22
21

## Slide 22

40
Having the two windows side by side:
Click “Erase Flash Configuration”
✎ Verify that a message indicates “erase flash complete”
Click “Format Serial Flash” 
✎ Verify that you get “fmt: 0, mounted 2:, init: 0, flash format complete” 
Click “Format SD Card”
Note: the formatting process takes about 20 seconds.
✎ Verify that you get “fmt: 0, mounted 1:, init: 0, sd format complete”
Note: if this message doesn’t appear, or the process takes too long (longer than 45 seconds), there is an issue with the SD card.
2026-02-09
Redwire Proprietary Information
22
[picture]
[picture]
23
25
[picture]
[picture]
27
24
26
28
Note: The SD formatting and flash formatting look similar.  The “Mounted” label indicates which device was formatted.  Ensure the correct section is used for verification.
Mounted 1 - SD Card
Mounted 2 – Serial Flash

## Slide 23

40
Reset the board using the reset button located near the J10 connector or by cycling the power to the board.
Wait 10 seconds, until you see blinking lights (red, blue, and green)
Either reload the XCOMM2 webpage or open a new one: 10.0.0.200 and login
Verify that the “Document Source” row under the green “HTTP Connection” section now says: “SD1” instead of “ROM”
Click on the “Configuration” link in the bottom middle of the page
Click the “Upload/Copy” link in the top left-hand corner of the page
2026-02-09
Redwire Proprietary Information
23
[picture]
[picture]
[picture]
[picture]

## Slide 24

40
Click on the “Import config” link on the bottom right-hand side of the page
Check the box that says “ignore above settings, import all” 
Click “Choose File”
Select the Initial Configuration file referenced in the text file. Slide 5
Copy and paste, follow, or go up a level in the file explorer, to the path outlined in the text file to navigate the vault to the correct config file
Click “Import configuration file”
Wait a few seconds for the file to load
✎ Check off in the traveler for “initial config load”
2026-02-09
Redwire Proprietary Information
24
[picture]
[picture]
[picture]
[picture]

## Slide 25

[picture]
40
After loading the initial config file, select “Choose File” again. Reference the text file for the directory to the Current Firmware Config File. Slide 5
Copy and paste, follow, or go up a level in the file explorer, to the path outlined in the text file to navigate the vault to the correct config file
Wait a few seconds for the file to load. 
✎ Check the box in the traveler for “Production Config Load” and note the config file name
2026-02-09
Redwire Proprietary Information
25
[picture]
[picture]

## Slide 26

40
Click on the “Gains” link in the bottom right-hand side of the page
On the “XCOMM serial number” row click on the box and type in the board serial number from the label on the board (5-5XXX)
Click the “Save” button up at the top
Click on the “Upload/copy” link at the top of the page
Click the “Save Config” button in the lower portion of the page (towards the middle)
Note: you will see a blue loading bar as it saves. This only takes a few seconds.
Note: now that the board is configured, if it is restarted, the IP address will be 10.128.1.2 until is it connected to an Autopilot
2026-02-09
Redwire Proprietary Information
26
[picture]
[picture]
[picture]
[picture]

## Slide 27

40
Switch browser tabs back to the “Main” page and then click the “Log files” link at the bottom of the page
Click the “XCEVLOG.TXT” file
When the file downloads, open it, and scroll down to verify that the encryption key is there (scroll about halfway down the page)
2026-02-09
Redwire Proprietary Information
27
[picture]
[picture]
[picture]
Encryption key is the highlighted 8 lines of text

## Slide 28

40
Do not change the contents of the text file. 
Save the text file as the serial number (i.e. 5-5XXX.txt)
File
Save As
Enter \\condor\Production\HEX Files\XComm\Logs in the address bar
Change the File name to the serial number
Click Save
✎ Check off the save encryption key step on the traveler.
2026-02-09
Redwire Proprietary Information
28
[picture]
[picture]

## Slide 29

40
Navigate to the main XCOMM webpage and verify the following:
Board Firmware version matches that in the Current Production Firmware text file
Config CRC checksum matches that of the Current Production Firmware text file
Board serial number matches that of the label on the board
Tail number is set to 1
Document Source indicates SD1:/www/
✎ Check off the “Final Verifications” step in the Traveler and note the Config CRC
2026-02-09
Redwire Proprietary Information
29
[picture]

## Slide 30

2026-02-09
Redwire Proprietary Information
30
Burn-In Procedure

## Slide 31

50
Unplug AUX cables and ensure that nothing else is plugged in here
Feed the harnesses through the passthrough in the back of the oven
Plug the hole using split foam
2026-02-09
Redwire Proprietary Information
31
[picture]
[picture]
[picture]

## Slide 32

50
Plug in the banana plugs into the power supply located on top of the oven, ensure correct polarity
Verify that the power supply is plugged into a wall outlet that will not get switched off
Turn on the power supply and set it to 28.1V and 2.5A
✘ DO NOT connect X-comm boards until the power supply has been set up.  Failure to set the power supply can result in damage to boards.
2026-02-09
Redwire Proprietary Information
32
[picture]

## Slide 33

50
Load the XCOMMs into the oven and plug the test harnesses into each one
Acceptable to hot mate this connector with the PSU turned on
Ensure the lights on the XCOMMs light up after being plugged in
Note the labels on each test harness to be able to tell which one goes to each board
Test Harness #6 does not work
2026-02-09
Redwire Proprietary Information
33
[picture]
[picture]
X
[picture]
X

## Slide 34

50
Close the oven once it is fully loaded and place a sign on the door: Testing in Progress. DO NOT OPEN.
2026-02-09
Redwire Proprietary Information
34
[picture]
[picture]

## Slide 35

50
Select “Profile Actions” on the oven home screen
Select “Go to Profiles”
Find profile 2, “XCOMM”, and select actions
Select “Run Profile”
2026-02-09
Redwire Proprietary Information
35
[picture]
[picture]
1
[picture]
4
[picture]
3
[picture]
2

## Slide 36

50
Leave the oven undisturbed for at least 6 hours
It is acceptable to leave it running overnight
2026-02-09
Redwire Proprietary Information
36
[picture]

## Slide 37

50
Do not open the oven
Gather either your laptop or the loaner laptop and plug in an ethernet cable and adapter configured for an XCOMM 10. network
2026-02-09
Redwire Proprietary Information
37
[picture]

## Slide 38

50
Navigate on the laptop to the XCOMM interface at 10.128.1.2 using a web browser
Login in using the default credentials
Username: stalker
Password: $talkerXE240
Verify the system time field says a minimum of 6 hours
Any less than 6 hours, as pictured above, is considered a failure and requires a retest or NCR
If testing a batch of boards, ensure you are looking at the matched board and traveler by using the numbers on the burn in harnesses matched with the ethernet ports you are plugged into as you test each board
2026-02-09
Redwire Proprietary Information
38
[picture]
[picture]
[picture]
X

## Slide 39

50
If the board successfully passed, disconnect the laptop
Flip the main power switch to turn off the power supply to the XCOMM
Demate the XCOMM from the test harness
Bag the boards individually in silver shielded ESD bags in a pink poly bag with the traveler
Clean the workspace and put away all test harnesses
Turn off the oven and return the loaner laptop to its appropriate location
🔍 Submit for closeout QC inspection.
2026-02-09
Redwire Proprietary Information
39
[picture]
[picture]
[picture]

## Slide 40

[picture]
[picture]
Appendix A: Bootloader Program Install, if there is no Pickit
A
Open the Real ICE software: MPLab IPE v4.05
Select “Settings” in the top toolbar, followed by “Release from reset.”
[picture]
In the “Operate” menu pane make sure the following settings are correct:Family: 32-bit MCUs
Device: PIC32MZ2048EFM144
➤ Note: The “Tool” setting will auto-select the correct setting. Also, if the device is already set correctly, there is no need to set the family dropdown. The family selection just narrows the list that populates on the device dropdown. 
Click the “Apply” button, followed by “Connect.”
Wait a few seconds.
 ➤ Note: if you get a red error message in the dialog, or it fails to connect, try unplugging and reinserting the USB cable to the programmer (Real ICE).
A
2026-02-09
Redwire Proprietary Information
40

## Slide 41

[picture]
[picture]
[picture]
A
Select “Browse” next to the “Source” menu. Upload the correct Bootloader File referenced in the text file. Slide 3
C:\JAI Vault 1\Projects\107 - Stalker XE, VTOL Gen 2\Electrical Design\Firmware and Hex Files\965-1-01-2004 (1607P01A) X-comm Firmware and Configs\Configuration\xcbteccp_104.hex
✎ Check off and record the bootloader firmware version on the traveler
Select the “Program” menu button on the left-hand side. Wait for “programming complete” to read in blue lettering in the output dialog.  This process should only take a second.
➤ Note: you should see a blinking red light next to the J10 connector when the programming finishes.
Unplug the ICSP programming box (Real ICE) and set it aside.  Slide 15
A
[picture]
Appendix A: Bootloader Program Install
2026-02-09
Redwire Proprietary Information
41
