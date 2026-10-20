# ENG-2944: [REMOVE from VXEP] VXE 689 - VTOL battery voltage sensor stopped working after power cycling.

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Highest
- **Created:** 2024-08-16
- **Updated:** 2026-03-27
- **Resolved:** 2026-03-27
- **Reporter:** Cameron Chapman
- **Assignee:** Adrian Garcia
- **Creator:** Cameron Chapman
- **Links:** relates to VXEP-550 (VXE 509 Connection to HLB BMS is causing ground issues, current offsets, and possible transients and damages. ); relates to VXEP-946 (VXE 401 Centerwing failing to report proper VTOL battery state)

## Description

**Description update 8/17/2024 From Cody Smisek**

- After a manual hover test of MAGNSS on 689, test team setup aircraft for next condition and ran through launch wizard, the aircraft was power cycled during launch wizard to attempt to clear a calibration fault. After the aircraft restarted, the GCS indicated ~50% HLB and 27.1V on HLB. The HLB was checked with handheld battery checker and showed nearly 100% energy. Voltage was checked with multimeter at main connector and voltage was commensurate with 100% state.
- HLB was swapped to another aircraft and other aircraft reported appropriately.
- New HLB was swapped placed in 689 and still showed incorrect voltage/%. With only the main HLB power connector (from center wing to HLB) connected and no smart battery harness connected, voltages reported 0. With just the smart battery connector connected and no main VTOL power connector, HLB voltages showed as previously reported.
- 686 center wing was then used with 689 fuselage. Issues were then not repeatable.
- AAR attached, this was taken after the vehicle was power cycled which coincided with when the issue was originally observed.

**Questions remaining**

- Did testing 689 CW on another vehicle show the issue followed the center wing? 
- Yes, caused the same issue on the Iron Bird
- @Cody Smisek working on troubleshooting 689 wing. Do you remember the order of how things were unplugged and plugged back in? It may help the troubleshooting to record and see if we can recreate/measure transients
- Power cycle standard operations usually means pulling main battery connector. Center wing and HLB fully connected. This may be bypassing the ground isolation circuitry and sending transients through the HLB data connector. Potential short term workaround, unplug data connection before power cycling. Demate first, mate it last.

- Testing data can be seen in this excel

## Corrective Action

There is 26AWG wire on a harness that goes through a lot of bending and pulling. This might be too much strain for that size of wire to handle.
Possible options:
- Move where the wire is spliced on from the main AS150 connector to the Lift Boom ground banana connector (on the same harness)
- This would put significantly less strain on the wire and is located closer to the CSB
- Connor mentioned there is a process in the E shop currently for the branch cable where the wires are done in a method to provide more strain protection

## Plan

- Quarantine and mark involved battery and CW.
- See photos below for investigation update.
- 689 CW in being driven back to SLO. Identify C/CA
- If issue appears to be with power contact, inspect closely and review data for VTOL power/current and duration.

- If the bms or xcom are damaged on 689, it could be due to the new hlb gnd to avbox case connection. @Jeremy Kostel 
- Testing done without the use of new harness and grounding connection and problem persists

- Replace 689 damaged dual CSA. Reperform CW SCO checkouts.
- Identify what component on the dual CSA is damaged and how. See if that damage explains/recreates issues described from the incident.
- Identify C/CA
- Quantify transients and risk to equipment of having the HLB data connector plugged in when plugging in the main battery  power (this bypasses the ground isolation board functionality).
- MAGNSS-new HLB gnd to avbox shell was added in branch cable V2 without much testing that I am aware of.
- Pre-MAGNSS (same fuselage harness as MAGNSS)
- VXE30. A HLB to Main gnd connection was added when the HLB BMS was introduced. I do not think this was planned. This also bypasses the ground iso board, but has not led to many/any known issues.
- VXE30 without HLB data connection (this was the original design and purpose of the ground iso board)
- For now, we have instructed MAGNSS flight crew to ensure the HLB data connector is demated when applying power to the aircraft or power cycling the aircraft. (Mate last, demate first). Need to determine if this needs to be distributed to operators and VXE30.

## Issue Status

- Issue isolated to 689 VTOL CSB. Need to determine C/CA. Possibly due to HLB data connector bypassing the ground iso board. Needs further testing.
- Issue has been resolved
- HLB (SN: 2-3230) and 689 Fuse are not the cause of this issue
- Dual Current Sense Board assembly (PN 107-102264) has been replaced by production and CW has passed functional testing

## Root Cause

Wire strain caused the ground wire in the dual current sense assembly (pn: 107-102264) to break. This meant that if the HLB was connected without the data cable, the battery was not grounded.

## Comments (11)

