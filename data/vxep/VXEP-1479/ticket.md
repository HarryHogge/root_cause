# VXEP-1479: Loss of link RTB HIL SIM (VXE-765)

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-08-19
- **Updated:** 2026-03-02
- **Resolved:** 2026-01-14
- **Reporter:** Jackson Riley Curvin
- **Assignee:** David Grosher
- **Creator:** Jackson Riley Curvin
- **Labels:** TIQUILA
- **Links:** relates to VXEP-1477 (VXE-30 RTB to undesired and un-commanded location); relates to FS2-3583 (Loss Comms RTB Test)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** HIL SIM
- **Corrective Action:** Fixed the log bug on FW AP in v6.6 release.
- **Plan:** Complete
- **Issue Status:** Resolved
- **Severity:** 3 - Degraded Performance - With Workaround
- **Components (EA Aircraft):** Aircraft, full assembly

## Description

Apologies for the high priority urgent meeting
 
We’ve been looking at the RTB during Link Loss based on the issue that was observed with the RTB sim.
 
During investigations on both Jennings (TO1) and OGCs/VCSi (TO2), the following has been observed:
 
When the aircraft is at a waypoint about 20km away from the landing zone, and Link Loss action has been set to RTB. When Link loss is initiated, the AV flies the path towards IP1, however about 10-15 minutes in, the AV starts descending towards IP2 instead, and completely misses IP1. There have been instances, where the AV has not even reached IP2, possibly due to maybe hitting terrain?
 
We have seen this issue on 6.5.0 GCS SW and OGCS 1.3.0 and VCSi beta 2 for OGCS/VCSi (TO2) and 6.5.0 for Jennings (To1)
 
We’re going to try and test this on the HIL with 6.4.0 too
 
UK flying has currently been restricted to VLOS and range no greater than 2km

## Root Cause

Waypoint capture logic is flawed at 19.98km and factors of 2 distances greater than that resulting in premature capture of waypoints at any point in the mission plan.

## Comments (20)

### Jackson Riley Curvin, 2025-08-20

@David Grosher apologies for the mix up the description was wrong for the ticket it is now corrected 
FYSA @Pat Wells @Drew Hildreth

### David Grosher, 2025-08-20

@Jackson Riley Curvin If you could get the mission that they used and then try to recreate the issues on our own HIL that would be helpful.

### David Grosher, 2025-08-20

In general, I’m having troubling linking MCM events to the XCOMM event log to see that the described test was actually performed.  
AAR_V765_20250819T100435Z: Launch Abort
AAR_V765_20250819T132234Z: LOS test appears to end early
AAR_V765_20250819T171334Z: This is NOT the described test case. Appears to be a Land Immediately at too high of an altitude. 
In the VSM event log we appear to detect landing while flying to IP1:
```
01:53:44.977958:  ap_msg          Mission Status Update - Active Waypoint: 11000
01:55:55.997917:  vsm_msg         Landing detected
```
It would be expected to transition to IP2-5 prior to detecting landing.

### David Grosher, 2025-08-20

@Scott Whitney This is a high priority incident for TIQ. They are not currently flying the fleet beyond visual line of sight. Can you have the SQA team create a test point where the following occurs: 
- Fly a mission where a portion of the mission is on the other side of hills or mountains.  LoS response should be RTB.  And Auto AGL should be enabled.
- Cause a LoS event by disconnecting the ethernet to the GCS.
- Observe the response of the aircraft. 
- Does it avoid the hills/mountains between the AV?
- Does it transition to IP2 prematurely?
- Does the simulation complete to landing at the origin?

Please run this test twice where the hills/mountains are inside the VTED region and then a second time where they are outside the VTED region.

### David Grosher, 2025-08-20

@Jackson Riley Curvin Can you clarify with the TIQUILA team their test setup. Specifically, I want to make sure that when they disconnected comms from the GCS that they didn’t inadvertently disconnect the HIL from the XPLANE simulation. Our setup in our lab has those on the same computer which makes LOS testing a bit nuanced. The datalogs seem to end prematurely and I’m not sure if it is the wrong dataset or an issue with the test setup.

### Jackson Riley Curvin, 2025-08-20

@David Grosher I reached out to TIQ awaiting their response

### Jackson Riley Curvin, 2025-08-20

@David Grosher i just received this from the customer and i added a video

So we did it a number of way but in all instances xplane and the HIL AV was still connected.
 
We also were able to replicate it which was also what’s seen in the video with the system still connected but no one in control so the Loss comms timer comes up and and does everything. I’ll have to see if I can grab the mission tomorrow but the way we did it was at SLO county airport we took off and put a 10 minute ish orbit at 5000ft AGL quite close to take off then placed the PLZ about 23KM west onto the sea with IP1 at 5000ft AGL and pattern alt 400ft AGL
 
There is a few copies of different times on there. The one with the latest timestamp was from the video run where I screen recorded it

### Logan Wright, 2025-08-20

