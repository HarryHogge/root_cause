# ENG-2973: Aircraft 439 Launch Failure-No HW to investigate

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Medium
- **Created:** 2023-07-13
- **Updated:** 2026-08-31
- **Resolved:** 2026-04-28
- **Reporter:** Cameron Chapman
- **Assignee:** Daniel Lloyd
- **Creator:** Cameron Chapman
- **Links:** relates to SMUP-86 (Add blade strike warning to manual); relates to VA-312 (Add blade strike ESC damage warning to manual. ); relates to VXEP-628 (Systemic VXE30 VTOL ESC Reliability Issues )

## Description

This was the second flight of the day for this aircraft. The launch wizard was completed without issue. At launch the aircraft lifted a little more than one foot from the stand and then abruptly pitched forward and left. After impacting the stand it settled to the right. The aircraft launched, aborted, crashed, all in about 2 seconds. The GCS did not indicate that it detected a landing, the software still had the activate user launch control window display. It did however pop up the AAR window and safe the lift system. Inspection of the aircraft showed no damage. Since the aircraft wasn’t sure that it had landed, the servos and motor braking were still powered. Of the 5 motors all exhibited braking affect except the forward left lift motor, it could spin freely. A launch wizard motor check was performed and the forward left motor would not spin and it would not home after the system was safed. 
The range on which they are operating has areas of tall grass. On the first landing of the day the aircraft drifted forward and landed in tall grass. The sound of the lift rotors hitting the grass could be heard. A post flight visual inspection of the left forward lift motor after the failed launch showed grass debris around the motor shaft.

## Comments (22)

### Cameron Chapman, 2023-07-13

Thanks @Daniel Lloyd for reporting. 
- Can you please email FDR when available?
- Did the motor spin during launch wizard?
- Does the motor spin via launch wizard after the abort?
- Are you able to swap a new boom and test if it works in that position?

### Daniel Lloyd, 2023-07-13

Edited the description, added pictures and AAR. Did not have the resources at the time to swap the lift boom. Do not have a spare motor on hand.

### Daniel Lloyd, 2023-07-14

It looks like my description didn’t save. I’ll try again later.

### Daniel Lloyd, 2023-07-14

Additional information. Aircraft 438 also drifted into tall grass on the last flight of the day (Thursday). The right front lift motor got tangled with grass (see photos). The debris was cleared and a launch wizard motor check was performed without issue. On the first flight of the next day (Friday) the right front lift motor sounded weaker than the other motors. After 4 motor spin checks the motor stopped responding. It would not home after the system was safed and it did not exhibit any braking affect. A different boom was swapped in and the aircraft was flown three times.

### Cameron Chapman, 2023-07-14

Thanks Dan. Great description. It sounds like latent ESC damage due to the blade strike, but could also be something (hardware or software) with the input signal. @John Clark do you have anyone available to review the attached FDR to see if the throttle signals look normal? 
Once data is confirmed normal, I suggest removing this motor assembly for inspection and maybe replacement.  
@Daniel Lloyd are you available to open the ESC lid and inspect for damage, or would you rather send back to us to do that.
@Sean Odell we should plan to RMA and send a replacement motor assembly.
FYI @Pat Wells

### Daniel Lloyd, 2023-07-14

Added information of a second incident and photos. 
I would like to look into the ESC but it is unlikely I will get permission from the U.S. Navy customer to perform maintenance.

### Daniel Lloyd, 2023-07-14

If we determine that the failure is related to the grass debris we need to get the manuals team involved to add a Caution to the operators manual.
I would recommend:
Allowing the aircraft lift system rotors to become entangled in tall grass/brush will cause irreparable damage to the lift motor ESC. Passing a launch wizard motor spin check is not a reliable indicator of a healthy motor system after such an event. The motor/ESC assembly must be replaced. Failure to replace the lift motor/ESC assembly may result in damage or loss of aircraft due to a lift motor failure.

### Cameron Chapman, 2023-07-16

Thanks Dan for the update. What does the US Navy customer usually do with damaged or suspect parts, or is this a first time? 
It would be best to inspect the ESC to confirm if possible. I have seen blade strikes damage ESCs before. It makes sense that tall grass could have the same effect. I agree that such a warning should be added. @Dana Holley, creating a corrective action to add that warning.

### Daniel Lloyd, 2023-07-17

The motors might be replaced at this location or the booms could be shipped back to ERI in Camarillo for maintenance. In either case they would probably send the motor assemblies to you if you request them.

### Dana Holley, 2023-07-17

@Cameron Chapman @Daniel Lloyd @Gregory Nichols @Artis Bertulis  Yes I can make this a Caution, but there's potentially bigger issue here with the esc/motor check.  Was there grass in the left front lift motor during the entirety of the second flight?

