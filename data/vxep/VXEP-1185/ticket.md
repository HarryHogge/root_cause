# VXEP-1185: RF Validation of 2122790-01 ARRAY ANTENNA MOUNT, WING TIP, RIGHT, ASSEMBLY

- **Issue type:** Epic
- **Status:** DONE
- **Resolution:** Done
- **Priority:** High
- **Created:** 2025-04-04
- **Updated:** 2025-04-08
- **Resolved:** 2025-04-08
- **Due:** 2025-04-08
- **Reporter:** Tobi Ogunro
- **Assignee:** Wesley Lilienthal
- **Creator:** Tobi Ogunro
- **Parent:** VXEP-1008 Mod Payload A-Kit Gen 2 design/release/test (Long term issue resolution)
- **Production Stakeholder:** Trevor Gronner
- **Leadership Stakeholder:** Greg Fryer

## Description

With receipt of the MOD B-Kit, we are now positioned to validate the new 2122790-01 ARRAY ANTENNA MOUNT, WING TIP, RIGHT, ASSEMBLY. This validation effort will focus on confirming the integrity of the RF cable assembly by performing a two-port VNA (Vector Network Analyzer) measurement from the MOD Payload radio to its antennas. This ensures optimal signal transmission and performance.

## Plan

Project Deliverables:
Two-port VNA measurement of the RF cable assembly between the MOD Payload radio and antennas.Validation report of RF signal transmission integrity.Procurement and tracking of required RF adapters.Identification and documentation of antenna connector types.Configuration of the VNA for testing.Final test execution and analysis.

## Issue Status

VNA Measurement Results 2025-04-08:
VNA RF integrity measurements on the CACI rig are complete. All three RF paths in the assembly check out as perfectly healthy when the connection is properly mated. Very well matched across the band, great return loss, insertion loss on par with expectations, and consistent group delay path-to-path. 
Please find an overview of results below. S-parameter s2p files are also attached for CACI's own plotting and review purposes.
Red Path "L":
[embedded: image-20250408-222617.png]
[embedded: Red L Path - Port 1 Antenna Mast SSMB - Port 2 Cable Assembly SMPM-T - With Port Extensions.s2p]
Green Path "F":
[embedded: image-20250408-222633.png]
[embedded: Green F Path - Port 1 Antenna Mast SSMB - Port 2 Cable Assembly SMPM-T - With Port Extensions.s2p]
Blue Path "R":
[embedded: image-20250408-222646.png]
[embedded: Blue R Path - Port 1 Antenna Mast SSMB - Port 2 Cable Assembly SMPM-T - With Port Extensions.s2p]

## Comments (3)

### Tobi Ogunro, 2025-04-04

FYSA @Greg Fryer & @Trevor Gronner

### Tobi Ogunro, 2025-04-08

@Wesley Lilienthal  Closing out this ticket. 
FYSA @Trevor Gronner

### Wesley Lilienthal, 2025-04-08

Updated the Issue Status field above with annotations for each image and uploaded the captured S-parameter s2p files.

## Attachments (6)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Blue R Path - Port 1 Antenna Mast SSMB - Port 2 Cable Assembly SMPM-T - With Port Extensions.s2p | other | 264 | 2025-04-08 | listed only |
| Green F Path - Port 1 Antenna Mast SSMB - Port 2 Cable Assembly SMPM-T - With Port Extensions.s2p | other | 264 | 2025-04-08 | listed only |
| Red L Path - Port 1 Antenna Mast SSMB - Port 2 Cable Assembly SMPM-T - With Port Extensions.s2p | other | 264 | 2025-04-08 | listed only |
| image-20250408-222617.png | image | 127 | 2025-04-08 | listed only |
| image-20250408-222633.png | image | 128 | 2025-04-08 | listed only |
| image-20250408-222646.png | image | 128 | 2025-04-08 | listed only |
