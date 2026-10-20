# VXEP-1913: VXE 1017 while conducting a launch the aircraft aborted due to a VTOL fault - lost GPS

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Confirmed
- **Priority:** Highest
- **Created:** 2026-06-11
- **Updated:** 2026-08-11
- **Resolved:** 2026-08-11
- **Reporter:** Michael Lindsay
- **Assignee:** Eric Brewer
- **Creator:** Michael Lindsay
- **Labels:** GS_Closed, MOLSON, RCCA, Software, Weekly-incident-tracker
- **Links:** relates to VXEP-1912 (VXE 1015 while conducting a launch the vehicle received a VTOL fault and aborted the takeoff)
- **Customer:** MOLSON
- **Vehicle Tail Number:** 1017
- **Vehicle Configuration:** VXE30 Adv Nav - Battery Config
- **Problem Type:** Discovered Issue
- **Plan:** Monitor
- **Severity:** 1 - Flight Critical

## Description

While conducting missions in support of exercise during the climb for launch they received a VTOL fault and lost GPS and aborted the launch proceed to land safely. 
Location: Shepherdsville KY

## Corrective Action

Aborts can occur sometimes, and this appears to be quite infrequent across the fleet.  Monitor behavior and evaluate if adjustments to thresholds may be required in the future.

## Issue Status

Thresholds were adjusted and subsequent launches did not abort.  Behavior will be monitored to see if it reoccurs.  This type of abort is quite rare across the fleet.

## Comments (8)

### Michael Lindsay, 2026-06-11

@Eric Brewer can you and a look at his as Dave is on PTO.  They had a VTOL fault on launch last nigh,t and the aircraft aborted. it happened on two different aircraft, @Scott Lovett

### Eric Brewer, 2026-06-12

@Michael Lindsay  @Scott Lovett it is aborting due to a position uncertainty just above the threshold.  The aircraft is tracking less satellites than I’d normally see, so wondering if it has to do with the location they are taking off.  Here is what the terrain around that site looks like, so lots of trees around:

[embedded image-20260612-140312.png]
[embedded image-20260612-140322.png]
Also, something that’s probably a little counterintuitive, but it might help to do a position nudge a little bit on the climb out, so just after the ‘pause’ on the climb.  This will allow the INS to converge out some uncertainties.
@David Grosher FYI.

### Michael Lindsay, 2026-06-15

@Eric Brewer @Drew Hildreth Eric I have uploaded the AAR for the flights this weekend in KT.  They are flying aircraft 1018 with the CW from 1017 that they did the thershold adjustments on.  They could not get into the VTOL webpage to open on the the CW for 1018.

### Michael Lindsay, 2026-06-15

Thresholds for the below have been updated from 15 to 30
[embedded image-20260616-005123.png]

### Eric Brewer, 2026-06-16

@Michael Lindsay thanks.  There was only one flight from this weekend included, the other AAR’s did not have any xcomm or vtol logs included.  The uncertainties stayed below 12' for the entire flight so this flight would have been successful without the new thresholds.

Here’s a summary of the attached logs.  If we get the logs from the other flights that would be great to review the data.


[embedded image-20260616-133545.png]

### Pat Wells, 2026-08-11

@Eric Brewer what is the CA for this?  It’s not stated above.

### Eric Brewer, 2026-08-11

@Pat Wells I updated above.  Let me know if you have questions.

### Pat Wells, 2026-08-11

Customer provided with work around. Monitoring for future occurences which may require further attention.

## Attachments (11)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T115_V1017_260611_161005_pack.zip | archive | 1065 | 2026-06-11 | listed only |
| image-20260612-140312.png | image | 2643 | 2026-06-12 | listed only |
| image-20260612-140322.png | image | 789 | 2026-06-12 | listed only |
| T115_V1018_260613_112337_pack.zip | archive | 265 | 2026-06-15 | listed only |
| T115_V1018_260613_154647_pack.zip | archive | 997 | 2026-06-15 | listed only |
| T115_V1018_260613_191223_pack.zip | archive | 933 | 2026-06-15 | listed only |
| T115_V1018_260613_220846_pack.zip | archive | 303 | 2026-06-15 | listed only |
| T115_V1018_260614_185211_pack.zip | archive | 977 | 2026-06-15 | listed only |
| T115_V1018_260614_213052_pack.zip | archive | 3237 | 2026-06-15 | listed only |
| image-20260616-005123.png | image | 70 | 2026-06-15 | listed only |
| image-20260616-133545.png | image | 41 | 2026-06-16 | listed only |
