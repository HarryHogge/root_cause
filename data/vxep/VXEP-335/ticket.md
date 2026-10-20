# VXEP-335: Investigate timeouts in VTOL entry criteria to see if performance/robustness can be improved.

- **Issue type:** Improvement
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2024-04-08
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Eric Brewer
- **Creator:** Eric Brewer
- **Links:** relates to FS2-1672 (V459 Incident Investigation)

## Description

Investigate timeouts in VTOL entry criteria to see if performance/robustness can be improved.

## Comments (8)

### Everett Werner, 2024-04-09

| State | Entry Criteria | Exit Criteria (nominal) | Timeout (if applicable) |
| 1 LAND_WAITRANGE | Next waypoint is landing | Distance <  val + airspeed*val | N/A |
| 5 LAND_START | VTOL is armed and exiting state 1 | VTOL power is on | N/A |
| 6 LAND_HOLD | Exit from state 5 | Time defined in state 5 runs down | <--- |
| 7 LAND_CMDLZ | Exit from state 6 | Runs through | N/A |
| 8 LAND_WAITCMDLZ | Exit from state 7 | VTOL cmd acknowledged | 9 seconds (3x3 seconds) |
| 9 LAND_CMDNOSAFE | Exit from state 8 | Runs through | N/A |
| 10 LAND_WAITCMDNOSAFE | Exit from state 9 | VTOL cmd acknowledged | 9 (3x3 seconds) |
| 12 LAND_WAITVTOL | Exit from state 10 | VTOL healthy | 15 |
| 13 LAND_TRANS | Exit from state 12 | Runs through | N/A |
| 14 LAND_WAITTRANS | Exit from state 13 | Airspeed low or been in vtol long enough (overlap with timeout?) | 3 + VtolEntryTime (not typically triggered?) |
| 15 LAND_WAITLZCMD | Exit from state 14 | VTOL acknowledges LZ cmd | 6 (3x2) |
| 16 LAND_WAITLZ | Exit from state 15 | Timeout runs down or within distance | distance from landing point*VtolNavSpeed +20, max 50s |
| 24 LAND_DESCENDING | Exit from state 16 | Lands | N/A |

### Eric Brewer, 2024-04-16

@Everett Werner a couple updates/questions below.
VtolEntryAltHoldTime in state 5 is 8 seconds.
Where does 9 seconds in state 8 come from? I see the timout of 30 (3s) but I do not see the 3x3 mentioned.  Same for state 10.
For LAND_WAITTRANS I’m seeing a vtolEntryTime (15) second timer that can be triggered by the IsNotFlying check, and an adjacent timeout that can cause an abort of 3 + vtolEntryTime (15 + 3s).  So it looks like the abort would never be triggered from this state?

If that’s the case, I think we could consider allowing that abort to be triggered, but I’m not positive if any adjustment to the timers is needed.

### Everett Werner, 2024-04-16

@Eric Brewer 
State 8:
-timeout = 30 and retries = 3 is set in state 7
-Once timeout is 0 if retries are 0 it aborts, if retries are not 0 it sets the timeout to 10 (1s)
-This gives a total timeout time of 5 seconds if retries is decremented, I dont see though where retries is decremented, there is a portion of code that is commented outthat would decrement retries.

[embedded: image-20240416-182044.png]
State 10:
Same with state 10, a commented out retries decrement however if it was to decrement it resets the timeout to 3s rather than 1s for a total time of 9s
State 14:
I agree, this seems like it wouldn't ever be triggered.

### Eric Brewer, 2024-04-16

Ah ok thanks.  Per our side discussion I was looking at the Autopilot_605j folder not the Autopilot folder.

### David Grosher, 2024-04-16

@Eric Brewer @Everett Werner The original intent of this task for the overshoot was to simply look at the 30 second timeout in which the AV traveled 500 ft before forcing a transition in the VTOL state to have the lift system take over. I was thinking that the 30 seconds was too long. I did not intend to dive into the details of the VTOL abort logic, sorry that wasn’t clear.  Jason has just delivered an extensive rework of that logic because it was very broken.

### David Grosher, 2024-04-16

@Eric Brewer @Everett Werner Should we decrease NvBuffer2.data.VtolEntryTime from the current value (30 seconds?)?

### Everett Werner, 2024-04-18

@David Grosher It would probably minimize our worst case scenario where the vehicle continues to fly off endlessley. A good stopgap improvement would be to disable the fixed wing helper if it is upwind of its landing point by a certain margin if the fw helper is a feedforward on windspeed as @Eric Brewer  suggested. It would be a good temporary fix until we rework the helper to be on integral of position error. I also believe it is currently at 15 seconds.

### Everett Werner, 2024-04-18

@David Grosher @Eric Brewer 
Moving APVTOL_LANDPREP and APVTOL_TRANSITION into one of the return false groups might also help
[embedded: image-20240418-190853.png]
It would stop the fw helper from running in the fly in state.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240416-182044.png | image | 94 | 2024-04-16 | listed only |
| image-20240418-190853.png | image | 47 | 2024-04-18 | listed only |
