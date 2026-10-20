# FS2-4500: Investigation of TIQ Aviboxes

- **Issue type:** Task
- **Status:** In Review
- **Priority:** High
- **Created:** 2026-04-14
- **Updated:** 2026-09-04
- **Reporter:** Scott Whitney
- **Assignee:** Scott Whitney
- **Creator:** Scott Whitney
- **Links:** relates to VXEP-1840 (VXE 655 unable to connect); relates to VXEP-1838 (VXE 622 unable to connect); relates to VXEP-1839 (VXE 648 unable to connect to VTOL due to damaged CAN transceiver )
- **Sprint:** FS2 Sprint 37, FS2 Sprint 39, FS2 Sprint 38

## Description

AV Box: 622
- Powered up avionics on Iron bird
- Black and grey alden only
- GCS version 6.6.1
- Attempted to connect GCS to vehicle
- GCS autodetect tail number
- Note: Magfault alert comes in from XCOMM (signs of life)
- Fails to connect to vehicle
[embedded: image-20260414-190855.png]
- Open Webpages - All looks normal 
[embedded: image-20260414-190521.png]
- Throughput page - No FWAP details
[embedded: image-20260414-190534.png]
- Navigated to Configs -> portmon is on (turn off based on SWQA recommendation)
- enable_portmon   Enable switch port monitor
- Switch enable_portmon 'off'
- Power cycle avibox
- Did not fix issue - still no info in throughput page
- Switch enable_portmon ‘on'
- XCOMM Log files link: [embedded: v622_DataLogs.zip]


AviBox 648
- Successful connected to jennings GCS 6.6.1
- AAR downloaded:  [embedded: T95_V648_260414_110442_pack.zip] 
- NOTE: VTOL data from Iron Bird Asset not from vehicle 648
- No additional steps taken

AviBox 655 (same result as 622)
- Powered up avionics on Iron bird
- Black and grey alden only
- GCS version 6.6.1
- Attempted to connect GCS to vehicle
- GCS autodetect tail number
- Note: Magfault alert comes in from XCOMM (signs of life)
- Fails to connect to vehicle
[embedded: image-20260414-190847.png]
- Open Webpages - all looks normal
[embedded: image-20260414-190714.png]
- Throughput page - no FWAP details
[embedded: image-20260414-190725.png]
- Logs pulled from XCOMM webpage: [embedded: v655_dataLogs.zip]


2026-04-16
AviBox 655
- Attempt to reflash FWAP to 6.5.0 v6.05s - same result “Failed to Connect”
- update was successful; power cycled avibox
- no details on Throughput page
- GCS unable to connect to vehicle
- Attempt to flash FWAP to 6.5.1 v6.05t - same result “Failed to connect”
- update was successful; power cycled avibox
- no details on Throughput page
- GCS unable to connect to vehicle

AviBox 622
- Attempt to reflash FWAP to 6.5.0 v6.05s - same result “Failed to Connect”
- update was successful; power cycled avibox
- no details on Throughput page
- GCS unable to connect to vehicle

## Comments (4)

### Scott Whitney, 2026-04-16

Through put webpage from Avibox 648. This avibox can successfully connect through gcs
[embedded: Screenshot 2026-04-16 092429-20260416-162430.png]

### Scott Whitney, 2026-04-16

After discussions with John and Scott h - it was evident that the issue is consistent with MPU 9250 failures and needs to be replaced
- MPU-9250 init fails
- then goes into a while loop and continues to fail Init

XCELOGS from 622:

[embedded: image-20260416-222951.png]
XCELOGS from 655

[embedded: image-20260416-223005.png]

### Stephan Johnson, 2026-04-27

@Scott Whitney are there any updates on these, by chance?

### Scott Whitney, 2026-04-27

@Stephan Johnson each avionics was handed off to the EE team. They have provided updated in their respective VXEP:
- https://jenaero.atlassian.net/browse/VXEP-1840
- https://jenaero.atlassian.net/browse/VXEP-1838
- https://jenaero.atlassian.net/browse/VXEP-1839

## Attachments (12)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V648_260414_110442_pack.zip | archive | 14281 | 2026-04-14 | listed only |
| image-20260414-190521.png | image | 151 | 2026-04-14 | listed only |
| image-20260414-190534.png | image | 87 | 2026-04-14 | listed only |
| image-20260414-190714.png | image | 151 | 2026-04-14 | listed only |
| image-20260414-190725.png | image | 88 | 2026-04-14 | listed only |
| image-20260414-190847.png | image | 16 | 2026-04-14 | listed only |
| image-20260414-190855.png | image | 16 | 2026-04-14 | listed only |
| v622_DataLogs.zip | archive | 3971 | 2026-04-14 | listed only |
| v655_dataLogs.zip | archive | 9388 | 2026-04-14 | listed only |
| Screenshot 2026-04-16 092429-20260416-162430.png | image | 91 | 2026-04-16 | listed only |
| image-20260416-222951.png | image | 51 | 2026-04-16 | listed only |
| image-20260416-223005.png | image | 71 | 2026-04-16 | listed only |
