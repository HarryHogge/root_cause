# ENG-2990: VXE 407 Error during transition for landing

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-05-01
- **Updated:** 2025-06-02
- **Resolved:** 2024-03-04
- **Reporter:** Dustin Gamble
- **Assignee:** David Grosher
- **Creator:** Dustin Gamble
- **Labels:** 8-28-Sprint, TIQUILA-Blocker
- **Links:** relates to VXEP-478 (Create HILs to support SW troubleshooting. ); relates to RMA-122 (VXE407 230519); relates to VXEP-11 (TPTR-5 VXE 407: (VTOL-AP-WD) Unexpected Behavior Seen During Vertical Landing)
- **Start date:** 2023-03-30

## Description

From Garret: Error during transition for landing.  Pop up said Emergency glide landing active.  ELZ red.  Commanded go to IP4 of ELZ while in IP2 of ELZ.  On downwind, aircraft engaged lift rotor system.  Commanded Land Immediately.  Did not get option for User Landing Control.  Aircraft taxied while descending and landed at PLZ.

Payload was a drop payload.
From my point of view I observed vehicle turn on the VTOL system, it looked like all rotors were spinning, then it looked like it aborted, dived down for airspeed, then started the emergency glide in pattern. On the downwind it transited to VTOL. It was pretty far out and I was concerned we did not have enough hybrid lift battery to come back. I requested Garret command a land immediately so it would descend and land out rather than taxi back. He sent the command but it did not take. As it was VTOL taxi-ing back I asked our crowd of guests to move out of its path because its path was directly over the people and the battery was draining. During landing the operator did not get the nudge pop up. It did land on the LZ. Motor did not shut off but we used the VTOL control cut and safe. At touch down it was about 15% HLB SOC.
The aircraft conducted two successful flight before this issue in Helendale, CA.
This aircraft is back at Edge in the engineering area, near the window/HIL area.


@Daniel Lloyd @Garret Moose @matthew.curran @Former user @John Clark @Kurt Burian

## Comments (15)

### Dustin Gamble, 2023-05-01

It looks like the VTOL controller reset during the transition and the fixed wing autopilot took over. Speculating now, the fixed wing autopilot might have kept trying to tell the VTOL to transition so when the VTOL controller woke up from its reset, the aircraft was in the down wind leg of the ELZ and VTOL took over and transited. 


VTOL event log “T95_VT407_230427_134013_vtevlog.txt”
It looks like a VTOL processor reboot between launch and landing.

[12:50:00.107 944.107] host vtol state was, is: APVTOL_TAXILZ APVTOL_FWFLIGHT
[12:50:00.110 944.111] mc alt soft on
~
[12:50:02.477 946.479] forced wd report
[12:50:02.479] ** crash restart dump **
[12:50:02.479] reset reason: 00000003 : OTHER
[12:50:02.479] nmi reason: 00000000
[12:50:02.479] crash addr: 00000000
~
[12:51:33.170 1037.171] mc proximity detected, slowing descent
[12:51:38.872 1042.872] mc close proximity detected, slowing descent

xcomm event log “T95_V407_230427_134013_xcevlog.txt”
[20:49:23.662 5603.662] ap dbg: vt lnd abort, health fail during taxi to lz

### Greg Fryer, 2023-05-03

@John Clark Hopefully you can delegate the first analysis to someone not working UAP.

### John Clark, 2023-05-04

@Dustin Gamble this is what Kurt refers to as a ‘false’ watch dog. If I understand him, it occurs when the microcontroller becomes task bound and cant kick the WD. I do see evidence of this in what looks as though it may correspond to the transition from FW to VTOL, and incidentally I see the FW AP abort the landing due to unspecified ‘health’ from VTOL. Regardless, there is an extreme laps in the log almost 60 sec that creates the spike shown here in Task Hits and Func Hits that I believe might have something to do with the WD not getting kicked and expiring.
As soon as that spike hits (time drop out) hostState changes from APVTOL_TAXILZ to APVTOL_FWFLIGHT. 

[embedded: image-20230504-223458.png]
Snapshot of CPU over the period…
[embedded: image-20230504-230445.png]

