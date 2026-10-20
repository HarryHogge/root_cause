# VXEP-985: VXE 560 Main battery connector was extremely hot after software upgrades

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-02-06
- **Updated:** 2026-09-09
- **Resolved:** 2026-03-25
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Steve Gonzales
- **Creator:** Alexander Alan Arnold
- **Labels:** Hardware, No_crash, PMA263, Weekly-incident-tracker
- **Links:** relates to RMA-467 (VXE-560 PMA263 250116-3); relates to VXEP-540 (Recent AS150 Connectors causing intermittency and difficulty to connect and disconnect correctly and safely (AS150 Socket Issues)); relates to VXEP-999 (VXE 598 with VXE 596 Center Wing. Lost connection to VTOL AP and ADB and crashed. )
- **Customer:** PMA263
- **Vehicle Tail Number:** VXE 560
- **Vehicle Configuration:** FSK power connector, then swapped to main battery power.
- **Root Cause:** This issue may be caused by inconsistent socket contacts
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

“Mike Mohr worked on by swapping SD cards in fuse and CW. He also uncovered 'excessive heat on main battery connector and noted arcing issues.”

During an SD card rework at the customer site, we noticed the main battery connector was extremely hot to the touch. We were using the power cable provided in the FSK. After disconnecting and letting it cool, we then swapped to battery power and noticed arcing in the connector while plugging in the battery. 
Incident Report Page: Flight Safety - VXEP-985 VXE 560 Main battery connector was extremely hot after software upgrades - All Documents

## Plan

- Assigning to @Steve Gonzales to review current status, ppt, and update plan. FYI @Pat Wells
- Fuse and CW located next to Adrian’s bench
- Measure anti-spark resistance on main battery connector
- Test harness and/or aircraft to identify potential causes.
- Acquire Travelers and compare aging/mating factor cycle
- Obtain Logs if needed
- This issue may be caused by inconsistent socket contacts. Do you have records of what battery was used when this happened? We should also record when and where the battery and internal harnesses were built.
- Held initial TS meeting 3/17/25.  Inventory request for 30 random connectors to test initial R.  3/17/25.  Plan to test R week ending 3/21/25.  Completed testing, all withing R spec.
- 4/1/25 Has not moved forward; no resources allocated.

## Issue Status

Main battery connector anti-spark resistance measured at 18 ohms, 3 times the expected resistance
From Laszlo’s findings there is no obvious indication of any short, intermittent connection, or other anomalies included the booms as well. The test shown no other indication or reason for heating up the power connector than the battery connection was not engaged fully, and the power was fed through the 6Ohm inrush limiting resistor and from the lengthy over current caused the heat-up of that resistor and resulted the permanent increase of resistance.
Harness pin diameters were measured: anti-spark measured at 0.275in and non antispark measured at 0.264in
Logs have been pulled and for logs XCL00000-XCL00005 there is a lower-than-expected voltage reading for apVbatt at around 19V, the 8-9 volts missing from the expected 28-volt reading is being seen by the anti-spark resistance and with a current of 1 A this leads to about 8-9 Watts of power being dissipated by this 6 ohm anti-resistor leading to heat buildup
Travelers have been acquired but the harness was outsourced so no traveler is present. Harness info below:
PN: 107-102189-1
SN: 0141 
This harness was outsourced from Compass Systems back in 2023, there is another incident [VXEP-999] VXE 598 with VXE 596 Center Wing. Lost connection to VTOL AP and ADB and crashed. - Jira that also reports an issue with the main battery connector with SN: 0157 that is also found in the same invoice. There may be more defective harnesses in this batch. The invoice is found in the attachments below.
Per Mike Mohr: FSK power harness used in this incident was pulled out of one of the FSKs that the unit had on site while doing the SD card swaps. The FSK power cable is not on hand so socket diameter measurements cannot be performed.

## Comments (23)

### Alexander Alan Arnold, 2025-02-06

@Rodney Linch Please have this delivered to engineering since there is a problem ticket associated now.

### Greg Fryer, 2025-02-06

@Alexander Alan Arnold @Rodney Linch Is this an RMA (meaning after this did it get come back)? Or is this still in the field? Was going to recommend RMA immediately, as overheating power connectors are a flight safety risk/issue.
Edit: Just saw the linked RMA! Did we get the plane back already?
@Cameron Chapman Moving to you, but maybe Laszlo could look at the battery connections?

### Alexander Alan Arnold, 2025-02-06

@Greg Fryer this aircraft is in the building. The RMA ticket has the bird being labeled as delivered to engineering.

### Cameron Chapman, 2025-02-11

@Adrian Garcia and @Giovanni Gonzalez can you please investigate this today. I would start by measuring the antispark contact for the resistor portion and regular contact impedance.

### Cameron Chapman, 2025-02-12

@Alexander Alan Arnold @Michael Mohr there seems to be a high chance that this issue was caused by inconsistent socket contacts. Do you have records of what battery was used when this happened? We should quarantine and test socket diameters it if so. We should also record when and where the battery and internal harnesses were built. 

See https://jenaero.atlassian.net/browse/VXEP-540 
@Brad Crampton @Steve Stack @Pat Wells @Sloan Payne was there ever containment of batteries in the field, or did we think they were not affected by this batch.

### Alexander Alan Arnold, 2025-02-12

