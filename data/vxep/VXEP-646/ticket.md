# VXEP-646: VXE 392 crash on VTOL launch

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2024-09-19
- **Updated:** 2026-03-02
- **Resolved:** 2026-01-20
- **Reporter:** Pat Wells
- **Assignee:** Jacob Troyer
- **Creator:** Pat Wells
- **Labels:** USASOC, Weekly-incident-tracker
- **Links:** relates to VA-573 (Poor Quality/higher impedance plating on AS150 power contacts - Containment and Corrective Action); relates to RMA-354 (VXE-392 240923-1)
- **Customer:** USASOC
- **Vehicle Tail Number:** 392
- **Root Cause:** Higher Impedance plating on AS150 power connector
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

Full Witness statement pending..

Operator stated that “Altitude Control fault” was displayed in VTOL messages

See video

Relevant Files: VXEP-646 - VXE 392 Crash on VTOL Launch
Incident Report Page: Flight Safety - VXEP-646 - VXE 392 Crash on VTOL Launch - All Documents
Checklist:

## Corrective Action

Corrective action found in the linked issue: [VA-573] Poor Quality/higher impedance plating on AS150 power contacts - Containment and Corrective Action - Jira

## Plan

8/5/2025
Plan to review 8/11/-8/15

@Giovanni Gonzalez can you please update the fields below, and create an investigation summary if needed? We should have more detail on C/CAs to hopefully try and prevent future occurrences. Some related questions we should answer
- How many flights did this vehicle have?
- Could this issue have been caught before it crashed?
- Does it look like the service bulletin for partially mated connector prevention was applied?
- Are the battery and harness contacts in spec (battery in HSV)
- When listing “higher than wanted” always include the measured value and the spec range.
- List reasons why the linked corrective actions did not prevent this issue.
- @Steve Gonzales to review after updates.

## Issue Status

Battery seems to be fine as seen in the activity below
CW Box was taken off the shelf for further hardware inspection, CW Box located at Adrian’s workbench
CW Power Connector antispark resistance measured at 5.9 ohms
VTOL logs show a sharp drop in output throttle on all 4 motors which correlates to the drop in IBatt seen, investigating if this throttle behavior was intended
Impedance check on CW Power Connector will be performed: Higher impedance plating measured on power connector

## Comments (27)

### David Grosher, 2024-09-19

@Cameron Chapman I see HLB Voltage and Current dropping off towards the tail end of the VTOL data log. It appears to capture more of the event than the XCOMM datalog. The voltage appears to drop to 21.25V. 

[embedded: image-20240919-210521.png]
@Pat Wells FYSA

### Cameron Chapman, 2024-09-19

It seems like either a battery or AS150 fault are most likely, considering the sharp voltage drop. @Pat Wells I recommend the following.
- Where is this located?
- Ship aircraft back to SLO if feasible. Battery too would be useful, but maybe harder to ship a damaged battery. If shipping is difficult, could perform these steps on site.
- Measure HLB cell voltages with cell checker if it is accessible. Record HLB SN.
- Inspect and photograph battery and CW power connectors for damage, burning smell, excess potting that should have been removed and mating indicator added with SB.
- Continuity check between CW battery and wing power connectors.
- Measure antispark resistance of the CW power connector. Tip of contact to base of the male contact with a line.
- Record flight history of this battery and aircraft.

[embedded: image-20240919-213955.png]


[embedded: image-20240919-214033.png]

### Pat Wells, 2024-09-19

@Cameron Chapman 
- Aircraft is currently in Georgia,
- We are making arrangements to return aircraft to SLO. HLB will be hand carried by FLOPS instructor who drove to the event.  HLB is returning to Huntsville so we’ll have to perform all the testing here. It can not be shipped in it’s current condition.

### Carson Buckley, 2024-09-19

@Cameron Chapman This vehicle was in for service on 2022-12-07, I am adding the AAR files from those flights.

### Pat Wells, 2024-09-20

@Cameron Chapman added witness statement from FLOPS instructor on site.

### Pat Wells, 2024-09-23

@Cameron Chapman we have the HLB here in Huntsville.
Could you please provide guidance on what tests you’d like performed on the battery.

### Cameron Chapman, 2024-09-23

@Pat Wells see the plan section:
“
- Measure HLB cell voltages with cell checker if it is accessible. Record HLB SN.
- Inspect and photograph battery and CW power connectors for damage, burning smell, excess potting that should have been removed and mating indicator added with SB.
- Check data logs for software version used.
- Continuity check between CW battery and wing power connectors. Maybe easiest to hookup to load and measure voltages. Ensure battery is safe to connect and/or discharge
- Measure antispark resistance of the CW power connector. Tip of contact to base of the male contact with a line.
- Record flight history of this battery and aircraft. anyone with log access and bandwidth at either site could do this”

