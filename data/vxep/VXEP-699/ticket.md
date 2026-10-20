# VXEP-699: 101-115866-01, VXE30 Std Config, Wing Utility "Pylon" - Production Docs

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2024-10-02
- **Updated:** 2024-11-21
- **Resolved:** 2024-11-21
- **Due:** 2024-10-16
- **Reporter:** Matt Philley
- **Assignee:** Brendan Palmer
- **Creator:** Matt Philley
- **Labels:** Gen1-Utility-Dropper
- **Parent:** VXEP-696 Practice Build - 101-115866-01, VXE30 Std Config, Wing Utility "Pylon"
- **Epic Link:** VXEP-696
- **Start date:** 2024-10-03

## Comments (3)

### Matt Philley, 2024-10-03

@Brendan Palmer @Nina Menon Jira for utility dropper production feedback

### Brendan Palmer, 2024-10-03

@Matt Philley update on progress from the Final Assembly (F.A.) practice build today (10/3/24):
First round of redlines on master drawing were done and handed off to @Scott Stuckey.
Servo processing will be done in Electronics (unprocessed servo PN: 100-113576) where they will handle wire cut lengths and terminations. This will end up as a sub-assembly we produce in-house. @Nina Menon @Luca Lauritzen 
Servo programming will be done in one-shot given limited production volume on this iteration of the dropper. 17 PCBs = 34 (2 per PCB) + 4 (spares). These 38 servos will be marked and segregated from the 600+ unprogrammed servos once they pass through receiving inspection. This will leave the F.A. technicians to use existing hardware to set the PWM of the servo during mechanical assembly. Programmed dropper servo PN: 2118851-01. I will coordinate with Geoffrey to find a good time to knock these out.  Servo programming will be performed by F.A. during the mechanical build process. A harness will need to be produced to connect servos to a computer for programming. This should be combined with a servo setter so the build tech can set the servo to the required PWM for the build process while it’s already connected to power
Mechanical assembly will be handled in Final Assembly as a single build process. The only new tooling required is a dedicated press for this process, with a custom insert that S. Stuckey is willing to provide. The purchase request for this press was placed 10/3/24). F.A. has adequate tooling on hand for the remainder of the build process. Engineering provided the remaining 3D printed jigs required. 
There are 4 potential sub-assemblies that are can reasonably be purchased from vendors (these are machined parts that need bearings and/or pins press fit):
- Under load latch, striker (PN: 101-114378-01) with 1x bearing (PN: 100-114327-01).
- Under load latch, catch (PN: 101-114378-02) with 2x bearing (PN: 100-114327-01) and 1x pin (PN: 100-114934-51).
- High tech servo, driver with sense (PN: 101-117064-01) and 1x pin (PN: 100-114934-28).
- Utility latch catch (PN: 101-117229-01) - I believe this is already a sub-assembly we are already ordering with 2x pins (PN:?) inserted.

Critical dimensions of these parts have yet to be determined but, will be so Quality can screen parts purchased from vendors during receiving. 
We have the tooling / jigs required to produce these during the F.A. mechanical assembly if required in the interim. S. Stuckey mentioned that we could provide vendors with the 3D printed jig designs that Engineering currently uses to produce these sub-assemblies.
The following is a list of documentation that is in-progress (for my visibility as much as yours):
- Traveler 
- Inspection points TBD.
- Functional test required.
- F.A. Work instructions / build procedure
- F.A. Servo Programming procedure
- F.A. Kit List
- Semi-related: identification of the screw that is supplied with each servo, for when it inevitably gets lost.
- Transit case (traveler, work instructions, placard, & labels)
- Operation manual has not been written.
- “See web manual” message will be included on the placard or a separate placard.

### Matt Philley, 2024-11-21

marked complete based on notes in ppt

## Attachments (0)
