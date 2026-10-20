# VXEP-1149: VXE 529 SD Card failure while following power cycling Advisory notice

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-03-19
- **Updated:** 2026-03-02
- **Resolved:** 2025-05-19
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** SD_Card, TIQUILA, Weekly-incident-tracker
- **Links:** relates to FS2-2854 (Jason's Open Investigations)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 529
- **Vehicle Configuration:** Standard battery
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

TIQ customer asset does not have updated Industrial SD Card.
Customer states that they have been complying with Advisory Notice  AN 24-001 Flash Memory Maintenance. 
Customer is experiencing connectivity issues with aircraft that closely align with previously known SD Card issues.
Suggest downloading data files to confirm that customer has been power cycling the aircraft.
Customer requests explanation as to why the SD Card failed even though they were complying with the Advisory Notice. 

SharePoint Folder VXEP-1149 VXE 529 SD Card Issue

## Issue Status

Removed avionics, tested on iron bird, bootloader working, nothing else after.
Opened avionics, removed SD Card, powered avionics, able to access Xcomm. Reconnected SD card while powered, unable to access logs. Cycled power, able to access logs, screenshot of logs and some logs attached. 
Last properly dated log file is from 09/03/2024

## Comments (14)

### Drew Hildreth, 2025-03-20

@Jason Scherer - both AC cases delivered to Engineering area.

@Rodney Linch

### Cody Smisek, 2025-03-20

@Drew Hildreth Do we have more information than this to go off of? 'Connectivity issues' is a very broad description of an issue.

### Pat Wells, 2025-03-20

@Cody Smisek it’s the usual symptom for a failed SD Card in the avionics.  Unable to connect to the aircraft.

### Cody Smisek, 2025-03-20

@Pat Wells @Drew Hildreth Last log with an actual date shows 09/03/2024.

### Pat Wells, 2025-03-20

@Cody Smisek that’s interesting and certainly doesn’t align with their claim that they have been power cycling every 30 days.

### Drew Hildreth, 2025-03-20

@Cody Smisek just so I am understanding everything correctly, the 2028/01/01 is only there because it never acquired GPS? Otherwise, it would have populated with the correct date?

### Cody Smisek, 2025-03-20

@Drew Hildreth correct. And at least 1 or 2 of those are from booting up here in SLO (after removing/inserting SD Card). Unsure if log files would restart in the ‘not connected’ state, so it’s possible more of those are from booting in SLO.

### Drew Hildreth, 2025-03-20

@Cody Smisek Thank you. That was my other thought that since the order of the files wasn’t interrupted that it was possibly your files.

### David Grosher, 2025-03-21

@Cody Smisek @Pat Wells There are a number of files with no date information between the 9/30/24 and Yesterday in SLO. The fact that there is no date on those files likely means that the coin battery for the RTC has died. And the other files could indicate that the system was powered but didn’t get a GPS fix, since it was probably inside. I’m not sure that we can conclude that they did not power the system unless we can go back through each of those csv files and see if they eventually got a GPS fix.

### Cody Smisek, 2025-03-21

@David Grosher Thanks for the information. The only information I provided to Pat and Andrew was that the last dated file was September. I did not conclude anything beyond the fact that I have started the system a few times in SLO so some could be related to my troubleshooting. 
I can go back through each file and look for GPS fix if desired.

### Cody Smisek, 2025-03-21

VTOL Indicates the following dates: 3/21/2025 Edge, 11/19/2024, remainder 2023. There are two files between 01/2024 and 11/2024 with unknown dates (haven’t looked in file). Screenshot attached. 
I’ll be reviewing Xcomm logs per Dave’s suggestion for dates/times and will provide update this morning. 
@David Grosher @Pat Wells FYI

### Cody Smisek, 2025-03-21

Checked the following, during my startups I was using power supply with power set to 28-29V. So I don’t think any of these are mine. Also there’s a new file that was created outside of screenshot with today’s date. 
File 26 no date ~80sec 27v
File 27 no date ~400sec 27v
File 28 no date ~400sec 26.5v
File 29 no date ~500sec 26.9v
File 30 no date ~500sec 26.9v
File 31 no date ~400sec 27.2v
File 32 no date ~600sec 27.2v
File 33 no date ~270sec 27.2v

### Pat Wells, 2025-04-07

@David Grosher the customer seemed satisfied with the answer that the SD Card is corrupted.  I suggest closing this out without any further action.

### David Grosher, 2025-05-19

Customer has closed the SCAR and will update to the Industrial uSD cards per the released containment.

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| APX00034.APX | other | 2 | 2025-03-20 | listed only |
| [FDR00034.csv](attachments/27461_FDR00034.csv.md) | csv | 44 | 2025-03-20 | converted |
| Screenshot 2025-03-20 125225.png | image | 349 | 2025-03-20 | listed only |
| [XC000101.txt](attachments/27459_XC000101.txt.md) | text | 29 | 2025-03-20 | converted |
| [XCEVLOG (27).txt](attachments/27460_XCEVLOG%20(27).txt.md) | text | 167 | 2025-03-20 | converted |
| [XCL00034.csv](attachments/27463_XCL00034.csv.md) | csv | 528 | 2025-03-20 | converted |
| vtol-529.PNG | image | 213 | 2025-03-21 | listed only |
