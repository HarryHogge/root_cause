# GCSS-362: Implement lockouts or significant warnings to prevent operators starting VTOL landing at too high of an altitude.

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-07-23
- **Updated:** 2025-04-01
- **Resolved:** 2025-04-01
- **Reporter:** Cameron Chapman
- **Assignee:** Eric Engstrom
- **Creator:** Cameron Chapman
- **Fix versions:** 6.4.0
- **Parent:** FS2-2342 VXEP-512 - Investigation and GCS CAs for Transition to VTOL above 2000ft
- **Links:** Cannot finish until linked issue is finished. VXEP-512 (VXE 556 vehicle transitioned to VTOL at 1200ft, operator unable to abort. HLB depleted and crashed); is cloned by OGCS-47 (Implement VTOL Land Now Lockout/Warnings); relates to VXEP-651 (VXE 594 Operator commanded RTB, AV went directly to IP5); relates to GCSS-425 (Improve 'VTOL Too High' warning when commanded to IP4.)
- **Epic Link:** FS2-2342
- **Sprint:** GCSS Sprint 26, GCSS Sprint 27, GCSS Sprint 31, GCSS Sprint 28, GCSS Sprint 24, GCSS Sprint 25, GCSS Sprint 29

## Description

**Request:**

Upon the operator triggering a vertical landing that meets any of the following criteria:
- would result in less than 200ft margin of remaining vertical lift system energy at completion of the landing
- would cause the vehicle to start descent from greater than 1000ft AGL

the GCS shall display a warning and require positive confirmation from the operator. 
**UI / Message Box:**

Warning: Landing Energy
Are you sure you want to command a landing?  The vertical lift system may not have enough energy to safely land the vehicle.  AGL at landing is estimated to be {height}ft greater than remaining energy.
[Proceed With Unsafe Landing] [Cancel Landing]

[Cancel Landing] button should be the default choice if the user clicks <Enter>
It is preferable that the button text does not just say ‘OK’ and ‘Cancel’ – it should say the actions being taken, in this case ‘Proceed With Unsafe Landing’ and ‘Cancel Landing’
**Notes:**

This warning should be shown for all methods of triggering a landing with an invalid altitude, including but not limited to:
- Commanding Land Immediately from too high of an AGL altitude
- This already has a warning, minor work to make it consistent.
- Commanding RTB with too high of a landing zone AGL
- This normally would be caught during mission checkout/simulation but there is a corner case where HLB has less charge than expected during flight.
- Commanding Go To IP4 without adequate time to descend (skipping IP2)
- The warning does not need to be shown if there is enough space for the vehicle to descend before reaching the LZ.  Use a conservative (worst case) descent rate calculated over the distance from the vehicle to the LZ.
- This is the primary motivation for the feature - warn operators about commanding direct to IP4.
- It isn’t possible to command a Go To IP3 or IP5, but if there were this check would also apply.

**Existing Behavior:**

The GCS currently warns about ‘Land Now’ when not enough energy is available.  It checks against exact AGL and does not include a buffer.
[embedded: image-20240930-212938.png]

[embedded: image-20240930-213000.png]

## Comments (17)

### David Grosher, 2024-09-24

@Ted Trowbridge  We should move this ticket to the GCSS project.

### Ted Trowbridge, 2024-10-02

@David Grosher @Scott Whitney  Desired behavior has been captured, ready for implementation and moved to GCSS project.

### Michael Berger, 2024-12-06

@Ted Trowbridge should the dialog message use meters when meters are selected for the altitude units?

### Ted Trowbridge, 2024-12-06

@Michael Berger if the system allows using meters for all the other altitude readouts then yes we should maintain consistency and show meters here too.

### Michael Berger, 2024-12-08

@Ted Trowbridge 
For the basic Land Immediately case
Display a warning in either of these cases.
- would result in less than 200ft margin of remaining vertical lift system energy at completion of the landing
- would cause the vehicle to start descent from greater than 1000ft AGL

Message
Are you sure you want to command a landing? The vertical lift system may not have enough energy to safely land the vehicle. AGL at landing is estimated to be {height}ft greater than remaining energy.

If you are at 150 ft agl and the energy available is 300 ft which is 150 ft of margin, then a warning should be displayed, but the message would end with:
AGL at landing is estimated to be -150 ft greater than the remaining energy.
This seems very confusing.

### Michael Berger, 2024-12-08

@Ted Trowbridge Would there be a different message for the greater than 1000 ft AGL case?

### Ted Trowbridge, 2024-12-09

@Michael Berger 
This is my updated suggestion for the message:
- Case #1: Estimated to lose power before landing:

Are you sure you want to command a landing?  The vertical lift system may not have sufficient energy to safely land the vehicle.
Vertical lift system is estimated to lose power at {estimatedAgl}ft AGL during landing.

