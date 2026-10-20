# VXEP-1230: VXE 401 Lost Connection After Mission Sync

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Low
- **Created:** 2025-04-28
- **Updated:** 2026-01-20
- **Resolved:** 2026-01-20
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Drew Hildreth
- **Creator:** Alexander Alan Arnold
- **Labels:** Weekly-incident-tracker
- **Links:** relates to VXEP-1307 (SB40x - N376VX: Network Issue); relates to VXEP-1310 (VXE689 - Network Issues); relates to XKIT-4730 (SB40x - N376VX: Network Issue)
- **Vehicle Tail Number:** VXE 401
- **Vehicle Configuration:** VXE 30, Battery Config, Vidar, Trillium Gimbal
- **Incident Type:** Mission Failure/Abort
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

OPERATOR STATEMENT
We were flying Stalker with Vidar. After a mission sync, we lost connection to the network internal to the aircraft. We still had good coms to the Silvus on the bird but could not ping the XCOM, VTOL, Gimbal, Payload, SA...
 The Stalker did its lost coms procedures well and landed safely. Once landed before power cycling battery I plugged into the Stalker via the Alden breakout cable. I was able to ping everything on the aircraft side (XCOM, VTOL...) but was unable to ping the Silvus.
 We did a variety of tests on the ground and got the issue to repeat if at least 2 of the 3 ip (192 space) based LWIR cameras were plugged while both lift booms were also plugged in. The Vidar hood payload also needed to be plugged into the hood port prior to powering up the aircraft with the battery. [So, if 0-1 boom were plugged in we couldn't repeat it, and if only 0 or 1 cameras were plugged in the problem wouldn't happen.] It was very repeatable last night with these rules. we power cycled probably 40 times to check.
 What is extra strange is that today we tried to repeat this problem and we couldn't... until we used Aux1 Aux2 payload power cycle through custom payload control. We are still tinkering away with what is causing this.
 
The Skylink gets the unicast feed from the SA camera. Skylink has a bug where they are not properly closing the unicast port to the SA camera when you close the application. When you reopen Skylink it opens a brand new port to the SA camera. If a user closes and reopens Skylink 4+ times they can really bog down the link and cause serious problems. The only way to clean up the traffic is to power cycle the entire aircraft. A user could configure Skylink to not pick up this feed but no one is going to go out of their way to do that. Is there a way we could have a power switch for the SA camera to fix this? It would be ideal if Trillium fixed their software, but still.
Yes, when the issue to occurs, we can see the Silvus of the aircraft but are unable to ping anything beyond the Silvus. And when you connect via a breakout Alden or Odu cable you can ping everything on the aircraft but are unable to see the SIlvus.
Another note is that the night Vidar was about 60ish Watts. We measured the power on the 24v line but never looked at the 12v toggle. We will look at that soon.
Attached are two previous flights we did. One with Day-Vidar and one with HD45. We had a HD40 on the Day-Vidar Stalker but I forget if it was plugged in on this particular flight.
Thanks,
Kendel
From: Cody Smisek <csmisek@edgeautonomy.io>
Sent: Monday, April 28, 2025 2:20 PM
To: Kendel Godfrey <kendel.godfrey@synergy-aero.com>; Pat Wells <pwells@edgeautonomy.io>; Alexander Arnold <aarnold@edgeautonomy.io>
Cc: Alex Jucan <alex@trinitybend.com>; Tom Carnes <tom@trinitybend.com>; Chris Joyce <chris@trinitybend.com>; Avery M. Mayfield <avery.mayfield@inl.gov>
Subject: RE: 401 Flight Issue Logs
Kendel
Can you confirm that when you describe the follow on troubleshooting, the ‘issue’ that is repeating itself is the loss of communications to the vehicle via Silvus RF? So for the 40 times that power was cycled, communications to AP via Silvus RF was lost (but still could see the vehicle Silvus node) when >1 boom and >1 camera connected?
Cody

Aircraft VIDAR and Trillium installed

5/20/25
- This happened on preflight just as we were about to launch
- The payload overheated a few times so we power cycled AUX-1/2 a few times to let it cool and turn the payload back on.
- I could ping the IPCOM from the Silvus Airside but not hardline in the Stalker.
- There was a gimble on the aircraft, its bitrate was 2.5-mbps.
- We tried replicating it three times afterwards and didn't get the issue to show up.

