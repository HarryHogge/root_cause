# User Guide - Athena Management Service - 1.1.pdf

Attachment 22211, pdf, 4210 KB, added 2024-07-30 by Mike DeJesus.

## Page 1

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
1 of 74 
 
Athena Management Service User Guide 
User Guide – Athena Management Service Software 
Configuration and maintenance of supported Athena AI software 
AMS Release Version: 1.1.0 
April 17 2024

## Page 2

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
2 of 74 
 
Overview 
 
General 
The Athena Management Service (AMS) is a locally hosted website enabling a user or administrator 
to change parameters and monitor system performance at runtime , through a unified management 
interface. 
 
The AMS supports the following Athena AI software products: 
- Computer Vision Inference Pipeline (CVIP) 
o Full Motion Video AI detection, recognition, and identification. 
- Battle Tracking Service (BTS) 
o Track geo-tagging, pattern of life analysis and data dissemination. 
- Decision Support Service (DSS) 
o Augmentation of sensor-to-effector workflows using weapons effects and battlespace 
data analytics. 
- Geospatial Services (GEO) 
o AI enabled analysis of geospatial imagery for rapid insights. 
 
Document Intent 
This document will cover items such as: 
- Package installation and removal of Athena AI software products (including the AMS) 
- Configuration of supported software products 
- Troubleshooting supported software products 
- Miscellaneous workflow guides and suggested usage

## Page 3

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
3 of 74 
 
Table of Contents 
Overview ......................................................................................................................................... 2 
General ........................................................................................................................................ 2 
Document Intent ......................................................................................................................... 2 
Table of Contents ........................................................................................................................ 3 
Applicable Software Versions ......................................................................................................... 6 
Athena Management Service (AMS) Web Interface ...................................................................... 7 
Accessing the Athena Management Service ............................................................................... 7 
Supported Browsers ............................................................................................................... 7 
Athena Management Service Quick Looks ..................................................................................... 8 
Quick Look: First time installation of Athena Management Service ...................................... 8 
Quick Look: Connecting to Athena Management Service ...................................................... 9 
Quick Look: Updating an Installed Package/Service ............................................................. 11 
Quick Look: Licensing an Athena Product............................................................................. 13 
Quick look: Service Status Indication .................................................................................... 14 
Quick Look: Controlling A Service’s State ............................................................................. 15 
Quick Look: Making configuration changes at runtime ........................................................ 16 
Quick Look: Accessing Logs ................................................................................................... 17 
Quick Look: Updating AMS ................................................................................................... 19 
Quick Look: System Configuration ........................................................................................ 23 
Computer Vision Inference Pipeline (CVIP) .................................................................................. 25 
Computer Vision Inference Pipeline Quick Looks ..................................................................... 25 
Quick Look: Starting the CVIP ............................................................................................... 25 
Quick Look: Imagery Uploading ............................................................................................ 26 
Quick Look: Loading Input Imagery ...................................................................................... 27 
Quick Look: Example usage of AMS to run CVIP................................................................... 28 
Quick Look: Watching a RTSP stream ................................................................................... 34 
Quick Look: Watching a CVIP demo video ............................................................................ 35 
Quick Look: Accessing Inference Artifacts ............................................................................ 36 
Profiles ...................................................................................................................................... 37

## Page 4

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
4 of 74 
 
Overview of Profiles .............................................................................................................. 37 
Uploading Profiles ................................................................................................................. 37 
Viewing Profiles .................................................................................................................... 39 
Saving the latest configuration ............................................................................................. 40 
Expected Values ........................................................................................................................ 41 
System Inputs ........................................................................................................................ 41 
System Outputs ..................................................................................................................... 44 
Detection and Recognition Models ...................................................................................... 48 
Data Processing ..................................................................................................................... 51 
Known Issues ............................................................................................................................. 54 
Troubleshooting ........................................................................................................................ 55 
Poor Performance ................................................................................................................. 55 
Constant restarting state of CVIP ......................................................................................... 55 
Object Localisation Service (OLS) .................................................................................................. 57 
Expected Values ........................................................................................................................ 57 
Geolocalisation Variables ...................................................................................................... 57 
Geolocalisation Confidence .................................................................................................. 58 
Battle Tracking Service (BTS) ........................................................................................................ 59 
Battle Tracking Service Quick Looks ......................................................................................... 59 
Quick Look: CVIP Configuration for BTS................................................................................ 59 
Quick Look: Connecting to a TAK server. .............................................................................. 60 
Quick Look: Interacting with BTS markings in ATAK. ............................................................ 62 
Quick Look: Using the BTS Chat Service................................................................................ 63 
Quick Look: Clearing BTS tracks from ATAK.......................................................................... 65 
Battle Tracking Service User Guide ........................................................................................... 67 
TAK server connections. ....................................................................................................... 67 
BTS Chat Service. ................................................................................................................... 67 
BTS ATAK Symbology. ........................................................................................................... 68 
Decision Support Service (DSS) ..................................................................................................... 71 
Decision Support Service Quick Looks ...................................................................................... 71 
Troubleshooting ............................................................................................................................ 72

## Page 5

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
5 of 74 
 
Constant Establishing Connection Screen............................................................................. 72 
Error When Downloading a File ............................................................................................ 74

## Page 6

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
6 of 74 
 
Applicable Software Versions 
Athena Management Service   : 1.1.0 
Athena Computer Vision Inference Pipeline : 1.1.0 
Athena Battle Tracking    : 1.1.0 
Athena Object Localisation    : 1.1.0

## Page 7

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
7 of 74 
 
Athena Management Service (AMS) Web Interface 
The AMS displays installed Athena services on the system alongside some useful utility options that 
can be used to enhance the user’s experience  such as a RTSP stream viewer, system configuration 
options and diagnostic tools. 
 
The interface of the AMS looks like this: 
 
Each tab can be clicked on and collapse d to show related information and tools.  
 
To learn how to configure an Athena service, see  it’s associated section in the documentation 
(Computer Vision Inference Pipeline (CVIP) , Object Localisation Service (OLS) , Battle Tracking 
Service (BTS) , Decision Support Service (DSS)) 
 
Accessing the Athena Management Service 
To access the Athena Management web page, in the address bar of a supported browser, navigate to 
the URL: 
http://<IP_OF_SYSTEM_HOSTING_AMS> 
Supported Browsers 
- Firefox 
- Chrome 
- Safari 
- Opera 
- Microsoft Edge 
- Samsung Internet 
 
A login page will appear, input the credentials provided by the Athena AI team and click Login.  
Please see the connection ‘Quick Look’ for more information.

## Page 8

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
8 of 74 
 
Athena Management Service Quick Looks 
 
Quick Look: First time installation of Athena Management Service 
To install the Athena Management Service for the first time, an administrator of the device will need 
to use the Apt or DPKG package management tools. 
Using APT, the host system’s command line: 
$ sudo apt install {location_of_ams_debian_package} 
 