Issue was first noticed when we plugged in the power supply cable in the FSK. I do not have a record of what battery was used after this. @Cameron Chapman

### Pat Wells, 2025-02-12

@Cameron Chapman I’m not aware of any containment of batteries in the field.  I wasn’t involved in that investigation.

### Brad Crampton, 2025-02-12

It is nearly certain that some defective batteries were released particularly early on when the connector fit problem was discovered. It would be very helpful if we could get a serial number for this battery.

### Alexander Alan Arnold, 2025-02-12

@Brad Crampton unfortunately this was performed at the customer site. I do not have the number, and I asked the customer if they kept a log of what batteries were provided for testing and they do not. 

We will be sure to include battery SN in our notes from visits from now on. @Brad Crampton

### Cameron Chapman, 2025-02-12

@Alexander Alan Arnold  do you have a log of the power supply FSK cable that was used? We could inspect that cable for this issue as well, to see if it supports the hypothesis. Considering it happened with a battery and power supply, there is a higher chance the problem is on the harness or aircraft side.

### Cameron Chapman, 2025-02-12

@Laszlo Juhasz @Adrian Garcia plan updated. Can you please test the power cable and see if you can identify a cause?

### Laszlo Juhasz, 2025-02-18

I’ve done a series of inspection and testing to ensure there is no obvious indication of any short, intermittent connection, or other anomalies included the booms as well. The test shown no other indication or reason for heating up the power connector than the battery connection was not engaged fully, and the power was fed through the 6Ohm inrush limiting resistor and from the lengthy over current caused the heat-up of that resistor and resulted the permanent increase of resistance. It would be more helpful to have the exact battery in hands was used during the incident.

### Adrian Garcia, 2025-02-27

Assigning to @Giovanni Gonzalez in the meantime while I help with LEMB testing. Can you pull the logs off the XCOMM and plot APVbatt and APIbatt against each other. Measure the AS150 on the Fuse Power Harness with calipers, or something better if you can come up with a more reliable/consistent way. Anti-Spark should be 0.275in and the non anti-spark should be 0.28. Talk to @Laszlo Juhasz about his findings and begin to fill out report. Here is the template - https://jenaero-my.sharepoint.com/:p:/r/personal/dgrosher_edgeautonomy_io/_layouts/15/Doc.aspx?sourcedoc=%7BEBE29A35-D378-4179-9853-BB2427A86052%7D&file=Vehicle%20Investigation%20Template.pptx&action=edit&mobileredirect=true  - please add it to the sharepoint. 

FYSA @Cameron Chapman @David Grosher

### Pat Wells, 2025-03-17

@Steve Gonzales is the team finished with aircraft portion of the investigation so that we can repair and return it to the customer.

### Steve Gonzales, 2025-03-17

@Pat Wells We need at least 5 more businesses days to continue the troubleshooting process pls.

### Cameron Chapman, 2025-03-18

@Steve Gonzales are you able to prioritize figuring out which parts can be kept for investigation vs which can be returned?

### Giovanni Gonzalez, 2025-03-20

This main battery connector, PN: 107-102189-1, was outsourced from Compass Systems back in 2023. The serial number for this harness is SN: 0141 and is found in the attached invoice below. Incident [VXEP-999] VXE 598 with VXE 596 Center Wing. Lost connection to VTOL AP and ADB and crashed. - Jira also reports an issue with the main battery connector with SN: 0157, this connector was also outsourced and is in the same invoice below. This batch may have other defective connectors.
[embedded: Invoice for PO-220526-11 INV-00001348 (5599-0744-011).pdf]
@Cameron Chapman @Steve Gonzales

### Cameron Chapman, 2025-03-21

@Giovanni Gonzalez  can you please add the location of the suspected parts to the status field above? We should try to perform a socket diameter measurement if feasible. @Steve Gonzales

### Alexander Alan Arnold, 2025-04-08

@Steve Gonzales Referencing your comment from march 17th asking for 5 more business days.  Is the aircraft ready to be returned to RMA so repairs can be scheduled and returned to customer?

### Alexander Alan Arnold, 2025-04-15

@Steve Gonzales @Cameron Chapman It seems like the connector is the root cause, this was not involved in a flight incident so we can we potentially send this back to RMA and schedule a replacement for the harness and close this one out 

FYSA @Pat Wells

### Steve Gonzales, 2025-04-15

@Alexander Alan Arnold Agreed.  I will send this vehicle to you today.

### Steve Gonzales, 2025-04-15

@Giovanni Gonzalez please gather vehicle 560 and give to Alexander in RMA across from shipping today. thank you.

### Alexander Alan Arnold, 2025-04-15

@Lauren Velasquez @Rodney Linch Please work with @Giovanni Gonzalez to return this aircraft to rma and schedule the repair the fuselage @Steve Gonzales I am in the huntsville office not SLO

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Invoice for PO-220526-11 INV-00001348 (5599-0744-011).pdf](attachments/27429_Invoice%20for%20PO-220526-11%20INV-00001348%20(5599-0744-011).pdf.md) | pdf | 501 | 2025-03-20 | converted |
| VXE 560 apVbatt & apIbatt XCL00000.png | image | 140 | 2025-03-21 | listed only |
| VXE 560 apVbatt & apIbatt XCL00001.png | image | 138 | 2025-03-21 | listed only |
