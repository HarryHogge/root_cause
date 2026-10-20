# VXEP-231: VXE-496 with 550 wing set-failure during VTOL transition-AS150 contact issues

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** High
- **Created:** 2023-12-20
- **Updated:** 2026-09-14
- **Resolved:** 2025-03-21
- **Reporter:** Pat Wells
- **Assignee:** Cameron Chapman
- **Creator:** Pat Wells
- **Labels:** Crash, Hardware, PMA263, Weekly-incident-tracker
- **Links:** relates to RMA-208 (VXE 496 Fuse 550 Wing 231220); is cloned by VXEP-233 (VXE-496 with 550 wing- abnormal behavior after transition to VTOL led to crash); relates to VXEP-12 (TPTR-87 VXE 511 VTOL Connector Issues 516 CW. Contains Main connector/contact C/CAs); relates to XKIT-1958 (Havoc 550 fuse 371 CW - Land Transition Failure 20240423); relates to XKIT-2421 (XKIT - Demo Prep Incident 20240612); relates to VXEP-628 (Systemic VXE30 VTOL ESC Reliability Issues ); relates to XKIT-760 (Main AS150 replacement issue-Develop new battery power connectors for Havoc Block 5)
- **Impact:** Significant / Large
- **Customer:** PMA263
- **Vehicle Tail Number:** 496
- **Other Stakeholder (as required):** Nadia Brown
- **Issue Status:** Center wing stuck in tree. Operator says they will not take it down.
- **Severity:** 1 - Flight Critical

## Description

From customer:
Mission Build was completed and validated. Launch Checklist was completed and A/V launched with no WCA's. Launch was at 0946. IP and VO noticed while in flight the HLB % was fluctuating from 57%-62% and the fixed wing flight indicator was fluctuating from green to red. we commanded RTB at 16-17 min into the flight. when the A/V came in on final and initiated VTOL Landing only the two left VTOL motors came on. At this time, Sgt Ricigliano took command of the Aircraft. the AV banked hard to the right while in the overhead of landing spot. A/V tried to initiate a glide down landing while VTOL motors were on and the IP canceled the Glide down landing. the A/V continued to climb vertically and got to approx. 1000 ft before the HLB depleted to 0%. Sgt Ricigliano tried to push the A/V away from personnel and vehicles by commanding "go to" orbit point 2 to try and get the main  motor to turn on. The main motor did not turn on and the AV did not respond to the "go to" command. Sgt Ricigliano then commanded the AV into U-Drive. U-Drive was responding erratically due to wind. the AV begins to glide down erratically and is porpoiseing. SGt Ricigliano steers the AV away from students and vehicles. once the AV gets over the tree line, the AV stops responding to to U-Drive inputs and crashes in the trees behind the GCS Sites. 


While executing its landing pattern, the AV began transitioning to VTOL at 300 ft. However, only two of the props activated, causing the AV to initially drift from its recovery location. Then the other two props activated, causing the AV to level out. Due to the issue in transitioning to VTOL, the system automatically sent itself to its Emergency Landing Zone which was set to 2000ft, to coincide with the mission altitude. The GCS had a notification that said the AV was going to the ELZ point and said “Ok” or “Cancel”. They attempted to cancel in order to continue with landing, but the system would not accept it. The AV continued to climb toward the ELZ until the hybrid lithium battery died at approximately 1000ft. At that time, the operator attempted to manually glide the AV down in the LZ, but erratic and unresponsive flight controls resulted in a glide into the trees along the LZ. The AV was recovered but severely damaged.
 The HLB was only used on 6 flights. The VTOL motors were used for approximately 50 flights with us, but I’m not certain if TALSA had previously used it. If I had to estimate number of hours, I’d say .2 for the HLB and 1.5 for the VTOL motors.
Summary of damage is as follows:
Fuselage, Tail Boom, Vertical Tail, Horizontal Tail, Center-Right-Left Wings, Left Lift Boom, Right Lift Boom, fuselage box (496), Wing Box (550), HD45 Trillium Payload (1941), 2 Wing Joiners, Main Battery (3-1341), HLB (2-1726)

Waiting on AAR data from customer 20 December
AAR files received on 20 December

## Vehicle Configuration

Battery power.
ACFT 496 with 550 wing set

## Corrective Action

- Have GCS recommend fixed wing landing if abnormal HLB voltages are seen during takeoff or prior to VTOL landing. Link to abort criteria issue.
- Contact issue C/CAshttps://jenaero.atlassian.net/browse/VXEP-12

## Plan

