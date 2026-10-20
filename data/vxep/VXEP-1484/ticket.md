# VXEP-1484: VXE 697 - Incorrect Baro data leading to aborted launch

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2025-08-21
- **Updated:** 2026-08-10
- **Resolved:** 2026-08-10
- **Reporter:** Michael Mohr
- **Assignee:** Drew Hildreth
- **Creator:** Michael Mohr
- **Labels:** Investigating, TIQUILA
- **Links:** relates to RMA-792 (VXE-697 250820-1)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 697
- **Issue Status:** Inconclusive.  Faulty component highly suspected. Unable to confirm since the removed electronics were scrapped.
- **Severity:** 1 - Flight Critical

## Description

Abnormal launch behavior

## Corrective Action

After consulting Quality, there is not enough VTOL failures either in production or due to RMAs to escalate corrective measures at this time.  Monitor VTOL performance through 2026.  Otherwise, this may be a one-off event.
- @Samuel Lopez @Drew Hildreth please link to investigation hardware tracking improvements and ensure that not scrapping equipment once removed if needed for investigation is added to that process and communicated.

## Plan

- EE inspection of baro sensor on VTOL board.
- Run through electronics shop test/calibration to determine if it can be recreated. Evaluate process updates to catch such issues in the future. @Daniel Ceja may be able to support.
- Further log analysis to see how long the issue was happening/contributing factors (vibe, temp, etc).
- Evaluation of trace data to determine if firmware could have prevented the data from being collected and defaulting it to 0.

## Root Cause

Inconclusive.  Faulty component highly suspected. Unable to confirm since the removed electronics were scrapped. 

While corrupted firmware or a faulty microcontroller cannot be ruled out, only the pressure data was misreported; airspeed and density values were secondary calculations derived from the barometric measurement. This makes a barometer component failure the most likely root cause. Alternatively, the issue may have originated from passive components associated with the barometer interface, such as the supply-voltage resistor (R97) or the SCLK and SDI series resistors (R98 and R99).

## Comments (19)

### David Grosher, 2025-08-21

The baro pressure from the internal sensor goes to zero and then derivative data is not usable. It is likely this fed into the controller leading to low climb rate abort. This does not appear to be related to a poor airspeed calibration, error signatures in related bad airspeed calibration issues did not show similar data. 
VTOL Event log has extensive baro jump warnings.
[embedded image-20250821-165543.png]

[21:20:31.618 1566.618] DebugMsg Climb abort, low climb rate

### David Grosher, 2025-08-21

Error logic in SensorBaro identified a consistent and persistent issue with the baro prior to it being flagged bad and set to zero in SensorBaro.cpp. The error did show significant variation in the value over time. 
[embedded image-20250821-171809.png]
Need to look at a mechanism to recognize the error state and then inform the operator of the issue (WCA). 
Also we need to throttle the message in the event log. 
A quick check of the Trace tables does not indicate a FW issue.

### Lauren Velasquez, 2025-09-03

@David Grosher This AC has arrived in the RMA area. 
@Michael Mohr FYSA

### David Grosher, 2025-09-03

@Lauren Velasquez Ok, you would need to check with QA, the Electrical engineering team and/or the EE shop on whether that sensor can be repaired on the VTOL board. if not, you will need a new VTOL AP board. @Connor Peebles @Cameron Chapman FYSA.

### Cameron Chapman, 2025-09-04

@David Grosher we can take a look at if this and see if it reworkable and deliverable after. @Connor Peebles can you provide a recommendation or delegate to someone to evaluate? 
How easy is it to plot data going back to pre-SCO flights? Do you have any indication on when this issue started? I am wondering if we could have caught it before shipment.

### Connor Peebles, 2025-09-09

@David Grosher @Cameron Chapman  Is this the Baro from the Air Data Board? Firstly, I would recommend replacing the ADP if so. 

Secondly on Cameron’s point about catching it before shipment; on a previous RMA [ENG-2982] VXE 339 Mishap. Abnormal readings, behavior, and slow descent led to HLB empty and crash - Jira We saw that intermittent solder joints would only cause erroneous data on the ADB baro when the board is cooled down. If this incident has similar reasoning, then if we had flags for during the ADB calibration in the eshop for when the calibration exceeded the expected value (in + or -) checkmarks, it may have been caught. Currently the ADB calibration program only checks that the calibration has achieved the expected values.

### Connor Peebles, 2025-09-09

If it is the VTOL AP, which it seems to be, then it is most cost effective to replace the VTOL AP. As far as I know, the Barometer on the VTOL is not calibrated in the Eshop. @David Grosher

