# VXEP-1799: B30 VXE 820 Forced to use ELZ due to HLB being to low to VTOL land safely

- **Issue type:** Incident (8D)
- **Status:** D6 - Implementing Corrective Actions
- **Priority:** Highest
- **Created:** 2026-03-27
- **Updated:** 2026-10-08
- **Reporter:** Christopher Ridgard
- **Assignee:** Christopher Ridgard
- **Creator:** Michael Mohr
- **Labels:** Hardware, MOLSON, RCCA, Weekly-incident-tracker
- **Links:** relates to RMA-970 (VXE-820 RMA 260421-1); relates to VXEP-1794 (VXE 820 Fuel Cell not charging HLB in flight); relates to VXEP-1586 ( VXE 593 smoking fuel cell); relates to RMA-973 (D4500799 RMA 260421-4)
- **Customer:** MOLSON
- **Vehicle Tail Number:** VXE-820
- **Root Cause:** Cathode duct breaking creates conditions where the fan is unable to cool the stack causing failure.
- **Incident Type:** Aircraft Damage
- **Severity:** 3 - Degraded Performance - With Workaround
- **Executive Summary:** Michael L is reviewing report with Charles to provide to customer.

## Description

Upon going to land at the HLZ, there was not enough HLB power to safely VTOL recover. Switched to the ELZ and recovered with minimal damage to E140 on board.

## Vehicle Configuration

VXE-30
Adv Nav
Fuel cell
E140

## Corrective Action

Redesigning HGS0794 (cathode blower duct) to have a redundant retaining flange to keep duct in place in the event of failure of adhesive. @Christopher Ridgard  was this done? Does this apply to D450 or 900 as well?

## Plan

@Charles Sweet  working on report.  Report Provided
Jack W. provide dispo on composites Dispo Provided
@Zack Garcia @Mathew Papaleo Action disposition from Jack W.

## Issue Status

--Smisek writes (7/20/2026)---
xcomm file 129 in large data pull is data for incident flight. 
[embedded image-20260720-203927.png]
Suspect some type of stack failure. Awaiting confirmation from @Charles Sweet @Sean Wendling 
--END--

## Comments (39)

### Alexander Alan Arnold, 2026-09-21

@David Grosher Can we get a dispo of the aircraft. currently in the RMA rack. the fuel cell RMA was completed last month. @Greg Fryer also for dispostion request moving forward who should be our primary POC for these?

### David Grosher, 2026-09-21

@Alexander Alan Arnold Reading this incident, I dont think there is anything to disposition here for my team. I think following any repair the system should go through system checkout.

### Jeremy Kostel, 2026-09-23

Just took a quick look at the aircraft in RMA. Aircraft is mostly in tact with some minor cracks and damage to a lot of the composite structures. The structures team will need to take a look and make dispos. The electrical system looks good and is low risk of damage outside of one connector that will need repair. We can do system testing once ME team has dispo’d what needs to be taken apart. @Jack Waeschle are you able to take a look?
[embedded bfdc8e65-3fbe-4a89-ac20-68e023f97f18.jpg]
FYSA @David Grosher @Alexander Alan Arnold

### Jack Waeschle, 2026-09-23

@Jeremy Kostel I am remote today. Happy to take a look tomorrow or help find another ME to take a look today

### Jeremy Kostel, 2026-09-23

@Jack Waeschle Tomorrow will be fine, thank you!

### Jack Waeschle, 2026-09-24

Dispo is as follows:
Fuselage: 1 ply carbon fiber with MGS resin wet layup repair on inside surface (near the fuel tank boss, obvious crack on outside surface). Extend patch 0.5 - 1 inch past edge of crack. Remove tank star foam pad if needed before repair. Permissible to tape up loose cables and leave most electronics in fuse during repair, unless wet layups deems it unreasonable to do this repair without removing all electronics.
Tail Boom: remove and replace plastic saddle. Make sure to remove any loose pieces of plastic that may have fallen into internals of tailboom.
Horizontal and vertical stabilizers: Remove and replace thumb screws
All components: clean with isopropyl, touch up paint to level deemed cosmetically appropriate (Full paint booth would produce best appearance, but require significantly more component disassembly. Paint pen would cover the scratches, but it would be apparent where the paint had been touched up. Dealers choice! Mechanically, both paint methods are flightworthy).

