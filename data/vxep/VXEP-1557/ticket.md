# VXEP-1557: VXE 930 Main battery to avionics power chain led to emergency landing

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** Highest
- **Created:** 2025-10-20
- **Updated:** 2026-10-07
- **Reporter:** Zachary Mann
- **Assignee:** Stephan Johnson
- **Creator:** Michael Mohr
- **Labels:** Ann_Arbor, Hardware, MOLSON, RCCA, Weekly-incident-tracker
- **Links:** split from VXEP-1547 (VXE 930 One or more VTOL Sensor fail); relates to VXEP-1865 (VXE 930 - Vehicle broke orbit, wouldn’t take commands and behaved erratically.); relates to RMA-972 (VXE-930 RMA 260421-3); relates to VXEP-1987 (VXE 1016 Battery warning aircraft RTB)
- **Customer:** MOLSON
- **Vehicle Tail Number:** VXE-930
- **Vehicle Configuration:** Adv Nav
- **Incident Type:** Mission Failure/Abort
- **Severity:** 1 - Flight Critical

## Description

“Immediately after takeoff and transition to VTOL, we got a fault indicating battery is below 10%, rapidly degrading to below 5%, where we recovered the bird safely. We tested the battery upon landing - the main battery was 73% with all cells level. HLB was down to 30%. When tail 930 was lifting off, there was a weird stall about 10 ft off the ground. Temperature is 8 degrees Celsius, winds are 9 mph, gusting 15 mph.”
(Created separate ticket for this battery issue from initial VXEP-1547)

Testing out confluence page for investigation summaries (might be faster and easier to find than office docs on sharepoint). We can port to a ppt later if helpful. https://jenaero.atlassian.net/wiki/x/PoAfSg

## Plan

Issue seems most likely battery related. See bold below. 
- Michael Mohr do you know where the main battery involved in this incident is? It could be defective/the cause as well
- Customer has a large number of batteries and is unsure which was used. Advised to start logging this info.
- @Michael Mohr can you ask them to monitor for a repeat of this issue (especially monitor voltages during launch wizard run up and flag any extra low ones). We can compare to other logs to establish normal/faulty limits. 
- Similiar issue on a different aircraft 3-2229. @Michael Lindsay  will write up issue soon. Please request returning the battery to SLO for troubleshooting.
- SN not filled out in logs.
- Aircraft in HSV. Here are some things to check while there.
- Run forward power (launch wizard check ok). Monitor for voltage drops. -Done. No issues.
- Attach AAR and review data. Message EE team and discuss next steps. Consider inspecting avbox. -Done. No issues. It seems the wrong AAR was uploaded. Both xcl show baseline current. 
- [embedded image-20260826-190443.png]
[embedded image-20260826-190453.png]
- Wiggle test and inspect connectors between MB and avbox to see if any power issues. -Done. No issues.

## Issue Status

Summary here https://jenaero.atlassian.net/wiki/x/PoAfSg 
- Main battery voltage drops with fwd motor throttle. Suggests intermittent or high resistance connection in the main battery, current sensor, avbox, or harness from main battery to avionics box. 
[embedded image-20260708-213739.png]
- Aircraft in SLO. Ready to test. Unsure of battery locations. @Samuel Lopez are you able to inspect this as well. Seems like it will be similar checks as 512.
- @Scott Whitney do we monitor voltage during launch wizard checks and flag any issues? It seems like doing so may have caught the issue in this case. We can compare to other standard LW runs to establish a limit.

## Executive Summary

Awaiting testing for aircraft and battery, test starting Aug 17, 2026 Customer delayed providing proper information to determine root cause. Probable cause; Battery.

## Comments (14)

### Drew Hildreth, 2025-10-20

@Tom Westrich can you push this for a review please?
@Cameron Chapman FYSA in the event we need EE support.

### Scott Lovett, 2026-02-02

Investigate further to see if it is was an individual cell failure and related to HLB, or if this is a unique issue.

### Jackson Riley Curvin, 2026-02-16

[embedded image-20260216-203906.png]

### Jackson Riley Curvin, 2026-02-16

[embedded image-20260216-203935.png]

### Jackson Riley Curvin, 2026-02-16

[embedded image-20260216-204013.png]

### Jackson Riley Curvin, 2026-02-16

[embedded image-20260216-204045.png]

### Jackson Riley Curvin, 2026-02-16

[embedded image-20260216-204120.png]

### Scott Lovett, 2026-07-06

@Tom Westrich@Cameron Chapman  Looks like this aircraft is in SLO. How do we test this?

### Tom Westrich, 2026-07-06

@Scott Lovett , do you know what the SN of the HLB in this test is, and where the battery is located?

### Samuel Lopez, 2026-07-27

@Cameron Chapman @Scott Lovett this aircraft is not in SLO.  I think it’s in Huntsville.  Please re-assign.

### Cameron Chapman, 2026-07-27

@Samuel Lopez I think it is according to the RMA. Will message you and Lauren. https://jenaero.atlassian.net/browse/RMA-972

### Stephan Johnson, 2026-08-17

@Samuel Lopez I added an AAR from earlier today where we ran the motors through SUAV Launch Wizard. We had a different main battery and HLB, to eliminate any questions about the battery’s veracity.

### Stephan Johnson, 2026-08-31

@Cameron Chapman did you need any other testing for this?

### Cameron Chapman, 2026-08-31

@Stephan Johnson I lost access to our teams message, but I think this was the wrong AAR. Neither xcomm log had battery current matching a motor run. Can you please double check and upload the matching plots?

## Attachments (11)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T115_V930_251008_102001_pack.zip | archive | 2040 | 2025-10-20 | listed only |
| image-20251008-234740.png | image | 25 | 2025-10-20 | listed only |
| image-20260216-203906.png | image | 44 | 2026-02-16 | listed only |
| image-20260216-203935.png | image | 26 | 2026-02-16 | listed only |
| image-20260216-204013.png | image | 19 | 2026-02-16 | listed only |
| image-20260216-204045.png | image | 28 | 2026-02-16 | listed only |
| image-20260216-204120.png | image | 31 | 2026-02-16 | listed only |
| image-20260708-213739.png | image | 136 | 2026-07-08 | listed only |
| T115_V930_260817_063000_pack.zip | archive | 592 | 2026-08-17 | listed only |
| image-20260826-190443.png | image | 45 | 2026-08-26 | listed only |
| image-20260826-190453.png | image | 8 | 2026-08-26 | listed only |
