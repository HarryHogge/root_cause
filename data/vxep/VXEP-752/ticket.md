# VXEP-752: Integrate Amprius Heavy Payload Main Battery for Hatchet+AEWE demos and future use

- **Issue type:** Major Project
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-10-30
- **Updated:** 2025-09-26
- **Resolved:** 2025-07-15
- **Reporter:** Cameron Chapman
- **Assignee:** Scott Whitney
- **Creator:** Cameron Chapman
- **Links:** relates to FS2-2496 (Data Investigation Amprius Battery ); relates to VXEP-763 (Create endurance estimate); relates to FS2-2522 (B30+40: Implement 12V load shedding when vbatt gets too low or overcurrent detected. ); relates to FS2-2551 (Heavy Lift Battery Test support); relates to FS2-2570 (Heavy Lift Battery gcs.ini)
- **Project Tier:** Tier 2
- **LRR Desired Delivery Date:** 2025-03-01
- **LRR Required Delivery Date:** 2025-08-01

## Description

Confluence https://jenaero.atlassian.net/wiki/x/LgDeH 
Schedule https://jenaero.sharepoint.com/:x:/r/sites/ProgramManagement97/Shared%20Documents/a.)%20PROGRAMS/Lethal%20Integration/HvyLiftBattery%20Integration%20Schedule.xlsx?d=w154aa55df9f54e009f1a6210cb27c268&csf=1&web=1&e=1aEwYy 
Sharepoint: Battery_NextGenForward
Files: 30V HL Amprius Battery
JIRA https://jenaero.atlassian.net/browse/VXEP-752 
 
Munitions
All ITAR Data is here: Edge US Only Material - Weaponization - All Documents (sharepoint.com)
All non-ITAR data is here: Program Management - Lethal Integration - All Documents
 
Generic Test plan: Prototype Main Battery Test Plan.docx
Specific battery test plan
AA report. HPMB SN 8-0001 Test Report.docx
Action List: Action - Heavy Payload Main Battery.xlsx
FRR:
HPMB FRR.pptx

Requirements from Jeremy:
- Make any required GCS battery adjustments for the new battery.
- Confirm available payload weight.
- Provide max endurance estimate

- Provide limits and procedures for required battery level, wx, or other performance limitations.
- We shouldn’t need 2 flight hours for the integration nor demo flights.


Latest plan (updated 11/19, outdated now, needs an update)
- @Rodney Linch I think you should schedule ~3 times/week HPMB scrums until we ship. Do you think asking for proj engineering support would help track all of the things?
- We should keep this list updated as we progress.
- Review previous data. Define what is good enough. Scott W to coordinate this.
- Done. https://jenaero.atlassian.net/browse/FS2-2496 Summarize here. Seems like we should be able to make it accurate enough. Will verify with ground testing.
- Refine schedule.
- Shipping schedules and process are longer for prototype batteries.
- What is demo cadence (how many batteries should we ship?)
- Record battery delivery schedule. 2 initial.
- Send this to Rodney and Jeremy. Need to get more detailed schedule and manpower requests.
- Design Review and Test Planning
- Integration
- Ground testing. See here for summary https://jenaero.atlassian.net/browse/VXEP-779
- Ensure charger is labelled with charge settings and procedure. Charging will be accomplished with the X16 charger used for Havoc, and a charge harness will be supplied with this delivery.  Configuration settings should be set to 7S, 29.4V max voltage, 9A charge rate.
- SW scope (updated 10/31/24)
- Investigate AAR from previous flight
- Implement changes required
- Create Amprius Battery installer w/ updated .ini and GCS from LRR.
- If this is not ready before flight, we recommend dedicating a specific GCS to HPMB flights that will have settings specific to it. Label laptop appropriately.
- HIL testing
- https://jenaero.atlassian.net/browse/VXEP-783
- Flight Test
- Aircraft has been flying recently. Needs replaced ADP.  https://jenaero.atlassian.net/browse/VXEP-781 
- Should not need separate SCO flights.
- Test with full weight config full endurance. 
- Check previous flight test plan, abort limits, etc. 
- Update RTB and land immediately voltages for this battery. 
[embedded: image-20241118-191247.png]
- https://jenaero.atlassian.net/browse/VXEP-782 
- Manual says 20-32VDC. Custom harness regulator used was 9-36V. Payloads documented here. VXE Payload List.xlsx
- Ship to HSV for Orbital Integration testing by 1st week of December 2024
- Define battery qty: Minimum two (2) Batteries and one (1) Charger
- Need to verify customer payloads are compatible with Amprius voltage range, or determine test plan for using the 24V output.
- FLOPs only.
- Needs to be customer viewable by AEWE (January 28 -29, 2025)
- Process improvements.
- Always have a design review with all stakeholders prior to building things. 
- EX: a new battery needs review from aircraft engineering team.
- Define Success Criteria - Program Manager
- Define requirements (ideally based on metrics) - Product Owner, PM, PE
- Design improvements. 
- Include an adapter cable for the existing battery charger or cell logging replacement.