### Cameron Chapman, 2024-08-16

[embedded: 😋]
[1:12 PM] Cody Smisek
apparently we have 686 out here Cameron Chapman Dave Grosher
 
[1:12 PM] Cody Smisek
we will swap with that aircraft center wing. it's Edge asset that was used for SW regression 
 
[1:13 PM] Cody Smisek
 
potentially aluminum spikes. picture from artis 
 
[1:14 PM] Cameron Chapman
Nice. You said vtol power connectors looked normal right? 
Could wave the spike over the vtol mag to check 
[1:14 PM] Cody Smisek
will inspect 
 
[1:14 PM] Cody Smisek
should i say some type of spell while i'm at it? Harry Potter style
like 1
 
[1:15 PM] Josh Boren
wingardium leviosa
laugh 1 heart 1
 
[1:19 PM] Cameron Chapman
Also smell  check the power connectors for burning (sounds like I am joking, but is an actual test) 
[1:21 PM] Cody Smisek
visual inspection complete, nothing obvious. center panel isn't bonded, so quick look yielded nothing as well. 
 
[1:21 PM] Cody Smisek
center wing swapped to 686, charge is as expected with and without smart battery connected 
 
[1:23 PM] Cody Smisek
scratch and sniff yielded nothing. 
 
[1:24 PM] Cameron Chapman
Ok. I am ok with proceeding with 686 cw if we verify it has the right firmware and 686 is not planned for any critical testing. 
Dave Grosher do you agree? 
[1:25 PM] Cody Smisek
Josh Boren need vtol configs
 
[1:26 PM] John Clark
Configs? for VTOL.
 
[1:26 PM] Josh Boren
build_rgm_test_6_3_4_20240815_second_drive 1.zip
 
[1:26 PM] Josh Boren
XComm/VTOL builds and configs
 
[1:26 PM] Cody Smisek
the van is going back to SLO to pick up more production aircraft. do we want to send back 689 cw
 
[1:29 PM] Cody Smisek
we waved the nail around the avionics and no notable changes 
 
[1:30 PM] Eric Brewer
how did you measure changes? did you look at vtol mag values in gui?
 
[1:30 PM] Eric Brewer
in any case, from the datapoints we have seems much more likely the drift is from moving close/far from other ground equipment
 
[1:30 PM] Scott Whitney
Cody Smisek
the van is going back to SLO to pick up more production aircraft. do we want to send back 689 cw

Was Vt_BATT reporting accurate levels with the replacement CW?
 
[1:31 PM] John Clark
Eric Brewer, are we concerned about FW mags on the ground?
 
[1:31 PM] Cody Smisek
i observed the XCOMM web page instrument panel (not vtol, is it vtol or xcomm that drifted, vtol would be completely different story if that's what's going on) 
 
[1:31 PM] Cody Smisek
[1:21 PM] Cody Smisek
center wing swapped to 686, charge is as expected with and without smart battery connected 
 
like 1
 
[1:32 PM] Scott Whitney

Cody Smisek
[1:21 PM] Cody Smisek center wing swapped to 686, charge is as expected with and without smart battery connected

 Yes, that is probably best, so we can investigate. We will also prep another CW asset to go back out on the van 

 
[1:32 PM] Dave Grosher
Meaning that the HLB is reading correctly with the second CW? 
 
[1:33 PM] Cameron Chapman
Cody Smisek 
the van is going back to SLO to pick up more production aircraft. do we want to send back 689 cw

 Yes please 
[1:34 PM] Dave Grosher
686 is an engineering asset, why can't we use that
 
[1:34 PM] Cody Smisek
We have removed 689 center wing and replaced it with 686 on 689 fuselage. After installation, we have vtol web page instrument panel and GCS sw opened. Both spots show 93% and 29.1v with a battery that was checked via battery checker. VTOL and GCS showed same values with and without the smart battery harness connected (which from problem center wing was different). 
like 1
 
[1:34 PM] Eric Brewer