Next steps.
- This incident is for the propulsion failure. The linked issue is investigating the abnormal behavior after that. https://jenaero.atlassian.net/browse/VXEP-233
- @Pat Wells do you have any information on if the battery involved had the squeeze out AD applied to it?
- Get CW out of tree. Send equipment back with RMA. Could send data back before if they prefer, or we can get when it arrives.
- Pull VTOL data from CW. Not happening.
- @David Grosher Has the test VTOL system before VTOL landing been implemented on the software in this incident? If not, that may have prevented this. We can link it as a CA.

## Root Cause

Failure between VTOL battery and VTOL system (proven by large delta between BMS and VTOL measured voltage). Likely due to these issues. https://jenaero.atlassian.net/browse/VXEP-12

## Comments (17)

### Cameron Chapman, 2023-12-20

@Pat Wells do you have an estimate for when the data will be available and when the aircraft will be returned? 
@David Grosher @Craig Burton , I am sure there will be lots learned from data review, but there seems to be some SW+FW issues we could start planning to resolve now. 
Ex: 
- The AV continued to climb toward the ELZ until the hybrid lithium battery died at approximately 1000ft.” Was this a VTOL climb? If so, then this should not be commanded. It should either fixed wing climb to that ELZ, or attempt to VTOL land, never VTOL climb during VTOL issue.
- Has the test VTOL system before VTOL landing been implemented? If not, that may have prevented this.

### Pat Wells, 2023-12-20

@Cameron Chapman I’ve requested the data from the customer.  “Hopefully” by close of business today.

### David Grosher, 2023-12-20

@Cameron Chapman 
1. There should be no VTOL climb of that altitude allowed at all. 
2. There have not been any new VTOL system checks implemented since the previous issue (v487) where a check was identified as beneficial.

### Pat Wells, 2023-12-20

@Cameron Chapman @David Grosher AAR files received and attached to this ticket.

### David Grosher, 2023-12-20

@Pat Wells There is no VTOL data in the AAR. Perhaps it is too damaged? We will want to get access to the HW to try and pull it off the SD card.

### Pat Wells, 2023-12-20

@David Grosher the HW is in the process of being returned to SLO.  Expected late next week.

### Pat Wells, 2023-12-20

@David Grosher @Cameron Chapman Just confirmed with customer.  Center wing panel is stuck 30 feet up in a tree. This explains the lack of VTOL data.
 I asked if they could attempt to recover it.  More to follow…

### Cameron Chapman, 2023-12-20

Data from Xcom log indicates a clear connector issue. 
[embedded: image-20231220-231347.png]
Next steps. 
- Separate incidents for connector failure and aircraft behavior after.
- Get CW out of tree. Send equipment back with RMA. Could send  data back before if they prefer, or we can get when it arrives.

- Inspect HLB and CW power connectors for damage. Attach photos of battery if damaged.
- When it arrives in SLO, perform inspection/measurement.
- Work on recreating SW behavior and determine C/CA

### Sean Odell, 2024-01-02

@Cameron Chapman Aircraft (As much as was recovered from customer) has been delivered to Engineering for Evaluation. 
@Pat Wells FYI

### Cameron Chapman, 2024-01-03

@Laszlo Juhasz can you please pull the vtol logs from this aircraft, then investigate c/ca for the transition failure? Thank you.

### Laszlo Juhasz, 2024-01-03

@Cameron Chapman , @Sean Odell First in the morning, I’m going to start the investigation.

### Cameron Chapman, 2024-01-04

@Laszlo Juhasz you can are welcome to check it out, but we probably won’t get much info until the cw and booms are returned.

### Pat Wells, 2024-01-04

@Cameron Chapman @Laszlo Juhasz the booms were returned.  @Sean Odell did you deliver those with the aircraft fuselage?

### Sean Odell, 2024-01-04

@Pat Wells What is left of the booms is in the wing case. Very badly damaged, but are there.
@Laszlo Juhasz fyi

### Christa Meck, 2025-03-06

@Cameron Chapman and/or @Pat Wells Is there more work to be done on  this incident from 2023?

### Pat Wells, 2025-03-06

@Christa Meck nothing further required from my side.

### Christa Meck, 2025-03-21

Not sure about Bermuda Triangle list but closing this one per comment from Pat.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| MISHAP 20231214 (496).PNG | image | 3241 | 2023-12-20 | listed only |
| T95_V496_231214_065114_pack.zip | archive | 1413 | 2023-12-20 | listed only |
| image-20231220-231347.png | image | 58 | 2023-12-20 | listed only |
