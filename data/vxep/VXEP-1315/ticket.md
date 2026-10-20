# VXEP-1315: B30 Systemic MCM Resets due to payload power

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** High
- **Created:** 2025-06-25
- **Updated:** 2026-10-14
- **Reporter:** Mike DeJesus
- **Assignee:** Drew Hildreth
- **Creator:** Mike DeJesus
- **Links:** relates to XKIT-4777 (2123714-01 SLA Breakout V3 - Rev B); relates to VXEP-1890 (VXE 902 - user power cycled aux 1&2 simultaneously, and lost comms with the A/C for ~2 minutes. CHAOS payload); relates to OGCS-612 (Payload Power Labels Unclear); relates to VXEP-1956 (VXE 880 MCM Reset inflight after gimbal power cycle); relates to VXEP-2005 (VXE 966 MCM reset led to uncommanded climb ); relates to MS-1684 (VSM: Accommodate MCM Restarts in Flight); relates to VXEP-723 (VXE 724 MCM reset when changing HLB, other potential issues); relates to VXEP-844 (VXE724 VTOL Climb Abort Lift System Fault); relates to FS2-3724 (Investigate MCM resets on V912.); relates to PLD-237 (SB30 Adv Nav 1003 - MCM Reset with Hoodtech Gimbal Connected)
- **Issue color:** dark_green
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Sharepoint repository: https://redwireglobal.sharepoint.com/:f:/r/sites/FlightSafety/Shared%20Documents/Incident%20Reports/VXEP-1315%20MCM%20Reset%20on%20E140%20Connection?d=w8f50ed2d94664f989d60b6fdf443ca3e&csf=1&web=1&e=gmSoVg
PPT for 8D report: https://redwireglobal.sharepoint.com/:p:/r/sites/FlightSafety/Shared%20Documents/Incident%20Reports/VXEP-1315%20MCM%20Reset%20on%20E140%20Connection/VXEP-1315%20MCM%20Reset%20on%20E140%20Connection.pptx?d=wb8edc8b9b4e045c384b9b05d9a271f65&csf=1&web=1&e=qo9Y4n
MCM reset measurements https://redwireglobal.sharepoint.com/:x:/r/sites/FlightSafety/Shared%20Documents/Incident%20Reports/VXEP-1315%20MCM%20Reset%20on%20E140%20Connection/MCM%20Reset%20Measurements.xlsx?d=w44bdddff83cf48cf8a5f3db7e33d4068&csf=1&web=1&e=H7VaZp
Teams Chat: MCM Reset Containment/Advisory Notice | Group Chat | Microsoft Teams

Internal. Has potential to lead to MCM resetting mid-flight if E140 is power cycled through system software. ​
Repercussions of MCM resetting during flight: Automatically restart MCM & OGCS, initiate contingency behavior with AP. Lose mission plan.

## Corrective Action

Sort this list into done/to do/etv
- Additional solution already inadvertently implemented for B35 and B40 aircraft: Putting MCM on the CRITICAL bus isolates it from the E140 inrush
- Update based on status field above. Seems fixed on latest adv nav
- https://jenaero.atlassian.net/browse/MS-1684
- Remove both on/off command or tell operators of affected configs not to use it?

## Plan

Recent event seems to have a MCM reset with Avbox Rev H, which we thought was not vulnerable to this. Need to verify. [PLD-237] SB30 Adv Nav #### - MCM Reset with Hoodtech Gimbal Connected - Jira
Determine containment plan
Drew Hildreth Scott Lovett I think we have a better idea of which aircraft configuration and payload combinations are vulnerable to the MCM reset issue.  https://jenaero.atlassian.net/browse/VXEP-1315 

- In order to make a containment plan, I think we should answer the following: 
- Can anyone list which customers have what aircraft and payloads?
- If not, could any group start and document a process to lookup such info?

