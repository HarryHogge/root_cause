# RMA-129: VXE 516 230705 TIQ

- **Issue type:** Bug
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-07-06
- **Updated:** 2024-02-29
- **Resolved:** 2024-02-29
- **Reporter:** Sean Odell
- **Assignee:** Sean Odell
- **Creator:** Sean Odell
- **Links:** relates to ENG-2983 (511 LW motor test failed. 511 and 516 center wings damaged. ); relates to VA-35 (511 CW Input power connector damaged); relates to RMA-128 (VXE 511 070523); relates to VA-31 (EA Internal: 516 center wing damaged. 511 fuselage+516CW LW motor test failed. ); relates to VXEP-12 (TPTR-87 VXE 511 VTOL Connector Issues 516 CW. Contains Main connector/contact C/CAs)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 516

## Description

a.       Center Wing 516        
b.       From LM  “One flight of 511 with 516 wing set was conducted. After that flight one of the students mentioned that the HLB (S/N 2-1801) had a strong smell from around the discharge connector. The connector looked normal. During the LW for the second flight the motor check failed to spin the lift rotors more than a half turn. The VTOL Control Window indicated VTOL launch not OK and the HLB voltage was fluctuating 7-25V. The LW was canceled. At this point we were no longer going to fly this aircraft. I inspected the CW high voltage connector and it appears to have some discoloration. For troubleshooting we tried a different HLB and were able to complete the LW without issue. We also retried the original HLB and passed the LW without issue. It seemed like a good day to not crash a plane so we did not attempt a flight.”
c.       SOW: Warranty Evaluation on Center Wing
d.       Carson Notes:
                 i.            Check Ohm of Anti-spark and verify correct current limit (not open or short).
                 ii.            Check Current Sense and Ground Iso boards, verify correct functionality.

Cam-Here is what I recommend for repair.
- replace CSB assembly. Red tag and give to engineering.
- Inspect and return equipment to final assembly for reassembly and SCO.

## Comments (24)

### Sean Odell, 2023-07-06

Induction photos and paperwork complete and attached to this ticket. 7-6-2023

### Cameron Chapman, 2023-08-09

@Sean Odell shouldn’t this RMA say 511 fuselage 516 wing? The 511 wing was also found to be damaged as well at the power connector. Did it go through RMA inspection?

### Sean Odell, 2023-08-09

@Cameron Chapman Both 511 and 516 went through an RMA inspection. On arrival, 511 Center wing was found to have a piece of glue in the spar. Engineering and myself removed the FOD in the SPAR. No other work was completed until 511 shows signs of power related issues.

### Matt Philley, 2023-09-11

@Sean Odell AC 516 both transit cases are hangin out over here in Engineering and I dont recall it being held for any active investigations anymore. Are you tracking this?

### Sean Odell, 2023-09-11

@Matt Philley I am trying to connect with Jeff from LM on the status of 509, 516, 510, 511, and 517.  In relation to RMA/Rework activities. I will likely pull that box over here until I get some guidance on these aircraft.  

FYI  @Pat Wells @Sam Miller

### Cameron Chapman, 2023-09-14

516 fuselage was never involved in any incident. That is a customer asset right? If so, should we return the fuselage now, or wait until the 516 CW is fixed? Is it cleaner to track RMAs per vehicle or incident. 
@Matt Philley FYI. 516 CW is still damaged and hopefully red tagged. It will probably be a CSA harness and left CW to boom power harness replacement.

### Cameron Chapman, 2023-09-19

@Sean Odell I suggest we separate the 511 and 516 RMAs, since they will be returned in separate cases right? 
@Greg Fryer @Former user since this is TIQUILA FAT related, are we approved to repair this equipment, or do we want to keep it until the incident is signed off by LM or customer?
Here is what I recommend for repair.
- replace CSB assembly. Red tag and give to engineering.
- Inspect and return equipment to final assembly for reassembly and SCO.

### Sean Odell, 2023-09-19

@Cameron Chapman Changed name to just 511 on this Ticket. Creating another for 516.

@Cameron Chapman CSB stands for? Current sense board? Part #('s)?

@Pat Wells @Greg Fryer @Sam Miller Do we have any clarity on 509, 510, or 517 at this time? Scope of work, if any? Or are they just waiting in RMA area until a decision is made?

### Cameron Chapman, 2023-09-19

107-102264 DUAL CURRENT SENSE, ASSEMBLY

### Greg Fryer, 2023-09-19

@Sean Odell You need to track down Glen, Jeran, or Sam - I don’t have visibility into what or how LM is approving repairs/RMAs. I do know it’s been a confusing issue. I think @Former user would have point, but you’ll need to track him down.

### Sean Odell, 2023-10-24

To ALL!  Update:  516 still  needs rework. This rework is not related to Silvus and could be connected to the recent AS150 pin issues on the center wing.  TBD, but awaiting engineering to complete SOW needed to make the aircraft air worthy. 
Moved this ticket back to Evaluation for this reason. 

NOTE: Dual Power current harness removed by engineering request and Edge will replace with new. Customer will be given a SOW for repair once engineering is complete. 

@Pat Wells FYSA

### Matt Philley, 2023-10-25

107-102264 Dual Current Sense Assy SN: 1125 has been removed from Centerwing and will be delivered to Engineering for testing.
The Assy has not been replaced at this time.
Centerwing has been given a red tag which states it is missing the Dual Current Sense Assy and it will be placed back in the transit case with the center tray cover taped shut.

