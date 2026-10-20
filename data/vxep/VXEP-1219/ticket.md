# VXEP-1219: VXE-758 Mag Cal issues

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-04-18
- **Updated:** 2025-06-24
- **Resolved:** 2025-06-24
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** Edge_Asset, Weekly-incident-tracker
- **Vehicle Tail Number:** VXE 758
- **Vehicle Configuration:** VXE30 standard battery config
- **Problem Type:** Discovered Issue
- **Incident Type:** Other (Record"Event Type: XXXXXX" in the description)
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

After updating VXE758 and SGCS1 Kit 95, we attempted performing the new Mag Cal Procedure with MagFit according to the newest VXE30 Operations Manual. While performing the test on multiple different occasions, it appears that there is a potential bug in the newest software. While performing the procedure, the MagFit GUI does not display any information while rotating the aircraft in any of the 6 listed positions. We only have one SGCS and aircraft currently in HSV to test. Attached is an AAR and video file from our most recent attempt to conduct the calibration.

## Corrective Action

Create Service Bulletin to alert customers to click allow access when they do a Mag Cal for the first time, with additional steps to go into the firewall if they did not select allow.

## Root Cause

MagFit was not allowed through firewall, suspected that operator did select allow during first Mag Cal after updating GCS to 6.4

## Comments (9)

### David Grosher, 2025-04-18

@Jason Scherer @Ted Trowbridge @Scott Whitney Did we miss something here?

### Scott Whitney, 2025-04-18

@Alexander Alan Arnold do you know which GCS configuration you have is? It may be a firewall issue. @Jo Brown

### Jackson Riley Curvin, 2025-04-22

@Scott Whitney  its the standard Config that comes from production.

### Alexander Alan Arnold, 2025-04-22

DO you need anything else from the GCS for the investigation? @Scott Whitney

### Scott Whitney, 2025-04-22

@Alexander Alan Arnold @Jackson Riley Curvin  - could you try re-installing 6.4 onto the GCS. When you run the installer select “repair” to reinstall. Then when you go through the mag check and start to open the magfit make sure to hit ‘Allow Access’ on the windows security alert

[embedded: image-20250422-204557.png]

### Alexander Alan Arnold, 2025-04-22

Will do. Our only asset was sent to the team at the AEWE demo. Once we have an aircraft back in Huntsville, we will try this again. @Scott Whitney

### Scott Whitney, 2025-05-06

@Alexander Alan Arnold  - any update on this? We recently ran into this issue in the field and if you go into the windows defender firewall → allowed apps the MagFit private needs to be checked
[embedded: image-20250506-212943.png]

### Calvin Rogers, 2025-05-08

@Scott Whitney We just checked the GCS laptop and discovered that the MagFit app was deselected. We allowed access and successfully completed a mag cal procedure with no issues.

### Alexander Alan Arnold, 2025-05-08

@Scott Whitney I am going to move this to D6, it seems the corrective action will be to create a Service Bulletin to alert customers to click allow access when they do a Mag Cal for the first time, with additional steps to go into the firewall if they did not select allow.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Mag Calibration Issues.mp4 | video | 48437 | 2025-04-18 | listed only |
| T95_V758_250418_114206_pack.zip | archive | 3373 | 2025-04-18 | listed only |
| image-20250422-204557.png | image | 438 | 2025-04-22 | listed only |
| VXE MUAV.lnk | other | 2 | 2025-04-24 | listed only |
| image-20250506-212943.png | image | 4525 | 2025-05-06 | listed only |