### Drew Hildreth, 2026-09-24

@Jack Waeschle Thank you, Jack.

@Zack Garcia @Mathew Papaleo Please action the above dispo from Jack.

@Lauren Velasquez FYSA

### Drew Hildreth, 2026-09-24

Thank you for the report Charles.

@Alexander Alan Arnold @Scott Lovett Please review the above report and get something on the calendar to discuss.

### Alexander Alan Arnold, 2026-09-24

@Drew Hildreth Mike L is reviewing and working with Charles to clear up any questions in the report. @Michael Lindsay

### Mathew Papaleo, 2026-09-25

@Drew Hildreth we got the saddle bondment on the way and me and zack are working on the fuse traveler today for composites. will also get parts cleaned up with the new requested hardware. thanks @Jack Waeschle

### Michael Lindsay, 2026-09-28

@Alexander Alan Arnold Closing this ticket as this fuel cell has since been RMA’d and repaired see https://jenaero.atlassian.net/browse/RMA-973.

### Michael Lindsay, 2026-09-28

@Alexander Alan Arnold disregard this be for ticket, it was should of been for https://jenaero.atlassian.net/browse/VXEP-1586 which I linked.

### Lauren Velasquez, 2026-09-30

@Mathew Papaleo @Zack Garcia Did we get a RFQ sent for the scope of work?

### Zachary Mann, 2026-10-07

Is there any movement on this ticket? @Michael Lindsay

### Michael Lindsay, 2026-10-07

@Zachary Mann This is just waiting for the report to be reviewed and finalized prior to it being closed.

### Zachary Mann, 2026-10-07

@Michael Lindsay Great thank you!

### Christopher Ridgard, 2026-10-08

@Cameron Chapman, design update is being implemented via RDW-ECR0247.

### Cameron Chapman, 2026-10-08

@Christopher Ridgard Thank you. Will any assets need rework when that is released?

### Christopher Ridgard, 2026-10-08

No, @Cameron Chapman, I think we should make this a running change.

### Cameron Chapman, 2026-10-08

@Christopher Ridgard ok. Please close this when that ECR is released.

### David Grosher, 2026-09-21

@Alexander Alan Arnold Reading this incident, I dont think there is anything to disposition here for my team. I think following any repair the system should go through system checkout.

### Jeremy Kostel, 2026-09-23

Just took a quick look at the aircraft in RMA. Aircraft is mostly in tact with some minor cracks and damage to a lot of the composite structures. The structures team will need to take a look and make dispos. The electrical system looks good and is low risk of damage outside of one connector that will need repair. We can do system testing once ME team has dispo’d what needs to be taken apart. @Jack Waeschle are you able to take a look?
[embedded bfdc8e65-3fbe-4a89-ac20-68e023f97f18.jpg]
FYSA @David Grosher @Alexander Alan Arnold

### Jack Waeschle, 2026-09-23

@Jeremy Kostel I am remote today. Happy to take a look tomorrow or help find another ME to take a look today

### Jeremy Kostel, 2026-09-23

@Jack Waeschle Tomorrow will be fine, thank you!

### Jack Waeschle, 2026-09-24

