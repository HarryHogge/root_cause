# VXEP-1959: VXE 857 experienced a loss of link and did not return.

- **Issue type:** Incident (8D)
- **Status:** D2 - Gathering Information
- **Priority:** Highest
- **Created:** 2026-07-14
- **Updated:** 2026-10-08
- **Reporter:** Stephan Johnson
- **Assignee:** Ted Trowbridge
- **Creator:** Stephan Johnson
- **Labels:** Crash, External, Investigating, RCCA, Weekly-incident-tracker
- **Customer:** Air_PMO
- **Vehicle Tail Number:** VXE 857
- **Incident Type:** Aircraft Loss
- **Severity:** 1 - Flight Critical
- **Executive Summary:** AARs received were incomplete. requested data from AIR PMO/end user awaiting data; probable cause Software or Hardware.

## Description

Who:
V1/1
Sgt Vito A. Calli
What:
VXE30 experienced a loss of link and did not return.
System 029
AV 857
SW 6.6.1
When:
12 July 2026
Launch 0805
Loss of Link 0835
Where:
MCAGCC Twentynine Palms, Ca.
Training Area DELTA
MGRS 11S NU 90529 02893
Heading 179.6 Degrees
Altitude 5439 ft MSL
Winds 10-15 knts from 10 degrees
Why:
While observing the video, the AV momentarily lost link a few times during flight. In one instance, it looks to have been receiving errors and even lost GPS.
Observation near end of flight video:
0832 Loss of Link
0833 Link established
-No GPS error / 31M AV 66025 99999
-Altitude 4832
0833 GPS and Alt. stabilize
0834 GPS drops and returns
0835 Loss of link
Shortly after, the GCS program crashed.
Customer Comments:
V1/1 will use their available PUMA to help search for the VXE AV. I gave them recommendations to start at the last known grid and search south spreading out (based on the last known heading and winds). I also explained and provided instructions for submitting a MISHAP report on the RMI-SIR site and submitting a report on the AIR PMO Issues/Features site. Jasmine noted that while looking through the laptop settings, she found that LandOnError=0 so that may not be the issue. I informed the Sgt that pulling the FDR, if possible, and sending it to AIR PMO will help us find out what happened.

## Vehicle Configuration

VXE30
SUAV 6.6.1

## Comments (7)

### Drew Hildreth, 2026-08-05

@Alexander Alan Arnold @Scott Lovett There is data in here. Has anybody looked at it? If so is it complete and usable? I assume they recovered the aircraft then if there is data.

### Scott Lovett, 2026-08-05

@Drew Hildreth I’ll take a look

### Drew Hildreth, 2026-08-05

@Scott Lovett Alex just told me they are incomplete and that he requested the operators get the FTP

### Alexander Alan Arnold, 2026-08-10

@Eric Brewer Can you see if the data thats attached is useable ?

### Eric Brewer, 2026-08-10

@Alexander Alan Arnold @Drew Hildreth confirm there is no vtol or xcomm logs in the AAR’s (seems expected based upon the description that the vehicle was lost). Do you know if they were able to recover it? I can’t tell a whole lot from the gcs logs other than it did seem to be losing connection with the ground (which could be caused by a lot of things)

### Alexander Alan Arnold, 2026-08-12

@Ted Trowbridge 889 and 857 were reported by same end user I was wondering if they used the same GCS to operate, 889 you discovered the land on error change. can you confirm if this had the same issue?

### Drew Hildreth, 2026-09-04

@Alexander Alan Arnold @Ted Trowbridge has there been any update on this?

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V857_260711_133300_pack_wouldnotRTBforcedlandimmediately.zip | archive | 590 | 2026-07-27 | listed only |
| T95_V857_260711_221246_pack_manipulatedwaypointstoland.zip | archive | 572 | 2026-07-27 | listed only |
