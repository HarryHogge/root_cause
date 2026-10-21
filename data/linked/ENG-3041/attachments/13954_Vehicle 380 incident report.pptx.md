# Vehicle 380 incident report.pptx

Attachment 13954, pptx, 74 KB, added 2023-04-17 by John Clark.

## Slide 1

Vehicle 380
Incident Log Analysis
J Clark
4/17/2023

## Slide 2

Summary
Lost Link During Launch:
After a successful 1st SCO flight for this aircraft, during the second launch, it reached about 250ft and aborted take-off on its own, landed safely. Debug window showed a message "VT lost link during lnch, aborting", 4 other flights were performed after this abort - the aircraft was able to take off and transition as usual. 
Log for this flight indicated the FW AP lost communications with the GCS in a critical phase.
[20:26:24.190 1821.190] ap dbg: lch timeout: 57
[20:26:25.190 1822.191] ap dbg: lch timeout: 56
[20:26:26.192 1823.192] ap dbg: lch timeout: 55
[20:26:27.018 1824.018] ap dbg: vt lost link during lch, aborting
[20:26:27.021 1824.021] ap dbg: vt lch abort triggered

## Slide 3

Summary
Normal Climb Sequence (edited)
[19:21:42.225 8757.225] ap dbg: lch state: 10
[19:21:42.309 8757.309] DebugMsg Start of climb
[19:21:59.004 8774.004] ap dbg: vt lch reached alt
Failed Climb Sequence (edited)
No observed state transition
[20:26:05.504 1802.504] DebugMsg Start of climb
[20:26:27.018 1824.018] ap dbg: vt lost link during lch, aborting
[20:26:27.021 1824.021] ap dbg: vt lch abort triggered

## Slide 4

Conclusion from Examination of FW AP Program
Aircraft did not complete “Wait for Departure Alt State”
LCH_GOALT,		// 9 command departure altitude
LCH_WAITGOALT,	// 10 wait for departure altitude, monitor health
Manage Lost Link function failed
[picture]

## Slide 5

UplinkStatus Failed: UplinkStatus = GetLinkStatus();

## Slide 6

Conclusion:
MaintainLink() Drives Link Status
MaintainLink(ONLINE_TIME); is reset anytime a message is received
Online Time is defined at 5: #define ONLINE_TIME 5
CanAbortLaunch above limits Launch Aborts to critical flight phases
Suggest not changing behavior since loss of communications in critical flight phase could result in more serious outcome.
