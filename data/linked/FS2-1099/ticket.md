# FS2-1099: v401 RACE condition investigation

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2023-10-28
- **Updated:** 2023-11-08
- **Resolved:** 2023-11-08
- **Reporter:** David Grosher
- **Assignee:** Jason Scherer
- **Creator:** David Grosher
- **Parent:** FS2-752 Vehicle Incident Investigation Support
- **Links:** relates to VXEP-146 (VXE-401 Loss of operator control during aborted landing); is blocked by FS2-1151 (Land Immediately during launch abort prevent position updates); relates to VA-796 (Investigate VXE-401 loss of control)
- **Epic Link:** FS2-752
- **Sprint:** FS2 Sprint 9

## Description

**Bug Description**

The current firmware allows for the operator to issue a land immediately command after a launch abort has been started. This sequence results in the autopilot getting stuck in an attitude update only mode. This causes the vehicle to drift horizontally as it descends to the ground until it lands. 
**Preliminary Analysis of the v401 flight data**

[embedded: VXEP-148 Preliminary Analysis.pptx]
**HIL Recreation**

- Start a normal launch sequence.
- After a few seconds (give yourself some altitude, ~50 or more feet, to provide time for the next command) abort the launch.
- Issue the “Land Immediately!” command from the GCS before the aircraft lands.
- The aircraft will now be in attitude update mode, and it will have a horizontal drift on descent. The severity of drift will depend on the altitude you issued the land immediately command from.
- Chart VTOL field fmMc to see what update mode the autopilot is in during descent. Mode 6 is Position Update. Mode 4 is Attitude Update
Multicontrol update modes shown in array below for reference
[embedded: image-20231101-233925.png]

**Resolution Potentials**

- Disable Land Immediately: The idea has been proposed that we should not allow the land immediately command when the aircraft is already in a launch abort situation. This would prevent the additional RTL situation which caused the undesired behavior.
- Kurt Suggestion: Update the FW AP to prevent a second land now trigger.
- Sticky Landing State: The reason the existing firmware doesn’t handle the two aborts is due to a sticky landing state. During RTLs (Return to Landing) situations, which are caused by the abort type commands, the aircraft temporarily gets into a global altitude hold mode that causes the aircraft to update attitude instead of position. For this flight, the first abort puts the aircraft into a active landing state. When the second abort happens the code that would put the aircraft back into position update mode doesn’t execute because the aircraft is already in a landing state. This is what results in the aircraft remaining in attitude update mode.
- One solution is to remove the check to see if the landing state has already been activated before activating the position update mode. I create a patch to validate this approach, and I was able to resolve the landing drift issue this way. The update involves commenting out lines 151 and 152 in file MultiLand.c (Repo: autopilot_202).
- Another solution is to turn off the landing state during an RTL situation, so that the landing software re-initializes correctly. This approach could have larger farther-reaching impacts.
- Attitude mode during ALT HOLD?: The other consideration is to question the reasoning for switching to attitude update mode when the altitude hold is applied to the aircraft. This is what caused the 401 flight to switch out of position update mode on landing in the first place. If this didn’t occur the aircraft would have stayed in position update mode the entire descent.

**Final Solution**

Modify the FW AP function hostintf::CommandRecover() to not allow a recover to occur during a launch abort. If the Land Immediately command is issued during a launch abort this update will prevent it from restarting a landing which causes the aircraft to get stuck in an attitude update mode resulting in the horizontal position drift.
Git Repo (fixed-wing-ap) commit hash: 4edead9
edgeautonomy / fixed-wing-ap / Commit 4edead98a5ce — Bitbucket
[embedded: image-20231106-212151.png]
Also, the VTOL log will indicate that the second abort was rejected as below.
[embedded: 3bc2b47f-b75e-407a-9878-c146e1c8121b.jpg]

## Comments (1)

### Jason Scherer, 2023-11-08

Investigation complete.
Investigation report completed and attached to https://jenaero.atlassian.net/browse/VXEP-146.
Bug incident created https://jenaero.atlassian.net/browse/FS2-1151.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [VXEP-148 Preliminary Analysis.pptx](attachments/17148_VXEP-148%20Preliminary%20Analysis.pptx.md) | pptx | 3022 | 2023-11-01 | converted |
| image-20231101-233925.png | image | 199 | 2023-11-01 | listed only |
| 3bc2b47f-b75e-407a-9878-c146e1c8121b.jpg | image | 17 | 2023-11-06 | listed only |
| image-20231106-212151.png | image | 36 | 2023-11-06 | listed only |