- Case #2: Estimated to be less than 200ft safety margin at landing:

Are you sure you want to command a landing?  The vertical lift system may not have sufficient energy to land the vehicle within safety margins.
Vertical lift system is estimated to land with only {esimatedReserve}ft remaining energy.

### Michael Berger, 2024-12-09

@Ted Trowbridge
The code will verify that the Primary (VTOL) LZ is selected before looking for these issues. This is not a problem if the Emergency LZ is selected.
Several more implementation questions:
should the 200 ft value. (margin of remaining vertical lift system energy at completion of the landing) be hard coded or configurable/overridable from the gcs.ini file? I think this would make sense to allow updates after testing.

Also, what message text would be shown for the. start descent from greater than 1000ft AGL case.

### Ted Trowbridge, 2024-12-09

@Michael Berger 
The 200ft should be configurable from the gcs.ini
I don’t think we need to differentiate a >1000ft AGL case.

### Michael Berger, 2024-12-09

@Ted Trowbridge @Scott Whitney 
VTOLpower 499ft power, 300 ft agl, safety margin 200 ft
[embedded: image-20241209-234600.png]
VTOLpower meters 499 ft power, 300 ft agl, safety margin 200 ft
[embedded: image-20241210-004032.png]
VTOLpower meters 200 ft power, 300 ft agl, safety margin 200 ft
[embedded: image-20241210-004332.png]
VTOLpower 200 ft, 300 ft agl, safety margin 200 ft:
[embedded: image-20241210-004509.png]
VTOLpower 50 ft, 300 ft agl, safety margin 200 ft

Implemented for Land Immediately Now.

The safety margin can be changed by added to the gcs.ini file
[VTOLTOOHIGH]
SafetyMargin=200
if not found it defaults to 200ft.

### Michael Berger, 2024-12-09

@Ted Trowbridge @Scott Whitney 
Issues with implementing on goto IP4:
We have no way of knowing what the power available for landing will be when the vehicle gets to the LZ. We only know the current value.
Issue with implementing on RTB:
The descent rate between the current position and the LZ is not known to the GCS and is vehicle dependent. Also the vehicle will not begin descending until it gets to IP1. After IP1, it will orbit down to the pattern altitude.

Additionally training should be updated to not train operators to do a GOTO IP4 command unless they absolutely sure that they are already at the pattern altitude.

Input/suggestions appreciated.

### Ted Trowbridge, 2024-12-10

@Michael Berger Nice job on the dialogs, it looks great!
I think a generic warning about directing straight to IP4 should be implemented.  It would be a third variant of the dialog, my suggestion would be:
Are you sure you want to go directly to IP4 prior to landing?  The vehicle may not have enough time to descend to a safe altitude for landing.
ACTION: Command landing through IP1 to descend to a safe altitude before landing.

Follow on question, what do you mean by “the vehicle will not begin descending until it gets to IP1” in the case where we direct to IP4 and it never intercepts IP1?  Will the vehicle not descend until it reaches the IP4 ground track?  What is the behavior?
Ideally we would be only show this new variant if there was reason to believe the vehicle would not descend enough in time.  However, since this is an unusual command I think the warning can be shown every time.

### Michael Berger, 2024-12-11

My comment “the vehicle will not begin descending until it gets to IP1. After IP1, it will orbit down to the pattern altitude.” was referring to the case of Commanding RTB with too high of a landing zone AGL. At the time of the RTB be command we have no way of knowing what the agl and the HLB power will be @Ted Trowbridge when the vehicle starts the VTOL descent.

### Michael Berger, 2024-12-11

@Ted Trowbridge I believe that the real solution for this is in https://jenaero.atlassian.net/browse/FS2-2318This should be done in the firmware rather than the GCS. Other than the Land Immediately case, we don’t have the proper information in the GCS to make the right decision.

### Michael Berger, 2024-12-11

New dialog screenshot (taken on XP so color different. IP4 message
[embedded: image-20241212-041748.png]

### Scott Whitney, 2025-03-25

@Eric Engstrom is this complete?

### Eric Engstrom, 2025-04-01

This is complete, marking as Done.

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240930-212938.png | image | 1292 | 2024-09-30 | listed only |
| image-20240930-213000.png | image | 1052 | 2024-09-30 | listed only |
| image-20241209-234600.png | image | 13 | 2024-12-09 | listed only |
| image-20241210-004032.png | image | 12 | 2024-12-09 | listed only |
| image-20241210-004332.png | image | 12 | 2024-12-09 | listed only |
| image-20241210-004509.png | image | 12 | 2024-12-09 | listed only |
| image-20241212-041748.png | image | 63 | 2024-12-11 | listed only |
