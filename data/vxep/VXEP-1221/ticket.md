# VXEP-1221: VXE 722 AV Unresponsive during descent

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-04-22
- **Updated:** 2026-09-09
- **Resolved:** 2025-10-28
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** Crash, PMA263, Training, Weekly-incident-tracker
- **Links:** relates to RMA-672 (VXE-722 RMA 250428-1); relates to FS2-3566 (Evaluate the State Machine in the VTOL AP that is left in Attitude control. Suggest a fix that lets it progress to Position Hold.)
- **Customer:** PMA263
- **Vehicle Tail Number:** VXE 722
- **Vehicle Configuration:** VXE 30, will update config once data is provided
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

"When commanded to enter the landing pattern the AV went to IP5 and began to VTOL from 1,200ft. After the landing began, the AV became unresponsive and started drifting out of the LZ while descending. It eventually crashed into trees about 800m away from the landing zone. The VTOL system fault code displayed was "Climb abort, lift system fault."
 
The operator attempted to Command the AV to land immediately but it did not respond. After it began to drift, the operator attempted to pause the landing and the AV did not respond to that either.
 
AC 722 which is updated to 6.3.4 and cleared to fly.

## Corrective Action

Block LI command when in the landing sequence (IP4 forward) It is already landing. 
Evaluate the State Machine in the VTOL AP that is left in Attitude control. Suggest a fix that lets it progress to Position Hold.  There are a lot of corner cases with the strategy of limiting LI and it has led to this bug needing to be fixed 3 separate times.

## Issue Status

SharePoint Folder Here VXEP-1221 VXE722

Removed FW avionics enclosure to expedite log download. Nose has damage and was not obvious if any harnesses were affected. Did not notice any RTV on enclosure connectors, asked Kyle E if there has been a change with this.

## Root Cause

Operator Error - Commanded Vehicle to VTOL at altitude.  v6.4 will have an interlock warning to help prevent this from occurring again. 
Bug- The unresponsive behavior came from the two land immediately commands during the landing sequence, leaving the VTOL controller in attitude control mode. This is a known issue.

## Comments (16)

### Alexander Alan Arnold, 2025-04-22

We are currently aware of an incident involving VXE 722, I will update the ticket once data is provided, aircraft will potentially be enroute to SLO for investigation by the end of this week.  @David Grosher @Greg Fryer

### Ruysser Gabler, 2025-04-23

@David Grosher  The drifting part sounds very close to the bug we found in regression testing a while back. where once its in VTOL landing and you use land immediately it will drift without the ability to do anything at all

### David Grosher, 2025-04-23

@Ruysser Gabler Good point, but I thought you could still nudge it in that case, is that not correct?

### Ruysser Gabler, 2025-04-23

Here is that ticket: https://jenaero.atlassian.net/browse/GCSS-333 

We were unable to nudge until like 20 ft AGL or so
@David Grosher

### Alexander Alan Arnold, 2025-04-23

@David Grosher I am adding the data we received but it is incomplete they stated after it crashed the CW connector was damaged and did not want to apply power.  
[embedded: image-20250423-183943.png]
in the debug log we see change active waypoint, Mission Primary LZ 4. 
We are assuming this is the operator telling the aircraft to go to IP4 instead of entering a full pattern.

### David Grosher, 2025-04-23

@Alexander Alan Arnold I agree with your assessment, we should verify with the XCOMM event log once it is received from the hardware.  They may have fallen into the other bug that Ruysser mentioned in their panic after the transition at altitude.  This would be characterized by a LI while the lift system was already active.

### Alexander Alan Arnold, 2025-04-23

I am also curious if the low battery could've caused issues for them, there is a low vehicle battery message as well. I believe that the rest of the data will have to be pulled off the aircraft once it arrives in SLO. Once we have an update I will provide it here. @David Grosher

### David Grosher, 2025-04-23

@Alexander Alan Arnold Possibly but that would cause an RTB, which would take them to IP1. But we can verify that with testing, we will prioritize this once we get data to analyze from the VTOL and XCOMM.

### Alexander Alan Arnold, 2025-04-30

@David Grosher 722 is in the building, once intake is complete, I will have the RMA team move the aircraft to Engineering.

### David Grosher, 2025-04-30

@Cameron Chapman We will need the EE team to pull data from this bird.

### Rodney Linch, 2025-04-30

@Cameron Chapman - the two cases were dropped off in the Engineering area.  Intake forma and pictures may be found in RMA ticket https://jenaero.atlassian.net/browse/RMA-672

### Cody Smisek, 2025-04-30

