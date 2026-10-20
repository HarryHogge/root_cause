# VXEP-39: TPTR-54 minor cut/graze caused during the removal of a HLB

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2023-08-23
- **Updated:** 2025-08-05
- **Resolved:** 2025-08-05
- **Reporter:** Allen Gardner
- **Assignee:** Hans Hershberger
- **Creator:** Allen Gardner
- **Links:** relates to ENG-1344 (Top Cutout Battery Area Enlargement Investigation); relates to VA-384 (Review manuals for HLB demating procedure and cautions about sharp edges. Add to manual if none exist. ); relates to VA-385 (Summarize options and status of changes to prevent cuts from fuselage when demating batteries. ); relates to VA-386 (Evaluating adding demating tool for power connectors to customer kits. )
- **Incident Type:** Squawk
- **Severity:** 4 - Annoyance
- **Impacted Disciplines:** Hardware, Training, Maintenance
- **Impacted Core Subsystems:** Aircraft

## Description

an individual had a minor cut/graze caused during the removal of a HLB when coming in to contact with the edge of the fuselage.

## Issue Status

Shah, Dhruti (UK) - Mon Jul 10 21:41:45 BST 2023 : Vendor PTR-B 10/7/23: No current solution to this issue. Potential inclusion in the manual for a procedure to remove the battery out of the fuselage

## Comments (10)

### Allen Gardner, 2023-08-24

@Cameron Chapman please create a task within VA to investigate the source of the cut/graze and create a corrective action plan. Perhaps it is as simple as a notation in the ops manual to be careful with certain operation.  Even if this is something super simple, let’s move on this one quickly. Should be an easy win.

### Matt Philley, 2023-08-28

FYSA this issue was brought up internally as well. We coordinated to enlarge the cutout for the fuselage to improve access and hopefully reduce the tendency for folks to run their hand into the edge of the fuse during battery disconnect. This was incorporated into the new fuse config, but that is still going thru first-articles so we have not tested it yet. 
https://jenaero.atlassian.net/browse/ENG-1344 

Additionally we have purchased a tool for SCO Flight Test to de-mate the connector so folks dont run their hand into the fuse during the initial “break loose” so if whoever investigates this connectors with Flight Test they should show you that.
[embedded file]

### Cameron Chapman, 2023-08-29

Thanks Matt for the the information and your work on this issue. I will link follow up tasks. 
@Hans Hershberger I remember someone evaluating padding on the sharp edge. How did that effort turn out? Not flush when the center wing is installled?

### Matt Philley, 2023-08-29

@Cameron Chapman sure thing
We did test a 3d printed bumper strip, but it caused interference with the centerwing even when it was extremely thin. If we implemented a bumper it would have to be something temporarily installed just for the insertion of the battery… Flight Test was not fond of that idea so I dont think they have been using it after testing.
Jeremy was most involved from Production Engineering.

### Jeremy Roberson, 2023-08-29

@Matt Philley @Cameron Chapman @Hans Hershberger https://nam10.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.harborfreight.com%2Fpanel-clip-pliers-63699.html%3Fccdenc%3DeyJjb2RlIjoiMTA1MDI5NDkiLCJza3UiOiI2MzY5OSIsImlzIjoiNi4yOSJ9%26utm_source%3Dgoogle%26utm_medium%3Dcpc%26utm_campaign%3D20361715379%26campaignid%3D20361715379%26utm_content%3D154770257481%26adsetid%3D154770257481%26product%3D63699%26store%3D%26gclid%3DEAIaIQobChMI9cnFi4mPgAMVUAOtBh36fQZ5EAQYASABEgLKgfD_BwE&data=05%7C01%7Cjroberson%40edgeautonomy.io%7C37332e58a97c4b672c7108db86c77789%7C1876f61a3bdb4843ae7075ed0ccb7404%7C0%7C0%7C638251963494012652%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=KFL%2BxAXxhnEzU6v2VEKQ9Yik9D0TGLZai1WwxOPsuIk%3D&reserved=0

### Hans Hershberger, 2023-09-07

I’m going to put a hold on the investigation of this issue until the new fuselage (with enlarged top cutout) is rolled in so we can have an accurate datum to measure from.

### Hans Hershberger, 2024-09-11

@Greg Fryer Do we know if this is still a reported issue with the enlarged (for epsilon) upper payload cutout (like where the lift battery is installed, etc.)?

### Greg Fryer, 2024-09-11

@Hans Hershberger Good question! Check with @Matt Weber , We discovered that fuselages were SUPPOSED to have been changed to have a longer opening, but that had not actually gotten implemented.
(This is the thing we discovered while editing the top opening during expanded payload bay - the rear of the opening should not have been impacted, but in actual cutting we were making the openings longer.)

### Hans Hershberger, 2024-09-11

@Greg Fryer Thank you for the information sir!

### Christa Meck, 2025-08-05

Closing this incident as it’s from August 2023 and any investigation is likely done at this point.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IMG_0273.MOV | video | 8058 | 2023-08-28 | listed only |