After which a set of checks will be made to ensure that certain network ports are able to be used. 
 
NOTE: Ensure that the command finishes completely, interrupting this process can cause corruption 
of the Debian package

## Page 9

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
9 of 74 
 
Quick Look: Connecting to Athena Management Service 
To access the Athena Management web page, in the address bar of a supported browser, navigate to 
the URL: 
http://<IP_OF_SYSTEM_HOSTING_AMS> 
 
A login page will appear: 
 
The default credentials are: 
Username: amsuser 
Password: [password removed] 
 
If an Athena Vision Management Service was previously installed at some point (< version 1.0) then 
the default credentials would be: 
 
Username: vmsuser 
Password: [password removed] 
 
For security purposes, it is recommended to alter these credentials. See Account for more 
information.

## Page 10

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
10 of 74 
 
The webpage will make a connection to the device hosting the AMS. If a connection is made, the status 
should say Connected.  
 
 
 
If a connection is not established, you will see this screen. 
 
An attempt to re-establish connection  is done  periodically every 5 seconds  until it successfully 
establishes a connection. If this view persists, attempt to refresh the page. See the “Troubleshooting” 
section for help if this issue remains after a refresh of the page.

## Page 11

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
11 of 74 
 
Quick Look: Updating an Installed Package/Service 
Via webpage 
To update a service, head to the System Configuration -> Packages tab, click the Debian Package 
Upload button and select an Athena AI service package. 
 
Once the Debian package has been successfully uploaded it will appear within the file explorer. To 
queue an update of a service, click on the Install button of the associated Athena AI service package:

## Page 12

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
12 of 74 
 
After acknowledging the warning prompt that a full installation of the package will take 
approximately 5 minutes to complete the installation then the installation will be queued and 
executed as soon as the system can. A prompt such as the following will be shown to inform that the 
installation is now being performed for the given service: 
 
When the service has been fully installed successfully the user will get the following prompt: 
 
After which the associated collapsible will show in the AMS webpage with corresponding version 
that the service was updated to:

## Page 13

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
13 of 74 
 
Quick Look: Licensing an Athena Product 
Specific Athena products provided by the Athena Management Service now require an active 
license to function correctly. The following is a step-by-step guide to request and activate a license 
for a given product: 
1. Within the AMS webpage, head to the System Configuration -> Licenses tab 
 
2. For a product that we want to request a license for (let’s say CVIP as an example) we 
firstly need to input a license key into the text field 
 
3. Click on the “Request” button for the product. A request file should be downloaded. 
 
4. Once the request file is downloaded, click on the link within the prompt to be directed to 
the Athena licensing server. 
 
5. Upload the request file to the Athena licensing server. Once uploaded, a license key file 
(.lic) will be downloaded. 
 
6. Return to the AMS webpage and the System Configuration -> Licenses tab. Click on the 
“Activate” button and upload the license key file (.lic) 
 
7. Once the license key has been uploaded, a prompt showing that the license was 
successfully activated will be presented. 
 
If you find any issues with activating a license for an Athena product, please contact 
visionsupport@athenadefence.ai

## Page 14

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
14 of 74 
 
Quick look: Service Status Indication 
When using the AMS to run these services, there is an indicator on the web page to show whether the 
service is running, restarting, or not running. This will be seen at the top of the associated service’s 
configuration section. 
 
When the service is not running the section will look like this: 
  
NOTE: When a service is not running, all configuration tabs will be locked until the service is running. 
 
If a service goes into a constant restarting state or if, after turning on the service the indicator goes 
back to red then see steps to rectify the issue in the Troubleshooting section for that service.

## Page 15

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
15 of 74 
 
Quick Look: Controlling A Service’s State 
To alter the state of one of these services, use the buttons highlighted below. 
 
The following explains the functionality of these control buttons: 
• Play button will start the service with the latest configuration. 
• Restart button will stop the service and start again using the latest configuration. 
• Stop button will stop the service thus causing all configuration tabs to be locked.

## Page 16

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
16 of 74 
 
Quick Look: Making configuration changes at runtime 
Changing values 
When changing values, all additions/edits to fields on the webpage are not instantly configured upon 
user input. Instead, users will need to apply configurations once they are satisfied that the fields are 
set as desired to configure a service. 
 
See the relevant properties table in the service’s Expected Values section for more information 
 
Applying configurations 
When configurations are pending to be applied (input fields with a blue border), the “Apply Changes” 
button will be highlighted and a note to signal to the user to configure changes. To apply the 
configuration settings that have been filled in on the AMS, click on the "Apply Changes" button. 
Depending on the changes made, it may take up to 5 seconds for them to be applied. 
  
Reseting configurations 
In the instance where a set of input fields have been given incorrect/undesirable values, users can 
click on the “ Reset Changes” button to revert the changes made to all input fields of a given service 
back to the values that the service is currently configured as.

## Page 17

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
17 of 74 
 
Quick Look: Accessing Logs 
Viewing Live Logs 
To view live logs, click on the "Logs" button within the service’s configuration tab. A window will 
display all the logs of the currently running instance of the service. 
 
 
 
To view service logs, users need to scroll to the bottom of the window. This action signals to the AMS 
that the user wants to view the logs in real-time. If the scroll is not at the bottom of the window, the 
view of that section of the logs will be preserved, allowing users to read certain sections without 
interruption from auto-scrolling due to additional logs.

## Page 18

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
18 of 74 
 
Downloading Logs 
Logs can be downloaded via the logs explorer located in the “System Configuration” -> “Logging” tab. 
Here, users will be able to view logs from the desired service’s logs directory. If the directory becomes 
too cluttered, individual logs can be deleted by pressing the delete button. The ability to download 
the whole logs directory for a given service can be done by pressing the “Download” button.

## Page 19

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
19 of 74 
 
Quick Look: Updating AMS 
To update the AMS, users can open the System Configuration -> Packages tab which will contain a file 
explorer and the ability to upload a Debian package. As seen below, this AMS currently has the 
athena-vision-management-service_0.12.21_arm64.deb package installed: 
 
How to update AMS 
 Via webpage 
1. Click on the Debian Package Upload button. 
2. Select an AMS Debian package. NOTE: An AMS package will need to be in either of the 
following formats to be able to be installed via the file explorer: 
 
athena-vision-management-service_{version_number}_{device_architecture}.deb 
athena-vision-management-
service_{version_number}_{customer_code}_{device_architecture}.deb 
 
An upload of the package will occur and once done will prompt the user that the file 
upload has succeeded.

## Page 20

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
20 of 74 
 
 
 
The newly uploaded AMS Debian package will appear in the file explorer. 
 
 
 
Click on the Install button to queue an installation of the package. Once the system has 
begun installing the package the browser will lose connection to the server hosting 
the webpage. It is recommended to refresh the page after around 5 minutes to ensure 
ample time to fully install the package. 
  
 Via command line 
To update the Athena  Management Service on the command line, execute  the following  
command: 
 
