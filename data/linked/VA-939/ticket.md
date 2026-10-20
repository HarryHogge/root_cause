# VA-939: VXE 398 Connector Hot and O-rings burnt

- **Issue type:** Epic
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** High
- **Created:** 2023-12-05
- **Updated:** 2025-06-02
- **Resolved:** 2025-06-02
- **Reporter:** Cameron Chapman
- **Assignee:** Cameron Chapman
- **Creator:** Cameron Chapman
- **Labels:** INL
- **Links:** clones VXEP-149 (VXE 398 Connector Hot and O-rings burnt); relates to RMA-175 (VXE-398 231023-2); is duplicated by VXEP-156 (VXE-398 Battery connector hot and o-rings burnt); relates to VA-700 (VXEP-149   VXE 398 Connector Hot and Burnt - Investigate C/CA); relates to VA-701 (VXEP-149   VXE 398 Connector Hot and Burnt - Get information and data from customers); is a parent of VA-700 (VXEP-149   VXE 398 Connector Hot and Burnt - Investigate C/CA); is a parent of VA-701 (VXEP-149   VXE 398 Connector Hot and Burnt - Get information and data from customers)
- **Vehicle Tail Number:** 398
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

Link to logs and photos VXEP-149 VXE398 Connector Hot and O-rings burnt
Working Investigation Summary PPT there-in: VXEP-149 VXE398 Connector Hot and O-rings burnt - Investigation PPT.pptx
From Customer – “In addition, but lower priority, 398 has not been flown since it was sent back from Edge late August ( we only used wingset). When ground testing this week there was a smell, and main battery removed. The battery cable was hot to touch and  O rings on the plugs were burnt. This happened twice this week, the first time it was chalked up to a bad battery. The second time it happened with a different battery, so we narrowed it down to aircraft side. See pic below. Kong/Tom fill in any details on 398 once we get 401 FDR exchange completed.”
Additonal Context from Customer - “The discrepancy happened here at the Synergy lab in MD, and the first event had happened with just an HD40XV sensor payload with no wings attached powered for approximately 30 minutes in preparation for packup . The second event happened five days thereafter fully dressed with the wings, an HD40LV, and the Vidar system powered on for roughly 2-3 hours. Hope the information provided helps, thank you in advance.“

## Sprint

VXE-1 Electrical-8, VXE-2 Everything Else 2024-03, VXE Product Dev & Sup 2024-07, VXE Product Dev & Sup 2024-05, VXE-1 Electrical-7, VXE Prod Dev & Sup 2024-08

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

## Comments (0)

## Attachments (0)
