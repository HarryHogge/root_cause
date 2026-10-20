# VXEP-1568: VXE-818 Lift System didn't disengage - Crash - CAN bus error

- **Issue type:** Incident (8D)
- **Status:** D6 - Verifying Corrective Actions Are Complete
- **Priority:** High
- **Created:** 2025-10-23
- **Updated:** 2026-10-01
- **Reporter:** Jackson Riley Curvin
- **Assignee:** Stephen Peters
- **Creator:** Jackson Riley Curvin
- **Labels:** 25thID, GS_Closed, LRR, Software, Weekly-incident-tracker
- **Links:** relates to VXEP-416 (VXE 539 Failure to launch); relates to FS2-2320 (Make XComm->VTOL SAFE On/Off messages require acknowledgements); relates to VXEP-1569 (VXE-828 Launch Abort - Air Data Fault - CAN bus error); relates to XKIT-5172 (B40 CAN Issues Investigation)
- **Customer:** 25thID, LRR
- **Vehicle Tail Number:** VXE-818
- **Vehicle Configuration:** Block 35X LEMB
- **Problem Type:** Other (explain in description)
- **Plan:** Investigation seems complete. See CA field for actions
- **Issue Status:** Investigation seems complete. See CA field for actions
- **Severity:** 1 - Flight Critical
- **Executive Summary:** CA created awaiting Epic investigation to be complete. Probable cause; Hardware Issue.

## Description

AC took off and climbed in VTOL normally, 10mph wind or so. AC then started transition to fixed wing normally. AC reached "normal point" to turn off VTOL motors but the motors never turned off. The AC continued to fly towards is mission point while still spinning the VTOL motors. AC Descended behind the tree line and out of sight. 

Investigation Slides here. 
Adv nav

## Corrective Action

- Containment and design improvement actions for LEMB. See here for status https://jenaero.atlassian.net/browse/VXEP-1880

Potential FW improvements: @Scott Whitney can you please create/link tickets for these improvements, or indicate if they won’t be implemented/tracked. 
- [DONE] Add additional diagnostics monitoring of the CAN health​
- [DONE] Launch Abort if CAN health is degraded.​
- [DONE] More efficient communication across CAN bus.

## Root Cause

Damage to LEMB circuits due to transients created noise on the CAN bus, which led to dropped communicaiton. 
- Vehicle investigation https://jenaero.sharepoint.com/:p:/r/sites/FlightSafety/_layouts/15/Doc.aspx?sourcedoc=%7BCC45616B-191B-4D74-A492-B4394C3879F9%7D&file=V818IncidentInvestigation.pptx&action=edit&mobileredirect=true
- LEMB investigation: https://jenaero.sharepoint.com/:p:/r/sites/FlightSafety/_layouts/15/Doc.aspx?sourcedoc=%7BCC45616B-191B-4D74-A492-B4394C3879F9%7D&file=V818IncidentInvestigation.pptx&action=edit&mobileredirect=true

## Comments (14)

### Jackson Riley Curvin, 2025-10-23

@David Grosher

### David Grosher, 2025-10-23

@Jackson Riley Curvin 

Initial Finding is that VTOL was put into RC mode just prior to completing launch. RC mode is supposed to be limited to Engineering. Looking into it further.  Some plots from @Eric Brewer added. RC commands were received. Current suspicion is that U-drive was intended. 


[embedded image-20251024-002916.png]
[embedded image-20251024-002925.png]


[13:05:17.451 920.451] rc activated
[13:05:17.453 920.453] global mode change was, is: FLIGHT_MODE_AUTO FLIGHT_MODE_RC

### Ruysser Gabler, 2025-10-24

@Eric Brewer @David Grosher during launch position nudge was activated but not used. After transition the Gcs ended its transition phase and as the aircraft continued to descend the operator attempted to u drive and climb the aircraft. There is a possibility that the u drive activation did not take as the Gcs has a loading symbol after clicking u drive. 
Something to note as well from the video is that the vtol system didn’t ever turn off. It seems that maybe it was still attempting to fly the aircraft while the fixed wing was attempting to fly as well.

### David Grosher, 2025-10-24

Further updates: The RC commands were sent to the VTOL from the FW AP.  It appears that the VTOL was not getting some updates over CAN for about 6 seconds during the final portion of the transition. The VTOL was not getting updated GPS data and missed XCOMM messages over CAN. It specifically missed a message to transition to ASSIST which starts the counter for brake and safe of the lift system. There is other logic in place to trigger the system to safe but it wasn’t triggered. We are still investigating.

### Jeremy Kostel, 2025-11-12

CAN captures with LEMB on the bus:
[embedded file]

### Eric Brewer, 2026-04-27

@Jeremy Kostel @David Grosher can we close this one since we traced it down to a couple LEMBs that have been pulled from service?

### Eric Brewer, 2026-05-05

Traced to bad CAN bus performance with specific LEMBs.

### David Grosher, 2026-05-05

@Eric Brewer I just heard today that the LEMBs are en route to SLO. @Jeremy Kostel is going to investigate further.

### Jackson Riley Curvin, 2026-06-30

@David Grosher Can we close this ticket?

### David Grosher, 2026-07-16

@Jackson Riley Curvin I believe the investigation is largely complete, it would be good to touch base with Sammy on the status though of the https://jenaero.atlassian.net/browse/VXEP-1880 task before formally documenting it here and closing it for the customer. Having said that, this task should continue to track the corrective actions for LEMBs. And it should be assigned to Tom or Stephen at that point.

### Pat Wells, 2026-08-11

@Scott Whitney  are there any updates on path forward for corrective action(s)?

### Scott Whitney, 2026-08-11

@Pat Wells Dave mentioned below:

 I believe the investigation is largely complete, it would be good to touch base with Sammy on the status though of the https://jenaero.atlassian.net/browse/VXEP-1880 task before formally documenting it here and closing it for the customer. Having said that, this task should continue to track the corrective actions for LEMBs. And it should be assigned to Tom or Stephen at that point.

Reassigning to @Stephen Peters for LEMB CAs

### Pat Wells, 2026-08-11

Tracking this to closure of the CA. 
@Stephen Peters and @Samuel Lopez what is the status of completing the CA?
@Drew Hildreth @Alexander Alan Arnold FYSA

### Jackson Riley Curvin, 2026-08-18

@Stephen Peters @Samuel Lopez  Can we get Status update?

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V818_20251023T214517Z.zip | archive | 14616 | 2025-10-23 | listed only |
| ImportedSegment.782950152.840866.mov | video | 47224 | 2025-10-23 | listed only |
| image-20251024-002916.png | image | 66 | 2025-10-23 | listed only |
| image-20251024-002925.png | image | 29 | 2025-10-23 | listed only |
| [LRR 25 ID Mishap.pdf](attachments/33310_LRR%2025%20ID%20Mishap.pdf.md) | pdf | 437 | 2025-10-24 | converted |
| 35X CAN Captures.zip | archive | 967 | 2025-11-12 | listed only |
