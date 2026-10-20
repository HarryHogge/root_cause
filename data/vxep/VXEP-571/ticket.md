# VXEP-571: VXE 444 Two aborted launches sequentially

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-08-28
- **Updated:** 2026-08-14
- **Resolved:** 2024-09-09
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** MARSOC, Software, Weekly-incident-tracker
- **Customer:** MARSOC
- **Vehicle Tail Number:** 444
- **Root Cause:** It is believed to be a software issue but given the lack of data it is hard to determine
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Received from operator:
Tonight we had two aborted launches back to back by the aircraft itself. Immediately after arming the aircraft and commanding launch, the flaps went up and the, VTOL motors kicked on, and the aircraft climbed where it stopped at about 10ft and executed an abort profile. We restarted the aircraft put a new battery in the bird and restarted the process where the exact same thing happened.

AAR’s attached.  I believe one is incomplete and I’ve already reached out to the operator about it.

## Comments (3)

### David Grosher, 2024-08-28

@Pat Wells It appears to have lost link with the GCS in the 2nd flight. The first flight AAR didn’t have any data from the vehicle. 
[15:54:54.050 410.050] ap dbg: vt lost link during lch, aborting
[15:54:54.053 410.053] ap dbg: vt lch abort triggered
The first things to check would be the radios and frequency clearance for the range.  
Note: this vehicle is on v6.1.2

### Pat Wells, 2024-08-28

@David Grosher I will relay to operator. Thanks

### Pat Wells, 2024-09-09

Loss of link

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V444_240828_084059_pack.zip | archive | 81 | 2024-08-28 | listed only |
| T95_V444_240828_085500_pack.zip | archive | 961 | 2024-08-28 | listed only |
