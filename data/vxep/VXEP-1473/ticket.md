# VXEP-1473: VXE 818 MCM/Comms issue SB35x

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-08-14
- **Updated:** 2026-03-02
- **Resolved:** 2025-10-28
- **Reporter:** Michael Mohr
- **Assignee:** Ted Trowbridge
- **Creator:** Michael Mohr
- **Labels:** LRR
- **Links:** causes OGCS-421 (Implement Crash Recovery Test)
- **Customer:** LRR
- **Vehicle Tail Number:** 818
- **Vehicle Configuration:** 35X
- **Incident Type:** Mission Failure/Abort
- **Severity:** 1 - Flight Critical

## Description

Another issue with SB35x here. Description: 
Two AC were flying at one time, frequency's were 100mhz apart and have been operating on these frequencies for multiple days. Both AC had a coms interruption at the same time both loosing coms for at least 4 minutes. One AC (828) came back on and the crew was able to continue to fly. The other AC (818) did not come back on OGCS however we cold still see the Silvius webpage, SA camera, and Epsilon so the coms at that point were okay besides the OGCS. There could have been coms interruptions from the nearby LM facility but not sure on that. 
For AC 818 we tired to trouble shoot what we could be ultimately could not get back into OGCS and had to let it land in lost coms. 
Things troubleshot: 
- SSH into MCM (this worked)
- Ping MCM (this worked)
- Open AC Radio webpage (this worked)
- Open SA video (this worked)
- Open EPS video (this worked)
- Change frequencies (did not work)
- Change laptops (did not work)
- Remove Ethernet router (did not work)
- Close webpage (did not work)
- Close google chrome (did not work)
- Log out of cached OGCS (did not work)
- Clear Cache of Chrome (did not work)
- Restart laptop (did not work)

Connect to non hardened laptop (did not work)

## Corrective Action

- Implement automatic restart of OGCS backend server after abnormal exit in OGCS 1.3.1
- COMPLETED
- Capture additional logs in OGCS AAR to aid future diagnostics.
- COMPLETED
- Verify automatic restart of OGCS 1.3.1 in HIL environment by triggering a crash using engineering tools.
- COMPLETED
- [Optional] Prepare instructions on how to patch released versions of OGCS (1.2.1 LRR, 1.3.0 TIQ) and perform the patch.
- WON’T DO

## Issue Status

CAs in progress for OGCS 1.3.1
Need decision on patch for OGCS 1.2.1 LRR

## Root Cause

All evidence points to the OGCS backend server having crashed during flight.  This would appear to the user like a lost communications.

## Comments (8)

### Ted Trowbridge, 2025-08-14

All evidence points to the backend having crashed during flight, though this is not conclusive.  Fortunately the VSM continued running, executed its lost comms behavior, and the vehicle landed safely.  While the backend crash is very concerning, this is the first known occurrence and the outcome was a safe landing, so I would classify the issue for now as very low probability and medium severity.
I plan to implement the following mitigations for 1.3.1:
- Implement automatic restart of docker containers that exit abnormally.
- Capture additional logs in AARs to aid future diagnostics.
- We were missing critical docker and NGINX logs that might've shed more light on the issue.
- Add engineering tools to allow forcing a backend crash (in a HIL environment) and validate system recovery.

My recommendation would be to continue with 1.2.1 flights unless the issue is experienced again.

### Ted Trowbridge, 2025-08-14

@David Grosher  there is a simple patch to docker-compose.yml that could be applied to existing vehicles, running any version of OGCS, that may prevent this issue.  It doesn’t change any of the flight tested binaries, just the behavior of docker if a container exits abnormally.  The change will become the default behavior in 1.3.1

### Greg Fryer, 2025-08-15

@Ted TrowbridgeNeed to make sure we drive this to closure, seems like you have the CAs identified, just need to list them in the section above, put a status for each, and move ticket to “implementing corrective action”.
Assuming Dave agrees. FYI this is high on the priority list, so getting it closed is good. 🙂 
Also, not sure if LRR will want a report, but you can close loop with @Addison Osborn.

### Ted Trowbridge, 2025-08-15

@Addison Osborn see updated status and CAs.
There is a low risk patch we could apply to 1.2.1 LRR birds, let me know if we would like to pursue that.

### Addison Osborn, 2025-08-15

@Ted Trowbridge - No need for the 1.2.1 patch on LRR aircraft. 1.3.1 will be installed before the next time that these are scheduled to fly. 
Based on the comments, my interpretation is that we reached the end of the log trail available and are left without an answer on why the OGCS backend crashed, can you confirm? 
For the report - I will have to give something to the Army on the root cause and CA. If the comments on this ticket capture everything we have, I’ll take care of capturing and communicating. Your time is better spent pushing toward 1.3.1 features and release.

### Ted Trowbridge, 2025-08-15

@Addison Osborn
my interpretation is that we reached the end of the log trail available and are left without an answer on why the OGCS backend crashed, can you confirm?

That’s correct, the exact cause of the crash (i.e. offending module or line of code) is still unknown.  I reached a “reasonable” end of the log trail given I don’t have an unlimited time to investigate.  I’m satisfied with the explanation and corrective actions.

### David Grosher, 2025-10-28

@Ted Trowbridge This is all released, correct?

### Ted Trowbridge, 2025-10-28

@David Grosher yes, released as of 1.3.0 so should be in the hands of both TIQ (1.3.0) and LRR (1.3.1)

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V818_20250814T182324Z.zip | archive | 9875 | 2025-08-14 | listed only |
| Photo of error when trying to log in..jpg | image | 60 | 2025-08-14 | listed only |