### Daniel Lloyd, 2023-07-17

There was no second flight for aircraft 439. In both cases the motor assemblies failed during the LW for the flight following the landing where grass was entangled.

### Dana Holley, 2023-07-17

@Daniel Lloyd @Artis Bertulis @Gregory Nichols Here’s what I think would be the best path moving forward based upon current documentation. The mx (maintenance) manual lists the pre-flight checklist items which includes lift motor and esc assembly. The Launch Site requirements states to avoid landing in tall grass. Tall grass is subjective and not defined. I will further add in the manual that tall grass is listed as motor height when the AV is on the ground. 
[embedded: image-20230717-165433.png]
[embedded: image-20230717-164638.png]

### Dana Holley, 2023-07-17

Forgot to add that a WARNING does exist for this. 
[embedded: image-20230717-170607.png]

### Cameron Chapman, 2023-07-17

@Dana Holley to keep the investigation focused, I think it will be best to move the manual update conversation here https://jenaero.atlassian.net/browse/SMU-52and keep this ticket for the investigation.  

“In both cases the motor assemblies failed during the LW for the flight following the landing where grass was entangled.”
@Daniel Lloyd Clarifying the order of events and questions from the description. It sounds like the following. 
- Aircraft flew, drifted forward during landing, and landed in tall grass. (Was this due to wind/normal drift, or could this also be an issue)
- The sound of the lift rotors hitting the grass could be heard. A post flight visual inspection of the left forward lift motor after the failed launch showed grass debris around the motor shaft.
- Do you suspect a similar strike on the front right, or just the left?
- The launch wizard was completed without issue. At launch the aircraft lifted a little more than one foot from the stand and then abruptly pitched forward and left. After impacting the stand it settled to the right. The aircraft launched, aborted, crashed, all in about 2 seconds. The GCS did not indicate that it detected a landing, the software still had the activate user launch control window display. It did however pop up the AAR window and safe the lift system. Inspection of the aircraft showed no damage. Since the aircraft wasn’t sure that it had landed, the servos and motor braking were still powered. Of the 5 motors all exhibited braking affect except the forward left lift motor, it could spin freely.
- A launch wizard motor check was performed and the forward left motor would not spin and it would not home after the system was safed.


I am pretty sure the front left ESC or motor is damaged. If you are unable/do not recommend inspection in the field, please send it back to us. @Sean Odell can you please open a RMA for this?

### Kurt Burian, 2023-07-17

Crash detect triggered after huge pitch departure. Digging in now.

### Daniel Lloyd, 2023-07-17

@Cameron Chapman 
- The forward drift on landing was not unusual. They may have been practicing some nudge.
- a. Both forward motors may have contacted the grass. The left front was the only one with evidence of grass debris around the motor shaft.

### Kurt Burian, 2023-07-17

It seems like the front left isnt consuming enough power. It gets commanded 91% throttle and doesn't seem to have any effect on slowing the pitch, while the roll gets corrected. The left boom current was lower then right the entire event. It would be neat if we had a table of throttle position to expected motor power/current. Any chance that exists? If so we can see if the boom currents add up to the expected.

[embedded: image-20230717-205152.png]

### Connor Peebles, 2023-07-17

Check out the this excel where Dustin calculated Expected Boom Power vs Actual in terms of Lift Throttle
Calculating Expected vs Actual Power for Lift Booms in terms of throttle The example one is from VIT426
I will separate the example in that folder from the formulas in a bit

### Kurt Burian, 2023-07-18

@Cameron Chapman Tagging you for further investigation. Let me know if there is anything else. Thanks. @Greg Fryer @David Grosher

### Cameron Chapman, 2023-07-18

Thanks Kurt. It seems like the evidence points to front left damage, but no indications of front right damage. I recommend returning the front left motor for replacement.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent.

### Christa Meck, 2026-04-27

@Cameron Chapman Can we close this ancient ticket from LMCO ?

## Attachments (10)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 439 Crash1.jpg | image | 5624 | 2023-07-13 | listed only |
| 439 Crash2.jpg | image | 5659 | 2023-07-13 | listed only |
| Grass debris.jpg | image | 1361 | 2023-07-13 | listed only |
| T95_V439_230713_103227_pack.zip | archive | 1211 | 2023-07-13 | listed only |
| 438 Grass Debris.JPG | image | 4116 | 2023-07-14 | listed only |
| 438 Grass Landing.JPG | image | 9553 | 2023-07-14 | listed only |
| image-20230717-164638.png | image | 12 | 2023-07-17 | listed only |
| image-20230717-165433.png | image | 16 | 2023-07-17 | listed only |
| image-20230717-170607.png | image | 9 | 2023-07-17 | listed only |
| image-20230717-205152.png | image | 110 | 2023-07-17 | listed only |
