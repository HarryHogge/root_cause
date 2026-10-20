# PrototypingResults.pptx

Attachment 20041, pptx, 1928 KB, added 2024-04-16 by Eric Brewer.

## Slide 1

(no text)

## Slide 2

Sim Results - Before
[picture]

## Slide 3

Sim Results – Before, 5 degree pitch estimation error
[picture]

## Slide 4

Issues with current design
Current fixed-wing helper is a function only of current airspeed	
When overshooting the TDP, the airspeed is high, causing fixed-wing helper to add throttle command making overshoot worse
Fixed-wing helper input is substantial
Up to 60% throttle which is more than cruise throttle at 35 knots (~50% based upon flight logs)
Causes trim angle of attack to be high, increasing risk of stall in hover

## Slide 5

Implementation
[picture]
Phase out of throttle command between 2 and 10 degrees pitch command.  Limit max throttle to 0.4
[picture]

## Slide 6

Sim Results - After
[picture]

## Slide 7

Sim Results – After, 5 degree pitch estimation error
[picture]

## Slide 8

Sim Results – Before, 50m step forward of vehicle
[picture]

## Slide 9

Sim Results – After, 50m step forward of vehicle
[picture]

## Slide 10

Sim Results – After, turbulence
[picture]

## Slide 11

Sim Results – Before, -5 degree pitch est error
[picture]

## Slide 12

Sim Results – After, -5 degree pitch est error
[picture]

## Slide 13

Sim Results – After, 10 degree pitch step
[picture]