### Matt Philley, 2023-10-25

@Cameron Chapman FYSA this Dual Current Sense harness SN: 1125 has been delivered to Engineering for testing. It has both a red tag and orange RMA tag linking it to AC516 and this RMA-129

### Mark Squillante, 2023-10-25

516 CSB made it back to engineering. AS150 contact measured 313 uOhms (>235 uOhms is failure). Anti-spark now measuring ~178 ohms.

### Mark Squillante, 2023-10-26

AS150 contact cleaned and remeasured, now 188 uOhms.

### Cameron Chapman, 2024-01-04

@Sean Odell @Pat Wells @Douglas Baker@Desiray Johnston, Matt from LM is asking to have this vehicle returned. It is approved for repair from engineering. 
Should we increase the priority of this repair?

### Pat Wells, 2024-01-04

@Cameron Chapman I was just notified of the same from Matt @ LM.  Have discussed with @Sean Odell and he understands the urgency in getting this completed. Please increase the priority for completion of this repair.

### Sean Odell, 2024-01-04

@Cameron Chapman @Laszlo Juhasz While reviewing the history of this Aircraft I saw and found the Lift booms in Engineering on a rack by the TV. Engineering requested them a while ago, but want to verify they are cleared to be tested and flown? They look fully intact and no visible damage detected. Am I free to use these booms? Do you know if Engineering has any other needs for these lift booms?
@Pat WellsFYI

### Desiray Johnston, 2024-01-04

@Sean Odell  please schedule a meeting to review what is needed for this repair with Production Management (Ian, Kelly, Kyle, and myself). We may also need to see what other RMA can then move out of January because we are over capacity for January.

### Cameron Chapman, 2024-01-04

@Sean Odell my recommendation was listed in the description. 
Cam-Here is what I recommend for repair.
- replace CSB assembly (if not already done). Red tag and give to engineering.
- Inspect and return equipment to final assembly for reassembly and SCO.

### Sean Odell, 2024-01-05

@Cameron Chapman I have taken the booms from engineering and having Carson check them.  Hover test if everything looks good. Then, if hover is passed, replace the dual current sense, SCO, test flight entire aircraft, source, and deliver. (Pending production meeting)
@Pat Wells @Desiray Johnston FYI

### Sean Odell, 2024-01-05

Hover test on the Lift booms showed no abnormal behavior. We will now be focusing on reworking the center wing dual current harness pending production meeting today.

### Matt Philley, 2024-01-09

Dual Current Sense SN 1125 was tested by Engineering and it passed…. i dont know what to make of that result, but harness and test report have been dropped off to Sean. I still recommend replacing it to close the RMA.

### Sean Odell, 2024-01-11

New dual current sense harness acquired and in the queue to get installed in 516’s center wing. ECD on harness is 1/12/24. Then SCO and test flight to confirm the aircraft is fully functional.
@Pat Wells FYI

## Attachments (29)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 20230706_133607.jpg | image | 5644 | 2023-07-06 | listed only |
| 20230706_133613.jpg | image | 6523 | 2023-07-06 | listed only |
| 20230706_133616.jpg | image | 7124 | 2023-07-06 | listed only |
| 20230706_133625.jpg | image | 6948 | 2023-07-06 | listed only |
| 20230706_133629.jpg | image | 2058 | 2023-07-06 | listed only |
| 20230706_133633.jpg | image | 6810 | 2023-07-06 | listed only |
| 20230706_133751.jpg | image | 2702 | 2023-07-06 | listed only |
| 20230706_133755.jpg | image | 8686 | 2023-07-06 | listed only |
| 20230706_133809.jpg | image | 3141 | 2023-07-06 | listed only |
| 20230706_133831.jpg | image | 8126 | 2023-07-06 | listed only |
| 20230706_133839.jpg | image | 2639 | 2023-07-06 | listed only |
| 20230706_133851.jpg | image | 7187 | 2023-07-06 | listed only |
| 20230706_133900.jpg | image | 2403 | 2023-07-06 | listed only |
| 20230706_135458.jpg | image | 3840 | 2023-07-06 | listed only |
| 20230706_135501.jpg | image | 3065 | 2023-07-06 | listed only |
| 20230706_135510.jpg | image | 6863 | 2023-07-06 | listed only |
| 20230706_135548.jpg | image | 7099 | 2023-07-06 | listed only |
| 20230706_135552.jpg | image | 2755 | 2023-07-06 | listed only |
| 20230706_135600.jpg | image | 6670 | 2023-07-06 | listed only |
| 20230706_135603.jpg | image | 7178 | 2023-07-06 | listed only |
| 20230706_135648.jpg | image | 6857 | 2023-07-06 | listed only |
| 20230706_135651.jpg | image | 2151 | 2023-07-06 | listed only |
| 20230706_135654.jpg | image | 3986 | 2023-07-06 | listed only |
| 20230706_135657.jpg | image | 6883 | 2023-07-06 | listed only |
| 20230706_135737.jpg | image | 2265 | 2023-07-06 | listed only |
| 20230706_135740.jpg | image | 6725 | 2023-07-06 | listed only |
| 20230706_135743.jpg | image | 2608 | 2023-07-06 | listed only |
| 20230706_135746.jpg | image | 7692 | 2023-07-06 | listed only |
| [VXE 516 Induction Report.pdf](attachments/15313_VXE%20516%20Induction%20Report.pdf.md) | pdf | 3263 | 2023-07-06 | converted |
