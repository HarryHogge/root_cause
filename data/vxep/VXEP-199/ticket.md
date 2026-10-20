# VXEP-199: VXE376 Damage During Attempted Takeoff (VXE300 Booms)

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-11-22
- **Updated:** 2025-03-22
- **Resolved:** 2025-03-22
- **Reporter:** Cody Smisek
- **Assignee:** Cameron Chapman
- **Creator:** Cody Smisek
- **Links:** blocks XKIT-673 (X-Kit System Testing & Prototype Flight (<55lbs)); blocks XKIT-741 (Baseline VXE30 Testing); is blocked by VA-867 (Investigate and resolve SW issues from VXE376 (300 Booms) for drop payload test.); is blocked by VA-868 (Investigate lift/control issue from VXE376 (300 booms) flight (hardware focus)); relates to VXEP-209 (Engineering assets should have logbooks, qualification for flight, inspection processes, assigned asset owners. ); relates to VXEP-215 (Verify lift motor production drawings for alignment notes)
- **Vehicle Tail Number:** VXE376
- **Vehicle Configuration:** 376 with 300 booms and modified 376 VXE30 centwering with drop payload
- **Incident Type:** Aircraft Damage
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

From: Artis Bertulis <abertulis@edgeautonomy.io>
Sent: Tuesday, November 21, 2023 2:24 PM
To: Scott Stuckey <sstuckey@edgeautonomy.io>; Jason Scherer <jscherer@edgeautonomy.io>; Cody Smisek <csmisek@edgeautonomy.io>
Cc: Ruysser Gabler <rgabler@edgeautonomy.io>
Subject: Payload drop flight test attempt
 
Hi all, see my notes of today's testing below.
 
I’ll summarize them in a test report next week, so for now they’ll live here.
For flight data go to flight ops condor – flight test data
Videos will be uploaded later today at Flight Ops condor – videos and pictures – folder with today's date.
 
Test performed with:
- AC 376 (with 300s lift booms and tail boom)
- Wing mounted payloads
- Center drop payload mechanism with no payload
- XE25 battery
- 6.1.2 software
- Autopilot FW 6.05m / csum C4D9
- Xcomm 4.67 / csum 154F
- VTOL 1.53 / csum initially E807, then 6799

 
- The aircraft was missing a tail in the morning, but Scott managed to gather parts and Frankenstein 1 whole aircraft
- The center wing LED button was blinking red indefinitely when powered up, which is probably caused by the custom configuration for arming/dropping. 
The problem with this is that it blinks in the same way that it blinks when VTOL system is armed, and telling “do not approach me”, so this creates a safety risk, as there’s no clear indication on whether it’s armed or not.
Spent some time looking into it and tested if pressing “Safe” for the VTOL system in the webpage changes the blinking light – it didn’t. Checked the code again and couldn’t find an issue.
Decided to go along with it and be safe (only putting booms on in a safe area with no one around, being ready to disarm if needed, and being cautious about the VTOL speed controller beeping for system arming indication), but with a request to not have this issue before the next time we’re flight testing.
- VTOL checksum was also different (E807) from what it is by default (6799), with the help of Carson we compared the VTOL gains with a default configuration and didn’t see any problem with it. The different checksum is probably caused by custom arming/dropping configuration
- Scott mentioned that the actual dropping wasn’t tested before today (the day of the test), which might not be true, nevertheless, we’ll try out the function and ensure it arms/releases
- The flathead bolts on the payload plate for the drop payload cause the center panel to not sit flush with the fuselage
- A few of the lift boom bolts holding down the motors and ESCs were loose, went over all the bolts to ensure they were installed correctly, and checked the props as well.
- The total weight of the aircraft with both wing drop payloads installed (and an empty center payload drop mechanism) was 51.9 lb with the VXE30 main battery and HLB. Will have to change the configuration to an XE25 main battery with foam inserts.
Changing the battery brought the weight down to 48.3lb and cg was 4.9
- Front left lift motor aligns in the opposite direction (blade facing forward)
- 10:45 – passed launch wizard check and a hover test with the drop payloads on
- 12:40 – passed launch wizard at Huasna, attempted take-off – failed. All lift motors started but the aircraft just pitched forward and didn’t take off the ground, fell out of the stand, and broke one lift prop until cut and safe was commanded.
- Replaced the prop, attempted to do RC hover, lift system made louder than usual noise coming from left boom when over 30% of the power.  The same sound was observed during failed take-off.
- Removed the wing-mounted drop payloads and did RC hover to see if any difference – still the same sound present, aircraft seemed to tend to pitch forward, RC pilot had to pull it back to keep it level.
- Re-flushed the VTOL firmware to attempt a hover to see if any difference with this aircraft in the default setup
- 13:30 – Hover sounded about the same, still pitching forward
- With the VTOL FW reflashed all FW and checksums now were correct, but the center panel red LED was still blinking red even without the custom config, so there might be something else wrong with it.
- To ensure that props are not at fault (sounded like the rear right was making noise), decided to swap rear left CCW to front right CCW propellers to see if the sound now comes from the left side or remains at the right side.
- Sound still came from the left side
- Did the same with CW props
- No loud noise after swapping CW props, interesting…
- Swapping the CW props back and replacing the HLB to do another hover to see if the noise is back with the props the way before.
- The noise was back
- Swapping CW blades back to the position that didn’t make any noise just to make sure
- If previously the noise was present at like 50% of the power, with CW blades this way the noise was present at around 75% throttle
- Added wing-mounted payloads to add the weight to see if that increases the noise
- Still seemed the same during hover, observed a lot of wobble in the left boom, almost seemed like it was wiggling.

