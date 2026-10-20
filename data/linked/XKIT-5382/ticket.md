# XKIT-5382: B40 974 VTOL motors not spinning in LW

- **Issue type:** Problem
- **Status:** Assigned
- **Priority:** Medium
- **Created:** 2026-03-18
- **Updated:** 2026-10-08
- **Reporter:** Cameron Chapman
- **Assignee:** David Grosher
- **Creator:** Cameron Chapman
- **Parent:** XKIT-5113 B40 Non Flight-blocker flight test issue collector/Squawk List
- **Links:** Linked issue cannot finish until this issue finishes. VXEP-1980 (VXE 1021 Rear Left VTOL motor would not spin while on ground)
- **Epic Link:** XKIT-5113

## Description

the guys flying block 40 said they were conducting motor check and on the First motor check the front left prop was not spinning, they power cycled and after power cycle, front left spun, but back right didnt.
AAR_V974_20260318T200614Z VTOL Motor didnt fire 1.zip
 Teams chat Jackson Curvin: Dave the guys flying block 40 said they were conducting motor chec... | B40 Flight Test Chat | Microsoft Teams

## Plan

Requested HLB serial and cycle count. Aircraft has had 5 flights without issues up until this point. 
@Scott Hunter  can you summarize in the plan and status fields here what you have investigated and what you recommend next?

## Issue Status

From Chat Cameron Chapman: I think Ted Trowbridge and Dave Grosher can make that official de... | B40 Flight Test Chat | Microsoft Teams
“Does anyone have objections to flying this aircraft?
I think Ted Trowbridge and Dave Grosher can make that official decision since it seems to involve FW and OGCS most
Based on the info above, it sounds like it may not have registered multiple OGCS commands in a short timeframe, and spacing them out may prevent the issue, but I have not investigated logs in detail. They would know better if this has happened before, is feasible, and level of risk to flight”

## Comments (7)

### Jeremy Kostel, 2026-03-18

Limited CAN data available but no errors during this event
[12:05:24.001 60.001] VTCAN: R/TEC=0/0 WARN R/Tx=0/0 BP R/Tx=0/0 BO=0
[20:04:48.221 142.221] XCCAN: R/TEC=0/0 WARN R/Tx=0/0 BP R/Tx=0/0 BO=0
[20:05:48.703 202.704] XCCAN: R/TEC=0/0 WARN R/Tx=0/0 BP R/Tx=0/0 BO=0

### Jackson Riley Curvin, 2026-03-19

@David Grosher

### Jackson Riley Curvin, 2026-08-19

@David Grosher can you take a look at this we had another Aircraft do the same thing I uploaded the AAR

### David Grosher, 2026-08-19

@Scott Hunter @Jeremy Kostel Could one of you take a look at this?

### Scott Hunter, 2026-08-19

