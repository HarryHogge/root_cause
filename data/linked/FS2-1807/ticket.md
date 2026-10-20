# FS2-1807: Investigation 6.2.9 landing overshoot

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-05-02
- **Updated:** 2024-07-09
- **Resolved:** 2024-07-09
- **Reporter:** Scott Whitney
- **Assignee:** Eric Brewer
- **Creator:** Scott Whitney
- **Components:** Vehicle Incident Support 
- **Parent:** FS2-1862 VXEP-315 Landing Performance Improvements
- **Links:** relates to VXEP-315 (VXE 459 Overshoot of LZ Mishap on landing, operator unable to nudge); relates to FS2-1672 (V459 Incident Investigation)
- **Epic Link:** FS2-1862
- **Sprint:** FS2 Sprint 19, FS2 Sprint 18, FS2 Sprint 20

## Description

During landing, there has been multiple reports that aircrafts have been missing their LZ in both lateral and longitudinal directions

## Comments (6)

### Eric Brewer, 2024-05-09

@David Grosher , let me know if there’s something specific you want me to look at here outside of the fixed-wing helper updates described in the issues attached here.

### David Grosher, 2024-05-09

@Eric Brewer , We should also look into the lateral excursions. That incident that Ben had recently (526?) seemed like there was a lateral transient that wasn’t fully explained by wind.

### Eric Brewer, 2024-05-13

@David Grosher thanks.  I took a look at 426 and added some notes to the presentation.  I put a summary on slide 25, but short version is it looks like the vehicle was not converged laterally when the transition started.  From discussions with Artis and Ruysser they thought it was operator error to land with a crosswind.  I believe if we adjusted the software to force the landing waypoint further back so the lateral controllers have more time to converge it may clean up the lateral tracking issues.

### David Grosher, 2024-05-13

@Eric Brewer I would generally agree that we shouldn’t be transitioning in a crosswind, but I’m not sure the manual actually says that.

### Eric Brewer, 2024-06-24

Attached test plan/test results from release work.

### Eric Brewer, 2024-07-09

Investigation completed. The scope of this task also grew a bit as we merged in the changes to the VTOL autopilot and they are included in the latest release.  The changes include:
- Add in fixed-wing helper phaseout to eliminate throttle usage when the vehicle is overshooting the touchdown point.
- Reduced max fixed-wing helper contribution to 0.4 from 0.6
- Implemented GPS rate calculation in accel updates (this was a separate ticket, but still tested here)

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Candidate1_55_TestResults.pptx](attachments/21172_Candidate1_55_TestResults.pptx.md) | pptx | 4974 | 2024-06-24 | converted |
| [TestPlan.docx](attachments/21171_TestPlan.docx.md) | docx | 16 | 2024-06-24 | converted |
