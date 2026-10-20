# VXEP-2000: B35/B40 Isolated Lift Boom Test Harness (2164761)

- **Issue type:** Minor Project
- **Status:** New
- **Priority:** Low
- **Created:** 2026-09-15
- **Updated:** 2026-09-15
- **Reporter:** Matthew Aguirre
- **Assignee:** Matthew Aguirre
- **Creator:** Matthew Aguirre
- **Parent:** VXEP-1762 B40 ENG Iron Bird Test Boards
- **Epic Link:** VXEP-1762
- **Issue Status:** In Review (step 7)

## Description

Overall goal is to create a test harness that can be used to power on (no high throttle tests) and troubleshoot isolated B35/40 lift booms. This harness will contain the following:
- Two CAN dsubs (one for left boom, one for right boom) for troubleshooting the CAN bus or sending/receiving messages
- An rj45 port for ethernet communication troubleshooting
- Critical power lines terminated with bullet connector for use with power supply
- Non-critical power lines terminated with bullet connector for use with power supply
- VTOL power lines terminated with bullet connector for use with power supply
- Proper shielding to prevent communication issues
- Proper potting and encapsulation of exposed soldered/crimped terminations to prevent from damage during use of troubleshooting harness.

## Plan

- Scope out power and signal integrity requirements
- Start wiring diagram
- Review with experienced EE
- Revise wiring diagram
- Create quick layout diagram
- Create draftsman diagram
- Review again with experienced EE
- Push BOM to the vault
- Request kit and construct harness
- Test pinout and ask experienced EE for pinout diagram check
- Test harness on both a left and right lift boom
- Document any changes made during construction/testing process to drawings

## Comments (0)

## Attachments (0)
