# Candidate1_55_TestResults.pptx

Attachment 21172, pptx, 4974 KB, added 2024-06-24 by Eric Brewer.

## Slide 1

Candidate 1.55 Test Results

## Slide 2

Fixed-wing helper updates

## Slide 3

Test Results – Test A
Software Under Test: Created test harness FWHelperTest.c attached
Create various test inputs and ensure output is as expected
[picture]
[picture]
Nominal operation, power input 100, command varies from -10 to 10
Edge case: fwmcthetaon = fwmcthetaoff
[picture]
This would create toggling behavior above/below threshold.  Fix if parameters are configurable, otherwise this case would never be hit. 
Fwmcthetaoff < fwmcthetaon could create similar issues
Result: Test passes, but handle case of min = max more gracefully if other code changes are needed

## Slide 4

Test Results – Test B
Software Under Test: Simulink models.  Repo control_analysis, branch remotes/origin/dev_ebrewer_fwhelper
Created model of fixed-wing helper in Simulink and ran various A/B comparisons to show improvement with new FWH

## Slide 5

Test B - Sim Results - Before
[picture]

## Slide 6

Test B - Sim Results – Before, 5 degree pitch estimation error
[picture]

## Slide 7

Issues with current design
Current fixed-wing helper is a function only of current airspeed	
When overshooting the TDP, the airspeed is high, causing fixed-wing helper to add throttle command making overshoot worse
Fixed-wing helper input is substantial
Up to 60% throttle which is more than cruise throttle at 35 knots (~50% based upon flight logs)
Causes trim angle of attack to be high, increasing risk of stall in hover

## Slide 8

Implementation
[picture]
Phase out of throttle command between 2 and 10 degrees pitch command.  Limit max throttle to 0.4
[picture]

## Slide 9

Test B - Sim Results - After
[picture]

## Slide 10

Test B - Sim Results – After, 5 degree pitch estimation error
[picture]

## Slide 11

Test B - Sim Results – Before, 50m step forward of vehicle
[picture]

## Slide 12

Test B - Sim Results – After, 50m step forward of vehicle
[picture]

## Slide 13

Test B - Sim Results – After, turbulence
[picture]

## Slide 14

Test B - Sim Results – Before, -5 degree pitch est error
[picture]

## Slide 15

Test B - Sim Results – After, -5 degree pitch est error
[picture]

## Slide 16

Test B - Sim Results – After, 10 degree pitch step
[picture]

## Slide 17

Test Results – Test C
Software Under Test: Before case: Release 1.54.02After case: autopilot_202, remotes/origin/dev_ebrewer_landingimprovements2
Created approach scenario with 20fps wind where fixed-wing helper would be enabled
Before case shown to the right – fixed-wing helper enabled with headwind.  Vehicle attitude is oscillatory due to simulation issues, overshoot seen in flight is not reproduced.
Fixed-wing helper throttle around 0.4 is expected.  Calculation is given by:        hwc = Limitf(hwc, 0.0f, fwmcmaxhwc);
        power = fwmchwcthr * (hwc - fwmcminhwc);    // kp * excess headwind
At 35fps IAS power = 0.015*(35-10) = 0.375Then add expo with exponent of 0.6:    float ratio = fabsf(in / fullscale);        // 10.0/20.0 = 0.5, should always be 0 .. 1    ratio = powf(ratio, expo);                  // always 0 .. 1    return fullscale*ratio*Signf(in);
In this case, ratio = 0.375/0.6, total output is 0.6*(0.375/0.6)^0.6 = 0.45
Output is as expected given code implementation at this airspeed
[picture]
[picture]

## Slide 18

Test Results – Test C
After case shown to the right
Pitch angle is mostly above 2 degrees in phaseout region of new FWH logic
Forward throttle comes on briefly during pitch transients
We can see pitch angle is low when fixed-wing helper engages
Overall tracking performance is poor due to sim issues in this flight condition
[picture]

## Slide 19

GPS Acceleration Fix

## Slide 20

