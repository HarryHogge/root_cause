# VA-41: VXE398 GCS says Centerwing Not Connected

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-05-10
- **Updated:** 2025-05-21
- **Resolved:** 2025-05-21
- **Reporter:** Cody Smisek
- **Assignee:** Kyle England
- **Creator:** Cody Smisek
- **Labels:** 1607P01A-XCOM, 8-28-Sprint
- **Links:** relates to RMA-121 (VXE398 230517); relates to VA-42 (Perform VXE-OS-22-005 Post Incident Flight Data Collection)

## Description

Customer states that GCS showing CW not connected. 
Vehicle flew 2 times prior same day, no changes other than batteries. 
History Summary:
398 originally customer was flying, had flown a lot that day, lost connection at some point.
Could get to XCOM and VTOL pages over ethernet, no link between them (indicates CAN failure).
Smart battery to XCOM did not work (indicates CAN failure in fuselage).
Found bad component on the XCOM board.
Replaced entire avionics box. Recalibrated, worked in SCO fine. When flying with 491 CW, started getting CAN dropouts. Delivered 398 fuselage to engineering at that point.
Have flown 491 CW a lot of times with other fuselage with no issues.

## Plan

Need engineering direction for fix by Monday 8/14 COB
- Due to upcoming deadline and inability to find cause of damage, please replace XCOM board, fuselage signal harness, and branch cable. @Kelly J Furlong @Kyle England @Sean Odell
- Please mark removed components with this Jira number and deliver to engineering for further troubleshooting.
- we should also get out hands on, label with incident number, and repair the XCOM in this incident.
- Continue troubleshooting removed components, or install them on a HIL or other test equipment and monitor for repeat occurence. 
- perform another functional check while manipulating those harnesses, now that they can bend more not being constrained in the fuselage. This may increase our odds of findings a cause.

## Issue Status

Reoccurrence:
- CAN Resistance checks look normal. 60ohm measured with VTOL AP connected to fuselage..
- Tested HIL XCOM on 398 fuselage. CAN signal looks good and communication worked. Completed shake test of fuselage, unable to recreate issues with manual vibration.
- Since the issue started with different center wings, batteries, and avionics boxes, it seems like it is either being caused by something in fuselage signal harness, or less likely we have some fault CAN components that ended up on two XCOM boards. Unable to find anything wrong with fuselage components.



Original issue:
Issue isolated to XCOM board. Asked Sean in linked RMA to coordinate a replacement.
6/1 update: Problem isolated to U13 (100-109988) on XCOM board (PN: 965-1-01-4008, SN: 5-5120). XCOM replaced, reworked one going into Fixed Wing AP HIL Box (107-111757, SN: S-S100040)
Failed part is labeled with a note saying where it came from and to keep for a year. A place will be created to keep these parts.

## Root Cause

Initial Root cause guesses (before reoccurence): Faulty component. Lack of comprehensive ESD protection at EA. Component storage issues. Possible damage from connected device.

## Comments (58)

### Cody Smisek, 2023-05-10

- Checked CW connector pins
- Restarted vehicle (multiple times)
- Attempted connection from multiple GCS

### Cody Smisek, 2023-05-10

@Cameron Chapman @Carson Buckley  
Edit: I may not have been specific enough, asking operator to confirm data cable also connected.
Data cable / heater cable wasn’t plugged in but has since been connected. Same status. 
[embedded: MicrosoftTeams-image (8).png]

### Cody Smisek, 2023-05-10

No backup center wing available at this time.

### Cody Smisek, 2023-05-10

@Cameron Chapman any other steps available? operator only has this system at the moment.

### Cody Smisek, 2023-05-10

@Sean Odell FYI. This will likely be coming back for an RMA.

### Sean Odell, 2023-05-11

@Cody Smisek Thank you for the heads up!

### Cody Smisek, 2023-05-11

Customer advised to return for RMA on 5/10. Customer only sending fuselage.

### Cameron Chapman, 2023-05-15

@Cody Smisek please add tracking when available. @Sean Odell

### Cody Smisek, 2023-05-15

They have not provided any tracking info yet. I will follow up to see if it has been shipped (unlikely). 
Per INL, it is shipping out today. Tracking information to follow.

### Cody Smisek, 2023-05-16

@Sean Odell Fedex tracking #398332468947. Currently out for delivery to SLO.

### Sean Odell, 2023-05-17

