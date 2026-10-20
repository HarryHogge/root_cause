# VA-482: 553  Current Sense CW Power Connector, AS150 pin has solder blob.

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2023-09-08
- **Updated:** 2023-11-03
- **Resolved:** 2023-10-31
- **Reporter:** Cameron Chapman
- **Assignee:** Adrian Garcia
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-13 (TPTR-51 516 VTOL Motors failed to engage during Launch Wizard 511/516 CW damage); relates to VA-483 (553 Current Sense CW Power Connector, AS150 pin has solder blob.); relates to VXEP-385 (New Connectors and Contacts, Overall Requirements Review)
- **Part Number(s):** 107-102264 Dual Current Sense Assy
- **Corrective Action:** https://jenaero.atlassian.net/browse/VXEP-13
- **Production Stakeholder:** Carson Buckley
- **Other Stakeholder (as required):** Matt Philley

## Description

Keep all files and flight data here: https://jenaero.sharepoint.com/:f:/s/FlightSafety/ElYfPImWachDjl0OuLV7TQMBk6GpOEOx0EltmIT0SLgmHw?e=pi92AT 
NCR-230906 - 1481
Current Sense CW Power Connector, AS150 pin. Likely the harness was not fully seated, pin reflowed and now has a solder blob. Fortunately no incident occured during flight.
We believe the reflow happened during the second flight based on marking on the battery connector which is the "heavy" flight with the 5.5-6lb dummy payload
107-102264 Dual Current Sense Assy
SN: C-S100803

[embedded: image-20230908-160822.png]

## Vehicle Configuration

2 batteries are suspect on this flight, since it's unclear if the damage happened during flight #2 or #3. The serials are 2-1287 (#2), 2-1286 (#3).
Flight #1 is minimum weight / no payload, flight #2 is maximum weight / weighted payload, flight #3 is normal weight / camera payload. It's very unlikely the connector would have overheated at minimum weight.

## Plan

- @Laszlo Juhasz @Adrian Garcia , this was removed from the aircraft and should be in the NCR cage. We should test it’s impedance to see if it had a defective contact, then add the measurement and 511/516 to the AS150 sheet (may have already added the last).
- This part was already replaced. Maybe ready for review and closure after step 1.

## Issue Status

See here for report in process.  Vehicle Investigation V553.pptx
Battery from the third flight shows melted solder/signs of overheat. Red tagged as NFF. This indicates the melting was likely on this flight. 
These were less experienced folks assembling them. When Carson brought up the direction to make sure it seats past the o-ring (i.e. keep pushing further after you hit the initial resistance) to them after seeing the reflow they were surprised... so its still just speculation that they were not fully seating the connector, but extremely likely.
None of the reviewed flights show signs of overcurrent. This is supporting evidence for the not fully mated theory.

## Root Cause

Equipment was scrapped. Unable to troubleshoot much further. Tracking C/CA here. https://jenaero.atlassian.net/browse/VXEP-13

## Comments (8)

### Cameron Chapman, 2023-09-08

@John Clark do you have anyone available for the following? It is holding up SCO, so high priority. 
- Flight data review of the incident described above. Data is one of the logs in the linked location. 
- Plot Voltage, power, and currents for the takeoff and landing portions of both flights.
- Identify battery SN connected for each.
- Identify any anomalies. Contact Cameron when complete for review.

### Cameron Chapman, 2023-09-08

FYI @Adrian Garcia and @Laszlo Juhasz

### Cameron Chapman, 2023-09-08

Nadia will start data review.

### Carson Buckley, 2023-09-08

HLB SN 2-1286 is tagged INOP due to solder re-flow damage to connector. Damage occurred on flight #3 of the vehicle. Other two batteries (3 flights per vehicle) have been inspected and do not show evidence of damage.

### Nadia Brown, 2023-09-08

I have created a ppt with some remarks on the data I reviewed at this location: 
553 Current Sense CW Power Connector, AS150 pin has solder blob

Vehicle Investigation V553.pptx

### Nadia Brown, 2023-09-12

I’ve added a few more slides on the PowerPoint that compares the vtVbatt and bmsVb, hybrid lift battery from current sense and sum of the individual battery cells respectively.

### Cameron Chapman, 2023-10-03

@Laszlo Juhasz @Adrian Garcia , this was removed from the aircraft and should be in the NCR cage. We should test it’s impedance to see if it had a defective contact, then add the measurement and 511/516 to the AS150 sheet (may have already added the last). 
Reviewing the report. 
It looks like you can see the damage happens between flight 2 and 3 by comparing the bms voltage to the CSB one. It is much closer on flight 2, indicating lower connector resistance. 
 
[embedded: image-20231003-221158.png]
[embedded: image-20231003-221222.png]

### Adrian Garcia, 2023-10-03

@Cameron Chapman I talked to Kat from quality to help me find the connector but it was already scrapped. We then checked the scrap rack and it was not there.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20230908-160822.png | image | 2127 | 2023-09-08 | listed only |
| image-20231003-221158.png | image | 254 | 2023-10-03 | listed only |
| image-20231003-221222.png | image | 281 | 2023-10-03 | listed only |
