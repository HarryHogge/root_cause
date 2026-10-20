# VXEP-1513: VXE-378 Fuel cell errors (overheating) and unable to maintain charge on HLB

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-09-18
- **Updated:** 2026-08-07
- **Resolved:** 2026-08-07
- **Reporter:** Michael Mohr
- **Assignee:** Sean Wendling
- **Creator:** Michael Mohr
- **Labels:** FBI, GS_Closed, Hardware, Weekly-incident-tracker
- **Links:** relates to FS2-3497 (XComm Fuel Cell GBurn is reset during fuel cell starts)
- **Customer:** FBI
- **Vehicle Tail Number:** 378
- **Severity:** 1 - Flight Critical
- **Components (EA Aircraft):** Battery, HLB, Fuel Cell

## Description

Had numerous attempted flights on 9/10/2025 and 9/11/2025 with a fuel cell bird during which we received errors in the GCS (related to overheating) as well has inability for the fuel cell to charge the HLB sufficiently for continued flight. 
Initial AARs from flights were missing logs so GS had the customer do a full pull form the aircraft 378.

## Vehicle Configuration

VXE-30
Battery

## Issue Status

Reviewing most recent log set (XCL178). Shows reactor unexpected high during flight, also observed some type of fuel cell power output issue coupled with reset of fuel remaining. 
Regarding reported ‘inability’ to charge HLB, it appears for this flight, operator launched aircraft and went immediately to 1200ft resulting in depletion of battery.

## Comments (9)

### Jackson Riley Curvin, 2025-09-25

[embedded image-20250925-140542.png]

### Cody Smisek, 2025-10-06

@Sean Wendling 
Just looked at the most recent flight in the logs. I see a reactor unexpected high (19472), which I’m guessing is what they’re referring to (although, I’m not sure how they know that, unless we recently implemented error deciphers in recent GCS SW). 
Also, not sure what happened around 2100sec, looks like fuel cell stopped outputting power. Not only that, do we have a bug where in air fuel cell restart resets fuel remaining?
[embedded image-20251007-022127.png]
[embedded image-20251007-022823.png]

### Cody Smisek, 2025-10-06

@Michael Mohr @Drew Hildreth What is the status of this customers aircraft / fuel cell? Is it still in use? Was it returned?

### Drew Hildreth, 2025-10-07

@Cody Smisek They haven’t been using them. We also haven’t received them via RMA yet. The customer is here in Huntsville so fairly easy access. Last discussion with the customer they were back in battery configuration.

### Cody Smisek, 2025-10-07

I was thinking that ‘GRemain’ was keeping track of actual remaining but maybe that’s not? Looks like ‘Burned’ kept track through the restart so not sure what the user would have seen for fuel remaining. 
[embedded image-20251007-145012.png]

### Sean Wendling, 2025-10-07

All,
First general notes, Fuel cell is a First Gen D450 / Not our latest hardware and also not running on the same software as the flagship product we are selling to the big programs right now (not that this reduces the urgency or need to address it, just want to tighten the scope of the investigation and not worry anyone about our more… vocal customers. 
Three issues to address in this ticket:
- Cody is correct that the “depletion” of the HLB is related to the rapid ascent and insufficient time for the fuel cell to rebound. You can see the prolonged period of ~1500W use resulting in depletion of the battery voltage while the fuel cell is still delivering power (just not enough to overcome the draw).
[embedded image-20251007-165112.png]
- The Actual fault that occurred “19742” is related to overheating reactor temperatures. This was the result of insufficient blower capacity in the first generation of fuel cells. Their Cathode blowers typically capped out at around 9,800-10,000 which I can see from the data. It flatlines bouncing off the top of that range as shown in the graph, it was not enough flow to overcome the combination of factors: (1) Ambient heat was high, (2) sat on the ground for a bit, (3) high output required leading to high fuel flow and the fuse temperature hasn't benefitted from the ram airflow for a while.
[embedded image-20251007-170734.png]


- The issue with the fuel count in the software I will need to pull the last active software config which will take some time. I am pretty concerned though given that the Gen1 D450 hasn’t had any change to the software on the fuel cell side in 2-3 years.. is this something we have seen anywhere else? @Cody Smisek @Michael Mohr @Drew Hildreth

Hope this clears some of this up. In terms of next actions, I can attempt to repair the fuel cell’s cathode and verify its efficiency if they would like to return the unit as an RMA. The stack looks healthy from the data I see here, assuming it is returned properly (lol) it should be a relatively smooth repair, just a challenge since the product is unsupported by our current production team so I will need to perform it myself. Additionally, @Michael Mohr what type of deliverable would the customer like to address the ticket? Report required?
Thanks, Sean

### Drew Hildreth, 2025-10-07

@Sean Wendling Thank you for the write up. We haven’t heard of these issues with any other customer that I am aware of. This Customer is easy to work with. We can send them an email, no formal report is necessary. 
As for returning the Fuel Cell, we will spin an RMA up and get it moving. Thank you all for the attention on this one.

### Ruysser Gabler, 2025-10-12

It is a known issue that fuel resets when the fuel cell is restartedhttps://jenaero.atlassian.net/browse/FS2-3497 See this issue here https://jenaero.atlassian.net/browse/FS2-3497 
We also reported it in OGCS testing a while back and it was discovered that the GCS, OGCS, and Xcom all had the same problematic code. @Ted Trowbridge fixed the OGCS code when we found it I believe

### Alexander Alan Arnold, 2026-08-07

replaced components on fc for customer

## Attachments (11)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| logs.zip | archive | 83518 | 2025-09-18 | listed only |
| T95_V378_250910_163431_pack.zip | archive | 153 | 2025-09-25 | listed only |
| T95_V378_250910_170324_pack.zip | archive | 262 | 2025-09-25 | listed only |
| T95_V378_250911_165417_pack.zip | archive | 454 | 2025-09-25 | listed only |
| T95_V378_250911_183451_pack.zip | archive | 296 | 2025-09-25 | listed only |
| image-20250925-140542.png | image | 19 | 2025-09-25 | listed only |
| image-20251007-022127.png | image | 161 | 2025-10-06 | listed only |
| image-20251007-022823.png | image | 13 | 2025-10-06 | listed only |
| image-20251007-145012.png | image | 35 | 2025-10-07 | listed only |
| image-20251007-165112.png | image | 80 | 2025-10-07 | listed only |
| image-20251007-170734.png | image | 106 | 2025-10-07 | listed only |
