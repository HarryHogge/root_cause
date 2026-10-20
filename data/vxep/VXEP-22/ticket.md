# VXEP-22: TPTR-55 Fuel Cell Failure Immediately after launch

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-08-23
- **Updated:** 2025-06-09
- **Resolved:** 2025-06-09
- **Reporter:** Allen Gardner
- **Assignee:** Cameron Chapman
- **Creator:** Allen Gardner
- **Links:** relates to ENG-3064 (TPTR-55 Fuel Cell Fault SN D4500249 /247 ); relates to VA-403 (TPTR-55 Fuel Cell Failure Immediately after launch - Identify C/CA); is blocked by VA-614 (Given unable to replicate, document possible causes and any CAs)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 510
- **Corrective Action:** Replacement and validation of proper performance.
- **Issue Status:** Investigation complete. Corrective Action Applied and Verified. Preparing for Return Shipment.
- **Root Cause:** Poor performance of Fuel Sensor or Solenoid.
- **Incident Type:** Mission Failure/Abort
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Aircraft 510 experienced a fuel cell failure immediately after launch. The aircraft was commanded to RTB and recovered without issue. The fault code was 19472, K_Fault_ReactorTemp_UnexpectedHigh. This included Fuel Cell S/N 249.
Note there was confusion when tickets created, @Greg Fryer decided this will carry the Aircraft 510 / Fuel Cell 249 issue.

## Plan

Perform Flight Data review to identify causes of failure in field. Operate Fuel Cell in attempt to replicate and diagnose behavior and report results. 
Complete investigation summary https://jenaero.sharepoint.com/:p:/r/sites/FlightSafety/Shared%20Documents/Incident%20Reports/Vehicle%20Investigation%20Example%20Template%20(1)-Cam%20Recommendations.pptx?d=wb492fba8a5c44e4fbe1741a920c24ce4&csf=1&web=1&e=cbnZ3E

## Comments (10)

### Allen Gardner, 2023-08-24

@Cameron Chapman Please create a task in VA to have someone perform the root cause investigation and create corrective action tasks.

### Cameron Chapman, 2023-09-19

@Tom Westrich @Sean Wendling do you have any more information on this incident (fuel cell SN, status, C/CA, etc)?

### Former user, 2023-09-26

@Tom Westrich @Greg Fryer @Sean Wendling Sean was never able to replicate this failure.  Recommend closing this TPTR.  [NOTE:  Legacy fuel cell (S/N 249) D450XR which will not be part of the Tiquila delivery.  We are moving to the new D450+ fuel cell.

### Greg Fryer, 2023-09-26

@Sean Wendling As part of making our incident response more robust, in instances we cannot replicate the issue, we done at least a first pass thorough a fishbone or similar tool. That way the likely potential causes could be identified. We then include that in an attached report, and close the issue. There is a special closure called “Bermuda Triangle” so we know which ones we never got to a root cause of.
Potential causes include the aircraft/ground station (e.g. is there anyplace the aircraft or ground station “interpret” data - or is this just a pass through?
Partially to make sure we are confident ourselves we’ve exhausted the angles, and also to show our customer that we are being robust.
We are keeping reports here (and there is also a blank template, though many slides get omitted if we can’t find the root cause): Incident Reports
@Former user FYI. We can still close the TIQUILA action if you are good with that, but we’ll want a bit of internal documentation.

### Sean Wendling, 2023-09-27

@Greg Fryer Hey Greg, thanks for the info! I wasn't familiar with this incident reporting process. I will review the structure and talk to our technician who investigated the RMA. I may have questions about the reporting process (and proper completion of the fishbone), would you be the best person to contact on this? I would like to echo your process to the best of my ability (or provide the correct information for your team so it may be documented) moving forward for FC related issues. Might be worth a quick teams meeting for me to understand the process so I can respond more quickly to tickets and incidents. 
Thanks everyone!

### Greg Fryer, 2023-09-27

@Sean Wendling Yes, absolutely. The best POCs are probably myself and @Cameron Chapman as a second. I was talking to Sam M. last night and we realized that he and Allen had not squared up all the new plans with you (you = all of Ann Arbor/Energy Systems).

### Cameron Chapman, 2023-11-07

@Sean Wendling do you have any updates on this TPTR, or recommendations of additional data to review/things to do. 
Here is a troubleshooting and fishbone template you could use https://jenaero.sharepoint.com/:p:/r/sites/FlightSafety/Shared%20Documents/Incident%20Reports/Vehicle%20Investigation%20Example%20Template%20(1)-Cam%20Recommendations.pptx?d=wb492fba8a5c44e4fbe1741a920c24ce4&csf=1&web=1&e=cbnZ3E  
https://jenaero.atlassian.net/wiki/spaces/EF/pages/89391105/Investigation+Reporting+and+Closure

### Sean Wendling, 2023-11-08

Hey Cameron, apologies for the delay on this. We are working through RMAs actively. I implemented CA on this unit, just waiting to validate the correction. I’ll update the ticket to match. Incident report is nearly complete as well. Should be able to upload it immediately after the corrective action has been confirmed.

### Greg Fryer, 2024-01-04

@Sean Wendling Reminder to come back and close this out (if it finished as expected). Be sure to close out the linked related task as well (either done or canceled if it turned out to be NA.)

### Sean Wendling, 2024-01-08

Hey @Greg Fryer , Report is attached. In the end we were able to identify a root cause and implement corrective action, so I cancelled VA614. I will make sure this unit is returned this week. It wont allow me to close this ticket for some reason, only gives me the option to reverse the progress or update the severity level. Appreciate the patience!

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [TPTR-55 Incident Investigation - 1.8.24.pptx](attachments/18259_TPTR-55%20Incident%20Investigation%20-%201.8.24.pptx.md) | pptx | 3646 | 2024-01-08 | converted |
