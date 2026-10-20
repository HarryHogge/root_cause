# Airworthiness Directive (AD) Software Update 2024-08-08_A (e5b5240d-1771-4f31-8f3b-4eeb386d4c93).pdf

Attachment 26170, pdf, 2907 KB, added 2025-02-11 by Jason Scherer.

## Page 1

Airworthiness Directive(AD)_Software Update_2024-08-08_A
Date: 12.Jul.2024
Rev: A
Airworthiness Directive(AD)_Software Update_2024-08-08_A
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 1/31

## Page 2

Date: 12.Jul.2024
Rev: A
Supplemental Documentation
This document is updated on a continuous basis as new equipment and procedures become available for the
VXE30. However, certain conditions (such as equipment modifications or safety concerns) make it necessary to
notify users before a revised manual is released. These documents are distributed as part of Edge Autonomy
customer support, and are available in three types:
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
This document is the PROPRIETARY PROPERTY of Edge Autonomy and shall be subject to and comply with
all applicable U.S. export control laws, economic sanctions laws and regulations. No part of this document
shall be disclosed in any manner to a third party without the prior written consent of Edge Autonomy. This
manual and its contents shall not be transferred, disclosed, modified, or otherwise provided to or made
accessible to any persons, or entities not authorized to receive or have access to the manual without written
authorization from Edge Autonomy.
Please see Home - Edge Autonomy for more details.
Contact us:
United States Support Office
831 Buckley Road, San Luis Obispo, CA 93401 USA
E-mail: Globalsupport@edgeautonomy.io
Phone: +1 855-334-3457
 
European Support Office
1 Jaunbridagi, Marupes nov. LV-2167, Latvia
Phone: +371 2026-2126
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 2/31

## Page 3

Date: 12.Jul.2024
Rev: A
Overview
 
Purpose:
This directive is a Safety of Use Message, and requires immediate implementation for safeoperation of the VXE30. The directive will address the release of Version 6.3.4; the latestsoftware and firmware updates for VXE30 system components. The software update willimpact the VTOL Controller, XComm, Fixed Wing Autopilot, and the GCS laptop. Theimprovement of code addresses a number of incidents across the fleet.
 
Scope:
Airworthiness Directive (AD)_Software Update_2024-08-08_A applies to VXE30 aircraft. AllOperators and Technicians of the VXE30 Unmanned Aircraft System must review andimplement updates.
 
Compliance:
If listed procedures are not followed, loss of aircraft could occur.
 
Cross Reference:
N/A
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 3/31

## Page 4

Date: 12.Jul.2024
Rev: A
List of Summary Changes
A list of summary changes is described below.
Changes:
NOTE
This Airworthiness Directive adds an additional level of safety to all aspects of operations. 
1. XCOMM, 4.69V:
Landing Abort fix support.
Generic STANAG style Warnings, Cautions, Advisories (WCA) messages. 
Task and Interrupt Service Routines (ISR) Diagnostics.
Remove operational data from event log.
2. VTOL AP, v1.55:
Bad Mag fault detection and rejection.
Fixes for external magnetometer driver.
Disable unused ISRs (strobe & slow servos).
Added detailed AP internal diagnostics to facilitate future debugging.
Fix for priority inheritance of Mavlink Message handler.
Remove operational data from event log.
PLZ overshoot mitigation 
Baro offset from LRF logic update
3. FW AP, v6.05p:
Landing Abort logic fix.
NOTE
It is expected that Landing Abort logic fix will result in a small percentage of flights where the aircraft will
automatically abort the PLZ landing pattern based on detected faults and proceed to the ELZ. It will be important to
review ELZ procedures in the Operations Manual. 
VTOL/FW AP ARM synchronization fix with unstable comms link.
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 4/31

## Page 5

Date: 12.Jul.2024
Rev: A
 
4. GCS, v6.3.4:
Generic STANAG style WCA message display that will initially be used with Magnetometer fault handling.
 
Example STANAG WCA Message Display
Negative 0 fix for waypoints.
Windows Error Reporting for GCS.
VTOL AP reset in launch wizard to power cycle between flights.
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 5/31

## Page 6