Test Results – Test A
Software under test:autopilot_202, hash 96b8b0ce2ea0db667dc8c46ce6c4c0cd4f8bf160
Moving data captured outside with updated software
Note: could not reproduce 5hz update rate with ublox (only occurs with open view of sky and too many SVs)
[picture]

## Slide 21

Test Results
Offline calculation run and compared against online
Not expected to be exact match because of logging rates
Special thanks to Brandon for hitting 10 ft/s with a cart!
[picture]
MATLAB offline calc
[picture]

## Slide 22

Test Results
Examining event log, dt calculation skipped twice due to dt of zero
Future work to identify why this happens (this appears to be existing behavior where it is called multiple times)



Dt calculation consistently shows 0.2 or 0.4
[picture]
[picture]

## Slide 23

Baro Offset

## Slide 24

Baseline Case
HIL results with latest candidate release.  Added debug line to ensure code is hit in HIL environment
LRF status bits shown below
[picture]
[picture]
[picture]

## Slide 25

Log Review of existing cases observed in the field
All issues occurred during APVTOL_FWFLIGHT
[picture]
Issue observed in v376
[picture]
Issue observed in v371
[picture]
Baseline Case
Issue observed in v426
[picture]

## Slide 26

Before  Fix – agl estimate corrupted when up and away
HILSim Tests
[picture]
After Fix – AGL estimate remains good
[picture]
Software under test: Candidate1.55, hash 38469417e4ba9b11cf4060b8ca73e7625dc42d67
To test, added corruption of AGL measurement here:
[picture]
Future todo: understand mechanism for corruption.  If the software were just reading agl it seems like eventually agl should converge to 5ft, but it doesn’t.  Only one bad update gets through.

## Slide 27

Heading Update Fix

## Slide 28

Mag failure injection code pulled in from scott’s branch, checked into branch here: <todo commit hash>
Be sure to set HIL mode internal for sensors to run this test!
External Mag Fail Test
[picture]
Vtol webpage/config/HIL
[picture]
Yaw rate bias 0
[picture]
Some heading errors (small since gyros are perfect and bias estimate is 0)
Before Fix
[picture]
Yaw rate bias  moves confirming fixed-wing heading is used.
Attitude and heading track well
[picture]
Some toggling due to data age > 200ms.  Note this only prints out every 10 cycles.  Will update value to 300ms to allow most updates through.  Should also test this on the bird to measure if latency increases when other cpu tasks are working hard.
After Fix
Autopilot 202 Commit hash: da17b69a857a6022174df9ea10663615682c350d
Pitch/Roll tracking poor in VTOL HIL internal mode

## Slide 29

Reviewed some additional data to ensure that FWAP heading is good during vTOL operations.
External Mag Fail Test
[picture]
T95_V604_240130_144610_pack – heading errors below 15 degrees for entire flight

## Slide 30

Baro Offset Backup

## Slide 31

Test results from above were not exactly as expected – for example why does it appear only one update from the laser agl occurs? One would expect that if the software lets one update in, it should allow continuous updates, in which case AGL should converge to laser agl measurement.  This is not the case.  The below analysis tries to determine why, but the conclusion remains future work.
Code Review

## Slide 32

LRF_BITS_RFMM does not currently prevent the agl update, it is only looked at before landing detection runs (see sensorAglTestBits)
a
Code Review
[picture]
[picture]
3 sets of gains, selected based upon flight state
[picture]
[picture]

## Slide 33

Potential bug, lrfbits only set to 0 when logging happens.  There is a commented out piece of code at the top of the agl fusion task that would do so.
Code Review
[picture]
[picture]
[picture]
Allows lrfgood and nogood to simultaneously be set here

## Slide 34

This function is never called, but would turn off the laser if fsIsSafe() && fsIsFlying()
Code Review
[picture]

## Slide 35

Ran with test code to set lrf agl to 5 when AGL is >500
Recreated case where baro offset is incorrectly calculated
Code Review
[picture]
[picture]
Hits this code in SensorAgl.c once and only once
Test Code (LidarLiteV1.c)
[picture]

## Slide 36

Still not positive mechanism for agl estimate to be corrupt.
Code Review
[picture]