### David Grosher, 2025-09-09

@Connor Peebles This data comes from the barometer on the VTOL board, not the ADP. I’m not sure why this baro value is used instead of the ADP, it is a legacy artifact.

### Cameron Chapman, 2025-09-11

@Connor Peebles some ideas for CA.
- If the VTOL baro issues can lead to aborted launches, it seems like we should do one of the following
- test and/or calibrate at some point during production
- AP ignore data if not useful.
- For the ADB issue below, does the ADB calibration happen in a temp chamber currently? Would it be easy to see erroneous data, or would we need FW updates to read and flag it?  I think we should open and link a separate issue to track this if not related to this incident.

### Connor Peebles, 2025-09-11

@Cameron Chapman 
- Here is the extent of the VTOL AP Baro testing in the eshop:
[embedded image-20250911-185353.png]
- Here was the suggestion from that ADB incident, put into a Jira ticket, then summarily cancelled: [VA-248] Review/ evaluate addition of anomalous value flags during initial ADB calibration and assembly - Jira. I think it would be relatively easy to include “IF BARO SEE -39999 DegreesC, THEN BAD” into the calibration code, but I am not a software person.

### David Grosher, 2025-12-11

@Scott Whitney Can you take the CA #1 and turn it into an epic for the baro sensor. 
@Greg Fryer It seems that there were some production calibration procedures that was being worked by Cameron, yourself and John C. I just wanted to follow up on them to ensure they are pushed over the line.

### Greg Fryer, 2025-12-11

@Cameron Chapman or @Nigel Goodison Can you make note of the listed CA? Determine if it’s still viable, and if so put it onto aproject list? If it is significant, LMK and I will escalate to the SEIT list.

### Cameron Chapman, 2025-12-11

@Greg Fryer I think we jumped ahead on investigation. Below was just based on data review. We have not inspected the equipment or recreated it. I think we should start there. Plan updated.

### Samuel Lopez, 2026-01-16

The VTOL AP and INT boards were replaced to verify that the issue was isolated to those assemblies. After the VTOL boards were replaced, the system underwent was fully tested using the Onboard Ground Control Station, after which the aircraft completed two successful flights. Barometer readings are now within normal limits.
The original VTOL boards could not be located despite an extensive search, preventing further root-cause analysis. Corrective actions will be implemented to strengthen configuration control and prevent similar gaps in the future.
While corrupted firmware or a faulty microcontroller cannot be ruled out, only the pressure data was misreported; airspeed and density values were secondary calculations derived from the barometric measurement. This makes a barometer component failure the most likely root cause. Alternatively, the issue may have originated from passive components associated with the barometer interface, such as the supply-voltage resistor (R97) or the SCLK and SDI series resistors (R98 and R99).

### Cameron Chapman, 2026-01-16

@Samuel Lopez this is good logic, but it belongs/lasts longer in the cause field more than comments. Please update that field.

### Samuel Lopez, 2026-01-20

@Cameron Chapman  Moved to RC and modified CA as well.

### Scott Lovett, 2026-02-02

Original VTOL boards can not be located after an extensive search, so further analysis cannot be performed.

### Drew Hildreth, 2026-03-25

@Scott Lovett I think we can start a report on this one.

### Drew Hildreth, 2026-08-10

Baro fix included in 6.7.1

## Attachments (10)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V697_20250819T212148Z.zip | archive | 11534 | 2025-08-21 | listed only |
| [Contingency A.json](attachments/31646_Contingency%20A.json.md) | text | 2 | 2025-08-21 | converted |
| [Contingency A_2.json](attachments/31650_Contingency%20A_2.json.md) | text | 2 | 2025-08-21 | converted |
| [Flight.json](attachments/31648_Flight.json.md) | text | 5 | 2025-08-21 | converted |
| [PersistedLandingPatterns.json](attachments/31647_PersistedLandingPatterns.json.md) | text | 3 | 2025-08-21 | converted |
| [Re_ Enterprise OR Failed Launch Data .msg](attachments/31651_Re_%20Enterprise%20OR%20Failed%20Launch%20Data%20.msg.md) | msg | 178 | 2025-08-21 | converted |
| [Test Route 1.json](attachments/31649_Test%20Route%201.json.md) | text | 3 | 2025-08-21 | converted |
| image-20250821-165543.png | image | 66 | 2025-08-21 | listed only |
| image-20250821-171809.png | image | 9 | 2025-08-21 | listed only |
| image-20250911-185353.png | image | 79 | 2025-09-11 | listed only |