@Cody Smisek Aircraft arrived and initial Photos taken. Moving this over to engineering.

@Cameron Chapman Please assign to the correct engineer please.

### Cameron Chapman, 2023-05-17

@Hayden Jeanor , can you please check this out or reassign if anyone else has more availability. I suggest removing the avionics box, testing on ironbird or HIL if CAN is still not working, then troubleshoot inside avionics box if not.

### Hayden Jeanor, 2023-05-18

will begin investigation later today or beginning of tomorrow

### Cody Smisek, 2023-05-22

@Hayden Jeanor any updates?

### Hayden Jeanor, 2023-05-23

with @Mark Squillante, removed avionics box from V398 fuse and tested on IB. No CAN signal read to or from Xcomm interface
[embedded: image-20230523-172815.png]
…. now troubleshooting Avionics box

### Hayden Jeanor, 2023-05-23

handing off to @Mark Squillante . Next ideas to execute:
- probe CAN bus when connecting avionics box to IB
- measure form VTOL AP side to avoid shorts
- use differential mode on scope and capture traces
- further isolate between boards in the avionics box
- swap Xcomm and fw AP - not sure if they are swappable though, i would ask Lawton

### Hayden Jeanor, 2023-05-23

captured the CAN bus traffic when V398’s avionic box was plugged into IB:
[embedded: DS1Z_QuickPrint9-20141101-190000.png]
Although the resultant differential waveform(purple) follows the CAN characteristics of ~0-2Vpp amplitude with sharp edges, the waveforms that produce the differential waveform (yellow - CAN high and blue - CAN low) do not. During the recessive state of the signals, both signals are getting pulled to ground, as opposed to ~2V as shown in a working CAN bus signal on the IB:
[embedded: DS1Z_QuickPrint8-20141101-190000.png]

Even though, the differential signal looks analogous, the CAN transceiver specifies a min and max for the recessive voltage:
[embedded: image-20230523-235220.png]

### Hayden Jeanor, 2023-05-23

measured the resistance between each CAN line and GND of V398: ~1.5kOhms
same resistance measured on a good Xcomm board: ~470kOhms

Was not able to identify where these buses are getting pulled down to GND through visual inspection, but the differentiating receiving op amp might have broken down within the CAN transceiver.
[embedded: image-20230524-004233.png]
Would be interested to measure the RXD signal out of the CAN transceiver

### Mark Squillante, 2023-05-25

After swapping the XCOM board in 398’s Avionics box with a known good one CAN Bus communications were good. Problem isolated to the XCOM board. Recommend replacing XCOM board.

### Cameron Chapman, 2023-05-25

Issue isolated to XCOM board. Asked Sean in linked RMA to coordinate a replacement. This customer is running low on equipment and needs it for an international trip soon. We can keep this issue open to track further XCOM troubleshooting. Reducing priority.

### Cameron Chapman, 2023-05-25

@Mark Squillante @Hayden Jeanor a next step for troubleshooting could be to remove the CAN IC, then measure this pin to the ground pin and compare it to another IC off the board. 
Can also measure the resistance of the pad with the IC removed. 
Depending on the results, install a new IC and see if it measures normal/works.

### Mark Squillante, 2023-05-25

@Cameron Chapman I could also lift the suspect pins and measure resistance to ground of the pins and also the pads on the board.

### Mark Squillante, 2023-05-25

I lifted the CANH and CANL pins of the IC. CANL (pin 6) measures 1.5k to ground, CANH (pin 7) measures ~72k ohms to ground. Pads measure open to ground. Problem likely U13 IC, pin 6.

### Cameron Chapman, 2023-05-25

Thanks Mark. I recommend pulling U13 IC fully off, measure compared to a new one. Placing in a labelled bag. Reinstall a new one, measure if normal resistance, then retest CAN connection.

### Cameron Chapman, 2023-05-25

@Cody Smisek do you know if this vehicle was flying any abnormal payloads? Is it possible to record what HLB was connected during the issue? The information may be in the flight logs. If not, we should open an improvement to start logging HLB cell voltages and SN if we aren’t already.

### Cody Smisek, 2023-05-25

@Cameron Chapman I’ll inquire on payload/battery (although battery is probably lost cause at this point if it’s not recorded in logs). Lets grab the logs off equipment if possible before xcomm swap.

### Cody Smisek, 2023-05-25

Customer reports using a PRC163 during their flights. Unknown what specific battery was in use, might be provided the range of ones that could have been used next week.