### matthew.curran, 2023-05-08

This is being factored into the airworthiness of VXE and I am being asked to report more on it.  Can we get some report on what it got hung up doing, why controls for manual mode were not available, and the likelihood of occurrence.   
It is probably not related, but this was a drop payload mission.

### matthew.curran, 2023-05-15

Our customer is now tracking this as an issue effecting the safety of Stalker.  Please escalate and help us understand what happened, why, and likelihood of occurrence.

### matthew.curran, 2023-05-16

Ping

### matthew.curran, 2023-05-18

Do we know if the xcomm board or vtol AP was hung?

### Greg Fryer, 2023-05-19

@Cameron Chapman Talked with Dave as well, let’s talk about if we can shake someone loose to try and replicate this.

### Cameron Chapman, 2023-05-21

Sounds good. @Hayden Jeanor can you please investigate this tomorrow. Ideas for troubleshooting: 
- Check in with Dave, as he has been doing the recent data review for this.
- Check if 12V aux still has power.
- Reset VTOL AP using reset button. See if rebooting the board creates the same cycling behavior as seen in the plots.
- Also see if 12V aux disables when VTOL AP is reset.

### matthew.curran, 2023-06-26

It’s been a month since the last status, and it’s currently not assigned. We are trying to get this airframe released back to us.

### Cameron Chapman, 2023-06-26

Thanks Matt for checking in. @David Grosher and @Hayden Jeanor have been troubleshooting this one. Can you guys please provide an update here?

### Cameron Chapman, 2023-06-26

Also adding @Pat Wells , our new director of global support. He is new and will have a lot to catch up on, but will be in charge of customer support, mishap tracking and resolution, and many similar tasks. He should be the best contact for status and priority requests in the future.

### Sam Miller, 2023-07-10

@David Grosher and @Hayden Jeanor , this is another PTR severity 1 being tracked by the TIQUILA customer. Please provide me with an ECD for closure ASAP.

### Hayden Jeanor, 2023-07-20

@matthew.curran , apologies for the delayed response. Although this ticket hasn't been updated recently, I want to assure you that we have been actively working on the investigation over the past month. Let me provide you with a concise summary of our findings so far:
During the VTOL transition, the red VTOL AP encountered an issue where it became hung up. Typically, this would trigger a hardware reset of the AP microcontroller through the WD (watchdog) mechanism. However, Gordon implemented a condition in the code to prevent this reset if the aircraft detected that it was in flight. As a result, the VTOL AP remained stuck in its current state, possibly due to an infinite loop, deadlock, or waiting for an external peripheral to respond.
While the VTOL AP was stuck, the fixed wing AP took over for approximately 50 seconds until, somehow, the VTOL AP managed to exit its hung-up state. We're still unsure about the exact cause of the microcontroller getting stuck or how it resolved itself. However, we do have a crash restart dump that allows us to trace the function call stack back to the specific function running during the incident (although we can't confirm if the stack dump was captured during the incident itself). The function at the top of the stack during the "crash" was the one responsible for writing to the event log.
Given that the suspected problematic function involves reading and writing from the microSD card on the VTOL AP, we are currently conducting hardware and software investigations in this specific area. On the software side, we are exploring potential scenarios that could have caused the observed behavior during the incident. We are running test cases on the functions suspected to be buggy and closely monitoring their responses to determine if we can replicate the same issue. Since the problem is intermittent, it's challenging to investigate the hardware, but we're still working on identifying any potential hardware non-conformities.
Based on the information we have, we are now more confident in narrowing down the problem to the red VTOL AP board. That being said, we would prefer to have more time with the entire system for troubleshooting which could take a couple more months to hopefully determine a concrete root cause. However if it's time-sensitive for LM, we can replace the VTOL AP board and send the vehicle back for RMA through the system checkout process ASAP. Please let us know your preference. Thanks!

### Cameron Chapman, 2023-08-24

Linking subtasks to parent.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V407_230427_134013_pack.zip | archive | 2553 | 2023-05-01 | listed only |
| image-20230504-223458.png | image | 31 | 2023-05-04 | listed only |
| image-20230504-230445.png | image | 23 | 2023-05-04 | listed only |
