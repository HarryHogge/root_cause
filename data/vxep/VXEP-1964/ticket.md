# VXEP-1964: Nail down Hadron design incorporation

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2026-07-16
- **Updated:** 2026-08-14
- **Resolved:** 2026-08-14
- **Reporter:** Josh Adams
- **Assignee:** Connor Peebles
- **Creator:** Josh Adams
- **Parent:** VXEP-1786 UAP Block 30 Adv Nav Hardware
- **Links:** relates to VA-2712 (100-112838 Hadron Carrier Board Obsolescence)
- **Epic Status:** To Do
- **Epic Color:** ghx-label-12
- **Issue color:** grey

## Plan

Threshold:
Wiring changes for new Hadron board. See https://jenaero.sharepoint.com/:p:/s/IRAD/IQBnnrb5qeQ-S53o1nwyWZkBAWTTYgISb9Clfdn7-2qrvnY?e=q69D6R
Objective, still need to determine if in scope or not: 
- Battery for MCM internal or external to avbox (plenty of related Jira to link for background). Battery for MCM internal or external to avbox (plenty of related Jira to link for background). Greg previously said this was out. Asking if it is back in consideration due to the need for Hadron swap and run out date ?

Likely out (seems not to operate the way we want)
- utilizing the new Power/Wake switch instead of switching MCM power through the SLA breakout 
- The Power/Wake switch is a momentary ‘pull down to GND’ to turn on the MCM. Currently the SLA Breakout controls power to the MCM with an active high pull up to the Efuse on the SLA Breakout Board from the XCOMM.
- There is potential here if we are willing to accept a firmware change to the XCOMM to do the momentary pull down to GND on the Power/Wake switch of the MCM

## Comments (3)

### Cameron Chapman, 2026-07-23

Background info: 
Connor reminded me that the XCOM battery is rechargeable. The problem previously encountered was that customers would leave avboxes unpowered for too long, which deep cycled and killed the battery. We could fix this with a doc/training update to power on equipment every (X weeks-he is checking duration) if feasible,.
 
For the MCM, there is a battery+harness connect tech sells designed to plug into the hadron. This would be easiest to implement and seems doable for UAP boxes. 
 
Any externally accessible one will require either giving up previously allocated pins on avbox connector and harness changes, or adding a new port/hatch to the avbox. Seems out of scope for initial UAP, but let us know if you recommend otherwise.

### Cameron Chapman, 2026-07-23

sounds good. I heard MCM battery was in consideration. Any others? 
Are you leaning internal or external yet? 
do you think worth evaluating sharing the battery with the XCOM, or different voltages/not worth it
 
absolutely but considering our time restraints we probably won't have time to rig up an external battery arrangement, but we'll include it in our proposal
 
Also thought about utilizing the new Power/Wake switch instead of switching MCM power through the SLA breakout, but turns out it doesn't quite operate the same
 
[embedded image-20260723-180834.png]
From ConnectTech:
 
[embedded image-20260723-180840.png]
From Nvidia:
it looks like connect tech forces it to operate that way when it could have been alot more useful to us a different way. If only we designed our own Hadron board

### Connor Peebles, 2026-08-14

result: do not pursue battery or sleep/wake function for UAP. Proceed with integrating the HadronNGX024

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20260723-180834.png | image | 146 | 2026-07-23 | listed only |
| image-20260723-180840.png | image | 24 | 2026-07-23 | listed only |
