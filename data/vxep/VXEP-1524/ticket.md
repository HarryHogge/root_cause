# VXEP-1524: VXE-555 Go To function would not work

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-09-24
- **Updated:** 2026-07-07
- **Resolved:** 2026-07-07
- **Reporter:** Jackson Riley Curvin
- **Assignee:** Ted Trowbridge
- **Creator:** Jackson Riley Curvin
- **Labels:** TIQUILA, Weekly-incident-tracker
- **Customer:** TIQUILA
- **Vehicle Tail Number:** VXE-555
- **Corrective Action:** sending customer tips to try incase this happens.
- **Problem Type:** Other (explain in description)
- **Root Cause:** Possible: GetTickCount() rollover after 49.7 days system uptime causing map tool continuous timeout.
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Description:
the detachment was flying RPA 555 with the intent to conduct BVLOS missions. The flight was conducted and lasted 1:15. Due to inclement weather the decision was made to bring the aircraft within VLOS. However upon attempt to use the GoTo function, it failed to function. When pressing GoTo on the toolbar, the icon would indent to show it had been pressed but when the cursor was moved onto the screen it remained an arrow instead of changing to a crosshair and when clicking on mission elements, it would not select them. When using the Hot Key (Ctr G) the GoTo functioned the same as when pressing the tool bar making the detachment unable to give the aircraft a positive command. The detachment confirmed control of the mission elements by lowering the height of the final wind orbit in which the RPA was currently in. The decision was then made to allow the UA to finish its current mission orbit (lasting 5 mins) instead of giving it a RTB due to recent PTS requiring RTB to monitored. The AOs concern was that the detachment would be able to monitor it but without GoTo would be unable to conduct immediate actions for the “RPA Goes of Task” emergency procedure. The aircraft then proceeded to finish its orbit and as it came through IP 5 preparing to land.
Additional Questions asked by LM:
- Could you provide logs of this issue.  Awaiting transfer
- Confirm environmental conditions Air temp 27 degrees, dropping once weather declined, wind gusting no more than 18knts
- Confirm Link conditions link conditions were good
- Were operators able to take manual control of the AV? No attempt to U-drive was made, decision was to allow aircraft to self recover.
- Any other unusual behavior observed on the GCS screen? No other unusual behaviour was observed on the GCS
- What did they press Go to to - which mission element? RPA was in its final wind orbit (last primary mission element), goto was selected once and used to attempt to send RPA to IP 1.
- Did they try the Go to button multiple times? When the first attempt failed secondary and tertiary attempts were made and all failed.


VXE-555 GO TO Function not Working

## Comments (10)

### Jackson Riley Curvin, 2025-09-24

Awaiting AARs

### Scott Whitney, 2025-09-24

FYSA @Ted Trowbridge

### Greg Fryer, 2025-09-24

@Scott Whitney @Ted Trowbridge FYI, I moved this to Gathering info and then to waiting. Please do this so it’s clear we aren’t ignoring when we review overall status.

### Jackson Riley Curvin, 2025-10-08

@Greg Fryer@Scott Whitney @David Grosher @Ted Trowbridge  I had trouble putting the entire data log on Jira but I pulled the FLT file for both XCOMM and VTOL and put the corresponding logs associated with it. rest of the data is here VXE-555 GO TO Function not Working

### Ted Trowbridge, 2025-10-14

@Jackson Riley Curvindo we have GCS logs from this?

### Jackson Riley Curvin, 2025-10-15

@Ted Trowbridge I do not believe we have gcs logs from this flight @Michael Mohr can you reach out to Dhruti and ask her if the operator can go into their GCS and grab the event log from this flight.

### Michael Mohr, 2025-10-16

@Ted Trowbridge Files uploaded

### Ted Trowbridge, 2025-11-06

@Jackson Riley Curvin  is it possible to ask the customer when the GCS laptop was last restarted?  Seeing a possible root cause if the system had not been restarted in the last 49 days, can we ask if that is a plausible explanation?

### Ted Trowbridge, 2025-11-06

@Jackson Riley Curvin  nevermind, I’ve found a way to determine this.

### Ted Trowbridge, 2025-11-06

I’ve spent a few hours tracing the code paths that would cause the reported behavior:
When pressing GoTo on the toolbar, the icon would indent to show it had been pressed but when the cursor was moved onto the screen it remained an arrow instead of changing to a crosshair and when clicking on mission elements, it would not select them.

It appears all the checks required for the button to be clicked passed:
- Vehicle was connected
- Vehicle was flying
- GCS was not in Demo Mode

Once the button click succeeds the “Go To Waypoint” becomes the active map tool.  This is what causes the map to show a “Go To” crosshair and process mouse clicks to command the vehicle to a waypoint.
The only conceivable root cause is something else in the system immediately switching the active map tool to something else.  There are a few areas that seemed suspicious but I have ruled out most of them:
- The active map tool has timeout logic that is susceptible to a bad calculation after system uptime of 49.7 days.
- I ruled this out via the logs, and it also would’ve only failed once every 49.7 days.

We don’t have enough information in GCS debug/event logs to investigate further.  I’ve added additional logging to help diagnose this in the future that will be merged into GCS 6.6.0.
I recommend closing this out due to very low likelihood (only one reported occurrence) with the corrective action being improved logging to the system starting with 6.6.0.
@David Grosher

## Attachments (13)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [FLTFILES (54f6c72d-ede3-48ce-97b5-162502be5320).TXT](attachments/32872_FLTFILES%20(54f6c72d-ede3-48ce-97b5-162502be5320).TXT.md) | text | 0 | 2025-10-08 | converted |
| [FLTFILES.TXT](attachments/32867_FLTFILES.TXT.md) | text | 0 | 2025-10-08 | converted |
| [VT250922.TXT](attachments/32876_VT250922.TXT.md) | text | 431 | 2025-10-08 | converted |
| [VTEVLOG.TXT](attachments/32875_VTEVLOG.TXT.md) | text | 113 | 2025-10-08 | converted |
| [VTL00025.CSV](attachments/32873_VTL00025.CSV.md) | csv | 283 | 2025-10-08 | converted |
| [VTL00026.CSV](attachments/32874_VTL00026.CSV.md) | csv | 1988 | 2025-10-08 | converted |
| [VTL00027.CSV](attachments/32877_VTL00027.CSV.md) | csv | 1624 | 2025-10-08 | converted |
| [XC250923.TXT](attachments/32871_XC250923.TXT.md) | text | 463 | 2025-10-08 | converted |
| [XCEVLOG.TXT](attachments/32868_XCEVLOG.TXT.md) | text | 80 | 2025-10-08 | converted |
| [XCL00032.CSV](attachments/32869_XCL00032.CSV.md) | csv | 860 | 2025-10-08 | converted |
| [XCL00033.CSV](attachments/32870_XCL00033.CSV.md) | csv | 17 | 2025-10-08 | converted |
| 20250925-DASOR10083_AC555.zip | archive | 5565 | 2025-10-16 | listed only |
| FDR_555.zip | archive | 109871 | 2025-10-16 | listed only |
