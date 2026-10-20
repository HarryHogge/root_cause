# VXEP-1687: VXE-533 Failed to transition to fixed wing flight

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2026-01-30
- **Updated:** 2026-05-05
- **Resolved:** 2026-05-05
- **Reporter:** Michael Mohr
- **Assignee:** David Grosher
- **Creator:** Michael Mohr
- **Labels:** RCCA, Rangers
- **Links:** relates to XKIT-5360 (B40 913 Crash (2026/03/04)); relates to RMA-944 (VXE-533 RMA 260312-3)
- **Customer:** 75TH_RANGERS
- **Vehicle Tail Number:** VXE-533
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

“We were training at Lee DZ on Fort Benning to test our Tracking Antenna for an upcoming training event. Since we were merely testing the antenna, no payload was attached. Preflight checks for the A/C and GCS were normal. Upon launching the A/C, its vertical takeoff was routine. However, during the transition to fixed-wing flight, it appeared that the A/C ceased function to the forward propeller and tumbled to the ground from the transition height with little to no forward momentum. The A/C sustained significant damage.”
Only a long rang kit (GCS3) was being used during launch
Additional comments from customer:
- Attachments: There was an empty hood scoop attached to the aircraft, but no other payload.
- Weight and Balance: We weighed the aircraft and tested the CG prior to the flight; both were within tolerance.
- Front Propeller: The front propeller appeared to attempt to engage but immediately failed. This caused the aircraft to nose-dive and flip as it fell.

## Vehicle Configuration

Standard VXE-30
Battery configuration
No payload

## Plan

- Hardware inspection.
- Specifically servo operation and returns to zero, fwd motor operation, power connections to nose.
- @Eric Brewer would you be able to tell a vehicle imbalance based on VTOL current due to imbalance? Reported in balance specs in comments below. Seems to be some evidence of yes “the front VTOL props were holding a good bit of weight (63 and 84% for RF/LF) just before they were turned off”
- Organize data review and test results into investigation summary?

## Issue Status

https://jenaero.sharepoint.com/:p:/r/sites/FlightSafety/_layouts/15/Doc.aspx?sourcedoc=%7B054AF97D-3410-4B98-92E2-2F0A7AC65317%7D&file=VXE937Crash_VXEP1775.pptx&action=edit&mobileredirect=true
Report complete.

## Comments (33)

### David Grosher, 2026-01-30

@Eric Brewer Can you take a look at this? It looked like both APs walked through transition as expected.

### Eric Brewer, 2026-02-02

@David Grosher it looks to me like an issue with pitch control - the front VTOL props were holding a good bit of weight (63 and 84% for RF/LF) just before they were turned off.  As soon as the front props were turned off the vehicle went into a nose dive.  The front prop was still drawing current, and lack of front prop thrust wouldn’t explain that dramatic of a nose dive.  It may be hard to tell since the vehicle is now damaged but I’d inspect things like CG within tolerance, elevator functioning as expected, any structural issues etc.

### Eric Brewer, 2026-02-02

[embedded: image-20260202-141247.png]

### David Grosher, 2026-02-02

@Michael Mohr Can you have the AV returned for inspection? And can you follow up with the operators regarding CG configuration?

### Jeremy White, 2026-02-05

@David Grosher @Michael Mohr From USASOC G8 (PM for USASOC UAS)

After our Monthly Update the other day, I got some feedback from 3-75 on the damaged VXE-30 TN# 533. It appears 3-75 sent flight logs to the Global Support Team who responded:  “The VXE30 gave CG Errors during transition.”.  Looking for thoughts on the way forward to the incident/repair – assuming RMA through SOFSA for a full assessment of the aircraft and flight log analysis?

Below are the 5-W’s for the incident:
WHO:  3/75 UMS Section
WHAT:  Stalker Air Vehicle (AV) VXE30 crash; TN# 533
WHEN:  26JAN2026
WHERE: LEE DZ - Fort Benning, GA

WHY:   Unknown; unit assessment is a main battery failure during transition. Prior to launch 3-75 operators confirmed the HLB (Hybrid Lift Battery) was fully charged, and main battery was Half Full. In addition, operators ensured CG (Center of Gravity) and weight was within tolerance. Operator intent was to do a quick launch and land to confirm everything was working properly.
 