- Determine guidance for B30 aircraft without Avbox V4 2119959 Rev H, or if it happens with that one.   https://redwireglobal.sharepoint.com/:x:/r/sites/FlightSafety/Shared%20Documents/Incident%20Reports/VXEP-1315%20MCM%20Reset%20on%20E140%20Connection/Aircraft%20PN%20History.xlsx?d=w33642b7f7e574a9590eea2332d49e35d&csf=1&web=1&e=dyoXLO See 
- Risk exists when powering on 28V payloads. The payload power return is common with the MCM on certain avionics boxes.
- Payloads should be powered on one at a time in order (Aux 1, 2, 3). The reason I recommend this is Aux 2 is sometimes shared between a 12V payload and the hood. In that case, Aux 1 first would power the lower payload first and reduce inrush when Aux 2 was powered.
- Off in any order should be acceptable.
- If using a 12V Trillium payload, Aux 1 and 2 should be on and off shortly after one another (don’t operate with just one on).
- Ensure that 12V and 28V/Vbatt rtns/gnds are isolated from each other in payload.
- Determine limit for custom payloads (ex: inrush current/input capacitance/etc must be less than X to power on in parallel with other devices <Y to power on in parallel by itself)
- AV team investigation estimates it would take at least 2 weeks of dedicated testing time to come up with the range of values for the inrush. Once the test parameters are nailed down it can be applied to the other configurations relatively quickly
- Release customer notification document. See https://redwireglobal.sharepoint.com/:w:/r/sites/grptechpubs/Shared%20Documents/MCM%20Reset.docx?d=wdf5b791c77c5461692bdb5d4fd4a5905&csf=1&web=1&e=lHE2Re


- Questions Move answered to comments. 
- @Mike DeJesus were there any gimbal settings updates that can reduce the inrush current? 
- If so, what SW version?
- What is the containment plan for those?
- Questions for operators who have experienced this. 
- What PN and rev Avionics box do you have?
- Are 12V RTN and Vbatt/28V rtn isolated on your payload? They should be and can exacerbate this and similar issues if not.
- Can you measure the inrush current of your payload when connected to the aircraft/battery power? Reducing it should reduce the occurrence of this issue.

## Issue Status

5/29/26 Cleaned up plan. 
- Identify when HW fix was implemented and if any resets have been seen since. Need to gather data on which configs experienced these issues. 
- Summary: 
- Aircraft Affected: B30 Pre-MAGNSS to Adv Nav with Avbox V4 2119959 Rev G and before. Global support to execute this. @Alexander Alan Arnold  to coordinate.
- Payloads Affected: E140 regular before interface board, MWIR, E95. Potentially other customer ones with high inrush current, but none reported yet. @Alexander Alan Arnold  to coordinate.
- Send AN for affected customers. @Josh Burrell 
- Risk of MCM reset. Lose initial altitude. Cannot continue with current mission or upload new ones if it does reset.
- Potential COAs:
- If needing to turn off payload, don’t turn it back on.
- If needing payload operation and ok with risking MCM reset, include recommendation for what to do if that happens. Ex: Udrive remaining mission and RTB, or RTB direct?
- Affected configurations. 
- Block 30 Avionics generations. 
- Heritage Block 25 and 30. Not affected, no MCM. 
- 965-1-01-3100 Original PN. Latest rev E
- 107-111718 H Appears to be 3100 above with a different PN due to the improved SD card.
- Pre-MAGNSS Add PN:
- Has MCM. Likely affected.
- MAGNSS Add PN:
- Likely affected.
- Advanced Nav: 
- Affected: Avbox V4 2119959 Rev G and before. 
- SLA Breakout Board V2  MCM powered by payload vbatt+rtn (non critical)
- Avbox V4 2119959 Rev H-Changed to SLA Breakout Board V3 2123714-01 rev A https://redwireglobal.sharepoint.com/:x:/r/sites/JAI_Operations/Shared%20Documents/CCB%20Engineering%20Changes/Done/2025/ECN%20%23239,%20Replace%20SLA%20Breakout%20Board%20V2%20with%20V3%20in%202119959-01.xlsx?d=w672bf75a42bf45f3a08cfecfbb2e6d4c&csf=1&web=1&e=6iXfC0
- SLA Breakout Board V3 2123714-01 Rev A: Added decoupling capacitors. Significantly reduced the likelihood of such an event, but it could still be possible with a lot of payload capacitance/inrush current.
- 365: https://jennings-aeronautics-2.365.altium.com/designs/A7A69C91-B62C-45D7-A90A-F78C2D33D5CE
- B30C-planning on moving MCM to critical bus with 2163676 fuse harness and 2163675 branch cable update. 
- @Nigel Goodison  @Josh Adams  are you tracking anywhere what is in vs out for 30C?
- UAP
- could disable/bypass the Efuse. Does the power need to be switchable? Does it need to be fused? Would the aircraft be able to RTB and land safely without an MCM?
- Planned for UAP XCOM update. Not happening. Functions moving to XCOM in this task. Targeting UAP avionics. https://jenaero.atlassian.net/browse/AV-717
- Block 40
- Should be resolved, MCM is on critical bus, payloads on non-critical. Let us know if any issues with this version: Rev H Added to avbox dwg 10/30/25 ECN 239

