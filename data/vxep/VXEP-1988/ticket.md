# VXEP-1988: VXE 1014 Inccorect altitudes entered during LW led to crash

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** Highest
- **Created:** 2026-09-03
- **Updated:** 2026-10-19
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** RCCA, Software, Training, Weekly-incident-tracker
- **Links:** relates to RMA-1103 (VXE-1014 RMA 260909-1); relates to VXEP-2006 (VXE 1013 Glide landed while PLZ was selected)
- **Customer:** ARMY_Cyber
- **Vehicle Tail Number:** VXE 1014
- **Vehicle Configuration:** VXE 30 ADV NAV ,OGCS 1.4.2, Battery, E95
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical
- **Executive Summary:** Investigating RC of incident

## Description

Operator states that RF motor did not engage after passing IP5. Operator states that other 3 motors appeared to be engaged as reported by ground crew. VXE 1014 failed to arrest descent and flew into a tree. 
Awaiting FDR and pictures of incident

## Corrective Action

Airworthiness directive for vehicles flying with airdata v3001 software but no fix for the altitude estimation issue in the autopilot avionics.

## Plan

- Determine what version airdata board was installed on the vehicle
- Recommend issuing airworthiness direction to implement pause after long climbs or descents to allow altitude measurement to stabilize
- Engineering to perform testing in order to provide a recommendation

## Issue Status

Identified altitude estimation error that caused vehicle to transition at <50' AGL.
Working to confirm airdata board version used in this aircraft
Stil lnvestigating what caused apparent stall during fixed-wing flight (unrelated to incident)

## Root Cause

Root cause appears to be altitude estimation error resulting in transition occurring at <50' AGL.  Investigating if known issue with airdata board is the culprit of the altitude estimation error.

## Comments (15)

### Everett Werner, 2026-09-03

Tag me please when data is available

### Alexander Alan Arnold, 2026-09-04

@Eric Brewer @Everett Werner @David Grosher AAR is uploaded please let me know what else you would like to me retrieve from customer if logs are not enough UPDATE i am aware the the VTOL logs are missing i have already reached out to customer.

### Eric Brewer, 2026-09-04

@Alexander Alan Arnold thanks.  The VTOL logs are not present in the AAR, are you able to get them?

### Jackson Riley Curvin, 2026-09-04

@Everett Werner @Eric Brewer @David Grosher  the ftp data is loaded.

### Alexander Alan Arnold, 2026-09-04

@Eric Brewer jack just got off the phone with the customer and loaded the FTP

### Pat Wells, 2026-09-04

Could we please update the plan fields above @Eric Brewer

### Eric Brewer, 2026-09-04

@Pat Wells updated, let me know if you have questions.  We’re still confirming a few things but looks like we have a pretty strong reason to believe we have identified the culprit.

Just FYI I am out of office next week supporting a test event, so @Everett Werner will be picking up the investigation next week.

### Alexander Alan Arnold, 2026-09-09

@Ted Trowbridge can we get the ticket updated to reflect your discoveries from yesterday?

### Ted Trowbridge, 2026-09-09

The most likely workflow that caused this was probably an attempt to edit 300 and make it 200
If you were to select and delete the 3 in 300 the value is immediately parsed/coerced so the text turns into 0 rather than 00.  The cursor also shifts to the end of the entry, so if you type 2 you are just left with 2 feet.
Moving quickly through launch steps may prevent an operator from noticing.
Both of these issues are fixed in 1.4.3 & 1.4.4.  The text doesn't immediately get coerced into a number AND the field is highlighted red and you must enter a value between 100 and 500

### Drew Hildreth, 2026-09-09

Still no response from the Customer in REF: RMA Request Forms. RMA # will be issued once forms are received. RMA Team checked in yesterday, as well as the PM.

@Pat Wells FYSA

### Pat Wells, 2026-09-09

@Drew Hildreth @Alexander Alan Arnold @Scott Lovett is the plan, root cause, and CA listed above still correct?  Are we still investigating those issues or do we need to move forward with report and customer notification, CA, etc?

### Cody Smisek, 2026-09-16

@Eric Brewer  Regarding stall in flight. I inspected the horizontal stab, nothing obvious stood out. Powered aircraft and observed current elevator trim position, it was aligned with trim sticker. Used OGCS surface step to move elevator servo, no obvious failures or misalignment. 
Spoke with Matt P regarding the previous B40 servo issues to see if there were any ideas for inspections for this B30 aircraft. Given the abnormal situation that occurred coinciding with the pitch trim changes in flight, may be worth going through the Pegasus servo check for the hall effect sensor just to be sure. 
Could potentially swap servos with a new one and keep the old one to expedite that aspect of the investigation without delaying the return of the equipment.

### Mathew Papaleo, 2026-10-19

@Cody Smisek as far as a dispo goes for 1014, the fuselage case parts look to be in good shape, while the wing components are either totalled or in bad shape. can you help us dispo what needs to be replaced?

### Cody Smisek, 2026-10-19

@Mathew Papaleo Please coordinate with the ME group. @Sanjay Menon @Jack Waeschle

### Jack Waeschle, 2026-10-19

@Mathew Papaleo Dispo is as follows:
Center Wing: Glue fresh 1/4-20 heatset inserts into right end rib with Hulk adhesive. Surface prep plastic however possible with isopropyl alcohol and sanding/scratching up the surface for roughness. Glue crack in end rib and skin with hulk. After structural repair, permissible to use standard composites finishing practices to smooth out repair area and then touch up paint. On left side of center wing, remove alignment pin, wax threads and pin and reinstall, then wipe hulk adhesive into crack and delam between carbon skin and plastic insert. Permissible to wick thin CA into delam before completing hulk repair. Post cure, remove waxed alignment pin, clean area and replace with fresh alignment pin.
Left Wingtip: if cosmetic standards are low, it would be possible to repair the large tear in the kevlar near the servo pocket with hulk. For most resilient waterproofness and cosmetics, I recommend a full replace of the wingtip. Electronics are likely perfectly reusable though.
Right Wingtip: Replace
Left Boom: Replace
Right Boom: Clean, touchup paint with paint pen, replacing fwd motor cowling, replace both lift blades, replace screws on power connector, replace 1/4-20 nylon bolts and retaining washers
Spar joiner tube(s): Replace both
Fuse: Remove and replace fwd blades.
All other components remain mechanically flightworthy.

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V1014_B30N_20260903T173511Z.zip | archive | 45758 | 2026-09-04 | listed only |
| AAR_V1014_B30N_20260904T134609Z.zip | archive | 48328 | 2026-09-04 | listed only |
| Photos-20260904T144518Z-1-001.zip | archive | 25328 | 2026-09-04 | listed only |
| VTOL-20260904T144508Z-1-001.zip | archive | 30268 | 2026-09-04 | listed only |
| XCOMM-20260904T144327Z-1-001.zip | archive | 9905 | 2026-09-04 | listed only |
| [frontend-logs-2026-09-04T14-00-41-687Z.txt](attachments/64432_frontend-logs-2026-09-04T14-00-41-687Z.txt.md) | text | 25 | 2026-09-04 | converted |
