# VXEP-1278: VXE-541 Failed to perform proper landing sequence actions, resulting in the aircraft crashing into the ground.

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2025-05-13
- **Updated:** 2026-05-12
- **Resolved:** 2026-04-27
- **Reporter:** Samuel Lopez
- **Assignee:** Samuel Lopez
- **Creator:** Jackson Riley Curvin
- **Labels:** GS_Closed, USASOC
- **Links:** relates to RMA-686 (VXE-541 RMA 250515-1); relates to FS2-3321 (VXE-541 Investigation: Failed to perform proper landing sequence actions); relates to VXEP-1279 (Make a confluence page showing examples of good and bad AS150 plugs and sockets, plots, etc. ); relates to VXEP-553 (AS150 Plug/Pin Connector Issue Systemic Collector)
- **Customer:** USASOC
- **Vehicle Tail Number:** VXE-541
- **Issue Status:** D4 - RCR, D5 CAT review needed.
- **Root Cause:** Connector was loosely mated to the HLB from the CW.
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

Customer did not report incident until beginning of May 2025
Who: SORD, ATOC, 4BN, 10SFG(A)
What: Stalker VXE30 (Tail #541) failed to perform proper landing sequence actions, resulting in the aircraft crashing into the ground.
Where: Agony North, Fort Carson, CO 80911
When: 06 December 2024 at 1200L
Why: During landing sequence, tail #541 failed to transition to the Vertical Take Off and Landing (VTOL) motors. The aircraft instead, continued to reduce its airspeed causing it to glide until it struck the ground. 
Investigation Report: Vehicle Investigation VXEP-1278.pptx
SharePoint Folder: Flight Safety - VXEP-1278 v541 - All Documents

## Corrective Action

Update existing AN for the main battery to include the HLB, or nothing.  Implement recommended design changes into B40.   
https://jenaero.atlassian.net/wiki/spaces/SEIT/pages/849838110/Project+Charter+-+Stalker+Block+31

## Plan

- @Samuel Lopez  please add photos and measurements from actual CW to the investigation ppt. See comments in ppt. Review below to see what steps have been compete vs still need doing.
- Jacob, please review plan, status, C/CA fields and report for this to see if you agree.


6/24/25
- @Steve Gonzales , @David Grosher recommends electrical as the next step in this investigation. Please update plan and status to latest. FYI @Connor Peebles  if you are working it.
- See ppt slides. Evaluate launch and prior flights to see if any abnormalities, things that could drive an abort.
- Look at AS150 history to see if SB was applied, impedance measured, etc.


Previous
@Jackson Riley Curvin 
- Plot Lift system Voltage, Total lift current and Current at each Boom during transition
- Plot attitudes (Pitch, Roll, Yaw) during transition as estimated by FW AP and VTOL AP
- Plot Airspeed
- Plot frequency of the GPS updates
- Re-evaluate Next Steps

## Comments (28)

### David Grosher, 2025-05-13

In the last XCOMM event log a series of errors (low power and differential power errors associated with CLIMB) were reported with the lift system. There was also a timeout. The errors culminated with an attitude fault which SAFED the lift system.
And finally a potentially unexpected state transition that may be the result of the attitude fault: VTOL State Change (was is):  LAND_WAITTRANS LAND_IDLE
In LAND_WAITTRANS the system can no longer abort the landing safely. If it can’t proceed in a good state then it will wait to hit the battery threshold and then descend. This did not happen as there was an attitude error before that happened. 
 
[18:38:29.078 5531.078] DebugMsg Climb abort, lift system fault
[18:38:29.079 5531.079] VT pwr fault: min pwr diff thr  0x31
[18:38:29.353 5531.353] ap dbg: land timeout: 11
[18:38:30.349 5532.350] ap dbg: land timeout: 10
[18:38:30.826 5532.827] sw 1 port rx reset 2
[18:38:30.827 5532.828] ave, flow 976  0
[18:38:31.417 5533.417] ap dbg: land timeout: 9
[18:38:31.842 5533.842] aux servo cycle complete
[18:38:31.969 5533.969] retract power was,is: on off
[18:38:32.403 5534.403] DebugMsg Climb abort, lift system fault
[18:38:32.404 5534.404] VT pwr fault: min pwr  0x21
[18:38:32.819 5534.819] ap link fault: local rx okay ap rx bad
[18:38:32.820 5534.821] ap link fault during landing
[18:38:33.442 5535.442] ap dbg: land timeout: 7
[18:38:34.442 5536.442] ap dbg: land timeout: 6
[18:38:35.236 5537.236] DebugMsg Climb abort, lift system fault
[18:38:35.237 5537.237] VT pwr fault: min pwr diff thr  0x31
[18:38:35.438 5537.438] ap dbg: land timeout: 5
[18:38:36.444 5538.444] ap dbg: land timeout: 4
[18:38:36.852 5538.852] DebugMsg Climb abort, lift system fault
[18:38:36.853 5538.853] VT pwr fault: min pwr  0x21
[18:38:37.444 5539.444] ap dbg: land timeout: 3
[18:38:38.037 5540.037] GNSS Query
[18:38:38.468 5540.468] DebugMsg Climb abort, lift system fault
[18:38:38.469 5540.469] VT pwr fault: min pwr diff thr  0x31
[18:38:38.511 5540.511] ap dbg: land timeout: 2
[18:38:38.872 5540.872] DebugMsg Climb abort, lift system fault
[18:38:38.873 5540.873] VT pwr fault: min pwr  0x21
[18:38:39.528 5541.528] ap dbg: land timeout: 1
[18:38:39.682 5541.682] DebugMsg Climb abort, lift system fault
[18:38:39.683 5541.683] VT pwr fault: min pwr diff thr  0x31
[18:38:40.287 5542.287] DebugMsg Climb abort, lift system fault
[18:38:40.288 5542.288] VT pwr fault: min pwr  0x21
[18:38:40.489 5542.489] DebugMsg Climb abort, lift system fault
[18:38:40.490 5542.490] VT pwr fault: min pwr diff thr  0x31
[18:38:40.657 5542.657] ap dbg: land timeout: 0
[18:38:42.577 5544.577] ap dbg: LaunchShouldFWStopRudder now: 1
[18:38:43.015 5545.015] DebugMsg Climb abort, lift system fault
[18:38:43.016 5545.016] VT pwr fault: min pwr diff thr  0x1031
[18:38:44.222 5546.222] DebugMsg Climb abort, lift system fault
[18:38:44.223 5546.223] VT pwr fault: min pwr  0x1021
[18:38:44.626 5546.626] DebugMsg Climb abort, lift system fault
[18:38:44.627 5546.627] VT pwr fault: min pwr diff thr  0x1031
[18:38:44.928 5546.928] DebugMsg Climb abort, lift system fault
[18:38:44.929 5546.929] VT pwr fault: min pwr  0x1021
[18:38:45.030 5547.030] DebugMsg Climb abort, lift system fault
[18:38:45.031 5547.031] VT pwr fault: min pwr  0x21
[18:38:45.652 5547.652] ap dbg: vt lnd attitude fault during active landing
[18:38:45.653 5547.653] RCS_SAFE 1
[18:38:45.654 5547.654] DebugMsg SAFE ON
[18:38:45.655 5547.656] RCS_SAFE 1
[18:38:45.657 5547.657] DebugMsg SAFE ON
[18:38:45.658 5547.658] RCS_SAFE 1
[18:38:45.659 5547.659] DebugMsg SAFE ON
[18:38:45.660 5547.660] MESSAGE_VTOL2:  114  100
[18:38:45.662 5547.664] VTOL State Change (was is):  LAND_WAITTRANS LAND_IDLE

### Jackson Riley Curvin, 2025-05-14

@David Grosher @Cameron Chapman  I added a picture of the VTOL power connector. I recieved photos this morning from @Alexander Alan Arnold  who is on site with the aircraft now.

### Alexander Alan Arnold, 2025-05-14

I believe next steps should be to send VXE 541 into SLO for investigation/RMA. @David Grosher @Jackson Riley Curvin 

FYSA @Drew Hildreth

### Jeremy White, 2025-05-15

A company called Theseus was working with 10th SFG to integrate their VBN solution. I do not know if they used this VXE for the effort or it contributed to the mishap. If able, please confirm they did not modify the aircraft/avionics box as part of this effort.

See photo on their website. I can’t make out the tail on this integration effort: Theseus: GPS Denied Navigation for Drones | Y Combinator

Photo on their website: https://www.ycombinator.com/media/?type=post&id=83768&key=user_uploads/1290514/edd612ed-a0d4-421d-afe4-36931183b93f

### Connor Peebles, 2025-06-10

@Logan Wright 541 avionics box was plugged back in. Resistance of the main power rails were not showing a short so it was deemed safe to power on the fuselage and CW.

### Cameron Chapman, 2025-06-24

@Steve Gonzales , @David Grosher recommends electrical as the next step in this investigation. Please update plan and status to latest. FYI @Connor Peebles  if you are working it.

### Cameron Chapman, 2025-06-24

@Jackson Riley Curvin @David Grosher did anyone start plotting data for this, or is that on the to do list?  FYI @Connor Peebles @Steve Gonzales

### Pat Wells, 2025-07-18

@Jackson Riley Curvin where did you leave off on this?

### Drew Hildreth, 2025-07-22

@Steve Gonzales Do you have any updates on this Investigation? Do you need anything from the FSRs?
@Jackson Riley Curvin have you provided the Plots elsewhere?

### Steve Gonzales, 2025-07-22

@Drew Hildreth I have not started this one.  I should be able to work on it this week.

### Cody Smisek, 2025-09-03

@Steve Gonzales I see these cases sitting in engineering area. Can we return to RMA area or?

### Steve Gonzales, 2025-09-03

@Cody Smisek Hi Cody, if they need the cases, that is fine by me.  I have not started any work on this one but it is next in line.

### Cody Smisek, 2025-09-03

@Steve Gonzales placed on the engineering rack for time being.

### Pat Wells, 2025-09-03

@Cody Smisek We can’t do anything with this until a root cause is determined.  
@Steve Gonzales

### Steve Gonzales, 2025-10-17

@Cody Smisek @Drew Hildreth @Connor Peebles Hi, the CW is missing from the case.  Does anyone know where it may be at?

### Drew Hildreth, 2025-10-17

@Steve Gonzales I have no idea where the CW would have gone. It was in the case when it arrived and intake was completed by the RMA team. I am sure it is around somewhere. @Lauren Velasquez the CW for 541 hasn’t found it’s way back to you has it?

### Lauren Velasquez, 2025-10-17

@Drew Hildreth I do not have VXE-541 CW

### Steve Gonzales, 2025-10-22

Performed analysis and completed report.

### Steve Gonzales, 2025-10-27

Completed connector tests 10/24/25.

### Steve Gonzales, 2025-10-28

Center-wing found 10/24/25

### Steve Gonzales, 2025-10-29

Report completed

### Lauren Velasquez, 2025-11-12

@Drew Hildreth are we clear to move forward with this?

### Drew Hildreth, 2025-11-12

@Lauren Velasquez No.

### Cody Smisek, 2025-11-18

@Lauren Velasquez @Drew Hildreth I see this is assigned to Steve who is no longer with Edge. The aircraft is in engineering. Can we move the aircraft back to RMA or what’s the status?

### Drew Hildreth, 2025-11-18

@Cody Smisek That is fine. Steve finished up the report so this can go back to RMA.

@Lauren Velasquez I will ask about this, I don’t think they will pay to have it repaired… but I may be wrong.

### Samuel Lopez, 2025-12-16

- Per the investigation by Steve Gonzalez, this aircraft failed because HLB connector was not seated properly.

- VXE-541 was tested on bench using batteries.  XCOMM and VTOL were found to be working normally.  No electrical damage has been observed.

- Damage to fuselage, tail boom, wing tip right and left, and center wing observed (see pics)
[embedded: Wing Tip Left.png]
[embedded: Wing Tip Right.png]
[embedded: Fuselage 1.png]
[embedded: Fuselage 2.png]
[embedded: Tail Boom 2.png]
[embedded: Center Wing 1.png]
[embedded: Air Data Pod missing.png]
[embedded: Tail Boom 1.png]
Air data pod is missing

- Main battery holder is loose

### Samuel Lopez, 2025-12-29

Material Disposition has been given to Lauren Velasquez, which she will give to customer.  Awaiting to hear if they want to fix the AC.

### Jackson Riley Curvin, 2026-01-20

Closed on Global support side report finalized quote, and report to PM

## Attachments (14)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| DoD SAFE-DqATqc4viFoq5NWc.zip | archive | 120108 | 2025-05-13 | listed only |
| 1612a8c2-c1e9-4a7a-b01b-d1f1917829f7.jpg | image | 28 | 2025-05-14 | listed only |
| 16d3ef81-5d84-40ba-86a4-cf605557907a.jpg | image | 32 | 2025-05-14 | listed only |
| 2c27dd7b-5283-4029-ac33-7ecfc453bf35.jpg | image | 40 | 2025-05-14 | listed only |
| d776f9d4-b1cf-4593-859b-ae2958ead904.jpg | image | 19 | 2025-05-14 | listed only |
| Air Data Pod missing.png | image | 24310 | 2025-12-16 | listed only |
| Center Wing 1.png | image | 20808 | 2025-12-16 | listed only |
| Fuselage 1.png | image | 11701 | 2025-12-16 | listed only |
| Fuselage 2.png | image | 11785 | 2025-12-16 | listed only |
| Tail Boom 1.png | image | 30456 | 2025-12-16 | listed only |
| Tail Boom 2.png | image | 14103 | 2025-12-16 | listed only |
| Wing Tip Left.png | image | 10874 | 2025-12-16 | listed only |
| Wing Tip Right.png | image | 10272 | 2025-12-16 | listed only |
| [VXEP-1278_VXE-541_Vehicle Investigation_20260122.pptx](attachments/56414_VXEP-1278_VXE-541_Vehicle%20Investigation_20260122.pptx.md) | pptx | 139082 | 2026-05-12 | converted |
