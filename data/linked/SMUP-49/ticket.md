# SMUP-49: Determine if behavior for landing with no GPS is accurate in the Manual.

- **Issue type:** Task
- **Status:** New
- **Priority:** Low
- **Created:** 2024-12-10
- **Updated:** 2025-10-06
- **Reporter:** David Grosher
- **Assignee:** Mark Spence
- **Creator:** David Grosher
- **Links:** relates to VXEP-451 (VXE 523 landing anomaly, vehicle landed 300m from PLZ); relates to FS2-3016 (Document results from landing with no GPS)

## Comments (3)

### Josh Burrell, 2025-02-20

@Dana Holley sending this your way for the OPS.

### Dana Holley, 2025-02-20

@Josh Burrell @David Grosher Fairly certain there is no information in the manual that states that the aircraft will land in it’s current location if a GPS failure is encountered in the landing pattern. I assumed it would just continue its approach path since the INS should still be accurate. I’ll write something up, but I need some more information. 
- Where in the landing pattern will it execute a VTOL landing? 
- Example - is it from IP4- IP5? IP1 seems like it would be too high in altitude.
- The aircraft typically states it has “entered the landing pattern” if a Go To command is given and could be considered part of the landing pattern although aircraft may be a few km’s away from landing pattern location.
- Does the aircraft autonomously command a Land Immediately! or similar action as it the AV has to go through its transition period?

### David Grosher, 2025-02-20

@Scott Whitney Can you have SQA do the testing below and document the results.

## Attachments (0)
