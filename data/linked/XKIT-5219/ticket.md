# XKIT-5219: AC 966 - Flight Test - Power bus fault

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-11-24
- **Updated:** 2026-03-18
- **Resolved:** 2026-01-14
- **Reporter:** Cameron Chapman
- **Assignee:** Samuel Lopez
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-1686 (VXE 966 Intermittent Loss of communication to Xcomm)

## Description

See NCR NCR-251121 - 7775 AC 966 - Flight Test - Power buss fault
Video: https://jenaero-my.sharepoint.com/:v:/g/personal/rgabler_edgeautonomy_io/Ea_-J8hj0khHrG3IO6bb5jABqgMVbHGE_vwNxM_MsbMS-Q?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=4gs40o 
Chat with production Cameron Chapman: Did anything happen to this aircraft, or still waiting investigat... | Investigation AC 966 - Flight Test - Power buss fault | Microsoft Teams

AC debug log shows power faults continuous. This happend in first flight test but seemed to clear after power cycle. Now AC has replicated symptoms on 2 power cycles and is an issue. not a normal thing to see for AC. both AARs attached 
Investigation ppt here.

## Corrective Action

Quality has been alerted about this issue.  They are aware of XCOMM units that fail in production due to issues with firmware, loading firmware, rebooting, etc…

## Plan

- Plots show B40 voltages on a B30 plane. 
- @Samuel Lopez Check if issue can be recreated.
- Check if checksums and SW match B30 configs.
- Reflash XCOM FW?


Previous plan. Reevaluate steps if above doesn’t work.
- @Sammy Lopez  are you available to investigate?
- See if issue can be replicated on ground without payloads.
- Pull avionics box and see if it replicates on iron bird.
- If the error log matches the schematic terminology, it seems to be an issue with the payload ports. @Eric Brewer  can you confirm if this error message is for this aux bus, and any documents connecting error messages to data points/HW? We should list such info here VXE-FCD-XCOMM Log Glossary.docx
- What was connected for this test? "This happend in first flight test but seemed to clear after power cycle. Now AC has replicated symptoms on 2 power cycles and is an issue. not a normal thing to see for AC. both AARs attached" first flight is no payloads right?
[embedded: image-20251124-222352.png]
- Does the error happen with no payloads connected? @r
- Desiray Johnston what is the priority of this vs other investigations/B40 work? https://jenaero.atlassian.net/browse/XKIT-5219
- Eric Brewer What triggers a bus fault like that? Overcurrent?
- Carson Buckley was this functional before flight test? Was anything changed after like ADP?
- Check OAT during test. Was it cold during this test? I am wondering if it had heated pitot that didn't turn on before and hit a current limit
- We could see if a cold pack on the pitot activates the heater in SCO. Agreed we should check that

December 29, 2025
- XCOMM on AC 966 has been replaced.  According to Carson Buckley, there are no more ‘anomalous voltages’ and there are ‘no further issues’.   The aircraft itself is considered finished.
- The XCOMM board removed from AC 966 is to be investigated.
- Visual inspection with Sammy Lopez and Natalie Lusk reveals no solder bridges, solder balls, tomb stoned components, or any other anomalies.
- Check voltages of ADC pins.  If they are reflective of voltage divider, then the problem is the microcontroller.

2026-01-06
- XCOMM board that was removed from AC 966 was tested alone on the bench where it displayed similar behavior as before (i.e. Vbatt 55V, Vpayload 16.55V, etc)
- ADC pins were measured with voltmeter and measure normally.  Root cause is in the microcontroller.
- Firmware was re-uploaded to XCOMM.  Voltages on Vbatt, Vpayload, Vservos now measure normally.
- After talking with Quality, there have been dozens of XCOMM boards fail in 2025.  At a glance, many of the issues appear to be associated with the microcontroller.

## Root Cause

