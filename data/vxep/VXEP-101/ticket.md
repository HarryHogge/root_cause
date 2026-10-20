# VXEP-101: VXE-487 488CW Damage to Center Wing power connector -Motors stopped at 90ft during VTOL landing

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-09-22
- **Updated:** 2026-09-14
- **Resolved:** 2023-12-18
- **Reporter:** Pat Wells
- **Assignee:** Cameron Chapman
- **Creator:** Pat Wells
- **Labels:** Crash, Hardware, PMA263
- **Links:** relates to ENG-3042 (487 Motors Stopped on Landing); is blocked by VA-627 (Investigation: VXE 487 (w/488 wing) VTOL motor stop at 90ft during landing); relates to FS2-1157 (v487 - Lift motors failing 2 at a time); relates to RMA-153 (VXE-487 Fuse and 488 Wing set 231003); relates to VA-573 (Poor Quality/higher impedance plating on AS150 power contacts - Containment and Corrective Action); relates to VXEP-12 (TPTR-87 VXE 511 VTOL Connector Issues 516 CW. Contains Main connector/contact C/CAs); relates to VXEP-220 (VXE 487 - GCS blocking resulting in multiple FWAP link losses )
- **Customer:** PMA263
- **Vehicle Tail Number:** 487
- **Problem Type:** Other (explain in description)
- **Issue Status:** Complete.
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

Customer reported that aircraft 487, during VTOL landing, at 90ft had the forward 2 motors stop followed by the aft 2 motors. The aircraft fell to the ground and was damaged.
ACFT 487 flying with 488 wing set
Flight logs and investigation files: Flight Safety - VXE 487 (VXEP-101) VTOL motors stopped at 90ft during landing - All Documents (sharepoint.com)
Latest Report: Vehicle Investigation Report VXEP-101.pptx

## Corrective Action

Discrepant contacts identified and contained in factory. AD/SB created. Possible incomplete mate possible, additional label to make incomplete mate visible crteated. Notify customer to apply ADs and SBs. Additional note to keep software/firmware up to date per those SBs.
https://jenaero.atlassian.net/browse/VXEP-12

## Plan

- Complete test report/fishbone.  @Jason Scherer working.
- Check takeoff for any indications of connector fault (low voltage). Plot in ppt.
- Complete all fields in this issue.

Complete

## Root Cause

Damage to Center Wing power connector (due to intermittent contact and/or sparking) resulted in battery voltage not reaching lift system. Backed up by VTOL log indicating a lift power failure (shows as low voltage).
https://jenaero.atlassian.net/browse/VA-573

## Comments (25)

### Sean Odell, 2023-11-09

@Greg Fryer @Cameron Chapman  Aircraft intake complete and aircraft delivered to Engineering for your continued evaluation. Photos are on the RMA ticket linked.

### Cameron Chapman, 2023-11-10

@Jason Scherer aircraft arrived. Are you available to pull and analyze flight logs?

### Jason Scherer, 2023-11-10

@Cameron Chapman Yes. Where should I meet you? Or where is the AV?

### Jason Scherer, 2023-11-10

Ok I found the fuselage. Was there a center wing returned as well? @Sean Odell

### Sean Odell, 2023-11-13

@Jason Scherer They used VXE-488 Wing case with VXE-487 Fuse. So two aircraft was involved in the incident.

### Jason Scherer, 2023-11-13

@Sean Odell Thanks! I knew that I just forgot. Sorry rookie mistake. I have the wing now.

### Cameron Chapman, 2023-12-04

@Jason Scherer will you be available to work on this when you return? We would like to repair and return the relevant equipment soon.

### Greg Fryer, 2023-12-05

Plan: @Jason Scherer To update the fields on this ticket and PPT to indicate no log of flight and old FW as conclusions, then close.

### Jason Scherer, 2023-12-05

@Cameron Chapman @Greg Fryer I am currently supporting the X-Kit critical path while also trying to close out investigations. I have pulled the logs off the aircraft, but not yet completed a review. I can return the avionics and wing if you want to start the RMA before I review the data. Let me know how I should proceed.

### Jason Scherer, 2023-12-05

To clarify, I was able to extract more logs. After the 455 investigation I had a better understanding of the log extraction process.

### Cameron Chapman, 2023-12-06

@Jason Scherer We should ensure the issue is not in the center wing before returning it for RMA. Initial indications seem to be battery and/or CW power connections. More to come.

### Jason Scherer, 2023-12-06

@Cameron Chapman Understood. I put the CW back into the CW 488 case on the engineering floor. Hayden took a quick look at the connector and noted some potential evidence of connector failure. I plan to update all the fields on this ticket and create a report today for this investigation with the data I have so far. I’ll also make sure all the logs I have are uploaded to SharePoint.

### Cameron Chapman, 2023-12-06

Thanks @Jason Scherer . 
- Do the logs list what battery was connected during this incident? If not, we can ask LM if they know.
- @Mark Squillante can you perform an impedance measurement of this connector and add photos of connector issues to the location in the description?

### Mark Squillante, 2023-12-06

@Cameron Chapman measured 305uOhms. After cleaning went down to 253uOhms. Both are failing numbers. I took pictures and uploaded to location mentioned in description. There is obvious damage to the AS150 contact. Anti-spark resistance measured 5.6 ohms.

### Pat Wells, 2023-12-18

@Cameron Chapman @Greg Fryer 
Is the final report releasable to the end user customer (PMA263)?  It’s currently marked as proprietary.

### Greg Fryer, 2023-12-18

@Pat Wells Yes, it’s releasable. Proprietary just means they can’t share it beyond the USG. (Technically there is a bunch of marking stuff we should do, but it’s never been required on our orders/contracts.) If/when you deliver it, you could ask them if they need it marked any particular way. (Most like would be a Distribution Statement).

### Pat Wells, 2023-12-18

@Greg Fryer understood.

### Greg Fryer, 2023-12-18

@Pat Wells That one should get tied up with our service bulletin on contacts.

### Greg Fryer, 2023-12-18

@Cameron Chapman @Jason Scherer @Pat Wells I made some minor updates to the fields, to keep them crisp. e.g. the root cause was bleeding into investigation status. Status can just be “Complete”. 🙂 
@Pat Wells Once you have communicated to the customer, we will fully close this, so please let Cameron and I know when done.

### Pat Wells, 2023-12-18

@Greg Fryer @Cameron Chapman communication to customer is complete.

### Greg Fryer, 2023-12-18

@Pat Wells Yes, it’s releasable. Proprietary just means they can’t share it beyond the USG. (Technically there is a bunch of marking stuff we should do, but it’s never been required on our orders/contracts.) If/when you deliver it, you could ask them if they need it marked any particular way. (Most like would be a Distribution Statement).

### Pat Wells, 2023-12-18

@Greg Fryer understood.

### Greg Fryer, 2023-12-18

@Pat Wells That one should get tied up with our service bulletin on contacts.

### Greg Fryer, 2023-12-18

@Cameron Chapman @Jason Scherer @Pat Wells I made some minor updates to the fields, to keep them crisp. e.g. the root cause was bleeding into investigation status. Status can just be “Complete”. 🙂 
@Pat Wells Once you have communicated to the customer, we will fully close this, so please let Cameron and I know when done.

### Pat Wells, 2023-12-18

@Greg Fryer @Cameron Chapman communication to customer is complete.

## Attachments (0)
