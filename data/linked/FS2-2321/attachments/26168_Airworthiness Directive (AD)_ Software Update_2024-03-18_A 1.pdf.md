# Airworthiness Directive (AD)_ Software Update_2024-03-18_A 1.pdf

Attachment 26168, pdf, 1258 KB, added 2025-02-11 by Jason Scherer.

## Page 1

3/18/24, 1:06 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1710786538827/manual/4520581/next/n/1 1/16
 Airworthiness Directive(AD)_Software Update_2024-03-18_A
Date: 18.Mar.2024
Rev: A
Airworthiness Directive(AD)_Software Update_2024-03-18_A
Airworthiness Directive (AD)_Software Update_2024-03-18_A

## Page 2

3/18/24, 1:06 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1710786538827/manual/4520581/next/n/1 2/16
 Date: 18.Mar.2024
Rev: A
Supplemental Documentation
This manual is updated on a continuous basis as new equipment and procedures become available for the VXE30.
However, certain conditions (such as an equipment modification or safety concerns) make it necessary to notify
users before a revised manual is released. These documents are distributed as part of Edge Autonomy customer
support, and are available in three types:
Service Bulletins (SB)
A service bulletin is a document notifying users to modifications or improvements to Edge Autonomy products in
terms of modifying or installing new components within the operational system.
Airworthiness Directives (AD)
An airworthiness directive is a mandatory document notifying users of a problem and a solution, not outlined in our
current documentation.The directive document notifies users of procedures or modifications Edge Autonomy
developed to correct the issue. Airworthiness directives are a procedural change.
Operational Supplement (OS)
An operational supplement is a descriptive document outlining a system component that is not a part of the standard
baseline configuration. This information contains operational descriptions and special procedures and only applies
to operations when that component is being utilized.
Notice
This manual is the PROPRIETARY PROPERTY of Edge Autonomy and shall be subject to and comply with all
applicable U.S. export control laws, economic sanctions laws and regulations. No part of this document shall
be disclosed in any manner to a third party without the prior written consent of Edge Autonomy. This manual
and its contents shall not be transferred, disclosed, modified, or otherwise provided to or made accessible to
any persons, or entities not authorized to receive or have access to the manual without written authorization
from Edge Autonomy
Please see Home - Edge Autonomy for more details.
Contact us:
www.edgeautonomy.io/contact-us/
United States Support Office
831 Buckley Road, San Luis Obispo, CA 93401 USA
Phone: +1 888-334-3457
 
European Support Office
1 Jaunbridagi, Marupes nov. LV-2167, Latvia
Phone: +371 2026-2126
Airworthiness Directive (AD)_Software Update_2024-03-18_A

## Page 3

3/18/24, 1:06 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1710786538827/manual/4520581/next/n/1 3/16
 Date: 18.Mar.2024
Rev: A
Overview
 
Purpose:
This directive is a Safety of Use Message, and requires immediate implementation for safeoperation of the VXE30. The directive will address the release of Version 6.2.9; the latestsoftware and firmware updates for VXE30 system components. The software update willimpact the VTOL Controller, XComm, Fixed Wing Autopilot, and the GCS laptop. Theimprovement of code will allow for greater situational awareness for critical flight elements.
 
Scope:
Airworthiness Directive (AD)_Software Update_2024-04-07 applies to VXE30 aircraft. AllOperators and Technicians of the VXE30 Unmanned Aircraft System must review andimplement updates.
 
Compliance:
If listed procedures are not followed, loss of aircraft could occur.
 
Cross Reference:
N/A
Airworthiness Directive (AD)_Software Update_2024-03-18_A

## Page 4

3/18/24, 1:06 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1710786538827/manual/4520581/next/n/1 4/16
 Date: 18.Mar.2024
Rev: A
List of Summary Changes
A list of summary changes is described below.
Changes:
NOTE
This service bulletin adds an additional level of safety to all aspects of operations. The improvement of code will
allow for greater situational awareness for critical flight elements.
 
1. GCS Software update Version 6.2.9
2. VTOL Controller update Version 1.54
Fixed i2c Driver Bug that could result in the i2c Bus hanging.
Fixed a bug in the handling of the Real Time Clock sync to GPS Time.
Improved flight control robustness through driver improvements, simplified task architecture, and better
interrupt handling.
Added detailed AP internal diagnostics to facilitate future debugging.
3. XComm Controller update Version 4.68
Multi-constellation GNSS support.
Disabled the deprecated Metadata Interface.
4. Fixed Wing AP update 6.05o
Fixed a RACE condition where a land immediately command while in a landing sequence would result in
the Aircraft being left in Attitude Hold Mode and drifting with the wind in landing.
Airworthiness Directive (AD)_Software Update_2024-03-18_A

## Page 5

3/18/24, 1:06 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1710786538827/manual/4520581/next/n/1 5/16
 Date: 18.Mar.2024