FWAP & VTOL log files pulled. Stored in link listed in issue status. 
@Cameron Chapman @David Grosher

### Cody Smisek, 2025-04-30

[embedded: image-20250430-220627.png]

### David Grosher, 2025-04-30

@Alexander Alan Arnold Looking at the XCOMM event log there is: “[14:50:00.659 10381.659] GoTo m,w 1  3”, which corroborates your assessment. We should align the two logs to ensure it is consistent with your assessment of the GCS log. Operator error would be the primary error here.  Note: this issue is resolved in 6.4 with an operator interlock that prevents this from inadvertently happening at AGLs that exceed the batter capacity. 
@Levi Purdy Can you see if this incident suffered from the LI bug that you just delivered a fix for (expected to be included in v6.6).  Based on the witness description it sounds like the vehicle may have been left in attitude control and drifted with the wind while it did its descent. This would be a secondary failure that would explain the perceived non-responsiveness. A slide or two explaining your conclusion can be included in Alex’s report.

### Levi Purdy, 2025-05-09

I am planning on syncing the data, and will produce some more conclusive graphs, just will be a bit of a longer lift. 
 
But with a cursory look I can confirm that multiple LI commands were issued, and the conditions to cause the state bug were there. (Can't confirm vtol did it without time sinc, but all the conditions for it to do it were there.)

[embedded: image (1).png]

What I am looking at is the MESSAGE_VTOL2 <prev> <next>. That is an alert that is generated when the main state variable changes in fwap for vtol stuff. 400s are land abort stuff. It should only ever increase. When I was recreating the bug before the key property was it running through the sequence again. 
 
From this message I can confirm that the conditions for the dual LI bug were there.

### Levi Purdy, 2025-05-14

I got the tools together to sync the data between vtol and FDR, so we can overlay the states and events. 

This is the visualization graph. It doesn’t capture all the state transition details because it is restricted to the update rate of the sampled logs. 
[embedded: image-20250514-235219.png]
Nonetheless, it does show VTOL going into Attitude mode while the FWAP is going into LI mode (states 400 to 500). 

This is the timeline graph: It shows the characteristic decrease of VTOL state characteristic of dual LI requests, but interestingly the dual requests likely didn’t make it to the log. 
[embedded: image-20250515-003229.png]
We have the sequence in XCEVLOG

There was a LI request and then quickly after an LI abort requested. The system successfully jumped out of the state down to 100, so this probably worked correctly. 

There were high rate logs right in the region we would expect to see the ‘first’ LI request, so likely it wasn’t recorded, but the state transitions from 401 to 407 still happened before the ‘second’ LI request hit and put the system into an error state. 
[embedded: image-20250515-004916.png]

## Attachments (16)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [T95_V722_250412_081920_debuglog.txt](attachments/28449_T95_V722_250412_081920_debuglog.txt.md) | text | 502 | 2025-04-23 | converted |
| [T95_V722_250412_081920_event.txt](attachments/28450_T95_V722_250412_081920_event.txt.md) | text | 98 | 2025-04-23 | converted |
| [T95_V722_250412_081920_fuelcelllog.csv](attachments/28452_T95_V722_250412_081920_fuelcelllog.csv.md) | csv | 0 | 2025-04-23 | converted |
| [T95_V722_250412_081920_gain.apx.txt](attachments/28454_T95_V722_250412_081920_gain.apx.txt.md) | text | 41 | 2025-04-23 | converted |
| [T95_V722_250412_081920_log.csv](attachments/28453_T95_V722_250412_081920_log.csv.md) | csv | 18937 | 2025-04-23 | converted |
| [T95_V722_250412_081920_notes.txt](attachments/28448_T95_V722_250412_081920_notes.txt.md) | text | 0 | 2025-04-23 | converted |
| T95_V722_250412_081920_trail.trl | other | 377 | 2025-04-23 | listed only |
| image-20250423-183943.png | image | 46 | 2025-04-23 | listed only |
| image-20250430-220627.png | image | 4 | 2025-04-30 | listed only |
| image (1).png | image | 11 | 2025-05-09 | listed only |
| image-20250514-235219.png | image | 81 | 2025-05-14 | listed only |
| image-20250515-003229.png | image | 49 | 2025-05-14 | listed only |
| image-20250515-004916.png | image | 583 | 2025-05-14 | listed only |
| timeline_722.html | html | 71 | 2025-05-14 | no text found |
| visualization_722.html | html | 1657 | 2025-05-14 | no text found |
| 10bc5dfc-7c62-4a7a-b5fd-01438a2b0176.png | image | 12 | 2025-08-05 | listed only |