See comment on September 2, 2026 that supersedes this comment.
NOTES: I got a little time to look at data before heading out for the week. There’s Strong evidence motor commands were ignored in 1021 but not in 974. 1021 has way more test commands logged in the event log than we see in the CSV files. These tables break out motor test commands and how much current the bms is reporting. The sample rate in 1021’s XC is only 1 sample every 10 seconds. The tests are 5 seconds long so there’s a decent chance the tests will be missed in the data. The motor commands in the vtol look more reliable but iBatt doesn’t show anything. Are the logs correctly aligned?
Vehicle 1021 
| # | UTC | CpuTime | Command | Motor | vtThr | bmsCurr+1s | Response |
| 1 | 16:54:15.829 | 405.8 | RCS_MOTOR 22401 | 1 | 0.000 | 0.060 A | at baseline |
| 2 | 16:54:17.641 | 407.6 | RCS_MOTOR 22404 | 4 | 0.170 | 0.760 A | above baseline |
| 3 | 16:54:22.347 | 412.3 | RCS_MOTOR 22404 | 4 | 0.170 | 0.760 A | above baseline |
| 4 | 16:54:27.543 | 417.5 | RCS_MOTOR 22403 | 3 | 0.170 | 0.250 A | above baseline |
| 5 | 16:54:30.597 | 420.6 | RCS_MOTOR 22404 | 4 | 0.170 | 0.250 A | above baseline |
| 6 | 16:54:37.704 | 427.7 | RCS_MOTOR 22402 | 2 | 0.170 | 0.220 A | above baseline |
| 7 | 16:54:43.198 | 433.2 | RCS_MOTOR 22404 | 4 | 0.000 | 0.220 A | above baseline |
| 8 | 16:54:45.986 | 436.0 | RCS_MOTOR 22404 | 4 | 0.000 | 0.220 A | above baseline |
| 9 | 16:54:53.632 | 443.6 | RCS_MOTOR 22404 | 4 | 0.000 | 0.070 A | at baseline |
| 10 | 16:54:55.953 | 446.0 | RCS_MOTOR 22404 | 4 | 0.000 | 0.070 A | at baseline |
| 11 | 16:54:59.620 | 449.6 | RCS_MOTOR 22404 | 4 | 0.170 | 0.070 A | at baseline |
| 12 | 16:55:22.941 | 472.9 | RCS_MOTOR 22401 | 1 | 0.000 | 0.070 A | at baseline |
| 13 | 16:55:25.715 | 475.7 | RCS_MOTOR 22404 | 4 | 0.000 | 0.070 A | at baseline |
| 14 | 16:55:27.115 | 477.1 | RCS_MOTOR 22404 | 4 | 0.000 | 0.070 A | at baseline |
| 15 | 16:55:27.352 | 477.4 | RCS_MOTOR 22404 | 4 | 0.000 | 0.070 A | at baseline |
| 16 | 16:55:27.568 | 477.6 | RCS_MOTOR 22404 | 4 | 0.000 | 0.070 A | at baseline |
| 17 | 16:55:27.774 | 477.8 | RCS_MOTOR 22404 | 4 | 0.000 | 0.070 A | at baseline |
| 18 | 16:55:27.972 | 478.0 | RCS_MOTOR 22404 | 4 | 0.000 | 0.070 A | at baseline |
| 19 | 16:55:28.160 | 478.2 | RCS_MOTOR 22404 | 4 | 0.000 | 0.070 A | at baseline |
| 20 | 16:55:28.353 | 478.4 | RCS_MOTOR 22404 | 4 | 0.000 | 0.070 A | at baseline |
| 21 | 16:55:29.676 | 479.7 | RCS_MOTOR 22404 | 4 | 0.000 | 0.070 A | at baseline |
| 22 | 16:55:29.855 | 479.9 | RCS_MOTOR 22404 | 4 | 0.000 | 0.070 A | at baseline |
| 23 | 16:55:30.035 | 480.0 | RCS_MOTOR 22404 | 4 | 0.000 | 0.070 A | at baseline |
| 24 | 16:55:30.239 | 480.2 | RCS_MOTOR 22404 | 4 | 0.000 | 0.070 A | at baseline |
| 25 | 16:55:32.403 | 482.4 | RCS_MOTOR 22402 | 2 | 0.000 | 0.070 A | at baseline |
| 26 | 16:55:34.423 | 484.4 | RCS_MOTOR 22402 | 2 | 0.000 | 0.070 A | at baseline |
| 27 | 16:55:37.576 | 487.6 | RCS_MOTOR 22403 | 3 | 0.170 | 0.240 A | above baseline |
| 28 | 16:55:41.618 | 491.6 | RCS_MOTOR 22404 | 4 | 0.170 | 0.240 A | above baseline |
| 29 | 16:55:52.825 | 502.8 | RCS_MOTOR 22404 | 4 | 0.000 | 0.070 A | at baseline |
| 30 | 16:55:54.221 | 504.2 | RCS_MOTOR 22404 | 4 | 0.000 | 0.070 A | at baseline |
| 31 | 16:56:47.790 | 557.8 | RCS_MOTOR 22401 | 1 | 0.170 | 0.220 A | above baseline |
| 32 | 16:56:51.954 | 562.0 | RCS_MOTOR 22404 | 4 | 0.170 | 0.220 A | above baseline |
| 33 | 16:56:54.493 | 564.5 | RCS_MOTOR 22404 | 4 | 0.170 | 0.220 A | above baseline |
| 34 | 16:56:56.642 | 566.6 | RCS_MOTOR 22404 | 4 | 0.170 | 0.060 A | at baseline |
| 35 | 16:56:56.907 | 566.9 | RCS_MOTOR 22404 | 4 | 0.170 | 0.060 A | at baseline |