Rev: A
Software Update for SGCS – Installation
A software and firmware update are required to provide additional levels of safety for operations. Prior to the
installation of this software and firmware, review the required parts below and obtain administrator permission.
1. Preparation for Task:
Required Tools:
Tools Part Number
N/A N/A
 
Required Parts:
Parts Part Number
VXEGCS_V6.2.9_Installer.msi. Software package file version 6.2.9 (*)
SGCS1 Laptop (all) Short range ground control station
 
NOTE
If you have received this bulletin without the referenced software installer, please download from
https://edgeautonomy.webmanuals.aero, or by contacting Edge Autonomy product support:
globalsupport@edgeautonomy.io
 
2. Procedure:
2.1:      Copy the installer program, “VXEGCS_V6.2.9_Installer.msi.”, to the GCS laptop. Double-click the installer, or
right click, install.
 
 
Vxegcs Software Installation
 
 
Airworthiness Directive (AD)_Software Update_2024-03-18_A

## Page 6

3/18/24, 1:06 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1710786538827/manual/4520581/next/n/1 6/16
 Date: 18.Mar.2024
Rev: A
2.2: Select, “Typical.”
 
Software Installation
 
NOTE
You may be prompted to provide administrator permissions.
 
2.3: Click “Finish” to complete the installation. The installer will create desktop icons for the software and load the
current collection of manuals and service bulletins under MyGCS\Manuals.
 
Finishing Software Installation
Airworthiness Directive (AD)_Software Update_2024-03-18_A

## Page 7

3/18/24, 1:06 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1710786538827/manual/4520581/next/n/1 7/16
 Date: 18.Mar.2024
Rev: A
GCS Windows Anti-Virus Exclusions 
The following Windows Security settings will permit Firmware updates for the Firmware Updates for Aircraft-
Installation, procedure. 
1. Preparation for Task:
Required Tools:
Tools Part Number
N/A N/A
 
Required Parts:
Parts Part Number
SGCS1 Laptop (all) Short range ground control station
 
2. Procedure:
2.1: Find the Windows Start Menu in the lower left corner. 
Windows Start Menu Location
 
2.2: Right-click on the Windows Start Menu. Then left-click on “Windows PowerShell (Admin)”. Enter admin
credentials (if prompted). 
 
Selecting Windows PowerShell
Airworthiness Directive (AD)_Software Update_2024-03-18_A

## Page 8

3/18/24, 1:06 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1710786538827/manual/4520581/next/n/1 8/16
 Date: 18.Mar.2024
Rev: A
2.3: Add the exclusion path by typing “MpPreference -ExclusionPath “C:\ProgramData\GCS” at the prompt, followed
by selecting Enter on the keyboard.
 
Entering the Exclusion Path 
Airworthiness Directive (AD)_Software Update_2024-03-18_A

## Page 9

3/18/24, 1:06 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1710786538827/manual/4520581/next/n/1 9/16
 Date: 18.Mar.2024
Rev: A
Firmware Updates for Aircraft – Installation
After updating SCGCS1 with the software update Version 6.2.9, the aircraft must be updated. To complete this
update, verify the aircraft is fully assembled and is powered on. Aircraft must be networked to the SGCS1 that was
just updated.
1. Preparation for Task:
Required Tools:
Tools Part Number
N/A N/A
 
Required Parts:
Parts Part Number
SGCS1 Laptop (all) Short range ground control station
VXE30 Aircraft Fully assembled and powered aircraft
 
2. Procedure:
2.1:   Power the aircraft on, with the center wing section installed. Establish a connection between the GCS and the
correct aircraft. Select “Comm” menu. Select “Connect.” When prompted select the correct tail number.
 
 
Updating Aircraft Firmware
 
 
Airworthiness Directive (AD)_Software Update_2024-03-18_A

## Page 10

3/18/24, 1:06 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1710786538827/manual/4520581/next/n/1 10/16
 Date: 18.Mar.2024
Rev: A
2.2:   Go to “Help” menu, select “About.” Select “Updates.”
 
Updating Aircraft Firmware
 
2.3:          A dialog will pop up with 3 firmware update options. This window indicates if the firmware needs to be updated.
Click “Update Firmware…” to open the update window.
 
              Updating Aircraft Firmware
 
Airworthiness Directive (AD)_Software Update_2024-03-18_A

## Page 11

3/18/24, 1:06 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1710786538827/manual/4520581/next/n/1 11/16
 Date: 18.Mar.2024
Rev: A
2.4:   To update the Autopilot Firmware, select “Update Autopilot Firmware.” Wait for the update to complete. Once
the firmware update is finished, “Current Ver.” and “New Ver.” should match (if not, restart the GCS software,
reconnect, and restart the whole process).
 
                Updating Aircraft Firmware
 
