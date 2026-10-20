# ENG-2998: VXE 438 Launch Aborts, uncommanded motor spin after second abort, R Aft rotor broken likely from contact with the aircraft stand.

- **Issue type:** Problem
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Medium
- **Created:** 2023-03-22
- **Updated:** 2025-06-02
- **Resolved:** 2023-11-09
- **Reporter:** Cameron Chapman
- **Assignee:** Cameron Chapman
- **Creator:** Cameron Chapman
- **Links:** relates to VA-238 (R Aft ESC needs to be inspected due to prop strike.   ); relates to VXEP-118 (VXE 438 Launch aborts, uncommanded blade spin after landing. Right aft prop strike.); relates to FS2-1057 (Implement user-focused messaging system between GCS and aircraft to indicate understood, causal behaviors); relates to GCSS-34 (Implement user-focused messaging system between GCS and aircraft to indicate understood, causal behaviors); relates to VXEP-183 (Establish aircraft grounding, bonding, shielding, etc. status and roadmap.)

## Description

Aircraft 438, TALSA East, Camp Lejeune, experienced two launch aborts, the second resulting in aircraft damage, during flight operations Monday night.
 
438 flew four flights earlier in the evening without incident. After sunset the students prepared for night operations. The launch wizard was completed without incident and the aircraft was armed for launch. Being that it was dark it was difficult to see but the aircraft appeared to liftoff about one foot before aborting and landing to the left of the stand. The VTOL system was still armed (red light flashing). The VTOL control window indicated a launch abort for a VTOL system failure. The system could not be disarmed with the “cut motors and safe vehicle” button in the software until the FDR was downloaded and AAR saved. After the AAR was saved the aircraft was safed. The aircraft was inspected and there was no damage.
 
A second flight was attempted. The launch wizard was again completed without incident. On this flight the aircraft lifted to approximately two feet and again aborted. After landing the VTOL system stopped, but because of the angle it could not be immediately determined if the system was still armed. A few seconds after touching down the lift rotors briefly spun up and stopped. The VTOL control window indicated a launch abort for a VTOL system failure and a magnetometer error. Again, the FDR was collected and AAR saved. The aircraft was made safe by pressing the cut motors and safe vehicle button. Upon inspection it was noticed that the forward right lift rotor was broken in two, likely from contact with the aircraft stand. It’s unclear if it occurred during the landing or subsequent throttle blip.
 
This aircraft is in the battery configuration. GCS software 5.0 6.4. Aircraft was not operating with the most recent firmware release.
 
This aircraft is not the same aircraft that I mentioned last week had a sensor error during the LW for an IMU mismatch.
 
Dan

## Comments (13)

### Cameron Chapman, 2023-03-22

@John Clark is anyone from your team available to review this data? The issues seem similar to previous ones. Would they likely have been fixed/improved by the new release (understood we will probably need data review to determine that).

### Daniel Lloyd, 2023-03-24

Added AAR’s and changed tail number to 438

### John Clark, 2023-03-27

@Cameron Chapman, investigation points to magnetometer error and attempting flights in spite of that.

### Cameron Chapman, 2023-03-27

@Daniel Lloyd I recommend returning the 438 CW and booms for magnetometer and ESC evaluation. @Sean Odell @Former user

### Daniel Lloyd, 2023-03-27

It sounds like all the issues experienced on these flights are fixed in the latest firmware release. Is this worth the effort to analyze?
Returning the booms for ESC evaluation will likely result in cancellation of classes at the TALSA. Would have to confirm with Matt on that. The aircraft has flown 8-10 flights since the mishap flight.

### Daniel Lloyd, 2023-03-27

In response to John’s comment, “investigation points to magnetometer error and attempting flights in spite of that.”
There was no indication to the operator of a magnetometer error. The operators did not bypass or ignore any system warnings.

### Cameron Chapman, 2023-03-28

@Daniel Lloyd I think the latest firmware has a flag to indicate if the primary magnetometer is not functioning, but it would not fix a hardware issue like this one seems to have experienced during those flights. 
Given the ESC operation 8-10 flights after the prop strike, it sounds like the ESC is in good working condition and doesn’t need to be inspected. That recommendation was if the aircraft was returned.  
I think we could put this incident in a monitor state, and report back during the TALSA classes the number of flights without a repeat issue and any repeat occurrences.

### Cameron Chapman, 2023-08-24

Linking subtasks to parent.

### Cameron Chapman, 2023-11-06

@Daniel Lloyd following up on some old issues, did this ever reoccur on 438? Is 438 still flying? 
@Craig Burton , are you able to link to the issue to improve launch abort reason descriptions?

### Craig Burton, 2023-11-07

@Cameron Chapman @David Grosher I linked both the FS and GCSS tickets.

### Daniel Lloyd, 2023-11-08

This has not reoccurred. The aircraft is one of MARSOC’s training aircraft and has completed 60-80 flights since that incident.

### Cameron Chapman, 2023-11-08

Thanks @Daniel Lloyd for the updates. 
Updated root cause. Issue has not repeated in 60-80 flights, so the magnetometer fault may have been environmental. CAs identified. This seems ready to close. @Greg Fryer @Pat Wells @Former user is there an official closure process for MARSOC incidents?

### Pat Wells, 2023-11-09

@Cameron Chapman this issue pre-dates me and I was not tracking it on my side or with MARSOC.  Per Dan’s comments below the aircraft seems to be functioning properly now after several flights.  Please close out as you deem necessary.

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V438_230320_200305_pack.zip | archive | 1276 | 2023-03-24 | listed only |
| T95_V438_230320_201705_pack.zip | archive | 2023 | 2023-03-24 | listed only |
| [Vehicle 499 incident report.pptx](attachments/13274_Vehicle%20499%20incident%20report.pptx.md) | pptx | 70 | 2023-03-27 | converted |