14:20 Test called off, will proceed upon further inspection
 
Fix before next time:
- Blinking red center wing light
- Loud noise/wobble for the left boom
- Paint the other one of the lift mounted drop payloads blue
- See if the center drop payload mechanism bolts that do not allow the center wing to sit flush with the fuselage could be adjusted/changed to have the wing flush

## Corrective Action

https://jenaero.atlassian.net/browse/ENGINF-195 
https://jenaero.atlassian.net/browse/VXEP-215

## Plan

Software
- Investigate resolve SW issues https://jenaero.atlassian.net/browse/VA-867

## Issue Status

System was hover tested after correct orientation of motor mounts implemented. RC pilot reported aircraft more stable and controllable. 
Shop hover video (post root cause correction) located here. \\192.168.10.5\Flight Ops\Videos and Pictures\2023\12.07 Shop Hover 376
Flashing CW LED was confirmed to be related to dropper configuration (enabling the dropper lines). Jason is working on determining next steps to not have LED flashing with this config. This will need to be corrected for X Kit.

## Root Cause

Front Left lift rotor mount (mount interface between lift rotor and motor) was incorrectly oriented likely resulting in blade imbalance and loss of lift. 
Flashing CW LED due to dropper config in VTOL FW.

## Comments (5)

### Cody Smisek, 2023-11-22

@Cameron Chapman @Carl Graf @Scott Stuckey @Artis Bertulis @Jason Scherer

### Cameron Chapman, 2023-11-24

@Hayden Jeanor @Cody Smisek @Artis Bertulis Here is what I recommend for troubleshooting. I also made a table to summarize motor issues observed and likely causes. 
- Repeat hover test with new booms to see if issues repeat.
- If not, inspect FL ESC for damage
- If no damage, test FL motor on the dyno.
- Replace FL motor and retest.


| Issue | Potential Causes/Indications |
| FL motor aligns in wrong direction | Likely wrong wiring. Could also be FW or bad position sensor |
| Passed hover test | Indicates motors are spinning in the right direction and providing lift |
| Aircraft pitches forward on takeoff | Problem with one or both front motors, or gains, or CG. |
| Replaced prop. Noise from left boom | Issue with front left motor. |

### Carl Graf, 2023-12-05

@Cody Smisek @Jeremy Kostel can either/both of you help out with the investigation?

### Cody Smisek, 2023-12-05

@Carl Graf It’s on my list of things to support this week. Just haven’t got to that part of the list yet.

### Jason Scherer, 2025-03-22

@Carl Graf @Cameron Chapman @Cody Smisek Can we close this ticket? Seems like we know the cause. The only open action is https://jenaero.atlassian.net/browse/VA-868 which has two sub tasks that are done.

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V376_231121_124023_pack.zip | archive | 1150 | 2023-11-22 | listed only |
| T95_V376_231121_132609_01_pack.zip | archive | 1415 | 2023-11-22 | listed only |
| T95_V376_231121_132609_02_pack.zip | archive | 1776 | 2023-11-22 | listed only |
| T95_V376_231121_132609_03_pack.zip | archive | 2204 | 2023-11-22 | listed only |
| T95_V376_231121_132609_04_pack.zip | archive | 2564 | 2023-11-22 | listed only |
| T95_V376_231121_132609_pack.zip | archive | 972 | 2023-11-22 | listed only |
| VID-20231121-WA0000.mp4 | video | 2591 | 2023-11-22 | listed only |