Incidents:
| Incident | Config | Cause |
| https://jenaero.atlassian.net/browse/VXEP-1890 | Adv Nav VXE. E95 gimbal and clarity on the hood | Pushed both ON command. |
| https://jenaero.atlassian.net/browse/VXEP-1956 | Aircraft configuration: B30 Adv Nav (880) Heavy Payload Main Battery  OGCS 1.4.1 using the Native App (6.6.1 firmware) E95 and Orbital Drop Payload System (attached to top AUX Port) | Aux 1 off command (SB lower payload/E95). Surprising. I would have guessed Aux 2 off (hood+lower) would be more likely. Double check command log and timeline. Could they have turned off then on right after? |
| https://jenaero.atlassian.net/browse/VXEP-2005 | VXE 30 ADV NAV, OGCS 1.4.2, firmware 6.7.1, E140 MWIR | Power cycled the MWIR |
| https://jenaero.atlassian.net/browse/VXEP-2003 | B30 Standard, MB. Any/which payloads? | Was an MCM reset OGCS outage confirmed on this flight, or just suspected? Not indicated in description. |
| Originally this incident? | Unsure Payloads:  6266 and the new EO sensor one |  |
| https://jenaero.atlassian.net/browse/VXEP-844 | None provided. Can likely find in logs/other records. |  |
| Need to write JIRA | AV1000 adv nav. E95 and Kirby (kirby on different circuit, so just E95).  https://teams.microsoft.com/l/message/19:meeting_N2Q2N2JmMzAtYjJhOS00NDJmLTkxMzItYTk1Mjc2Yjk1ODUw@thread.v2/1790720324707?context=%7B%22contextType%22%3A%22chat%22%7D | Turning on E95 |
|  | Hoodtech gimbal. Reported on tail number that should have rev H Avbox (which we thought not susceptible to this) |  |

## Root Cause

- Inrush current, on theNON_CRITICAL bus, of E140payload + DC-DC converter​
- Resulting back-fed inrushcurrent tripping the fast-tripcomparator on the TPS16630Efuse (max 45A)

## Comments (3)

### Cameron Chapman, 2025-06-26

Teams history: Starting 6/25

Connor, Ruysser will meet up with you when he gets back. If you get a chance I am curious (and somewhat concerned) what the behavior of the MCM will be when the payload port is power cycled. please check that. It is a pretty common procedure in flight
 
Mike DeJesus changed the group name to E140 MCM - Reset.
 
Also, Ruysser Gabler can you confirm what SN's this was observed on? I need to get with riga and verify configurations
 
Mike DeJesus added Greg Fryer to the chat.
 
Connor Peebles added Cody Smisek to the chat and shared all chat history.
 
re-creating on bench with our own equipment now
 
sans FC
 
Awesome
 

Mike DeJesus 
Also, Ruysser Gabler can you confirm what SN's this was observed on? I need to get with riga and verify configurations

 6266 and the new EO sensor one

 