Unit confirms mission planning was sufficient for the VXE SUAV Program. Incident: during launch the Stalker AV gained altitude to transition altitude at 300 feet AGL; then the system began transitioning into fixed wing flight. At that point, the Stalker AV lost power to the forward prop causing the aircraft to tilt downwards and lose lift. This caused the Stalker AV to begin an uncontrollable spiral downward to the ground.
 
Initial Damage Assessment: Lift booms, tail boom, main body, main motor, HLB, main battery. 3-75 assess the center wing is still usable, however they have not conducted any testing of that wing since the incident.

### Alexander Alan Arnold, 2026-02-12

@Eric Brewer Is it possible a bad pitot cal could've created this issue?

### Eric Brewer, 2026-02-12

@Alexander Alan Arnold it would be plausible that the vehicle would nose down if it were going really slow after the transition.  The groundspeed was 46fps which I think is pretty low, but unclear if low enough to cause this type of dramatic pitch down.  Do we have reports of the local wind during the takeoff?

### Alexander Alan Arnold, 2026-02-12

@Eric Brewer We do not have local wind reports do you want me to try and find a previous mishap where bad cal was indentifeid as the root cause to compare it to?

### Eric Brewer, 2026-02-12

@Alexander Alan Arnold In this case it has an airspeed reading on the ground and the bias between airspeed and groundspeed stays pretty consistent up until the transition.  To me this makes an airspeed cal issue unlikely - it’s more likely there was a 10 fps wind present and some other issue.  The airspeed cal issues we had typically resulted in overspeed (if the pitot was pushed or not shielded and we got some non-zero wind captured as a ‘zero’ value).
[embedded: image-20260212-154907.png]

### Alexander Alan Arnold, 2026-02-12

@Eric Brewer I know they were using only and SGCS 3 for connectivity is it possible that during the transition, the aircraft lost link coinciding with the transition phase and wanted to abort the launch, but FW was already taking control? Just trying to eliminate some of the ideas in my head, I can reach out to them when they aren't busy to try and get more information, we are currently waiting on the equipment to be returned?

### Eric Brewer, 2026-02-12

@Alexander Alan Arnold I don’t see any evidence of this in the logs.  The state machines both transitioned normally, it just nosedived once the vtol motors shut off - but both fixed-wing and vtol thought it should be flying in fixed-wing mode at that time and there were no indications of lost link.

### Alexander Alan Arnold, 2026-02-12

@Eric Brewer Thank you for the info and for entertaining the ideas.

### David Grosher, 2026-02-24

@Scott Lovett @Michael Mohr @Alexander Alan Arnold From our perspective this incident is on hold while we wait for the equipment.

### Alexander Alan Arnold, 2026-02-24

@David Grosher copy ty, reaching out to customer again to see what the holdup is. I Believe there is a third party making this slower.

### Cody Smisek, 2026-03-06

@Cameron Chapman potential for servo inspection

### David Grosher, 2026-03-17

@Greg Fryer This AV was received. We will need electrical and mechanical help to inspect the elevator servo, CG alignment (if possible), air data, And any structural issue (if possible given the crash)

### Greg Fryer, 2026-03-17

@David Grosher I asked Nigel to collect it and assign someone to do a first review, probably Sammy if he’s not lost to the other LRR things.

### Lauren Velasquez, 2026-04-16

@Samuel Lopez

### Samuel Lopez, 2026-04-20

First Observation by Sammy Lopez
- After connecting the center wing to the fuselage, the AC powers on normally and I can connect to the XCOMM and VTOL webpages.
- I am able to induce the forward motor to propel normally using the Motor Test webpage.
- This is true for 15 fps, 30 fps, and 55 fps.
- Not immediately able to reproduce the error.

### Eric Brewer, 2026-04-22

@Samuel Lopez Can you check the elevator function? Did it go hard over or is it trimmed as it should be? Does it respond normally during surface checks?

### Jackson Riley Curvin, 2026-04-27

@Samuel Lopez @Eric Brewer  if we are unable to reproduce the error what are the next steps?

### Eric Brewer, 2026-04-27

