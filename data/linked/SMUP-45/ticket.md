# SMUP-45: Review VXEP-652 and perform corrective actions

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-12-30
- **Updated:** 2025-03-16
- **Resolved:** 2025-01-09
- **Reporter:** Cody Smisek
- **Assignee:** Dana Holley
- **Creator:** Cody Smisek
- **Fix versions:** New beginnings!
- **Links:** relates to VXEP-652 (VXE 573 Cruise motor stopped during RTB, aircraft crashed)

## Description

Review VXEP-652 and perform corrective actions
Operator CFIT due to commanding Go To IP2. Manuals do not appear to explicitly outline the ramifications of performing this action. It is alluded to by the recommendations to avoid Go To IP4.

## Comments (16)

### Josh Burrell, 2024-12-31

@Cody Smisek this needs to be assigned to someone in FLOPS to examine and provide the manual correction. @Gregory Nichols can you please tag someone from your group?

### Gregory Nichols, 2025-01-06

@Josh Burrell Please get in contact with Dana Holley for the manual corrections.

### Dana Holley, 2025-01-09

@Cody Smisek Looks like the operator went to IP2 and not IP4. Either method would put em' in a CFIT. Unable to not use IP4 as it is required for various situations. AN-24-002 states how to plan for a IP4 landing. I added when the appropriate times were to use IP4 approaches. Both are now in the new Ops Manual.  Marking ticket as Done.

### Cody Smisek, 2025-01-09

Confirming we added no wording to prohibit or discourage go to IP2? @Dana Holley 

Your first sentence suggests I stated they went to IP4, which is not the case. They most certainly went to IP2. However, I'm not seeing any type of guidance to discourage that action. Just the guidance regarding IP4

### Dana Holley, 2025-01-09

@Cody Smisek I was referring to the statement made in the description of this SMU ticket…”It is alluded to by the recommendations to avoid Go To IP4.” I’m thinking this is meant to say IP2? 
If we aren’t using IP2, is there a plan to block that feature in the next software release? Or should I just state in the manual as a CAUTION that commanding Go To IP2 beyond 1 KM from the WP is not recommended as the aircraft will adopt the waypoint properties to include it’s altitude and could result in CFIT?

### Cody Smisek, 2025-01-10

my wording is intended as written. the AN suggests that you should take precautions when not using the standard RTB method of returning to the LZ. one could reasonably draw conclusions that this would also be applied to IP2 as well.
I cannot speak to future software plans. All I can speak to is the right now state of the hardware, and the right now state is that if you go to IP2 you will have the same outcome as IP4. But I do not see that written in any manuals or ANs. 
@Dana Holley

### Dana Holley, 2025-01-10

@Cody Smisek Sounds good. So what statement or content would you like to put into the manual?

### Cody Smisek, 2025-01-10

@Pat Wells says it’s completed. close ticket.

### Pat Wells, 2025-01-10

@Dana Holley @Josh Burrell the same language used for the GOTO IP5 AN should be applicable to this.  Correct me if I’m wrong.

### Josh Burrell, 2025-01-10

@Pat Wells I think so but I’m going to defer to @Dana Holley to answer if that’s correct. However, it sounds like there was an issue with mismatching software in this case. So, is there really a need for a change in the OPS if thats the case?

### Dana Holley, 2025-01-10

@Pat Wells @Josh Burrell In my opinion it does not apply. The Go To IP4 AN had language structured and technique written specifically for IP4 , which is why we created two orbits with one 100 ft. above landing pattern altitude. The AN was also missing language as to why you would conduct an IP4 landing vs. a “normal” approach, so I had carefully input those in consideration in regards to all scenarios (See below).  Bullet point 2 and 3 are the main reasons we do not use Go To IP2. 

Operators should only plan and use the “Go To” IP4 technique when the following conditions are met: 
- Energy remaining is insufficient to climb IP1.
- When flight over any prior segment of the landing pattern poses a risk to ground property or personnel.
- When the aircraft fails to descend in IP2, which can be common on a hot or windy day.

### Dana Holley, 2025-02-18

@Pat Wells Can we cancel this ticket or is there something you would like me to add based on my previous feedback?

### Pat Wells, 2025-02-18

@Dana Holley so are you saying that there were no updates made to the manual on this issue?

### Dana Holley, 2025-02-18

@Pat Wells That is correct. Previous recommendation was to add the same language in IP4 situations for aircraft using GOTO IP2, but IP4 approaches are only used for different reasons (see comment below). Really don’t have any use cases for using GOTOIP2. Only corner case instance I can think of where using a GOTO IP2 for an appropriate reason would be for straight-in approaches if the aircraft cannot descend in IP2 and their is terrain prevent from orbiting down adjacent to IP4.
I could clarify a bit more on GOTO in the Ops Manual stating that the aircraft will adopt the WP properties to include altitude as soon as the command is given? And add an extra CAUTION stating GOTO commands for IP2 or IP4 should not be given within 1 KM of the landing pattern?
[embedded: image-20250218-203214.png]

### Pat Wells, 2025-02-18

@Dana Holley I like your suggestion. Let’s make that adjustment and close this out.

### Dana Holley, 2025-02-18

@Pat Wells Added Caution and additional content to 3.17.2 of Ops manual.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20250218-203214.png | image | 21 | 2025-02-18 | listed only |
