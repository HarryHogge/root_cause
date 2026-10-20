# VXEP-433: VXE3Std - Wing Utility Drop - Prototype Feedback

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-06-11
- **Updated:** 2025-01-29
- **Resolved:** 2025-01-29
- **Reporter:** Greg Fryer
- **Creator:** Greg Fryer
- **Labels:** Gen1-Utility-Dropper
- **Parent:** VXEP-337 Create, Test, and Release VXE30 Standard Config Wing Utility Drop
- **Epic Status:** To Do
- **Epic Color:** ghx-label-6
- **Issue color:** green

## Description

- Thicken up the mounting ridge (found in Eng)
- Create a notch for the wires to exit between pylon and ring
- Re-finish pylon harness wtih TE369 connector (easier to use in field) and appropriate heat shrink or braid.
- Provide extra parts in FSK (GF: Just in the case) including extra nylon bolt/washer.
- Wiring
- Label wires for right and left to ensure GCS drop configuration consistency.
- Extend one set of wire 2-3” to ensure sufficient length after installation. (See attached photo)
- Place label or sticker on release button. It is hard to see when installed.
- Label attachment lug for direction of flight.


SOFTWARE FEEDBACK: (May need separate tasking or move to FS/GCS project)
- Software (from Dana)- The color code system on the GCS “Custom Payload” page shows disarmed if the page is closed. We did not test to determine if the dropper was actually disarmed.
- There was a popup asking to arm the droppers even when manually armed. Clicking Ok may have caused the early drop on drop 2. 10th will share log data.
- Is it possible to build a minimal drop profile to ensure the flight plan meets the minimum 200m ground track requirement? We had two early drops possibly due to initial ground track waypoint being too close to the drop waypoint.
- Map data and DTED were minimally useful for planning. They should have the ability to upload 1m DTED/imagery to enhance flight planning.

SW Narrative:
The  VXE30 software requires a few updates from the drop mission planning aspect.  At rehearsal on Sunday, one mission was planned to perform a dry run to see where the aircraft was positioned relative to its drop point. We had to be precise as AO was tight and had lots of people/property. The event waypoint was selected to “event off” for our drop location and the payload was not armed. The operator (who was flying and not part of any of our practice sessions) selected ok in the arm payload pop-up when advised not to, which caused the event waypoint to become active and drop the payload despite the precautions we took while setting up the mission. The software must be fully representative of what the operator has selected for the settings in the software. If it isn’t and our customers start performing live fire drops, it will become a big safety issue. The arming pop-up window should either not appear or have no function if the event waypoint is selected to “event off”.
 
The drop payload mission conducted for the demo was late due to the operator placing the ground track end point over the event waypoint. The software was never able to register the event waypoint as both waypoint types were  too close in proximity although we had advised the operator multiple times to adjust mission set. Although the release was 200m late for our mission plan as we had to manually drop, there was no referenced target we were trying to hit for those spectating. We had demonstrated the ability to hit close to target the day prior coming within 3ft of a soccer net. 
 
As the drop payload missions become more common, the need for higher resolution DTED data and accuracy becomes more important from both the VXE software and the gimbal software. The lowest version DTED in the VXE software I believe is 10m, followed by 100m then 1000m. This means the highest margin of error with event waypoints could be near 16.5ft with the lowest resolution DTED, not including the published lateral fixed wing waypoint capture variations in windy or convective environments. Higher DTED will allow us to provide more lethal and successful drops while hopefully being able to remove the higher DTED resolutions that are taking up SGCS hard drive space and causing a greater latency when downloading maps. In the current configuration, maps still have to be downloaded to both Trillium and Epsilon gimbals which requires additional memory from the computer.

## Comments (2)

### Greg Fryer, 2024-06-11

@David Grosher @Ted Trowbridge Can you please review the software portion of the feedback on the droppers? I am sure some of this is a much more extensive project (e.g. the 1m DTED is a lot of data, and also there was discussion that it’s distribution is (or at least was) controlled in some way). That said, some of the drop waypoint functionality (enforcing the ground track being in a valid/good location) might be simpler.
The wing drop kit for standard is on it’s way towards production, so this will be needed. I think the state is “it works” but could be a lot simpler. If you move tasks to other epics (in FS2 or GCSS?) please link here.

### Dana Holley, 2024-06-20

@Greg Fryer You are correct in your assessment of the 1m DTED. There is a correction in my report referring to software DTED resolution being a minimum of 10m. It’s actually far greater at 30m resolution. 10m or 1/3 arc second would be the best suited, depending on laptop memory available. I know this 10m resolution isn’t restricted based on other platforms that I’ve flown.

## Attachments (0)