Dispo is as follows:
Fuselage: 1 ply carbon fiber with MGS resin wet layup repair on inside surface (near the fuel tank boss, obvious crack on outside surface). Extend patch 0.5 - 1 inch past edge of crack. Remove tank star foam pad if needed before repair. Permissible to tape up loose cables and leave most electronics in fuse during repair, unless wet layups deems it unreasonable to do this repair without removing all electronics.
Tail Boom: remove and replace plastic saddle. Make sure to remove any loose pieces of plastic that may have fallen into internals of tailboom.
Horizontal and vertical stabilizers: Remove and replace thumb screws
All components: clean with isopropyl, touch up paint to level deemed cosmetically appropriate (Full paint booth would produce best appearance, but require significantly more component disassembly. Paint pen would cover the scratches, but it would be apparent where the paint had been touched up. Dealers choice! Mechanically, both paint methods are flightworthy).

### Drew Hildreth, 2026-09-24

@Jack Waeschle Thank you, Jack.

@Zack Garcia @Mathew Papaleo Please action the above dispo from Jack.

@Lauren Velasquez FYSA

### Drew Hildreth, 2026-09-24

Thank you for the report Charles.

@Alexander Alan Arnold @Scott Lovett Please review the above report and get something on the calendar to discuss.

### Alexander Alan Arnold, 2026-09-24

@Drew Hildreth Mike L is reviewing and working with Charles to clear up any questions in the report. @Michael Lindsay

### Mathew Papaleo, 2026-09-25

@Drew Hildreth we got the saddle bondment on the way and me and zack are working on the fuse traveler today for composites. will also get parts cleaned up with the new requested hardware. thanks @Jack Waeschle

### Michael Lindsay, 2026-09-28

@Alexander Alan Arnold Closing this ticket as this fuel cell has since been RMA’d and repaired see https://jenaero.atlassian.net/browse/RMA-973.

### Michael Lindsay, 2026-09-28

@Alexander Alan Arnold disregard this be for ticket, it was should of been for https://jenaero.atlassian.net/browse/VXEP-1586 which I linked.

### Lauren Velasquez, 2026-09-30

@Mathew Papaleo @Zack Garcia Did we get a RFQ sent for the scope of work?

### Zachary Mann, 2026-10-07

Is there any movement on this ticket? @Michael Lindsay

### Michael Lindsay, 2026-10-07

@Zachary Mann This is just waiting for the report to be reviewed and finalized prior to it being closed.

### Zachary Mann, 2026-10-07

@Michael Lindsay Great thank you!

### Christopher Ridgard, 2026-10-08

@Cameron Chapman, design update is being implemented via RDW-ECR0247.

### Cameron Chapman, 2026-10-08

@Christopher Ridgard Thank you. Will any assets need rework when that is released?

### Christopher Ridgard, 2026-10-08

No, @Cameron Chapman, I think we should make this a running change.

### Cameron Chapman, 2026-10-08

@Christopher Ridgard ok. Please close this when that ECR is released.

## Attachments (11)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 820 Full Data Pull.zip | archive | 88889 | 2026-06-03 | listed only |
| T115_V820_260326_163407_pack.zip | archive | 477 | 2026-07-02 | listed only |
| image-20260720-195922.png | image | 144 | 2026-07-20 | listed only |
| image-20260720-200753.png | image | 51 | 2026-07-20 | listed only |
| image-20260720-203927 (4236a9dd-cc73-4a2f-8661-7ecc0a3bf8ce).png | image | 197 | 2026-07-20 | listed only |
| image-20260720-203927.png | image | 197 | 2026-07-20 | listed only |
| image-20260722-163149.png | image | 159 | 2026-07-22 | listed only |
| image-20260827-154241.png | image | 105 | 2026-08-27 | listed only |
| image-20260827-170450.png | image | 403 | 2026-08-27 | listed only |
| [VXEP1799 RCI Presentation.pptx](attachments/64503_VXEP1799%20RCI%20Presentation.pptx.md) | pptx | 10138 | 2026-09-11 | converted |
| bfdc8e65-3fbe-4a89-ac20-68e023f97f18.jpg | image | 37 | 2026-09-23 | listed only |