$ sudo apt install {location_of_ams_debian_package}

## Page 21

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
21 of 74 
 
Backing up files 
Upon updating the AMS, all files within the /usr/share/athena-vision-management-
service/file-system directory will be saved across updates of the AMS. Which means any files 
in file explorers within the AMS will all be saved into the new version of AMS, such files that 
will be backed up are for example: 
• Debian Packages 
• Config files 
o CVIP config files 
o Pylon camera config files 
• Imagery 
• Inferenced Artifacts 
• Logs

## Page 22

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
22 of 74 
 
Verifying a valid Debian package 
A .md5 file has been provided alongside the Debian package of the AMS. To verify that the 
Debian package has not been corrupted run the following commands: 
md5sum {path_to_a_AMS_deb_package}.deb  
cat {path_to_corresponding_AMS_md5}.md5 
If both values are the same, then the Debian package has been downloaded correctly onto the 
device. If they’re not the same, then the Debian package has been corrupted and it is 
recommended to attempt to download the Debian package again.

## Page 23

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
23 of 74 
 
Quick Look: System Configuration 
Account 
The credentials of a user can be updated by going to the System Configuration -> Account tabs. Input 
into the username field the desired user to change the password of. Add the new password into the 
necessary password fields and click the Set button. 
 
If the system successfully updates the credentials a popup such as the following will appear:

## Page 24

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
24 of 74 
 
Package Configuration 
The System Configuration -> Packages tab is the main way to upload and install updates to the AMS 
and Athena services.  Any Athena packages that are installed and stored within  the 
/usr/share/athena-vision-management-service/file-system/debian-packages directory will have a 
tick in the Installed column. 
 
 
For assistance with updating the AMS head to the Quick Look: Updating AMS  section. Otherwise, if 
updating any other Athena service then go to the Quick Look: Updating an Installed Package/Service 
section. 
 
Power 
The power of the device hosting the AMS can be altered via the webpage. In. the System Configuration 
-> Power tab the user will have the option to turn off or restart the device.

## Page 25

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
25 of 74 
 
Computer Vision Inference Pipeline (CVIP) 
 
Computer Vision Inference Pipeline Quick Looks 
Quick Look: Starting the CVIP 
To start the CVIP, a profile file must be used. To use a profile, in the “CVIP Profiles” tab is a file explorer 
which contains any CVIP profiles that have been uploaded or saved to the AMS (/usr/share/athena-
vision-management-service/file-system/CVIP/configs/vision-configs). To make the CVIP use a profile, 
press the “Load” button. 
 
A ‘default.cfg’ profile will always be packaged within the AMS to allow for users to quickly run the 
CVIP with a basic configuration. It is suggested that users do not alter this profile as it provides a good 
starting state to configure the CVIP from the AMS and a solution to the CVIP being in a configuration 
that is invalid.

## Page 26

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
26 of 74 
 
Quick Look: Imagery Uploading 
Imagery upload can be found within the “ Inference Pipeline->System Inputs->Imagery Explorer” tab. 
When uploading imagery, the following file formats are accepted: 
jpg, jpeg, ts, tts, mp4, mov, avi, zip 
 
Note: If the user wants to upload a folder of imagery, a zip file is recommended to upload. Therefore, 
to zip a file run the following command: 
 
$ zip -r <output_file> <directory_to_compress> 
 
Currently, for security precautions  the zip file will not be unzipped upon a successful uploa d. 
 
Imagery will be uploaded to “ /usr/share/athena-vision-management-service/file-
system/CVIP/imagery”. By uploading a set of imagery into this directory, users can set the fmv_uri 
property within a CVIP config file to point to “ /usr/share/athena-vision-management-
service/uploads/imagery/{imagery_name}”. To set the fmv_uri easily with the correct path to the 
desired input imagery, click the “Load” button of the associated imagery in the file explorer.  See the 
Quick Look: Loading input imagery section for more information.

## Page 27

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
27 of 74 
 
Quick Look: Loading Input Imagery 
Users can quickly configure the CVIP to inference on input imagery by accessing the “ Inference 
Pipeline -> Inputs -> Imagery Explorer” tab in AMS.  
 
By clicking the “Load” button on a set of imagery, the AMS will set the FMV URI to the location of that 
imagery. If the value of the FMV URI was set correctly the following is the expected view: 
 
 
Note: Transport stream files (.TS) without In-Band KLV Metadata as input are currently not 
supported and may cause undefined behaviour

## Page 28

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
28 of 74 
 
Quick Look: Example usage of AMS to run CVIP 
 
This section will go through a step -by-step example for running the CVIP using a configuration file 
and by setting up a configuration using the UI elements in the webpage. However, understand that 
these examples are a quick guide to be able to use a specific type of input imagery and output to a 
specific format.  
Additional configuration settings may need to be altered depending on input imagery to achieve the 
best results. 
To see configuration options available by the CVIP see the  System Inputs , System Outputs  and 
Detection and Recognition Models sections. 
Using a profile 
1. Upload a profile to use (For more detail see Uploading Profiles) 
 
2. Click “Load” on the uploaded config file (For more detail see Quick Look: Starting the CVIP 
using a profile) 
3. Verify that the CVIP is running 
 
 
 
4. If output imagery settings are configured to host an RTSP video stream, the output video can 
be viewed within the Video tab (See Quick Look: Watching a RTSP stream  for more detail)  
 
Otherwise, all inferenced artifacts can be accessed in the file explorer within the Inference 
Pipeline->Inferenced Artifacts tab (See Quick Look: Accessing Inference Artifacts  for more 
detail)

## Page 29

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
29 of 74 
 
Setting a configuration 
1. Click “L oad” in the profile explorer on  default.cfg to have the CVIP in a running state to 
consume configuration messages (For more detail see Quick Look: Starting the CVIP using a 
profile) 
2. Once the CVIP is in a running state, a user can modify any configuration setting in the tabs  
 
For example, the default configuration for the Imagery Overlay section is: 
 
 
 
In the instance that the user modifies some of these fields, the interface will look like the 
following (as mentioned previously, blue border around a configuration element indicates a 
modified and non-applied configuration):

## Page 30

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
30 of 74 
 
Once the user has clicked Apply Configuration , the fields will now reflect the latest 
configuration of the CVIP: 
 
 
 
 
RTSP to RTSP 
1. Click “L oad” in the profile explorer on  default.cfg to have the CVIP in a running state to 
consume configuration messages (For more detail see Quick Look: Starting the CVIP using a 
profile) 
2. Alter FMV URI to the address of the RTSP stream

## Page 31

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
31 of 74 
 
 
 
3. In System Outputs -> Imagery Settings, ensure that RTSP Video Stream is enabled  
 
