# VXEP-1912: VXE 1015 while conducting a launch the vehicle received a VTOL fault and aborted the takeoff

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2026-06-11
- **Updated:** 2026-09-28
- **Resolved:** 2026-09-28
- **Reporter:** Michael Lindsay
- **Assignee:** Eric Brewer
- **Creator:** Michael Lindsay
- **Labels:** GS_Closed, RCCA, Software, Weekly-incident-tracker
- **Links:** relates to VXEP-1913 (VXE 1017 while conducting a launch the aircraft aborted due to a VTOL fault - lost GPS )
- **Customer:** MOLSON
- **Vehicle Tail Number:** 1015
- **Vehicle Configuration:** VXE30 Adv Nav, battery config
- **Problem Type:** Discovered Issue
- **Root Cause:** Aborted due to position uncertainty. 6.7.1 should improve performance
- **Severity:** 2 - Degraded Performance - No Workaround
- **Executive Summary:** Awaiting 6.7.1 update. Probable cause Software update.

## Description

While conducting missions in support of exercise during the climb for launch they received a VTOL fault and lost GPS and aborted the launch proceed to land safely. 
Location: Shepherdsville KY

## Comments (11)

### Michael Lindsay, 2026-06-11

@Eric Brewer this is the second aircraft that had the VTOL fault on launch.  @Scott Lovett

### Eric Brewer, 2026-06-12

@Michael Lindsay @Scott Lovett it is aborting due to a position uncertainty just above the threshold.  The aircraft is tracking less satellites than I’d normally see, so wondering if it has to do with the location they are taking off.  Here is what the terrain around that site looks like, so lots of trees around:

[embedded: image-20260612-140312.png]
[embedded: image-20260612-140322.png]
Also, something that’s probably a little counterintuitive, but it might help to do a position nudge a little bit on the climb out, so just after the ‘pause’ on the climb.  This will allow the INS to converge out some uncertainties.

### Michael Lindsay, 2026-06-15

The below thresholds have been changed from 15 to 30 in the VTOL webpage for aircraft 1015.  This aircraft has not been tested since the threshold change.
[embedded: image-20260616-004852.png]

### Michael Lindsay, 2026-06-30

testing flights to be conducted with the unit during the week July 6-10, 2026.  All AAR will be updated after these flights for review.

### Alexander Alan Arnold, 2026-08-07

How were the test flights on this aircraft?@Michael Lindsay

### Michael Lindsay, 2026-08-07

@Alexander Alan Arnold No they have not flown this aircraft as of yet, I believe that they are taking it out to Saskatoon in a couple weeks.  I will be with them so I will make sure that it gets flown.  I am happy to close this ticket as they have completed the threshold changes.

### Pat Wells, 2026-08-11

Awaiting CA 6.7.1 software update 8/11/2026

### Michael Lindsay, 2026-09-25

@Eric Brewer I have update this aircraft to 6.7.1, do you need anything additional in order to close this ticket?

### Eric Brewer, 2026-09-25

@Michael Lindsay no this should be good to close from my perspective.

### Michael Lindsay, 2026-09-28

Aircraft has been updated to software version 6.7.1, and new issues will be captured in a new Jira ticket.

### Michael Lindsay, 2026-09-28

Software has been updated to 6.7.1

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T115_V1015_260611_181130_pack.zip | archive | 1078 | 2026-06-11 | listed only |
| image-20260612-140312.png | image | 2643 | 2026-06-12 | listed only |
| image-20260612-140322.png | image | 789 | 2026-06-12 | listed only |
| image-20260616-004852.png | image | 70 | 2026-06-15 | listed only |
