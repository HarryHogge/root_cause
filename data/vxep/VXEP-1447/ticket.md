# VXEP-1447: VXE 880 Fuel Flame out

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-07-23
- **Updated:** 2026-08-10
- **Resolved:** 2026-08-10
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Sean Wendling
- **Creator:** Alexander Alan Arnold
- **Labels:** GS_Closed, RCCA, Weekly-incident-tracker
- **Customer:** Redwire
- **Vehicle Configuration:** 35 x fuselage, standard HLB, E140G2Z, updated airdata pod
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

During an endurance flight the fuel cell 4500856 went from 200 grams remaining to zero
aircraft weighed 46.5 lbs. 
tank 1240 was tank weight 928 was fuel weight 

Flight time was 6 hours and 32 minutes 
we were shooting for 8+

## Corrective Action

AA to provide updated list of fuel cell faults to flight ops and SLO engineering. List to be published on confluence at minimum. @Sean Wendling 
AA to provide fuel cell system accuracy to HSV flight ops for publishing in manuals @Sean Wendling @Anthony Hansen 
Consider GCS improvement for fuel cell equipped aircraft to provide range of fuel remaining based on system accuracy as provided by AA. For example, if system has 5% possible error, at 800g of fuel used with 100g remaining, display a value that includes the minimum, 60g (800g*0.05=40g….. 100g-40g=60g) @Ted Trowbridge @Scott Whitney

## Issue Status

---Cody Smisek writes ---
Data indicates fuel starvation. Fuel PWM, fuelset & fuelreal all indicate no fuel available to fuel cell. 
Based on duration of flight and fuel remaining at time of landing, it would seem that the tank was likely empty (at time of landing) resulting in fuel starvation (that is, no abnormal failures preventing fuel to the fuel cell). 
Unfortunately, likely within the normal margin for error for this system. With no method to measure actual fuel remaining, operator must actively monitor status of fuel cell during last ~10-15% of fuel and prepare contingencies in event of early fuel cell shutoff. 
I defer to AA team if there is reason to perform a leak check of this system to confirm that no leaks are present. My personal recommendation would be to not allocate time to this check. 

Ticket was created July of 2025. Recommend closing out. 
---END---

## Root Cause

Fuel starvation resulting in operator performing landing. Fuel remaining measurement likely within overall system error margin which resulted in system indicating fuel remaining when no actual fuel was remaining in tank.

## Comments (13)

### Jackson Riley Curvin, 2026-07-13

@Charles Sweet Can you please take a look at this?

### Cody Smisek, 2026-07-13

@Jackson Riley Curvin @Alexander Alan Arnold the vehicle config in this ticket says B35. Based on the AAR, that doesn’t seem correct. Is this a B35X? Have we flown B35X vehicles with fuel cell before?

### Jackson Riley Curvin, 2026-07-13

@Cody Smisek this is a 35x fuselage with standard 30 centerwing

### Cody Smisek, 2026-07-13

The description does not match the data. 
@Alexander Alan Arnold can we get additional information on this. Where was it observed that the fuel remaining went from 200 to 0? 
I see starting fuel was set to 926, the system landed with >0g (~100g). I do see the fuel PWM railed high prior to landing but not sure how much more we want to look into this until we have a better description of events.
@Charles Sweet 

[embedded: image-20260714-010015.png]
[embedded: image-20260714-010117.png]

### Cody Smisek, 2026-07-13

@Jackson Riley Curvin And we have previously flown 35X with fuel cell and this is a supported configuration?

### Jackson Riley Curvin, 2026-07-13

@Cody Smisek I’ll have to do some more digging in the morning and get back with you do you know what the difference is between and 35x fuselage and an advanced nav? Is it just the LEMB data cable?

### Cody Smisek, 2026-07-13

@Jackson Riley Curvin The hardware is all the same. I’m getting at this possibly being an unsupported configuration with regard to software. One point in time long ago 35X was stop gap to be used with LEMB. Maybe it does supports fuel cell, but I’m not 100% sure, I want to make sure we aren’t flying something that is getting ahead of the software support. I asked @Scott Whitney very nicely if he’d ask the SW team.

### Cody Smisek, 2026-07-13

I’m making guesses based on this ticket name / description. 
First, if we’re not training this we need to be. Simply because a fuel amount was entered into the launch wizard does not mean that’s the fuel remaining. It’s an estimate unfortunately. Many variables could result in that value being inaccurate, such as incorrect weighing of tank (to include incorrect starting weight, incorrect fueled weight, incorrect sticker weights), incorrect fuel flow from the fuel cell, and potential leaks in the system. 
As of today, VXE systems do not have a method to measure actual fuel remaining (no special tank float sensors). 
It appears we just ran out of fuel during flight with the system indicating it still had ~100g remaining. I do not see a STOP command sent in the logs, but I do see the system state go to 6 ( I believe this is cooldown) from 5 (running) with fuel PWM going high (normal ~500, and high being ~1000 indicating system asking for fuel but not getting it). Which can be further confirmed by looking at fuelset vs fuel real (fuel real dropped below set point). 
@Charles Sweet can you remind me the accuracy of our fuel flow meter sensor? I feel like 5% comes to mind and a message with Tom from a while ago confirms that. 5% of 900g is ~45g. So right of the go, we could have up to 45g of fuel used that isn’t properly measured by the sensors. 

[embedded: image-20260714-012955.png]

### Cody Smisek, 2026-07-13

I just noticed this ticket was created July 2025. 
Unless there is additional leadership request to further analyze this issue, I would close it out based on my findings and not spend any additional engineering resources on investigating. 
Future designs for B40 are to provide more robust fuel remaining information. 
@Scott Whitney @Jackson Riley Curvin @Alexander Alan Arnold @Charles Sweet @Sean Wendling

### Alexander Alan Arnold, 2026-07-13

This ticket was created at the end of the LRT (marine corps test event) it was an adv nav or 35x configuration(I dont believe there’s many differences) while 35x isn’t a continued platform a better understanding of endurance limitations in an ADV Nav configuration would be beneficial due to the decreased endurance  of swapping from standard VXE to ADV NAV. @Cody Smisek @Jackson Riley Curvin

### Scott Whitney, 2026-07-13

@Cody Smisek @Jackson Riley Curvin  - Fuel Cell is not supported in B35x configuration - it has never been tested or flight qualified.

### Cody Smisek, 2026-07-14

@Alexander Alan Arnold Added recommended corrective actions to ticket.

### Alexander Alan Arnold, 2026-08-10

after testing in HSV we found vxe 30adv nav typically get to 6.5-7.5 hours. we will provide updated data once flight ops complete endurance testing suite

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T115_V880_250721_073132_pack.zip | archive | 6695 | 2025-07-23 | listed only |
| image-20260714-010015.png | image | 108 | 2026-07-13 | listed only |
| image-20260714-010117.png | image | 141 | 2026-07-13 | listed only |
| image-20260714-012955.png | image | 109 | 2026-07-13 | listed only |
