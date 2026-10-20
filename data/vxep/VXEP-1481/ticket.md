# VXEP-1481: VXE-525 Crash after FPV drop

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-08-20
- **Updated:** 2026-03-02
- **Resolved:** 2025-10-29
- **Reporter:** Jackson Riley Curvin
- **Assignee:** David Grosher
- **Creator:** Jackson Riley Curvin
- **Labels:** USASOC
- **Customer:** USASOC
- **Vehicle Tail Number:** VXE-525
- **Vehicle Configuration:** VXE-30 Battery Configuration
- **Problem Type:** Other (explain in description)
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical
- **Components (EA Aircraft):** Aircraft, full assembly

## Description

We flew the stalker all day no issues. Attached a Nero’s archer 3lbs on the wings. Flew about 3k out then imitated our first drop. As soon as we dropped both the Nero’s and the stalker pretty much nosedived into the ground at about 800 ft agl.
Again, center panel broke off and we replaced screws. More damage to a tail boom and right wing.
Customer had 2 Nero archer drones one on each wing they only dropped one of the Drones. upon dropping 1 of them the aircraft nosedived.

## Plan

- Sort out if we have data from this flight. Ask for correct data, or if they want to close out the incident. Evaluate and determine plan.
- Review manual guidance for drop pylon limitations, determine if sufficient. Sam says within limits.
- Close if customer approves.

## Comments (12)

### Jackson Riley Curvin, 2025-08-20

[embedded image-20250820-191314.png]

### David Grosher, 2025-08-20

It looks like the system may have been in some sort of override mode because the elevator command was constant. Then there is a big jump when the munition was dropped, which would imply that the placement of the mass was not near the Xcg of the aircraft. Ideally the mass should be centered on the Xcg line projected out towards the wings. 

[embedded image-20250820-213148.png]
This is in the FDR file.

### Jackson Riley Curvin, 2025-08-20

@David Grosher  the customer said that they had 3 pounds on each wing along with a HD40 which weighs about 2-3 pounds

### Cody Smisek, 2025-08-20

any photos of the aircraft damage? which orientation are the FPVs mounted? and how are they arming them when releasing? they didn’t by chance hit a control surface, such as the tail, upon release? I didn’t look at the data, just saw this ticket and that’s what comes to mind. @Jackson Riley Curvin @David Grosher

### Jackson Riley Curvin, 2025-08-20

@Cody Smisek I will engage the customer tomorrow asking for that information

### Cody Smisek, 2025-08-20

I don’t see any type of limitations in the supplement for utility pylon. Was that intentional? Seems like we should have at least a weight and dimensional size limit (if known) on there. 
I guess I made an assumption… were they using utility pylon or some type of R&D method for dropping?

### Cody Smisek, 2025-08-20

@Jackson Riley Curvin the wording of the issue description could use some TLC. It reads like they were at 3000ft but then they were at 800ft? And did they have 1x or 2x FPVs? I just re-read it and it seems like just 1x

### Cody Smisek, 2025-08-20

@David Grosher I seem to remember that standard stalker didn’t have any issues doing the blood bag drops out of the payload area a couple years ago.

### Jackson Riley Curvin, 2025-08-20

@Cody Smisek will do we have had so many tickets came in in the past couple of days that I have just been putting the customer statements into the description with out reading them

### Drew Hildreth, 2025-08-26

@Jackson Riley Curvin @Michael Mohr Please get some updates to Cody. I thought they were flying with 2 Archers and when they dropped 1 that is when it rolled. Please verify and keep this ticket moving. 

Also get some confirmation on their statement. Pretty much nose-dived and only broke the screws on the center wing and some damage to the tail boom. I find their statement a bit off.

### Jeremy White, 2025-09-30

@Cody Smisek They were using our Wing Utility Pylon (PN 500-117326) with Jenning Legacy GCS for release. The only place with weight constraints is the Payload ICD which states 2lbs, but Sam said should be updated to 2.5lbs while integrating the Orbital Research munitions. No update has been made to the ICD.

### Cody Smisek, 2025-10-06

@David Grosher Looks like you’re referencing FDR00123 for your screenshot (last FDR in logs), and that FDR appears to show just a normal VTOL landing. 
Screenshot below for x-axis relative to time instead of row. 
The corresponding xcomm log also shows vtol throttles at beginning and end of log file (indicating normal VTOL landing). 
Given this, I would recommend the ticket is cancelled or put in a different bucket until someone provides information that can be correlated to the logs that were provided so we don’t have to hunt around. @Jackson Riley Curvin @Drew Hildreth @Jeremy White  
[embedded image-20251006-205454.png]
[embedded image-20251006-210119.png]

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| VTOL_VXE525.zip | archive | 69184 | 2025-08-20 | listed only |
| XCOMM_VXE525.zip | archive | 17648 | 2025-08-20 | listed only |
| image-20250820-191314.png | image | 43 | 2025-08-20 | listed only |
| image-20250820-213148.png | image | 21 | 2025-08-20 | listed only |
| image-20251006-205454.png | image | 105 | 2025-10-06 | listed only |
| image-20251006-210119.png | image | 128 | 2025-10-06 | listed only |
