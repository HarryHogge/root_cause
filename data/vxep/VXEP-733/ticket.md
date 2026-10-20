# VXEP-733: VXE510 Pitch Up during forward transition

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Low
- **Created:** 2024-10-22
- **Updated:** 2024-12-05
- **Resolved:** 2024-12-05
- **Reporter:** Cody Smisek
- **Assignee:** Eric Brewer
- **Creator:** Cody Smisek
- **Labels:** FlightSystems
- **Vehicle Tail Number:** VXE510
- **Vehicle Configuration:** standard stalker battery configuration no payload
- **Corrective Action:** None.
- **Issue Status:** Recommended for closure.
- **Incident Type:** Squawk
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

LM Testing in Pendleton, OR 10/22/2024.
Aircraft in battery configuration, no payload. 
During vtol transition (after vtol motors stopped and fixed wing flight began) large pitch up followed by pitch down. Customer and LM commented about the excessive look of pitch.

T95_V510_241022_085416_pack - AAR for flight

## Root Cause

It is unclear what caused the pitch up but subsequent flights looked normal so the issue is likely due to environmental factors.

## Comments (12)

### Cody Smisek, 2024-10-22

@Greg Fryer @Douglas Baker FYI

### Greg Fryer, 2024-10-22

@Scott Whitney Another record to have someone look at. (@Cody Smisek Dave is out this week so skipping to Scott)

### David Grosher, 2024-11-07

@Eric Brewer Could you take a look at this.

### Eric Brewer, 2024-11-07

@David Grosher @Greg Fryer @Cody Smisek It looks like toward the end of transition the vtol motors were holding a good bit of trim (LR/RR motors still on significantly, RR > 0.6).  As soon as the motors power down the vehicle pitches up.  The things I’d check:
1. CG - is this a configuration we’ve flown before? Anything different about it?
2. Elevator trim - was there a large offset in the 0 value of the elevator?  The trim command logged on xcomm does not indicate this is the case but still worth checking.
Has this vehicle been flown again since? Any other AAR’s before/after we can review?

### Cody Smisek, 2024-11-07

@Eric Brewer vehicle configuration is in the details section. no payload would put the aircraft at forward limit for the flight. I added all AARs from the testing while I was there. The flights after had payloads installed with alternate CGs. Elevator trim offset should be in the logs? There was no abnormal trim changes during launch wizard for these flights. 
Yes aircraft flew immediately after the flight.

### Eric Brewer, 2024-11-07

@Cody Smisek thanks.  That big overshoot (>36 degrees) shows up on this log as well - T95_V510_241023_132040_pack.  The other logs were around 20-25 degrees pitch up after transition which compares well with typical birds.  Is it possible this is just normal for vehicles in the forward CG configuration? Do you know of any reference logs in that configuration you could point me to?

### Cody Smisek, 2024-11-07

@Eric Brewer first flight of every new SCO aircraft is no payload forward CG. I will grab a few and add to subtask to divide the clutter.

### Greg Fryer, 2024-11-07

@Eric Brewer Did you check “the fundamentals” too - e.g. firmware versions and such? If there’s no indication of what’s different (I saw your notes under the subtask), we may simply have to close “Bermuda Triangle”. Given following flights were all normal, there doesn’t seem to be much else to investigate. Review with @David Grosher prior to doing that though.
Also, moved this to D4 investigating root cause. Bermuda Triangle is under D8, if needed.

### Eric Brewer, 2024-11-08

Thanks @Greg Fryer .  The configs and software versions looked correct to me.
There were two flights that had the large overshoot - T95_V510_241022_085416_pack and T95_V510_241023_132040_pack.  Given it happened twice would that fit as a 'bermuda triangle' or does this warrant more investigation?
I think if we wanted to look into it more the next steps would be physical inspection to verify:
- Elevator trim and operation (range, backlash etc)
- CG location
- Anything else off-nominal

### David Grosher, 2024-12-04

@Greg Fryer @Pat Wells Do we need to investigate this further? Or can we close this?

### Greg Fryer, 2024-12-05

@David Grosher @Eric Brewer We have not stated a conclusion, no. Since the plane flew normally in other flights (right after, per @Cody Smisek , the physical investigation is unlikely to show anything.
If nothing is showing as wrong, we can state as “likely environmental factors” in the root cause box, and then close Bermuda triangle (since we can’t prove it, and Cody was there so we know it wasn’t some obvious environmental factor).
What I’m saying is “You have to type something in the root cause box, even if it’s just our best estimate. Then you can close it.”

### Eric Brewer, 2024-12-05

@David Grosher @Greg Fryer Root cause updated above.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V510_241022_085416_pack.zip | archive | 1878 | 2024-10-22 | listed only |
| T95_V510_241022_101722_pack.zip | archive | 3645 | 2024-11-07 | listed only |
| T95_V510_241022_144355_pack.zip | archive | 4501 | 2024-11-07 | listed only |
| T95_V510_241023_132040_pack.zip | archive | 3792 | 2024-11-07 | listed only |
| T95_V510_241023_141931_pack.zip | archive | 4491 | 2024-11-07 | listed only |
