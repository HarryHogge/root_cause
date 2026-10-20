# 2120003-01 - Electronics - Xcomm Board (1607P01A) 2 - Initialization Procedure.pptx

Attachment 44671, pptx, 4179 KB, added 2026-02-19 by Ben Norris.

## Slide 1

2120003-01 (1607P01A)X-Comm Board Initialization and Setup ProcedurePart Number:		2120003-01 (1607P01A)Assembly Revision:	DDescription:		X-Comm Initialization procedure
Procedure Revision: E
07 November 2025
1
Edge Autonomy Proprietary Information
[picture]
UNCONTROLLED WHEN PRINTED

DATE PRINTED:__12/3/2025__

PRINTED COPIES ARE ONLY VALID FOR 24 HOURS FROM THE PRINT DATE UNLESS MARKED “CONTROLLED COPY” IN RED INK.
COPIES OF THESE CONTROLLED DOCUMENTS ARE NOT AUTHORIZED.
2025-11-07

## Slide 2

| Rev | Description | Date |
| A | Original Release. | 2022-11-14 |
| B | Revised to include current firmware versions.  Set up new locations in the Vault to control firmware files. | 2023-07-14 |
| C | PN updated per ENG-2735 | 2024-10-22 |
| D | Industrial SD Card 2120068-01 | 2025-01-03 |
| E | Updated part rev to D | 2025-11-07 |
2
Revision History:
Edge Autonomy Proprietary Information
2025-11-07

## Slide 3

1607P01A X-Comm Board Initialization and Setup Procedure:
i
Tools/Materials: 
Vehicle harness with network connection and power connection
Microchip ICSP programmer and software (Real ICE) 
Power supply
Laptop
Xcomm2 boards

File Path References: Slide 6  Slide 8  Slide 15  Slide 16
C:\JAI Vault 1\Projects\107 - Stalker XE, VTOL Gen 2\Electrical Design\Firmware and Hex Files\965-1-01-2004 (1607P01A) X-comm Firmware and Configs\1607P01A X-Comm Current Production Firmware Version.txt
[picture]
Intro:
This procedure is for new boards, that haven’t had anything loaded onto them. If you are troubleshooting a bricked board, work with someone who has experience troubleshooting them. 
This procedure covers installing the bootloader and firmware, as well as setting the configuration and formatting the on-board storage for the Power Comms (also know as the Xcomm2) board. 
When the software is initially loaded, the IP address of the Power Comms (XComm2) board is 192.168.10.70, so only computers configured as 192.168.10.XXX (standard for our office network) can talk to the board.  After the initialization configuration is loaded (and power is cycled), the board IP address will be 10.128.123.2, so only computers configured as 10.XXX.XXX.XXX (standard network configuration for vehicle components) will be able to talk to the board.
This procedure is to be done after the initial buildup.  Once complete, conformal coat board and perform the Xcomm burn in procedure.
Edge Autonomy Proprietary Information
3
2025-11-07

## Slide 4

[picture]
[picture]
[picture]
[picture]
[picture]
Bootloader Program Install:
Connect the board to be tested the power connection and network connections on the Ironbird (labeled “main harness” and “aux harness” on the box).
Plug in the power supply and ensure that the board is drawing about 0.2A at 28V.
1
2
Connect the ICSP programming (Real ICE) connector to the board at the J10 connector (near the SD).
Plug the ICSP programming (Real ICE) box cable into the USB drive on the computer.
Edge Autonomy Proprietary Information
4
2025-11-07

## Slide 5

[picture]
[picture]
Bootloader Program Install:
3
Open the Real ICE software: MPLab IPE v4.05
Select “Settings” in the top toolbar, followed by “Release from reset.”
Edge Autonomy Proprietary Information
5
[picture]
In the “Operate” menu pane make sure the following settings are correct:Family: 32-bit MCUs
Device: PIC32MZ2048EFM144
➤ Note: The “Tool” setting will auto-select the correct setting. Also, if the device is already set correctly, there is no need to set the family dropdown. The family selection just narrows the list that populates on the device dropdown. 
Click the “Apply” button, followed by “Connect.”
Wait a few seconds.
 ➤ Note: if you get a red error message in the dialog, or it fails to connect, try unplugging and reinserting the USB cable to the programmer (Real ICE).
4
2025-11-07

## Slide 6