4. Click Apply Configuration and wait for the CVIP to output an RTSP stream 
5. To watch the  RTSP stream, visit the Video tab  (For more information check  Quick Look: 
Watching a RTSP stream) 
RTSP to JPEG 
1. Click “L oad” in the profile explorer on  default.cfg to have the CVIP in a running state to 
consume configuration messages (For more detail see Quick Look: Starting the CVIP using a 
profile) 
2. Alter FMV URI to the address of the RTSP stream

## Page 32

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
32 of 74 
 
3. In System Outputs -> Imagery Settings, ensure that JPEG Folder Output is enabled 
 
 
 
4. Click the Apply Changes button and wait for the CVIP to output an RTSP stream 
5. To see the inference artifacts, visit the Inference Artifacts Explorer tab. For more information 
see Quick Look: Accessing Inference Artifacts. 
JPEGS to JPEGS 
1. Click “ Load” in the profile explorer on default.cfg to have the CVIP in a running state to 
consume configuration messages (For more detail see Quick Look: Starting the CVIP using a 
profile) 
2. Click “Load” in the imagery explorer on a folder of JPEGS  (For more detail see  Quick Look: 
Loading input imagery) 
3. In System Outputs -> Imagery Settings, ensure that JPEG Folder Output is enabled 
 
 
 
4. Click the Apply Changes button 
5. Wait for the CVIP to start inferencing. All  inference artifacts will be located in the 
corresponding timestamped directory in the Inference Artifacts Explorer . For more 
information see Quick Look: Accessing Inference Artifacts 
JPEGS to RTSP 
1. Click “ Load” in the profile explorer on default.cfg  to have the CVIP in a running state to 
consume configuration messages (For more detail see Quick Look: Starting the CVIP using a 
profile) 
2. Click “Load” in the imagery explorer on a folder of JPEGS

## Page 33

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
33 of 74 
 
3. In System Outputs -> Imagery Settings, ensure that RTSP Video Stream is enabled 
 
 
4. Click the Apply Changes button. 
5. Wait for the CVIP to start inferencing. All inference artifacts will be located in the 
corresponding timestamped directory in the Inference Artifacts Explorer.  For more 
information see Quick Look: Accessing Inference Artifacts

## Page 34

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
34 of 74 
 
Quick Look: Watching a RTSP stream 
 
To watch an RTSP stream, an Athena Computer Vision Inference Pipeline (CVIP) must be outputting 
an RTSP stream on the device. Verify this by checking that the Unicast RTSP Video toggle in the 
Inference Pipeline -> Outputs -> Imagery tab is on: 
 
If this isn’t toggled on, click on the toggle and click on the Apply Changes button. For help configuring 
the CVIP head to the Expected Values section. Once the CVIP is outputting a RTSP stream, head to the 
Inference Pipeline -> Video tab, select CVIP Output in the selector and click on the play button to watch 
the RTSP stream: 
 
Once the connection to the RTSP stream has been established the stream will be visible:

## Page 35

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
35 of 74 
 
Quick Look: Watching a CVIP demo video 
To watch a demo video of the CVIP, head to the Inference Pipeline -> Video tab and using the 
video/stream selector select one of the two test videos provided. Once an option has been selected, 
click the play button and the video will be shown in the web player like so: 
 
 
When hovering over the stream, the following icon can be used to pop out the video from the web 
player:

## Page 36

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
36 of 74 
 
Quick Look: Accessing Inference Artifacts 
 
Inference artifacts can be found within the “ Inference Pipeline ->Inference Artifacts Explorer”  tabs. 
Here, users can download or delete inferenced artifacts that are outputted by the CVIP. In this file 
explorer, there will be a list of directories named according to the time of which the CVIP was started. 
This file explorer is sorted by creation time and so will show the most recent inference artifacts at 
the top of the file explorer: 
 
In these timestamped inference artifacts directories exists a “ Payload” and an “Imagery ” directory. 
Depending on the configuration of the CVIP, when “ MQTT Payload Stream”  is turned on, MQTT 
payloads will be saved into the Payload directory in the form of a .txt file.  
 
 
 
Whereas having “MPEG-TS Video File" and/or “JPEG Folder Output” will save the necessary file into 
the “Imagery” directory.

## Page 37

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
37 of 74 
 
Profiles 
Overview of Profiles 
 
A profile is a collection of settings used by the software describing its desired functions and states. 
Profiles are primarily used to quickly configure the state of the CVIP for  system inputs, system 
outputs, detection and recognition models and data processing to a configuration known to produce 
effective results from the CVIP.  
Please Note: A profile must contain a ‘.cfg’ file extension.  
Uploading Profiles 
CVIP Profiles 
To upload a profile to the AMS, click on the Profile Upload button. This will prompt the user 
to upload a .cfg file. After uploading a profile, it will be visible within the file explorer. 
 
If a profile with the same name as an already existing file is uploaded onto the device, the new 
profile will overwrite the profile.

## Page 38

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
38 of 74 
 
Pylon camera config files 
 
The uploading of Pylon camera config files can be found in “Inputs->Pylon Configuration" 
within the “Inference Pipeline” tab. Here, you will be able to upload a .pfs file (Camera Config 
File that can be generated via Pylon Viewer Software). Keep in mind that uploading a Pylon 
camera config file will not automatically configure it for the pipeline. You will need to enable 
the “Use Pylon CFG File” toggle and click Load on the given file. Following this click the “Apply 
Changes” Button to apply the desired changes.

## Page 39

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
39 of 74 
 
Viewing Profiles 
CVIP Profiles 
Upon uploading a CVIP profile, users will be able to view the profile in the file explorer. This 
will display all profiles within the /usr/share/athena-vision-management-service/file-
system/CVIP/configs/vision-configs directory.  
 
By clicking on a table row in the file explorer containing a file, a pop up will show the contents 
of the config file  (viewing other config file types will work the same as this) . Here are the 
contents of “new.cfg”: 
 
 
 
The ability to download, delete or load the profile is also possible within the file explorer. 
When clicking on the load button, the CVIP will load the properties of the profile and update 
all property values within the AMS webpage.

## Page 40

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
40 of 74 
 
Saving the latest configuration 
CVIP Profiles 
When a user has altered the values of properties via the webpage and wants to be able to save 
the latest configuration that the CVIP is currently configured upon, A user can input a file 
name of their choice into the input field including the necessary file extension (.cfg) and click 
the Save Profile button to save the current configuration as a profile. The file explorer will 
update and show the newly saved file.

## Page 41

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
41 of 74 
 
Expected Values 
System Inputs 
The CVIP can be configured to process a variety of input imagery, through configuration of the Inputs 
drop-down panel of the AMS. 
See Quick Look: Loading input imagery for detailed instructions to run selected imagery. 
The following sections will outline supported imagery types, and how to configure the CVIP to use 
them. 
 
Supported Input Imagery Containers 
• MPEG-4 Part 14 (.mp4)  
• Audio Video Interleave (.avi)  
• MPEG-2 Transport Stream (.ts)  
• MPEG Transport Stream (.ps)  
• Matroska (.mkv)  
 
