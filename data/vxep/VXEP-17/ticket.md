# VXEP-17: TPTR-56 AV reported as not being able to hold position during landing in high winds

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2023-08-23
- **Updated:** 2024-03-26
- **Resolved:** 2024-03-26
- **Reporter:** Allen Gardner
- **Assignee:** David Grosher
- **Creator:** Allen Gardner
- **Links:** relates to ENG-2979 (VXE493 Rearward Drift on Landing); relates to FS2-849 (VXEP-17 TPTR-56 AV reported as not being able to hold position during landing in high winds); relates to FS2-1392 (Evaluate MC FW helper control loops.)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** VXE 493
- **Root Cause:** Winds (20-25mph) were above the specified limits for the vehicle (20mph),
- **Severity:** 2 - Degraded Performance - No Workaround
- **Impacted Core Subsystems:** Aircraft

## Description

Aircraft 493 was reported as not being able to hold position during landing in high winds resulting in a rearward drift and landing downwind of the planned landing zone. 
Investing whether customer may have exceded wind limit as defined in the manual

Shah, Dhruti (UK) - Mon Jul 10 21:37:17 BST 2023 : Vendor PTR-B 10/7/23: Confirm the wind conditions as this may have exceeded the wind conditions for Launch and Recovery (20mph). EA to assign engineer to look at data provided by Dan to confirm if issue requires investigation

## Corrective Action

Do not fly in winds above the specified limits.  Evaluate potential improvements to the FwHelper in the future to improve robustness to high wind.

## Plan

From VXE493 Investigation.pptx
- Attempt to Reproduce Issue on HIL: ​
- HIL will allow wind settings.​
- Use HIL and Flight Testing to understand VTOL​ Behavior.
- Keep trying to get data? Can it be downloaded from 493? Send Dan OS.

## Issue Status

Closed, see root cause and corrective actions.  More details included in https://jenaero.sharepoint.com/:p:/r/sites/EngineeringTeam/_layouts/15/Doc.aspx?sourcedoc=%7BD30018A2-39D8-42E1-A35A-15C1BFD5022A%7D&file=VXE493%20Investigation_Update2024_01_30.pptx&action=edit&mobileredirect=true

## Comments (7)

### Allen Gardner, 2023-08-25

@David Grosher Can you create a task to assess the root cause fo this issue?

### David Grosher, 2023-08-28

@John Clark, I linked the original issue in VIT2 (VIT2-323).

### Pat Wells, 2024-01-23

@David Grosher is this possibly to related to the recent issues we looked at with 401 or 501?
There is a lot of recent discussion on the VIT2 ticket related to this VXE Problems ticket. 
https://jenaero.atlassian.net/browse/VIT2-323

### David Grosher, 2024-01-23

@Pat Wells It is unclear because the data was not provided for the underlying incident. Data was provided for the wrong flight. I doubt there will be a conclusive conclusion given that.

### Eric Brewer, 2024-01-30

Latest analysis here:
https://jenaero.sharepoint.com/:p:/r/sites/EngineeringTeam/_layouts/15/Doc.aspx?sourcedoc=%7BD30018A2-39D8-42E1-A35A-15C1BFD5022A%7D&file=VXE493%20Investigation_Update2024_01_30.pptx&action=edit&mobileredirect=true

### Greg Fryer, 2024-03-26

Per finding, winds above rating for landing, drift expected.

### Greg Fryer, 2024-03-26

@Eric Brewer @Pat Wells @Rodney Linch @David Grosher I wandered into this ticket from the TIQ tracking. We stated it was complete but did not push the button. I have moved this to closure, so PM can report it as done.

## Attachments (0)
