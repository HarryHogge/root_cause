# VXEP-484: 0002P01G Green Autopilot Reliability Issues/Fallout Study

- **Issue type:** Major Project
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-04-03
- **Updated:** 2025-09-02
- **Resolved:** 2024-08-30
- **Due:** 2023-04-14
- **Reporter:** Connor Peebles
- **Assignee:** Connor Peebles
- **Creator:** Connor Peebles
- **Labels:** 8-28-Sprint, Crash, FixedWingAP
- **Links:** relates to ENG-3079 (451 - GCS not connecting to aircraft ); relates to ENGPRJA-58 (0002P01G Green AP's have a high failure rate); relates to ENG-3054 (VXE 455 Uncommanded departure from orbit and crash into Potomac); relates to ENG-2992 (VXE 444 Crash in Landing Pattern); relates to ENG-3011 (VXE 483 avionics box appears not to be powering up. ); causes ENG-1313 (0002P01G Green Autopilot Fallout Longterm Before-After Study); relates to VXEP-466 (IRAD: Unified Autopilot); relates to ENG-2921 (Replace 0002P01G Autopilot-processor ST10F168SQ6 obsolete.); relates to ENG-3060 (VXE 465 Cannot Connect to GCS); relates to ENG-723 (Dry cabinet(s) and ESD bag sealer - Improve PCBA and component handling concerning humidity); relates to VA-156 (Receiving qty 800 new processors (st10...) evaluate and test with hand soldering and small batch to Sierra); relates to VA-155 (Evaluate Burn-in failures, consider 1710A01A failure of MPU-9250 during burn-in); relates to VA-154 (Record re-work process changes); relates to VA-153 (Firmware tests to more thoroughly test processor functionality ); relates to VXEP-499 (Draft Green AP "Modified" Containment Traveler); relates to VA-152 (Document disposition of existing inventory (fielded, in planes here, in avionics boxes, processed, unprocessed, retested after initial failure, etc.) ); relates to VA-150 (Develop enhanced stress tests to ensure reliability of new assembly processes we are trying. ); relates to VA-148 (Document plan for alternate production processes); relates to VA-149 (Evaluate burn in profile, to see if realistic or too extreme. ); relates to VXEP-498 (Add all AP SNs to the failure sheet (to another tab) to help determine failure rates and points. Ok to link or copy from SN tracker. Try to determine when this started happening. ); relates to VXEP-497 (Scour ALL plane records and figure out which ones were burned in twice. List planes they were installed into. ); relates to VA-145 (Investigate if we have purchased processors from alternate vendors in the last few years, and if we can determine a difference in failure rate vs original stock. ); relates to VA-144 (Evaluate having Sierra hand solder the chips, depending on longer bake out result); relates to VA-143 (Update description with investigation summary. Summarize main causes discovered, investigation plan, corrective actions. ); relates to VXEP-496 (Inspect old autopilots for cracks to see if it is a newer problem); relates to VA-141 (Determine if increasing bake in time decreases processor crack or failure rate. ); relates to VA-140 (0002P01G Green AP - Have Sierra inspect processors before, after bake in, and after reflow for cracks and other issues. Hold all cracked ones at EA. Add all process requirements to the PO and eventually the PCB drawing); relates to VA-139 (Add inspect for cracks to PCB receiving inspection and AP traveler. Hold any APs with cracks. ); relates to VXEP-495 (Figure Out Date-codes of chips, add to failure sheet and investigate for trends. ); relates to VXEP-493 (Compare/ inspect bare processors for micro-cracks); relates to VXEP-494 (Find out the burn-in profile); relates to VXEP-492 (Before sending out processors to be decapped, reflow all solder joint in a toaster oven and try again? Doubtful); relates to VXEP-491 (Look at all the unprocessed green AP's in inventory to look for micro-cracks); relates to VXEP-490 (Fix the custom to re-burn boards, if it fails flag it and NCR it); relates to VXEP-489 (Could we have all chips we have stored out to be x-rayed?); relates to VA-132 (Send some failed boards (only their respective processors) to be decapped); relates to VXEP-487 (Ask Sierra if they have batch # - Ask Sierra about baking the chips); relates to VXEP-488 (Scour the records of VIT tail numbers to see which ones failed burn in the first time, but passed the second burn in); relates to VA-128 (Evaluate conformal coating by Sierra on next orders if it does not interfere with inspection.  Possibly brush coating or other compounds to touch up. ); causes VA-589 (Evaluate solder reflow profiles using in-house solder reflow oven - to eliminate cracking); causes VA-590 (Evaluate proper baking out of ST10F168 - measure dry weight)
- **Part Number(s):** 0002P01G 965-1-01-2004
- **Production Stakeholder:** Ryan Ferguson
- **Supply Chain Stakeholder:** Victor Vandor
- **Other Stakeholder (as required):** Sam Miller
- **Problem Type:** Discovered Issue
- **Job Number:** J100078 - Sustainment: VXE-30

## Description

Link to NCR for known bad FW AP boards: Bad Green AP boards (NCR 844)
Starting shared list and worksheet: 0002P01G Green Autopilot Failures.xlsx
Ongoing PowerPoint summary: 0002P01G Green Autopilot Reliability Issues
Investigation Word Summary: 0002P01G Green Autopilot Failures Summary.docx'
Status: See 0002P01G Green Autopilot Reliability Issues. Updated >weekly.  

ST10F168SQ6 Current FW AP processor. 
Find out why 0002P01G are apparently failing at a high rate;
- Identify root cause for green AP failures that did not make it through production
- Identify root cause for supposed green AP failures in VITs tail numbers:
- 424 - AP SN 10190 - Tested 9/11/2021
- 437 - AP SN 10182 - Tested 11/21/2021
- 444 - AP SN 10211 - Tested 10/7/2021
- 445 - AP SN 10215 - Tested 10/7/2021
- 446 - AP SN 10207 - Tested 10/26/2021
- 451 - AP SN 10231 - Tested 3/25/2022
- 455 - AP SN 10246 - Tested 5/7/2022 - board MIA
- 483 - AP SN 10303 - Tested 12/22/2022 - closed, determined to be XCOMM component failure


Going to make a subtask for every green AP analyzed, Keep them updated in the spreadsheet above

Investigation Plan:
- Visually inspect boards and do preliminary probing
- Take them all to ironbird area to power up the boards and do individual probing
- For VIT affected ones take special care and deliver Root, cause, corrective action for each individual VIT2 ticket

## Comments (10)

### Connor Peebles, 2023-04-03

@Greg Fryer @Sam Miller @Cameron Chapman Feel free to add more to this ticket

### Cameron Chapman, 2023-04-03

@Connor Peebles please see linked project https://jenaero.atlassian.net/browse/ENGPRJ-255 . @Ryan Ferguson did some great work diagnosing a batch of these boards. We could take that information and continue the investigation and metrics.

### Ryan Ferguson, 2023-04-03

I have brought all 13 of the failed autopilots I could find in Electronics to @Connor Peebles.  Attached is a spreadsheet of all SN’s left in Electronics so we can track what information exists.  I also wrote up NCR-844 to track the failures there. 
[embedded: GreenAP Root Cause SNs.xlsx]

### Greg Fryer, 2023-04-04

@Sam Miller This is where we are consolidating the investigation into the failing FW APs.

### Ryan Ferguson, 2023-04-04

I have gone through SCO and pulled all travelers related to the crashed planes and photographed the FWD AP and Avi Enclosure travelers as well as any burn-in graphs.  The photos of those travelers can be seen in the .zip file attached.  For the majority of these autopilots there were no anomalies noted.  One of them, 483, had an incomplete traveler.  The traveler used on this one also had no callouts for burn-in as it was of the old ENG format.  
Of note, only one autopilot of the 8 in question failed burn-in on first attempt.  All others had clean burn-in graphs.

### Cameron Chapman, 2023-04-25

@Connor Peebles I think you should add a link to the latest ppt to this issue description and combine all investigation spreadsheets into one then add the link as needed, to make them easy to find.

### Cameron Chapman, 2023-04-27

@Maxime Jeanneau

### Cameron Chapman, 2023-05-09

@Garrett O'Neill , you may be able to help with some of these tasks after your mod payload and remote ID tasks.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent

### Greg Fryer, 2024-08-30

Actions were completed, but epics and project not closed. Completing.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [GreenAP Root Cause SNs.xlsx](attachments/13425_GreenAP%20Root%20Cause%20SNs.xlsx.md) | xlsx | 13 | 2023-04-03 | converted |
| Crashed Plane AP Travelers.zip | archive | 5498 | 2023-04-04 | listed only |