Date: 12.Jul.2024
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
VXEGCS_V6.3.4_Installer.msi. Software package file version 6.3.4 (*)
SGCS1 Laptop (all) Short range ground control station
 
NOTE
If you have received this directive without the referenced software installer, please download from
https://edgeautonomy.webmanuals.aero, or by contacting Edge Autonomy product support:
globalsupport@edgeautonomy.io
 
2. Procedure:
2.1: Copy the installer program, “VXEGCS_V6.3.4_Installer.msi.”, to the GCS laptop. Double-click the installer, or
right click, install.
 
 
Vxegcs Software Installation
 
 
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 6/31

## Page 7

Date: 12.Jul.2024
Rev: A
2.2: Select, “Typical.”
 
Software Installation
 
NOTE
You may be prompted to provide administrator permissions.
 
2.3: Click “Finish” to complete the installation. The installer will create desktop icons for the software and load the
current collection of manuals and service bulletins under My GCS\Manuals.
 
Finishing Software Installation
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 7/31

## Page 8

Date: 12.Jul.2024
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
 
Example 1 :Selecting Windows PowerShell
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 8/31

## Page 9

Date: 12.Jul.2024
Rev: A
 
Example 2 :Selecting Windows PowerShell
 
2.3: Add the exclusion path by typing, Add-MpPreference -ExclusionPath “C:\ProgramData\GCS”, at the
prompt, followed by selecting Enter on the keyboard. Ensure that the command executes as expected, if successful,
the command will complete with no additional output to the terminal as in the image below.
 
NOTE
If an error is printed to the console, then contact the IT team responsible for maintaining the computer and ensure
that they setup exclusions as required for the GCS software package within the Firewall security software installed
on the computer.
 
Entering the Exclusion Path 
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 9/31

## Page 10

Date: 12.Jul.2024
Rev: A
Firmware Updates for Aircraft – Installation
After updating SCGCS1 laptop(s) with the software update Version 6.3.4, the aircraft must be updated. To complete
this update, verify the aircraft is fully assembled and is powered on. Aircraft must be networked to the SGCS1 that
was just updated.
1. Preparation for Task:
Required Tools:
Tools Part Number
N/A N/A
 
Required Parts:
Parts Part Number
SGCS1 Laptop (all) Short range ground control station
VXE30 Aircraft Fully assembled and powered aircraft
 
2. Procedure:
2.1: Power the aircraft on, with the center wing section installed. Establish a connection between the GCS and the
correct aircraft. Select “Comm” menu. Select “Connect.” When prompted, select the correct tail number.
 
 
Connecting to Aircraft 
 
 
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 10/31

## Page 11

Date: 12.Jul.2024
Rev: A
2.2: Go to “Help” menu, select “About.” Select “Updates.”
 
 Updating Aircraft Firmware
 
2.3: A dialog will pop up with 3 firmware update options. This window indicates if the firmware needs to be updated.
As indicated, click  “Update... Firmware…” to open the update window.
 
              Updating Aircraft Firmware
 
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 11/31

## Page 12

Date: 12.Jul.2024
Rev: A
2.4: To update the Autopilot Firmware, select “Update Autopilot Firmware.” Wait for the update to complete. Once
the firmware update is finished, cycle aircraft power.  Verify “Current Ver.” and “New Ver.” match (if not, restart the
GCS software, reconnect, and restart the whole process).
Updating Autopilot Firmware
 
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 12/31

## Page 13

Date: 12.Jul.2024
Rev: A
2.5: To update the XCOMM Firmware, select “Update XComm Firmware.” Wait for the update to complete. Once the
firmware update is finished, cycle aircraft power. Verify “Current Ver.” and “New Ver.” match (if not, restart the GCS
software, reconnect, and restart the whole process).
     Updating XCOMM Firmware
 
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 13/31

## Page 14

Date: 12.Jul.2024
Rev: A
2.6: To update the VTOL Firmware, select “Update VTOL Firmware.” Wait for the update to complete. Once the
firmware update is finished, cycle aircraft power. Verify “Current Ver.” and “New Ver.” match (if not, restart the GCS
software, reconnect, and restart the whole process).
       Updating VTOL Firmware
 
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 14/31

## Page 15