Airworthiness Directive (AD)_Software Update_2024-03-18_A

## Page 12

3/18/24, 1:06 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1710786538827/manual/4520581/next/n/1 12/16
 Date: 18.Mar.2024
Rev: A
2.5:   To update the XComm Firmware, select “Update XComm Firmware.” Wait for the update to complete. Once the
firmware update is finished, “Current Ver.” and “New Ver.” should match (if not, restart the GCS software, reconnect,
and restart the whole process).
 
     Updating Aircraft Firmware
 
Airworthiness Directive (AD)_Software Update_2024-03-18_A

## Page 13

3/18/24, 1:06 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1710786538827/manual/4520581/next/n/1 13/16
 Date: 18.Mar.2024
Rev: A
2.6:   To update the VTOL Firmware, select “Update VTOL Firmware.” Wait for the update to complete. Once the
firmware update is finished, “Current Ver.” and “New Ver.” should match (if not, restart the GCS software, reconnect,
and restart the whole process).
 
       Updating Aircraft Firmware
 
Airworthiness Directive (AD)_Software Update_2024-03-18_A

## Page 14

3/18/24, 1:06 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1710786538827/manual/4520581/next/n/1 14/16
 Date: 18.Mar.2024
Rev: A
2.7:    If you receive a “Firmware Update Unconfirmed” while updating VTOL firmware, please use the steps below for
guidance.
 
Firmware Update Unconfirmed
GCS SW needs to be restarted.
Use the “About” menu to verify Firmware Update Confirmation.
If Firmware Failed Update, then Update should be attempted again.
Aircraft Restart only on successful Update or if multiple attempts to restart the process have failed.
 
 
 
                     Handling Unconfirmed Updates
 
 
2.8:    Repeat update procedures for all SGCS1 and other aircraft.
 
Airworthiness Directive (AD)_Software Update_2024-03-18_A

## Page 15

3/18/24, 1:06 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1710786538827/manual/4520581/next/n/1 15/16
 Date: 18.Mar.2024
Rev: A
Additional Information
Included below are three sections addressing additional information for the software update. The known limitations
and bugs will help the user identify potential bugs, what you can expect to see, and how to address them. Next,
there is guidance on how to troubleshoot issues that might arise during the software update process. Finally, there
are two tables that will provide a baseline for all systems to be current and up to date.
Known Software Limitations and Bugs:
Software out of date pop up has been suppressed due to reliability issues. User must select Help -> About
to verify software configuration.
The VTOL and XComm checksum and firmware version does not reliably display in the GCS. Please
restart GCS software to resolve the issue.
The maintenance log incorrectly reports flight hours but the correct flight count. Time change interval
components affected by this are the cruise motor and servos. Users should use the Files > Vehicle Status
hours to determine time change service interval.
Vehicle endurance estimate during an inflight simulation might display not enough Endurance, when there
actually is. Please use pilot’s best judgement.
It is recommended to avoid use of MUAV software. It has the following issues:
a. Runs slow
b. Occasional fail initial connection
c. “LOC GCS” doesn’t work with GCS location
“Set fixation point” command doesn’t work with the Trillium camera.
 
Troubleshooting:
On connect, if the user is prompted with a software update and the fixed wing software update is
unavailable then follow the following steps:
1. Ensure GCS software is closed.
2. Open Windows Explorer, Go to: "C:\Users\SGCS1-XX\AppData\Local\VirtualStore"
3. Delete all contents of this folder. If folder is blank, no further action is required.
4. Browse to desktop, ensure Recycling Bin is empty.
5. Run GCS software installer, select Remove option.
6. Run GCS software installer, select Typical to install software.
 
Checksum not displayed properly.
1. If the checksum does not reliability report in the GCS, please restart GCS software, connect to the
vehicle, and wait for ~10 sec.
Airworthiness Directive (AD)_Software Update_2024-03-18_A

## Page 16

3/18/24, 1:06 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1710786538827/manual/4520581/next/n/1 16/16
 Date: 18.Mar.2024
Rev: A
Current Baseline:
At the conclusion of this software update, the new baseline software and firmware versions shall be the following:
 
Item Version
GCS Software 6.2.9
Autopilot Firmware 6.05o
Autopilot Checksum 0xC4D9
XComm Firmware 4.68
XComm Checksum 0x5F8F
VTOL Controller Firmware 1.54
VTOL Controller Checksum 0x2D8D
 
The following Silvus & Trillium versions are recommended for use:
 
Item Version
Silvus Firmware 4.0.3.14
Silvus Configuration XE40314R1
Trillium ‘Skylink’ Software 24.1.13509
 
 
NOTE
Verify and/or update SGCS 2 and SGCS 3 radios to match the most current Silvus firmware and
configuration to match the current baseline.
 
Airworthiness Directive (AD)_Software Update_2024-03-18_A
