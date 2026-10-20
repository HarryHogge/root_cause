# VXEP-1635: During NSW IQT, both customer E95 gimbals had multiple issues connecting to three different Advanced Nav aircraft used during training. Also, the gimbals would not power off when cycling power in the custom payload control in VXE-SUAV.

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-12-12
- **Updated:** 2026-08-07
- **Resolved:** 2026-08-07
- **Reporter:** Michael Mohr
- **Assignee:** Grant Goodman
- **Creator:** Michael Mohr
- **Labels:** NSW, Weekly-incident-tracker
- **Links:** relates to VXEP-1639 (E95 S/N E8093 experienced multiple issues during NSW IQT); relates to VXEP-1637 (E95 S/N E8090 experienced multiple issues during NSW IQT); relates to PLD-139 (E95 SN 8098 and  8115 Vector nav not responding when tested with 987.)
- **Customer:** NSW

## Description

Some duplication of Jira incidents. 

Problem Description. 
E95 gimbals E8090 and E8093 experienced multiple connection and power issues during NSW’s IQT. Connection, power, and problems were experienced with multiple aircraft. Aircraft tails used during training included VXE-920, VXE-946, VXE-956
EDIT: Also noticed that gimbal would not power off when cycling power to port through tools.
In Epsilon Errors
-Critical error - Tilt Encoder No Index
-Secondary error - GPS no communication GPS init failed

## Comments (7)

### Michael Mohr, 2025-12-12

@Jeremy White @Drew Hildreth @Cameron Chapman @Cody Smisek @John Gober @Mike DeJesus Created an Epic ticket linking S/Ns E8090 and E8093 gimbal tickets. We were on a very compressed IQT schedule and didn’t spend a large amount of time trouble shooting.

### Cody Smisek, 2025-12-13

@Cameron Chapman @Mike DeJesus @John Gober 
I was provided a picture from @Anthony Hansen from one of the gimbals (unsure which SN at this time) that showed what I added to the issue description above. 
I would recommend we do not connect any further E95s to advanced nav aircraft. 
Based on what I’ve reviewed from the travelers included in the cases, the GPS was checked in HSV and working for these (not 100% sure, but sounds like they have been checked on standard vxe30 aircraft due to difficulty in setting up for bench harnesses). Seems like a common factor so far is adv nav vehicles.
I’m also linking the 2 separate gimbals we tested yesterday in SLO.

### Anthony Hansen, 2025-12-15

For some context on the Tilt Encoder issue, we were flying at the dirt/sand airfield located on Ft. Hunter-Liggett, CA. We believe the tilt encoder faults were caused by sand/fine gravel being thrown into the gimbal area by the front propellor during ground motor testing (pre-flight). We were able to get some gimbal functionality by blowing out as much sand/fine gravel as possible before launch

### Michael Mohr, 2025-12-16

@Cameron Chapman @John Gober @Cody Smisek Also noticed during training that gimbals would not power off when cycling power to port through tools.

### Mike DeJesus, 2025-12-22

@John Gober please report E95 findings on this Jira ticket.

### John Gober, 2025-12-22

Tested E95’s EPS8090 and EPS8093 after they were returned. Results on their respective tickets above.

### Alexander Alan Arnold, 2026-08-07

RMA complete, gimbals repaired

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| E8090.mov | video | 8400 | 2025-12-15 | listed only |
| Spinning E95.mp4 | video | 6183 | 2025-12-15 | listed only |
