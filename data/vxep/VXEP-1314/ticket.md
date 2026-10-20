# VXEP-1314: VXE 491 - CW 4036 - Failure in transition to VTOL

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-06-24
- **Updated:** 2025-12-04
- **Resolved:** 2025-06-26
- **Reporter:** Scott Whitney
- **Assignee:** Greg Fryer
- **Creator:** Scott Whitney
- **Parent:** VXEP-573 Sustainment: VXE30 Incident Investigation
- **Issue color:** yellow
- **Vehicle Configuration:** VXE30 plus Block 35X prototype center wing
- **Problem Type:** Other (explain in description)
- **Plan:** Complete
- **Issue Status:** Closed
- **Incident Type:** Aircraft Loss
- **Monitor Type:** None
- **Severity:** 1 - Flight Critical
- **Components (EA Aircraft):** Aircraft, full assembly
- **Product/Tech Owner:** Greg Fryer

## Description

AC 491 SCO incident
FLOPs Asset: 491 w/ 35X centerwing 
- Vehicle config BLK 30
- Software: 6.5.0

## Corrective Action

No product/production action. Will propose to SCO/FLOPS a quality check when major elements are assembled (perhaps similar to what Final Assy does)

## Root Cause

Aircraft 491 was previously used to flight test a spare Avionics Enclosure, which requires un-mating/remating the Main System Harness, which provides power to the avionics. Data shows loss of power to Avionics during VTOL landing. Further, on inspection of asset, it was noted that the Main System Harness was not connected to the avionics (“Black Alden”). That connection is robust enough, if fully mated, that it is not expected to un-mate, even in a crash. Given the alignment of the physical state and data, the root cause is determined to be incomplete re-assembly, allowing the connector to come un-mated due to vibration during vehicle prep and flight.

## Comments (14)

### David Grosher, 2025-06-24

VXE30 CW for MOLSON
All lift motors stopped at the same time.
 
VTOL Event log stops at transition to descent.
XCOMM event log shows messages from the VTOL event log for 4.5 seconds after transition to descent.
XCOMM data log shows updates to data from VTOL system up to 6.8 seconds following transition to descent.
VTOL data log shows updates for 10.4 seconds following the transition to descent.
 
Video shows props spin up at ~13 seconds and event occurring at  ~41-42 seconds. Or a delta of 29 seconds.
Impact at ~45 seconds
 
Props get non-zero throttle at VTOL CpuTime 1624.5
Log ends at 1653.6
Delta is - 29.1 seconds - VTOL data log covers basically all of the nominal flight until the event.
 
Last XCOMM event log is 20.7 seconds after the lift motors are un-safed.
XCOMM event log is quite stale especially considering that it was in the middle of printing out the TRACE table
 
No Power anomalies prior to the end of the log.
Throttle maintained until the end of the log.
 
Possible Causes:
- Power failure to avionics [seems very plausible considering XCOMM log is very stale]
- Power failure to lift system [unlikely to occur after logging ends]
- WDT on the VTOL [possible but doesn't explain the XCOMM log - usually XCOMM log will extend longer than VTOL in this case and often will maintain power after crashing.]
- A lost XCOMM resulting in lift system shutting down?

 
Next steps:
- Pull GCS logs and see if there are any messages from the AV after the event but prior to the crash.
- Hardware inspection? Not sure if anything of value can be learned here.
- Test in HIL whether the XCOMM being lost could result in the lift system shutting down.

 
Corrective Actions:
- Port File I/O changes to XCOMM for more robust logs?

### David Grosher, 2025-06-24

@Jason Scherer Can you take a look and see if I missed anything here?

### Jason Scherer, 2025-06-24

@David Grosher I don’t see anything obvious. After looking at both datalogs It looks like the vehicle had a successful transition before the data stops. Can we pull the FDR? That usually has longer data in my experience. If it was a VTOL lift system failure, I think we typically see the data cut out earlier than this data. Given the abrupt end of XComm logs I am inclined to think maybe this is an avionics power issue in which case the FDR won’t help. If the FDR data goes longer than that could be evidence that the avionics power wasn’t disrupted.
While not too bad, it does seem like the autopilot was having a bit of difficulty achieving stability. Maybe winds? The booms are a bit uneven, and the throttles are a bit divergent. At the same time the pitch/roll are +/- 10 degrees.
VTOL data during landing for reference.
[embedded image-20250625-025451.png]

### David Grosher, 2025-06-25

@Ryan Smith Can you pull the FDR data and the GCS logs?

### Ryan Smith, 2025-06-25

Uploaded as 2025062025_491_FDRRECOV.csv

### Ryan Smith, 2025-06-25

Was communicated in person but wanted to write this down for future reference that when taking the avionics box out of the fuselage, the grey debug connector was the only one connected. The black main harness and transponder port were disconnected. Apologies if this was not communicated earlier and that photos were not taken. @David Grosher @Jason Scherer

### Greg Fryer, 2025-06-25

Per discussion with Carson, FLOPS also noted that the Main System Harness (Black Alden that Ryan referenced below) was disconnected. I will verify with them on their return this afternoon. If that is correct, this matches the sudden loss of all data as it would remove power from avionics. Further (also per Carson) 491 just recently had it’s avionics swapped (it is used to test individual spare parts such as avionics enclosures). It is reasonable that the Main System Harness connector did not get mated all the way, and so was vulnerable to the vibration of assembly/launch/flight/land.
Beyond verifying the circumstances, there is no further way to prove this, but it aligns with info.
@Jason Scherer Can you verify that all the data cut off at once? (That’s how it was casually described to me, so call this “for the record”)
@Scott Whitney If @David Grosher and I agree, we can convert this ticket to an incident, fill out the sections, and close.

### Scott Whitney, 2025-06-25

Ben Norris report and dispo of battery is in https://jenaero.atlassian.net/browse/FS2-3426?focusedCommentId=55138

### Scott Whitney, 2025-06-25

@Greg Fryer - yes, please feel free to move as needed

### David Grosher, 2025-06-25

@Greg Fryer The data is buffered and logged so it doesn’t ever all end at the same time. But there is no data for any system after the lift system loses power.

### Ryan Smith, 2025-06-25

Correction just the black main harness this avionics box does not have a transponder port

### Greg Fryer, 2025-06-25

@David Grosher Understood. Given there’s no further info and this seems very likely based on circumstances, any issue if I document it as closed? I may issue a CA to add an inspection in re-assembling test assets.

### Jason Scherer, 2025-06-25

@Greg Fryer This is a look at where each processor stops logging by correlating VTOL Throttles. All logging stops within 5.22 seconds.
[embedded image-20250625-220127.png]

### David Grosher, 2025-06-25

@Greg Fryer Agreed.

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [VTEVLOG (2) 1.txt](attachments/30138_VTEVLOG%20(2)%201.txt.md) | text | 159 | 2025-06-24 | converted |
| [VTL00011.csv](attachments/30139_VTL00011.csv.md) | csv | 6937 | 2025-06-24 | converted |
| [XCEVLOG (10).txt](attachments/30137_XCEVLOG%20(10).txt.md) | text | 161 | 2025-06-24 | converted |
| image-20250625-025451.png | image | 130 | 2025-06-24 | listed only |
| v491 investigation.zip | archive | 3086 | 2025-06-24 | listed only |
| [2025062025_491_FDRRECOV.csv](attachments/30154_2025062025_491_FDRRECOV.csv.md) | csv | 151 | 2025-06-25 | converted |
| T95_V491_250624_145154_pack.zip | archive | 163 | 2025-06-25 | listed only |
| image-20250625-220127.png | image | 206 | 2025-06-25 | listed only |
