# VXEP-188: Repeat SCO Test Failure - iBatt Results during Lift System Check due to Hybrid Lift Battery (114-106085)

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2023-07-25
- **Updated:** 2025-02-05
- **Resolved:** 2025-02-05
- **Reporter:** Matt Philley
- **Assignee:** Cameron Chapman
- **Creator:** Matt Philley
- **Labels:** InternalIncident, Production
- **Links:** relates to VA-174 (1911P01A Ground Isolation Board)
- **Part Number(s):** 114-106085, 1911P01A, 107-102425
- **Production Stakeholder:** Ryan Ferguson
- **Other Stakeholder (as required):** Matt Philley
- **Plan:** @Connor Peebles can you please update plan and status fields, then create a linked task in VA for C/CA.

## Description

7/26/23 - Based on results of detailed testing renaming this Jira ticket to reference the iBatt issue instead of targeting the Ground Iso Board, which was found not to be the cause.
Ref NCRs 1170, 1178, 1287, and 1288 for iBatt failures in SCO that are attributed to the Ground Iso Board not performing properly.
We currently have a test performed in Electronics, but we are no longer confident the test is verifying the correct functionality for the aircraft.
Need support to evaluate NCR’d boards and current testing to evaluate improvements.
SCO Failure Description:
| Value | Condition | Expected & Good Value | Rejection Value |
| ib = iBatt | Motor Startup | “short spike” 6-20 | ~10 |
| ib = iBatt | Motor On | steady somewhere around 3-4 | unsteady from -3 to +1 |

During SCO Testing iBatt during Launch Wizard motor run is instable. Log file shows negative values. iBatt during hover test reports low by almost half expected value. This will cause launch abort if flight is attempted.
SCO is expecting a small jump when motor starts up then a stable value until the motor stops.

Value we are monitoring:
[embedded file]
Acceptable:
[embedded file]
Rejection:
[embedded file]

Troubleshooting:
7/25/23
- We swapped new board from inventory into 532 and 533 and both failed a second time
- We swapped out the first “known good” board from the original ironbird, which worked! However, we found out that this board has a different resistor in position R1 (which is also blown) so the result is just confusing
- After noticing R1 is different between the original ironbird (blue resistor with “101” on it), the current inventory (black resistor with “1000” on it), and first article samples from SPM (black resistor with “101” on it) Connor started helping us try to figure out what is correct. It should be a 100ohm resistor, which matches the current Sierra boards and the SPM board (even though they are marked different)
- This is when we de-soldered the blue resistor and found it to be bad
- We tested the rejected boards from SCO to the existing “power supply” test in Electronics
- Rejected boards from SCO still pass this test
- The “blue resistor” board failed this test
- We then setup an ironbird check to replicate what Carson is seeing
- All boards seemed fine per ironbird test
- Suspect that motors not being loaded may be a factor or something else in the system
- We brought the full centerwing over from 533 to ironbird and the same board still passed
- We then went back to SCO and re-tested a “bad” board in 533 and it still showed the same issue
- We installed a new board from SPM into 533 and it showed the same issue
- We are beginning to suspect the issue is not with the Ground ISO Board and may be one of the following
- Current Sense Board which is part of 107-102264
- Current Sense Cable which is part of the main system harness 107-103302
- As a last test we picked the other “known good” iso board from Ironbird #2… and it passed. We tested a couple more “new boards” and they passed
- NOTE this was tested without connecting the payload or heater for HLB
- We put in a “bad” board and it now passes!!
- We began reconnecting items to get it to fail again. The branch cable connection to the battery is causing the reading issue, which points to a CANBUS issue(?)
- We swapped to a different battery and the problem was resolved
- Payload may have been disconnected
- We swapped back to the original battery and payload is connected.. problem is back
- Original battery, payload connected, battery heater not connected… problem is gone
- We swapped the payload with another old JAI payload that does not connector branch cable and problem was back
- Are battery grounds sharing grounds with the payload…?
- Recommend swapping branch cable…?
- Worst case could be Avi Box…?

