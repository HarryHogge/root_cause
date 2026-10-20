# VXEP-1452: New E140 Assemblies video quality issues

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** High
- **Created:** 2025-07-24
- **Updated:** 2026-02-09
- **Reporter:** Cameron Chapman
- **Assignee:** Mike DeJesus
- **Creator:** Cameron Chapman
- **Links:** is cloned by VXEP-1453 (New E140 Assemblies DCDC getting hot during operation.); relates to VXEP-1486 (E140ZG2 Randomly Losing Connection); relates to VA-2842 (2125741-01 E140ZG2 Interface Board - Rev  A); relates to VXEP-1318 (Contain and replace all internal and external conductive payload plates. ); relates to VXEP-1509 (MOLSON report: E140 unable to get GPS fix and unable to slew to GPS location); relates to VXEP-1497 (VXE 734 E140 Connection Issues ); relates to VA-2855 (2125741-01 E140ZG2 Interface Board - Rev B); relates to PLD-55 (Productize E140 Interface Board); relates to VA-2865 (2126421-01 E140MWIR Interface Board); relates to VA-2873 (2127071-01 E140ZG2 Interface Board V2); relates to VA-2874 (2127163-01 DSUB-DSUB MWIR Flex)
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Files: VXEP-1452 New E140 Assemblies video not working DCDC getting hot during operation
Investigation Summary test plan and data New E140 Assemblies video not working DCDC getting hot during operation.xlsx
Gimbal SN/Issue Trackerhttps://jenaero.sharepoint.com/:x:/s/FlightSafety/ESjhkbjkZ4hHkZzRRBBjOS4BPZ-Gn1g97DWqg7P1wqAqBA?e=7b16H5

## Plan

Has not been updated in a while. 
- Abel or Mike. I think it would be useful to outline and track a schedule for the remaining days. Who is doing what by when, etc.
- New PCB design. Connor, Abel, Cam C. Hans. Laszlo out. Colbourne going to ramp up this weekend.
- Investigation report. Due Tuesday
- C/CA tracker in sheet linked above. Summary in word doc. Planning to transcribe and prepare for customer audience in the ppt.
- If any engineers are not working on critical tasks for this or other project, please take a look at the cause summary tab and help fill out information (especially if you are the indicated POC) Investigation Summary test plan and data   New E140 Assemblies video not working DCDC getting hot during operation.xlsx
- Answer ATP questions. What was tested before. Cam review added steps. Regulated Payload Cable Test Plan_Procedure.docx
- Need application note recommending filters. -Mark. Steve helping .
- Daniel working on cable drawing . Alden to HD15 build. When do we need to kick this off? We can likely prototype this by pulling a regulator off existing cables.
- Irfan Update and keep ordering shopping list, E140 shopping list.xlsx. Add ETAs to all. Mark has been pulled into Novatel testing.
- Add HD15 extender for MWIR testing
- Was HSV scope ordered? Irfan is not aware of it. Add to tracker.
- Make gimbal installation document. Mike D/Cam R. See existing one I sent.
- Identify alternate ethernet cable-Abel
- Flight test request.
- Test planning to verify requirements  for next PCB assembly

 
V2 or later
- LKS PCB or similar fabricator. Order-Adrian.
- Plan for MWIR
- Find better connector for payload-Steve, Sammy, Mark

## Issue Status

Updated list of deliveries:
 
- ASAP MOLSON qty 1, for VXE30 Std. COMPLETE - Satisfied with existing demo harness, uses old DC/DC.

- ASAP Qty 4 LRR First-Delivery gimbals. OPEN

2.1) ASAP Qty 4 USSS MWIR gimbals
- <=1 week - Qty 4* Demo gimbals, used in asset AVs

- <=3 weeks - Qty 8-12 finished harnesses to upgrade various users.

- TBD** - finished harness in production

 
*I think this is 4, not sure what/how many demos are outstanding.
**This really depends on if any gimbals are shipping for delivery and when. I suspect the need is end-of-August, since we probably ship every month.

## Comments (2)

### Cameron Chapman, 2025-07-24

Some of teams chat Connor let's synch for the status of your testing yesterday when avaialable
 