Firmware corruption in microcontroller.
Microcontroller reported incorrect voltage readings from ADC inputs.  After firmware was re-uploaded, voltage readings are normal. 
Final root cause inconclusive.  XCOMM may be susceptible to transients in productions.

## Comments (10)

### Eric Brewer, 2025-11-25

@Cameron Chapman linked an investigation powerpoint above.  Looks like both aux1 and payload were reading 0 voltage.

### Jeremy Kostel, 2025-12-04

[embedded: image-20251204-180927.png]
MB voltage reading 55V

### Cody Smisek, 2025-12-11

should this be in VXEP or xkit jira?@Cameron Chapman

### Cameron Chapman, 2025-12-11

@Cody Smisekdisregard previous message. It is 56V battery. It belongs in Xkit. I will try to update status

### Rajesh Budhabhatti, 2025-12-11

Suggested to swap avbox and see if fault persists. Awaiting Desiray to swap the box and let us know. Offered to find an avbox if they don’t have one.

### Samuel Lopez, 2025-12-11

@Rajesh Budhabhatti  and @Cody Smisek we are waiting for Scott Whitney to provide us with a firmware engineer who can ‘check configs and other processor firmware to see if they can tell if anything is corrupted and why'.

I’ll check with him today if he can predict how long this will take.  If it’s too long, I’ll check back with the group to re-strategize.

### Samuel Lopez, 2025-12-16

Summary.
XCOMM logs on AC 966 reveal incorrect readings.  Vbatt, and servo voltages read maximum values as shown below.

| VBatt | VPayload | VServo1 | VServo2 | VServo3 |
| 55 | 16.55 | 16.55 | 16.55 | 16.55 |
| 55 | 16.55 | 16.55 | 16.55 | 16.55 |
| 55 | 16.55 | 16.55 | 16.55 | 16.55 |

Errant readings persist whether using a main battery or a DC power supply. 
However, when connected to the GCS and webpage instrumental panel, main battery readings are normal and consistent with power supply/battery as shown below.  This must be because those are coming from the nose cone, not the XCOMM measurements.
According to firmware team, checksum readings from the GCS are correct for Advanced Nav, so there’s no issue there.
- Fixed Wing AP 0x81B5
- XCOMM 0x2024

Culprit is highly suspected to be the XCOMM ADC pins and that microcontroller is faulty.

After talking with Desiray Johnston/Cameron Chapman, recommend replacing XCOMM and re-testing.  Old board will be kept by engineering for troubleshooting/analysis.

### Samuel Lopez, 2025-12-29

- As of December 29, 2025, XCOMM on AC 966 has been replaced.  According to Carson Buckley, there are no more ‘anomalous voltages’ and there are ‘no further issues’.   The aircraft itself is considered finished.
- The XCOMM board removed from AC 966 is to be investigated.
- Visual inspection with Sammy Lopez and Natalie Lusk reveals no solder bridges, solder balls, tomb stoned components, or any other anomalies.
- Check voltages of ADC pins.  If they are reflective of voltage divider, then the problem is the microcontroller.

### Samuel Lopez, 2026-01-05

2026-01-05
Standalone XCOMM board still read incorrect Vbatt, VPayload, and Vservo readings on the bench.  ADC pins measure normally with voltmeter. 
Conclusion:  The issue is almost certainly the microcontroller itself.

The microcontroller was re-flashed.  Voltage readings on xcomm webpage are now reading normally for Vbatt, Vpayload, etc.  
Cause is determined to be COTS PIC32 microcontroller.

### Samuel Lopez, 2026-01-14

XCOMM firmware was corrupted.  In the future, re-loading of firmware should be attempted before XCOMM board is removed from aircraft.  Quality is aware that XCOMM boards have systemic issues in production.  Final root cause is ultimately inconclusive.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20251124-222352.png | image | 80 | 2025-11-24 | listed only |
| image-20251204-180927.png | image | 147 | 2025-12-04 | listed only |