### Mark Squillante, 2023-05-30

Old part after removal:
Pin 6 to GND (pin 2): 2.15k ohms
Pin 7 to GND: 72k ohms

New part before installing:
Pin 6 to GND: 433k ohms 
Pin 7 to GND: 433k ohms

After installing new part on PCB:
Pin 6 to GND: 373k ohms
Pin 7 to GND: 373k ohms
I will put removed part in an ESD bag and label it.

### Mark Squillante, 2023-06-01

I verified that the XCOM board which had U13 replaced does communicate via CAN Bus, so it looks like U13 was the source of the problem.

### Cameron Chapman, 2023-06-01

Looks ready to close. Does the damaged part physically match the replacement one (not seem counterfeit). ?
In investigation status,  record PN and SN of the XCOM and SN for which HIL box it gets installed into, in case it has issues in the future. Record location where bad IC is currently stored. We should establish a location. Keep for ~1 year. mark that on the label 
Root cause guesses: Faulty component. Lack of comprehensive ESD protection at EA (link to that ticket). Component storage issues. Possible damage from connected device.  
Pasting info from Mark: I replaced U13 on the XCOM board and verified the Can bus communication on the iron bird. I'm using the reworked XCOM board on one of the HIL boxes and I believe Lawton replaced the XCOM in the avionics box for 398, tested it and sent it to final assembly already.

### Cody Smisek, 2023-06-02

@Cameron Chapman @Mark Squillante is the aircraft back in @Sean Odell area yet?

### Mark Squillante, 2023-06-02

@Cody Smisek yes, Sean has the aircraft.

### Cameron Chapman, 2023-06-02

Updated location to this and RMA issue.

### Mark Squillante, 2023-06-02

The removed part matches the replacement part as far as the marking on the package. I do not believe it was counterfeit but I am not 100% sure.

### Sean Odell, 2023-06-07

@Cody Smisek Replacement hardware in the Queue for July to repair this aircraft. Will attempt to pull in, but no guarantee.

### Mark Squillante, 2023-06-08

I have the failed part labeled with a note saying where it came from and to keep for a year. I will make a place to keep these parts.

### Carson Buckley, 2023-08-10

@Cody Smisek @Sean Odell Problem seems to still remain. After recalibration and electronics check (with no issue) vehicle was taken to the range for test flight, and the center wing connection failed. ADP was dropping data, smart battery was not reporting cells, and fault indicators were cycling. Either: XComm failed again or, Main System Harness may be suspect.

### Cameron Chapman, 2023-08-11

The previous cause of this issue was a faulty CAN transceiver. Since it happened again on a new board (confirming), it seems likely that either something else in the aircraft is damaging them, or less likely that we have a fault batch. This is concerning, as many devices are connected to the CAN bus, so the fault could be in any of them (HLB BMS, VTOL AP, ADB, XCOM, Lots of Harnesses).
 
Test plan:
- Measure CAN bus resistance on this aircraft and compare to normal.
- Options of where  to test: VTOL AP if accessible. Mate to an open battery BMS.
- Measure CAN bus signal on this aircraft and compare to normal.

### Mark Squillante, 2023-08-11

Confirmed another CAN transceiver failure in avionics box. As @Cameron Chapman mentioned it is likely something else is damaging them.

### Mark Squillante, 2023-08-14

Verified a known good avionics box communicates via CAN bus on 398’s fuselage with AP HIL box. Good avionics came from iron bird.

### Mark Squillante, 2023-08-14

@Desiray Johnston or @Carson Buckley do either of you know which harness was changed previously on 398? There is nothing noted in an NCR or RMA about this.

### Carson Buckley, 2023-08-14

@Mark Squillante To my knowledge, no harness was changed, only the AVBox was replaced.,

### Cameron Chapman, 2023-08-14

@Desiray Johnston reports “Power cable was replaced”. I asked which one.

### Desiray Johnston, 2023-08-14

@Cameron Chapman @Mark Squillante @Carson Buckley @Kyle England @Sean Odell Fuselage Power Harness 107-102189 was replaced and Sean was informed to update the RMA quote to include this

### Mark Squillante, 2023-08-14

I measured 6 ohms resistance across anti-spark connector, which is normal

### Mark Squillante, 2023-08-14

CAN bus resistance looks same as known good aircraft. 120 ohms avionics box only, 60 ohms when plugged into HIL box
CAN signal is dead with the latest 398 avionics box, but looks good with known good avionics box (iron bird) connected to 398 fusleage and HIL center wing.