@Jackson Riley Curvin @Samuel Lopez I recommend checking elevator function as requested below.

### Jackson Riley Curvin, 2026-04-27

@Eric Brewer  thanks I see that now @Samuel Lopez have you had a chance to do this?

### Samuel Lopez, 2026-04-27

@Jackson Riley Curvin  and @Eric Brewer 

Last week, I set up the AC and rotated the fuselage.  This induced both the vertical and horizontal tails on the elevator.

### Eric Brewer, 2026-04-27

@Samuel Lopez @Jackson Riley Curvin thanks Sammy.  I’m not able to tell from your response exactly what test was run and what you observed.  Can you clarify?

### Samuel Lopez, 2026-04-27

@Eric Brewer @Jackson Riley Curvin 

I connected the vertical and horizontal tails and then picked up the fuselage and moved it around.  This induced both tails to move.  The test was to confirm is the signal/power is getting from the battery to the elevator.  If you have an additional idea I’m all ears as I’m a bit at a loss at the moment.  

I’m looking through the logs trying to figure out what commands are elevator related and which columns are relevant to our investigation.

### Eric Brewer, 2026-04-27

@Samuel Lopez thanks. Check if the elevator is ‘trimmed’ - i.e. should match the black line on the vertical surface.  Also check for any grinding or off-nominal sounds when the elevator moves.


[embedded: image-20260427-184702.png]

### Samuel Lopez, 2026-04-29

@Eric Brewer and @Jackson Riley Curvin 

To be clear, the boom is completely broken.  I borrowed the boom from 797 and attached the two tails from VXE 533.  They do respond to fuselage/centerwing movement.  I then swapped out the 533 tail for the 797 tail and subjected the fuselage to the same movement and it responded similarly.

### Eric Brewer, 2026-04-29

@Samuel Lopez thanks. Do we have access to the old servo that was in the tail from 533? There is an issue we had with some servos and we can inspect to see if it impacts this one.  Reach out via IM and we can chat on it.

### Samuel Lopez, 2026-04-30

@Eric Brewer  we checked the line with Robert M and it was fine.

### Samuel Lopez, 2026-04-30

@Eric Brewer  and @Jackson Riley Curvin 

By sight, there is nothing wrong with the horizontal tail of VXE-533.  I also compared to the borrowed horizontal tail of 797 and the two looked identical.  However, I will note that is did seem a bit ‘sluggish’ when prompted with the LaunchWizard.  This may just be the way that the horizontal tail operates.
[embedded: IMG_5779.MOV]
[embedded: IMG_5780.mov]

### Eric Brewer, 2026-05-05

Investigation concluded.  Root cause cannot be determined due to aircraft damage on crash.

### Eric Brewer, 2026-05-05

@Samuel Lopez @Michael Mohr @David Grosher @Alexander Alan Arnold @Jackson Riley Curvin completed report linked above.  I’m marking this as ‘bermuda triangle’ as we cannot determine root cause.  Mostly likely explanation is servo out of trim or failure, but we cannot determine definitively.

## Attachments (14)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V533_260127_175657_01_pack.zip | archive | 2104 | 2026-01-30 | listed only |
| image-20260202-141247.png | image | 183 | 2026-02-02 | listed only |
| IMG_4082.jpeg | image | 4090 | 2026-02-04 | listed only |
| IMG_4083.jpeg | image | 3063 | 2026-02-04 | listed only |
| IMG_4084.jpeg | image | 4125 | 2026-02-04 | listed only |
| IMG_4085.jpeg | image | 2623 | 2026-02-04 | listed only |
| IMG_4086.jpeg | image | 2772 | 2026-02-04 | listed only |
| IMG_4087.jpeg | image | 1739 | 2026-02-04 | listed only |
| IMG_4088.jpeg | image | 3769 | 2026-02-04 | listed only |
| IMG_4089.jpeg | image | 2463 | 2026-02-04 | listed only |
| image-20260212-154907.png | image | 130 | 2026-02-12 | listed only |
| image-20260427-184702.png | image | 244 | 2026-04-27 | listed only |
| IMG_5779.MOV | video | 8882 | 2026-04-30 | listed only |
| IMG_5780.mov | video | 3418 | 2026-04-30 | listed only |
