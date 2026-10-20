# VXEP-1858: VXE 885 Transition at 20 feet, operator aborted

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2026-04-20
- **Updated:** 2026-09-17
- **Resolved:** 2026-08-12
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Ted Trowbridge
- **Creator:** Alexander Alan Arnold
- **Labels:** GS_Closed, RCCA, Training, USAACE_(2-13th), Weekly-incident-tracker
- **Customer:** USAACE
- **Vehicle Tail Number:** VXE 885
- **Vehicle Configuration:** ADV NAV w OGCS Standard Battery 140G2Z
- **Corrective Action:** Implement launch wizard checks in OGCS to prevent invalid launch transition altitudes.
- **Issue Status:** Fix implemented in OGCS 1.3.3
- **Severity:** 1 - Flight Critical

## Description

Operators reported that aircraft attempted to enter FW flight at approximately 20 feet AGL, Operators then aborted launch. 
*Awaiting Operator Statement
*I need someone to confirm that both logs indicate normal flight as I believe they keep sending incorrect data

## Plan

Waiting for more information.  (4/21/26 - Slovett)
@Ted Trowbridge  @Scott Whitney are you able to link the CAs for these? Ex: don’t allow waypoints under ground?

## Root Cause

Launch route was modified to use an unsafe MSL altitude which was 10ft below the ground.  Unclear why the operator made this change or if it was accidental.

## Comments (10)

### Ted Trowbridge, 2026-04-20

Looking at OGCS logs from AAR_V885_20260415T200613Z it appears the operator changed the first launch waypoint from the default 200ft AGL to a value of ~4750ft MSL, which is 10ft below the MSL value at calibration of 4760ft.  I’m not sure at what point the AP starts checking a transition goal altitude, but it may have gotten 20ft before running that check for the first time.
I can only assume the change was accidental, but it seems hard to imagine how it would’ve happened.  They would’ve needed to manually select MSL and change the value.
We should block launch in OGCS if the goal altitude is too low.
@David Grosher

### Scott Lovett, 2026-04-22

Agreed… looks like the operator commanded a 300 ft takeoff climb. Aircraft got to hover at ~4 ft AGL, initiated forward-transition (airspeed built to 97 fps), then airspeed collapsed in 1 second (~45 fps/s deceleration) and never recovered. Aircraft never actually climbed, just stayed at 2–5 ft AGL the whole time and then settled back to the ground.

### Pat Wells, 2026-08-11

@Ted Trowbridge please verify status a CA.  Did we Implement launch wizard checks in OGCS to prevent invalid launch transition altitudes.
@Josh Burrell FYSA for documentation @Grace Burgess FYSA for training

### Ted Trowbridge, 2026-08-11

@Pat Wells OGCS 1.3.3 implemented limits on allowed launch transition altitudes, and OGCS 1.4.3 implemented limits on allowed landing transition altitudes. I am tracking the CA implementation as completed.
@Josh Burrell / @Grace Burgess do we emphasize preferring AGL over MSL altitudes to avoid operator error?  If not, I think we should.

### Josh Burrell, 2026-08-11

@Ted Trowbridge @Pat Wells I think that saying that the preferred is AGL over MSL would be confusing to the operators since we provide both AGL and MSL. Since the fixes are already in 1.3.3 and coming out in the 1.4.3 I don’t think there’s a need for any document change. Please let me know if you disagree @Ted Trowbridge .

### Alexander Alan Arnold, 2026-08-12

@Ted Trowbridge wasn't there a fix in OGCS that now stops operators from inputing incorrect values for launch? or does that only apply to AGL?

### Ted Trowbridge, 2026-08-12

@Alexander Alan Arnold Yes, see my note below in the comments:
OGCS 1.3.3 implemented limits on allowed launch transition altitudes, and OGCS 1.4.3 implemented limits on allowed landing transition altitudes. I am tracking the CA implementation as completed.

### Alexander Alan Arnold, 2026-08-12

CA completed

### Grace Burgess, 2026-08-13

@Ted Trowbridge We do typically recommend AGL for launch. Due to easily making errors when using MSL, we can continue to suggest AGL until OGCS can block launch if altitude is too low.

### Ted Trowbridge, 2026-09-17

@Alexander Alan Arnold @David Grosher 
Here is a video of deleting the 3 from 300 and attempting to change it to 2 for 200 but ending up with just 2 . 
[embedded LandingPatternTwoFtAlt.mp4]

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V885_20260415T183610Z.zip | archive | 16247 | 2026-04-20 | listed only |
| AAR_V885_20260415T200613Z.zip | archive | 18063 | 2026-04-20 | listed only |
| LandingPatternTwoFtAlt.mp4 | video | 71089 | 2026-09-17 | listed only |