[picture]
[picture]
[picture]
5
Select “Browse” next to the “Source” menu. Upload the correct Bootloader File referenced in the text file. Slide 3
C:\JAI Vault 1\Projects\107 - Stalker XE, VTOL Gen 2\Electrical Design\Firmware and Hex Files\965-1-01-2004 (1607P01A) X-comm Firmware and Configs\Configuration\xcbteccp_104.hex
✎ Check off and record the bootloader firmware version on the traveler
Select the “Program” menu button on the left-hand side. Wait for “programming complete” to read in blue lettering in the output dialog.  This process should only take a second.
➤ Note: you should see a blinking red light next to the J10 connector when the programming finishes.
Unplug the ICSP programming box (Real ICE) and set it aside.
6
Edge Autonomy Proprietary Information
6
[picture]
2025-11-07
Bootloader Program Install:

## Slide 7

8
In the ethernet box, change the last octet of the IP address to 72 (the default is 71, which is the autopilot).
 ➤ Note: do not press the enter key when finished, as it will close the program. Just change the number and click out of the IP settings window.
9
Press the “Connect” button and wait for the connection. 
Verify that the dialog reads “Device connected” and shows the bootloader version uploaded in the previous step.
 ➤  Note: You should see a green light by the XComm2 board ICSP connector.
 ➤  Note: If you are not working on a new board (a board without software loaded), hit the reset button on the board by the J10 connector right before you press “Connect.”
Edge Autonomy Proprietary Information
7
Main Firmware Install
Run the JAI AP bootloader interface software: apbl.exe
7
[picture]
[picture]
[picture]
2025-11-07

## Slide 8

[picture]
[picture]
[picture]
10
Select “Load Hex File” button and browse for the Current Production Firmware Hex File referenced in the text file. Slide 3
C:\JAI Vault 1\Projects\107 - Stalker XE, VTOL Gen 2\Electrical Design\Firmware and Hex Files\965-1-01-2004 (1607P01A) X-comm Firmware and Configs\Firmware Version 467\xcomm467.hex
11
Select “Erase-program-verify” and wait for the programming to complete. 
 ➤  Note: it takes about 100 seconds to complete the programming, you will see the blue light next to the J10 connector blinking during the programming process. 
When completed, the dialog will read “Programming completed, Verification successful” and the blue light will go off.
Select “Disconnect.” 
✎ Check off and record the bootloader firmware version on the traveler.
12
Edge Autonomy Proprietary Information
8
2025-11-07

## Slide 9

[picture]
On-board Storage Formatting
13
Reset the board using the reset button near the J10 connector or by cycling the power to the board.
Wait 10 seconds, until you see blinking lights (red, blue, and green).
14
Using a web browser, navigate to the Xcomm2 page: 192.168.10.70 or 10.0.0.200Log in to the webpage using the standard log in credentials:
Username: stalker    Password: [password removed]
15
Verify on the webpage that the correct firmware is listed in the row labeled “Board” under the blue “System Information” section. Record this in the traveler if not done already.
➤  Note: On the “Document source” row, which is under the green “HTTP Connection” section, you will see “ROM.” 
➤  Reference the Current Firmware Version text file for details on what is the expected firmware revision.
Edge Autonomy Proprietary Information
9
[picture]
2025-11-07

## Slide 10

[picture]
[picture]
[picture]
[picture]
[picture]
On-board Storage Formatting
Click on the “Utilities” link at the bottom of the page, followed by “Enter Utilities.”
16
17
Open another browser tab, navigate to the Xcomm2 main page, and select the “Messages” link at the bottom to view the log. This will make checking the status of subsequent steps a bit easier.
Edge Autonomy Proprietary Information
10
2025-11-07

## Slide 11

[picture]
[picture]
On-board Storage Formatting
In the tab with the Utilities page open, click the button labeled “Format Serial Flash” then wait about 10 seconds.  Click “Erase Flash Configuration” then switch back to the Messages tab.  Verify that a message indicates “erase flash complete” and buy off the “Erase Flash Config” step in the traveler.
18
Edge Autonomy Proprietary Information
11
2025-11-07

## Slide 12

[picture]
[picture]
[picture]
18
Navigate back to the tab with the “Utilities” page.  
Click the “Format SD Card” button on the bottom left followed by “OK.”
➤  Note: the formatting process takes about 20 seconds.
When the formatting is complete the log will read:  
fmt: 0
mounted: 1
init: 0
sd format complete
➤  Note: if this message doesn’t appear, or the process takes too long (longer than 45 seconds), there is an issue with the SD card.
19
Navigate back to the tab with the “Utilities” page open.  Click the “Format Serial Flash” button on the bottom right, followed by “OK.”
➤  Note: this process takes about 2 seconds.
➤  This step must be done again as the erase config step previously wiped the flash in preparation for this step.
Edge Autonomy Proprietary Information
12
2025-11-07

## Slide 13

