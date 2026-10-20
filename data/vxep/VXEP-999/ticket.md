# VXEP-999: VXE 598 with VXE 596 Center Wing. Lost connection to VTOL AP and ADB and crashed.

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2025-02-11
- **Updated:** 2026-09-09
- **Resolved:** 2026-07-13
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Jacob Troyer
- **Creator:** Alexander Alan Arnold
- **Labels:** Crash, GS_Closed, Hardware, PMA263, Weekly-incident-tracker
- **Links:** relates to FS2-2835 (Investigate VXEP-999); relates to RMA-528 (VXE-598  RMA 250213-1); relates to VXEP-540 (Recent AS150 Connectors causing intermittency and difficulty to connect and disconnect correctly and safely (AS150 Socket Issues)); relates to RMA-529 (2177 TRILLIUM  RMA 250213-2   ); relates to VXEP-985 (VXE 560 Main battery connector was extremely hot after software upgrades); relates to VXEP-1196 (Respond to FoSUAS 4/7 Email)
- **Customer:** PMA263
- **Vehicle Tail Number:** VXE 598
- **Vehicle Configuration:** Unknown at this time
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

30Jan2025 29 Palms Incident/PMA263
“V27 contacted me at 1627 on 30 January reporting that they lost a VXE-30 and that they did observe "issues" with the system prior. I have been informed that Sgt Roth, a Marine with the system, will be contacting me in the morning, as they are still in the training area. V27 wanted to report it to the TALSA as soon as possible. There is little information in the incident, but I will continue updating you on the situation as more information comes in.”
“They are stating that the system changed its commanded altitude during flight to negative 900AGL, and simultaneously they lost control link. During the incident, they continued to receive video feed and observed the AV descending. They lost visual link before it touched down. They currently have the GCS but do not have the AV itself.”

Please see attached witness statement.  The reporting is quite a bit different than the initial report above.  

Report: VXEP-999 V598-CW596-Incident-Report.pptx
SharePoint Folder: VXEP-999 - Commanded to negative 900 AGL

## Corrective Action

- See https://jenaero.atlassian.net/browse/VXEP-540. 
- We may want to reevaluate issuing a AN to operators with potentially affected batteries.

## Plan

- Assigning to @Steve Gonzales to review current status, ppt, and update plan, disposition asset. FYI @Pat Wells
- Invesitgate when and where power harness was manufactured. Determine couse of action with that information.
- @Steve Gonzales to review and update report.
- 3/4 meeting actions. 
- Inspect FW ESC for damage.
- Check OAT for flight.
- Report if no evidence of solder reflow. ##
- Inspect and test XCOM and FWAP. Look for reasons why FWAP reset and not VTOL AP. #
- Update C/CA with evidence of incomplete mate.
- Test at what point connector loses connection compared to normal.
- Discuss potential service bulletin/AN for batteries in the field. Try to isolate dates.
- See additional potential actions in email subtask.

## Issue Status

Nothing unusual found in the hardware inspection other than the Fuse Power Harness was extremely difficult to fully mate. This could be the main root cause in tandem with the bad battery but will need further inspection.
Main battery AS150s are out of spec and failed pull testing. 
Main Battery is in red metal bucket in ENG Bay 
Battery is out of its shell and is under inspection
Fuse power harness was built by compass system with an order date of 5/31/22
report is complete and ready for review

## Root Cause

Some evidence of fuse power harness damage due to OOS socket contacts on the battery. @Adrian Garcia please update findings and plan in above and in the ppt. See https://jenaero.atlassian.net/browse/VXEP-540

## Comments (35)

### Adrian Garcia, 2025-02-24

@Pat Wells 
[embedded image-20250224-205554.png]

### Adrian Garcia, 2025-02-24

@Cameron Chapman @David Grosher I updated the PowerPoint with the AS150 findings. I did not add the battery investigation since it does not seem like a root cause and depleted because it was powered on for so long.

### Hayden Jeanor, 2025-03-14

@Adrian Garcia @Pat Wells @Cameron Chapman I have reviewed this investigation and agree with the conclusions drawn. I plan to schedule a close out meeting with investigation https://jenaero.atlassian.net/browse/VXEP-946  after i finish reviewing that one.

### Pat Wells, 2025-03-17

@Hayden Jeanor taking note of your comment on the report:
”Not sure if we have to data to support the fact the the connector over heated, only an asumption”
Was this made before your comment below stating that you agree?  Trying to bring this to closure so that we can inform the customer.

### Hayden Jeanor, 2025-03-17

@Pat Wells was a comment because of the verbiage used. Cannot confirm it over heated - can only heavily assume, so our description should match as such

### Cameron Chapman, 2025-03-17

