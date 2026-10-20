# VXEP-1778: VXE-512 Lost Power during transitiion resulting in crash

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2026-03-18
- **Updated:** 2026-09-22
- **Resolved:** 2026-09-22
- **Reporter:** Jackson Riley Curvin
- **Assignee:** Samuel Lopez
- **Creator:** Jackson Riley Curvin
- **Labels:** Hardware, RCCA, Weekly-incident-tracker
- **Links:** relates to RMA-1016 (VXE-512 RMA 260506-3); relates to VXEP-1970 (VXE 525 Nose dive after transition )
- **Customer:** SOCOM(SUMS)
- **Vehicle Tail Number:** VXE-512
- **Vehicle Configuration:** VXE-30 standard, Battery Config.
- **Corrective Action:** None
- **Problem Type:** Discovered Issue
- **Root Cause:** Cannot Reproduce
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical
- **Components (EA Aircraft):** Aircraft, full assembly

## Description

Operator Statement:
Winds on ground were 6-7 kts and gusting up to 13. AV VTOL climbed to 300ft agl then transitioned to horizontal flight where it climbed to 400ft and reached wp1. AV then initiated a right hand turn towards the mission loiter, after turning roughly 90° AV rapidly descended an estimated 200ft while still initiating a right hand turn. At this time the AV operator lost connection with the aircraft. AV operator commanded RTB in an attempt to recover the aircraft safely. AV continued to descend until it collided the ground.

## Plan

Investigation summary: https://jenaero.sharepoint.com/:p:/s/FlightSafety/IQAziFJhBXR6TJhaaMlcRoD1AWhYrPHhu-aR5v3Mm6rEmDA?e=XIJM7G
Aircraft arrived in SLO. Inspect for avionics power loss cause. See below. @Samuel Lopez can you please coordinate inspecting this when available? 
- See comments in test notes for additional tests that could be performed. @Samuel Lopez
- Summarize findings. (see confluence template, seems more efficient). 
- Nose ODU seems to be latching correctly. Unlikely related.
- Black Alden still had RTV bonded.  Unlikely related.
- Avbox opened and inspected. No abnormalities.
- Do we know what main battery was used in this incident? Record SN, locate, and inspect.

Full Test Notes can be found here!!
Test Notes

## Issue Status

Aircraft in SLO. Ready for inspection.  FSR tried to have the operator conduct FTP procedure to pull data but could not connect to aircraft had them try and open the XComm and VTOL webpages with no success. 
GCS was on 6.3.4, aircraft should be on 6.6.1. Should be unrelated, but could be valuable to include in report.
Extensive testing yields no cause of failure yet.
Although the customer did not keep track of which battery was used, the customer can very easily run an impedance check on each of the batteries (which should be around 1.2-1.3milliohms per cell) using the battery chargers.  Since this is a quick check, we're requesting they just do this to every battery.  If even one is unbalanced, that may explain the failure.

## Executive Summary

Requesting customers use charger to run impedance test on batteries available. We are unable to identify single point of failure. Extended wait time for customer to return on RMA. Probable cause Operator Error/ Hardware.

## Comments (31)

### Jackson Riley Curvin, 2026-03-19

[embedded: image-20260319-224018.png]

### Jackson Riley Curvin, 2026-03-19

[embedded: image-20260319-224146.png]

### Jackson Riley Curvin, 2026-03-19

[embedded: image-20260319-224309.png]

### Jackson Riley Curvin, 2026-03-19

VXE-SUAV version on 6.3.4 Aircraft on 6.6.1

### Drew Hildreth, 2026-03-25

Waiting on Customer to provide Data

### Jackson Riley Curvin, 2026-04-29

Waiting on customer to RMA aircraft once it arrives RMA team will need to pull data.

### Jackson Riley Curvin, 2026-05-06

@David Grosher Just received data for 512 Xcomm and Vtol logs here: https://jenaero.sharepoint.com/:f:/s/FlightSafety/IgCxCPGFm13XRrMSGH5GnwXNAW6pgoFNwbURht7ruqUS6Ig?e=AfImg4

### Scott Lovett, 2026-05-06

XCOMM & VTOL zips added to attachments here to avoid using Sharepoint which is being slow

