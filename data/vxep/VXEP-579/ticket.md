# VXEP-579: VXE 513 Multiple magnetometer faults displayed during flight

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-08-29
- **Updated:** 2026-03-02
- **Resolved:** 2025-02-25
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** 1st_SFG, USASOC, Weekly-incident-tracker
- **Customer:** 1SFG(A), 1st, USASOC
- **Vehicle Tail Number:** 513
- **Root Cause:** Software bug due to lack of FPU support in Mag calc task. This had been found independently and a fix is in v6.4
- **Incident Type:** Other (Record"Event Type: XXXXXX" in the description)
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

From Edge instructor and customer training event:
We just landed an aircraft that had multiple magnetometer faults presented in flight and on landing.The aircraft performed perfectly. Heading on aircraft status was accurate. The faults did populate but nothing occurred out of the ordinary. Admittedly, we had to use the xcomm page to warm the HLB, and it was left up during he flight. That was an error on my part and I wasn’t almost 100% certain I had closed it. I’m not sure if that would affect anything regarding the magnetometer faults.  Completed MAG cal post flight and everything passed with no issues.
AAR attached

## Corrective Action

CAs are already implmented to address this.  Fix I2C initialization timeout and add FPU support to the Mag processing. https://jenaero.atlassian.net/browse/FS2-2097

## Comments (6)

### David Grosher, 2024-08-29

@Pat Wells Did this vehicle have a payload?
@Eric Brewer Can you look at the mag data to see why it was throwing errors? 
@Scott Hunter Can you look at the mag driver to see if there were any issues with the interface?

### Cameron Chapman, 2024-08-29

@Pat Wells @David Grosher should the trainer need to use the xcom page to warm up the HLB, or should it warm itself up automatically? It shouldn’t affect this issue, but maybe a separate lower priority issue.

### Pat Wells, 2024-08-29

@David Grosher yes the vehicle had a Trillium payload.

### Eric Brewer, 2024-08-30

[embedded: image-20240830-142112.png]
It definitely had a failure of xmag (when those first 2 bits of IMUSrc are set xmag is valid, when it’s 0 it’s invalid).  We switched over to fixed-wing heading updates for the rest of the flight (confirmed in VTOL debug outputs).  @Scott Hunter any ideas why mag is failed? See above the raw readings look pretty reasonable to me so I don’t think they should have tripped any of our failure detection.  @David Grosher

### Scott Hunter, 2024-09-05

The data in the event log shows some kind of problem with either the logging or sensor interface. The fault records a failed test of the ratio between the expected mag field strength and the measured mag field strength at 10:10:57. Both values for the expected field and measured field are impossible.
There are 3 relevant entries in the log file:
- [09:55:01.003 32.004] WMM 0:/WMM.COF WMM-2020
- [09:55:01.072 32.072] field 0.5253
- [10:10:57.001 988.001] MAGFAIL: ratio > [ratio, 1+margin, mag, erf] 55555560  399  166666  3

Entry 1 indicates the file containing the expected mag field strength was read successfully. Entry 2 indicates the expected field strength is .5253 Gauss. The 3rd entry indicates the mag/erf ratio was excessive. The 4 values multiplied by 1000 to capture floating point data where floating point variables aren’t supported. The 4 values are:
- Calculated ratio (55555.560)
- 1+margin (.4), the threshold for a fault. Note: due to a bug this is actually 1-margin, the actual threshold is 1.6
- Measured mag strength (166.66 Gauss)
- Expected Field (.003 Gauss)

We know the expected field was correctly read as .5253 from the 2nd log entry and we know the 166 Gauss reading for measured mag field strength is impossible since the range of the sensor’s scaling is 4 Gauss.
Based on the data recorded to the .CSV file there was no excessive mag field. Below is a plot showing the magnitude of the mag field with upper/lower thresholds and the mag validity flag overlayed. You can see the measured mag field does not approach the thresholds and there’s no anomalous data near the good->bad transitions of the mag health flag.
[embedded: image-20240905-192341.png]

This same issue appears to be captured in Jira as https://jenaero.atlassian.net/browse/FS2-2097?atlOrigin=eyJpIjoiNWVhYTgyODE3YjNlNDNmMTgyNjViM2E1YWEzNGRlNmUiLCJwIjoiaiJ9

### Alexander Alan Arnold, 2024-12-10

@David Grosher is D4 still an accurate status of this investigation?

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V513_240828_130942_pack.zip | archive | 2775 | 2024-08-29 | listed only |
| image-20240830-142112.png | image | 74 | 2024-08-30 | listed only |
| image-20240905-192341.png | image | 210 | 2024-09-05 | listed only |
