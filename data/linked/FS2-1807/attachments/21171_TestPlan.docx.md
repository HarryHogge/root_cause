# TestPlan.docx

Attachment 21171, docx, 16 KB, added 2024-06-24 by Eric Brewer.

This document defines the test procedure for the following changes to be merged into release 1.55:
1. Fixed-wing helper modification to reduce overshoot
2. GPS acceleration fix
3. Baro Offset
4. Fixed-wing aiding to vtol in case of xmag fail

1. Fixed-wing helper modification to reduce overshoot
The software modification consists of two main changes:
1. Fwhelper_phaseout function which limits the authority of the fixed-wing helper power according to the current pitch angle command
2. Reduction of max throttle fixed-wing helper is allowed to contribute

Test A 
Goal: Ensure that phaseout function returns the expected values in all scenarios:
Venue: This test will be performed in a test harness since it would be difficult to perform on the hardware.

Test: Input various values of pitch_cmd and fwh_power_in and ensure that below pitch_cmd of fwmcthetaoff the power return is 0, above the fwmcthetaon the input is returned unchanged, and in between there is linear interpolation between the input and 0.  This also validates that the function can only return values between the input power and 0, so at very worst it will just turn off the fixed-wing prop.

Test B 
Goal: Verify performance of vehicle with changes in place.  
Venue: This will only be performed in the Simulink test environment
Test: Perform A/B comparisons in various transition cases to ensure that the new FWH improves and does not degrade performance in any case

Test C
Goal: Verify that software limits FWH contribution as a function of pitch angle as expected on hardware
Venue: HIL
Test: 
Perform A/B comparisons of approach cases where fixed-wing helper is engaged to full and causes overshoot of the TDP.  Verify that with new software the fixed-wing output is turned off when pitch angle is high.  Set debug prints in code to ensure that code is being called and calculations are running as expected.

Test D
Goal: Verify that the software successfully limits the FWH total output to 0.4 instead of 0.6.
Venue: HIL
Test: Create a test scenario where fixed-wing helper comes on maximum during approach
Run A/B comparison to ensure that new software limits maximum output to 0.4.

Test E
Goal: Verify performance of FWH and modifications in flight
Venue: Flight
Test: Run approach with significant headwind and verify FWH performs as expected.  NOTE: this may be difficult if wind conditions are calm in SLO.

2. GPS acceleration fix
This software modification consists of two changes:
1. Reduce GPS update rate to 5hz
2. Ensure that correct dt is calculated from the GPS messages

Test A
Goal: Verify that dT is calculated correctly, and that GPS-based acceleration is calculated correction
Venue: HIL with GPS
Test: Allow vehicle to obtain a GPS fix, ensure that PosRate and VelRate in VTOL logs are 5hz as expected.  Move the vehicle around, verify that GPS acceleration is calculated as expected.

Test B
Goal: Ensure that nothing unexpected happens when the GPS has a full view of the sky and runs for a long time
Venue: HIL with GPS
Test: Turn on debug outputs to see if acceleration calculation is skipped and what dt value is calculated.  Allow vehicle to obtain a GPS fix with an open view of the sky.  Let the autopilot run for 8 hours or more.

3. Baro Offset
This is a 2-line change to ensure that the baro agl offset is only calculated when in VTOL flight (i.e. not in fixed-wing when the vehicle is up and away).

Test A:
Goal: Verify fix works in happy path case
Venue: HIL
Test: Create a test case that triggers incorrect baro zero due to measurement in HIL flight.  Create A/B comparison with software fix and make sure it fixes the issue.
Test B
Goal: Verify no unintended consequences
Venue: Ground test?
Test: TODO?

4. Fixed-wing Heading Updates

The goal of the fixed-wing heading updates is to allow the fixed-wing autopilot heading estimate to aid vtol in the case the external magnetometer has failed.  The following tests will be performed:

Test A:
Goal: Baseline case – fail mag and make sure that heading updates happen.  Make sure vtol nav filter functions as expected.
Venue: HIL
Test: fail mag in HIL with sensors on internal mode, ensure that nav filter functions as expected.

Test B:
Goal: ensure updates work on hardware with real sensors
Venue: Full up bird (or iron bird if we have one with fixed-wing and vtol ap populated)
Test: Perform two tests – one with old software and one with new.  Fail mag by disconnecting or using a magnet.  With old software verify that the yaw gyro bias estimate is frozen.  With new software ensure that fixed-wing heading is used.  Move vehicle to multiple headings and ensure it tracks fixed-wing heading as expected.
