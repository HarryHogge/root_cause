# VXEP-1955: VXE 966 Abort button on the Razor hand controllers to not function to abort the landing

- **Issue type:** Incident (8D)
- **Status:** D6 - Verifying Corrective Actions Are Complete
- **Priority:** Medium
- **Created:** 2026-07-09
- **Updated:** 2026-09-02
- **Reporter:** Stephan Johnson
- **Assignee:** Ted Trowbridge
- **Creator:** Stephan Johnson
- **Labels:** Software
- **Links:** is fixed by OGCS-617 (Razor Controller Abort Not Working)
- **Customer:** Redwire
- **Vehicle Tail Number:** VXE 966
- **Vehicle Configuration:** VXE-30 ADV Nav
- **Problem Type:** Discovered Issue
- **Issue Status:** Corrective Action Implemented
- **Incident Type:** Other (Record"Event Type: XXXXXX" in the description)
- **Severity:** 3 - Degraded Performance - With Workaround
- **Executive Summary:** Bug created, worked tracked by engineering in Bug; Probable cause Software Issue.

## Description

VXE 966 - Abort button on the Razor hand controllers to not function to abort the landing and return to IP1 of the landing plan. It was seen that the pause button does function while in VTOL descent. 


same aircraft seperate attempt Hadley held pause from about 150 feet until 40 on this last recovery with Xbox controller and the aircraft did not pause until selected in OGCS VTOL window

## Corrective Action

OGCS 1.5.0 will add the ability to abort back to IP1 from the joystick while enroute to or in the landing pattern.  An additional notification will appear for confirmation to the operator.

## Root Cause

The root cause is a miscommunication about this features availability.  This behavior was never implemented in Jennings or OGCS.
The abort button on all joysticks (XBOX, Razor, SCIP, etc.) does not allow aborts while enroute to or in the landing pattern.
OGCS does not allow aborting from the joystick until after IP5, at which point the abort window is extremely small. Realistically, only pause can be executed from the joystick.

## Comments (4)

### Alexander Alan Arnold, 2026-07-10

@Ted Trowbridge Unsure if you are already tracking this issue or not. If you are do, we need to keep reporting it? If it is already tracked somewhere, can you provide the link so the HSV team can be aware of this issue and brief the instructor team.

### Ted Trowbridge, 2026-07-10

@Alexander Alan Arnold I was not tracking this issue, i’ve filed https://jenaero.atlassian.net/browse/OGCS-617  to address it and linked it to this issue.

### Alexander Alan Arnold, 2026-07-10

@Ted Trowbridge understood. I will add additional AARs and Logs once the team returns from the training site. Please let me know what else needs to collected data wise. @Anthony Hansen

### Ted Trowbridge, 2026-08-25

@Alexander Alan Arnold ticket updated - this feature was never implemented in OGCS or Jennings and was likely expected to work based on a miscommunication.
We have implemented it in 1.5.0 and it will be available once that is released.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V966_B30N_20260630T184957Z (1).zip | archive | 13768 | 2026-07-09 | listed only |
| [Land Abort Inop Reporting Procedure Form.docx](attachments/63361_Land%20Abort%20Inop%20Reporting%20Procedure%20Form.docx.md) | docx | 109 | 2026-07-09 | converted |
