# VXEP-183: Establish aircraft grounding, bonding, shielding, etc. status and roadmap.

- **Issue type:** Major Project
- **Status:** New
- **Priority:** Medium
- **Created:** 2023-11-08
- **Updated:** 2026-04-20
- **Reporter:** Cameron Chapman
- **Assignee:** Cameron Chapman
- **Creator:** Cameron Chapman
- **Labels:** EE-Active, EE-Consultant
- **Links:** relates to ENG-2998 (VXE 438 Launch Aborts, uncommanded motor spin after second abort, R Aft rotor broken likely from contact with the aircraft stand.); relates to VXEP-500 (VXE 674 E140ZG2 gimbals interfere with magnetometer.); relates to VXEP-915 (VXE30 EMI/EMC Issue and Improvement Collector); relates to XKIT-4112 (Generate E3/EMI/Bonding Plan)
- **Production Stakeholder:** Trevor Gronner
- **Supply Chain Stakeholder:** Victor Vandor
- **Other Stakeholder (as required):** Greg Fryer
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Shared folder Bonding and Shielding Project
Confluence https://jenaero.atlassian.net/wiki/spaces/EE/pages/93356041/Grounding+shielding+and+EMI+design 
Onenote: Grounding, Bonding, Shielding Project  (Web view)
Good guide on grounding here: https://jenaero.atlassian.net/wiki/pages/viewpageattachments.action?pageId=93356041&preview=%2F93356041%2F169215127%2FGrounding tips.pdf

## Plan

Using this page to link potential improvements. 
See here for roadmap
- Edit - Stalker Block >40/35 deferred work/improvements list/Roadmap - Product Design and Operation - Confluence

## Comments (2)

### Cameron Chapman, 2023-11-17

@Barry Mendez , @Greg Fryer and I think that this would be a good area for a consultant to help us establish some basic best practices and aircraft evaluation. Could you please ask Belcan if they have anyone who could help with this?

### Cameron Chapman, 2026-04-20

old plan/description. Project Order
- Diagnose major issues and easier/low scope fixes.
- Research industry standards, best practices, etc. List applicable practices in the confluence above. Below are attached. 
- List others AC 21-99 Aircraft Wiring and Bonding.pdf
- AS50881Rev_C_Wiring_Aerospace_Vehicle
- Research and list more.
- Document best practices (shielding, grounding, impedance, etc). for all electrical equipment and protocols. 
- Protocols in harness and on PCB. 
- Ethernet
- CAN
- analog
- power
- serial
- List others
- Which should be twisted and shielded separate, vs combining protocols in a single cable. Which ones need shielding most, which usually don’t.
- System
- What is the best architecture for grounding and bonding between harnesses, PCBs, batteries, airframe. etc.
- PCB
- What are the best grounding architecture for PCBs?
- harness, 
- Tie shields to backshells in all locations, or prevent ground loops by using tree pattern?
- Should brackets tie to airframe and harness?
- airframe 
- Should be bond panels together?
- Best way to bond carbon fiber.
- Enclosures
- How are these best bonded to the airframe, power, and signal ground.
- Antennas, ground planes, etc.
- Make a rollout plan for how and when to implement improvements to our aircraft. Highest ROI, easiest implementations, etc.
- Select parts to enable improvements (shielded cable, grounding hardware, etc.)
- Create and link projects to improve systems as practical.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| [AC 21-99 Aircraft Wiring and Bonding (ac381fa8-b9dc-4435-8e35-ea9e37ce2f0b).pdf](attachments/17414_AC%2021-99%20Aircraft%20Wiring%20and%20Bonding%20(ac381fa8-b9dc-4435-8e35-ea9e37ce2f0b).pdf.md) | pdf | 19293 | 2023-11-08 | converted (cut) |
| [AC 21-99 Aircraft Wiring and Bonding.pdf](attachments/17412_AC%2021-99%20Aircraft%20Wiring%20and%20Bonding.pdf.md) | pdf | 19293 | 2023-11-08 | converted (cut) |
| [AS50881Rev_C_Wiring_Aerospace_Vehicle.pdf](attachments/17413_AS50881Rev_C_Wiring_Aerospace_Vehicle.pdf.md) | pdf | 2217 | 2023-11-08 | converted (cut) |