Supported Input Imagery Codecs 
• MPEG-TS (STANAG-4609 Supported) 
• H.264 
• H.265 
• JPEG Stills (See <configuring JPEG inputs section>) 
• MJPEG 
 
Supported Input Imagery Protocols 
• RTSP  
• Unicast UDP  
• Multicast UDP  
• SRT

## Page 42

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
42 of 74 
 
Input Imagery Properties 
Property Meaning Type and 
Range 
Auto Restart on 
Stream Disconnect 
or EOS signal 
Sets the CVIP to restart upon a UDP or RTSP stream 
disconnect and an end of stream signal 
Boolean 
FMV URI Input URI to the encoded stream. The URI can be a file, an 
HTTP URI, an RTSP live source, v4l2 device source, UDP live 
source, pylon device or an argus video device source. 
String 
Input Width User input width of the input video. Failing to match this 
value with the input video’s width will result in scaling being 
performed, potentially causing performance issues. 
Integer 
1 - 3840 
Input Height User input height of the input video. Failing to match this 
value with the input video’s width will result in scaling being 
performed, potentially causing performance issues. 
 
Integer 
1 - 2160 
 
Scaled Width This value is what the input imagery will be scaled down to 
prior to inference. This will also be the value relative screen 
coordinates are calculated for and rendered overlays are 
rendered atop. These values are the dimensions of any crop 
taken from input imagery 
Integer 
1 - 8000 
 
Scaled Height This value is what the input imagery will be scaled down to 
prior to inference. This will also be the value relative screen 
coordinates are calculated for and rendered overlays are 
rendered atop. These values are the dimensions of any crop 
taken from input imagery 
Integer 
1 - 8000 
In-Band KLV 
Metadata Support 
Specifies whether the input imagery has  MISB.0601.1 In -
Band KLV Metadata and to use it to provide geospatial data 
to the Athena system. This will change the structure of the 
screenspace message by including geospatial data of 
detected objects. 
 
Note: In-Band KLV Metadata is required for Athena Battle 
Tracking Service functionality 
Boolean

## Page 43

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
43 of 74 
 
Imagery Cropping Properties 
Imagery cropping can be performed prior to inferencing, this can allow for more accurate results 
from the CVIP for objects that are extremely small in the input imagery. When a crop is performed, it 
is done based upon the native resolution. The relevant properties are: 
 
Property Meaning Type and Range 
Scaled Width Specifies the width of the crop  Integer 
1 - 8000 
Scaled Height Specifies the height of the crop Integer 
1 - 8000 
Padding Specifies whether padding should 
be enabled prior to inferencing 
Integer 
0: disabled 
1: enabled 
(default = 0) 
Crop X Offset Specifies the point on the x-axis of 
the input imagery to place the top 
left corner of the cropped image  
Integer 
0 – {input_width – scaled_width} 
Crop Y Offset Specifies the point on the y-axis of 
the input imagery to place the top 
left corner of the cropped image 
Integer 
0 – {input_height – scaled_height} 
 
It is recommended for best results to set the scaled resolution to be the same or close to the resolution 
of the model (network resolution) being used to inference. For more information about models visit 
the Detection and Recognition Models section. 
 
Note: Cropping is currently not supported for Transport Stream (.TS) files as input

## Page 44

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
44 of 74 
 
System Outputs 
 
The CVIP can output inference artifacts with optional detection marker overlays to a variety of 
imagery formats and situational awareness data payloads. Allowing users to effectively analyse the 
input imagery. 
Imagery Settings 
Property Meaning Type and Range 
Unicast RTSP Video Toggle to output RTSP Video Stream 
Boolean 
[False, True] 
Default: False 
MPEG-TS Video File Toggle to output MPEG-TS Video File 
Boolean 
[False, True] 
Default: False 
JPEG Folder Output Toggle to output JPEG Images 
Boolean 
[False, True] 
Default: False 
Pylon Frames Toggle to output full resolution Pylon Frames 
Boolean 
[False, True] 
Default: False 
Imagery Overlays Settings 
This is a sub-menu within Imagery Settings. 
Property Meaning Type and Range 
Marker Box 
Marker Box Overlay 
 
Boolean 
[False, True] 
Default: False 
Marker Circle 
Marker Circle Overlay 
 
Boolean 
[False, True] 
Default: False 
Marker Text 
Marker Text Overlay 
 
Boolean 
[False, True] 
Default: False 
Market Labels 
Marker Labels Overlay 
 
Boolean 
[False, True] 
Default: False

## Page 45

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
45 of 74 
 
Marker Triangle 
Marker Triangle Overlay 
 
Boolean 
[False, True] 
Default: False 
Marker Amplifier 
Marker Amplifier Overlay 
 
Boolean 
[False, True] 
Default: False 
Show Tracking ID 
Show Tracking ID Overlay  
(Marker Text needs to be enabled) 
 
Boolean 
[False, True] 
Default: False 
Encoding Settings 
This is a sub-menu within the Imagery Settings. 
Property Meaning Type and Range 
Codec Sets the Video Codec to H.264 or H2.65 
Boolean 
[False, True] 
Default: False 
False = H.264 
True = H.265 
Video Framerate Sets the output video framerate. 
String (value will be in the form 
of a fraction) 
e.g 30/1, 40/2 
(default = 30/1) 
Output Width Sets the output video width. 
Integer 
1 – 3840 
(default = 1280) 
Output Height Sets the output video height. 
Integer  
1 – 2160  
(default = 720)

## Page 46

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
46 of 74 
 
RTSP Settings 
This is a sub-menu within Imagery Settings. 
Property Meaning Type and Range 
Stream Name Specifies the RTSP video mount string String 
RTSP Video Port Specifies the port of the RTSP stream hosted by 
the CVIP 
Integer  
1024 – 49151  
(default = 10000) 
Data Settings 
Property Meaning Type and Range 
MQTT Payloads Toggle to enable MQTT Payloads 
Boolean 
[False, True] 
Default: False 
Write JSON to File Toggle to save Payloads to filesystem 
Boolean 
[False, True] 
Default: False 
MQTT Settings 
This is a sub-menu within Data Settings. 
Property Meaning Type and Range 
Output IP Set IP address of MQTT Broker String 
Default: 0.0.0.0 
Output Port Set Port of MQTT Broker 
Integer 
>= 0  
Default: 11002 
Output Topic Set Topic to publish MQTT Payloads 
String 
e.g 
vision/athstream/tracks/scree
nspace 
Payload Settings 
This is a sub-menu within Data Settings. 
Property Meaning Type and Range 
Required Data: 
Detection Data Toggle to only output frames with detection data 
Boolean 
[False, True] 
Default: False 
Required Data: 
Inference Frames Toggle to only output frames from inference data 
Boolean 
[False, True] 
Default: True 
Required Data: 
Vehicle Telemetry 
Toggle to only output frames with vehicle 
telemetry 
Boolean 
[False, True] 
Default: False 
Optionally Include: 
Detection Crop 
Toggle to attach a base64 detection crop in the 
payload 
Boolean 
[False, True] 
Default: False 
Sensor Callsign Update the sensor callsign String 
e.g., Indigo_1 
Output Interval Update the messaging interval per frame 
Integer 
>= 0  
Default: 8

