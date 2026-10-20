# VXEP-847: Raj PTO Task Handoff 12/30-1/13

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2024-12-26
- **Updated:** 2026-03-30
- **Resolved:** 2026-03-30
- **Reporter:** Rajesh Budhabhatti
- **Creator:** Rajesh Budhabhatti
- **Links:** relates to VXEP-848 (New ADP and Camera Cavity harness. )
- **Other Stakeholder (as required):** Grant Goodman

## Description

Cam comments in bold
I will be traveling to India 12/30-1/13. While I will have communications, there is a 11.5 hour time difference so I will be available 8:00 am to about 12:00 noon PST. I can be reached by teams or Outlook mail.
- Software quick start guide to new SA camera setup for Omron USB and Boson FLIR cameras here: Sightline Quick Start Guide.docx
- Please work with @Scott Whitney  to assign a GCS eng to scope the camera integration to GCS, and handoff info to them.
- This Sharepoint folder has all the relevant files: Documents
- Sightline will be supplying new software/firmware for Boson MIPI camera. Contact John Gober or Grant Goodman for status on Omron MIPI.
- New ADP harness and Camera cavity harness are being reviewed by John Gober. Once done, Cameron will review them. Please link a Jira task for this and attach redlines. Has mfg been notified of this build? Is there a production support request? Please create one if needed and link to the Jira task. Do we have all parts ordered? Jira link: https://jenaero.atlassian.net/browse/VXEP-848
- Gary Angelus has been informed about the harness drafting. Upon Cameron’s approval, Gary is ready to draft the new ADP harness drawings, schematics, wire list and BOM. Gary will also be issuing part numbers for new parts and harnesses. 
- @Gary Angelus can start now, as long as we incorporate the changes from John and my review.  This can be tracked in the linked Jira task requested above.

## Plan

- Create list of tasks ranked in priority, summarize due dates, links to those tasks.
- Identify who will take over critical tasks and handoff to them.
- Confirm with them they are aware of and accepting the handoff.

## Issue Status

- Sightline Encoder to USB, FLIR camera tested and working.
- Sightline-Omron MIPI interface awaiting Sightline support.
- ADP harnesses in works.

## Comments (4)

### Cameron Chapman, 2024-12-26

@Rajesh Budhabhatti  please merge this list from doc with above statuses and stop using doc to prevent duplication
PTO or Leaving Handoff 
Raj’s task handoffs December 29-January 10. will be available 8-12 am everyday and checking my messages.
- Sightline RMA: I will ship the damaged 1750 board with proper RMA documentation. Board will be coming back when it is fixed.

- All SA Camera stuff is lined up in marked boxes in my office. I have boxes marked with supplier names such as Sightline, Boson, Omron IONODES etc. I will point them out to Grant so they can be easily located.

- Relevant documents are located in sharepoint here: https://jenaero.sharepoint.com/:w:/r/sites/EngineeringTeam/Shared%20Documents/Electrical/SA%20Camera%20Replacement/SA%20Camera%20evaluation.docx?d=w465b4a8f2d4e4739863121572df5dd84&csf=1&web=1&e=FBhfcG

- FLIR Camera is working. We needed an updated license which Sightline provided. Note that Boson 320 FLIR camera needs External power (5-15V). This is represented in the redlines that will be reviewed by Cameron Chapman. See here: ADP Harness redlines.pdf

 
SA Camera remaining tasks-12/19:
- Is John taking the handoff for these items? Have you called him to discuss and verify he understands the details and accepts the handoff? Yes, John and I are in daily contact. He is taking over the MIPI camera testing when we receive new firmware from Sightline

- Integrate Omron MIPI camera- Sightline received the camera and will provide us with updated software.
- When? How will they notify us when ready? Email the team? Yes, John and I are copied on the communication and well connected with Nick Whaley from Sightline.
- New Latency and Power measurements with Omron MIPI camera. Earlier tests used Raspberry Pi MIPI camera with 2.0 interface board.
- Image comparison: Depth of field, Viewing angel and low light operation.
- Test Boson FLIR with Sightline 1750 board and FLIR interface board. Done. Needed additional license. FLIR is working.
- Where are the setup and installation documents for these saved? Ex: how would someone know how to install the required HW and SW? They are saved on Sharepoint SA Camera folder here: Sightline Quick Start Guide.docx
-
- ADP Harness redlines and deliver it to CAD team for drafting. Done. Will scan and have Cameron review it.
- Please create a JIRA task and link for this. Attach redline to JIRA task. Will do.
- Work with Manufacturing for Micro D-sub and Molex Clamshell connector harness wiring. Done. Will have Cameron review it and give it to Gary for drafting.
- Is there a prototype build for this? Please attach photos to the cable task. Not yet. John is peer reviewing the redlines. After that I will send the redlines to you for your review.
- Fit check with new ADP housing
- Thermal analysis and measurement in new SA camera housing.
- Hand over a Sightline setup to Software team.
- Can you please do this before you leave? Discuss with Scott W who and record here. Yes. Will do.

### Cameron Chapman, 2024-12-26

FYI @Grant Goodman @John Gober . @Scott Whitney have we identified a GCS engineer to scope and perform the software work required to get these cameras working in our GCS? Can you please link a Jira task for that?

### Scott Whitney, 2025-01-08

@Cameron Chapman @Rajesh Budhabhatti  - I talked with @Grant Goodman about this. We likely do not need a GCS Eng at this time. The ADP needs to be setup on a HIL to do verification testing. As long as the Sightline board is configured correctly then the image should come through to the GCS.  
We can support the HIL setup if necessary, and if there are issues after the ADP is setup then we can support investigating a solution.

### Cameron Chapman, 2025-01-09

@Scott Whitney we can give it a shot, but if it is not straight forward, I think a GCS or FW eng would be a lot more efficient getting everything configured correctly. @Grant Goodman  mentioned this was the plan next week.

## Attachments (0)
