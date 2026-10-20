# VXEP-485: Electrical Drawing updates: Update electrical harness drawings to latest standards and resolve common issues

- **Issue type:** Major Project
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-05-12
- **Updated:** 2025-11-10
- **Resolved:** 2025-05-21
- **Reporter:** Cameron Chapman
- **Assignee:** Christa Meck
- **Creator:** Cameron Chapman
- **Labels:** 8-28-Sprint
- **Fix versions:** 11/10/2025
- **Links:** relates to ENG-1725 (Adding dummy pins to procedures and checks on travelers and eng docs); relates to VA-91 (E3 Software Implementation and training); is blocked by VA-91 (E3 Software Implementation and training); relates to ENG-1808 (Using heat shrink on top of wire insulation in crimp contacts (JST contacts)); relates to ENG-1865 (107-102275 Vertical Servo Boost Drawing Updates needed); relates to ENGINF-293 (Document and train EEs for electronics part and build standards. ); relates to VA-324 (107-103302 Current Sense Harness, create E3 drawing); relates to VA-325 (107-101710 Center Wing Power Cable, create E3 drawing); relates to VA-333 (107-102065 VXE30 Center Wing Cable, create E3 drawing); relates to VA-334 (107-102066 ADP Harness, create E3 drawing); relates to VA-335 (107-102094 Boom Power Harness, create E3 drawing); relates to VA-336 (107-102095 Boom Signal Harness, create E3 drawing); relates to VA-337 (107-102291 Nose Signal Harness, create E3 drawing); relates to VA-347 (107-103302 Current Sense Harness, review/release E3 drawing); relates to VA-355 (107-101710 Center Wing Power Cable, review/release E3 drawing); relates to VA-356 (107-102065 VXE30 Center Wing Cable, review/release E3 drawing); relates to VA-357 (107-102066 ADP Harness, review/release E3 drawing); relates to VA-358 (107-102094 Boom Power Harness, review/release E3 drawing); relates to VA-359 (107-102095 Boom Signal Harness, review/release E3 drawing); relates to VA-360 (107-102291 Nose Signal Harness, review/release E3 drawing); relates to VA-202 (Create, peer review, and release E3 drawings); relates to VA-214 (Prioritize and manage list of assemblies that need E3 drawings); relates to XEO-209 (107-102275 Servo Boost, Vertical Missing Label Location); relates to XEO-203 (107-102280 Servo adapter procedure does not match BOM); relates to ENG-1998 ( PN 107-102281 CABLE ASSEMBLY documentation Improvements); relates to VA-607 (107-102275 Servo Boost Assembly, Vertical, review/release E3 drawing); relates to VA-608 (107-102281 Servo Adapter, Horizontal, review/release E3 drawing); relates to VXEP-329 (Updates to VXE30 System Architecture Diagram); relates to ENG-3682 (Improve EE checklists, design review process, etc. Ensure everyone uses them )
- **Production Stakeholder:** Ryan Ferguson
- **Other Stakeholder (as required):** Matt Philley

## Description

Drawing update status: E3 Drawings List.xlsx (sharepoint.com)

@Kelly J Furlong @Ryan Ferguson @Matt Philley @Liam Limon @Connor Peebles what do you think of the following plan to start updating all of our harness drawings to the latest standards?  
Latest plan here (Web view), copied below. 
Dan project order
- Define standard https://jenaero.atlassian.net/browse/ENG-1743 
- Define default harness tolerances ENG-1914: Develop harness default tolerance guides. ASSIGNED
- Start according to drawing order.


Drawing Order List
- Sort JIRA issues assigned to you by priority. https://jenaero.atlassian.net/issues/?filter=10148
- Look at JIRA issues assigned to Nadia or Cameron dealing with documentation things.
- We should start using a JIRA tag documentation.
- Using this list, sort cables (column F) by the following, drawing+bom(col q) missing first, needs update second, start with high risk.

Electronics Dept PN and Documentation Review.xlsx
 