## Page 47

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
47 of 74 
 
Example Payload 
{ 
  "payload_metadata" : { 
    "fmv_rtsp_url" : "rtsp://10.0.0.10:10000/athena-video", 
    "athena_node" : "ath-example-stream", 
    "athena_session" : "d8386584-7ddc-46ca-b1e1-d892e2e46cc5", 
    "frame_count" : 528, 
    "schema_ver" : "0.11.0", 
    "buffer_timestamp" : "2023-11-15T23:59:57.475Z" 
  }, 
  "entities" : [ 
    { 
      "tracking_id" : 0, 
      "class" : "Vehicle", 
      "object_of_significance" : 0, 
      "detection_confidence" : 0.90987396240234375, 
      "tracker_confidence" : 0.97779220342636108, 
      "labels" : [ 
        { 
          "label_class" : "military vehicle", 
          "label_confidence" : 0.58599999999999997 
        } 
      ], 
      "bounding_box" : { 
        "rel_center_x" : 0.81134539842605591, 
        "rel_center_y" : 0.65484350919723511, 
        "rel_w" : 0.089583300054073334, 
        "rel_h" : 0.075868070125579834 
      } 
    } 
  ] 
}

## Page 48

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
48 of 74 
 
Detection and Recognition Models 
Sensor Configuration 
Depending on the environment of the system input to the CVIP, a change of the sensor’s configuration 
may be needed to achieve better results from the CVIP.  In the Inference Pipeline -> Detection and 
Recognition -> Sensor Configuration tab, users can alter the following:  
• Domain 
• Spectrum 
• Resolution 
• Primary Model Profile 
 
NOTE: Resolution should match the scaled width & scaled height. Input Imagery Properties 
The display of available configurations will be dependent on the sensor spectrum being used.

## Page 49

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
49 of 74 
 
Thresholds 
The thresholds for detection and recognition models can be modified to improve the results from the 
CVIP by setting a minimum confidence value that a detection or recognition must exceed  to classify 
an object to a label. The view of the thresholds will look like this: 
 
 
 
When altering an attribute’s threshold, all label thresholds will be set to this value. In the case where 
a label threshold is altered, the attribute’s threshold will change according to the minimum threshold 
value of its labels. 
If a user wants to reset a threshold back to its default threshold value, a reset button to the right of 
the slider can be clicked on and upon applying configuration the threshold will be set back to the 
default threshold. In the case where a user wants to reset all thresholds back to default, the larger 
reset button to the top right corner of the threshold view can be clicked on to enforce a reset of the 
thresholds. 
Frequencies 
The model’s detection and recognition frequencies can be adjusted . The detection frequency 
represents the frequency of running the detector. The recognition frequency represents the 
frequency of running the classifier. The detection frequency can be adjusted between 0 Hz and 30 Hz. 
The recognition frequency can be adjusted between 0 Hz and 10 Hz.

## Page 50

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
50 of 74 
 
 
Please note that mean_label_filtering within the [data_processing] section of the config file must be 
set to 0 to avoid jumps within the confidence levels of the detected and classified entities. 
Custom Models 
Custom models can be uploaded via the webpage as a zip file. This can be found within the “Inference 
pipeline”->”Detection and Recognition Models” tabs   
 
Upon uploading a custom model, the zip file will be unzipped, and the uploaded files and directories 
will be found in  the custom model file explorer which is mounted to  “/usr/share/athena-vision-
management-service/file-system/CVIP/custom-models” To use a custom model, the “ Custom Model” 
button will need to be enabled and the file path to the directory of the custom model .  
 
When clicking load on a custom model directory, the value of the model structure file path will be 
adjusted to the path of that directory.  
NOTE: A model_structure.cfg is required to exist in this directory’s path for custom model support to 
work.

## Page 51

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
51 of 74 
 
Data Processing 
Object Significance Matrix. 
The object significance matrix allows for a detect ed entity with a combination of labels to have a 
custom message attached to the outgoing payload. The selected labels must all be present on the 
detected entity for the entity to be marked as a significant object.  
NOTE: ALL selected labels must be present for the object to be marked. 
 
To configure an object of significance, choose one of the class headers on the left side of the bottom 
table. When clicking on one of these you will see the child attributes that can be detected from the 
CVIP. 
NOTE: Only one child attribute can be output by the CVIP for each detection, so if multiple children 
are selected from one parent that object significance group will never be detected.

## Page 52

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
52 of 74 
 
After selecting the labels which describe your significant object you can click the save icon on the 
right to save the object significance matrix. 
 
After clicking save the above pop-up will appear which allows you to save the matrix. After saving an 
object significance matrix a new table will appear underneath the label selection table. On the left of 
this table all of the saved matrices will be displayed, and clicking on one of them will display the 
message and labels for the matrix.

## Page 53

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
53 of 74 
 
Object Filtering 
The CVIP allows for specific object to be filtered.  To enable this feature, enable the Filter Toggle to 
On and select the desired entities to filter for. The selected entities will be the only entities displayed 
with detection overlays. Additionally, the selected objects will be the only objects published to the 
MQTT Broker, meaning that BTS’s observations will only contain the filtered objects. 
 
 
Before: 
 
After:

## Page 54

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
54 of 74 
 
Known Issues 
• On Jetson Xavier AGX and NX devices encoding issues on inference artifact imagery output 
while outputting concurrently over MQTT, RTSP and to TS file and/or JPEG 
• Occasional failure to handle end-of-stream messages from MPEG-TS video sources. This may 
require an operator restart the CVIP. 
• Possible hanging of inference pipeline following ATAK connection to RTSP server. This may 
require an operator to restart the CVIP.

## Page 55

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
55 of 74 
 
Troubleshooting 
 
To obtain more information about the cause of a problem with the CVIP we recommend viewing the 
logs of the CVIP (Head to Quick Look: Accessing Logs for more detail about logging). This section will 
go through common issues that a user may find themselves in and how to resolve the issue.  
 
Poor Performance 
When analysing the performance of inference artifacts and objects are not detected and/or 
classifications are frequently incorrect it could mean one or more of the following: 
• Low resolution of input imagery that is vastly different to the network resolution of model 
• Incorrect Input dimensions configured  (Needs to be set to the dimensions of the input 
imagery) 
• Scaled dimensions when using cropping are extremely different to the network resolution of 
the model being used 
• Sensor configuration is not configured correctly for the input imagery being used 
• Primary interval is too high (recommended to be < 60) 
• Secondary Interval is too high (recommended to be < 60) 
• Unnecessarily high threshold value on a class’s label 
 
