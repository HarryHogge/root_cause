# VXEP-1278: VXE-541 Failed to perform proper landing sequence actions, resulting in the aircraft crashing into the ground.

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2025-05-13
- **Updated:** 2026-05-12
- **Resolved:** 2026-04-27
- **Reporter:** Samuel Lopez
- **Assignee:** Samuel Lopez
- **Creator:** Jackson Riley Curvin
- **Labels:** GS_Closed, USASOC
- **Links:** relates to RMA-686 (VXE-541 RMA 250515-1); relates to FS2-3321 (VXE-541 Investigation: Failed to perform proper landing sequence actions); relates to VXEP-1279 (Make a confluence page showing examples of good and bad AS150 plugs and sockets, plots, etc. ); relates to VXEP-553 (AS150 Plug/Pin Connector Issue Systemic Collector)
- **Customer:** USASOC
- **Vehicle Tail Number:** VXE-541
- **Issue Status:** D4 - RCR, D5 CAT review needed.
- **Root Cause:** Connector was loosely mated to the HLB from the CW.
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

Customer did not report incident until beginning of May 2025
Who: SORD, ATOC, 4BN, 10SFG(A)
What: Stalker VXE30 (Tail #541) failed to perform proper landing sequence actions, resulting in the aircraft crashing into the ground.
Where: Agony North, Fort Carson, CO 80911
When: 06 December 2024 at 1200L
Why: During landing sequence, tail #541 failed to transition to the Vertical Take Off and Landing (VTOL) motors. The aircraft instead, continued to reduce its airspeed causing it to glide until it struck the ground. 
Investigation Report: Vehicle Investigation VXEP-1278.pptx
SharePoint Folder: Flight Safety - VXEP-1278 v541 - All Documents

## Corrective Action

Update existing AN for the main battery to include the HLB, or nothing.  Implement recommended design changes into B40.   
https://jenaero.atlassian.net/wiki/spaces/SEIT/pages/849838110/Project+Charter+-+Stalker+Block+31

## Plan

- @Samuel Lopez  please add photos and measurements from actual CW to the investigation ppt. See comments in ppt. Review below to see what steps have been compete vs still need doing.
- Jacob, please review plan, status, C/CA fields and report for this to see if you agree.


6/24/25
- @Steve Gonzales , @David Grosher recommends electrical as the next step in this investigation. Please update plan and status to latest. FYI @Connor Peebles  if you are working it.
- See ppt slides. Evaluate launch and prior flights to see if any abnormalities, things that could drive an abort.
- Look at AS150 history to see if SB was applied, impedance measured, etc.


Previous
@Jackson Riley Curvin 
- Plot Lift system Voltage, Total lift current and Current at each Boom during transition
- Plot attitudes (Pitch, Roll, Yaw) during transition as estimated by FW AP and VTOL AP
- Plot Airspeed
- Plot frequency of the GPS updates
- Re-evaluate Next Steps

## Comments (28)

### Drew Hildreth, 2025-07-22

@Steve Gonzales Do you have any updates on this Investigation? Do you need anything from the FSRs?
@Jackson Riley Curvin have you provided the Plots elsewhere?

### Steve Gonzales, 2025-07-22

@Drew Hildreth I have not started this one.  I should be able to work on it this week.

### Cody Smisek, 2025-09-03

@Steve Gonzales I see these cases sitting in engineering area. Can we return to RMA area or?

### Steve Gonzales, 2025-09-03

@Cody Smisek Hi Cody, if they need the cases, that is fine by me.  I have not started any work on this one but it is next in line.

### Cody Smisek, 2025-09-03

@Steve Gonzales placed on the engineering rack for time being.

### Pat Wells, 2025-09-03

@Cody Smisek We can’t do anything with this until a root cause is determined.  
@Steve Gonzales

### Steve Gonzales, 2025-10-17

@Cody Smisek @Drew Hildreth @Connor Peebles Hi, the CW is missing from the case.  Does anyone know where it may be at?

### Drew Hildreth, 2025-10-17

@Steve Gonzales I have no idea where the CW would have gone. It was in the case when it arrived and intake was completed by the RMA team. I am sure it is around somewhere. @Lauren Velasquez the CW for 541 hasn’t found it’s way back to you has it?

### Lauren Velasquez, 2025-10-17

@Drew Hildreth I do not have VXE-541 CW

### Steve Gonzales, 2025-10-22

Performed analysis and completed report.

### Steve Gonzales, 2025-10-27

Completed connector tests 10/24/25.

### Steve Gonzales, 2025-10-28

Center-wing found 10/24/25

### Steve Gonzales, 2025-10-29

Report completed

### Lauren Velasquez, 2025-11-12

@Drew Hildreth are we clear to move forward with this?

### Drew Hildreth, 2025-11-12

@Lauren Velasquez No.

### Cody Smisek, 2025-11-18

@Lauren Velasquez @Drew Hildreth I see this is assigned to Steve who is no longer with Edge. The aircraft is in engineering. Can we move the aircraft back to RMA or what’s the status?

### Drew Hildreth, 2025-11-18

@Cody Smisek That is fine. Steve finished up the report so this can go back to RMA.

@Lauren Velasquez I will ask about this, I don’t think they will pay to have it repaired… but I may be wrong.

### Samuel Lopez, 2025-12-16

- Per the investigation by Steve Gonzalez, this aircraft failed because HLB connector was not seated properly.

- VXE-541 was tested on bench using batteries.  XCOMM and VTOL were found to be working normally.  No electrical damage has been observed.

- Damage to fuselage, tail boom, wing tip right and left, and center wing observed (see pics)
[embedded Wing Tip Left.png]
[embedded Wing Tip Right.png]
[embedded Fuselage 1.png]
[embedded Fuselage 2.png]
[embedded Tail Boom 2.png]
[embedded Center Wing 1.png]
[embedded Air Data Pod missing.png]
[embedded Tail Boom 1.png]
Air data pod is missing

- Main battery holder is loose

### Samuel Lopez, 2025-12-29

Material Disposition has been given to Lauren Velasquez, which she will give to customer.  Awaiting to hear if they want to fix the AC.

### Jackson Riley Curvin, 2026-01-20

Closed on Global support side report finalized quote, and report to PM

### Steve Gonzales, 2025-10-29

Report completed

### Lauren Velasquez, 2025-11-12

@Drew Hildreth are we clear to move forward with this?

### Drew Hildreth, 2025-11-12

@Lauren Velasquez No.

### Cody Smisek, 2025-11-18

@Lauren Velasquez @Drew Hildreth I see this is assigned to Steve who is no longer with Edge. The aircraft is in engineering. Can we move the aircraft back to RMA or what’s the status?

### Drew Hildreth, 2025-11-18

@Cody Smisek That is fine. Steve finished up the report so this can go back to RMA.

@Lauren Velasquez I will ask about this, I don’t think they will pay to have it repaired… but I may be wrong.

### Samuel Lopez, 2025-12-16

- Per the investigation by Steve Gonzalez, this aircraft failed because HLB connector was not seated properly.

- VXE-541 was tested on bench using batteries.  XCOMM and VTOL were found to be working normally.  No electrical damage has been observed.

- Damage to fuselage, tail boom, wing tip right and left, and center wing observed (see pics)
[embedded Wing Tip Left.png]
[embedded Wing Tip Right.png]
[embedded Fuselage 1.png]
[embedded Fuselage 2.png]
[embedded Tail Boom 2.png]
[embedded Center Wing 1.png]
[embedded Air Data Pod missing.png]
[embedded Tail Boom 1.png]
Air data pod is missing

- Main battery holder is loose

### Samuel Lopez, 2025-12-29

Material Disposition has been given to Lauren Velasquez, which she will give to customer.  Awaiting to hear if they want to fix the AC.

### Jackson Riley Curvin, 2026-01-20

Closed on Global support side report finalized quote, and report to PM

## Attachments (14)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| DoD SAFE-DqATqc4viFoq5NWc.zip | archive | 120108 | 2025-05-13 | listed only |
| 1612a8c2-c1e9-4a7a-b01b-d1f1917829f7.jpg | image | 28 | 2025-05-14 | listed only |
| 16d3ef81-5d84-40ba-86a4-cf605557907a.jpg | image | 32 | 2025-05-14 | listed only |
| 2c27dd7b-5283-4029-ac33-7ecfc453bf35.jpg | image | 40 | 2025-05-14 | listed only |
| d776f9d4-b1cf-4593-859b-ae2958ead904.jpg | image | 19 | 2025-05-14 | listed only |
| Air Data Pod missing.png | image | 24310 | 2025-12-16 | listed only |
| Center Wing 1.png | image | 20808 | 2025-12-16 | listed only |
| Fuselage 1.png | image | 11701 | 2025-12-16 | listed only |
| Fuselage 2.png | image | 11785 | 2025-12-16 | listed only |
| Tail Boom 1.png | image | 30456 | 2025-12-16 | listed only |
| Tail Boom 2.png | image | 14103 | 2025-12-16 | listed only |
| Wing Tip Left.png | image | 10874 | 2025-12-16 | listed only |
| Wing Tip Right.png | image | 10272 | 2025-12-16 | listed only |
| [VXEP-1278_VXE-541_Vehicle Investigation_20260122.pptx](attachments/56414_VXEP-1278_VXE-541_Vehicle%20Investigation_20260122.pptx.md) | pptx | 139082 | 2026-05-12 | converted |
