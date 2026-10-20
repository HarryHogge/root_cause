# VA-486: VXE466 Test ADP. Production Test, WindTunnel Test, Hot/Cold Test

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2023-09-11
- **Updated:** 2023-11-09
- **Resolved:** 2023-09-11
- **Reporter:** Connor Peebles
- **Assignee:** Mark Squillante
- **Creator:** Connor Peebles
- **Links:** relates to VXEP-381 (VXE466 Course Deviation and Crash - Internal Investigation)

## Description

VXE466 Test ADP. Production Test, WindTunnel Test, Hot/Cold Test, 

Customer Matt C. specifically want’s an answer to this “the data points to the airdata system not working. we assumed this to be a result of snow. did anyone ever test the airdata unit to make sure it generates the correct values at flight airspeed? If it does, then the crash was caused by snow. customer is asking“

## Comments (10)

### Connor Peebles, 2023-09-11

@Mark Squillante @Madeleine Masiello @Cameron Chapman

### Mark Squillante, 2023-09-11

Production test checked out fine. Static probe was coming out of ADP when disconnecting cube from static probe.

### Mark Squillante, 2023-09-11

Passed wind tunnel test up to 60fps.

### Cameron Chapman, 2023-09-11

Thanks @Connor Peebles for creating and @Mark Squillante for performing that test. We need to document this investigation in detail. 
- Can you please elaborate on "Static probe was coming out of ADP when disconnecting cube from static probe." could this be a failure cause?
- Since Matt just asked for “make sure it generates the correct values at flight airspeed” I think we can just provide results and inspection details from the wind tunnel and standard production tests. No need to do hot/cold yet unless that is part of the standard ADP test.

### Connor Peebles, 2023-09-11

@Cameron Chapman Would you like a fish scale incident investigation style report made?
We could repeat the test with varying degrees of the static probe pulled out
Also note that this ADP has had plenty of good flights of VXE371. I’m asking Sean to identify a timeframe where it was installed and we can figure out how many flights it went through on VXE371. [VA-487] VXE466 Identify Date 466 ADP was installed on VXE371 - Jira (atlassian.net)

### Mark Squillante, 2023-09-11

Here is a video showing how the static probe can pull out. During test it was pulling out while disconnecting the static pressure tube according to 107-101141 - Final Assembly - Air Data Pod Checkout (ADP HIL) - Procedure.pptx
[embedded: Static probe pulling out.mp4]
No indication this could be cause for failure.

### Mark Squillante, 2023-09-11

Attached is the test data from 466 ADP at room temperature.
[embedded: ADP 466 test traveler.pdf]

### Connor Peebles, 2023-09-11

Here is a link to the WindTunnel testing of 466ADP and 376A ADP:
Wind Tunnel Testing of 466ADP and 376A ADP.xlsx

### Mark Squillante, 2023-09-11

@Cameron Chapman closing task. Testing complete.

### Cameron Chapman, 2023-09-11

Great work. Thank you.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [ADP 466 test traveler.pdf](attachments/16200_ADP%20466%20test%20traveler.pdf.md) | pdf | 1099 | 2023-09-11 | converted |
| Static probe pulling out.mp4 | video | 27584 | 2023-09-11 | listed only |
