# GCSS-366: GCS froze during RTB command

- **Issue type:** Bug
- **Status:** To Do
- **Priority:** Highest
- **Created:** 2024-09-30
- **Updated:** 2025-12-31
- **Reporter:** Scott Whitney
- **Assignee:** Michael Berger
- **Creator:** Scott Whitney
- **Components:** GCS Application
- **Parent:** FS2-2335 VXEP-555 Anomalies on Launch and in flight
- **Links:** relates to VXEP-555 (VXE 530 Anomalies on Launch and in flight)
- **Epic Link:** FS2-2335
- **Sprint:** GCSS Sprint 30

## Description

- When RTB was commanded, GCS screen froze with hourglass for 90+ seconds. When the sim (or whatever it was doing) finished, a window popped up for 1 or 2 seconds stating that the aircraft was executing the Lost Comms Mission. when the window closed, the aircraft entered the active landing pattern with no user input. Comms indicator remained green throughout and comms (per Silvus GUI) were great.

More details in https://jenaero.atlassian.net/browse/VXEP-555

## Comments (2)

### Ted Trowbridge, 2024-11-20

@David Grosher  @Eric Brewer @Jason Scherer @Michael Berger 
Based on the presence of an hourglass cursor on the map and the defect narrative it appears the application froze during mission simulation for about 111 seconds.
```
CSimResults CSamsView::RunSimulation(...)
{
  debug->DebugInt("qsim:" ...);     // <-- This is seen in the logs @ 15:50:12
  
  ... sim setup ...
  
  SetMapMousePointer(moHourglass);  // <-- Cursor set to hourglass
  
  ... sim running, *application freeze* ...
  
  SetCursor(m_CurrentCursor);       // <-- Normally cursor is set back here
  
  ... build dialog to show simulation results ...
  
  TrackingLayerRepaint(true);       // <-- This is seen in the logs @ 15:52:21 after the freeze
}
```
All debug messages inside simulation are dependent on the SIMDEBUG compiler directive which is not enabled. That means we can’t tell precisely where the app hung during simulation.
The simulation code runs on the UI thread and will block the entire application until it completes, it also creates and updates a progress dialog during the simulation.  It seems likely that either the simulation failed to complete for 111 seconds or a blocking UI call was made to an MFC component that hung the windows event loop, or some combination of the two.
The simulator is faster-than-real-time and only has two termination criteria:
- The simulated time exceeds the vehicle endurance, which can be as high as 8+ hours.
- The simulated vehicle detects “touchdown” by looking at vehicle altitude below DTED.

If the simulator never detects the vehicle touching down, it will run until it has simulated for the full vehicle endurance time.
Next steps:
- Determine how long the simulator could run in real time if it ran a full simulation of an 8+ hour mission that never lands.  This should be run in RELEASE mode on the target GCS hardware for an accurate reading.
- We may be able to re-create a test of the simulator given the vehicle's reported state at the time the RTB was commanded and the mission loaded.  This may uncover a defect in the simulation causing it to not complete.
- We should investigate additional termination criteria based on the findings in 1 & 2, examples may include:
- Terminate the simulation if it exceeds a given wall clock time (e.g. no more than 10 seconds real time)
- Terminate the simulation if the simulated vehicle is stuck in a loop or not flying normally.  This would be dependent on the findings in #2 above.

### Christa Meck, 2025-12-31

@Scott Whitney Does this need to be assigned to someone to be worked or did we cover it in another ticket at some point?

## Attachments (0)