@Hayden Jeanor  can you please ensure all of these fields are updates and any further actions that can be done after the investigation are linked in separate tasks? 
[embedded image-20250317-210500.png]

### Hayden Jeanor, 2025-03-17

@Cameron Chapman once the proposed action items are reviewed and determined by stakeholders, i can create the tasks

### Pat Wells, 2025-04-09

@David Grosher can we add a corrective action task for the software that Provides an Operator Warning if climb thresholds from the Operators Manual are exceeded in operation?

### David Grosher, 2025-04-09

@Pat Wells Yes that is fine.

### Alexander Alan Arnold, 2025-04-15

@Steve Gonzales Should this be moved to D6 since there is a CA linked?

### Steve Gonzales, 2025-04-18

4/18 attached surface profile report of as150 contacts.

### Cody Smisek, 2025-11-18

was assigned to steve, reassigned to @Greg Fryer just to assign to someone that works here. vehicle still in engineering, can we move to RMA? @Drew Hildreth @Lauren Velasquez 
FYI @Cameron Chapman

### Cameron Chapman, 2025-11-19

@Greg Fryer, I recommend @Jacob Troyer  review and clean up the investigation status and plan when available per priority list

### Lauren Velasquez, 2026-01-08

@Jacob Troyer Where are we with this investigation? This AC is in the RMA area pending disposition.
@Drew Hildreth  FYSA

### Jacob Troyer, 2026-01-08

@Lauren Velasquez I unfortunately haven’t had time to look into this investigation yet. @Samuel Lopez might be able to look into this more, but I know he has a lot of investigations on his plate too. This is where getting some of these investigations on the engineering priority list might be helpful.
Is there a deadline (or similar) so that I can try to prioritize this with my other work? Anticipating it might take some time to get through this as the primary people who worked this are gone.

### Jacob Troyer, 2026-01-08

@Lauren Velasquez Sammy said he can start looking into this soon once VXE-697 wraps up

### Samuel Lopez, 2026-01-14

@Lauren Velasquez and @Drew Hildreth 

VXE-598 aircraft not recommended to go back to the customer. 
- Visibly Physically damaged.  The aircraft crash landed and most everything is has some signs of fracture – internally or externally.  At most, the Center Wing has no heavy damage (that can be observed).  Nothing else can be trusted to go back to the customer and perform reliably.
- Electrically damaged.  Even the things that aren't broken, there is a high likelihood for that many things are not electrically sound.  Per the user manual, the AC should only ascend 2000 ft before a 5-minute break.  Instead, this aircraft pulled 58A during an ascent for 4000 feet.  At a minimum, the Fixed Wing AP stopped working (and for reasons that are not super clear, if they can even be ascertained).  The fact that the failure was probably caused by the FWD ESC circuit means everything is subject.  All motors, servos, etc, must be replaced.  All motors heavily smell of burn and it’s unknown if it’s from damage or heavy usage.  The XCOMM is ‘probably’ fine, but as a reminder, whatever caused the FW AP to turn off also connects to the XCOMM.  Why risk it?  Quite frankly, it'd be easier to name the components that don't need to be replaced.
- Invisible physical damage.  By the photos, the impact of the frontal force destroyed the nose.  Even if the Center Wing 'looks' okay, there may be unseen damage, particularly to the pitotubes.  Also, the harness took more current for longer than it should have.  More trouble than it’s worth with an uncertain outcome.

 
Recommend VXE-598 to be marked as scrap.  Quote the customer new aircraft minus case.  However, do NOT discard electrical components Avionics Box, CSB Harness, FW ESC and VTOL boards for the time being.

### Lauren Velasquez, 2026-02-04

@Samuel Lopez Sammy- May we retrieve this AC from you?

### Samuel Lopez, 2026-02-05

@Lauren Velasquez 

Yes, omw now

### Jackson Riley Curvin, 2026-07-13

Report sent corrective action canceled

### Cameron Chapman, 2025-03-17

@Hayden Jeanor  can you please ensure all of these fields are updates and any further actions that can be done after the investigation are linked in separate tasks? 
[embedded image-20250317-210500.png]

### Hayden Jeanor, 2025-03-17

@Cameron Chapman once the proposed action items are reviewed and determined by stakeholders, i can create the tasks

### Pat Wells, 2025-04-09

@David Grosher can we add a corrective action task for the software that Provides an Operator Warning if climb thresholds from the Operators Manual are exceeded in operation?

### David Grosher, 2025-04-09

@Pat Wells Yes that is fine.

### Alexander Alan Arnold, 2025-04-15

@Steve Gonzales Should this be moved to D6 since there is a CA linked?

### Steve Gonzales, 2025-04-18

4/18 attached surface profile report of as150 contacts.