[picture]
Navigate back to the browser window with the log and verify that the following message appears: 
fmt: 0
mounted: 2
init: 0
flash format complete
✎ Check off SD card and serial flash format step on the traveler.
20
Edge Autonomy Proprietary Information
13
Note: The SD formatting and flash formatting look similar.  The “Mounted” label indicates which device was formatted.  Ensure the correct section is used for verification.
1 - SD Card
2 – Serial Flash
2025-11-07

## Slide 14

[picture]
[picture]
[picture]
Configuration Install:
21
Reset the board using the reset button near the J10 connector or by cycling the power to the board.
Wait 10 seconds. 
Either reload the Xcomm2 page in the web browser, or open a new one (192.168.10.70) and log back in. 
Verify that the “Document source” row under the green “HTTP Connection” section now says: “SD1” instead of “ROM.”
22
Click on the “Configuration” link in the bottom middle of the page, followed by the “Upload/copy” link at the top left-hand side of the page.
Edge Autonomy Proprietary Information
14
[picture]
2025-11-07
[picture]

## Slide 15

[picture]
[picture]
Click on the “Import config” link on the bottom right-hand side of the page.
23
24
Check the box that says “ignore above settings, import all” then click “Choose file” 
Select the Initial Configuration file referenced in the text file. Slide 3  
C:\JAI Vault 1\Projects\107 - Stalker XE, VTOL Gen 2\Electrical Design\Firmware and Hex Files\965-1-01-2004 (1607P01A) X-comm Firmware and Configs\Configuration\Initial B25 Configuration.CFG
Click “Import configuration file.” 
Wait a few second for the file to load. Check the box in the traveler for “Initial Config Load”
Edge Autonomy Proprietary Information
15
2025-11-07

## Slide 16

Edge Autonomy Proprietary Information
16
[picture]
24
After loading the initial config file, select “Choose File” again.  Reference the Text File for the directory to the Current Firmware Config File. Slide 3
C:\JAI Vault 1\Projects\107 - Stalker XE, VTOL Gen 2\Electrical Design\Firmware and Hex Files\965-1-01-2004 (1607P01A) X-comm Firmware and Configs\Firmware Version 467\update467.cfg
Wait a few second for the file to load. Check the box in the traveler for “Production Config Load” and note the config filename.
2025-11-07

## Slide 17

[picture]
[picture]
[picture]
26
Click on the “Gains” link in the bottom right-hand side of the page.  On the “Xcomm serial number” row click on the box and type in the board serial number from the label on the board (5-5XXX). 
On the “Tail number” row, click on the box and type in 123 as the tail number. 
Click the “Save” button up at the top.
27
Click on the “Upload/copy” link at the top of the page, followed by the “Save Config” button in the lower portion of the page (towards the middle). 
➤  Note: You will see a blue loading bar as it saves. This takes only a few seconds.
✎ Check off the “import configuration file and update gains values” step on the traveler. 
➤  Note: now that the board is configured, if it is restarted, the IP address will be 10.128.1.2 until it is connected to an Autopilot.
Edge Autonomy Proprietary Information
17
2025-11-07

## Slide 18

[picture]
[picture]
[picture]
Save the Encryption Key:
Switch browser tabs back to the “Main” page and then click “Log files” link at the bottom of the page. 
Select the “XCEVLOG.TXT” file. 
When the file downloads, open it, and scroll down to verify that the encryption key is there (you may have to scroll about half-way down the page). 
Do not change the contents of the text file.  Save the text file as the serial number (i.e. 5-5XXX.txt):
	\\condor\Production\HEX Files\XComm\Logs

Note that a USB drive may be required to transfer files off the IronBird as it is not on our network.  Save the log files to the USB drive and copy them onto Condor.
✎ Check off the save encryption key step on the traveler.
28
Edge Autonomy Proprietary Information
18
[picture]
Encryption key is the highlighted 8 lines of text
2025-11-07

## Slide 19

[picture]
Final Verifications:
Navigate to the main X-Comm webpage and verify the following:
Board Firmware Version matches that in the Current Production Firmware text file
Config CRC checksum matches that of the Current Production Firmware text file
Board serial number matches that of the label on the board
Tail number is set to 123
Document Source indicates SD1:/www/
Note the Config CRC in the traveler and buy off the “Final Verifications” step.
28
Edge Autonomy Proprietary Information
19
2025-11-07

## Slide 20

Quick Reference
Common IP Addresses:
192.168.10.72 – X-Comm in bootloader mode, awaiting programming from APBL.
192.168.10.70 – X-Comm with flashed bootloader.  Firmware versions prior to 4.67 used to jump to this address after flashing with APBL.
10.0.0.200 – X-comm after fresh install of firmware 4.67 without a config loaded.
10.128.1.2 – X-comm after loading initial configuration files.
Edge Autonomy Proprietary Information
20
2025-11-07
