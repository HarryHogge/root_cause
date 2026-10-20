# VXEP-18: TPTR-59 Wing vibrations during VTOL Landings

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2023-08-23
- **Updated:** 2023-09-27
- **Resolved:** 2023-09-27
- **Reporter:** Allen Gardner
- **Assignee:** Greg Fryer
- **Creator:** Allen Gardner
- **Links:** is blocked by VA-389 (Get write up from wing flapping during VTOL prior incidents, review if applicable to TIQ incident VXEP-18); relates to ENG-3162 (VXE490, 491 Oscillation )
- **Customer:** TIQUILA
- **Corrective Action:** None required, no risk to aircraft or airworthiness.
- **Plan:** Review occurrence to compare to prior incidents. Complete
- **Issue Status:** Complete
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

strange wing vibrations which happened twice during VTOL landings. At no point was it violent enough to cease flying however that is irrelevant as it was in a VTOL landing an once committed the airframe has no way of leaving that manoeuvre. After each occasion VTOL rotors were thoroughly checked and this never occurred during take-off. However it was extremely visible and all of the team commented it looked like a bird flapping. After the second occasion we ceased flying and then tried it again the next day, were upon it flew correctly. Inzpire commented that the wings are only held on by a clip rather than screws and if those vibrations become more pronounced or violent it could cause the clip to fail, however it would need to be far more violent than what was experienced.
Shah, Dhruti (UK) - Mon Jul 10 21:25:48 BST 2023 : Vendor PTR-B 10/7/23: Recommend lowering PTR Priority. Issue is not as extreme as described. Issue is present on all Platforms and not considered a flight safety issue. Triggered further by flight conditions and due to stiffness of the structure.

## Root Cause

Link to report on prior incident. Behavior caused by combination of controls, wind conditions, and exact decent profile.
https://jenaero.sharepoint.com/:w:/s/EngineeringTeam/EaBzWiraHjVDm8zZr6Ijq4ABL8NWjHFn5Dp2k6VgoPOVAA?e=XPA7mc

## Comments (6)

### Cameron Chapman, 2023-08-24

@Scott Stuckey have we done any troubleshooting on this yet? Can you please link if so?

### Cameron Chapman, 2023-08-29

@Matt Weber @Hans Hershberger see question below.

### Matt Weber, 2023-09-05

First I’ve heard of this, I just watched the videos in the linked issues.  Were the lift blades checked for imbalance?  Looks like some resonant frequency that can only be tied to the motor rpm.  
Edit:  re-watching the clip it looks like the oscillation happens at more than just one rpm, so blades are unlikely to remain in sync and is more likely a controls/roll-correction-timing issue than a hardware balance issue.

### Greg Fryer, 2023-09-27

@Matt Weber - There was some test/analysis done by @Jack Waeschle and @Ryan Christino. We basically determined that there is a combination of mechanical stiffness and the controls. The immediate conclusion is there is no threat to the aircraft or it’s airworthiness (it does not amplify/resonate, and it just does it). 
I think there’s an intent to have @Everett Werner do some analysis (@Former user and Ryan C. discussed it, at least.)
Given it is not a flight issue, I will likely close this incident (there is a report linked to https://jenaero.atlassian.net/browse/VA-389 that I will link here) and move the investigation tasks to a project.
Everyone has today, or at least a few hours, to object!

### Matt Weber, 2023-09-27

@Greg Fryer  Jack kept me in the loop and I was able to see the analysis.  I agree that it does not appear to be a flight safety concern, but is a gain/clock speed issue that we should be able to sort out.

### Greg Fryer, 2023-09-27

Investigation tasks moved to Project https://jenaero.atlassian.net/browse/VXEP-104 and Epic https://jenaero.atlassian.net/browse/VA-606
Will be on hold pending time available.

## Attachments (0)