### Cody Smisek, 2025-11-18

was assigned to steve, reassigned to @Greg Fryer just to assign to someone that works here. vehicle still in engineering, can we move to RMA? @Drew Hildreth @Lauren Velasquez 
FYI @Cameron Chapman

### Cameron Chapman, 2025-11-19

@Greg Fryer, I recommend @Jacob Troyer  review and clean up the investigation status and plan when available per priority list

### Lauren Velasquez, 2026-01-08

@Jacob Troyer Where are we with this investigation? This AC is in the RMA area pending disposition.
@Drew Hildreth  FYSA

### Jacob Troyer, 2026-01-08

@Lauren Velasquez I unfortunately haven’t had time to look into this investigation yet. @Samuel Lopez might be able to look into this more, but I know he has a lot of investigations on his plate too. This is where getting some of these investigations on the engineering priority list might be helpful.
Is there a deadline (or similar) so that I can try to prioritize this with my other work? Anticipating it might take some time to get through this as the primary people who worked this are gone.

### Jacob Troyer, 2026-01-08

@Lauren Velasquez Sammy said he can start looking into this soon once VXE-697 wraps up

### Samuel Lopez, 2026-01-14

@Lauren Velasquez and @Drew Hildreth 

VXE-598 aircraft not recommended to go back to the customer. 
- Visibly Physically damaged.  The aircraft crash landed and most everything is has some signs of fracture – internally or externally.  At most, the Center Wing has no heavy damage (that can be observed).  Nothing else can be trusted to go back to the customer and perform reliably.
- Electrically damaged.  Even the things that aren't broken, there is a high likelihood for that many things are not electrically sound.  Per the user manual, the AC should only ascend 2000 ft before a 5-minute break.  Instead, this aircraft pulled 58A during an ascent for 4000 feet.  At a minimum, the Fixed Wing AP stopped working (and for reasons that are not super clear, if they can even be ascertained).  The fact that the failure was probably caused by the FWD ESC circuit means everything is subject.  All motors, servos, etc, must be replaced.  All motors heavily smell of burn and it’s unknown if it’s from damage or heavy usage.  The XCOMM is ‘probably’ fine, but as a reminder, whatever caused the FW AP to turn off also connects to the XCOMM.  Why risk it?  Quite frankly, it'd be easier to name the components that don't need to be replaced.
- Invisible physical damage.  By the photos, the impact of the frontal force destroyed the nose.  Even if the Center Wing 'looks' okay, there may be unseen damage, particularly to the pitotubes.  Also, the harness took more current for longer than it should have.  More trouble than it’s worth with an uncertain outcome.

 
Recommend VXE-598 to be marked as scrap.  Quote the customer new aircraft minus case.  However, do NOT discard electrical components Avionics Box, CSB Harness, FW ESC and VTOL boards for the time being.

### Lauren Velasquez, 2026-02-04

@Samuel Lopez Sammy- May we retrieve this AC from you?

### Samuel Lopez, 2026-02-05

@Lauren Velasquez 

Yes, omw now

### Jackson Riley Curvin, 2026-07-13

Report sent corrective action canceled

## Attachments (16)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [Incident Report JAN_30 STALKER VXE_No PII 1.xlsx](attachments/26176_Incident%20Report%20JAN_30%20STALKER%20VXE_No%20PII%201.xlsx.md) | xlsx | 1630 | 2025-02-11 | converted |
| VTOL_VXE596.zip | archive | 49755 | 2025-02-11 | listed only |
| XCOMM_VXE598.zip | archive | 105575 | 2025-02-11 | listed only |
| image-20250218-215850.png | image | 884 | 2025-02-18 | listed only |
| image-20250218-215946.png | image | 19 | 2025-02-18 | listed only |
| image-20250218-220059.png | image | 12 | 2025-02-18 | listed only |
| image-20250218-220123.png | image | 9 | 2025-02-18 | listed only |
| image-20250218-223022.png | image | 95 | 2025-02-18 | listed only |
| image-20250221-211831.png | image | 952 | 2025-02-21 | listed only |
| image-20250221-211840.png | image | 11896 | 2025-02-21 | listed only |
| image-20250221-211846.png | image | 10453 | 2025-02-21 | listed only |
| image-20250221-211853.png | image | 11321 | 2025-02-21 | listed only |
| image-20250221-230954.png | image | 14 | 2025-02-21 | listed only |
| image-20250224-205554.png | image | 1489 | 2025-02-24 | listed only |
| image-20250317-210500.png | image | 66 | 2025-03-17 | listed only |
| [as150 profile report.pdf](attachments/28320_as150%20profile%20report.pdf.md) | pdf | 2954 | 2025-04-18 | converted |
