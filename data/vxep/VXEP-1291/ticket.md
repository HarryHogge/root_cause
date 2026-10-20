# VXEP-1291: VXE 592 Crash

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-05-30
- **Updated:** 2026-03-02
- **Resolved:** 2025-12-01
- **Reporter:** Michael Mohr
- **Assignee:** David Grosher
- **Creator:** Michael Mohr
- **Labels:** MOLSON, Weekly-incident-tracker
- **Links:** relates to RMA-704 (VXE-592 RMA 250602-1); relates to RMA-705 (E140ZG2 S/N 6170 RMA # 250602-2); relates to VXEP-1072 (Center wing 592 unable to connect); relates to VXEP-453 (VXE 592 crash on landing)
- **Customer:** MOLSON
- **Vehicle Tail Number:** VXE-592
- **Plan:** Implement corrective actions
- **Root Cause:** See PPT linked above.  Best guess is a software glitch corrupting the AHRS, but cannot rule out sensor failure.
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

Statement from instructors on site:
Aircraft was in and orbit at 700 ft AGL viewing ground targets with the Octopus payload. All of the sudden they realized that the aircraft was on the ground and had crashed. 
From Edge FLOPS: During orbit video appeared to go upside down, with a hard turn to the right and then lost comms. 
Investigation PPT: Vehicle592Crash
File Location: Flight Safety - VXE592_CrashInFWFlight - All Documents
NOTE: no evidence it’s related, but this aircraft was involved in an incident last year (linked below).

## Corrective Action

- CA: Implement clipping in software to avoid single erroneous measurement corrupting AHRS filter​ - see edgeautonomy / fixed-wing-ap Pull Request #103: fixes to AHRSupdate — Bitbucket and edgeautonomy / autopilot_202 Pull Request #271: Bugfix/FS2-3418 limit sensor capture for mag data — Bitbucket
- CA: Implement buffering to avoid loss of xcomm logs in similar event.​ [FS2-3487] Implement buffering to prevent loss of xcomm log data on crash. - Jira

## Issue Status

6/27/2025 - Brewer - At this point our best guess is some sort of software glitch that corrupted the AHRS (pitch/roll estimates of the vehicle were bad). We have implemented a software patch that will go into future releases.

6/20/2025 - smisek - tested elevator booster board using electronics checkout, checked okay. checked booster plus elevator servo using electronics iron bird with RC, movements commensurate with RC control. 
6/20/2025 - brewer suspects possible corrupt mag data from vtol to fwap. investigating

## Comments (39)

### David Grosher, 2025-05-30

@Michael Mohr Please let me know when you get data. @Eric Brewer @Jason Scherer FYSA.

### Michael Mohr, 2025-05-30

@David Grosher They were able to pull the XComm files but when they went to get the Vtol logs, there were no files in there. Center wing panel was ripped off as well as some of the internal center wing wiring.

### David Grosher, 2025-05-30

@Michael Mohr Ok, please ensure that they recover the SD card on the VTOL board. We will be able to recover any data on it once it is returned. In the meantime, please post the XCOMM data once you have received that.

### Michael Mohr, 2025-05-30

@David Grosher Files uploaded

### David Grosher, 2025-05-30

@Michael Mohr is the video available?

### Pat Wells, 2025-06-01

@David Grosher I’ve requested the video from the flight ops team. Will post here when and if it’s available. Additionally, any reason to believe that the GCS utilized during this flight should be grounded or is it safe for flight?
@Michael Mohr  FYSA

### Jackson Riley Curvin, 2025-06-02

[embedded: image-20250602-132138.png]

### Pat Wells, 2025-06-02

@David Grosher the video was not recorded.

### Jackson Riley Curvin, 2025-06-02

[embedded: image-20250602-135545.png]

### Jackson Riley Curvin, 2025-06-02

[embedded: image-20250602-135646.png]

### Jackson Riley Curvin, 2025-06-02

[embedded: image-20250602-135732.png]

### Jackson Riley Curvin, 2025-06-02

[embedded: image-20250602-135852.png]

### Cody Smisek, 2025-06-02

I see a message in debug about fixed wing ignoring vtol mag. Unsure if it’s related at all but it reminded me that others may not know this. The E140 has a option that can be enabled ‘flipping mode’. This will send the in use sensor to the bottom (helps with obstructions and better view). So switching between EO to IR, the gimbal will do 180deg in pan and 180deg in tilt rather rapidly (<1sec). Flight ops states this was enabled.

### Cody Smisek, 2025-06-02

@Jackson Riley Curvin I would recommend plotting against CPU time or GPS time. You will get skewed results by plotting against cell row count as we increase our logging rate for certain phases of flight (such as takeoff and landing) and excel doesn’t know how to interpret that.

### Jackson Riley Curvin, 2025-06-03

@Cody Smisek Thanks, for this particular incident which one do you think would be best CPU time or GPS?

### Cody Smisek, 2025-06-04

[embedded: image-20250604-165709.png]

### Cody Smisek, 2025-06-05

@Jackson Riley Curvin Is someone able to provide a map of debris location? It looks like the fuselage is a distance away from the wing components from the pictures, was that where it was when found?

### Jackson Riley Curvin, 2025-06-05

@Cody Smisek I'll ask them we never got photos as to where the center wing was when it crashed.

### Cody Smisek, 2025-06-05

@Jackson Riley Curvin and was the HLB still in the fuse? cant tell from picture

### Jackson Riley Curvin, 2025-06-05

@Cody Smisek according to the team the HLB was on the other side of the berm I just attached  photos

### Eric Brewer, 2025-06-06

@Cody Smisekthanks.  The ‘fixed-wing using vtol mag’ message comes after impact so I suspect that’s when contact with the VTOL system was lost.  I created a timeline slide here.  Vehicle592Crash

### Eric Brewer, 2025-06-06

@Ted Trowbridge in the debug log I saw a couple ‘PollMainLoop blocked’ messages - do you know what these might indicate?  One occurred ~10s before the incident.

### Ted Trowbridge, 2025-06-10

@Eric Brewer It means the main poll loop that handles vehicle tx/rx was blocked and not executing for that number of ms.  Generally means the GCS was frozen for that amount of time, but there’s some nuance.

### Cody Smisek, 2025-06-19

aircraft rcvd, just pulled vtol AP, working on data collection

### Cody Smisek, 2025-06-19

@Eric Brewer @David Grosher VTOL logs added to sharepoint folder

### Pat Wells, 2025-06-27

Has this been looked at since 6/20?
@David Grosher @Cody Smisek @Eric Brewer @Drew Hildreth

### Eric Brewer, 2025-06-27

@Pat Wells yes - sorry have been working it but didn’t update the ticket.  At this point our best guess is some sort of software glitch that corrupted the AHRS (pitch/roll estimates of the vehicle were bad).  We have implemented a software patch that will go into future releases.

### Drew Hildreth, 2025-07-09

@Eric Brewer I know that everybody is busy and pulled in multiple directions. Do you happen to have an update on this? Are we calling it a SW problem?

### Eric Brewer, 2025-07-09

@Drew Hildreth correct - our best guess at this time is that this was a software issue.  @David Grosher FYI.

### Pat Wells, 2025-07-10

@Eric Brewer @David Grosher do we need to notify customers about this with any sort of work around in the interim while the final report and CA is being created?

### David Grosher, 2025-07-10

@Pat Wells No, the issue is not fully understood and there is no workaround. I believe that the proposed fix is actually data validation prior to being used.

### Eric Brewer, 2025-07-17

@Pat Wells @David Grosher I updated ticket status above and the powerpoint.  I believe this closes this incident investigation but let me know if you need anything else.

### Pat Wells, 2025-07-17

@Drew Hildreth @Alexander Alan Arnold @Jackson Riley Curvin Please review and prepare the final report for a customer facing release.

### Pat Wells, 2025-08-20

@Eric Brewer were the CA’s for this implemented yet?

### Eric Brewer, 2025-08-20

@Pat Wells The PR’s have been merged but they are in 6.6 which is not yet released.

### Jackson Riley Curvin, 2025-08-25

@Eric Brewer @David Grosher could you please look at the report and see if I need to change anything before sending it to the customer. [embedded: CustomerReportVXE-592 (42d1d66a-07a4-4d66-a81e-f75035ae0433).pdf]

### David Grosher, 2025-08-25

@Jackson Riley Curvin Looks good

### Tim Muchmore, 2025-08-29

When can we expect the report to be released to the customer?

### Pat Wells, 2025-09-03

Report sent to the customer PM on 9/3/25

## Attachments (24)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Cngt_Rng_Skeet_Rng1.trl | other | 13 | 2025-05-30 | listed only |
| Cngt_Rng_Skeet_Rng1_Mishap.vmis | other | 4 | 2025-05-30 | listed only |
| IMG_5732.jpg | image | 10651 | 2025-05-30 | listed only |
| IMG_5735.jpg | image | 9237 | 2025-05-30 | listed only |
| IMG_5742.jpg | image | 10367 | 2025-05-30 | listed only |
| Mishap_Cngt_Rng_30May2025(2).JPG | image | 69 | 2025-05-30 | listed only |
| Mishap_Cngt_Rng_30May2025.JPG | image | 631 | 2025-05-30 | listed only |
| VTOL log.PNG | image | 53 | 2025-05-30 | listed only |
| XCOMM_VXE592 (d91a3421-c017-4558-8fb6-0ed2e218b00e).zip | archive | 3569 | 2025-05-30 | listed only |
| XCOMM_VXE592.zip | archive | 3569 | 2025-05-30 | listed only |
| [Mishap Reporting Procedure Form- MOLSON 5-30-25.pdf](attachments/29540_Mishap%20Reporting%20Procedure%20Form-%20MOLSON%205-30-25.pdf.md) | pdf | 358 | 2025-06-02 | converted |
| image-20250602-132138.png | image | 25 | 2025-06-02 | listed only |
| image-20250602-135545.png | image | 10 | 2025-06-02 | listed only |
| image-20250602-135646.png | image | 16 | 2025-06-02 | listed only |
| image-20250602-135732.png | image | 15 | 2025-06-02 | listed only |
| image-20250602-135852.png | image | 17 | 2025-06-02 | listed only |
| [T95_V592_250530_103929_debuglog.txt](attachments/29611_T95_V592_250530_103929_debuglog.txt.md) | text | 33 | 2025-06-04 | converted |
| image-20250604-165709.png | image | 38 | 2025-06-04 | listed only |
| IMG_5223.jpeg | image | 1276 | 2025-06-05 | listed only |
| IMG_5224.jpeg | image | 123 | 2025-06-05 | listed only |
| [592-elevatorBoostBoardTest.csv](attachments/30067_592-elevatorBoostBoardTest.csv.md) | csv | 2 | 2025-06-20 | converted |
| image-20250804-155523.png | image | 1 | 2025-08-04 | listed only |
| [CustomerReportVXE-592 (42d1d66a-07a4-4d66-a81e-f75035ae0433).pdf](attachments/31719_CustomerReportVXE-592%20(42d1d66a-07a4-4d66-a81e-f75035ae0433).pdf.md) | pdf | 1324 | 2025-08-25 | converted |
| [CustomerReportVXE-592.pdf](attachments/31718_CustomerReportVXE-592.pdf.md) | pdf | 1324 | 2025-08-25 | converted |
