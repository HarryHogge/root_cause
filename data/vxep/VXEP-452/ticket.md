# VXEP-452: VXE 488 vehicle is resetting during pre-flight

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2024-06-28
- **Updated:** 2026-03-02
- **Resolved:** 2024-12-06
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** Marine_3rd_LAR, Weekly-incident-tracker
- **Customer:** Marine_3rd_LAR
- **Vehicle Tail Number:** 488
- **Root Cause:** None, did not receive aircraft.
- **Incident Type:** Mission Failure/Abort
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Report from operator: 
Received multiple vehicle reset errors during pre-flight. 

AAR Attached

## Comments (7)

### Pat Wells, 2024-06-28

@David Grosher FYSA

### David Grosher, 2024-06-28

@Kurt Burian This looks like the bug you mentioned this morning. 
I see a crash dump in the T95_VT488_240610_095907_vt240610.txt file.  Which led me to: 

[embedded: image-20240628-205312.png]
Looking at the crash dump it seems that the system hadn’t initialized, so maybe it was a forced crash dump given the history in the log before that. Or perhaps it did reset but the fileI/O had not been up in the previous power cycle.

### Pat Wells, 2024-07-16

@Kurt Burian @David Grosher Any updates on this one?
Customer is asking if aircraft is flightworthy or not?  They have an upcoming operation that requires support.

### David Grosher, 2024-07-16

@Pat Wells Kurt is out for PTO this week.  He can get you a response next week. 
This error will occur during initialization. The data shows one incident, but the description references multiple events. If that is the case then additional data would be beneficial. I would also be inclined to recommend RMA in that case.

### Pat Wells, 2024-07-17

@David Grosher  requested that customer return aircraft on RMA for further evaluation.

@Sean Odell FYSA

### David Grosher, 2024-12-05

@Pat Wells Did we receive this vehicle?

### Pat Wells, 2024-12-06

@David Grosher the customer never returned the aircraft. I suggest we close this with no action.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V488_240610_095907_pack.zip | archive | 1072 | 2024-06-28 | listed only |
| [flightdataloggcs-6.2.9-0.csv](attachments/21314_flightdataloggcs-6.2.9-0.csv.md) | csv | 27 | 2024-06-28 | converted |
| image-20240628-205312.png | image | 24 | 2024-06-28 | listed only |
