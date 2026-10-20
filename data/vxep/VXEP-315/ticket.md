# VXEP-315: VXE 459 Overshoot of LZ Mishap on landing, operator unable to nudge

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-03-29
- **Updated:** 2026-09-03
- **Resolved:** 2024-08-23
- **Reporter:** Pat Wells
- **Assignee:** David Grosher
- **Creator:** Pat Wells
- **Labels:** GNSS-Rate, MARSOC, Software, Weekly-incident-tracker
- **Links:** relates to VXEP-12 (TPTR-87 VXE 511 VTOL Connector Issues 516 CW. Contains Main connector/contact C/CAs); relates to VA-93 (Record typical, max, and max tested lift current and voltage profiles. Save test data to confluence. Establish and implement limits and abort if exceeding.); relates to FS2-1697 (Fixed-wing helper implementation results in excessive landing overshoot.); relates to FS2-1696 (Reduced fixed-wing helper throttle.); relates to FS2-1672 (V459 Incident Investigation); relates to FS2-1807 (Investigation 6.2.9 landing overshoot); relates to FS2-1862 (VXEP-315 Landing Performance Improvements); relates to RMA-256 (VXE-459 240605); relates to VXEP-427 (VXE 430 abnormal landing behavior); relates to VXEP-412 (VXE 426 Overshoot on landing, becoming progressively worse); relates to FS2-1999 (Implement Fixed wing Helper Fix)
- **Customer:** MARSOC
- **Vehicle Tail Number:** 459
- **Issue Status:** Investigation Closed.
- **Incident Type:** Aircraft Damage
- **Severity:** 1 - Flight Critical

## Description

Information received from operator:
During the transition 3 of the 4 Vtols turned on with the last one kicking on 1-2 seconds later. I do not know if that is related. The VXE proceeded to over shoot the landing zone by apx 500M. The operator hit abort but sense the AC was already transitioned and it had no effect.
 The aircraft hovered back to its landing location but to the rear of it by about ten 10 meters where it began to descend, he activated user landing and tried to nudge it with no response. At that point I attempted to nudge it as well with no visual response on the aircraft, I did momentarily look to verify user landing controls were active and saw the screen was up.
 The VXE descended onto a wire and caught the rear tail pad and the nose dropped down to face vertical, with the AC hanging about 2-3 feet off the ground and the VTOL Motors on. I informed the operator I would need him to cut and safe motors in a moment. The plan was to stop it from dropping once the motors were safe. As I approached the VXE the operator hit the Safe and cut and it dropped the 2-3 feet right onto the front VTOL boom.
 During the flight we used Udrive so i'm confident he XBOX controller was working as we also had a green XBOX Icon.
 There were no issues during the launch transition.
 Attempting to download the AAR from the produced ARR screen failed three times before working. see attached for the files.

## Corrective Action

Short-term fixes​
- Use logic to fix case where the vehicle is flying past TDP and FW helper is making situation worse (relatively quick fix)​
- Use ground velocity to scale/gate when FWH can be activated​ (See VXEP-322).  See implementation on remotes/origin/dev_ebrewer_landingimprovements2.
- Reduce FWH output at higher winds to reduce AoA and avoid stall (quick fix)​, (see VXEP-323).  See implementation on remotes/origin/dev_ebrewer_landingimprovements2.
- Examine potential changes to VTOL entry timeouts to improve performance. (see VXEP-335)
- Update GPS acceleration correction to account for varying dt.  See powerpoint here.
- Consider providing some operator feedback on how much nudge commands have shifted target TDP.  Perhaps a dot on the map?  Does the operator on u-drive sticks look at the map or is he only looking at the airplane?​ See VXEP-324

​
Longer-term​
- Rewrite logic/controllers for high wind cases – probably a month or more in total to implement software/test, but could potentially increase wind envelope for vehicle​ - see VXEP-325

## Plan

If VTOL autopilot is available, test pitch rate gyro to determine if measurement errors are present that could have caused estimation issues seen in flight. Not expected for 2-3 months. 4/9 UPDATE 6/17: issue appears to be due to ublox GPS update rate.  Pitch rate gyro testing not required.
- @David Grosher @Eric Brewer this aircraft has arrived. What next steps do you recommend? Please summarize here.

## Root Cause

- Pitch estimation errors led to the vehicle coming into transition too fast
- Implementation of fixed-wing helper in combination with pitch estimation errors exacerbated landing overshoot.
- Operator nudge commands moved target TDP without providing feedback to the operator.
- Cause of pitch estimation errors unknown.  Current best guess is pitch rate gyro errors.

See report here.

## Comments (24)

