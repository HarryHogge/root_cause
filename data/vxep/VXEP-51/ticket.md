# VXEP-51: Internal - Aircraft 450 VTOL Landing Crash - ESC soft start

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-07-27
- **Updated:** 2025-05-21
- **Resolved:** 2025-05-21
- **Reporter:** Cameron Chapman
- **Assignee:** Cameron Chapman
- **Creator:** Cameron Chapman
- **Labels:** 8-28-Sprint, MARSOC
- **Links:** is duplicated by VXEP-44 (VXE-450 VTOL Landing Crash); is blocked by VA-309 (VXE450 Hands on troubleshooting. Identify root cause); is blocked by VA-310 (VXE450 Review root cause and document Corrective Actions); is blocked by VA-311 (VXE450 Implement Corrective Action: Eng create inspection guidance for MOSFETs. 107-102974 Lift ESC Assembly ); is blocked by VA-491 (VXE450 Implement CA: Production update traveler to include inspection.); is blocked by VA-492 (VXE450 Implement CA: Quality to create inspection document per Eng input.); relates to FS2-755 (ESC Check prior to VTOL transition); causes VXEP-480 (Create Master Document for Quality: IPC-A-610, IPC-A-620 Conformances and Engineering Deferrals/ Deviations); relates to VA-363 (Aircraft 450 VTOL Landing Crash); is blocked by VA-851 (VXE450 Implement CA: Proposed Lift ESC Board Updates); is blocked by VXEP-198 (VXE450 Implement CA: Procurement Evaluate/Order new datecode FDMS86540 MOSFETs (IPN: 100-110341))
- **Sprint:** VXE-1 EE Team Sprint 8/28-9/17
- **Customer:** MARSOC
- **Vehicle Tail Number:** 450
- **Plan:** In review
- **Incident Type:** Aircraft Loss
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

This issue is for internal troubleshooting efforts. 
Customer visible issue: https://jenaero.atlassian.net/browse/VIT2-327 
Live Customer visible copy:  Vehicle Investigation V450 V2.pptx. 
Internal only visible copy: VIT2-237 VXE 450 - VTOL Landing Crash.pptx

Aircraft was participating in operator training at Camp Lejeune NC. It was in the fuel cell configuration with a Trillium HD55 payload. This was the second flight on this day. During the LW the ground crew indicated that the right front lift motor sounded different during the spin-up checks. The check was repeated several times and determined to be fine. The launch was uneventful. Per the flight profile, at around twenty minutes into flight the aircraft was commanded to RTB. The aircraft transitioned to vertical flight and then continued to drift past the programmed LZ toward the south. Attempts to nudge the aircraft back to the LZ produced no effect. The aircraft was placed in manual nudge which also produced no effect. At some point the aircraft dropped suddenly to the ground.
The crash site was isolated from the flying field by dense woodlands and had to be accessed by boat. Reports from the site were the aircraft was entirely consumed by fire. The center wing was recovered from within the trees.
Pictures and AAR data are not available until released by the customer.
Centerwing was spares CW SN 4008
Surviving Lift ESC Assy (Front Right) 107-101631-2 SN 069

## Corrective Action

- https://jenaero.atlassian.net/browse/VA-851
- https://jenaero.atlassian.net/browse/VA-311
- https://jenaero.atlassian.net/browse/FS2-755
- https://jenaero.atlassian.net/browse/VA-221
- https://jenaero.atlassian.net/browse/VXEP-198

Tertiary CA as a ‘nice-to-have’:
- https://jenaero.atlassian.net/browse/VA-640

## Issue Status

- Motor [& ESC] sounds like it was damaged before this flight. “During the LW the ground crew indicated that the right front lift motor sounded different during the spin-up checks.”
- In the video, it looks like the front right motor does not activate during attempted transition to descent.
- Data review found the autopilot commanded correctly, but front right motor did not respond.
- Inspection of the remaining hardware found anomalies in the front right Lift ESC assembly that could not be a result of the crash.
- MOSFET Q20 found detached from solder pad, suggesting breakdown and then solder melting from high heat.
- Failure from the MOSFET then caused the 5V regulator, U1, to be destroyed, which then rendered the ESC inoperable

## Root Cause

- MOSFET Q20 found detached from solder pad, suggesting breakdown and then solder melting from high heat.
- Failure from the MOSFET then caused the 5V regulator, U1, to be destroyed, which then rendered the ESC inoperable

## Comments (14)

### Cameron Chapman, 2023-07-27

@Greg Fryer @John Clark @Sam Miller @David Grosher @Connor Peebles @Laszlo Juhasz 
Here is the internal issue to track 450 troubleshooting. Please use this for ongoing troubleshooting and status. @Pat Wells will update the customer visible one periodically to ensure they see we are making progress. 
@Connor Peebles, can you please update the fields above with our current status, plan, actions, etc. 
Notes from the meeting. Holding on posting this to JIRA until we sort out LM visibility questions. We can create an internal issue to track if helpful. 
Actions
Data review
a.	Add timeline, series of events. Line up physical report with data. Establish template?
b.	Get everything on the same time reference. Show events on plots.
c.	Was there any current spikes during fixed wing mode. Thinks no, can double check. 
Test
- Desolder motor and test in place.
- Inspect underside of board.
- Recreate damage with startup.
- Test changing capacitance.

