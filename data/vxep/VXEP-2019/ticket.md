# VXEP-2019: VXE 918 VTOL GPS error followed by Lost Comms Message

- **Issue type:** Incident (8D)
- **Status:** D2 - Gathering Information
- **Priority:** High
- **Created:** 2026-10-09
- **Updated:** 2026-10-20
- **Reporter:** Alexander Alan Arnold
- **Assignee:** David Grosher
- **Creator:** Alexander Alan Arnold
- **Labels:** Crash, Precision, RCCA, Weekly-incident-tracker
- **Customer:** Precision
- **Vehicle Tail Number:** VXE 918
- **Vehicle Configuration:** ADV NAV with OGCS, battery, unknown payloads
- **Severity:** 1 - Flight Critical

## Description

VXE 918 Crash 09 October 2026,
49 LBS
OGCS
Radio Relay payload/battery
PIC Smaltbie
GC Nrobinson
 
VXE 918 was 22KM away from the LRS at 3000 AGL.
Winds were reported 17 mph from 240t
VXE was on way back from furthest point 53 min into flight, and was going to take apx 45 mins to RTB and still had 70% battery, PIC commanded dash to see new apx rtb time and see power draw. After commanding Cruise and adjusting route to have VXE fly closer to road looked at Silvus page to see the interference on 902, OGCS alerted to a VTOL GPS error, looked at the GNSS Tab and saw 28 for FW and 0 Sats for VTOL followed by a lost coms. Looking at the Aircraft last known location VXE 918 was in a 7620 FPM decent and at 2700 AGL 41.4 MPH IAS and in a bank to the left.
VXE was found apx an hour after lost coms on the ground with the nose cone 350 feet away, 100 meters from the last know location. Props had 23 cycles left until replacement.
Tail boom and nose cone heavily damaged, Right spar broken, slight delamination on right rear center wing. Cosmetic damage to wings in multiple places.

## Comments (9)

### Alexander Alan Arnold, 2026-10-09

@David Grosher AAR attached let us know if you need anything else in terms of data

### Alexander Alan Arnold, 2026-10-12

@Eric Brewer Can we get an initial analysis of the data for this one? Customer is delaying testing with other aircraft until they here back from us.

### Eric Brewer, 2026-10-12

@Alexander Alan Arnold I dumped some plots at the very end of this deck: https://redwireglobal.sharepoint.com/:p:/r/sites/FlightSafety/_layouts/15/Doc.aspx?sourcedoc=%7BC5B76AA8-0138-4956-9EFC-59CB66BEBAA4%7D&file=V918Investigation.pptx&action=edit&mobileredirect=true&wdwpf=doclib-t
Right now, my best guess is that the INS was reporting an erroneous altitude and vertical speed.  That would be most likely caused by a Novatel IMU failure (we have not seen one of those previously so an unlikely event) or spoofing (unless someone was running a CUAS system domestically this would be surprising?).  The logs cut off before I can get more insight into how exactly it crashed but this is what I know so far.

### Alexander Alan Arnold, 2026-10-12

@Eric Brewer thanks eric. @Ted Trowbridge Given this was an OGCS flight is there anything in the OGCS logs that provide any insight?

### Ted Trowbridge, 2026-10-12

@Alexander Alan Arnold I doubt there is anything that would provide additional insight beyond what is in the AP logs (that are cut off)

### Eric Brewer, 2026-10-12

@Ted Trowbridge @Alexander Alan Arnold I did plot some of the ogcs stanag messages as well and as Ted says unfortunately those cut right around the same time as the flight logs on the vehicle.

### Alexander Alan Arnold, 2026-10-13

@Eric Brewer Is the consensus that without the hardware back in SLO this cannot be investigated further?

### Eric Brewer, 2026-10-13

@Alexander Alan Arnold yes I would send it back and we can evaluate some things to try to determine what happened.  the nose cone landing so far away was kind of surprising too, there didn’t appear to be a hard impact right on the nose of it but it still came undone and flew that far.

### Alexander Alan Arnold, 2026-10-20

@Eric Brewer equipment requested and RMA generated, awaiting return to aid in investigation.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V918_B30N_20261009T171329Z.zip | archive | 45686 | 2026-10-09 | listed only |
| Pics.zip | archive | 13743 | 2026-10-09 | listed only |
