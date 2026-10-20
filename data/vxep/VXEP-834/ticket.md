# VXEP-834: VXE 567 Low battery warning during mission and link loss during RTB resulted in crash

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2024-12-12
- **Updated:** 2026-09-09
- **Resolved:** 2024-12-18
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Cody Smisek
- **Creator:** Alexander Alan Arnold
- **Labels:** Crash, PMA263, Weekly-incident-tracker, battery
- **Links:** relates to RMA-434 (VXE-567  250124-2 PMA263 GW AC); relates to VXEP-540 (Recent AS150 Connectors causing intermittency and difficulty to connect and disconnect correctly and safely (AS150 Socket Issues))
- **Customer:** PMA263
- **Vehicle Tail Number:** 567
- **Vehicle Configuration:** VXE 30 standard battery configuration
- **Plan:** data review
- **Root Cause:** Root cause is undetermined based off of data given
- **Incident Type:** Aircraft Loss
- **Severity:** 1 - Flight Critical

## Description

Operator statement
The set up and preflight of the VXE 30 stalker underwent with no issues. The bird was launched at 0901, successfully climbed to 300ft and transitioned to fixed-wing at 0902. When the bird was climbing to its orbit of 1,500ft a messaged poped up stating that the datalink had been lost for more than 15 seconds. Quickly following that message a battery warning popped up stating that the battery was low at 20% and then at 10%. It jumped back up to 20% and then back down. The battery bar was showing a rapid decline in the amount of flight time left. Return to base was initialized because of the low battery and the bird started to make its way back. The payload lost connection as it took action to return and soon after complete loss of link occured at approximately 0915. Last known grid of the bird was at 51 QVA 10071 46409 making its way to return to base at an altitude of 900ft. End result the stalker was found in the ocean by a local fisherman. We've managed to be able to talk to the local to retrieve whatever was left of the stalker.

## Issue Status

Both cases have signs of mold and poor smell. Recommend use of N95 or better when handling. Do not leave open in engineering area. 
Fuselage avionics enclosure was already separated from remaining components of fuselage. Opened enclosure to check for water intrusion. No signs of water ingress. Powered on using breakout harness and power supply. Pulled last few logs from xcomm. 
VTOL Center Wing was clearly damaged, removed avionics cover and obvious signs of water intrusion. Components have signs of corrosion. Attempted to remove SD card and entire SD card holder hardware separated from PCB.
Jason attempted to check VTOL SD card, appears data is unrecoverable. 
Inspected fuselage main battery connector, no obvious defects noted. 

Files stored here VXEP-834 VXE567 Loss of Link and Crash

## Comments (9)

### Alexander Alan Arnold, 2024-12-12

This crashed aircraft was discovered during an FSR visit to the storage facility for TALSA PAC. We attempted to download data from the VXE 30 but were unsuccessful. Aircraft is currently in the RMA area of SLO @Greg Fryer

### David Grosher, 2024-12-12

@Cameron Chapman Can you have someone pull the data off the system?

### Cody Smisek, 2024-12-18

@David Grosher xcomm logs pulled. VTOL logs not recoverable. Did a quick glance and seems like there’s probably enough data for someone to review. 
Seems power / battery related. 

[embedded image-20241218-190634.png]

[embedded image-20241218-190412.png]

### Cody Smisek, 2024-12-18

Added slides with some data plotting to folder link. Seems similar to AS150 intermittent connection issue. 
Given condition of hardware and exposure to saltwater, seems unlikely any explicit root cause will be determined. Customer report indicates recovery of Main battery, again, seems unlikely anything useful would be gained from inspection given saltwater exposure and time since incident (>6months). 
@Greg Fryer any recommendations on next steps?

### Greg Fryer, 2024-12-18

@Pat Wells This is drifting towards the Bermuda Triangle. Given the low probability and only partial recovery, if we close that way will this customer balk?
@Cody Smisek Does your comment mean the main battery was recovered, but they did not send it to us? (likely due to shipping constraints of a busted battery, being optimistic).
I’m in favor of Bermuda Triangle, since I can’t see a way to get more info. Let’s see what Pat says.

### Cody Smisek, 2024-12-18

correct, the attached incident report (from the customer) indicates that main battery was recovered. Assumption is we’d never see that, as you said, shipping issues.  @Greg Fryer

### Greg Fryer, 2024-12-18

Ok then, yes I definitely vote Bermuda Triangle. @Pat Wells I moved to the triangle, let us know if that blows up or will blow up.

### Alexander Alan Arnold, 2024-12-23

@Pat Wells Please review

### Sam Miller, 2025-01-24

@Pat Wells Based on the information provided, I approve a good will replacement for this aircraft.

## Attachments (11)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [20240606 NBCO Incident report v1.0 VXE567 PMA263.xlsx](attachments/24985_20240606%20NBCO%20Incident%20report%20v1.0%20VXE567%20PMA263.xlsx.md) | xlsx | 1624 | 2024-12-12 | converted |
| Media (14).jpg | image | 418 | 2024-12-18 | listed only |
| Media (15).jpg | image | 356 | 2024-12-18 | listed only |
| Media (16).jpg | image | 383 | 2024-12-18 | listed only |
| Media (17).jpg | image | 285 | 2024-12-18 | listed only |
| Media (18).jpg | image | 130 | 2024-12-18 | listed only |
| Media (19).jpg | image | 178 | 2024-12-18 | listed only |
| Media (20).jpg | image | 219 | 2024-12-18 | listed only |
| [VXE567.txt](attachments/25067_VXE567.txt.md) | text | 1 | 2024-12-18 | converted |
| image-20241218-190412.png | image | 34 | 2024-12-18 | listed only |
| image-20241218-190634.png | image | 21 | 2024-12-18 | listed only |