[embedded image-20250821-010429.png]
I was able to repro the issue (based on my understanding of the description) as seen with the green flight trail on BLK30 with 6.5.1 builds. I put the PLZ ~20km away from takeoff location, disconnected from vehicle in-flight triggering LOS mission (which is configured to RTB to PLZ), and watched the path in X-Plane. The mission was planned around Camp Roberts and the terrain has some hills, but it’s mostly flat. Here’s a zoomed-out view of the terrain map where the mission covered:
[embedded image-20250821-010923.png]
I reconnected the vehicle to the GCS while flying to track the vehicle path and it still performed as described (missed IP1 waypoint). I will try to recreate again in a different direction at Camp Roberts to get to a more mountainous terrain and adjust PLZ orientation. The orientation of my PLZ is currently “worst-case” where IP1 is positioned just outside the orbit and beyond the trajectory of the vehicle. The next flight will target a similar “worst-case” situation where the vehicle will not happen to pass through IP1 on its way to orbit.
AAR, if desired:
[embedded file]
 @Scott Whitney @David Grosher

### David Grosher, 2025-08-21

@Logan Wright You might be able to use the OGCS 3D mode and overlay to visualize the elevation in the local area to ensure you can place the PLZ behind terrain. 
If we do indeed confirm the bug then the next step is to confirm a workaround, which I think is changing the settings for LOS to follow the LOS route and update that as required during a mission to ensure flight to the initial LOS waypoint is safe from the current position.

### Jackson Riley Curvin, 2025-08-21

@Logan Wright @David Grosher 
[embedded file] [embedded file] [embedded file] [embedded file] [embedded file] 
We re ran this again with the same results, part way of the journey to IP1 the active landing moved to IP2, We left the AV flying until it landed. Lucky were we put these landing patterns had a nice valley so the AV didn’t hit terrain but did go down to 400ft AGL
 
This was all done with VCSi and OGCS. VCSi was just used to upload the landing pattern, route and set loss link action. After that we launched with OGCS waiting for the AV to get into the 1 WP mission of an orbit then released control in OGCS and waited for it to RTB

### David Grosher, 2025-08-21

@Jackson Riley Curvin Thanks for confirming. We do need to put the PLZ behind some hills or mountains because the aircraft does access the elevation model to make some decisions. I want to be sure that it isn’t transitioning to IP2 early simply because it knows it can do that safely.

### Jackson Riley Curvin, 2025-08-28

@Josh Burrell

### Jackson Riley Curvin, 2025-08-28

@Greg Fryer @David Grosher @Pat Wells are we still planning on releasing 6.5.1 with this known issue? My understanding @Josh Burrell already sent the SB and ASA to Sam for his approval.

### David Grosher, 2025-08-28

@Jackson Riley Curvin Yes. We can’t resolve every issue with each release.

### Josh Burrell, 2025-09-02

@David Grosher So the ASA we just wrote for 6.5.1 needs to be rewritten to address this issue as well? I’m going to need to get the write up from someone along with the corrective action. Who can help me with this?

### David Grosher, 2025-09-02

@Josh Burrell This is unrelated to the ASA that was just written. We don’t have a solution for this at the moment. I would think this would be an AN. Also, we still have to fully characterize the issue.

### Alexander Alan Arnold, 2025-09-02

@David Grosher @Logan Wright LM encountered issues while conducting LOS workaround, I have added a video and an attachment labeled LOS workaround issue in the ticket. I have also added the AAR from the observed issue today labeled LOS-Mission-IP2-40KM

### David Grosher, 2025-09-02

@Ted Trowbridge FYSA

### Alexander Alan Arnold, 2025-09-03

@David Grosher Dhruti completed testing after the JSMT I uploaded her email in the attachments section of the ticket “LOS follow up after JSMT” data will be loaded shortly, SIM data flown after JSMT meeting has been updated

### David Grosher, 2026-01-14

@Jackson Riley Curvin This is resolved with v6.6

## Attachments (17)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V765_20250819T100435Z.zip | archive | 14826 | 2025-08-19 | listed only |
| AAR_V765_20250819T132234Z.zip | archive | 13980 | 2025-08-19 | listed only |
| AAR_V765_20250819T171334Z.zip | archive | 25995 | 2025-08-19 | listed only |
| IP1 and IP2 Issues.mp4 | video | 8744 | 2025-08-20 | listed only |
| T95_V111_250820_172840_pack.zip | archive | 1224 | 2025-08-20 | listed only |
| image-20250821-010429.png | image | 284 | 2025-08-20 | listed only |
| image-20250821-010923.png | image | 1720 | 2025-08-20 | listed only |
| AAR_V765_20250821T133456Z.zip | archive | 19788 | 2025-08-21 | listed only |
| [Contingency A_3.json](attachments/31638_Contingency%20A_3.json.md) | text | 1 | 2025-08-21 | converted |
| [Flight_6.json](attachments/31636_Flight_6.json.md) | text | 1 | 2025-08-21 | converted |
| [PersistedLandingPatterns.json](attachments/31634_PersistedLandingPatterns.json.md) | text | 3 | 2025-08-21 | converted |
| archive_20250821_133838.zip | archive | 849 | 2025-08-21 | listed only |
| LM video for LOS issue.mov | video | 2815 | 2025-09-02 | listed only |
| [LOS Workaround issue.pdf](attachments/31955_LOS%20Workaround%20issue.pdf.md) | pdf | 343 | 2025-09-02 | converted |
| LOS-Mission-IP2-40KM.zip | archive | 1839 | 2025-09-02 | listed only |
| [LOS follow up after JSMT.pdf](attachments/31983_LOS%20follow%20up%20after%20JSMT.pdf.md) | pdf | 906 | 2025-09-03 | converted |
| 9325-LossCommsMission.zip | archive | 36119 | 2025-09-04 | listed only |