Date: 12.Jul.2024
Rev: A
2.7: If you receive a “Firmware Update Unconfirmed” while updating VTOL firmware, please use the steps below for
guidance.
Firmware Update Unconfirmed
GCS SW needs to be restarted.
Use the “About” menu to verify Firmware Update Confirmation.
If Firmware Failed Update, then Update should be attempted again.
Aircraft Restart only on successful Update or if multiple attempts to restart the process have failed.
 
 
                     Handling Unconfirmed Updates
2.8: Restart the aircraft prior to flight.
2.9: Repeat update procedures for all SGCS1 laptops and other aircraft.
 
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 15/31

## Page 16

Date: 12.Jul.2024
Rev: A
Additional Information
Included below are three sections addressing additional information for the software update. The known limitations
and bugs will help the user identify potential bugs, what you can expect to see, and how to address them. Next,
there is guidance on how to troubleshoot issues that might arise during the software update process. Finally, there
are two tables that will provide a baseline for all systems to be current and up to date.
Known Software Limitations and Bugs:
Software out of date pop up has been suppressed due to reliability issues. User must select Help > About
to verify software configuration.
The VTOL and XComm checksum and firmware version does not reliably display in the GCS. Please
restart GCS software to resolve the issue.
The maintenance log incorrectly reports flight hours but the correct flight count. Time change interval
components affected by this are the cruise motor and servos. Users should use the Files > Vehicle Status
hours to determine time change service interval.
Vehicle endurance estimate during an in-flight simulation might display not enough endurance when there
actually is. Please use pilot’s best judgment.
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
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 16/31

## Page 17

Date: 12.Jul.2024
Rev: A
Current Baseline:
At the conclusion of this software update, the new baseline software and firmware versions shall be the following:
 
Item Version
GCS Software 6.3.4
Autopilot Firmware 6.05p
Autopilot Checksum 0xC4D9
XComm Firmware 4.69
XComm Checksum 0x13F9
VTOL Controller Firmware 1.55
VTOL Controller Checksum 0x7B26
 
The following Silvus & Trillium versions are recommended for use:
 
Item Version
Silvus Firmware 4.0.4.1.1
Silvus Configuration Profile XE4041R1
Trillium ‘Skylink’ Software 24.1.13509
 
 
NOTE
In order to communicate with other Silvus radio nodes on the same network, Silvus radio firmware on all SGCS'
must match and have the same configuration profiles applied. 
 
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 17/31

## Page 18

Date: 12.Jul.2024
Rev: A
Appendix A – VXE30 Firmware Update Notes
Firmware Versions: (Fixed Wing AP: 6.05p, XComm: 4.69, VTOL: 1.55)
 
Overview of Updates: 
A check has been added to the fixed wing autopilot, to ensure a valid mission is loaded before allowing
VTOL launch.
Land Abort behavior has been updated to resolve a bug in the firmware that allowed a partial land abort to
occur, resulting in unpredictable and uncontrollable behavior.
Attitude faults reported during VTOL landing will now activate ELZ.
Glide Landing will now be canceled automatically after receiving a “Go To” command if VTOL is not active.
An alert message for the external magnetometer health has been added to the system.
A fix for PLZ overshoot was included in this update.
A fix on the barometer bias offset calculation was included in this update.
Update to reset the VTOL AP between flights. 
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 18/31

## Page 19

Date: 12.Jul.2024
Rev: A
Vehicle will no longer arm/launch if a mission is not loaded
Summary of New Behavior:
The fixed wing autopilot will now check to ensure that a valid mission is loaded before arming the VTOL
Controller for launch.
 
Previous Behavior:
The fixed wing autopilot would not validate that a mission was loaded prior to arming the VTOL Controller for launch.
This, in combination with a bug found in the GCS, allowed the vehicle to launch with no mission loaded due to uplink
outages to the aircraft. The GCS does not currently ensure that a valid mission is loaded before allowing the
operator to launch.
 