## Comments (7)

### Scott Whitney, 2024-10-31

@David Grosher @Rodney Linch @Cameron Chapman @Greg Fryer  - @Eric Brewer has completed the investigation. He comments from https://jenaero.atlassian.net/browse/FS2-2496 below

I reviewed the data and provided a suggested parameter update to resolve the jumps in state of charge. Thanks to @Everett Werner for some help as well.
Old vs. new with the param update is shown here:

[embedded: image-20241031-191830.png]

### Greg Fryer, 2024-10-31

Looks promising! Need to review (2nd set of eyes who knows how the data is used. @David Grosher or you can call it!) to declare good enough, or not - then firm up deployment plan (e.g. is this in custom GCS SW or do we start baking it in the finished product, or what).
@Jeremy White  It looks like a good chance at the simple adjustments working. Hopefully I didn’t just jinx us.

### Rodney Linch, 2024-11-01

[embedded: Prototype Main Battery Test Plan.docx]
@Connor Peebles , for everyone’s awareness, can you verify that we (SLO) will also conduct ESR testing and forgo Low Voltage Testing?

### Connor Peebles, 2024-11-01

@Rodney Linch You might have meant to tag Cameron Chapman?

### Jeremy White, 2024-11-01

All ITAR Data is here: Edge US Only Material - Weaponization - All Documents (sharepoint.com)
All non-ITAR data is here: Program Management - Lethal Integration - All Documents

### Cameron Chapman, 2024-11-05

Added to plan section
Tom Westrich Greg FryerEric Brewer  Cody SmisekI have the following questions and recommendations for the SLO ground testing plan. Let me know if you have answers or recommended changes. We can schedule a meeting if preferred. 
 
Questions
- How much of the curve do we want to validate with an aircraft discharge test?  ~lower 50%? What SOC can we ship at?
- Do we need to be able to climb at lower SOC, or just cruise?
- What is an average cruise load estimate of VXE30 at max weight? We should add this to confluence for future reference. https://jenaero.atlassian.net/wiki/spaces/EE/pages/11272193/Power+and+Temperature+Profiles 
- Average MB climb duration and load of VXE30 at max weight

 
Here are my recommended updates for this specific battery qualification: Prototype Main Battery Test Plan.docx
 
ESR Measurement section in aircraft ship voltage to 0% SOC. Load AA ESR measurement before the test.
- Validates AA testing and calculations as seen by the aircraft.

- Aircraft Low Voltage No Load Test-skip. IR test is more important.
- Aircraft Integrated Battery Test
- Recharge to ~10% SOC.
- Ramp throttle to 100% for 10 seconds.       This step is to verify max power at lower SOC.
- 500W VXE30 (750W havoc) until the battery reaches 0% SOC (define cell and pack cutoff voltage). This step is to ensure battery can support cruise loads at low voltage.
- Change 7.6 and 7.7 to have generic flight test recommendations, but indicate that a specific plan for each battery/project needs to be developed, documented, and approved by FRR.

 
Power and Temperature Profiles
Updated 2 months ago
Prototype Main Battery Test Plan.docx
 
Cameron Chapman added Jeremy Kostel to the chat and shared all chat history.
 
Hayden Jeanor and Jeremy Kostel please also review, let me know what you think, and determine who can be available for this testing (I think early next week)

### Scott Whitney, 2024-11-21

Added an update schedule as a link. The attachmend is static and not updated (i do not have the permissions to remove it)

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20241031-191830.png | image | 34 | 2024-10-31 | listed only |
| [Prototype Main Battery Test Plan.docx](attachments/24348_Prototype%20Main%20Battery%20Test%20Plan.docx.md) | docx | 368 | 2024-11-01 | converted |
| image-20241118-191247.png | image | 24 | 2024-11-18 | listed only |
| [HvyLiftBattery (as of November 20, 2024).xlsx](attachments/24622_HvyLiftBattery%20(as%20of%20November%2020,%202024).xlsx.md) | xlsx | 38 | 2024-11-20 | converted |