### Mark Squillante, 2023-08-14

Iron bird’s avionics communicates through CAN bus successfully with both GCS and web pages. Can talk to smart battery and VTOL AP.

### Mark Squillante, 2023-08-14

Also performed a wiggle test without seeing CAN comms drop out using avionics from iron bird. This shows harnesses in fuselage are not intermittent.

### Mark Squillante, 2023-08-14

I left 398’s fuselage over by @Sean Odell's desk. Avionics box is in the case and the screws for it are screwed into the avionics box. I was going to deliver it to @Kyle England but he has left for the day and I wasn’t sure exactly where to leave it

### Sean Odell, 2023-08-15

@Desiray Johnston @Kyle DeBernardi @Cameron Chapman @Carson Buckley @Kyle England   UPDATED Quote of repair being completed this morning for the following parts. Please let me know team, if I missed anything. 

| - VXE30 Avionics Box  (NEW)                           PN: 965-1-01-3100.2 |
| - New XCOMM board to be replaced           PN: 965-1-01-4008 |
| - New Branch Cable Assembly                       PN: 115-107145 |
| - Fuselage Cable Assembly                             PN: 107-103806 |
| - Fuselage Power Harness                           PN:  107-102189 |
| - SCO and Test Flight |
| -Various Labor for Engineering Evaluation and troubleshooting |

### Cameron Chapman, 2023-08-15

Avionics box contains an XCOM board, so you will be replacing one or the other, not both. Fuse power harness does not need to be replaced for this investigation. Are you referring to the previous swap due to the old pull strap that came off? 
If you plan to scrap the parts, please deliver or save for engineering equipment that is pulled out of the aircraft. We can label it with the incident number and continue to troubleshoot/use on an engineering ironbird. This could eventually lead to discovering the cause of the issue.

### Sean Odell, 2023-08-15

@Cameron Chapman I will change the verbiage. Meant to say the XCOMM replacement was on the brand new avionics box. Appreciate the help.

### Mark Squillante, 2023-08-15

Removed branch cable (115-107145) and fuselage cable assembly (107-103806) delivered to Engineering with red tags, will store in Engineering Iron Bird parts bin

### Cameron Chapman, 2023-08-15

Thanks @Mark Squillante . For next steps, I recommend performing another functional check while manipulating those harnesses, now that they can bend more not being constrained in the fuselage. This may increase our odds of findings a cause.

### Cameron Chapman, 2023-08-15

@Mark Squillante we should also get out hands on, label with incident number, and repair the XCOM in this incident.

### Connor Peebles, 2023-08-16

@Katherine Duberg Passing this XCOMM to @Mark Squillante 

From the linked RMA Jira: “replaced XCOM board in A398, tagged the damaged board (5-5362) and passed it off to @Connor Peebles @Matt Philley“

### Carson Buckley, 2023-08-18

@Sean Odell @Cameron Chapman @Mark Squillante Artis performed 3 flights on 398 (with 491 wings), no issues.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent

## Attachments (15)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| MicrosoftTeams-image (4).png | image | 224 | 2023-05-10 | listed only |
| MicrosoftTeams-image (5).png | image | 165 | 2023-05-10 | listed only |
| MicrosoftTeams-image (6).png | image | 211 | 2023-05-10 | listed only |
| MicrosoftTeams-image (7).png | image | 319 | 2023-05-10 | listed only |
| MicrosoftTeams-image (8).png | image | 124 | 2023-05-10 | listed only |
| screenshot.jpg | image | 415 | 2023-05-10 | listed only |
| DS1Z_QuickPrint8-20141101-190000.png | image | 50 | 2023-05-23 | listed only |
| DS1Z_QuickPrint9-20141101-190000.png | image | 53 | 2023-05-23 | listed only |
| image-20230523-172815.png | image | 189 | 2023-05-23 | listed only |
| image-20230523-235220.png | image | 28 | 2023-05-23 | listed only |
| image-20230524-004233.png | image | 73 | 2023-05-23 | listed only |
| Debug.png | image | 112 | 2023-08-10 | listed only |
| GCS Status and Faults.png | image | 475 | 2023-08-10 | listed only |
| XComm Remote Air.png | image | 133 | 2023-08-10 | listed only |
| XComm Smart Battery.png | image | 95 | 2023-08-10 | listed only |