Background: 
A vehicle incident resulting in a crash led to the discovery of multiple software bugs in the VXE system that allow the
vehicle to be launched with no mission if an uplink outage is experienced during the mission upload part of the
launch wizard. The VTOL launch code was corrected to validate mission prior to launching. 
The below “LAUNCH ERROR” window will pop-up if the operator selects “Launch” and no mission has been
successfully uploaded to the aircraft. This message can mean that the mission was not uploaded successfully to the
aircraft. If the “Launch” button has been selected and the pop-up message appears, the aircraft should not activate
its VTOL motors in preparation for launch. The operator’s follow-on action is to close out and reattempt the Launch
Wizard. If VTOL motors do engage with the “LAUNCH ERROR” present, abort aircraft takeoff immediately.
NOTE
Intermittent or Lost Comms could cause a failure to successfully upload the aircraft mission. The operator should
monitor aircraft datalink is sufficient while uploading mission.
 
Launch Failure due to failure of mission upload
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 19/31

## Page 20

Date: 12.Jul.2024
Rev: A
Land abort code patched to resolve partial land aborts
Summary of New Behavior:
N/A
 
Previous Behavior:
System faults were able to trigger autopilot commanded land aborts that were not allowed to complete. This led to
partial abort behavior resulting in the fixed wing autopilot attempting to fly the ELZ mission while the VTOL autopilot
attempted to continue landing.
 
Background:
The flight phase where the vehicle is transitioning between fixed wing and VTOL flight capabilities, is the riskiest
phase of flight. Additionally, starting that transition and aborting back to the previous flight mode has an even further
risk that is relative to what part of transition the abort starts from. To mitigate unacceptable risk, some parts of the
transition are not allowed to be aborted from. This is logic that has been part of VXE for a long time.
While the firmware previously contained logic to determine if the current state is an allowed state to abort from, this
functionality was not universally enforced in the code. This meant some states that were not valid abort states would
still complete part of the abort behavior which led to the land abort bug.
For this software revision, it was decided to modify the code to enforce the already defined parameters of abort
behavior.
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 20/31

## Page 21

Date: 12.Jul.2024
Rev: A
Attitude faults reported during VTOL landing will now activate ELZ
Summary of New Behavior:
If an attitude fault is reported during the transition phase of flight in any VTOL landing type (“RTB” and
“Land Immediately!”), the fixed wing autopilot will now automatically:
Disable and safe the VTOL motors.
Activate and proceed to IP1 in the ELZ landing pattern.
 
Previous Behavior:
If an attitude fault was reported during various states in VTOL landings, the fixed wing autopilot would cut and safe
the VTOL motors. This behavior resulted in the vehicle immediately falling to the ground.
 
Background:
If an attitude fault was reported during the transition phase of a VTOL landing it was assumed that the VTOL has lsot
stability. In this case, it was also assumed to be safer to crash the vehicle immediately where it is than to let the
system continue to fly unpredictably. 
However, after consideration during land abort behavior review, it was decided to update the code in this release to
allow the vehicle to attempt an ELZ landing in the event of VTOL failure. The new behavior still disables the VTOL
system, but it also lets the fixed wing attempt to recover the vehicle and glide land.
 
WARNING
Do not attempt to retry VTOL landing after an attitude fault. This action may result in uncontrolled flight.
 
Below are the dialog of screenshots seen on the GCS during activation of ELZ due to an attitude fault.
 
ELZ activation message.
 
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 21/31

## Page 22

Date: 12.Jul.2024
Rev: A
 
 
Alert that the vehicle has entered Glide Landing Pattern.
 
ELZ activated on GCS.
 
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 22/31

## Page 23

Date: 12.Jul.2024
Rev: A
Glide Landing automatically deactivates after receiving a “Go To”command
Summary of New Behavior:
The “Go To” command will now automatically deactivate glide landings. A glide landing is performed either
by using the ELZ landing pattern or by commanding “Land Immediately!”- when the ELZ is selected as the
active landing pattern and the aircraft is flying at an active waypoint type. When the aircraft receives the
“Go To” command while conducting a glide landing, the vehicle will now adopt commanded mission
waypoint properties, including altitude. The GCS will continue to show the “land override” window until a
land abort is commanded.
 
Previous Behavior:
Glide landing would not be deactivated unless an abort command was sent. If a “Go To” command was sent during
an active glide landing, the vehicle would change course to fly to the commanded waypoint, but the vehicle would
continue to descend.
 