### Eric Brewer, 2024-04-02

@Cameron Chapman done.  @Everett Werner @David Grosher FYI.

### David Grosher, 2024-04-02

@Eric Brewer This system is currently deployed. It is a priority because it has the new software.

### Eric Brewer, 2024-04-05

@Everett Werner @David Grosher @Pat Wells @Cameron Chapman I added some more notes along with conclusions and recommendations to the powerpoint.  There are a few recommended near term actions.  If we have the VTOL AP I’d recommend testing the y-gyro on a rate table to see if it was indeed faulty, otherwise I’d consider this investigation closed.

### Pat Wells, 2024-04-05

@Eric Brewer the aircraft is currently deployed overseas and is not expected to return for quite some time so testing VTOL AP is not possible at this time.  
My interpretation of your findings is that the customer should not continue to fly the aircraft due to a faulty gyro.  Is this correct as I will need to notify them ASAP if that’s the case?

### Eric Brewer, 2024-04-05

@Pat Wells That is the correct interpretation, I would not recommend flying this aircraft until the gyro is replaced.  Let me know we want to try to do any additional trouble-shooting.  We could recommend some ground tests to confirm suspicions on the gyro, but it may not be terribly useful if the end result is that we recommend replacement anyway.

### Pat Wells, 2024-04-05

@Eric Brewer I will work with the customer on the return of the aircraft. It may be an extended period so I recommend leaving the investigation open in Jira is a “waiting” status.

### Eric Brewer, 2024-04-05

@David Grosher I created 3 issue reports to track suggested changes to improve performance in the future.  Let me know if there is anything additional required to make sure they get a look in upcoming sprint planning.

### David Grosher, 2024-04-08

@Eric Brewer Should we also consider reducing the timeout from the current 30 seconds?

### Eric Brewer, 2024-04-08

@David Grosher added https://jenaero.atlassian.net/browse/VXEP-335.

### Eric Brewer, 2024-06-17

@Pat Wells see update above, given we’ve discovered the GPS update rate issue, the inspection of the gyro is not required.  I did confirm in this log that the GPS update rate was 4 or 5hz for most of the flight vs. 10 expected.

### Pat Wells, 2024-06-17

@Eric Brewer does the investigation team still require the aircraft or can we move on to replacing it for the customer?

### Eric Brewer, 2024-06-17

@Pat Wells Now that we do not believe the gyro is implicated I do not believe we need the bird.  FYI @David Grosher

### Pat Wells, 2024-06-17

@Sean Odell  FYSA see below on aircraft repair/replacment

### Pat Wells, 2024-06-18

@Eric Brewer @David Grosher just confirming that you do not require the aircraft for the investigation.

### Eric Brewer, 2024-06-18

@Pat Wells confirmed.  FYI @David Grosher

### Pat Wells, 2024-06-18

@Sean Odell  see below. Engineering team does not need aircraft. 
Please proceed with repairs.

### Sean Odell, 2024-10-10

@David Grosher Does your team need any of the hardware from this incident. We need the transit cases in Final Assembly to get prepped and cleaned for the replacement.  
@Cameron Chapman @Greg Fryer FYSA

### David Grosher, 2024-10-10

@Sean Odell No, we have completed the investigation.

### Eric Brewer, 2025-02-28

@David Grosher @Sean Odell updated powerpoint based upon what we learned over the past few months.  Adjusted to use latest template.

### David Grosher, 2025-02-28

@Pat Wells See the updated report.

### Sean Odell, 2024-10-10

@David Grosher Does your team need any of the hardware from this incident. We need the transit cases in Final Assembly to get prepped and cleaned for the replacement.  
@Cameron Chapman @Greg Fryer FYSA

### David Grosher, 2024-10-10

@Sean Odell No, we have completed the investigation.

### Eric Brewer, 2025-02-28

@David Grosher @Sean Odell updated powerpoint based upon what we learned over the past few months.  Adjusted to use latest template.

### David Grosher, 2025-02-28

@Pat Wells See the updated report.

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| IMG_4348.jpeg | image | 6419 | 2024-03-29 | listed only |
| IMG_4349.jpeg | image | 3815 | 2024-03-29 | listed only |
| IMG_4350.jpeg | image | 4006 | 2024-03-29 | listed only |
| IMG_4351.jpeg | image | 1891 | 2024-03-29 | listed only |
| IMG_4352.jpeg | image | 1567 | 2024-03-29 | listed only |
| T95_V459_240329_124002_01_pack.zip | archive | 3929 | 2024-03-29 | listed only |
| T95_V459_240329_124002_pack.zip | archive | 563 | 2024-03-29 | listed only |
