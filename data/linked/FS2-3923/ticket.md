# FS2-3923: Land Immediately Command from VSM to XCOMM not receieved

- **Issue type:** Bug
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2025-11-11
- **Updated:** 2025-12-15
- **Resolved:** 2025-11-17
- **Reporter:** Scott Whitney
- **Assignee:** Wesley Reynolds
- **Creator:** Scott Whitney
- **Environment:** BLK35x
OGCSC 1.3.1
Avionics 6.5.1
LEMB
- **Parent:** FS2-3934 Investigation: Land Immediately Not Accepted 
- **Links:** relates to VXEP-1592 (VXE-881 Would not accept Land immediately Commands)
- **Epic Link:** FS2-3934
- **Sprint:** FS2 Sprint 35

## Description

Steps for Testing:
- Configuration
- BLK35x
- OGCS 1.3.1
- Avionics 6.5.1
- LEMB?
- Default mission - normal landing
- Make sure the vehicle is in FW flight
- Command normal RTB landing
- Between IP4 and IP5
- Inject VTOL nav fault
- Confirm abort and goes to to ELZ
- Select Land Immediately 6 times
- Change landing to Primary Landing
- Command Land Immediately (write down what the vehicle action is)
- Expect that it will reject land immediately commands.


Repeat test to verify ideal behavior:
- Default mission - normal landing
- Make sure the vehicle is in FW flight
- Command normal RTB landing
- Between IP4 and IP5
- Inject VTOL nav fault
- Confirm abort and goes to to ELZ
- Change landing zone from ELZ back to PLZ.
- If required - retask to a waypoint that’s low enough to allow vtol landing.
- Select Land Immediately
- Verify VTOL transition and landing

## Comments (6)

### Wesley Reynolds, 2025-11-11

Here is the data from the incident: [embedded: AAR_V881_20251110T101020Z.zip]

### Wesley Reynolds, 2025-11-13

This PowerPoint serves as the report for this incident: V881_LandImmediatelyNotAccepted.pptx

### Wesley Reynolds, 2025-11-14

Eric: “Updated slides here, please review.  I think all we are waiting on is HIL confirmation of the behavior as well as confirmation that if PLZ had been activated it would have done LI to vtol as expected.”

### Wesley Reynolds, 2025-11-14

I uploaded the AAR and a video recording of the behavior here: SharePoint Link
Findings (Video timestamps included)
- When the VTOL gets a GPS Fault during the Primary Landing Pattern (between IP4 and IP5, in particular), the vehicle will go to the ELZ after passing IP5 and before attempting to transition.
- [ 1:50 - 2:35 ]
- When this happens (vehicle automatically reroutes to ELZ), the OGCS does not display a checkmark in the radio button next to the "LAND ELZ" button.
- [ 2:25 - 3:10 ]
- If the LAND NOW button is pressed, the vehicle will perform a glide land immediately. (The radio button suggests that it should be a vertical land immediately, but it is a glide land immediately)
- [ 6:25 - 7:40 ]
- The glide land immediately can be aborted. Admittedly, the way I tested this didn't make it clear whether the "ABORT LANDING" or the "LAND PLZ" triggered the abort.
- [ 7:35 - 8:00 ]
- While the vehicle is in route to the ELZ, if the GPS Fault is cleared AND the user explicitly presses the radio button next to the "LAND PLZ" button (this button will already have a checkmark, but click it again), then the user click the "LAND NOW" button, the vehicle will perform a vertical land immediately and have nudge controls.
- [ 10:35 - 13:15 ]

### David Grosher, 2025-12-11

@Wesley Reynolds Did we work with @Josh Burrell to add information in the log to describe the expected LI behavior in the manual?

### Josh Burrell, 2025-12-15

@Mark Spence FYSA, can you look at this and see if this is something we captured or not?

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V881_20251110T101020Z.zip | archive | 38382 | 2025-11-11 | listed only |
