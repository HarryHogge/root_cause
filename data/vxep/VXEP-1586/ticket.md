# VXEP-1586: VXE 593 smoking fuel cell

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-10-31
- **Updated:** 2026-09-29
- **Resolved:** 2026-09-29
- **Reporter:** David Grosher
- **Assignee:** Sean Wendling
- **Creator:** David Grosher
- **Labels:** MOLSON
- **Links:** clones VXEP-1554 (VXE-593 Aborted launch ); relates to VXEP-1794 (VXE 820 Fuel Cell not charging HLB in flight); relates to VXEP-1799 (B30 VXE 820 Forced to use ELZ due to HLB being to low to VTOL land safely); relates to RMA-973 (D4500799 RMA 260421-4)
- **Customer:** MOLSON
- **Vehicle Tail Number:** 593
- **Incident Type:** Mission Failure/Abort
- **Severity:** 1 - Flight Critical

## Description

During the take-off we had a magnetometer fail and the aircraft aborted launch and landed safely.  We have attached the AAR for the flight.
Post landing while disassembling the air vehicle we notice smoke coming from the nose cone we proceed to remove the nose cone and the fuel all and it was smoking internally (see attached picture and video)
We operated in the following configuration:
VXE30 in fuel cell configuration 
E140Z G2 gimbal
 
No additional payloads.
Aircraft SN: 593
Fuel Cell SN: D4500799

## Vehicle Configuration

Standard VXE30
Fuel Cell
E140 G2-Z

## Plan

Gathering Information:
- @Michael Mohr , do you think you could gather the general timeline of events from the users. When the abort occurred, what steps did they take to evaluate the abort? Immediate inspection and disassembly? Did they allow the fuel cell to cool down. Perhaps they have more than just the one AAR package?
- @Sean Wendling Will review data and try to use timeline to relate to the incomplete data provided.
- Based on the info, Root Cause/Corrective Action can begin.

## Issue Status

Awaiting additional information from the customer to begin RCA. I think due to the disconnected fuel cell smoldering in the video it would make sense to receive this back as an RMA. We can perform some verifications to see if its still flight worthy, (if the customer does not want to pursue a return yet, I could potentially advise on an in field test to assess damage.

## Comments (12)

### Michael Mohr, 2025-10-31

@Sean Wendling Can you weigh in on the fuel cell for this also please?

### David Grosher, 2025-10-31

@Eric Brewer can you look into the Mag portion of this issue?

### Greg Fryer, 2025-10-31

@Tom Westrich @Christopher Ridgard Tagging just for awareness on this “fuel cell smoking” issue. Sean W got tagged already.

### Eric Brewer, 2025-10-31

@David Grosher there is a pretty significant disturbance in the mag readings right when the vtol system spools up.  The attitude estimate on vtol becomes inaccurate leading to the abort.  Close to touchdown the mag readings ramp up even further before the magnetometer is (correctly) declared failed.  

[embedded: image-20251017-150806.png]
I double-checked the SCO logs when this bird went out and the mag readings look clean.  I’d be curious about the following:
1. When the vehicle is powered back on, do the mag readings now look normal?
2. Could there have been an electrical issue? Either with the VTOL system or potentially the E140 ground loop issue?  Does the ground loop issue affect the vtol mag? I thought it was typically limited to the fixed-wing mag.  The throttles have already ramped up to 75% or so before the mag magnitude increases.

I would have thought potentially an environmental issue (i.e. mag disturbance on the runway) but this doesn’t really track since the disturbance follows the vehicle up 100'.

### Eric Brewer, 2025-10-31

@Michael Mohr probably worth asking the customer about item 1 above.  Have them power up on the ground and then send us an AAR.  

Let’s get some answers internally about the E140 ground loop before we reach out about that.

### Sean Wendling, 2025-10-31

@Michael Mohr , did they let the Fuel Cell cooldown normally before removing it from the airframe?

### Michael Mohr, 2025-10-31

@Sean Wendling They did. I informed them that it was likely adhesives burning in but to give the fuel cell and fuselage a once over just to be sure.

### Sean Wendling, 2025-11-03

@Michael Mohr Okay, I am just asking as the video they sent shows the fuel cell actively smoldering while being unplugged from the vehicle. 
Normal cooldown would bring internal temperatures below 150°C, and the adhesives on the fuel cell will not melt or smolder at that temperature (RTV is tolerant to 315°C). Are we 100% confident that this fuel cell went through normal cooldown? Do they have any additional AARs from after the flight was aborted?

### Michael Mohr, 2025-11-04

@Sean Wendling from customer today: “I believe we let the fuel cell go through its normal cool down after the aborted landing but I cant be sure.  We notice the smoke after we brough the aircraft it into the storage trailer after we disassemble the aircraft outdoors.
 Is there an issue if we didn’t let the fuel cell run its normal cool down?  Should we do a ground run with this fuel cell?”

### Michael Mohr, 2025-12-16

@Sean Wendling Can you provide the field test? I will ask them to perform and report back their findings.

### Michael Lindsay, 2026-09-28

@Alexander Alan Arnold This is an old ticket, this was the fuel cell in 820, as it has been RMA and repaired can we close this ticket.

### Alexander Alan Arnold, 2026-09-29

fuel cell RMAd after failing to charge HLB during flight

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Fuel Cell Pic 1.png | image | 244 | 2025-10-31 | listed only |
| Smoke from fuel cell.mp4 | video | 1095 | 2025-10-31 | listed only |
| T95_V593_251015_164320_pack.zip | archive | 1190 | 2025-10-31 | listed only |
| image-20251017-150806.png | image | 116 | 2025-10-31 | listed only |