Cause theories and corrective actions. 
- FET got so hot that it disconnected the bulk capacitor leads, which removed power from the ESC.
- Transients from motor operation.
- What fixes can we implement with current hardware/firmware?
a.	Can we help with ramp rate.
b.	Laszlo to add more.
- Fixes for future hardware.
a.	New ESC.
b.	Prevent shoot through.
- Old component/suspect sourcing and storage.
- Check current inventory.
- Add inspections to assembly process?
- Old PCB manufacturer was not as detail oriented in assembly and inspection. New mfr SPM catches such issues, has reported poor solderability, fixed other things. Could be due to rusty leads, age, suspect sourcing.
- Corruption of ESC firmware. Application note-Controller not recommended for motor controller.
- Have proven in one case, reprogramming fixed issue.
- Can add CRC to vtol controller to prevent corrupt firmware.
- Should disable spin, bad motor tone would also help. Could point the prop the wrong way.
- Would Temperature sensor or hall effect sensor help with controls?
- Flawed design. Unsure of where it came from, probably open source ESC. Hard to ensure each soft start fet carries the same amount of current.

Corrective actions not relevant to specific causes. 
- List potential causes and what we do about for each.
- Add esc feedback.
- Motor test in the air. Measure expected vs actual current. If it doesn’t pass, move to glide landing.
a.	What does land immediately do if lift motors not working.
- Customer button to attempt glide landing or go around.

### Connor Peebles, 2023-07-31

@Pat Wells (writing down a question from last Thursday) From Dan Lloyd; he is adamant that V450 does not have 261 flights and that sounds true according to these logs, but what I am hoping we can ask the customer (tactfully) is how frequently they swap vehicle LRUs - like the booms - between tail numbers. 

You can see in this log that V450 has few flights compared to V438. V438 has quite a high flight count. I am wondering if they were using the booms from V450 on V438 at some point, perhaps while attempting to adhere to the 150 flight cycle limit on the booms that is in the maintenance manual.

[embedded file]

### Cameron Chapman, 2023-08-03

@Connor Peebles , thanks for the great work. Can you please add ideas of how to test each of your theories to investigation plan?

### Cameron Chapman, 2023-08-24

Linking subtasks to parent

### Cameron Chapman, 2023-10-04

10/4 meeting notes. 
- Add to ppt, timeline of what you think happened. List where supporting information/slide.
- Can we do anything to prevent
- With current ESCs and firmware changes.
- Current ESCs with new components/reasonable skywire.
- Future ESCs. Record changes we should make, but will likely replace with brand new ESC
- Record anyt
- Story to customer. Statistical argument that it is infrequent. List other corrective actions.

### Pat Wells, 2023-10-18

@Cameron Chapman  was the ppt ever updated since your notes on 10/4?  I don’t see the statistical argument that we discussed.

### Cameron Chapman, 2023-10-18

It was not. @Connor Peebles is assigned to troubleshoot this, but has been diverted to other projects. https://jenaero.atlassian.net/browse/VA-309

### Connor Peebles, 2023-10-18

I’ll attempt to update the ppt shortly

### Connor Peebles, 2023-11-20

@Cameron Chapman Please review this Incident Investigation and the Internal Report VIT2-237 VXE 450 - VTOL Landing Crash.pptx. I believe we are ready to move on from D4 for this incident.

### Cameron Chapman, 2023-11-21

@Connor Peebles great work. 
- Are the Q20 FETS obsolete? If so, we should state that in the ppt. If not, should we order some with newer date codes?

Other than that, I think this is ready to move to implementing CA.

### Cameron Chapman, 2023-11-21

@Pat Wells would you like @Connor Peebles to update the LM visible version of this ticket with the information here, or would you like to? https://jenaero.atlassian.net/browse/VIT2-327

### Pat Wells, 2023-11-21

@Cameron Chapman  please have @Cameron Chapman update the LM visible ticket and include any additional narrative he feels necessary with the final investigation report.  Thank you for wrapping this up Connor.

### Connor Peebles, 2023-11-21

@Cameron Chapman Thanks,
- The FETs are available and active, see here: https://www.onsemi.com/products/discrete-power-modules/mosfets/FDMS86540
- We have ~1,400 boards-worth of them in our stock now. (we would be effectively scrapping that many?)
- I recall Procurement had some trouble with this chip, don’t recall the trouble. Probably Chip Shortage related.
- It is probably worth it to have procurement contact Onsemi directly and ask for newest datecode chips, and get procurement's past perspective on these.
- I’ll make a CA task for these things and get procurement to work them. https://jenaero.atlassian.net/browse/VXEP-198

And I’ll update the LM visible ticket. - I excluded links to some CA’s, particularly the one mentioning xkit

### Cameron Chapman, 2023-11-21

Responding to Connor in the subtask.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20230726-215659.png | image | 32 | 2023-07-31 | listed only |
