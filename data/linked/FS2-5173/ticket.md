# FS2-5173: V863 Stuck Semaphore Issue

- **Issue type:** Task
- **Status:** To Do
- **Priority:** Low
- **Created:** 2026-09-30
- **Updated:** 2026-10-05
- **Reporter:** Eric Brewer
- **Assignee:** Scott Hunter
- **Creator:** Eric Brewer
- **Parent:** FS2-5074 Flight Critical Gremlins
- **Links:** relates to VXEP-1978 (VXE 863 Loss of Link warning resulted in uncontrolled descent )
- **Epic Link:** FS2-5074

## Description

Fix for issue uncovered here:
https://redwireglobal.sharepoint.com/sites/FlightSafety/Shared%20Documents/Forms/AllItems.aspx?viewid=0c1aa895%2D9073%2D46b2%2Db705%2Dfcb1f8f035fb&id=%2Fsites%2FFlightSafety%2FShared%20Documents%2FActive%20Cases%2F2026%5F08%5FVXE863Investigation%2Fxcomm%5Fcomms%5Ffreeze%5Fsummary%2Emd&parent=%2Fsites%2FFlightSafety%2FShared%20Documents%2FActive%20Cases%2F2026%5F08%5FVXE863Investigation

Note: this should be part of a broader effort to get rid of ALL infinite wait semaphores in the ap, but this one can be prioritized ahead of that overall effort since it crashed a plane.

## Comments (1)

### Scott Hunter, 2026-09-30

Initial analysis of implementing a fix. Note the goal is to replace an infinite timeout for network TX with a reasonable timeout. When that timeout is experienced, a reset of the network stack is required to restore function. That’s proposed at the application level, polling the flags at some rate e.g. 10Hz or 1Hz.
@Eric Brewer - FYI

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [network_timeout_analysis.md](attachments/65006_network_timeout_analysis.md.md) | text | 12 | 2026-09-30 | converted |