Process
- Run through this process once. Working with @Cameron Chapman, create ideal drawing standard to be applied to the remaining one.
- See task [ENG-1721] Update electrical harness drawings to latest standards and resolve common issues - Jira (atlassian.net)
- Create a JIRA Engineering Change Issue for each electrical cable/harness with the following format.
- PN Desc documentation improvements.
- Ex: 107-102264 DUAL CURRENT SENSE, ASSEMBLY documentation improvements.
- Priority: Lowest by default. Make higher if known issues (ex: parts missing, antispark pins unclear).
- Use the checklists here while you are working on, or improving drawings. Please add checks as you run across them. We should create a new tab for E3 drawings. EE Checklists.xlsx
- Search JIRA for the same PN (ex: 107-102264). Link any issues that may be resolved at the same time with the drawing. Attempt to resolve with the same release.
- Ask @Kelly J Furlongand @Ryan Ferguson of any known issues with the part. They can forward question if preferred.
- Update drawing. Send to EE for review (thinking @Garrett O'Neill for now, but not final). Garrett, please also ensure steps 2-4 are complete.
- Change improvement to engineering change and process. I think most will be level 0 changes. Ok to release if so, release after CCB if not. See here. https://jenaero.atlassian.net/wiki/spaces/EF/pages/13008930/How+To+Release+an+Engineering+Change

 
 
 
Things to update on old Harness drawings
- Update to latest template. (using the Altium or SW template file)
- Replace tough seal. Hold on drawing update if a replacement has not yet been approved.

ENG-467: Safety Hazard - Alternate Potting Adhesive for Tough Seal Product Line NeededIN PROGRESS
- Replace twisted wire with bundles. https://jenaero.atlassian.net/browse/ENG-292
- Replace old band with new.

XEO-284: Band-It Change to Tie-Dex BandsIN PROGRESS A31186 bands rather than the older SCPSE-03 bands
- Add EA PNs. Add note to templates that Mfr PNs are for reference only. Update to latest templates.
- Remove mfr PNs from drawing. Should only be on BOM as reference only.
- If necessary, and the Drawing is too crowded, move BOM to another sheet.
- Change designators from text to numbers. Update notes accordingly.
- Missing dummy pins. Usually included in every connector. If not including them on purpose, a note should say so.

## Comments (15)

### Cameron Chapman, 2023-05-12

@Greg Fryer starting a plan here

### Thomas McMillan, 2023-05-25

@Matt Philley @Emalee Johnson  new ticket linked above.

### Cameron Chapman, 2023-06-30

@Sam Omiotek @Jeremy Roberson see this ticket for drawing improvement process. See Process in description

### Dan Marano, 2023-08-08

@Cameron Chapman Is there a defined drawing order yet?

### Cameron Chapman, 2023-08-08

See above. 
Drawing Order
- Sort JIRA issues assigned to you by priority. https://jenaero.atlassian.net/issues/?filter=10148
- Look at JIRA issues assigned to Nadia or Cameron dealing with documentation things.
- We should start using a JIRA tag documentation.
- Using this list, sort cables (column F) by the following, drawing+bom(col q) missing first, needs update second, start with high risk.

Electronics Dept PN and Documentation Review.xlsx

### Cameron Chapman, 2023-08-24

Linking subtasks to parent

### Cameron Chapman, 2023-09-13

Good afternoon @Garrett O'Neill and @Dan Marano . Can you please send me a link to your tracker sheet and add it to the description here? Please also ensure you update the various JIRA tasks with in progress, complete, and log hours

### Dan Marano, 2023-09-13

Tracker attached

### Cameron Chapman, 2023-09-13

Drawing update status: E3 Drawings List.xlsx (sharepoint.com). Please update to latest status and keep updated, then tag @Ryan Stafford when the sheet is updated for tracking.

### Dan Marano, 2023-09-13

@Cameron Chapman as for updating the Jira tasks, as I have moved on to a new cable design, should we create a task for cable 107-102275? This formboard and schematic is just about complete, just ironing out some details now.

### Cameron Chapman, 2023-09-13

@Dan Marano it looks like there already is a problem issue for that one, so the action would be to move it to the VA project and change it to a task type issue.

### Dan Marano, 2023-09-13

[embedded file]
@Ryan Stafford Good day! Please see the latest status of our cable drawings in E3. This included schematics, formboard drawings, and BOMS. In the process of creating cables, parts are also being created and added to the library for usage on other cables as well. Those parts can all be viewed in E3, in the “Edge Harness Builder” library.

### Cameron Chapman, 2024-04-10

@Ryan West Jimenez this is your main project second in priority behind any urgent production support tasks. Please coordinate with Garrett first and me if he does not have bandwidth currently.

### Christa Meck, 2025-05-21

@Daniel Lavallee you changed the status on this ticket in March, 2025.  Still relevant?

### Daniel Lavallee, 2025-05-21

@Christa Meck I completed a few of the related tickets but not it looks like there are a few in progress that I have not been a part of. I think we can close this ticket.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [E3 Drawings List.xlsx](attachments/16234_E3%20Drawings%20List.xlsx.md) | xlsx | 19 | 2023-09-13 | converted |
