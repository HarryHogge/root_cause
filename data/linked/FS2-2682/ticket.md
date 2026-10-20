# FS2-2682: VXEP-546 Test Case

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-01-06
- **Updated:** 2025-02-06
- **Resolved:** 2025-02-06
- **Reporter:** Scott Whitney
- **Assignee:** Brandon Slater
- **Creator:** Scott Whitney
- **Parent:** FS2-2342 VXEP-512 - Investigation and GCS CAs for Transition to VTOL above 2000ft
- **Links:** relates to VXEP-546 (VXE 470 transitioned to VTOL at 2400 AGL then crashed); relates to FS2-2736 (VXEP-546 Launch speedgoat from elevation >50ft from SLO Office)
- **Epic Link:** FS2-2342
- **Sprint:** FS2 Sprint 28, FS2 Sprint 29

## Description

The PMA-263 customer has come back with some questions regarding the advisory notice we released for this issue. If possible could you please assist in answering the below questions?
What happens during Mobile operations? If an Operator has selected Mobile Mount antennas and has chase GCS on for example? 
Can we still perform Handoffs?  It has been awhile but if handing off to another GCS with a different antenna location that may be +/- 50 ft would this cause issues?

## Comments (8)

### Brandon Slater, 2025-01-06

@Scott Whitney after going through these questions I think they can only be tested from a flight test and not HIL? Chase mode needs a camera and something to follow and the second question looks like it requires two GCS 50ft apart during flight for handoff 

@Artis Bertulis @Ruysser Gabler adding for your awareness if you may know about these

### Artis Bertulis, 2025-01-06

Chase GCS requires the GCS location uplinked to the vehicle. Haven’t tested this, but I’d assume that upon loss of link, it would remain in the last commanded waypoint until the LOS timer is executed (2 min by default).

Handing it off depends on what antenna is used, if SGCS1 is within its range, it wouldn’t care about the vehicle location, for SGCS2 if it’s anywhere within its 120-degree field of view within that range it’ll catch it. For SGCS3 you’d have to point it at the right direction, the further the antenna from the vehicle the more accurate the positioning should be. @Brandon Slater

### Brandon Slater, 2025-01-06

@Scott Whitney We could attempt the handoff using HIL flight using 3 radios and two GCS that are 50ft apart though I’m not sure if this would be accurate enough to answer the question. Let me know if we should proceed with this test we’d need two more radios and an IPComm from production

### Scott Whitney, 2025-01-08

@Ben Triplett can you and @Brandon Slater test this on SpeedGoat.

### Brandon Slater, 2025-01-15

Using speed goat, chase mode feature is broken. Why active it only tracks the last active waypoint

### Brandon Slater, 2025-01-15

@Scott Whitney  do you know if the vehicle needs to be in flight for this one:
Can we still perform Handoffs?  It has been awhile but if handing off to another GCS with a different antenna location that may be +/- 50 ft would this cause issues? 

If not I think I can use a vehicle and have two GCS’s 50 ft apart and do handoff

### Brandon Slater, 2025-01-15

@Scott Whitney handoff >50ft works with SGCS1

### Brandon Slater, 2025-02-06

@Ryan Smith closed this one out when I was out sick

## Attachments (0)