Connor Peebles 
re-creating on bench with our own equipment now

 Have you replicated yet?

 
6432 i think
 Sounds right 
Ruysser Gabler
Have you replicated yet?

noh
 
Reading the email chain, this feels like an electrical issue with this MCM.
 
just throwing it out there. We should still test assuming that it's not
 Like this unit specifically? 
Yes. It shut down the first time when they were just swapping the fuel tank and filter. That sounds like something the MCM was doing on its own, or maybe a short.
 Itd be nice if you’re correct. 
we are able to recreate the MCM resetting when power cycling the E140
 In the Jennings GCS? Power cycle by unplugging? Or from the SW ^^^ 
Ruysser Gabler
Power cycle by unplugging?

Both
 Ugh Das not good Have you tried with batteries yet? And does it happen in that configuration as well? 
not yet
 
Ruysser Gabler are you able to support this? I think it would be smart to have a flops person at least providing recommendations.
 They replicated with a power supply here so I think it’s safe to say it is both. But will need to be confirmed 
Thinking about work arounds now, it isn't an EMI problem but a system problem in how the various GNDs of the Epsilon are all tied together, the resulting transients are enough to trip either the MCM enable pin, or to trip the Efuse protecting the MCM itself
 Is there an interim solution we could incorporate into a cable while Riga takes the time to address the actual issues in the gimbal it’s self? 
looking into it, thinking about inline harness solutions
 
The yellow line is the 3.3V enable line that lets VBATT pass to the MCM. The Pink line is the 28V payload line (non-critical VBATT).
When the E140 is installed there is a shift in relative GND for the 3.3V signal that enables the MCM. Granted this didn't always guarantee that the enable line would drop.
 
There are still a couple of configurations I will play around with tomorrow, such as including a HLB in there. And a couple of different spots I want to probe. I also want to try with a couple different payloads.
 
In the SLA Breakout V3, which will be installed into all SB35 / SB40 planes, the MCM is being moved to the VBATT_CRITICAL bus and its GND and PWR is being separated from the VBATT_NON_CRITICAL. I will install this new board into my test set up and that may solve the problem. I'll make a PPT to summarize everything.
 
Here's a similar issue that caused the MCM to reset sometimes when swapping out a HLB: VXEP 730 - 128-117156-01 Rev B SLA Breakout Board - Increment to Rev C.pptx
 
Connor I think we should investigate the in-line solution regardless. e.g. we don't want even non-critical loads to get bounced by the gimbal. It may become less urgent for B35X, but still a potential issue for those with an E140 and some other payload. Let alone other elements of the system that might only be vulnerable in extremes?
 
Oh absolutely
 
You probably meant that all along, and I am just tired and still typing. I better get to the internet comment section.
 
Mike DeJesus added Anna Stirāne and Aleksandrs Guks to the chat and shared all chat history.
 
[PLD-29] E140/MCM Reset on connection - Jira
Jira
 
Connor Peebles added Cameron Chapman to the chat and shared all chat history.
 
Cameron Chapman
 
please review

### Cameron Chapman, 2026-05-29

Did it reset with E140 connected to the Alden or glenair? I'm surprised if alden, since gnd is not common until the nose, but feasible. Or could it also be when E140 didn't isolate 12V and 28V gnd? Alden. Alden payload rtn is common with glenair and MCM in the nose.

### Cameron Chapman, 2026-05-29

find solution for permanent Advanced Navigation vehicle fix
@Connor Peebles  does below still show the latest status. Was MCM moved to critical on B30, or just B40? 
- MCM was not moved to critical bus on B30, only B40.- CP 5/28/26
- Below is still the latest; resources have still not been allocated to what I identified as Corrective action 2.- CP 5/28/26
>>2. TBD fix for TPS16630 (aircraft permanent fix).​ - CP 5/28/26
- Connor suggest finding a new fuse/switching solution or simply removing the Efuse since it is a critical application. - CP 5/28/26

## Attachments (0)
