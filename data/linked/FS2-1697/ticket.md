# FS2-1697: Fixed-wing helper implementation results in excessive landing overshoot.

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2024-04-05
- **Updated:** 2024-05-14
- **Resolved:** 2024-04-17
- **Reporter:** Eric Brewer
- **Assignee:** Eric Brewer
- **Creator:** Eric Brewer
- **Parent:** FS2-1862 VXEP-315 Landing Performance Improvements
- **Links:** relates to VXEP-315 (VXE 459 Overshoot of LZ Mishap on landing, operator unable to nudge)
- **Epic Link:** FS2-1862
- **Sprint:** FS2 Sprint 16, FS2 Sprint 17

## Description

Fixed-wing helper forward motor throttle command is a function of only the vehicle’s current airspeed.  This works well for a steady hover, but when the vehicle is in transition to VTOL mode it can result in incorrectly increasing throttle when the vehicle is already past the touchdown point and pointed away from it.  Logic should be added to correct this issue.  See https://jenaero.atlassian.net/browse/VXEP-315 for details.

## Comments (8)

### Eric Brewer, 2024-04-16

@David Grosher @Everett Werner @Ben Triplett please review.  Prototyping for recommended quick fix attached.  It reduces the trim angle of attack for nominal VTOL flights in wind and significantly reduces landing overshoot in the case of pitch estimation errors.  See https://jenaero.atlassian.net/browse/VXEP-315 for context of the issue.

### Ben Triplett, 2024-04-16

Looks great, I’m on board

### David Grosher, 2024-04-16

@Eric Brewer Are there other flight conditions that this change could impact that were not tested?

### Eric Brewer, 2024-04-16

@David Grosher good question.  The test case has forward flight plus steady-state at the end of the test.  The only other condition I could think of is a step forward of the vehicle (i.e. start with vehicle stationary and command it to go forward 50m).  I added test results for this case to the back of the powerpoint.  Let me know if you can think of any others.

### Eric Brewer, 2024-04-16

Also added a case in turbulence and with -5 degree pitch estimation error.

### David Grosher, 2024-04-16

@Eric Brewer Maybe a Fwd Nudge, I’m not sure if it would be different whether it is in position hold or attitude hold.

### Eric Brewer, 2024-04-16

@David Grosher In position hold the nudge will change the position setpoint so should look the same as the position step.  I’m less certain on the attitude control.  I could envision a problematic case where you do an attitude step that takes you through the transition region of 2-10 degrees pitch and you could get some coupling of the fixed-wing helper phaseout and the pitch loop.  I’m not sure how to simulate this though since any attitude mode would leave position open-loop.  The 2-10 degree band is pretty wide and there is also a 0.1 per second rate limit on the throttle which would hopefully help in this case.  I did add a plot of a 10 degree pitch hold for 2 seconds in VTOL mode, you can see this results in a pretty big velocity and position step, so it’s unlikely we’d have anything that aggressive when in an attitude mode.  I also double-checked the code after producing these results, and I believe fwmcActive() will return false if the autopilot is not in a position hold mode.

### Eric Brewer, 2024-04-17

Prototype implemented, ready for porting onto the autopilot.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [PrototypingResults.pptx](attachments/20041_PrototypingResults.pptx.md) | pptx | 1928 | 2024-04-16 | converted |