Background:
This behavior was discovered during testing. It was decided to automate the abort landing behavior if a “Go To”
command is sent and the VTOL is not active.  After receiving the “Go To" command after IP5 of the ELZ, the GCS
will continue to show the “Landing Active” window but the vehicle will continue to the commanded waypoint (see
Figure 1). If user landing control has been activated (see Figure 3). 
 
Figure 1 “Landing Active” window remains open after “Go To” command
 
 
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 23/31

## Page 24

Date: 12.Jul.2024
Rev: A
To avoid accepting nudge commands, click “Abort Landing”. 
 
Figure 2 Click “Abort Landing” to clear “Landing Active” window
 
Follow if “Activate User Landing Control” is selected and active. Once user landing control has been activated, the
vehicle will accept all inputs from the hand controller even if the active waypoint is outside of the landing zone. Click
“Abort Glide Landing” to disable the “Glide Landing Override” window. This will prevent the vehicle from receiving
controller input.  
 
Figure 3 Click “Abort Glide Landing” to clear the “Glide Landing Override” window and prevent nudge in flight
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 24/31

## Page 25

Date: 12.Jul.2024
Rev: A
An alert for health of the external magnetometer has been added tothe system
Summary of New Behavior:
Alert messages with different levels of severity have been implemented. The following describes each
level of severity.
–  
  Advisory or Informational message to provide situational awareness for the
operator. 
 –  
  Caution message that provides information of an issue that may have some level
of urgency and could require an action on the part of the operator to mitigate. 
 –  
  Warning message that informs the operator of a critical issue that should be
addressed immediately. 
The center wing external VTOL magnetometer data is excluded from the heading calculation during
landing when a sensor fault is detected. Heading measurements during VTOL and transition phases of
flight condition shall be considered degraded.
The operator is notified when the “Magnetometer fault” is detected as a Pop-Up Alert in regard to a
“Navigation” fault that will display either a Caution, Warning, or Advisory message.
 
Example message of Magnetometer fault.
The operator is notified when the sensor fault clears for more than 30 seconds. Assume normal operation
of the aircraft after a fault has cleared.
 
Magnetometer fault cleared message
A 3rd fault causes a hard failure of the sensor and is reported to the operator. This fault will not clear. 
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 25/31

## Page 26

Date: 12.Jul.2024
Rev: A
NOTE
 Faults experienced prior to launch do not count against the 3 faults rule. Ensure aircraft is free of metal objects and
test payloads for operability as both may trigger external magnetometer faults.
 
Alert message after 3rd Magnetometer fault.
 
The section below describes fault alerts and advice to the operator on what action to take dependent upon
the phase of flight.
 
1. Preflight
Restart the aircraft and make sure there are no outside factors (I.E. magnetic sources,
metals) disrupting the external magnetometer.
If issue persists:
Perform magnetometer check and calibration (if necessary) with gimbal and/or
payload installed.
 Send AAR to support email @ Globalsupport@edgeautonomy.io.
“CAUTION: Navigation
“ACTION: “Do Not Launch”
 
1. Launch
“CAUTION: Navigation”
“ACTION: “Abort VTOL Launch”
Send AAR to support email address.
 
 
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 26/31

## Page 27

Date: 12.Jul.2024
Rev: A
NOTE
Aircraft should auto-abort launch sequence. If the aircraft does not auto-abort, the Operator shall manually abort the
launch.
 
3. Fixed Wing Flight 
If fixed wing mag data is available:
“CAUTION: Navigation”
“ACTION: None. VTOL using FW Mag”
The external VTOL magnetometer is not used while in fixed wing flight.
The operator may continue with the mission and aircraft will use the fixed wing magnetometer
for VTOL landing if mag fault does not clear. 
 
If no fixed-wing mag data is available:
“CAUTION: Navigation”
“ACTION: See Bad Mag Procedure”
Operator shall follow the Bad Mag Procedure documented below.
Send AAR to support email address.
 
  
 
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 27/31

## Page 28

