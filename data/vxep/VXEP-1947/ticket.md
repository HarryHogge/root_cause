# VXEP-1947: VXE 921 avionics will not stay on after trying to flash MCM to JP6

- **Issue type:** Problem
- **Status:** New
- **Priority:** High
- **Created:** 2026-06-26
- **Updated:** 2026-06-26
- **Reporter:** Cameron Chapman
- **Assignee:** Josh Adams
- **Creator:** Cameron Chapman
- **Links:** relates to XKIT-5454 (Unclear guidance and automation to prevent MCM from overheating. )
- **Plan:** Assigning to @Josh Adams . Please update when parts ship

## Description

Teams discussion https://teams.microsoft.com/l/message/19:02d28e5d0bcc457285d7f8a749dcb581@thread.v2/1782500891539?context=%7B%22contextType%22%3A%22chat%22%7D 

TN:921 was utilized last minute as the air vehicle to support the LRR M-Code bench top demonstration. After the M-code receiver was verified on the air vehicle using the logs. The team was going to update the air vehicles software to move from Jetpack 5 to Jetpack 6 to support the latest of OGCS.  Before beginning the flash, the MCM and aircraft quit responding. The team power cycled the air vehicle with no success, nothing was reachable in the avionics enclosure. Pulle d IB avionics enclosure and placed in aircraft after performing continuity checks and verified power. All checks and boards reachable to IB Avionics Enclosure (A826). 

Adv Nav Avionics Box (Damaged)
PN: 2119959-01
SN: A921

Adv Nav Avionics Box (B35Y crashed asset from IB. Replaced above. Updated to JP6 in same conditions).
PN:2119959-01
SN: A826

- What vehicle was it? 921 (Block 30 Adc Nav)
- What was running on the vehicle? Baseline OGCS or more functions?  AV M-Code @Alan Burnsworth Please add the details about software here.
- Payload installed and running? No E140 payload was installed.
- Battery or power supply? Battery
- Was this in the facility or outside? Inside.
- Prior to this it was being used for MANI testing by Abel and John. (Rpi test setup connected to Alden most likely). Unsure if related. That port should be protected and separate.

## Issue Status

Still need to breakdown before/after configs to further narrow RCCA, but below is the hardware status - 
 
921 Vehicle
Continuity checks vehicle cables  - all passed
A826 IB avionics box checkout on the vehicle - all boards online and reachable 
New Avionics Box (Received this morning) on the vehicle - all boards online and reachable
Going to send the 921 vehicle back through SCO in HSV with the new avionics box to validate prior to returning to MANI testing. (May need to load OGCS and set gain values prior to SCO)
 
921 Avionics Box
Connected to the iron bird, verified all boards unreachable.
Slight electrical burn smell is coming from the box, but no visually detectable burn marks found
 
Status
Problem is bracketed to the 921 avionics box itself. 
Next step is to return the box to SLO for further decomposition and analysis

## Comments (0)

## Attachments (0)
