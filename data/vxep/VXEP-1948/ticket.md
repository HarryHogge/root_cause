# VXEP-1948: VXE 886 two seperate fuel cells failed to produce 450 watts in flight

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2026-06-26
- **Updated:** 2026-10-08
- **Resolved:** 2026-10-08
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Charles Sweet
- **Creator:** Alexander Alan Arnold
- **Labels:** Hardware, RCCA, Weekly-incident-tracker
- **Links:** relates to VXEP-1396 (VXE 674 Fuel cell D4599988 running hot); relates to RMA-1059 (D4599988 RMA 260708-4)
- **Customer:** Redwire
- **Vehicle Tail Number:** VXE 886
- **Vehicle Configuration:** VXE 30 ADV NAV w OGCS, SOFC 450w, E140g2z
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Fuel cell 508 shutoff in flight after saying it was over temp, next flight failed to produce 450 watts in flight 
Fuel Cell 998 performed as expected one flight, the next cycle it failed to produce 450 watts in flight 
I have added both flights where the issue occurred. On Monday we will collect more data if needed


Fuel 508 failure resulted in immediate recovery after transition to fix wing
Fuel Cell 988 resulted in RTB due to difficulty maintaining charge of HLB

## Corrective Action

Heat exchanger production process is being updated. The assembly order of the heat exchanger is being re-written to accommodate the assembly of the flame extender happening at the first step, where it is more open and accessible to allow the use of laser welding on this particular seal as it is a stronger, more repeatable, more robust method of attaching the flame extender than resistance tack welding - ensuring weld integrity and thus resistance to vibration or warp induced repositioning that has been previously been the root cause of stacks shorting. New training, tooling, and fixturing has been created to rewrite this assembly process.

## Root Cause

508 suffered a sudden internal short. The weld between the chimney and heat exchanger failed, either from vibration on a poor weld or warping of the bottom plate severing the weld. Molten silver present on the chimney confirms contact here causing the short and conversely the temperature spike causing the fault. Evidence is also present on the end zal with damage caused during removal due to flame extender not being parallel to the stack.

## Executive Summary

Fuel Cells expereinced a heat exhanger failure resulting in updates to assembly and production procedure moving from tack welding to laser welding

## Comments (14)

### Sean Wendling, 2026-06-29

Hey @Charles Sweet , see me tomorrow so we can talk through evaluating this issue.  
Thank you @Alexander Alan Arnold for sending this our way. If you do get more information such as an operator statement or any information about the conditions leading up to the failures that would help, but this should be enough for us to get started.

### Jackson Riley Curvin, 2026-06-30

@Sean Wendling  I was the operator for both of these aircraft.  We were using OGCS 1.4.1.
508:  We powered on the fuel cell roughly 30 minutes before launch temp was normal according to OGCS. Once it reached operating temp we launched after transition and was established in the loiter I noticed that the temp of the fuel cell was in the red and the fuel cell shut off and the aircraft was auto RTB.
One the next flight everything appeared normal once established in loiter the fuel cell was only producing roughly 417 watts I believe and constantly in a 1w deficit taking over an hour to charge the battery to 100 percent.

998:  everything looked normal on ground. Once we launched and established in our loiter were only generating 408 watts I believe, and constantly in a 1w deficit for the entire flight the fuel cell would charge the HLB but it was very slow. it took us roughly 30-40 minutes at the same altitude to get the HLB charged in order to climb.

### Charles Sweet, 2026-07-02

@Alexander Alan Arnold Hello, I’m attempting to look through each file, however, the fuel cell serial number is listed as 508 in both. Do you have the logs for 998? Thank you.

### Alexander Alan Arnold, 2026-07-02

@Charles Sweet should have the 998 flight now as well.

### Charles Sweet, 2026-07-06

@Jackson Riley Curvin These each appear to be fuel cell related issues, could you please coordinate with @Lauren Velasquez to prepare an RMA so we can investigate further?

### Jackson Riley Curvin, 2026-07-06

@Charles Sweet I have our asset manager working on the RMA now

### Charles Sweet, 2026-08-18

@Alexander Alan Arnold 508 suffered a sudden internal short. The weld between the chimney and heat exchanger failed, either from vibration on a poor weld or warping of the bottom plate severing the weld. Molten silver present on the chimney confirms contact here causing the short and conversely the temperature spike causing the fault. 988 is more difficult to tell without a detailed story of the stack's lifetime, cell degradation across the board is evident but the cause of it happening is so few cycles is unable to be determined - early cell failure.
[embedded: image-20260818-160056.png]
[embedded: image-20260818-160041.png]
[embedded: image-20260818-160023.png]

### Alexander Alan Arnold, 2026-08-25

Is this going to be apart of a larger investigation into stack relaibility/imporvement? @Charles Sweet

### Charles Sweet, 2026-08-25

@Alexander Alan Arnold This particular weld failure has been an observed and recorded finding previously in AA. Permanent preventative corrective actions (process order, tooling and fixturing improvements, training, and weld method) have been underway for some time and hopefully fully executed in the next couple of weeks. Please let me know which direction you’d like to follow.

### Alexander Alan Arnold, 2026-08-25

@Charles Sweet internal asset no report required please update root cause field with applicable information and up CA to include what was mentioned in above comment. ticket should then be moved into D6

### Alexander Alan Arnold, 2026-10-08

@Charles Sweet Do you know if the discussed CA has been implemented into production?

### Charles Sweet, 2026-10-08

@Alexander Alan Arnold The updated process has been released for review from the MFG department. They are currently waiting on stakeholder approval and have been for some weeks. I will push on this and get back with you

### Charles Sweet, 2026-10-08

@Alexander Alan Arnold This is now fully implemented.

### Alexander Alan Arnold, 2026-10-08

item closed, corrective action implemented into production of fuel cells

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 2-OGCS-Logs-2026-06-17T06_41_09.575Z.zip | archive | 54075 | 2026-06-26 | listed only |
| AAR_V886_B30N_20260622T004212Z.zip | archive | 20026 | 2026-07-02 | listed only |
| image-20260818-160023.png | image | 309 | 2026-08-18 | listed only |
| image-20260818-160041.png | image | 269 | 2026-08-18 | listed only |
| image-20260818-160056.png | image | 2714 | 2026-08-18 | listed only |