FYI, FLOPS in HSV has one of the cables with the old DC/DC, and should have the laser fix. They will be testing that today (right now). If sufficient, it may solve the most critical need. We will still owe the permanent fix and schedule. May need an intermediate fix, depending on how that evolves.
 
Yesterday I basically replicated the problem with the new E140 and Harness that was sent overnight from HSV
 
To confirm, that won't have PPS and will reset the MCM when power cycling right? Anything else? Are those acceptable if needed for CANSOF delivery? I think so, but want to verify
 
Connor Peebles
Yesterday I basically replicated the problem with the new E140 and Harness that was sent overnight from HSV

Were you able to test with the old cable, or with a switch in line?
 
Cameron Chapman
Were you able to test with the old cable, or with a switch in line?

That's the plan for this morning
 
Cameron Chapman
To confirm, that won't have PPS and will reset the MCM when power cycling right? Anything else? Are those acceptable if needed for CANSOF delivery? I think so, but want to verify

The immediate excercise is with a VXE30 (no advanced nav). So Yes.
 
Here is the problematic capacitor isolation that is a likley cause/contributor to this issue and many others. Hopefully we can get rid of them soon. I imagine the E140 has similar lack of magnetics, but I don't have the schematics to verify 
 
They WILL need the permanent fix as well, and possibly an intermediate one if the permanent takes too much time. Hard to say what too much is, but likely anything beyond weeks is too much
 
10:09 AM Meeting ended 24m 13s
 
Current Status and Things Tried
 
We're not getting video on an aircraft with the new regulator cable. It's some kind of networking issue. We get enough of a connection to find the gimbal; we can change settings and read them back, move it, etc., but there's no video. We did some pings and we're losing probably half the packets when connected to an aircraft or an IB.
 
We've tried three gimbals: G2, G3 and E95 and an IB. The problem seems to be the same on VXE30 and the 35.
 
Every cable was tested in production on a G2 with the new Alden ground support cable - they all worked fine (and still do).
 
I’ve found a switch to test Cameron’s suggestion on the missing magnetics. FLOPS is testing the last gen payload cables to see if they will serve MOLSON in the interim. As soon as they get done with the equipment, I’ll run the magnetics test.
 
I’ve also found stock on some M27500, 26AWG, 4-conductor, twisted, shielded at a local vendor. Ryan is trying to get that paid for so I can pick it up later today.
 
Other things tried – and helpful suggestions
 
Had a look with Wireshark – nothing obvious.
 
Justin on the SE team suggested we might put it on a block 35 and be able to get more details on the network interfaces from Linux on the MCM. He’s seen a similar problem before where a controller as continually resetting – comes up sends a few packets, resets, send a few more, etc.  We were planning to try that this morning, but they’ve been busy. If anyone thinks this approach will yield insight, I’ll push in that direction.
 
I reached out to LV last night to see if they had seen this problem before or if they had any insights or suggestions. I got the typical response – crickets. 
 
I've also replicated the problem on an old payload with the new harness that was sent to me
 
After testing, if we do determine that shielded cable would help. Actual ethernet cable (specific twist rate, controlled impedance) would be best. HSV may have this in stock as it was used on previous harnesses. If not, SLO should 
 
| GSC-03-84820-00 | 2120791-01 |

 
 
If the switch does fix the issue, we can inform latvia and request they add magnetics long term (and figure out a shorter term in harness/pcb plan)
 
Cameron Chapman
After testing, if we do determine that shielded cable would help. Actual ethernet cable (specific twist rate, controlled impedance) would be best. HSV may have this in stock as it was used on previous harnesses. If not, SLO should            GSC-03-84820-00  2120791-01

Evan, our inventory manager, reached out to Ethel and Spenser. No stock in SLO. Wire masters is also out of stock. 
 
We may have some in engineering
 
I will check
 
The wire order to the local vendor went through and has been ack'd. They're pulling it now. Going to call us when it's ready
 
sounds good. 27500 could help and definitely wont hurt

### Connor Peebles, 2026-01-26

@Mike DeJesus I don’t have time to finish the 8D for this, so I am un-assigning it from myself. Perhaps Abel?

## Attachments (0)