Date: 12.Jul.2024
Rev: A
4. Landing
If fixed-wing mag data is available: 
“CAUTION: Navigation”
“ACTION: None. VTOL using FW Mag”
The aircraft will continue to land once the VTOL motors are active.
Pausing and Nudging may still be used with Pop-Up alert displayed and
should be used minimally, as possible.
Send AAR to support email address.
 
If no fixed-wing mag data is available: 
“WARNING: Navigation”
“ACTION: Land Immediately”
If this fault is encountered during the VTOL landing, the Operator continues performing
normal landing procedure and shall exercise extreme caution with all people and property on
the ground.
Send AAR to support email address.
 
NOTE
The aircraft won’t automatically abort before IP5 in the PLZ landing pattern if fixed wing mag data is unavailable.
 
 
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 28/31

## Page 29

Date: 12.Jul.2024
Rev: A
 
5. Postflight
“NOMINAL: Navigation”
“ACTION: “System Maint Required”
Send AAR to support email address.
 
 
Previous Behavior:
A magnetometer fault was recorded in the logs and data from a backup sensor was used if that backup sensor was
healthy.
 
Background:
Improvements to magnetometer processing were implemented based on data review from multiple incidents.
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 29/31

## Page 30

Date: 12.Jul.2024
Rev: A
Bad Mag Procedure
If the vehicle can’t land within 10 minutes then errors in the navigation solution could grow to the point where it
may be dangerous to execute a VTOL landing. In this case do the following:
1. Execute an ELZ glide landing if possible
If the vehicle can be recovered in less than 10 minutes or if an ELZ landing is not possible in the area of
operations, then proceed with the following procedure to handle the system if a loss of control is observed.
If the vehicle begins to descend, but appears to be flying unevenly, is dangerously unlevel, or meets
any of the following criteria:
Large attitude variations in roll or pitch
Continuous rotation in yaw (full circle or more)
Pronounced variability in lift system sound
Steady-state or increasing oscillation
Do the following:
1. Activate PLZ and perform PLZ or Land Immediately! landing. 
2. Activate Landing Override by clicking the “Activate User Override” button in the Landing Active dialog.
3. Switch to U-drive mode by moving the slider in the Status window of the GCS or by clicking the
“Manual Nudge” button in the User Override dialog. This will activate the Manual Mode Override
(described in Flight Modes with Direct Operator Control). Help to steer the vehicle safely to the ground.
4. Once the vehicle has landed, wait a few seconds for the flashing red light on top of the wing to go out.
The lift motors should also beep and re-align the rotors.
5. If, after five seconds, the light does not go out and the lift motors do not beep and re-align: wear eye
protection and carefully approach the vehicle coming directly in along the tail boom. Push and hold the
red light on the top of the center wing until the light goes out.
 
WARNING
If the vehicle unexpectedly powers up rotor blades can cause injury. If the rotors are just powering up and have
low torque, the injury will be less severe, however at full speed, rotor blades can cause serious injury. Never
approach a moving rotor. If a rotor blade hits something solid, including a person, it could shatter sharp plastic
fragments, which could also cause injury. When approaching the vehicle, wear eye protection to prevent plastic
debris from injuring your eyes.
 
 
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 30/31

## Page 31

Date: 12.Jul.2024
Rev: A
VTOL Reset between flights
Summary of New Behavior:  
During the Launch Wizard when the FW AP is reset, the VTOL AP will be reset. This can take up to
120 seconds but is usually much faster.  
During the reset, “No center wing detected” warnings will be suppressed as it will be expected since
these warnings are triggered by the lack of an active data connection to the autopilot.  
 
Dialog window displaying VTOL AP resetting
 
Previous Behavior: 
The VTOL AP was not reset or power cycled between flights explicitly.  
 
Background:
It was observed over multiple flights without a power cycle that the VTOL could experience an exception when
calculating the CRC of the configuration parameters when queried from the GCS.  
To prevent this from adversely affecting flight, the VTOL AP will be reset at the beginning of the Launch Wizard.
This is expected to add about a minute to pre-flight checks.  
 
 
Airworthiness Directive (AD)_Software Update_2024-08-08_A
   
8/8/24, 3:11 PM Web Manuals - Reader
https://edgeautonomy.webmanuals.aero/1720487990917/manual/4551812/next/n/18 31/31