Cody Smisek
i observed the XCOMM web page instrument panel (not vtol, is it vtol or xcomm that drifted, vtol would be completely different story if that's what's going on)

 ok - yea if we just waived it over quickly I think the only sensor values that would respond quickly would likely be the raw mag values from vtol mag (fixed-wing mag would too but we can't measure that directly) 

 
[1:34 PM] Cody Smisek
Dave Grosher
 
[1:35 PM] Cody Smisek
we had it sitting near the avionics for >15sec, so how much time 
 
[1:35 PM] Cameron Chapman
Dave Grosher 
686 is an engineering asset, why can't we use that

 I think they are. Scott is wondering if we should send a spare in case something else happens. 
[1:36 PM] Eric Brewer

Cody Smisek
we had it sitting near the avionics for >15sec, so how much time

 I'm honestly not too worried about the spikes... 

 
[1:36 PM] Cody Smisek
looking for next steps. do we need to perform another mag cal or stick with current cal.  should we launch from pad or launch away from pad in the dirt
 
[1:36 PM] Cody Smisek
mags are currently stable on the pad 
 
[1:37 PM] Cameron Chapman
Cody Smisek 
i observed the XCOMM web page instrument panel (not vtol, is it vtol or xcomm that drifted, vtol would be completely different story if that's what's going on)

 I was saying wave the nail over vtol mag since it is more accessible and closer to the surface vs  xcom. You would then view vtol mag page for interference (to help determine if the nail is ferrous), but like Eric said. Likely low risk 
[1:37 PM] Eric Brewer
we need to update software first before launching right?
 
[1:37 PM] Eric Brewer
we had no issues launching from the pad previously, let's just launch from the pad.
like 1
 
[1:37 PM] Eric Brewer
just make sure we sit it out there long enough that attitude is stable
 
[1:38 PM] Cameron Chapman
Right. The alternate launch location was a step to try if there was still drift after calibrating on the pad and not moving it off. 
[1:42 PM] Cody Smisek
we will wave over the VTOL mag
 
[1:43 PM] Cody Smisek
we are updating software but are stopped because i currently do not know if what we are doing is the appropiate method 
 
[1:43 PM] Cody Smisek
Josh Boren states the config he sent me came from 689. my question to Dave Grosher or someone is if that will also wipe out the vehicle specifc values for mags and other calibrations. i believe the answer is yes
 
[1:48 PM] Cameron Chapman
Seems like we should at least mag check and possibly recalibrate with a new center wing in any case. FW team would know best. Did you do amag check with 686 wing?
 
[1:48 PM] Cameron Chapman
In my experience, waving a magnet over the vtol mag will cause the webpage to respond immediately. Not sure about nails, but I think they use a screwdriver in electronics. Again, low risk/check maybe not needed, but should be quick
 
[1:49 PM] Cody Smisek
we just got done holding it for 60secs, no changes on vtol, held against vtol
 
[1:49 PM] Cameron Chapman
Did you do mag check?
 
[1:50 PM] Eric Brewer

Cameron Chapman
Seems like we should at least mag check and possibly recalibrate with a new center wing in any case. FW team would know best. Did you do amag check with 686 wing?

 mag cal is done without center wing on though right? so i think only mag check 

 
[1:50 PM] Cody Smisek
lets all get back on a call
 
[1:52 PM] Dave Grosher

Cody Smisek
Josh Boren states the config he sent me came from 689. my question to Dave Grosher or someone is if that will also wipe out the vehicle specifc values for mags and other calibrations. i believe the answer is yes

 Cody reach out to Liam Shaw on how to do this 

 
[1:52 PM] Cameron Chapman

Eric Brewer
mag cal is done without center wing on though right? so i think only mag check

 good point 

 
[1:53 PM] Liam Shaw

Cody Smisek
Josh Boren states the config he sent me came from 689. my question to Dave Grosher or someone is if that will also wipe out the vehicle specifc values for mags and other calibrations. i believe the answer is yes

 Before changing anything on the 686 CW please save off the configs.  

 
[2:03 PM] Cameron Chapman
please also quarantine and mark the specific battery involved in the prior flight. Possible it was damaged if too much heat on the connector. 
 
[2:05 PM] Cameron Chapman
Tracking here. Please add detail when available (lower priority than current test efforts) https://jenaero.atlassian.net/browse/VXEP-542 
VXEP-542: VXE 689 - VTOL battery voltage sensor stopped working after power cycling.
 
[2:06 PM] Cameron Chapman
Eric please add any useful info from data review there as well. Specifically, the vtol power and duration from the previous flight could be useful

### Jeremy Kostel, 2024-08-17

@Hayden Jeanor @Adrian Garcia and I investigated the center wing today
**Initial Inspection:**

- visual inspection yielded nothing of note
- CW Power contacts passed impedance testing (167 microohms uncleaned) and power resistor measure 5.9 ohms
- Passed “tug test” on all connectors

**Connecting to center wing (no fuse) through webpage:**

- initial testing was powering CW from two supplies (12V and 28V) and seeing measurements on the webpages
- reported Vbatt as 0V, SOC 0%

**Iron Bird Testing:**

- The next step was to connect the CW to the iron bird and viewed results
- One by one pieces of the iron bird center wing were “swapped” for pieces of the V689 CW to try and determine the malfunctioning piece of hardware

Configurations Tested:
- IB Fuse, IB Ground Iso and current sense board in 689 CW
- IB Fuse, IB VTOL AP in 689 CW
- IB Fuse, IB current sense harness in 689 CW
- IB Fuse, IB VTOL Interface Board
- IB Fuse, IB GPS and Mag in 689 CW
- IB Fuse, IB ADP
- After each component was tested, it was replaced with original 689 part afterwards. Example: After IB current sense harness was used, it was replaced by the 689 CW before next component switched.
- Configurations and results can be seen here

Persisting Problems:
- When the HLB data cable is disconnected, no voltage (or current, SOC, Vref) is read
- AP VTOL ground is measured as 28.5V higher than HLB ground
- When reading voltage, the charge circuit constantly switches from an ON state to an OFF state leading to inaccurate readings when it is off

**Conclusions from (8/17)**

- Unable to determine cause of the issue (suspected grounding problem)
- We were able to connect it to this specific center wing
- vehicle testing performed on V689 Fuse - CW689 continued to cause the same issues regardless of HLB used and using a different CW solved the issue
- We were able to determine this is a hardware issue
- using the IB VTOL AP (production VXE30 SW/FW) yielded the same problems
- Excel tracking all findings found here

### Jeremy Kostel, 2024-08-19

As noted in the issue status field, the problem has been isolated to the dual CSB.
- Testing with iron bird CSB resolved the issue, with all other parts of the CW being original to tail 689
- Cause and corrective action testing results to come

### Matt Philley, 2024-08-19

@Jeremy Kostel @Cameron Chapman Per support request #115
PN 107-102264 Dual Current Sense Assembly was replaced with 
SN C-S103762
It was finished after QA Inspection left for the evening. Since this is urgent I went ahead and dropped it off on Jeremy’s workstation in Engineering.
If yall still want QA to take a look let me know and we can circle back to it in the morning. 
@Scott Whitney FYSA

### Jeremy Kostel, 2024-08-20

CW with replaced dual current sense assembly is performing as designed
- Seeing 29.1V (measured 29V) when data cable is disconnected
- Charging circuit not shutting on and off 
- constant OFF state (as expected at this battery state)
- No ethernet cutouts when connected to battery data cable 
- seen yesterday on NCR’d CSB

### Jeremy Kostel, 2024-08-20

@Scott Whitney 
Please advise on the priority of getting this CW checked out with SCO as they have a lot of other MAGNSS checkouts to do as well. Engineering can do if needed
FYSA @Matt Philley

### Jeremy Kostel, 2024-08-20

Problem resolved
- The dual current sense harness (pn: 107-102264) had a broken connection to ground (DP1).
- See red highlighted path in the drawing
- The ground line is 26 AWG and potted with three other wires (11 AWG 2x, 8 AWG 1x)
- There is no ground line stuck out in the potting where the break occurred, so it could have happened while the potting was still wet
- See attached images
- This severed connection meant that we were not grounding the battery, until the data cable was connected.
- Original CSB has been tested with a makeshift ground harness and performed as intended

### Cameron Chapman, 2025-02-25

@Adrian Garcia if we can prove the issue is resolved with a replacement, then we could remove the faulty part for investigation and return the aircraft for RMA. Doing this should always be the priority.
If we carefully probe and/or disassemble, we should be able to identify exactly where the wires are breaking, solder is incomplete, etc. This will be important for the CA for both. Can you please investigate. Laszlo may be able to help carefully disassemble. We want to try to maintain evidence. With 2x of this issue recently, it seems like something recently changed (assembly, installation, parts, etc).
Please update the plan field in each issue each time.

### David Grosher, 2025-05-20

This is an integration issue on an internal Edge asset on pre-released hardware, it is not a VXEP incident. @Pat Wells do you want to close this?

### Pat Wells, 2025-05-20

@David Grosher yes from our side it can be closed. We were never tracking this.

### Christa Meck, 2026-03-27

Canceling this work item and it’s children per previous comment from Pat.

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 20_f.png | image | 1 | 2024-08-16 | listed only |
| IMG_8584.png | image | 267 | 2024-08-17 | listed only |
| IMG_8585.png | image | 256 | 2024-08-17 | listed only |
| T95_V689_240816_103119_01_pack.zip | archive | 5418 | 2024-08-17 | listed only |
| [107-102264_d dual current sense, assembly 1 (1).pdf](attachments/22512_107-102264_d%20dual%20current%20sense,%20assembly%201%20(1).pdf.md) | pdf | 714 | 2024-08-20 | converted |
| Image (1).jpg | image | 240 | 2024-08-20 | listed only |
| Image.jpg | image | 247 | 2024-08-20 | listed only |
