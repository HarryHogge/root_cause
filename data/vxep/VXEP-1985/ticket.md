# VXEP-1985: VXE 918 lost comms did not execute LOS COMMS Logic

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2026-08-25
- **Updated:** 2026-09-02
- **Resolved:** 2026-09-02
- **Reporter:** Jackson Riley Curvin
- **Assignee:** David Grosher
- **Creator:** Jackson Riley Curvin
- **Labels:** RCCA, Weekly-incident-tracker
- **Customer:** Precision
- **Vehicle Tail Number:** VXE 918
- **Vehicle Configuration:** ADV NAV ,main battery ,Clarity payload. OGCS 1.4.2 e95
- **Problem Type:** Discovered Issue
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround
- **Components (EA Aircraft):** Aircraft, full assembly

## Description

Today we were flying AC 918 Adv Nav in support of the CHAOS dev team. During flight we went lost comms for about 8 mins. When we regained comms instead of finding the AC in our LC flight plan, it was still flying the CHAOS mission. After landing and reviewing CHAOS logs it was determined that CHAOS released control back to OGCS due to the loss of comms after 100 seconds, at which point OGCS handed control back to CHAOS unrequested. This went back and forth several times preventing the OGCS lost comms plan from even nitiating. If this is the case there is no way to recover from loss of comms aside from the low battery RTB feature.

## Executive Summary

During CHAOS testing the aircraft lost comms for about 8 minutes and never executed lost comms mission. Probable cause is Software.

## Comments (6)

### Jackson Riley Curvin, 2026-09-02

@David Grosher have you had a chance to look at this or assign someone to it?

### David Grosher, 2026-09-02

@Ted Trowbridge Is this the same issue that you already looked into?

### Ted Trowbridge, 2026-09-02

@David Grosher yes - Justin was communicating with the CHAOS about it.  According to the logs there was a connected GCS (CHAOS or OGCS) actively in control of the vehicle at all times, the system was behaving as designed.
I believe they may have set a lost comms timer to 10min and then expected it to go lost comms after 2m.  It sounded like operator error but @Justin Peterson  may have more details.

### Justin Peterson, 2026-09-02

This was resolved by the customer to be an issue with their CUCS system (Arbitrator).  The Stalker and VSM operated exactly as designed.  @David Grosher This issue may be closed.

======

As a bit more technical detail, Arbitrator does not have filters in place to operate when multiple aircraft are on the network.  The customer turned on another aircraft while on the ground.  At the same time, they changed a frequency on the ground radio that resulted in lost communication with the aircraft. This inadvertently networked the two aircraft.  Due to the lack of filtering in Arbitrator, Arbitrator never released the aircraft and the Stalker never conducted its lost comms contingencies.  As Ted specified, a CUCS was in control of the aircraft at all times.
This customer has taken it upon themselves to update their test procedures and prioritize filtering so they may operate in a mulit-aircraft environment.  They have also prioritized testing contingencies with their software in the loop and have pulled us in to review their contingency procedures and test plans.

### David Grosher, 2026-09-02

@Jackson Riley Curvin  see above. I’m going to close this issue.

### David Grosher, 2026-09-02

Operator Error, communicated to customer outside of this thread.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V918_B30N_20260825T155313Z.zip | archive | 82354 | 2026-08-25 | listed only |