### David Grosher, 2026-05-06

Investigation Notes: It appears that the system simply lost power during launch transition. Both the VTOL and XCOMM stop at roughly the same time at altitude. I didn’t see any data in a quick look at the logs that indicate issues in the system prior to the event. 

XCOMM 4.74, 2ae959d
The incident appears to be in XC000101.T06 and paired with XCL00071.csv
Event Log Stops at LCH_FLY_ASSIST at CpuTime 2155.530
Data Log stops at CpuTime 2156.821
There is no WDT dump to indicate that a reset occurred
VTOL data log stopped at  VTOL CpuTime 1809.26 and UTC 175136.894
VTOL event log stopped at VTOL CpuTime  1808.159
 
@Scott Lovett @Jackson Riley Curvin @Drew Hildreth @Cameron Chapman

### Zack Garcia, 2026-06-15

intake complete, awaiting assessment of avionics box @Drew Hildreth

### Drew Hildreth, 2026-06-16

@Zack Garcia Did we conduct the FTP Procedure on this aircraft?

If not, please do so, then I am okay with the avionics going to be evaluated.

### Alexander Alan Arnold, 2026-06-29

@Lauren Velasquez @Cameron Chapman @Scott Whitney can we have someone looking at the logs or taking a look at the aircraft @Drew Hildreth customer is calling asking for status updates.

### Cameron Chapman, 2026-07-01

@Alexander Alan Arnold It looks like Dave already looked at the logs below. Next step appears to be hardware inspection. Do you have updates on that?

### Alexander Alan Arnold, 2026-07-01

@Zack Garcia Was the avionics given to engineering for assessment?

### Zack Garcia, 2026-07-01

@Alexander Alan Arnold it was planned too, as of right now i don't have proof of it going to engineering but i know a full pull was done

### Alexander Alan Arnold, 2026-07-01

copy on the FTP. Can we please locate the avionics? @Zack Garcia

### Zack Garcia, 2026-07-01

@Alexander Alan Arnold was this incident at flight ops, if so was it yesterday or today?

### Alexander Alan Arnold, 2026-07-01

the incident was March 18th, this a customer avionics for VXE 512, since the data is loaded in the ticket Dave is saying there is nothing else available in the Logs so we need to get the avionics to the engineering side of the house so they can begin inspection/investigation of the component to hopefully locate a failure that contributed to the mishap. I believe it should be delivered to @Samuel Lopez

### Zack Garcia, 2026-07-01

@Alexander Alan Arnold i have the box right now in rma i will get that done asap

### Samuel Lopez, 2026-07-08

@Alexander Alan Arnold , @Zack Garcia  @Cameron Chapman 
On 7/2 and 7/7
I tested the avionics box on the iron bird bench.  It powers normally and does not show a sudden loss of power.  I was also able to download log files from the xcomm webpage on both of these days.

On 7/9
I powered on the same avionics box on the 512 aircraft and could not log in to the XCOMM webpage.  I took 512 av box back to the iron bird and still could not establish communication using the same laptop/dongle as the day before either with the xcomm webpage or the launch wizard.  However, though we could not talk to the webpage, rotating the avionics box did cause the servos to action.

After 20 minutes, Matt P was able to establish connection with his laptop.  I re-tried with my own laptop and was able to establish connection as well.  I still cannot, however, log in to the ‘log files’ webpage.  It’s unknown how mysterious behavior is correlated with root cause.

### Cameron Chapman, 2026-07-08

@Samuel Lopez thank you. please check the whole harness (MB to current sense board to black alden)

### Samuel Lopez, 2026-07-15

Summary of tests and results
Tests
·       Avionics box on the bench is on for 5 minutes with no issues.
·       Complete fuselage – Motor Test (no blades) of 60fps for five minutes.  Power supply pulled 1.5A.  No failures.
·       Complete Fuselage – Motor Test (with blades).  Battery pulled 52A for 40 seconds.  No failures.
Irregularities
·       Checksum of autopilot is different than when intake occurred.
·       First and second day of testing avionics box on the iron bird went without incident.  On third day of testing, xcomm and vtol webpages could not be loaded.  After 20 minutes of attempting different setups, connection was mysteriously established.  When xcomm page loaded up, ‘log files’ page would not load.  After a reset, everything was back to normal.  This behavior has not re-occurred.

