# VXEP-149: VXE 398 Connector Hot and O-rings burnt

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-10-18
- **Updated:** 2026-03-02
- **Resolved:** 2025-05-28
- **Reporter:** Cody Smisek
- **Assignee:** Cameron Chapman
- **Creator:** Cody Smisek
- **Labels:** INL
- **Links:** relates to VA-700 (VXEP-149   VXE 398 Connector Hot and Burnt - Investigate C/CA); relates to VA-701 (VXEP-149   VXE 398 Connector Hot and Burnt - Get information and data from customers); relates to RMA-175 (VXE-398 231023-2); is duplicated by VXEP-156 (VXE-398 Battery connector hot and o-rings burnt); is cloned by VA-939 (VXE 398 Connector Hot and O-rings burnt)
- **Customer:** INL
- **Vehicle Tail Number:** 398
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

Link to logs and photos VXEP-149 VXE398 Connector Hot and O-rings burnt
Working Investigation Summary PPT there-in: VXEP-149 VXE398 Connector Hot and O-rings burnt - Investigation PPT.pptx
From Customer – “In addition, but lower priority, 398 has not been flown since it was sent back from Edge late August ( we only used wingset). When ground testing this week there was a smell, and main battery removed. The battery cable was hot to touch and  O rings on the plugs were burnt. This happened twice this week, the first time it was chalked up to a bad battery. The second time it happened with a different battery, so we narrowed it down to aircraft side. See pic below. Kong/Tom fill in any details on 398 once we get 401 FDR exchange completed.”
Additonal Context from Customer - “The discrepancy happened here at the Synergy lab in MD, and the first event had happened with just an HD40XV sensor payload with no wings attached powered for approximately 30 minutes in preparation for packup . The second event happened five days thereafter fully dressed with the wings, an HD40LV, and the Vidar system powered on for roughly 2-3 hours. Hope the information provided helps, thank you in advance.“

## Plan

- Remove fuselage power harness, inspect for faults.
- It might be helpful to ask what happened between august and the incident wrt power ups, parts changed, etc.

## Issue Status

Perform resistance measurement from the tip of the AS150 anti-spark contact to the base. Report findings.
 9.8 tip to base positive pin (this seems high??)  it was 5.7 on the other birds
- Repeated measurement, 21.1 Ohms Anti-spark tip-to-base.

Measure resistance between positive (from the base of the terminal) and negative terminals.
3.5 base to base negative-pos , 0.9 inside negative to base of positive
- Repeated measurement, 1.0 MOhm which drops and rises because of capacitance in the fuselage


- Could not replicate failure. No short present upon arrival at EA SLO.
- Fuselage powered up on power supply, all systems functional.
- Damage found to one of the MAIN BATT power pins of the Fuselage Payload Harness on the upper payload hood. Damage is reminiscent of arcing.
- Current through this pin would not have been enough to damage the battery connector.
- No sign of hot swapping on the Nose Power Harness.
- No XCOMM logs show any major power surges.
- The most that can be found are continuous 3A draws for a couple of hours on end.
- No signs of damage in the FWD ESC
- No signs of damage in Avionics Box, loose screw
- wiggle testing harnesses while powered did not show any anomalies - The damage to that connector and no others strongly suggests an issue in the fuse power harness.
- Measuring the contact resistance of the AS150 anti-spark contact came up with a value of 488uOhms. This is about twice as high as the acceptable field test value of the AS150 contacts (for the Center Wing that is, an acceptable value hasn’t been defined for the fuselage AS150 yet).
- This may be related, or due to the high temperature damage of the incident.
- 4A pull through the fuselage power harness for 1 hour did not build up any excess heat at the AS150 connector.

## Comments (12)

### Pat Wells, 2023-10-18

@Greg Fryer 
@Sean Odell FYSA

### Greg Fryer, 2023-10-18

@Cameron Chapman Moving over to you, since it seems like a contact issue or related? It’s main battery though…

### Pat Wells, 2023-10-18

@Cameron Chapman questions have to sent to customer.

### Cameron Chapman, 2023-10-25

Questions we asked the customer and their response:
Perform resistance measurement from the tip of the AS150 anti-spark contact to the base. Report findings.
 3.5 base to base negative-pos , 0.9 inside negative to base of positive
Measure resistance between positive (from the base of the terminal) and negative terminals.
9.8 tip to base positive pin (this seems high??)  it was 5.7 on the other birds
Aircraft is enroute on RMA as of 10/25/23

### Sean Odell, 2023-10-26

@Cameron Chapman Aircraft evaluated, photos taken, added to RMA ticket for reference. I am bringing over the aircraft today.

@Pat Wells FYSA

### Cameron Chapman, 2023-10-27

3.5 base to base negative-pos , 0.9 inside negative to base of positive. 
- If + to - is 0.9Ohms There seems to be a short. @Connor Peebles , can you please have someone today try to isolate this issue?

Measure resistance between positive (from the base of the terminal) and negative terminals.
9.8 tip to base positive pin (this seems high??)  it was 5.7 on the other birds 
- This is probably from damage to the resistor due to high current/heat.

### Connor Peebles, 2023-10-30

Was the fuselage the only component under test during the incident? Were there any other modules attached (such as the CW)?

### Cameron Chapman, 2023-10-30

@Connor Peebles a normal CW only receives current limited 12V from the avionics box, so it should not have been able to create this much current load. CW pins would show damage if there was that much load.

### Connor Peebles, 2023-11-01

@David Grosher Could we have someone from software give a second pair of eyes into the XCOMM logs on this ticket? It could be done relatively quickly. I cannot identify any anomalies besides some peaking current on the 12V AUX. I’m hoping you could identify something I haven’t. Please put results in [VA-700] VXEP-149 VXE 398 Connector Hot and Burnt - Investigate C/CA - Jira (atlassian.net)

### Connor Peebles, 2023-11-16

See investigation status for more detail - In summary: no anomalies can be found with 398, other than a high resistance AS150 anti-spark and the melted carbon ring on said AS150.
- I would recommend replacing aft portion of the Fuselage Power Harness [(107-102189-1) or the whole 107-102189 FWD and AFT, whichever is easier for Production].
- Continue testing the removed 107-102189-1
- Recommend re-assembling and re-testing the avionics box through the check-out procedure and then doing the same for the whole VXE398, which is done in the RMA process I believe.
- Recommend re-testing of the FWD ESC
- and FWD Motor
- Request customer to send SN information of and perform battery cell check, or to send back the batteries in question.

@Cameron Chapman  for review

### Cameron Chapman, 2023-11-18

@Connor Peebles good recommendations. I agree with them except the battery part. It is very unlikely that two batteries caused this issue. I hope disecting the harness will give us a lead.

### Connor Peebles, 2023-11-21

Removed aft portion of the Fuselage Power Harness (107-102189-1) for further diagnosis. The rest of the Fuselage can go back into RMA. @Sean Odell @Pat Wells @Cameron Chapman

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| connector.png | image | 1272 | 2023-10-18 | listed only |
| [XCL00043.csv](attachments/17009_XCL00043.csv.md) | csv | 897 | 2023-10-25 | converted |
| [XCL00045.csv](attachments/17008_XCL00045.csv.md) | csv | 613 | 2023-10-25 | converted |
| [XCL00047.csv](attachments/17007_XCL00047.csv.md) | csv | 565 | 2023-10-25 | converted |