### Pat Wells, 2024-09-23

@Cameron Chapman we’ll handle the tasks specific to the battery here in HSV.
We do not have the aircraft back in SLO yet. 

@Michael Mohr

### Pat Wells, 2024-09-24

@Cameron Chapman checked cell voltages.  Looks good to me.
HLB S/N: 2-2048
[embedded: HLB Cell check.jpg]

### Cameron Chapman, 2024-09-24

@Pat Wells can you please also coordinate these steps. @John Gober can provide local EE support. 
- Record HLB SN.
- Inspect and photograph battery and CW power connectors for damage, burning smell, excess potting that should have been removed and mating indicator added with SB.
- Check data logs for software version used.
- Continuity check between CW battery and wing power connectors. Maybe easiest to hookup to load and measure voltages. Ensure battery is safe to connect and/or discharge

### Pat Wells, 2024-09-25

@Cameron Chapman the only component we have in HSV is the HLB. I did the cell check and inspection on it yesterday.  The connectors on the battery are pristine and show no signs of any issues.  No excess potting material present.

The aircraft is on it’s way to SLO, this is where the investigation will need to pick back up.

### Sean Odell, 2024-11-07

@Cameron Chapman @Pat Wells Aircraft has been delivered to Engineering for you to continue your investigation. My apologies on not letting you know earlier as it was brought over last Friday.

### Cameron Chapman, 2024-11-07

@Adrian Garcia can you please work on this?

### Cody Smisek, 2024-11-07

@Sean Odell can we include the RMA labels on all aircraft that come over to engineering going forward?

### Adrian Garcia, 2024-11-07

@Cameron Chapman Assigning to @Giovanni Gonzalez while I work on SD Card Investigation but will help him when needed.

### Sean Odell, 2024-11-07

@Cody Smisek Yes, I can include the labels when it goes over to Engineering. Originally I only had a small amount, but I have made more since then.

### Cody Smisek, 2024-11-12

@Cameron Chapman @Adrian Garcia @Giovanni Gonzalez Recommend updating the plan accordingly along with status. I see 392 case is no longer in the stack of cases.

### Alexander Alan Arnold, 2024-12-10

@Giovanni Gonzalez Any updates on this issue?

### Giovanni Gonzalez, 2024-12-10

@Alexander Alan Arnold Impedance check on CW power connector was performed which showed a higher impedance than wanted likely relating to the following issue: [VA-573] Poor Quality/higher impedance plating on AS150 power contacts - Containment and Corrective Action - Jira. Since the battery check came out ok as did the antispark resistance, this is likely the root cause of the incident.

### Alexander Alan Arnold, 2025-01-10

@Giovanni Gonzalez If we are saying the AS150 impedance is the root cause can we move this to D5/6?

### Lauren Velasquez, 2025-02-17

@Pat Wells 
Back in RMA per your request. - NO RMA TICKET FOR THIS

### Pat Wells, 2025-02-25

@Cameron Chapman we’re basically wrapped with this on the customer side.  Can we close it out on our end?  Not sure if your team still has more tasks to complete.

### Cameron Chapman, 2025-02-25

@Pat Wells see updated plan. It seems close to closure, but I think we should add more detail to C/CA.

### Pat Wells, 2025-03-05

@Cameron Chapman aside from implementing CA’s this looks to be done. Could we start working on a final report?

### Cameron Chapman, 2025-03-05

@Pat Wells assigning to @Steve Gonzales to finalize report.

### Christa Meck, 2025-08-05

@Steve Gonzales What is the status of this investigation?
Leaving open until Aug 12 for feedback.

### Steve Gonzales, 2025-08-05

@Christa Meck added notes to plan field.  I plan to review next week. thx.

## Attachments (12)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AC392 Mishap SA Feed (1).mpg | video | 938 | 2024-09-19 | listed only |
| Image (1).jfif | image | 396 | 2024-09-19 | listed only |
| Image (2).jfif | image | 403 | 2024-09-19 | listed only |
| Image (3).jfif | image | 428 | 2024-09-19 | listed only |
| Image (4).jfif | image | 366 | 2024-09-19 | listed only |
| Image (5).jfif | image | 313 | 2024-09-19 | listed only |
| MOV_0797.mov.mov | video | 7903 | 2024-09-19 | listed only |
| T95_V392_240919_110152_02_pack.zip | archive | 1428 | 2024-09-19 | listed only |
| image-20240919-210521.png | image | 32 | 2024-09-19 | listed only |
| image-20240919-213955.png | image | 64 | 2024-09-19 | listed only |
| image-20240919-214033.png | image | 37 | 2024-09-19 | listed only |
| HLB Cell check.jpg | image | 2472 | 2024-09-24 | listed only |
