# VXEP-1929: VXE 878 - Lithuanian Border Guard Near Miss - GPS Fault

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2026-06-23
- **Updated:** 2026-07-06
- **Resolved:** 2026-07-06
- **Reporter:** Stephan Johnson
- **Assignee:** David Grosher
- **Creator:** Stephan Johnson
- **Labels:** GS_Closed, RCCA, Weekly-incident-tracker
- **Links:** relates to FS2-4848 (VXEP-1929 investigation)
- **Customer:** Lithuania-Border-Guard
- **Part Number(s):** 107-102461
- **Vehicle Tail Number:** VXE 878
- **Severity:** 1 - Flight Critical

## Description

During the landing of VXE 878, a VTOL error populated when the aircraft hit IP5 and tried to send the aircraft into an Emergency Landing. This occurred twice before the operator was able to descend to ~400ft AGL, and use Pause/Nudge to land the aircraft. The aircraft was able to land safely, but the customer has suspended operations until the root cause of the issue is identified. 
Customer stated this is a continuous issue. Previous historical AARs have been added for reference.

## Comments (14)

### Drew Hildreth, 2026-06-23

@Scott Lovett @David Grosher Please take a look at these. The customer has “grounded” their fleet.

### Cody Smisek, 2026-06-23

Have they considered the possibility of GNSS jamming in their area?
Are they also losing comms during this? It seems like that is also occurring (edit: maybe that’s just legacy GCS thing when mission sync is occurring, looking at debug logs). 
Are they operating in an area where other RF equipment is located?
Is this their only system? Is it occurring on only this system?

[embedded: image-20260623-133446.png]
[embedded: image-20260623-133537.png]

### Drew Hildreth, 2026-06-23

@Cody Smisek Currently this is the only system they have. 937 had a XCOMM Processor reset and crashed, 938 presenting resets so we are getting them a new avionics. 878 is their last.

### Drew Hildreth, 2026-06-23

@Cody Smisek I have reached out to the customer to see if GNSS Jamming has been common in their area. They typically fly at night their time so it may be a few hours before we hear back from them

### David Grosher, 2026-06-23

@Drew Hildreth @Cody Smisek 
They are almost certainly experiencing jamming from a specific direction, the Cn0 is a function of heading while in an orbit. 

[embedded: image-20260623-191458.png]

### Drew Hildreth, 2026-06-23

@David Grosher @Cody Smisek I appreciate the look at these.

I will communicate to the customer.

### Drew Hildreth, 2026-06-26

@David Grosher we have communicated that they were most likely getting jammed and that the aircraft was behaving as it should. Is there anything else that has popped in the data that we should be aware of? Customer wants to get back to flight, just wants an official “Yes you can fly” from us.

### David Grosher, 2026-06-26

@Drew Hildreth There was nothing that I saw that would make me think it is unsafe to fly. Having said that, we don’t analyze all of the data in detail if it isn’t releated to the reported incident, as there is a massive amount of data and it could be extreamly time consuming.

### Drew Hildreth, 2026-06-26

@David Grosher Thanks Dave.

### Stephan Johnson, 2026-06-29

- @Scott Whitney can you take a look at this. Initial thoughts were jamming, but we want to verify with you all.

### Scott Whitney, 2026-06-30

@Stephan Johnson - Based on Dave comments below it seems like there should be nothing stopping the customer from continuing flights.  @Eric Brewer is currently on PTO, but I can have him take a second look at the data and give his findings.

### Alexander Alan Arnold, 2026-07-06

@Drew Hildreth see Scotts comment

### Eric Brewer, 2026-07-06

@Scott Whitney @Stephan Johnson @Alexander Alan Arnold concur there are frequent CN0 drops during flight that do not appear in earlier logs (I looked at T95_V878_260617_131816_pack for reference).  It looks like it’s impacting both fixed-wing and vtol.  VTOL will pop up more frequent alerts because it’s more sensitive to GPS outages.  If they are seeing this across multiple aircraft it’s likely jamming, if it’s just this one they could inspect the antenna hardware, though it looks like both fixed-wing and vtol gps are affected.

### Scott Lovett, 2026-07-06

Suspected GPS jamming. Will reopen if this issue re-appears.

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 878 - 17JUN26.zip | archive | 10069 | 2026-06-23 | listed only |
| 878 - 23JUN26.zip | archive | 4125 | 2026-06-23 | listed only |
| T95_V878_260623_055148_pack.zip | archive | 3062 | 2026-06-23 | listed only |
| image-20260623-133446.png | image | 127 | 2026-06-23 | listed only |
| image-20260623-133537.png | image | 222 | 2026-06-23 | listed only |
| image-20260623-191458.png | image | 107 | 2026-06-23 | listed only |
