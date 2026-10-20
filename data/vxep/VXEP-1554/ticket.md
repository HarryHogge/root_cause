# VXEP-1554: VXE-593 Aborted launch

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2025-10-16
- **Updated:** 2026-03-02
- **Resolved:** 2025-12-16
- **Reporter:** Michael Mohr
- **Assignee:** Eric Brewer
- **Creator:** Michael Mohr
- **Labels:** MOLSON
- **Links:** is cloned by VXEP-1586 ( VXE 593 smoking fuel cell)
- **Customer:** MOLSON
- **Vehicle Tail Number:** 593
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

During the take-off we had a magnetometer fail and the aircraft aborted launch and landed safely.  We have attached the AAR for the flight.
Post landing while disassembling the air vehicle we notice smoke coming from the nose cone we proceed to remove the nose cone and the fuel all and it was smoking internally (see attached picture and video)
We operated in the following configuration:
VXE30 in fuel cell configuration 
E140Z G2 gimbal
 
No additional payloads.
Aircraft SN: 593
Fuel Cell SN: D4500799

## Vehicle Configuration

Standard VXE30
Fuel Cell
E140 G2-Z

## Root Cause

Looking at AAR from flight on 17Oct2025, there seems to be no anomalies or mag/IMU issues. We have decided to BT this as there was most likely rebar or some type of metal in the concrete pad that was flown from when the abort occurred.

## Comments (13)

### Michael Mohr, 2025-10-16

@Sean Wendling Can you weigh in on the fuel cell for this also please?

### Greg Fryer, 2025-10-16

@Tom Westrich @Christopher Ridgard Tagging just for awareness on this “fuel cell smoking” issue. Sean W got tagged already.

### David Grosher, 2025-10-16

@Eric Brewer can you look into the Mag portion of this issue?

### Eric Brewer, 2025-10-17

@David Grosher there is a pretty significant disturbance in the mag readings right when the vtol system spools up.  The attitude estimate on vtol becomes inaccurate leading to the abort.  Close to touchdown the mag readings ramp up even further before the magnetometer is (correctly) declared failed.  

[embedded image-20251017-150806.png]
I double-checked the SCO logs when this bird went out and the mag readings look clean.  I’d be curious about the following:
1. When the vehicle is powered back on, do the mag readings now look normal?
2. Could there have been an electrical issue? Either with the VTOL system or potentially the E140 ground loop issue?  Does the ground loop issue affect the vtol mag? I thought it was typically limited to the fixed-wing mag.  The throttles have already ramped up to 75% or so before the mag magnitude increases.

I would have thought potentially an environmental issue (i.e. mag disturbance on the runway) but this doesn’t really track since the disturbance follows the vehicle up 100'.

### Eric Brewer, 2025-10-17

@Michael Mohr probably worth asking the customer about item 1 above.  Have them power up on the ground and then send us an AAR.  

Let’s get some answers internally about the E140 ground loop before we reach out about that.

### Eric Brewer, 2025-10-31

@Michael Mohr any updates on this?

### Michael Mohr, 2025-10-31

@Eric Brewer I requested a new ground run AAR on the 20th with no reply. I’ll request again today.

### David Grosher, 2025-12-11

@Michael Mohr Any news here?

### Michael Mohr, 2025-12-11

@David Grosher Reached out again today to see if they had a chance to run through a launch wizard and get some additional data.

### Michael Mohr, 2025-12-16

@David Grosher @Eric Brewer Uploaded files we received from customer. They said they haven’t run the fuel cell yet but “did a mag calibration and a small flight on Oct 17, which was a couple days after the incident.” He can also do a ground run of 593 later this week if needed to get more data. Also, FYI, 593 is scheduled to go to SLO for ADV NAV upgrade in Jan.

### Eric Brewer, 2025-12-16

@Michael Mohr thanks.  The mag values are definitely noisier than when it was here for SCO, but the flight performance looked ok in the latest flights and the mag did not have the large disturbance that we observed during the abort.  That likely points to the issue with the fuel cell being related to the mag disturbance.

I didn’t see evidence of the mag calibration - the two latest AARs from 10/17 show the same mag cals as when it left the factory.

### Michael Mohr, 2025-12-16

@Eric Brewer Update from customer: They moved 100 feet from original location (concrete pad) into grass for this most recent flight. That is probably why it looks better.

### Michael Mohr, 2025-12-16

Probable rebar in the concrete pad where the IMU/MAG issue occurred

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Fuel Cell Pic 1.png | image | 244 | 2025-10-16 | listed only |
| Smoke from fuel cell.mp4 | video | 1095 | 2025-10-16 | listed only |
| T95_V593_251015_164320_pack.zip | archive | 1190 | 2025-10-16 | listed only |
| image-20251017-150806.png | image | 116 | 2025-10-17 | listed only |
| T95_V593_251017_114428_pack.zip | archive | 685 | 2025-12-16 | listed only |
| T95_V593_251017_143205_pack.zip | archive | 3189 | 2025-12-16 | listed only |
| T95_V593_251017_150518_01_pack.zip | archive | 4199 | 2025-12-16 | listed only |
| T95_V593_251017_150518_pack.zip | archive | 1579 | 2025-12-16 | listed only |