Constant restarting state of CVIP 
This issue can arise from configuring the CVIP with invalid values or paths to files/directories that 
the system cannot find. Consult the logs to ensure that this is the case and if it has been verified that 
the file or directory exists at that location then a log will show that a particular property has an invalid 
value. Head to Quick Look: Accessing Logs being able to access the necessary logs.

## Page 56

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
56 of 74 
 
 
If the issue persists  after attempting to resolve it, then contact Athena Support via email  to 
visionsupport@athenadefence.ai with an attached latest configuration of the CVIP ( Head to Saving 
the latest configuration  for detail about saving the latest configuration ) and CVIP logs (Head to 
Downloading Logs  for detail in downloading the latest CVIP logs).  If necessary, also attach the 
inference artifacts of the instance of CVIP that had the issue (Head to Quick Look: Accessing Inference 
Artifacts for more detail). The following is an email template that can be used  in requesting for 
support: 
 
 
 
 
 
  
Subject: Request for Support with Computer Vision Inference Pipeline Issue 
 
Dear Athena AI Support Team, 
 
I am requesting assistance regarding an issue I am encountering with the Computer Vision Inference 
Pipeline. 
 
The specific issue I am facing pertains to the Computer Vision Inference Pipeline's performance and 
functionality. I have  reviewed the documentation and troubleshooting steps, but unfortunately, I 
have not been able to identify a solution to the problem. 
 
[Explain the issue that the user is facing] 
 
[Explain what files have been attached] 
 
 
Best regards, 
[Your Name] 
[Your Contact Information]

## Page 57

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
57 of 74 
 
Object Localisation Service (OLS) 
Expected Values 
Geolocalisation Variables 
[Description of Geolocalisation Variables section] 
Property Meaning Type and 
Range 
Geolocalisation of 
Tracked Entities 
A detection from the CVIP can either be Inferenced (High 
Precision) or Tracked (Low Precision). This property limits 
the geolocalisation of only the inferenced detections to 
maximise program throughput while keep accuracy high 
Boolean 
Smooth Camera 
Position 
Whether to smooth the position of the sensor to better 
geolocalise when the source sensor does not have a stable 
position 
Boolean 
Moving Average 
Smoothing 
Whether to use a moving average for the smoothing 
method (FFT Smoothing takes precedence) 
Boolean 
FFT Smoothing Whether to use FFT Smoothing for the position of the 
source sensor 
Boolean 
Frame Center 
Correction 
Whether to apply a calculated correction to the center of 
the frame 
Boolean 
Camera Frames to 
Smooth 
The amount of camera frames to smooth Integer 
4-10 
Detection Positions 
to Smooth 
The amount of detection positions to smooth Integer 
4-10 
Duration of Frames 
to Smooth 
The window of time to smooth a detections position over Float 
0.5-2 
Duration to Store 
Frames 
The window for how much detection positions to store  Integer 
1-10 
Video Frames Per 
Second 
The Video Frames Per Second to allow for a correct 
duration of frames to store 
Integer 
1-60

## Page 58

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
58 of 74 
 
Geolocalisation Confidence 
[Description of Geolocalisation Confidence section] 
Property Meaning Type and 
Range 
Distance from 
Sensor 
Whether to use the distance of a detection from the sensor 
in the calculation of the geolocalisation confidence 
Boolean 
Distance from Frame 
Center 
Whether to use the distance of a detection from the frame 
center in the calculation of the geolocalisation confidence 
Boolean 
Camera Pose Whether to use the sensor’s camera’s pose in  the 
calculation of the geolocalisation confidence 
Boolean 
Maximum Distance 
Between Sensor and 
Detection 
Maximum distance to calculate the position of a detection 
from a sensor 
Float 
1-15 (km)

## Page 59

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
59 of 74 
 
Battle Tracking Service (BTS) 
Battle Tracking Service Quick Looks 
Quick Look: CVIP Configuration for BTS 
To enable the battle tracking service there are a few configuration elements which are REQUIRED. 
To ensure that the data needed for battle tracking is being provided to the BTS. 
The first requirement is that the data that is being processed by the CVIP does contain KLV metadata. 
For the CVIP to pass the KLV metadata through the “In -Band KLV Metadata Support” in “Inference 
Pipeline” -> “Inputs”. 
To ensure that the BTS receives any of the data in “Inference Pipeline” -> “Outputs” -> “MQTT 
Payloads” must be enabled. It is also suggested that in “Inference Pipeline” -> “Outputs” -> “Payload” 
that “Inference Frames” and “Vehicle Telemetry” are enabled as this will reduce unnecessary data 
being sent. 
Once these are enabled the BTS will be able to process and geolocalise the tracks from the CVIP.

## Page 60

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
60 of 74 
 
Quick Look: Connecting to a TAK server. 
To connect to a TAK server, open the Battle Tracking Tab and Start the BTS (For more information, 
see “Quick Look: Controlling A Service’s State” earlier in this guide). 
Once started, the service can be configured.  
Open the “TAK Server Connection” Tab.  
 
The first selection element allows for the selection of which type of TAK server you are connecting 
to. 
Next, the BTS requires the IP and port of the TAK server, these are provided via the “TAK Server IP” 
and “TAK Server Port” text fields. 
The “Callsign” field provides a callsign to identify the instance of the BTS.  
 
NOTE: Please ensure that each instance of the BTS has a unique callsign, if using multiple Athena 
Vision systems.

## Page 61

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
61 of 74 
 
To connect to a secure server via TLS/SSL, click the TAK Server SSL Upload button to start a sequence 
of prompts to upload the required certificates. For more information on the required certificates see 
the below section “Required Certificates” 
 
 
NOTE: It is highly recommended to use a secure port when connecting to a TAK Server to ensure BTS 
can operate at full functionality. 
 
After these certificates have been uploaded ensure that the “TLS/SSL Connection” toggle is set to 
“ON”. To confirm these changes, click the “Apply Changes” button and the BTS will use these settings 
and will attempt to connect to the TAK Server

## Page 62

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
62 of 74 
 
Quick Look: Interacting with BTS markings in ATAK. 
Both observation and individual tracks placed by the BTS have extra information which can be 
accessed within the details of the ATAK element.  To find this information tap on one of the BTS’ 
markings and within the radial menu select the “details ” option. This will open a side panel which 
contains the extra information.  
 
For Observations this contains a series of reports based on when individual tracks were spotted that 
make up the observation. 
 
For individual tracks these contain a report of what has been detected of the entity.

## Page 63

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
63 of 74 
 
Quick Look: Using the BTS Chat Service. 
By default, the BTS will output only observations. If you want the images and a heatmap for the 
observation they can be requested via the BTS Chat Service.  
There are two fast ways to send the observation to the chat service. 
Send through the radial menu. 
Interact with an observation by tapping on the observation. When the radial menu appears, 
tap and hold on the “details” icon and then on the second radial menu select the “send” option.  
 
