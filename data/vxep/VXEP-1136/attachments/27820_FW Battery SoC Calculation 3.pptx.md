# FW Battery SoC Calculation 3.pptx

Attachment 27820, pptx, 389 KB, added 2025-04-01 by Steve Gonzales.

## Slide 1

FW Battery SoC Calculation

## Slide 2

Fixed Wing: VBlife (State of Charge) Calculation
vbz = millivolts of empty battery
vbf = millivolts of full battery
vrange = vbf - vbz

life = ((vbatt - vbz) * 100L + (vrange/2) / vrange
life += BatteryTable[(life+2)/5]

## Slide 3

Set the Battery Model from GCS Message
[picture]
[picture]
[picture]
[picture]
[picture]

## Slide 4

BatteryOverride Structure
[picture]
This structure is used to store the battery stats provided by the GCS during the Launch Wizard.

## Slide 5

Fixed Wing updates energy @1Hz
[picture]
[picture]
Next Slide
[picture]

## Slide 6

CalcVBLife() – SoC Estimation
[picture]
[picture]
[picture]
[picture]
[picture]
[picture]
[picture]
[picture]
[picture]
[picture]
[picture]
[picture]

## Slide 7

CalcVBLife() – SoC Estimation cont.
[picture]
[picture]
[picture]
