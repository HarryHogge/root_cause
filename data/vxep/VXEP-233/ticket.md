# VXEP-233: VXE-496 with 550 wing- abnormal behavior after transition to VTOL led to crash

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-01-02
- **Updated:** 2026-09-03
- **Resolved:** 2024-08-23
- **Reporter:** Cameron Chapman
- **Assignee:** David Grosher
- **Creator:** Cameron Chapman
- **Labels:** Land_Abort_Logic
- **Links:** clones VXEP-231 (VXE-496 with 550 wing set-failure during VTOL transition-AS150 contact issues); relates to RMA-208 (VXE 496 Fuse 550 Wing 231220); relates to FS2-1512 (VTOL Abort logic fix); relates to VXEP-283 (VXE-533 Uncontrolled drift and crash after failed VTOL abort)
- **Impact:** Significant / Large
- **Customer:** PMA263
- **Vehicle Tail Number:** 496
- **Other Stakeholder (as required):** David Grosher
- **Issue Status:** From description, it sounds like a HLB or power connector issue. Need to review data.
- **Severity:** 1 - Flight Critical

## Description

This issue tracks the abnormal behavior after the transition failure. We can track the failed transition in the original. 

From customer:
Mission Build was completed and validated. Launch Checklist was completed and A/V launched with no WCA's. Launch was at 0946. IP and VO noticed while in flight the HLB % was fluctuating from 57%-62% and the fixed wing flight indicator was fluctuating from green to red. we commanded RTB at 16-17 min into the flight. when the A/V came in on final and initiated VTOL Landing only the two left VTOL motors came on. At this time, Sgt Ricigliano took command of the Aircraft. the AV banked hard to the right while in the overhead of landing spot. A/V tried to initiate a glide down landing while VTOL motors were on and the IP canceled the Glide down landing. the A/V continued to climb vertically and got to approx. 1000 ft before the HLB depleted to 0%. Sgt Ricigliano tried to push the A/V away from personnel and vehicles by commanding "go to" orbit point 2 to try and get the main  motor to turn on. The main motor did not turn on and the AV did not respond to the "go to" command. Sgt Ricigliano then commanded the AV into U-Drive. U-Drive was responding erratically due to wind. the AV begins to glide down erratically and is porpoiseing. SGt Ricigliano steers the AV away from students and vehicles. once the AV gets over the tree line, the AV stops responding to to U-Drive inputs and crashes in the trees behind the GCS Sites. 


While executing its landing pattern, the AV began transitioning to VTOL at 300 ft. However, only two of the props activated, causing the AV to initially drift from its recovery location. Then the other two props activated, causing the AV to level out. Due to the issue in transitioning to VTOL, the system automatically sent itself to its Emergency Landing Zone which was set to 2000ft, to coincide with the mission altitude. The GCS had a notification that said the AV was going to the ELZ point and said “Ok” or “Cancel”. They attempted to cancel in order to continue with landing, but the system would not accept it. The AV continued to climb toward the ELZ until the hybrid lithium battery died at approximately 1000ft. At that time, the operator attempted to manually glide the AV down in the LZ, but erratic and unresponsive flight controls resulted in a glide into the trees along the LZ. The AV was recovered but severely damaged.
 The HLB was only used on 6 flights. The VTOL motors were used for approximately 50 flights with us, but I’m not certain if TALSA had previously used it. If I had to estimate number of hours, I’d say .2 for the HLB and 1.5 for the VTOL motors.
Summary of damage is as follows:
Fuselage, Tail Boom, Vertical Tail, Horizontal Tail, Center-Right-Left Wings, Left Lift Boom, Right Lift Boom, fuselage box (496), Wing Box (550), HD45 Trillium Payload (1941), 2 Wing Joiners, Main Battery (3-1341), HLB (2-1726)

Waiting on AAR data from customer 20 December
AAR files received on 20 December

Received picture of HLB from customer on 3Jan2024, picture attached.
Additional info received from customer on 3Jan2024
”The Unit did verify all the HLBs in their system were IAW the AD covering Batteries prior to this incident.”

## Vehicle Configuration

Battery power.
ACFT 496 with 550 wing set

## Corrective Action

- Have GCS recommend fixed wing landing if abnormal HLB voltages are seen during takeoff or prior to VTOL landing. Link to abort criteria issue.

## Plan

Next steps.
- Get CW out of tree. Send equipment back with RMA. Could send data back before if they prefer, or we can get when it arrives.
- Pull VTOL data from CW.
- Work on recreating SW behavior and determine C/CA.
- Cam to Clean up list below.



- Review data.
- Compare BMS voltage to CSB measured voltage. This will indicate if it is a battery or connection issue.
- Link to connection issue Jira if connection issue.
- Has the test VTOL system before VTOL landing been implemented? If not, that may have prevented this.
- “The AV continued to climb toward the ELZ until the hybrid lithium battery died at approximately 1000ft.” Was this a VTOL climb? If so, then this should not be commanded. It should either fixed wing climb to that ELZ, or attempt to VTOL land, never VTOL climb during VTOL issue.

## Comments (9)

### Cameron Chapman, 2024-01-02

@David Grosher I created this issue to track the abnormal behavior after the transition failure. We can track the failed transition in the original.

### Pat Wells, 2024-01-03

@David Grosher @Cameron Chapman received picture of HLB from customer today. Picture attached. 
Added note from customer stating that they were in compliance with latest AD on the HLB connector glue issue.

### Cameron Chapman, 2024-01-03

Thanks @Pat Wells do you or @Sean Odell know where the battery power connectors are? Does the customer have them or were they included with the aircraft? We would like to inspect those if not attached to the battery.

### Sean Odell, 2024-01-03

@Cameron Chapman Pat and I asked the customer to double check and I checked the large amount of parts in the transit cases at Edge. No connectors found.
@Pat Wells FYI

### Cameron Chapman, 2024-01-03

@Pat Wells @Sean Odell It looks like most of the CW (including the avionics) was not returned. It could be still in the tree along with the power connectors. Hopefully they can find a long pole or ladder to get it.

### Pat Wells, 2024-01-03

@Cameron Chapman I’m in communication with the customer on retrieving the wing from the tree.  Nothing yet…

### Pat Wells, 2024-01-08

@Cameron Chapman I requested information from the customer last week regarding the whereabouts of the HLB power connectors.  Have not received anything back as of today.

### Pat Wells, 2024-01-16

@Cameron Chapman the customer followed up with me today and they have essentially given up on recovering the wing and battery connectors. 
Do not expect anything further.

### David Grosher, 2024-02-05

@Jason Scherer this sounds similar to the bug that you found regarding the REACE condition on the initial transition in VTOL flight. Is there a way to identify the issue from the logs in the previous production release?

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| MISHAP 20231214 (496).PNG | image | 3241 | 2024-01-02 | listed only |
| T95_V496_231214_065114_pack.zip | archive | 1413 | 2024-01-02 | listed only |
| image-20231220-231347.png | image | 58 | 2024-01-02 | listed only |
| HLB.jpg | image | 102 | 2024-01-03 | listed only |