### Samuel Lopez, 2026-07-16

@Lauren Velasquez and @Zack Garcia 

Can you put the order to open the avionics box be opened for inspection for this aircraft to inspect the xcomm and fwap?

### Lauren Velasquez, 2026-07-16

@Samuel Lopez I believe between the VXEP parameters you are able to open and inspect, But we are able to also do that. What is it that you are looking for? 
“Putting in an order” would signify we already know the repair scope of work. 
@Drew Hildreth Please let me know if you have any objections to us cracking this avionics open, given the failure and findings at this time.

### Samuel Lopez, 2026-07-16

@Lauren Velasquez 

We are looking for burn damage in the av box due to a short.  This is likely not root cause, but our due diligence demands an inspection since we can’t find anything else.

@Drew Hildreth 
Any objections to opening the av box?

### Drew Hildreth, 2026-07-17

@Samuel Lopez I have no objections to this. It will change how we do SCO and Flight Test, but as long as we have good dispo we are good

### Alexander Alan Arnold, 2026-08-10

@Samuel Lopez were you able to find anything while inspecting?

### Samuel Lopez, 2026-08-10

@Alexander Alan Arnold 
No.  It could either be
- Microcontroller Failure
- Bad Battery
- Improper Mating


and it’s probably not
- Avionics Box Hardware
- Harness

The customer did not keep track of which battery they used.  They could, however, do a quick check of all their batteries to check for imbalanced cells.

### Drew Hildreth, 2026-08-27

@Lauren Velasquez can you please get a quote request in for this. Also confirm with Jermey that we can quote for an advnaced nav. Brooks emailed about it this morning.

### Lauren Velasquez, 2026-08-27

@Drew Hildreth Has warranty been determined?

### Drew Hildreth, 2026-09-03

@Lauren Velasquez Based on the report. This is Non-warranty.

## Attachments (19)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 100318bb-15c1-4db9-939c-4a181446e85a.jpg | image | 145 | 2026-03-18 | listed only |
| 1d39937a-1db7-48f3-a1eb-d10905927298.jpg | image | 87 | 2026-03-18 | listed only |
| 3152ed4b-c5ca-48bf-90b9-f43d3279edc3.jpg | image | 147 | 2026-03-18 | listed only |
| 4d47b252-6679-4172-be5f-af2238aef3ac.jpg | image | 146 | 2026-03-18 | listed only |
| 513d0d91-40be-49f2-955f-a98fd381983f.jpg | image | 151 | 2026-03-18 | listed only |
| 6bfadf4f-3563-4b3b-8eaa-625ee19dbd89.jpg | image | 105 | 2026-03-18 | listed only |
| 8c608df5-7a7a-4c2b-b41b-a03ee0154162.jpg | image | 93 | 2026-03-18 | listed only |
| a10abe46-1676-4873-ad6e-1e150222ee7d.jpg | image | 165 | 2026-03-18 | listed only |
| d7a262a0-a0e8-44ed-a732-ef7dff72b467.jpg | image | 132 | 2026-03-18 | listed only |
| T95_V512_260315_125110_01_pack.zip | archive | 204 | 2026-03-19 | listed only |
| image-20260319-224018.png | image | 81 | 2026-03-19 | listed only |
| image-20260319-224146.png | image | 11 | 2026-03-19 | listed only |
| image-20260319-224309.png | image | 17 | 2026-03-19 | listed only |
| T95_V512_260315_125110_pack_repacked.zip | archive | 5908 | 2026-05-06 | listed only |
| VTOL.zip | archive | 131782 | 2026-05-06 | listed only |
| XCOMM.zip | archive | 44881 | 2026-05-06 | listed only |
| aar512.zip | archive | 6771 | 2026-06-17 | listed only |
| vxe512 full pull.zip | archive | 5251 | 2026-06-17 | listed only |
| [VXEP-1778_VXE-512_Vehicle Investigation_20260921.pdf](attachments/64810_VXEP-1778_VXE-512_Vehicle%20Investigation_20260921.pdf.md) | pdf | 576 | 2026-09-22 | converted |
