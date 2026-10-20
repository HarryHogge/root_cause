# VXEP-1762: B40 ENG Iron Bird Test Boards

- **Issue type:** Epic
- **Status:** In Process
- **Priority:** Low
- **Created:** 2026-02-26
- **Updated:** 2026-03-23
- **Reporter:** Jeremy Kostel
- **Assignee:** Matthew Aguirre
- **Creator:** Jeremy Kostel
- **Labels:** EE-Intern
- **Parent:** VXEP-1667 New EE/Intern/Specialist Projects
- **Epic Status:** To Do
- **Epic Color:** ghx-label-2
- **Issue color:** dark_yellow

## Description

Main ticket for tracking progress of this project

Design and implement removable “passthrough” test-point PCBs and short harness adapters for the Block 40 Iron Bird that provide safe, convenient probing access during bench testing without disturbing the system.
At each targeted connector interface, the solution should insert inline (connector → passthrough board/harness → connector) while maintaining normal aircraft-style configuration when installed, and allowing quick removal to return the bench to the baseline configuration.
A dedicated PCB may not be required at every location—some interfaces may be best served by a simple inline harness adapter with labeled breakout/probing leads, depending on complexity, space, and test needs.
Minimum requirements:
- Electrical integrity: rated to carry the required current/voltage with acceptable temperature rise and minimal added resistance/voltage drop.
- Signal integrity & shielding: preserve shield paths/terminations and overall EMC intent (no broken shields, improper grounds, or new noise coupling).
- Harness/workmanship standards: maintain wire type/gauge, strain relief, labeling, and build practices consistent with our harness standards.
- Serviceability: install/remove should be straightforward and repeatable, with minimal disruption to the existing setup and no rework to the base harness.

## Plan

- Identify candidate locations: Compile a complete list of connector interfaces on the Block 40 Iron Bird where adding a passthrough test-point board/harness would be useful.
- Review and validate with Jeremy: Walk through the proposed locations with Jeremy to confirm feasibility, access, and test value.
- Prioritize: Rank the locations/boards by impact and urgency (e.g., most frequently probed, highest troubleshooting value, highest risk if disturbed).
- Break out execution: Create a separate Jira ticket per connector interface (board + any required short harnessing), with clear scope, requirements, and acceptance criteria for each.

## Comments (1)

### Matthew Aguirre, 2026-02-26

Starting out with fuse distribution connector 2123373-01

## Attachments (0)
