# FlashReformat.docx

Attachment 15234, docx, 649 KB, added 2023-06-28 by John Clark.

Flash Reformat and File Recovery

1.	Introduction	3

2.	Mitigation	3

2.1.	Accessing Main Menu	4

2.2.	Selecting the Utilities to Reformat the Serial Flash	6

2.3.	Accessing the Configuration and Uploading	8

2.4.	Selecting the Utilities to Reformat the SD	10

Figure 1 Connecting To The Aircraft	4

Figure 2 Accessing the VTOL	4

Figure 3 The Main Menu	5

Figure 4 Messages (Cleared)	5

Figure 5 Utility Page Menu	6

Figure 6 Utilities	6

Figure 7 Serial Flash Format Pop Up	7

Figure 8 Format Serial Flash Log Messages	7

Figure 9 IP Address Calculator	8

Figure 10 Configuration Page Menu	9

Figure 11 File Transfer / Upload Menu	9

Figure 12 Import Configuration menu	10

Figure 13 Utilities Menu	11

Figure 14 SD Format Messages	11

Flash Reformat and File Recovery

Project Number: N/A

Job Number: N/A

Description

Provide a procedure to Reformat VTOL AP Flash, apply new configurations and save to SD VXE30.

Scope of Work

Perform recovery procedures and document them

Objective and Deliverables:

This document

Recovery path for Serial Flash corruption

Configuration File

Active Tasks:

| Action | Owner |
| Recovery path for Serial Flash corruption | John Clark |
|  |  |
|  |  |
|  |  |

## Introduction

VTOL Motor Spin-up has been reported in V456 (VIT-54) targeted an incident in which both Serial Flash and SD Card files are known to be corrupted. It is suspected that default values in Servo Neutral values are to blame.

## Mitigation

A mitigation procedure that performs the following is recommended

Reformat Serial Flash

Load known good configuration

Reformat SD

## Accessing Main Menu

The procedures are performed from within the GCS Software Interface. It is necessary to start the application and connect to the aircraft on which the mitigation procedures are to be performed.

Figure  Connecting To The Aircraft

Using the Tail Number for the Targeted Aircraft, connect and using Tools Tab, select the IP Address Calculator and Open the VTOL.

Figure  Accessing the VTOL

Figure  The Main Menu

The Main Menu is used to access the mitigation procedures described in this document. The Configuration and Utilities links will be used to access Web Pages where the procedures are. Right click on the links to select the new Tabs

The Reformat Serial Flash status is shown in the Messages link page. Right click on the link, then select the “Clear Log” button in the Messages Tab to better see the Reformat Serial Flash messages.

Figure  Messages (Cleared)

## Selecting the Utilities to Reformat the Serial Flash

Select the Utilities link in the Main Menu. The Utility Page menu should appear as below.

Figure  Utility Page Menu

Selecting the Enter Utilities link will open the Utilities.

Figure  Utilities

Use the “Format Serial Flash” button to begin the flash format process. The Pop Up is used to confirm the process. Wait a few seconds for the process to complete. Then view the logs in the Messages Tab to confirm the process.

Figure  Serial Flash Format Pop Up

Figure  Format Serial Flash Log Messages

## Accessing the Configuration and Uploading

The Aircraft must be rebooted following the Serial Flash Format and a reconnection must be made to the VTOL.

Using the Tail Number for the Targeted Aircraft, connect and using Tools Tab, select the IP Address Calculator and Open the VTOL. As shown previously and in the figure below.

Figure  IP Address Calculator

From the Main Menu select the Configuration link.

From the Configuration Menu select the Upload/Copy link.

Figure  Configuration Page Menu

Then Use the Import Config link to select the Import Config Tab.

Figure  File Transfer / Upload Menu

Ensure the “Ignore above settings, import all” box is checked. Use the “Choose File” to select the configuration file to restore and then the “Import Configuration File” buttons to load the provided configuration file.

This process takes about 20 seconds to complete.

Figure  Import Configuration Menu

## Selecting the Utilities to Reformat the SD

From the Main Menu select the Utilities link at the top of the Web Page. The Utility Page menu should again appear.

Selecting the Enter Utilities link will open the Utilities.

Figure  Utilities Menu

Use the “Format SD Card” button to begin the format process. The Pop Up is used to confirm the process. The format completion can be verified in the Messages Tab using the same method as the Format Serial Flash.

The “Format SD Card” process takes 20 – 25 seconds. Reboot the Aircraft to complete the process.

Figure  SD Format Messages