7/26/23
- Run #1 - 491 full aircraft with payload and same SCO battery (SN 2-19-15) - FAIL 
- Change focus of testing to battery as the variable since 491 flew recently just fine so very confident centerwing and fuse are all good
- Run #2 - 491 full aircraft with payload and battery it last flew with (SN 2-16-77) - PASS
- Run #3 - 491 full aircraft with payload and original SCO Battery (SN 2-19-15) - FAIL again
- Test 533 CW, booms, wings, etc. on 491 with payload and SCO Battery (SN 2-19-15) - FAIL
- Test 533 CW, booms, wings, etc. on 491 with payload and alt Battery (SN 2-16-77) - PASS
- Test 533 CW, booms, wings, etc. on 491 with payload and alt Battery 2 (SN 2-1330) - PASS
- Test 533 Complete aircraft with alt battery 2 (SN 2-1330) - PASS

Aircraft Conclusion
Issue follows battery SN 2-19-15 only and not fuselage or centerwing.
SN 2-19-15 is a current gen HLB, but it was rejected from Production so has been used in SCO for checkouts for recently in the last month or two. 
Aircraft will be checked out for now using HLB SN 2-1330 as a “known good” battery in SCO for acceptance purposes.
SN 2-19-15 will be red tagged and no longer used for SCO checkouts
SCO testing will ensure that all lift motor testing will include fully connecting payload and smart battery connector (from branch cable) since there is some interaction there that we dont fully understand that may impact the current sense.
Next Steps
Carson to test additional SCO/Flight Test Batteries to see if any more present the same condition to help understand if this is isolated to this battery of if there is something larger happening.
Request Engineering support to try and understand how something in the HLB could be impacting the current sense system. HLB SN 2-19-15 is free to be used for any form of testing needed. Matt P will find a home for it for now awaiting investigation. 
- Idea: This battery was rejected for having an out of balance cell. Could be an interaction in the system trying to charge/balance the cell causing some funny stuff

## Comments (7)

### Matt Philley, 2023-07-25

Next task is to test the rejected boards per the existing test procedure (Doc# 109759) to see if they fail in SCO, but pass in Electronics.

### Matt Philley, 2023-07-25

@Carson Buckley lets gather some notes on the failure in SCO here.
@Ryan Ferguson @Desiray Johnston @Marc Richardson FYSA

### Matt Philley, 2023-07-26

@Greg Fryer @Cameron Chapman can we get someone assigned to look into it at some point? I handed off the red tagged battery to Connor to deposit in Engineering’s flam cabinet. Right now it appears isolated to this single battery, however we will be checking the rest of the SCO/Flight Tast HLB’s to see if any others present the same symptoms.

### Cameron Chapman, 2023-07-26

Changed issue type to incident, which seems a better form for troubleshooting like this.
Assigning to PCB production support lead @Connor Peebles . Connor, can you please summarize investigation status, plan, etc like we do for incidents. Please then continue to troubleshoot after MARSOC incident work, or handoff either to someone else. 
The HLB should normally not affect the current sense board or ground iso board, as the only connections between them are power and ground. It is possible that issues with grounding or the CAN connection to the VTOL AP could disrupt communication or measurements.

### Connor Peebles, 2023-07-26

@Cameron Chapman Absolutely will do. The prevailing theory is that there was a big ground loop through the CAN to the HLB, which bypassed the iso board

### Matt Philley, 2023-07-28

@Connor Peebles FYI Carson encountered this again on AC538 today. Battery SN 2-1330. Carson swapped to a fresh battery and problem resolved.
@Carson Buckley verify numbers, but battery was below 50% change and cell delta of 0.012
This seems to support @Ben Norris theory that it has something to do with the battery being out of balance and the system’s response to that causing some weird grounding or interference in CANBUS, which causes interference in current sense.

### Christa Meck, 2025-02-05

Canceling per comment on https://jenaero.atlassian.net/browse/VXEP-97

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| iBatt expected values.MOV | video | 16519 | 2023-07-26 | listed only |
| iBatt out of range.MOV | video | 22280 | 2023-07-26 | listed only |
| image-20230726-172934.png | image | 628 | 2023-07-26 | listed only |
