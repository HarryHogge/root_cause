# VXEP-1472: LRR LEMB Chargers (Stalker 28V Battery Charger) smoking

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-08-14
- **Updated:** 2026-07-07
- **Resolved:** 2026-07-07
- **Reporter:** Michael Mohr
- **Assignee:** Tom Westrich
- **Creator:** Michael Mohr
- **Labels:** Ann_Arbor, GS_Closed, LRR, RCCA, Weekly-incident-tracker
- **Links:** relates to BAT-101 (Battery Charger software update, correcting input DCDC failure when power supply drops); relates to RMA-787 (LEMB-007 RMA 250815-2  ); relates to RMA-789 (LEMB-0024 RMA 250815-4); relates to RMA-788 (LEMB-0013  RMA 250815-3); relates to BAT-84 (LRR charger repair prior to release to customer - march LRR delivery (2025))
- **Customer:** LRR
- **Part Number(s):** 2123091-01
- **Severity:** 1 - Flight Critical

## Description

Today we had 3 LRR Chargers smoke when being plugged in. 
Charger S/N’s were: 0007, 0013, and 0024
The smoke came out of the left front side of the charger as well as the vent on the right side. There was an audible "click" noise that came just as the smoke started. All chargers were unplugged after the incident and no fires were started.  
Attached are the pictures of the Chargers/power supply/discharger for what SN's were plugged into each other. The pictured that does not have a charger was used with Charger SN 0024. 
 Some notes about conditions:
- Same power source as the other days this week
- Same power chord as the other days this week
- Same location in sun as the other days

The Humidity was much higher at 92-94% Other days were closer to 80% This seems like this likely issue but nor 100% sure

## Comments (18)

### David Grosher, 2025-08-15

@Sean Wendling @Stephen Peters @Tom Westrich This was assigned to me, but I think it should be AA.

### Tom Westrich, 2025-08-18

@Michael Mohr , I’ve also gotten this image from @Addison Osborn .  Do we have any other evidence on this ticket?  I am particularly interested in the operational details during failure here.  For example, this image shows a failure of the input power DCDC chip in the charger, which would happen if the charger was on and the AC power supply was cycling on & off, or if the power supplies were hot swapped onto chargers before they were told to stop charging.
[embedded 3bc468fe-9136-4630-b7c0-323c46191e38.jpg]
@Addison Osborn , my initial suspicion is that humidity was not a factor here, but I need more information to determine the root cause.

### Addison Osborn, 2025-08-18

@Ruysser Gabler & @Calvin Rogers - Can either of you provide circumstances around the failure of the chargers at Courtland last week since you were both present? Were the charger on and the AC power supply cycled or were the power supplies hot swapped onto chargers before they were told to stop charging.

### Michael Mohr, 2025-08-18

@Ruysser Gabler Can you add any other details for this investigation for Tom?

### Ruysser Gabler, 2025-08-18

@Tom Westrich The first charger to die was 0024, This was a student that did this and I am not 100% sure what the cause of it was, however he mentioned that plugging in the charger to the power supply, it occurred. 
The 2nd one to die, it was also a student that plugged it in (the same student) and there was no charging happening when anything was disconnected so it wouldn't have been that they did not wait long enough. However it was in the act of plugging in the charger to the power supply that it happened. 
The 3rd charger also happened in the same state and this one I did. Some steps here of what happened. 1. The charger was plugged into the power supply (that was plugged in) and the charger was not turning on. The charger was then unplugged and plugged into a different power supply and still did not turn on. Then plugged back into the original power supply and it smoked. 

Something to note as well, all 3 chargers were working before this occurred on the same day. they had been on for about 1-2 hrs. The safety breaker in the power strip did trip a few times during those first 1-2 hrs however at this point when these chargers smoked, there however was no tripping of the breaker in the 10-20 min before the magic smoke appeared

### Michael Mohr, 2025-08-18

The three chargers are on their way to Ann Arbor BTW.

### Tom Westrich, 2025-08-19

@Ruysser Gabler , did all three charger failures occur on the same charger power supply?  Was this power supply power cycled (unplugged from 110VAC) during these failures?  Was this power supply successfully used after these charger failures?

### Ruysser Gabler, 2025-08-19

@Tom Westrich This was a different power supply for each one. The pictures above link each power supply to the respective charger that failed. 
For the 1st one, no it was not unplugged. The 2nd one I cant not say for sure if it was or was not.  But the 3rd one I can confirm was unplugged before the incident occurred.

### Pat Wells, 2025-08-25

@Tom Westrich any further updates on this?
My fear is that the internal asset chargers we used to replace these may also fail during the next training event with the customer.

### Tom Westrich, 2025-09-01

Physical damage on each of the three received chargers matches a condition where the following conditions all existed:
- The battery was plugged into the charger
- The user requested that the battery is charged, thereby initiating the onboard DCDC circuitry
- The input power to the charger experienced a dropout, or loss of voltage below the battery voltage (21-29.4V)

If setup properly (as per instructions on chargers), the battery is only installed to the charger AFTER the charger is powered on by the power supply.  And once complete, or a fault occurs, or the charging is stopped, the user must remove the battery FIRST before depowering and removing charger power supply.  @Ruysser Gabler , can you confirm that this was the case for these charger failures?  If these steps are followed, then the only time that this failure might occur is if the power supply browns out during a charge cycle.
A software fix is recommended to address this potential issue.  https://jenaero.atlassian.net/browse/BAT-101

### Jackson Riley Curvin, 2025-09-02

@Pat Wells @Drew Hildreth

### Pat Wells, 2025-09-02

@Jackson Riley Curvin please check with the other instructors that were on this class.  Reference Tom’s question to Ruysser.
Ruysser is on PTO

### Tom Westrich, 2025-09-03

Operational note:@Travis Blaschke  confirmed that in at least one instance, the AC input power to a charger power supply was unplugged and plugged back in after a “FAULT” message, without first disconnecting the battery.  This is an example of improper usage that may result in the observed failures - especially if the charger was attempting to charge the battery when the “FAULT” occurred.
Corrective action: 1) Improved training and communication to the user that during a fault or disassembly, the battery must be removed before any other disassembly can take place.  Similarly, during assembly, the battery is the last item to be added. 2) Updated software (V1.2.35, as shown on the display during startup) will substantially reduce this failure mode by detecting a brownout on the power supply and operation of the internal circuitry in a fail-safe manner.  This has been tested on  chargers in AA with HLBs and LEMBs by removing power to the power supply during a charge cycle.  Resuming the charge cycle requires the battery to be removed, the power supply plugged in (powered), the battery reconnected and the charge cycle restarted.

### Jackson Riley Curvin, 2025-12-29

@Tom Westrich can we close this ticket?

### Scott Lovett, 2026-02-02

@Tom Westrich Has the team been able to analyze the broken chargers to determine the root cause?

### Scott Lovett, 2026-07-06

@Tom Westrich Is this project still active? Can this be closed?

### Tom Westrich, 2026-07-06

@Scott Lovett , we can close this issue.  Corrective actions tracked in relevant BAT jiras.

### Scott Lovett, 2026-07-07

Corrective actions tracked in relevant BAT jiras.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Image (17).jpg | image | 95 | 2025-08-14 | listed only |
| Image (18).jpg | image | 100 | 2025-08-14 | listed only |
| Image (20).jpg | image | 85 | 2025-08-14 | listed only |
| 3bc468fe-9136-4630-b7c0-323c46191e38.jpg | image | 84 | 2025-08-18 | listed only |
