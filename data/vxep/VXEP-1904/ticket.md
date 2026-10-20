# VXEP-1904: VXE 896 Failure to land PLZ

- **Issue type:** Incident (8D)
- **Status:** D6 - Implementing Corrective Actions
- **Priority:** Medium
- **Created:** 2026-06-04
- **Updated:** 2026-10-13
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** GS_Closed, Hardware, RCCA, Weekly-incident-tracker
- **Links:** relates to RMA-1041 (VXE-896 RMA 260615-2)
- **Customer:** USSS
- **Vehicle Tail Number:** VXE 896
- **Vehicle Configuration:** VXE 30 ADV NAV SUAV, Battery, 140MWIR
- **Root Cause:** VTOL AP WDT occurred during landing
- **Incident Type:** Near Miss
- **Severity:** 1 - Flight Critical
- **Executive Summary:** Aircraft currently in RMA awaiting VTOL AP replacement. Probable cause; Software Issue.

## Description

Statement from Operator:

Approaching the end of the third flight of the day, I (Simpson) initiated RTB as the main battery was down to 27%. 
 
The aircraft went into its landing pattern, going through IP1, IP4 and IP5 where it transitioned from fixed wing to VTOL as designed. 
 
Immediately after starting VTOL, the aircraft went back into fixed wing flight. I never received the Activate User Control window. The aircraft drifted off the designated land zone while continuing to descend. 
 
I put the aircraft into u-drive and steered it away from the water/river and back over land/golf course and once I cleared the edge of the water I activated the land immediately function. At this time the aircraft was approximately 50’ in height. 
 
The aircraft landed safely with no damage to persons or property. 
 
Just before the aircraft went back into fixed wing from VTOL the SA camera cut out and as I called out to my team that I lost the SA camera they called out that the aircraft overshot the LZ and was continuing flight. SA camera then came back on a few seconds later. 
 
At the start of the third flight, when going through the launch procedures, the aircraft was giving an error saying that it was not connected to any satellites. Avant rotated the vehicle 360 degrees, then I restarted the SAV program and we were able to proceed without errors. However throughout the launch process, I noticed that the aircraft would go in and out of being connected to satellites.
 
Timeline:
Started prelaunch process at approximately 1320.
Able to successfully launch at 1329.
RTB approximately 1525. **this is when things started to go outside of planned/anticipated procedures.
Safely landed with no damage to persons/property 1528.

## Comments (13)

### Alexander Alan Arnold, 2026-06-04

[embedded: image-20260604-202232.png]
The debug aligns with operator statement of issues during recovery Lift system fault in debug after start of transition

### Alexander Alan Arnold, 2026-06-04

I believe the aircraft is up to date, but the GCS software seems to be on 6.5.1

### Alexander Alan Arnold, 2026-06-05

Based on a conversation with Cody S, he stated there was a WD reset when the AV attempted to transition. customer also reported a lot of spotty connection with Novatel on ground, Eric i know you worked with 909/910 and was wondering if you could pick and see if anything is relevant or similar to those two.  @Eric Brewer

### Eric Brewer, 2026-06-05

@Alexander Alan Arnold yea it looks like there was a watchdog reset on the VTOL processor - these are quite rare.  I believe this bird should likely be RMA’d - @David Grosher agreed?  

WDT shows line 623 of datalog.c, which doesn’t seem to make sense.  @Scott Hunter @Scott Whitney FYI.


[embedded: image-20260605-151503.png]

### David Grosher, 2026-06-05

@Eric Brewer @Alexander Alan Arnold This bird should be RMA’d. The VTOL should be replaced.

### Alexander Alan Arnold, 2026-06-05

Understood, thanks for the heads up. Ill reach out to customer@Eric Brewer @David Grosher

### Alexander Alan Arnold, 2026-07-29

@David Grosher @Eric Brewer What exactly should be replaced on this aircraft so the RMA team can get it into the production que? @Drew Hildreth

### Eric Brewer, 2026-07-29

@Alexander Alan Arnold I would replace the VTOL board.  @David Grosher please weigh in if anything else needs a look.

### Pat Wells, 2026-08-11

@Alexander Alan Arnold was the correction for this to replace VTOL board?  Has it been started. 
Should this be linked to the larger effort to address xcomm resets?

### Mathew Papaleo, 2026-08-24

@Pat Wells we have requested the avionics board assembly(107-101161). doing so will allow for a smoother remove and replace operation. otherwise just replacing the red ap on the stack will have additional testing and firmware. ill post again here when r&r is finished.

### Pat Wells, 2026-08-24

@Mathew Papaleo thanks

### Alexander Alan Arnold, 2026-10-13

@Jeremy Kostel @Eric Brewer since we are replacing the board is that the appropriate corrective action or is there somehting else we should add to the CA to get this ticket moved along. The aircraft did not crash we had the aircraft RMAd before an incident occured

### Eric Brewer, 2026-10-13

@Alexander Alan Arnold @Jeremy Kostel the only issue I saw with it was the watchdog, so I think after the vtol board is replaced it can proceed back through production/sco checkouts and should be good to go if it passes those.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T115_V896_260531_133046_pack.zip | archive | 2820 | 2026-06-04 | listed only |
| image-20260604-202232.png | image | 21 | 2026-06-04 | listed only |
| image-20260605-151503.png | image | 18 | 2026-06-05 | listed only |
