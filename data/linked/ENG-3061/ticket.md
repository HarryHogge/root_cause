# ENG-3061: VXE 454 Center Wing Power Connector solder melted

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-04-19
- **Updated:** 2025-06-02
- **Resolved:** 2025-05-05
- **Reporter:** Dustin Gamble
- **Assignee:** Cameron Chapman
- **Creator:** Dustin Gamble
- **Links:** relates to RMA-115 (VXE-454 230419); relates to VA-93 (Record typical, max, and max tested lift current and voltage profiles. Save test data to confluence. Establish and implement limits and abort if exceeding.); relates to ENG-3084 (VXE 401 Failed VTOL Landing from 10ft (Crash)); relates to ENG-3160 (Determine overcurrent abort limit, then implement auto-abort when present. Update manuals accordingly. ); relates to VA-318 (FTP to 454 VTOL AP shows corruption); relates to ENG-3179 (Add data visuals to sharepoint per Cameron's comment); is caused by VA-791 (VXE 454 Center Wing Power Connector solder melted identify C/CA); relates to VXEP-385 (New Connectors and Contacts, Overall Requirements Review); causes SP-206 (Improve Power Connector, Contacts, and Signal Connectors)

## Description

files for investigation: https://jenaero.sharepoint.com/sites/EngineeringTeam/Shared%20Documents/Forms/AllItems.aspx?csf=1&web=1&e=6x2Zf4&cid=aebb2846%2D2c37%2D4640%2D8ae5%2D75bb420a62b8&FolderCTID=0x01200083B249CA3EB99742ACC0F1840D0086D5&id=%2Fsites%2FEngineeringTeam%2FShared%20Documents%2FGeneral%2FVehicle%20Incidents%2FVIT2%2D281&viewid=38f95ce4%2Df481%2D4883%2Daf41%2D672a33b5b619
Marcus with MCWL completed a normal flight. Post landing he could smell burning. On inspection he found the VTOL center wing black connector had melted solder on the contact. 
@Jeff Hartsell is providing a shipper to Marcus to return the wing case.

@Former user

## Comments (38)

### Jeff Hartsell, 2023-04-19

FedEx tracking for 454 Wing Case return.  791351986460
@Sean Odell @Cameron Chapman @Dustin Gamble

### Cameron Chapman, 2023-04-19

@Dustin Gamble do you have data for this vehicle? We should review to see if any of the voltage/current/power levels were abnormal. If not, it would indicate a part defect.

### Dustin Gamble, 2023-04-19

When I spoke to Marcus I was thinking the same thing. He said he would post it soon to vxehelp and we’ll get it on this ticket.

### Cameron Chapman, 2023-04-19

Assigning to John’s group once data is available to review. Check for abnormal voltages, currents, throttle duration, etc.

### John Clark, 2023-04-20

@Cameron Chapman @Dustin Gamble flight logs required for required analysis

### Sean Odell, 2023-05-08

@John Clark @Cameron Chapman  The case has arrived. I will be doing my intake on it this morning. I will than move the case to Engineering. Will update Jira once it is delivered to engineering for your team to start the evaluation.

### Cameron Chapman, 2023-05-09

Assigning to @Sean Odell until intake is complete. Please assign to @Laszlo Juhasz when delivered.

### Sean Odell, 2023-05-09

@Laszlo Juhasz The Aircraft has been delivered for your evaluation. Only initial damage seen is the solder melted in the plug (photos above).  Carson said he has scene this exact thing a couple times when the power cable is not fully engaged. If that helps at all. Otherwise, thank you for your evaluation.

### Laszlo Juhasz, 2023-05-09

@Sean Odell Thank you for letting me know. Yes, indeed we’re seeing this problem with multiple aircrafts. I’m in the process of setting up a high current test platform to duplicate the problem on a bench and find a workaround of the issue. Looks like when the lift-motors are drawing high current (>200A) the soldering melts in the power connector and that leads to loss of power. Earlier I was assigned to evaluate to use higher temperature solder, but the priority was not that high. Now, I’m on it and with the test platform I’m going to verify if the use of higher temperature solder will fix this problem.

### Sean Odell, 2023-05-09

@Laszlo Juhasz Appreciate the hard work and would love to check out the test platform when your ready to try it out.

### Cameron Chapman, 2023-05-10

@Laszlo Juhasz , after initial connector inspection, we should first pull the logs from these vehicles, then review lift current for this flight.

### Laszlo Juhasz, 2023-05-11

[embedded: IMG_20230511_113736988.jpg]
Yes, this image is to show the inrush limiting resistor meltdown and the heat can exceed the melting point of the solder as well.
I’m working on pulling the flight data to see the level of current at the last flight.

### Cody Smisek, 2023-05-17

@Cameron Chapman @Sean Odell @Laszlo Juhasz Have the logs been downloaded from this system yet?

### Laszlo Juhasz, 2023-05-18

@Cody Smisek Good Morning, Yes, the data was downloaded and attached.
[embedded: VTOL_VXE454.zip]

### Cody Smisek, 2023-05-18

@Laszlo Juhasz reading between the lines just a little here. Looks like all the other data was corrupt?

### Laszlo Juhasz, 2023-05-18

Yes, basically we’ve had difficulties to recover the data using the standard procedure. This is what we were getting after several trials.

### Cameron Chapman, 2023-05-18

Logs here https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Root%20Cause%20Task%20Force/Flight%20Data%20Reviews/VXE%20454%20Center%20Wing%20Power%20Connector%20solder%20melted?csf=1&web=1&e=OLNzsJ

### Cody Smisek, 2023-05-18

[embedded: image-20230518-172442.png]

### Cameron Chapman, 2023-05-18

@Cody Smisek thanks for plotting this. I recommend creating a word doc here https://jenaero.sharepoint.com/:f:/r/sites/EngineeringTeam/Shared%20Documents/Root%20Cause%20Task%20Force/Flight%20Data%20Reviews?csf=1&web=1&e=y1HaZc,  adding the link to description, then adding plots like this with context and evaluation notes to it. 
The plot below does not look very abnormal. We can verify by adding some comparison plots of other flights  to the word doc. Compare voltage, current, and duration. 
@Laszlo Juhasz can you please update the fields above with major findings and next steps recommended. See https://jenaero.atlassian.net/wiki/spaces/EF/pages/23363854/VIT2+Project-Incident+Troubleshooting+and+Resolution+Tracking.

### Sean Odell, 2023-06-09

@Laszlo Juhasz @Cameron Chapman Just getting a status update for my update to Lockheed. Any ETA on this aircraft or next steps to tell the customer?

### Cameron Chapman, 2023-06-09

Recommended plan:
- Ask John Clark if data can be uncorrupted. Review other data logs to see if they indicate overcurrent conditions (I think the XCOM log may log some VTOL power details). 
- xcl log columns vtVbatt vtIbatt. (Need to FTP from XCOM) . IP address in in the GCS/tools/IP calculator.
- Open center wing. Inspect CSB and boom power connectors for damage.

### Sean Odell, 2023-07-06

@Cameron Chapman @Laszlo Juhasz @John Clark VXE454 Fuse transit case arrived yesterday.  I was told to request the Fuse to continue investigation. Who should I notify that it has arrived? I will be bringing it over to engineering after Chris Jones and I do an initial intake of the parts.

### Laszlo Juhasz, 2023-07-06

@Sean Odell @Cameron Chapman @John Clark  Thanks Sean, Please let me know when the 454 is available for investigation.
Thanks.

### Laszlo Juhasz, 2023-07-07

@Sean Odell @John Clark @Cameron Chapman  The data from the fuselage was fully recovered and attached for further analysis (VXE454LogBook.zip).

### Cameron Chapman, 2023-07-07

@Laszlo Juhasz can you please work with Hayden, Connor, or Liam to plot this data in the plotter tool, then review VTOL current for the most recent flights?

### Cody Smisek, 2023-07-10

@Hayden Jeanor Deleted my last comment and reposting. If the guidance is to use the unfiltered data for these lift system issues, is that what we’ve been doing for the other similar issues? I can’t recall why or by who, but I was pointed in the direction of using the filtered data for lift system voltage/currents. Which obviously obscures some of the high points.

### Hayden Jeanor, 2023-07-10

@Cody Smisek youre right, Cody. Deleting my last comment to avoid confusion. I thought you were performing your own filtering on the dataset that was already filtered. I mixed up my variables in the analysis

### Hayden Jeanor, 2023-07-10

@Cody Smisek Laszlo confirmed that the VTOL log files are corrupted on the lift AP

### John Clark, 2023-07-10

@Laszlo Juhasz @Hayden Jeanor , I compiled the data I shared with the two of you this morning and based on our conversation created a short report. The droop on the VTOL battery voltage suggests a lot of energy went somewhere. I didnt see a increase in current and concluded that energy melted the solder.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent.

### Sean Odell, 2023-09-05

@Laszlo Juhasz What is the status on VXE-454 since you now have both Fuse and Wing case in the building?  Thank you for your hard work!

### Cameron Chapman, 2023-11-08

This issue has been sitting for a while. We will investigate soon with recent connector findings and troubleshooting methods.

### Adrian Garcia, 2023-11-08

Created folder to put files for investigation on: https://jenaero.sharepoint.com/sites/EngineeringTeam/Shared%20Documents/Forms/AllItems.aspx?csf=1&web=1&e=6x2Zf4&cid=aebb2846%2D2c37%2D4640%2D8ae5%2D75bb420a62b8&FolderCTID=0x01200083B249CA3EB99742ACC0F1840D0086D5&id=%2Fsites%2FEngineeringTeam%2FShared%20Documents%2FGeneral%2FVehicle%20Incidents%2FVIT2%2D281&viewid=38f95ce4%2Df481%2D4883%2Daf41%2D672a33b5b619

### Laszlo Juhasz, 2023-11-08

@Cameron Chapman @Sean Odell Due to the solder blub the AS-150 will not fully mate with the female connector. That is probably an indication of not been fully connected during the last flight. Anyway, the CSB harness needs to be replaced. 
[embedded: MicrosoftTeams-image (1).png]

### Cameron Chapman, 2023-11-08

@Laszlo Juhasz and @Adrian Garcia the solder blob is likely a symptom of a previous overcurrent, rather than the cause of it. We should try to identify in the data logs or by contact inspection what caused the solder to melt. It may be partially due to the connector not being fully mated issues. 
In the logs, we should look for low battery voltages, high currents, compare power, battery connected, etc.

### Sean Odell, 2023-11-15

@Cameron Chapman After reading some of the findings on this aircraft, it seems to be connected to the AS150 type of investigation that has been going on several months. Is your team at a point where I can have the physical aircraft to repair it?  Your team can have any parts you might need and I can back fill them.
@Pat Wells FYI

### Cameron Chapman, 2023-11-16

@Sean Odell ok to replace the dcsa and keep it red tagged in engineering. We should also review the current from previous flights before reusing the ESCs, but the rest of the aircraft is OK to return for rma actions.

### Cameron Chapman, 2023-11-16

@Adrian Garcia please plot data listed below and link ppt in description.

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IMG_6997.jpeg | image | 2137 | 2023-04-19 | listed only |
| IMG_6999 (a1bd15fa-c401-47e5-8cac-0ef7361071e3).jpeg | image | 1043 | 2023-04-19 | listed only |
| IMG_6999.jpeg | image | 1043 | 2023-04-19 | listed only |
| IMG_20230511_113736988.jpg | image | 2547 | 2023-05-11 | listed only |
| VTOL_VXE454.zip | archive | 2454 | 2023-05-18 | listed only |
| image-20230518-172442.png | image | 36 | 2023-05-18 | listed only |
| [Vehicle 454 incident report.pptx](attachments/15392_Vehicle%20454%20incident%20report.pptx.md) | pptx | 5247 | 2023-07-10 | converted |
| MicrosoftTeams-image (1).png | image | 990 | 2023-11-08 | listed only |
