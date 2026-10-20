# VXEP-600-PreliminaryAnalysis.pptx

Attachment 24285, pptx, 510 KB, added 2024-10-30 by Jason Scherer.

## Slide 1

VXEP-600 AV600
Preliminary Analysis – Jason Scherer (10/30/2024)

## Slide 2

[picture]
Analysis Summary
Release Version: 6.1.2
Launch/Land Aborts? No
Air Speed Match Ground Speed? NA (No Flight)
Battery Voltage/Current levels within limits? Within Limits
Fuel Cell Used? No
Lowest CNO: 44.3
Ap Link Reset Count: 2
GCS Disconnects, Rebukes, Timeouts? No
Vehicle Resets, Type? No
Error/Unusual messages: Yes
Summary: No flight occurred due to errors in the launch wizard. Battery within limits, CNO above threshold, Several odd errors/messages in logs indicating GCS socket errors, packet timeouts, and IMU error checks failed.

Flight Time: (Flight Duration: NA, Launch-Time: NA, Land-Time NA)

## Slide 3

Flight Timeline
Not flight occurred due to launch wizard failure.

## Slide 4

Firmware & Config Versions
GCS:
Build: 6.1.2.0 (Release Date: ?? )
Fixed Wing AP: 6.05m
AP Build: 0605000D
Gains Match?
XComm: 4.67
build: 2023/02/06 11:24:40
code checksum: 55CF3E55
VTOL AP: 1.53
build: 2023/07/27 11:34:30
code checksum: EFEBD4B8

## Slide 5

Battery Voltages & Currents
Primary Battery (If not FC) – Within Limits
Voltage (vbatt): High (28.14), Low (27.4)
Current (ibatt): Max 5.75A
HLB
Voltage (vtvbatt): High (29.3) Low (27.7)
Current (vtibatt): Max 3.93A

## Slide 6

GPS Health
Lowest CNO (Threshold=40): 44.3

## Slide 7

Error/Unusual Messages
GCS Socket Errors
GCS SysCmd Failed
GCS Packet Timeouts
XComm IMU error check failed
More than average number of Air Data Calibration messages

## Slide 8

GCS Event Log (T95_V600_240828_121206_pack)
[picture]

## Slide 9

Debug Log (T95_V600_240828_121206_pack)
[picture]
[picture]
[picture]
[picture]
[picture]
[picture]
[picture]

## Slide 10

Debug Log (T95_V600_240828_135022_pack)
[picture]
[picture]
[picture]
[picture]
[picture]
[picture]

## Slide 11

XComm Log (T95_V600_240828_135022_pack)
[picture]
[picture]
[picture]
[picture]

## Slide 12

VTOL Log (T95_V600_240828_135022_pack)
[picture]
