# FS2-751: Speedgoat Test Capability Development

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2023-08-22
- **Updated:** 2026-02-09
- **Resolved:** 2026-02-09
- **Reporter:** David Grosher
- **Creator:** David Grosher
- **Components:** WDT Investigation
- **Links:** blocks VXEP-9 ((Duplicate) TPTR-74 VXE 510 Watchdog Software Fault); blocks VXEP-11 (TPTR-5 VXE 407: (VTOL-AP-WD) Unexpected Behavior Seen During Vertical Landing); relates to FS2-1174 (EE portion-Design, build, and document speedgoat hil); blocks FS2-1528 (Create injection points for margin/robustness testing in HIL); Linked issue cannot finish until this issue finishes. FS2-1414 (HIL margin validation -  XKit (Controls Analysis))

## Description

HIL v2.0 see WDT investigation slides

## Comments (4)

### David Grosher, 2023-10-06

@Everett Werner I’m going to start assigning you tasks from this epic to develop the HILv2.0.  I have downloaded the speedgoat toolbox with the drivers for their hardware.  We also have a computer with Mathworks Simulink Real-Time to be the host computer for this development.  Let’s discuss Monday and I can address any questions that you might have.

### David Grosher, 2023-11-09

@Ben Triplett This is the speedgoat hardware integration epic.  If you are going to pull something in, I would suggest the ublox. It is a complex but well documented interface. u-blox8-M8_ReceiverDescrProtSpec_UBX-13003221.pdf  The messages that we use can be found in autopilot_202 repo gps.cpp. I’m not sure if we need to handle initialization messages, it depends on whether the AP drivers require responses. Also the VTOL AP and FW AP have  different configurations. Kurt can help you there.

### David Grosher, 2023-11-14

@Cameron Chapman See https://jenaero.atlassian.net/browse/FS2-773 and https://jenaero.atlassian.net/browse/FS2-1175 for EE work.

### David Grosher, 2023-11-14

@Everett Werner @Ben Triplett @Ryan Christino Here is an architectural drawing that will help with laying out the Speedgoat HIL 2023-08-25 VXE30 System Block Diagram - Aircraft.pdf

## Attachments (0)