Vehicle 974
| # | UTC | Command | Motor | #active | bmsCurr+1s |
| 1 | 17:29:41.689 | RCS_MOTOR 22401 | 1 | 1 | 0.22 A |
| 2 | 17:29:43.395 | RCS_MOTOR 22404 | 4 | 2 | 0.45 A |
| 3 | 17:29:45.339 | RCS_MOTOR 22402 | 2 | 3 | 2.18 A |
| 4 | 17:29:47.051 | RCS_MOTOR 22403 | 3 | 3 | 1.35 A |
| 5 | 17:29:51.555 | RCS_MOTOR 22401 | 1 | 2 | 0.91 A |
| 6 | 17:29:52.921 | RCS_MOTOR 22404 | 4 | 2 | 0.96 A |
| 7 | 17:29:54.250 | RCS_MOTOR 22402 | 2 | 3 | 1.44 A |
| 8 | 17:29:55.653 | RCS_MOTOR 22403 | 3 | 4 | 0.66 A |
| 9 | 17:29:56.981 | RCS_MOTOR 22403 | 3 | 4 | 1.21 A |
| 10 | 17:29:58.359 | RCS_MOTOR 22402 | 2 | 3 | 1.63 A |
| 11 | 17:29:59.874 | RCS_MOTOR 22404 | 4 | 2 | 1.00 A |
| 12 | 17:30:01.051 | RCS_MOTOR 22401 | 1 | 2 | 0.97 A |
| 13 | 17:30:05.924 | RCS_MOTOR 22403 | 3 | 2 | 1.44 A |
| 14 | 17:30:07.711 | RCS_MOTOR 22402 | 2 | 2 | 1.09 A |
| 15 | 17:30:10.706 | RCS_MOTOR 22404 | 4 | 3 | 1.06 A |
| 16 | 17:30:12.262 | RCS_MOTOR 22401 | 1 | 3 | 2.57 A |
| 17 | 17:30:14.725 | RCS_MOTOR 22402 | 2 | 3 | 0.58 A |
| 18 | 17:30:17.382 | RCS_MOTOR 22403 | 3 | 3 | 0.42 A |
| 19 | 17:30:19.810 | RCS_MOTOR 22404 | 4 | 2 | 1.06 A |
| 20 | 17:30:21.985 | RCS_MOTOR 22401 | 1 | 3 | 0.55 A |
| 21 | 17:30:25.873 | RCS_MOTOR 22404 | 4 | 2 | 0.48 A |
| 22 | 17:30:27.980 | RCS_MOTOR 22401 | 1 | 2 | 0.40 A |
| 23 | 17:30:30.374 | RCS_MOTOR 22402 | 2 | 3 | 0.34 A |
| 24 | 17:30:33.358 | RCS_MOTOR 22403 | 3 | 2 | 1.15 A |
| 25 | 17:30:38.432 | RCS_MOTOR 22403 | 3 | 2 | 0.22 A |
| 26 | 17:30:40.020 | RCS_MOTOR 22402 | 2 | 2 | 0.43 A |
| 27 | 17:30:42.212 | RCS_MOTOR 22401 | 1 | 3 | 0.84 A |
| 28 | 17:30:43.679 | RCS_MOTOR 22404 | 4 | 3 | 1.06 A |
| 29 | 17:30:59.015 | RCS_MOTOR 22401 | 1 | 1 | 0.27 A |
| 30 | 17:31:00.904 | RCS_MOTOR 22404 | 4 | 2 | 0.42 A |
| 31 | 17:31:04.169 | RCS_MOTOR 22402 | 2 | 3 | 1.24 A |
| 32 | 17:31:05.793 | RCS_MOTOR 22403 | 3 | 3 | 1.08 A |
| 33 | 17:31:07.994 | RCS_MOTOR 22401 | 1 | 3 | 0.67 A |
| 34 | 17:31:08.905 | RCS_MOTOR 22404 | 4 | 4 | 1.61 A |
| 35 | 17:31:10.393 | RCS_MOTOR 22402 | 2 | 4 | 1.20 A |
| 36 | 17:31:11.170 | RCS_MOTOR 22403 | 3 | 4 | 0.91 A |
| 37 | 17:31:14.360 | RCS_MOTOR 22401 | 1 | 3 | 1.35 A |
| 38 | 17:31:15.412 | RCS_MOTOR 22404 | 4 | 4 | 0.36 A |
| 39 | 17:31:16.634 | RCS_MOTOR 22402 | 2 | 3 | 0.46 A |
| 40 | 17:31:17.472 | RCS_MOTOR 22403 | 3 | 4 | 0.69 A |
| 41 | 17:31:24.827 | RCS_MOTOR 22401 | 1 | 1 | 0.19 A |
| 42 | 17:31:25.720 | RCS_MOTOR 22404 | 4 | 2 | 0.36 A |
| 43 | 17:31:26.641 | RCS_MOTOR 22402 | 2 | 3 | 0.51 A |
| 44 | 17:31:27.925 | RCS_MOTOR 22403 | 3 | 4 | 0.81 A |
| 45 | 17:31:33.500 | RCS_MOTOR 22401 | 1 | 1 | 1.60 A |
| 46 | 17:31:34.360 | RCS_MOTOR 22404 | 4 | 2 | 1.60 A |
| 47 | 17:31:35.266 | RCS_MOTOR 22402 | 2 | 3 | 0.93 A |
| 48 | 17:31:35.964 | RCS_MOTOR 22403 | 3 | 4 | 0.69 A |
| 49 | 17:31:41.783 | RCS_MOTOR 22401 | 1 | 1 | 1.54 A |
| 50 | 17:31:42.515 | RCS_MOTOR 22404 | 4 | 2 | 3.42 A |
| 51 | 17:31:43.319 | RCS_MOTOR 22402 | 2 | 3 | 3.42 A |
| 52 | 17:31:44.317 | RCS_MOTOR 22403 | 3 | 4 | 2.26 A |
| 53 | 17:31:51.382 | RCS_MOTOR 22401 | 1 | 1 | 1.30 A |
| 54 | 17:31:51.902 | RCS_MOTOR 22404 | 4 | 2 | 0.45 A |
| 55 | 17:31:52.605 | RCS_MOTOR 22402 | 2 | 3 | 0.57 A |
| 56 | 17:31:53.526 | RCS_MOTOR 22403 | 3 | 4 | 0.69 A |
| 57 | 17:32:01.436 | RCS_MOTOR 22401 | 1 | 1 | 0.57 A |
| 58 | 17:32:02.141 | RCS_MOTOR 22404 | 4 | 2 | 0.57 A |
| 59 | 17:32:02.847 | RCS_MOTOR 22402 | 2 | 3 | 0.52 A |
| 60 | 17:32:03.824 | RCS_MOTOR 22403 | 3 | 4 | 0.70 A |
| 61 | 17:32:12.197 | RCS_MOTOR 22401 | 1 | 1 | 0.54 A |
| 62 | 17:32:13.101 | RCS_MOTOR 22404 | 4 | 2 | 0.55 A |
| 63 | 17:32:14.335 | RCS_MOTOR 22402 | 2 | 3 | 2.44 A |
| 64 | 17:32:15.182 | RCS_MOTOR 22403 | 3 | 4 | 1.00 A |
| 65 | 17:32:43.138 | RCS_MOTOR 22401 | 1 | 1 | 0.37 A |
| 66 | 17:32:44.462 | RCS_MOTOR 22404 | 4 | 2 | 0.39 A |
| 67 | 17:32:46.618 | RCS_MOTOR 22402 | 2 | 3 | 0.51 A |
| 68 | 17:32:47.523 | RCS_MOTOR 22403 | 3 | 4 | 1.38 A |
| 69 | 17:32:50.303 | RCS_MOTOR 22401 | 1 | 3 | 3.75 A |
| 70 | 17:32:51.315 | RCS_MOTOR 22404 | 4 | 4 | 0.69 A |
| 71 | 17:32:53.407 | RCS_MOTOR 22402 | 2 | 3 | 1.33 A |
| 72 | 17:32:55.228 | RCS_MOTOR 22403 | 3 | 4 | 0.36 A |
| 73 | 17:32:57.017 | RCS_MOTOR 22401 | 1 | 3 | 1.08 A |
| 74 | 17:32:58.834 | RCS_MOTOR 22404 | 4 | 3 | 1.32 A |
| 75 | 17:33:00.540 | RCS_MOTOR 22402 | 2 | 3 | 1.23 A |
| 76 | 17:33:02.158 | RCS_MOTOR 22403 | 3 | 3 | 1.48 A |
| 77 | 17:33:14.400 | RCS_MOTOR 22401 | 1 | 1 | 0.88 A |
| 78 | 17:33:15.242 | RCS_MOTOR 22404 | 4 | 2 | 0.88 A |
| 79 | 17:33:16.239 | RCS_MOTOR 22402 | 2 | 3 | 0.88 A |
| 80 | 17:33:17.310 | RCS_MOTOR 22403 | 3 | 4 | 2.30 A |
| 81 | 17:33:27.042 | RCS_MOTOR 22403 | 3 | 1 | 0.28 A |
| 82 | 17:33:27.808 | RCS_MOTOR 22402 | 2 | 2 | 0.42 A |
| 83 | 17:33:29.285 | RCS_MOTOR 22404 | 4 | 3 | 4.16 A |
| 84 | 17:33:30.104 | RCS_MOTOR 22401 | 1 | 4 | 0.82 A |





