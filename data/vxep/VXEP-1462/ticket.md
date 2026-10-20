# VXEP-1462: VXE 895 Loss of GPS after VTOL motor checks.

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-08-06
- **Updated:** 2026-03-02
- **Resolved:** 2025-10-16
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** Novatel_Reset, Secret_Service
- **Links:** relates to VXEP-1463 (SW Patch for NovAtel Investigation)
- **Customer:** Secret_Service
- **Vehicle Tail Number:** VXE 895
- **Vehicle Configuration:** VXE 30 Advanced NAV, Battery NO gimbal
- **Severity:** 1 - Flight Critical

## Description

OPERATOR STATEMENT
Aircraft (895) was undergoing pre-flight lift motor checks and subsequently lost GPS.
-VTOL GPS Fault
-GPS Fault
 
Additionally, while on the phone with Global Support at 09:57 am EDT 8/6/2025, it indicated a Dead Reconning in the VXE SUAV GUI (See attached screen snip), while still grounded. No flight was obtained. AAR completed and FDR downloaded.
FDR File name: T115_V895_250806_061116_PACK.ZIP
Per Alex at Global Support, we are conducting a power cycle, and conduct pre-flight checks again.
After power cycling and reconnecting to VXE SUAV GUI, the GPS coming back momentarily, then loses all GPS and says No-Fix (see screen snip). The heat sink on the fuselage GPS is fairly warm, and the ambient temp is 73 degrees and overcast.
 
Spoke to Alex and Global Support again at 10:15 am EDT 8/6/2025, he recommended swapping the center wing from another aircraft to isolate wing from the possible issue.
After changing the center wing to that of 897, the GPS Fix still did not re-acquire.
 
Spoke to Alex at Global Support again at 10:33 am EDT 8/6/2025, and he advised to disassemble 895, and he would open an investigation into the flight data and logs.
Alex asked that we run through everything with 897, before we officially begin the investigation with 895, as a means to isolate the issue.
FDR for the second attempt is under file name: T115_V895_250806_071150_PACK.ZIP
 
Per a call back at 10:37 am EDT 8/6/2025, Alex asked that we DO NOT conduct a mag check with 897, and we go straight into the launch wizard.
 
897 immediately has 25 Satellites acquired without Mag Checks.
 
Per Alex at Global Support at 1100 am EDT 8/6/2025. We advised the aircraft was acquiring satellites. He stated that we need to conduct cardinal checks, and then we can fly 897. Once they receive the FDR files, and screen snips, the Global Support team will review and ikely be sending us an RMA to return 895, for possible hardware issues on the fuselage.

## Plan

This appears to be the same Novatel reset issue. Hot fox for that issue is being tested (8/15). Once available test with that update and confirm it resolves the issue.

## Comments (6)

### Alexander Alan Arnold, 2025-08-06

[embedded: image-20250806-160037.png]
This is from one of the AARs, it seems like potetinially the NOVATEL is not pushing data to the GCS. I did some digging in the NCR list and 897 presented a similar issue discovered in SCO. NCR List - AdvNav GPS not responding to FW AP query
After a power cycle the GPS momentarily comes back and is then lost. 

897 is the other aircraft the customer currently has and seems to be presenting no issues after the NCR Corrective action was applied. I am hoping this one is a similar fix. 

I am going to have this aircraft RMAd as soon as possible

### Greg Fryer, 2025-08-06

@Eric Brewer Can you please look in Dave’s absence. Can we figure out if this is the FWAP reset issue killing Novatel?
@Scott Whitney FYSA

### Eric Brewer, 2025-08-06

@Greg Fryer yes - this shows ‘heartbeat timeouts’ so likely related to the issue we’re actively investigating.

### Jackson Riley Curvin, 2025-09-16

@David Grosher  can we close this ticket?

### David Grosher, 2025-09-16

@Jackson Riley Curvin Yes, as long as we have updated this bird to v6.5.1.

### Greg Fryer, 2025-10-16

@David Grosher @Jackson Riley Curvin Based on the comment, I’m moving this to closed.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IMG_0346.jpeg | image | 389 | 2025-08-06 | listed only |
| System 895 Flight 1 issue.PNG | image | 3374 | 2025-08-06 | listed only |
| T115_V895_250806_061116_pack.zip | archive | 1340 | 2025-08-06 | listed only |
| T115_V895_250806_071150_pack.zip | archive | 633 | 2025-08-06 | listed only |
| image-20250806-160037.png | image | 25 | 2025-08-06 | listed only |
