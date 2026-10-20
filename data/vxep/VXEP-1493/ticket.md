# VXEP-1493: VXE-863 Flight anomalies

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-08-29
- **Updated:** 2025-10-29
- **Resolved:** 2025-10-29
- **Reporter:** Michael Mohr
- **Assignee:** David Grosher
- **Creator:** Michael Mohr
- **Labels:** CBP, Edge_Asset
- **Vehicle Tail Number:** 863
- **Other Stakeholder (as required):** Jeremy White
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround
- **Components (EA Aircraft):** Aircraft, full assembly

## Description

During our flight today, it appeared that the AGL being recorded on the GCS was higher than our actual altitude.  We have flown many flights in this area, and although the GCS registered as 400-600 AGL, it consistently appeared to me and the payload operator that our actual altitude was lower.
The SA video from the flight will be included in the google drive link.  At the 8-minute mark, the aircraft goes nose down sharply before leveling off and then nose down again.  I have not seen this behavior before with the aircraft.  I will note that the area we were flying in is mountainous terrain with very steep (2-400 ft near vertical drops) valleys, but this is the only time I have noted this sharp nose down behavior while flying in this area.
During landing, being that the aircraft was orbiting around us at 400 ft, rather than RTB, I commanded a go to IP4.  The aircraft appeared to maneuver as expected and then transitioned to VTOL at 300 AGL.  At this point, it appeared that the aircraft was hovering but not coming down.  I believe I looked at the GCS and it showed an AGL of around 280.  10 seconds later, it still showed 280 feet.  It was then noted by me and the ground crew, that the aircraft was indeed descending, however it appeared much slower than the normal landing decent.  Decent was also manually paused near the ground, as the normal 20ish foot automatic pause did not appear to happen. iPhone video of landing also in google drive link.
After talking to global support, we started to take the aircraft apart and began inspecting the components.  I noted one of the under-wing sensors appears cloudy or has moisture in it.  See attached image, which is also included.
Customer is CBP and aircraft is Edge asset on loan to CBP

## Vehicle Configuration

VXE30
Battery

## Comments (18)

### David Grosher, 2025-08-29

@Michael Mohr Which AAR is the issue in?

### Michael Mohr, 2025-08-29

@David Grosher Should be T95_V863_250829_053247. The others are for comparison.

### Michael Mohr, 2025-08-29

Also, for weather considerations, he did mention that it was drizzling rain slightly.

### Jackson Riley Curvin, 2025-08-29

@David Grosher looks like it lost link right after a sim was generated.

### David Grosher, 2025-08-29

[embedded image-20250829-201508.png]

Baro Altitude appears to have had its calibration adjusted mid flight around where there were some altitude disturbances. I haven’t observed this before and will continue to look into it. @Michael Mohr

### Michael Mohr, 2025-08-29

@David Grosher Thank you Dave!

### Michael Mohr, 2025-09-02

@David Grosher Should this aircraft be grounded until we can figure out the issue? They only have the one at their location.

### David Grosher, 2025-09-02

@Michael Mohr the conservative approach would be to ground the vehicle, but i don’t know that it is necessary given that the vehicle safely recovered. I think someone with some context into the mission CONOPS and risk appetite of the customer would have to make that call.

### Jackson Riley Curvin, 2025-09-02

@David Grosher  this is a comment from an older ticket about Sim issues does this relate to the issue here?
[embedded image-20250902-154540.png]
https://jenaero.atlassian.net/browse/VXEP-220

### David Grosher, 2025-09-02

@Jackson Riley Curvin This is not related to the current issue. That ticket is related to a frozen GCS. I don’t believe that is what is described here.

### Jackson Riley Curvin, 2025-09-02

@David Grosher ok I had just saw the multiple simulations that were ran before a loss of link occurred.

### Michael Mohr, 2025-09-08

@David Grosher How long into the flight was the reset and do we know what the probable cause was? I am going to advise them to fly this aircraft, but exercise increased caution during recovery.

### David Grosher, 2025-09-08

@Michael Mohr It was about 10 minutes into the flight.

### Michael Mohr, 2025-09-09

@David Grosher Is there any data to support that the distortion/moisture in the LRF lens pictured caused the abnormal recovery? I was informed that these are not sealed so this could present itself as a problem again. Also, do we have any idea why the calibration adjusted?

### David Grosher, 2025-09-09

@Michael Mohr They saw a slow descent at ~300 ft altitude but the LRF does not get reliable data until it reaches 80-100 ft. It is likely that the vehicle thought it was lower to the ground because of the baro cal reset, which would have resulted in a lower vertical speed setpoint. The LRF data looks normal, I don’t think moisture impacts the laser frequency in the LRF.  This needs to be verified, but I don’t believe it is an issue.

### Jeremy White, 2025-09-09

@David Grosher This is not a customer asset. It is a bailed VXE30 due to the prolonged delays with Block 40.

### Michael Mohr, 2025-10-29

Replacement ADP sent out and replaced on 9/30/2025. Flight anomalies were resolved.

### Michael Mohr, 2025-10-29

Replaced ADP and flight anomalies went away.

## Attachments (12)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 20250829_070355.jpg | image | 2517 | 2025-08-29 | listed only |
| 863 baro agl.png | image | 19 | 2025-08-29 | listed only |
| 863 loss of link after sim.png | image | 119 | 2025-08-29 | listed only |
| 863 wind conditions.png | image | 31 | 2025-08-29 | listed only |
| MISB-08292025-053258-1-0.mpg | video | 66661 | 2025-08-29 | listed only |
| T95_V863_250827_111538_01_pack.zip | archive | 2872 | 2025-08-29 | listed only |
| T95_V863_250828_054332_pack.zip | archive | 4120 | 2025-08-29 | listed only |
| T95_V863_250828_085910_pack.zip | archive | 3814 | 2025-08-29 | listed only |
| T95_V863_250829_053247_pack.zip | archive | 2419 | 2025-08-29 | listed only |
| VID-20250829-WA0000.mp4 | video | 14116 | 2025-08-29 | listed only |
| image-20250829-201508.png | image | 50 | 2025-08-29 | listed only |
| image-20250902-154540.png | image | 58 | 2025-09-02 | listed only |
