# VXEP-1490: CBP has been unable to verify the status of their transponder installed on their A/C 863.

- **Issue type:** Problem
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Highest
- **Created:** 2025-08-28
- **Updated:** 2026-01-15
- **Resolved:** 2025-08-28
- **Reporter:** Michael Mohr
- **Assignee:** Cody Smisek
- **Creator:** Michael Mohr
- **Labels:** Weekly-incident-tracker
- **Customer:** Boarder_Patrol
- **Vehicle Tail Number:** 863

## Description

Ticket created to track the issue/solution of verifying the transmitting status off the ping200 transponder installed on CBP’s VXE30.

## Plan

- Confirm geographic location is within view of an ADSB site. If not, customer should utilize a known working receiver to verify operation.
- Review operational procedures for all recommended steps and settings below. Update procedures if not sufficient. FYI @Grant Goodman  and procedures group (forgetting names)

## Comments (11)

### Michael Mohr, 2025-08-28

@Cody Smisek @Mike DeJesus @Cameron Chapman @Wesley Lilienthal @Erik Hanson

### Michael Mohr, 2025-08-28

Alan Richie (CBP) reached out and asked if there was a method to verify if his transponder was transmitting. After setup and verification of the control and config page and disconnection of the GCS from the ping200. how does an operator verify that the unit is transmitting?

### Michael Mohr, 2025-08-28

I tried to track him this morning on Flight Radar 24 but no joy. He said he ordered a ADSB dongle and is going to build a raspberry pi receiver this weekend and will know for sure if it’s just not hitting any ground stations or not working.

### Cody Smisek, 2025-08-28

First thing I would confirm with the uavionix manual is that having a blank aircraft registration is acceptable. i would also confirm that there are no limitations on ICAO addresses. i see here they have just 5, which seems extremely unlikely to be legitimate.

I also see in the email someone tried to confirm they could see it on flightradar. That would assume the aircraft is in an area covered by the site of choice. Where geographically is this at?
They could purchase one of many readily available adsb receivers from vendors such as Garmin, Stratux, Stratus etc. and link to a appropriate device with appropriate software.  @Michael Mohr

### Cody Smisek, 2025-08-28

@Michael Mohr  it looks like they’ve also got a flag for maintenance required in the top right corner.

### Cody Smisek, 2025-08-28

looks like ‘on ground’ is also checked. need to verify with uavionix manual if that is correct to use.

### Cody Smisek, 2025-08-28

@Cameron Chapman  i have updated step 1.

### Michael Mohr, 2025-08-28

Moving to Teams chat.

### Jeremy White, 2025-09-09

@Drew Hildreth Was there resolution on this? I don’t believe I was added to the Teams Chat.

### Drew Hildreth, 2025-09-09

@Jeremy White Not yet. Still working through it.

### Cody Smisek, 2025-09-09

@Drew Hildreth I have configured and verified our own tranpsonders at APEX. please advise if further assistance is needed.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| CC page 2.jpg | image | 244 | 2025-08-28 | listed only |
| CC page.jpg | image | 260 | 2025-08-28 | listed only |
