# VXEP-1547: VXE 930 One or more VTOL Sensor fail

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-10-08
- **Updated:** 2026-05-05
- **Resolved:** 2026-05-05
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Eric Brewer
- **Creator:** Alexander Alan Arnold
- **Labels:** MOLSON, RCCA, Weekly-incident-tracker
- **Links:** split to VXEP-1557 (VXE 930 Main battery to avionics power chain led to emergency landing); relates to FS2-3760 (Testing for Observed NovAtel Heading Drift); relates to VXEP-1774 (VXE-933 During launch wizard, Error pops up saying "The autopilot has detected that one or more of its sensors have failed")
- **Customer:** MOLSON
- **Vehicle Tail Number:** VXE 930
- **Vehicle Configuration:** ADV NAV VXE 30, Battery config
- **Corrective Action:** Software update will automatically correct large heading errors during preflight.
- **Plan:** Implement corrective action.
- **Issue Status:** Implementing corrective action to be released in version 6.7.1.
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

Operator Statement 
“During liftoff procedure on Tail 930 of one of our new adv nav birds (Tail 930), this fault has shown 3 times, always at the “Shield Pitot” step. Between these faults displaying, we have swapped batteries, power cycled the bird. In one case, this fault cleared and we proceeded with launch - immediately after takeoff and transition to VTOL, we got a fault indicating battery is below 10%, rapidly degrading to below 5%, where we recovered the bird safely. We tested the battery upon landing - the main battery was 73% with all cells level. HLB was down to 30%. When tail 930 was lifting off, there was a weird stall about 10 ft off the ground. Temperature is 8 degrees Celsius, winds are 9 mph, gusting 15 mph.”

## Root Cause

Motion during initialization can cause the INS to disagree with the fixed-wing and vtol processors.  This results in a VTOL sensor fault that is difficult to understand/repair.

## Comments (25)

### Alexander Alan Arnold, 2025-10-09

@Eric Brewer Thank you! if other Adv Nav user report the issue, i will create a seperate ticket and link it to this one.

### David Grosher, 2025-10-16

@Alexander Alan Arnold I suggest splitting this investigation into two, one for the heading discrepancy and another for the battery.  Regrading the battery, there is a known issue with the model in the battery checker using an incorrect chemistry model for the battery, yielding incorrect values.

### Drew Hildreth, 2025-10-17

@Eric Brewer @David Grosher With the VTOL Sensor failures being a disagreement between Novatel and the APs do we need to start looking into an Advisory Notice for this? Is there any concern with the customer flying this aircraft knowing this is an issue? I am sure they will be looking for some sort of documentation.

### Drew Hildreth, 2025-10-17

@Alexander Alan Arnold @Michael Mohr Let’s make sure this gets broken into two separate tickets like Dave asked below.

### Eric Brewer, 2025-10-20

@Drew Hildreth I think it would depend how frequently this issue is occurring.  Does his occur often in the flight testing that you’ve been doing?  The heading disagreement should not be a flight safety concern as the launch wizard will prevent launch if the disagreement is greater than 20 degrees. @David Grosher @Alexander Alan Arnold FYI.

### Drew Hildreth, 2025-10-20

@Eric Brewer Thank you for this. We aren’t experiencing these issues here. This is a customer asset that was presenting the issue. We will continue to monitor and if like issue present themselves, we will look into writing an AN at that time.

### David Grosher, 2025-10-31

@Eric Brewer If you are tracking this larger investigation elsewhere can you link it here.

### Eric Brewer, 2025-11-05

@David Grosher linked above to the testing ticket.

### Jackson Riley Curvin, 2025-11-20

I think that this investigation should be closed, after looking at the AAR
 VXE-SUAV was on 6.5.0
 The XCOMM firmware was from 6.5.1
The VTOL firmware was from 6.5.0 
@David Grosher @Eric Brewer

### David Grosher, 2025-12-11

@Jackson Riley Curvin The VTOL firmware did not change between v6.5.0 and v6.5.1. And there should be no issue with using the older GCS. However, if the v6.5.0 FW AP was used with v6.5.1 XCOMM that would be concerning.

### Scott Lovett, 2026-02-02

@Eric Brewer Is there further action for this ticket required?

### Eric Brewer, 2026-02-02

@Scott Lovett the testing/investigation above is still ongoing but I think the relation to this incident can be closed.

### Scott Lovett, 2026-02-02

Overall investigation will be ongoing but the investigation related to VXE-930 will be closed.

### Tim Muchmore, 2026-02-25

@Eric Brewer @Drew Hildreth @Michael Mohr A similar thing happened last week with VXE928 (VTOL Sensor Failure). Could it have been related to the ‘observed novatel heading drift?’

### Eric Brewer, 2026-02-25

@Tim Muchmore definitely could be - best way to confirm is to review an AAR.  We are working on a fix for this but it’s a little ways out from rolling into the baseline software.

### Tim Muchmore, 2026-02-25

@Eric Brewer Thanks. Is there a way to pull an AAR if you can’t get past the launch wizard? Same process?

### Eric Brewer, 2026-02-25

@Tim Muchmore yep same process in OGCS.  If you’re on legacy GCS it’s tools->produce after action report.

### Scott Lovett, 2026-03-25

Re-opened until a fix is deployed. v-933 exhibited the same issue/symptoms

### Cameron Chapman, 2026-03-25

@Eric Brewer I recommend filling out C/CA and GS reviewing that is acceptable prior to closing issues. FYI @Scott Lovett

### Eric Brewer, 2026-05-05

Corrective action implemented in software version 6.7.1 to be released soon.

### Tim Muchmore, 2026-02-25

@Eric Brewer Thanks. Is there a way to pull an AAR if you can’t get past the launch wizard? Same process?

### Eric Brewer, 2026-02-25

@Tim Muchmore yep same process in OGCS.  If you’re on legacy GCS it’s tools->produce after action report.

### Scott Lovett, 2026-03-25

Re-opened until a fix is deployed. v-933 exhibited the same issue/symptoms

### Cameron Chapman, 2026-03-25

@Eric Brewer I recommend filling out C/CA and GS reviewing that is acceptable prior to closing issues. FYI @Scott Lovett

### Eric Brewer, 2026-05-05

Corrective action implemented in software version 6.7.1 to be released soon.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T115_V930_251008_102001_pack.zip | archive | 2040 | 2025-10-08 | listed only |
| image-20251008-232057.png | image | 30 | 2025-10-08 | listed only |
| image-20251008-234740.png | image | 25 | 2025-10-08 | listed only |
| one or more vtol sensors fail.jpeg | image | 796 | 2025-10-08 | listed only |