[embedded: image-20260819-232026.png]

VT sample rate is higher and the WHused seems to track the tests but iBatt is stuck at 0. Need to double check if the logs are correct for this version of VT code.  For 1021 in VTOL data the dWH/dt looks to line up with motor movement pretty well. I believe the motors moved for these tests that were commanded. But the table shows some commands did not result in any current draw.
[embedded: image-20260820-051052.png]

### Scott Hunter, 2026-08-26

@Jeremy Kostel and I looked at this data together yesterday, all I can say is there are commands to spin the motors recorded in the logs. Sometimes the commands result in current from the battery and sometimes they don’t. We’re using battery current as a proxy for motors spinning. A first pass through the event log looked like any time the throttle was commanded the motors drew current. But there wasn’t a throttle command for each motor test requested from the GCS. If we have access to the vehicle some interactive testing would be helpful.

### Scott Hunter, 2026-09-02

A closer analysis of the 1021 data shows there’s no smoking gun in the motor tests that weren’t responded to. It’s an artifact of the very slow sample rate in the collected data. 
[embedded: MotorsNoSpinLW_V1021_CsvCapture.md]

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V974_20260319T173634Z.zip | archive | 28820 | 2026-03-19 | listed only |
| AAR_V1021_B35_20260819T165708Z.zip | archive | 36876 | 2026-08-19 | listed only |
| image-20260819-232026.png | image | 450 | 2026-08-19 | listed only |
| image-20260820-051052.png | image | 515 | 2026-08-19 | listed only |
| [MotorsNoSpinLW_V1021_CsvCapture.md](attachments/64401_MotorsNoSpinLW_V1021_CsvCapture.md.md) | text | 7 | 2026-09-02 | converted |