Send through the observation details. 
From within the details section of the observation ( For more information on accessing this 
view, see Quick Look: Interacting with BTS markings in ATAK)  select the send option in the 
bottom left of the observation’s details.

## Page 64

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
64 of 74 
 
Once within the sending menu, select the instance of the BTS. The name of the BTS will be “Athena -
BTS-[Callsign]” where callsign is what was entered into the BTS configuration. Select this user in the 
chat and send the observation. 
 
The BTS should send an update at the top of the observation’s “Remarks” section in the details.  
 
Shortly after , attachments should be sent to all users for the observation which was requested.  
Depending on how many images there are, this may take some time.

## Page 65

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
65 of 74 
 
  
To view all the attachments, press the “attachments” button in the bottom middle of the observation’s 
details section. This will open a grid view of all the attachments. 
  
The requested heatmap will be labelled KMZ and will have a different icon to the images. To view the 
heatmap, tap the heatmap file and select “Image Overlay File” and ATAK will display the heatmap  
 
Quick Look: Clearing BTS tracks from ATAK. 
If there are too many tracks or observations with large amounts of attachments ATAK’s performance 
can start to degrade. If this is the case, then the “Clear Tracks from ATAK” button will process a 
deletion message for every observation and individual track that BTS has within its database.

## Page 66

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
66 of 74 
 
As there can be a large volume of messages being sent through this can take some time to process. 
Sometimes after this clearing has occurred some ATAK clients can have tracks that were not deleted, 
if this is the case then simply re -use the button as many times as needed to ensure that all ATAK 
instances have had the BTS tracks removed.

## Page 67

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
67 of 74 
 
Battle Tracking Service User Guide 
TAK server connections. 
When using the BTS it is highly recommended to use a TLS/SSL secure connection. This is because 
there are features of the BTS which are unable to be used on a non-TLS/SSL connection. 
The primary feature which cannot be used when using a non-secure port is the BTS chat service. The 
chat service allows for the BTS to operate within network bandwidth limited environments and still 
be able to deliver all its features.  
Required Certificates  
Here is a list of TLS/SSL files which are required and some example files names.  This includes 
example certificate names based on default user naming and default conventions for both TAK -
Product-Center/Server and Free TAK Server. 
File Type Example File Names 
Certificate Authority ca.pem, ca.crt 
User Key Takserver-user-1.key, 
user[Hash String].key 
User Certificate Takserver-user-1.pem, 
Takserver-user-1.crt, 
user[Hash String].pem, 
user[Hash String].crt 
 
BTS Chat Service. 
The BTS Chat Service allows for interactions between the user on ATAK and the BTS. When viewing 
an observation in ATAK it can be sent to the BTS, the BTS will then generate a heatmap for the 
observation and will send this along with all stored images that belong to the observation. This means 
that the BTS can operate with its standard output ready for low bandwidth environments and will 
only have to send large amounts of data upon the user’s request. 
The chat service also has a configuration option , that when enabled , will mean that when an 
observation is requested, it will also send the individual tracks that are not stale to ATAK.

## Page 68

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
68 of 74 
 
BTS ATAK Symbology. 
The BTS uses the CoT typing schema which means that the individual units can be output with 2525C 
symbology. The default affiliation of all detected units within the 2525C schema is for them to be 
marked as unknown, these default affiliations can be changed if it is known which affiliation these 
units are.  
 
BTS also allows for the output of ATAK symbology using the default iconography provided by ATAK. 
This output allows for someone who is inexperienced with 2525C symbology to be able to 
understand all of the individual tracks that the BTS creates and sends to all users.

## Page 69

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
69 of 74 
 
The default colours of BTS’s observation can be changed in the AMS. These configuration options can 
be reached via “Battle Tracking” -> “ATAK Configuration” -> “Visualisation” -> “Colors”.

## Page 70

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
70 of 74 
 
Any individual tracks that are output from BTS will have several fields to present the detected 
information for the given track.  
 
The first field that can appear is if the track is an object of significance (For more information see, 
Quick Look: Object significance) the custom message/s will be displayed under “Messages”. Next will 
be the “Characteristics” which contains all the secondary classifications that the CVIP detected. Next 
is the “First Spotted” and “Last Spotted” which contains the time and positions and timings of when 
the track was first and last spotted by the CVIP. The last field is the “Spotted By” field, this shows the 
callsign of the sensor that spotted the track.

## Page 71

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
71 of 74 
 
Decision Support Service (DSS) 
Decision Support Service Quick Looks

## Page 72

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
72 of 74 
 
Troubleshooting 
To obtain more information about the cause of a problem with the AMS we recommend viewing the 
logs of the AMS (Head to Quick Look: Accessing Logs for more detail about logging). This section will 
go through common issues that a user may find themselves in and how to resolve the issue. 
 
Constant Establishing Connection Screen 
Before attempting any further troubleshooting steps to resolve this issue, attempt to refresh the 
page. 
If the user experiences an establishing connection screen for over a minute this may be because: 
• Device is not reachable i.e., turned off, disconnected from network 
o To verify that the device is still reachable over the network run the following 
command on a command line: 
 
$ ping {IP_OF_SYSTEM_HOSTING_AMS} 
 
If the device can be reached a similar output to the following should be seen: 
 
 
If a similar view to the above is not seen it may mean that the device has been turned 
off or disconnected from the network.

## Page 73

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
73 of 74 
 
• The AMS has exited unexpectedly 
o To verify that the AMS is running, execute: 
$ docker ps -a 
A docker container named “athena -vision-manager” should be present and in a 
running state. 
o To verify that the server hosting the AMS is still up run the following command on a 
command line: 
$ ps aux | grep 'node src/app.js' 
 
If the server is still up the following should be the output: 
 
 
o To verify that the MQTT broker is still up run the following command on a command 
line: 
$ ps aux | grep 'mosquitto -c config/mosquito.conf' 
 
If the MQTT broker is still up the following should be the output: 
 
 
In the case where the server or MQTT broker is not up, run the following command 
to boot the server and MQTT broker back up. 
$ sudo systemctl restart athenavision.service 
 
• The systemd service managing the AMS has stopped unexpectedly 
o To verify the systemd service of AMS is still active run the following command on a 
command line: 
$ sudo systemctl status athenavision.service 
 
If the systemd service is still up the following should be the output: 
 
 
In the case where the systemd service has exited, run the following command to 
activate the AMS’s systemd service: 
$ sudo systemctl start athenavision.service

## Page 74

VERSION 
1.1.0 
CLASSIFICATION 
COMMERCIALLY SENSITIVE 
DOC 
User Guide – Athena Management Service 
PAGE 
74 of 74 
 
Error When Downloading a File 
This error can occur when attempting to download a file that has been deleted from the system and 
the file explorer has not yet updated to reflect the file being deleted (File explorers update every 5 
seconds).  
 
Currently though, users are not able to download the ‘.configuration.tmp’ file. Instead, users will need 
to save the latest configuration and then download the newly saved file.
