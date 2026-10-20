# VXEP-1310: VXE689 - Network Issues

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2025-06-14
- **Updated:** 2026-02-19
- **Resolved:** 2026-02-19
- **Reporter:** Cody Smisek
- **Assignee:** Scott Whitney
- **Creator:** Cody Smisek
- **Links:** relates to VXEP-1309 (SB40X VXE376 Xcomm SD Issue); relates to VXEP-1230 (VXE 401 Lost Connection After Mission Sync); relates to VXEP-944 (VXE 614 Erratic behavior and propulsion failure led to crash )
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

During 6.5 SW testing, flight ops reported network issues on VXE689. 
Last messages indicate that replacing the silvus enclosure resolved the issue.

## Plan

Gather information about troubleshooting that occurred and any relevant events. 
Determine location of replaced Silvus.

## Comments (4)

### Cody Smisek, 2025-06-14

@Scott Whitney Can we get more information populated in this ticket from the troubleshooting that occurred in the field on 5/30/2025?
@Artis Bertulis where did the replaced radio enclosure end up?

### Artis Bertulis, 2025-06-16

@Cody Smisek @Scott Whitney We used an asset vehicle radio to complete flight testing, and reinstalled the original 689s radio back in it once the test was completed. Here’s a summary of the chat describing the issue:

Friday May 30

In the morning, vehicle 689 was reported to be ready for testing. FLOPS retrieved it from ENG. It was outside of the vehicle’s case, connected to the power supply, but the power supply was powered off, so it got disconnected and packed up.

09:20 - FLOPS can’t connect to the 689, assumed frequency was different, performed some troubleshooting and: Can’t log in to the Silvus webpage, SGCS1 radio is blinking green (searching), tried power cycling the vehicle - no luck. Direct connect using AUX port - webpages are inaccessible (XCOMM, VTOL), but not the Silvus page. The radio was warm to the touch, so I believe it was receiving power.

Did some additional troubleshooting with Carson (will copy below), but determined that the radio is dead. Replaced it with an asset vehicle radio, and everything was working. Once the testing was completed, the “non-working” radio was reinstalled, but not fully secured (ENG was informed of that).

 Troubleshooting with Carson:
”Default IP for AdvNav is 10.128.1.30
Try to ping that see if it comes up. If it does then it's unconfigured.
Otherwise ping 10.130.117.30 and see if it responds.
XComm - Throughput page - Scroll down, SW2, Port4 Link, that should be the Silvus
Is that responding? Does it have anything after Bad?”
 
Pinging - nothing 
SW2 Port5 link - RX was 0 and TX was jumping between 17-50
Checked radio connectors, both ODU connectors in the nosecone - fully seated
SA camera was responding when directly connected.
Connecting Trillium - video feed was present when directly connected
Radio was determined to be inop.

### David Grosher, 2026-01-30

@Drew Hildreth I think this was resolved, can we close this?

### Drew Hildreth, 2026-02-19

Radio was confirmed inop

## Attachments (0)
