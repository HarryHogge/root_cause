# VXEP-1464: VXE 829 LRR Asset mishap during VTOL landing-ESC corruption

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-08-10
- **Updated:** 2026-08-21
- **Resolved:** 2026-08-21
- **Reporter:** Drew Hildreth
- **Assignee:** Drew Hildreth
- **Creator:** Drew Hildreth
- **Labels:** GS_Closed, Hardware, LRR, Weekly-incident-tracker
- **Links:** Linked issue cannot finish until this issue finishes. RMA-767 (VXE-829 RMA # 250811-1); relates to VXEP-628 (Systemic VXE30 VTOL ESC Reliability Issues )
- **Customer:** LRR
- **Vehicle Tail Number:** VXE-829
- **Plan:** - Organize previous investigation findings and devise plan
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical
- **Product/Tech Owner:** Travis Blaschke
- **Tech Lead:** Addison Osborn
- **Program (Marquee):** LRR
- **Executive Summary:** Long term ESC change required
- **RMA Disposition:** RMA was completed before this Section was added. Aircraft has been repaired.

## Description

Report:
Sharepoint: VXE 829 LRR Mishap
PPT: VXE 829 LRR Mishap Investigation Report-VXEP-1464.pptx
Detailed Word Summary: VXE 829 LRR Asset mishap during VTOL landing-Redone.docx
Original description:
AC 829 incident description:
AC config: 829, Internal asset LEMB, Internal asset HLB (3 cycles) , Customer E140 payload,
Weather: 10mph wind on landing, gust factor 3-4mph
AC did launch wizard mostly good (had to power cycle due to roll issues in calibrate page)  
AC launched and did 2-3 orbits no issues with GPS or anything
AC flew landing plan properly without any abnormal issues
AC started VTOL decent well and normal
At about 100ft AGL about 36 seconds or so after VTOLs turned on (maybe lower AGL but hard to tell)  
AC pitched up and started an uncontrolled spin to the right
Pilot attempted to pause and nudge to slow decent or control AC but the right hand spin was not stopping
At about 5 or so feet AGL the AC slowed slightly and hit the ground
AC stopped motors and then started motors again
Pilot cut and safe and VTOL stopped
It was noticed after the cut and safe was sent there was a GPS fault of "ACTION: Prepare to Nudge. VTOL GPS fault"
It is unknown if the GPS fault caused the issue, or maybe a VTOL motor failed. And then the GPS failed due to abnormal attitudes. 
An after mishap lift motor test was run and all four motors appeared to operate normally. It was noted that after the motors were safed the right rear lift motor did not park/home the prop in the proper position.  The other three were properly parked/homed.

## Corrective Action

https://jenaero.atlassian.net/browse/VXEP-628 
External Audience
- Replacement of heritage ESCs with more reliable and capable ESCs. The replacement ESCs will have CAN commanding and telemetry, which will enable earlier fault detection and incident prevention, isolated digital and power returns, which prevent microcontroller corruption.
- Currently implemented on B40. Project to implement on B30 linked above.

Discuss if external or not. 
- Additional training and process development of investigation and evidence handling processes. Ensure modifications to evidence are approved by investigation leads (ex: get approval from FS before reprogramming ESC. Ensure flight config was pulled if possible, or list not possible if that is the cas)
- Review ESC code to detect a possible hang-up situation or check and reset the ESC controller. This may kick start the motor and possibly avoid the crash. @John Clark is this possible and worth doing, or better to focus on replacing the ESCs? 
- Better to focus on B40 ESCs and integrating them into B30.

## Root Cause

- ESC microcontroller code corruption. Suspect caused by high current, voltage transients, and shared return paths of microcontroller and power on the ESC.
- The VTOL ESCs are exposed to intense conditions during launch and landing. A small percentage of ESCs will pass all initial tests and develop latent failures that could not have been caught during initial checkouts. The corrective actions listed below should help with earlier detection and reduce the occurrence of such failures.

## Comments (46)

### Drew Hildreth, 2025-08-11

@Eric Brewer just wanted to let you know that we opened a ticket for this.

### Pat Wells, 2025-08-11

Added post mishap lift motor test to the description above.

### Greg Fryer, 2025-08-11

@Drew Hildreth @Pat Wells Eric looked at the log and the GPS fault was a side effect o the failure, vehicle tilt caused satellite loss, which triggered the message (correctly, but uselessly).
Trying to track down who has the vehicle so we can move it to investigation.

### Drew Hildreth, 2025-08-11

@Greg Fryer we have the aircraft in our RMA cage.

### Pat Wells, 2025-08-11

@Greg Fryer we will overnight the aircraft to SLO today so that the lift motor/esc can be investigated.  Additionally the aircraft requires repairs which will need to be prioritized @Drew Hildreth

### Greg Fryer, 2025-08-12

@Pat Wells Production/RMA is doing an inspection, but I need them to hold on repairs until we verify that something is wrong with the ESC/Motor, on the very outside chance that it is a wiring issue or similar. I will try to crack one of the electrical folks loose today, but they are in high demand for VBN and such. Will advise.

### Pat Wells, 2025-08-12

@Drew Hildreth  FYSA

### Greg Fryer, 2025-08-12

@Cameron Chapman @Scott Stuckey can we pull anyone to look at the ESC for obvious failure today 2025-08-12 without breaking priority work? Just enough to verify the issue is within the ESC to free up Tail 829 for full repair and return to FLOPS.

### Scott Whitney, 2025-08-12

Based on data review and manually spinning the motor, Eric Brewer said the following “yea I'm done with the review, seems like motor failure and if there's crunching on the ground seems like good confirmation”
[embedded: image-20250812-184302.png]
“the GPS funny business was mostly after the crash - just some low CN0 which was probably due to the high attitude.” -Eric Brewer  
[embedded: image-20250812-184358.png]
FYSA: @Cameron Chapman

### Greg Fryer, 2025-08-12

@Pat Wells  @Drew HildrethI’ve cleared production to start work on 829, we got bad behavior from the suspect ESC running the boom w/o the rest of the plane. From @Jeremy Kostel : 
”Weird clicking noise at high RPM (cody thinks sounds like a bearing) and motor not homing correctly
 I would say while we dont know if it is motor or ESC related we are seeing weird behavior with that motor and ESC on the bench. Mark is inspecting further but i have no reason to assume the problem was related to other parts of the aircraft”

### Jack Waeschle, 2025-08-12

@Greg Fryer @Desiray Johnston I measured the pure bending and torsional stiffness of the center panel today and found no issues: 
[embedded: image-20250812-212804.png]
As the SB35X wing uses a standard VXE30 spar and layup, aside from a few minor differences in trim, it is identical to a VXE30 Std wing. As the highlighted row above shows, post crash this center panel is within 2.6% of a standard wing, which I would expect as well within standard variance. I will coordinate a glue repair of the small crack along the trailing edge, but otherwise this center panel remains flightworthy.

### Mark Squillante, 2025-08-12

Removed right aft lift motor and ESC from boom, no obvious problems found.
Removed cover from ESC and visually inspected, no obvious problems found, although potting prevents thorough visual inspection
[embedded: ESC.jpg]

### Greg Fryer, 2025-08-13

@Mark Squillante I know we have a teams chat going for fast discussion, but once we craft a plan there (or anywhere) please update the “Plan” field with new steps so everybody can quickly see where we are going. This has LRR customer visibility, so we need to make sure everyone is kept up to date. Thanks!

### Mark Squillante, 2025-08-13

Checked back EMF of motor by measuring voltage across 50 ohm load resistor across boom power leads while manually spinning motor using a hand drill. Compared to the same test run with a known good motor some abnormality was observed. The suspect motor produced not as smooth of a waveform which indicates likely a problem with one of the phase legs in the motor. See attached scope plots of known good vs suspect motor. Known good motor produced 252mV peak to peak of back EMF, suspect motor produced 364mV peak to peak.
[embedded: Suspect motor-ESC spun with drill, lower frequency, not as smooth.png]
[embedded: Good motor-ESC spun with drill, lower frequency, smooth.png]

### Mark Squillante, 2025-08-13

Tested MOSFETs in ESC to determine whether there was a short in any of them, no indications of damage to FETs.

### Mark Squillante, 2025-08-13

Spun motor up on bench, unloaded. No problems observed.

### Mark Squillante, 2025-08-13

Replicated problem of ESC not homing on bench.

### Mark Squillante, 2025-08-14

I tested this motor and ESC on the dyno, no strange noises or behavior observed other than the not properly homing issue. The ESC did not get that hot, about 32C with 10% throttle, 38C with 40% throttle, and 68C with 85% throttle. The motor got to 81C after the 85% throttle test (ramping up over 10 seconds, holding for 10 seconds, ramping back down over 10 seconds), will compare this to a known good motor/ESC.

### Mark Squillante, 2025-08-15

Running same dyno profile on known good motor/ESC for reference showed the good motor got to 67C, which points to a problem in the motor since the suspect motor got to 81C. Will keep investigating.

### Mark Squillante, 2025-08-19

Checked current draw from each motor phase leg, unloaded, and compared to known good motor. Suspect motor draws ~200mA more on each phase leg. Will investigate further while loaded in the dyno room.

### Mark Squillante, 2025-08-21

Handing this task off to @Laszlo Juhasz

### Rajesh Budhabhatti, 2025-08-22

Tested the VTOL prop blades. The MAG value for suspect side prop blade was 0.10. It should be 0.05. Checked with Dillon Bolton who said that they have found customer returns with much more out of tolerance blades that seem to work. Investigating Pitch, Roll and Yaw during the landing mishap and will have more info soon. I will compile my findings in a document and attach it here.

### Greg Fryer, 2025-09-03

Added the short video of the prop being spun by hand and giving off audible “grinding”

### Rajesh Budhabhatti, 2025-09-03

This is a working document with findings being added real-time. VXE 829 LRR Asset mishap during VTOL landing.docx

### Rajesh Budhabhatti, 2025-09-08

I ran the throttle 3 (Right rear motor) profile on dyno using two motors, the 829 motor and a known good motor. BOth motors shut down at about 43s into the profile. Something to do with sharp changes in throttle command seem to cut the motors out. I am going to try running the profile a few more times to see if I can get more information. Still now clear why the throttle was so high and changing fast. I am updating the investigation report to add new findings.

### Rajesh Budhabhatti, 2025-09-09

Performed side by side comparison of suspect motor and a known good motor. Apart from the motor not homing correctly, I find no difference. We may have to send the suspect motor to the supplier to find out. Comparison charts in the unformatted investigation report here: VXE 829 LRR Asset mishap during VTOL landing.docx. I will format the report now.

### Rajesh Budhabhatti, 2025-09-15

Aircraft was flown with new boom on Wednesday 9/10/2025 and operated normally. Flight team did not download the AAR as requested but rather saved it on GCS which is in customer’s possession.

### Cameron Chapman, 2025-09-16

9/16 Cam met with raj. Populated plan field. Please execute those tests and report findings.

### Greg Fryer, 2025-10-02

@Rajesh Budhabhatti @Cameron Chapman Can you clarify this sentence? “Root cause seems to be the damaged motor controller inside motor 3 (right rear).” I do not believe there is a “controller” inside the motor, likely just a wrong word?
Also, report is formally required to LRR. Ergo the report from the vendor must include “what will prevent this from happening again”. e.g. different inspection/test/process by them, by us, etc.

### Rajesh Budhabhatti, 2025-10-02

I managed to replicate the fault. I found that during the landing phase even with the throttle active, motor stops running. I flashed the ESC again and fault went away. Motor/ESC work normally. When I checked the traveler for this Motor/ESC pair, there was no indication of misbehavior. To further investigate the issue, I found 8 other motor/ESCs that had homing issue however none of them displayed the behavior this one did before reflashing. I am still investigating what could have done this. Until we identify the issue, I am going to ask production to flash the ESC 3 times (Greg’s suggestion). Meanwhile, I will work on better check-out procedure for production.

### Greg Fryer, 2025-10-02

@Rajesh Budhabhatti Also be sure to have them start a log, separate from just NCRs so we can track. John Clark might be a good POC to do more detailed investigation into ESC firmware loading. (Thought I had after we talked)

### Rajesh Budhabhatti, 2025-10-02

@Greg Fryer Good idea. I will report back to you once that is done.

### Greg Fryer, 2025-10-09

@Rajesh BudhabhattiWith root cause established, can you please also start finalizing that part of the report (leave root cause alone). Since this will need to go to the customer, it needs to be clear/polished. Since we had to investigate so many potential directions, I think it might be suitable to move the non-root causes to an Appendix, and simply point to them in the main text. e.g. “Possible issue with throttle command due to IMU instability - disproven, see Appendix A.1” or similar. Reading through all the disproven items is informative, but only to the tech savvy folks.
Also, I put a link to the report doc up at the top of the ticket under description,

### Rajesh Budhabhatti, 2025-10-09

Hi Greg,
Thank you for your input. Will do. I have got myself tied up with thermal testing for power budget on 35X. I'll see if I can get report rehashed today.
Thank you,
Raj

### Rajesh Budhabhatti, 2025-10-15

Latest reports here: 
Word doc-VXE 829 LRR Asset mishap during VTOL landing-Redone.docx
Powerpoint: VXE 829 LRR Mishap Investigation Report-VXEP-1464.pptx

### Greg Fryer, 2025-10-29

@Rajesh Budhabhatti - Just checking in, were you able to get back to investigating possible corrective actions for the ESCs based on the 829 incident?

### Rajesh Budhabhatti, 2025-10-29

@Greg Fryer Hi Greg, Yes, I analyzed the VTOL current and there is a way for VTOL software to determine that the motor is not drawing current however that will only tell the VTOL AP that aircraft is crashing. My findings are in the ppt above. I discussed this matter with John Clark and the right way to do this is to identify and fix the bug that locks up the ESC. His concern was that we have the source code but he cannot be sure that the source code we have is indeed the one that created the image file we are using. Is there something further you would like me to do on this issue? The aircraft went through our SCO and successfully flew a few times before this incident happened.

### Greg Fryer, 2025-10-30

@Rajesh Budhabhatti To ask specifically (and the answer may be “no”): With the information we have, is there any change we could make to the SCO flight or other production steps to detect this issue reliably?
For example, the answer might be “No, the issue occurs randomly, and is triggered by effectively random events/timing, so no adjustment will make us confident we have detected it”

### Rajesh Budhabhatti, 2025-10-30

Thank you Greg. I will do so. There are a couple of things I can add.
Raj
Get Outlook for iOS<https://aka.ms/o0ukef>

### Jackson Riley Curvin, 2026-01-20

Report sent to customer closed on Global support side.

### Pat Wells, 2026-08-11

@Cameron Chapman back to you since this was never re-assigned after Rajesh left.  What is the current status on the CA?

### Cameron Chapman, 2026-08-11

Completed plan steps 
Generate the following plots this ESC, motor, prop, vs normalPower vs RPM Thrust vs powertemp profiles during those runsThermal photo of PCB after each run. Electrical efficiency vs rpmTotal efficiency vs rpmScott Whitney is going to add some plots from data review. Scott Whitney or Dave Grosher did we ever implement the pre landing ESC test? If so, were there any anomalies there?
Almost certainly a hardware failure, but it would be good to look into if we could have detected it and aborted transition/reverted to FWMark Squillante and/or Laszlo Juhasz can you please perform a hardware inspection of this when it arrives. Lid off top of the ESC only for now. We can meet after that to determine next steps.Removed lid from ESC, no obvious problem found.Spin motor on bench, unloaded, checking for abnormal behavior.Replicated homing problem on bench.Dyno test motor and ESC and compare to known good motor/ESCSuspect motor got quite a bit warmer than known good motor during dyno test, using same ramp profile. This indicates likely problem with motor.Check current draw to each motor phase leg while loaded, compare to known good motor.Raj reports ESC 4 is probably cooked. It ran at 95% for 45s on takeoff. Same with other three to a lesser extent.Please add to investigation summary. Talk to FS (Eric B or Everett) We should figure out why. Ex: do we know what configuration it was flying in (overweight or in limits), environmental anomalies, link to the CA to abort based on high current (not implemented yet) Link to previous data indicating safe operational throttle range and duration. Investigate component ratings, temperature etc. Would this throttle profile cause them to be exceeded. Identify if homing fault is on the motor, ESC, or both. Meet with Cam after these steps are done. Replicate the failureFlash the ESC and see if the fault persists.

### Cameron Chapman, 2026-08-11

old status: 10/3 Met with John Clark and discussed the issue. He acknowledges that some sort of “bit flipping” can cause this kind of fault. We have an image file that we use to program the ESCs with. The source code that was delivered to us has never been compiled or worked on. We do not know the tool chain used to compile and build the image file we are using. There is a certainty that if this source code was compiled, the image file would not look like the one we are using. 
9/22 After several runs of AAR flight profiles, we were able to replicate the fault mode observed during the flight incident. During the Dyno test running the incident flight profile, motor stopped rotating during the landing stage same as during the crash. Further investigation is being conducted. Once the ESC was programmed, the problem went away. 
9/16 Cam met with raj. Populated plan field. Please execute those tests and report findings. 
Aircraft in SLO ready for inspection. Investigating suspect lift motor/ESC. Motor 3 does not home. We suspect that due to high throttle, motor was overloaded and damaged the motor controller (not the ESC). While the motor #2 exhibited some grinding sound, it does not seem to be the cause of failure.

### Cameron Chapman, 2026-08-11

@Pat Wells @Drew Hildreth I cleaned up the fields above and some of the report. Report has been sent to the customer and CAs are tracked in the linked systemic issue. Is this ok to close? I think so.

### Drew Hildreth, 2026-08-11

@Cameron Chapman Thank you for updating all of that. For my awareness, this https://jenaero.atlassian.net/browse/VXEP-628 ticket, should we change that from ‘relates to’ to ‘is fixed by’?

### Cameron Chapman, 2026-08-11

@Drew Hildreth we have not been that strict with the linkage type. The issue isn’t fixed by that one until that one is compelte, but for the sake of clarity, fixed by does sound like the most accurate linkage.

## Attachments (21)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IMG_8884.mov | video | 140045 | 2025-08-10 | listed only |
| IMG_8885.jpeg | image | 10042 | 2025-08-10 | listed only |
| IMG_8886.jpeg | image | 9584 | 2025-08-10 | listed only |
| IMG_8887.jpeg | image | 10738 | 2025-08-10 | listed only |
| IMG_8888.jpeg | image | 6095 | 2025-08-10 | listed only |
| IMG_8889.jpeg | image | 11646 | 2025-08-10 | listed only |
| IMG_8890.jpeg | image | 6496 | 2025-08-10 | listed only |
| IMG_8891.jpeg | image | 3749 | 2025-08-10 | listed only |
| IMG_8892.jpeg | image | 3821 | 2025-08-10 | listed only |
| IMG_8893.jpeg | image | 6275 | 2025-08-10 | listed only |
| IMG_8903.jpeg | image | 3652 | 2025-08-10 | listed only |
| IMG_8904.jpeg | image | 3186 | 2025-08-10 | listed only |
| IMG_8916.jpeg | image | 2709 | 2025-08-10 | listed only |
| AAR_V829_20250810T152651Z.zip | archive | 12226 | 2025-08-11 | listed only |
| ESC.jpg | image | 390 | 2025-08-12 | listed only |
| image-20250812-184302.png | image | 96 | 2025-08-12 | listed only |
| image-20250812-184358.png | image | 78 | 2025-08-12 | listed only |
| image-20250812-212804.png | image | 11 | 2025-08-12 | listed only |
| Good motor-ESC spun with drill, lower frequency, smooth.png | image | 63 | 2025-08-13 | listed only |
| Suspect motor-ESC spun with drill, lower frequency, not as smooth.png | image | 65 | 2025-08-13 | listed only |
| 829 hand-spin, grinding sound.mp4 | video | 931 | 2025-09-03 | listed only |