## Plan

- Operator to continue to troubleshoot. 
- last message received was that they were having difficulty replicating the issue again. Their next steps of diagnosis were to attempt to access ipcomm from direction connection to aircraft, I believe if this was to fail then this would indicate something going on with the network explicitly between xcomm and ipcomm.
I don’t think there’s anything further for us to do until they reply with additional information.
- 5/20/25 Customer Response - I could ping the IPCOM from the Silvus Airside but not hardline in the Stalker.
- 5/21/25 Asked Customer to verify: if they could connect directly after the initial incident, and if they can connect after removing the payload. 
Hold on below.
- Check data logs for network traffic. Dave or Jason’s Grafana playground. 
- Ask Jo Brown networking questions, troubleshooting ideas, thoughts on logs.
- Provide user ideas for testing, or hold until they test more.

## Issue Status

AAR for this issue is T95_V401_250426_191713

Numerous bus faults during VTOL landing. Probably unrelated. Current theory is gimbal stuck during retract resulting in increased current draw. 
[00:03:35.625 3871.625] DebugMsgInt VAux: 0
[00:03:35.626 3871.626] vaux fault
[00:03:35.627 3871.627] DebugMsgInt Bus Fault: 16


Current theory for lost comms issues, ipcomm is struggling for whatever reason in the identified configurations. loss of ipcomm would exhibit the same symptoms, inability to access anything through silvus and inability to access silvus through direction connection (ipcomm is the middle switch between xcomm and silvus). possible ground loop issues?
4/28-210pm: customer states, can access ipcomm via silvus RF, but unable to get to xcomm. (seems more like xcomm ethernet chip issue then)

## Comments (6)

### Alexander Alan Arnold, 2025-04-28

@Cody Smisek Ticket for Chris Joyce”s issues this weekend.

### Alexander Alan Arnold, 2025-04-28

Added a VIDAR flight and a TRILLIUM flight AAR. @Cody Smisek

### Cody Smisek, 2025-04-29

@Steve Gonzales @Cameron Chapman 
Looks like plan was updated and assigned to Steve. I haven’t heard anything further from the customer since yesterday, last message received was that they were having difficulty replicating the issue again. Their next steps of diagnosis were to attempt to access ipcomm from direction connection to aircraft, I believe if this was to fail then this would indicate something going on with the network explicitly between xcomm and ipcomm. 
I don’t think there’s anything further for us to do until they reply with additional information. Depending on how serious we are about supporting this configuration (VIDAR), probably worth reviewing the schematics/wiring diagrams (if available) of their hardware to verify any obvious design issues.
 
Here’s screenshot of network traffic on xcomm. Lost comms occurs at the drop off. 
[embedded image-20250429-203913.png]


Additionally, this ticket contains two separate issues. Recommend breaking out the Trillium issue and delegating to appropriate party.

### Cameron Chapman, 2025-04-29

Thanks @Cody Smisek. You are welcome to update the plan and other fields above to get everyone on the same page in the future. See above. 
FYI @Steve Gonzales sounds like we can hold on this for now.

### Drew Hildreth, 2025-05-20

@Cameron Chapman Customer sent another AAR from when this happened. I have uploaded it for review.
along with some notes that placed above in the Description.

### Cameron Chapman, 2025-05-20

@Drew Hildreth see plan field. Have we received any info if they were able to recreate or not. If unable to, then this seems low priority/closeable. 
## Plan

- Operator to continue to troubleshoot.
- last message received was that they were having difficulty replicating the issue again. Their next steps of diagnosis were to attempt to access ipcomm from direction connection to aircraft, I believe if this was to fail then this would indicate something going on with the network explicitly between xcomm and ipcomm.
I don’t think there’s anything further for us to do until they reply with additional information.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| HD45_V464_250425_092652_pack.changetozip | archive | 1471 | 2025-04-28 | listed only |
| T95_V401_250426_191713_pack.changetozip | archive | 3289 | 2025-04-28 | listed only |
| VIDAR_V401_250425_084031_pack.changetozip | archive | 783 | 2025-04-28 | listed only |
| image-20250429-203913.png | image | 218 | 2025-04-29 | listed only |
| T95_V401_250519_152201_pack.zip | archive | 1832 | 2025-05-20 | listed only |
