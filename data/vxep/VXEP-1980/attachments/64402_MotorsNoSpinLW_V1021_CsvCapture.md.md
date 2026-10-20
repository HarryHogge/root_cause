# MotorsNoSpinLW_V1021_CsvCapture.md

Attachment 64402, text, 7 KB, added 2026-09-02 by Scott Hunter.

# V1021 Motor Test CSV Capture

> **TL;DR:** XComm received and forwarded every logged motor-test request, while VTOL can silently ignore a same-motor request if that channel already has an active override. Rows 9 and 10 have no XComm CSV sample inside their five-second windows, so the logs cannot determine whether row 9 activated the motor; row 10 would be ignored if it did.

Sources:

- XComm event log: `AAR_V1021_B35_20260819T165708Z/xc_xcevlog.txt`
- XComm CSV: `AAR_V1021_B35_20260819T165708Z/xc_xcl00281.csv`

Each `RCS_MOTOR 2240X` command requests a five-second motor test. The event log and CSV use the XComm `CpuTime` clock, so their times can be compared directly. The event log contains 35 motor-test commands from CpuTime 405.828 through 566.906.

The CSV is not sampled at a uniform rate over this interval. It contains both 0.1-second sample intervals and gaps of approximately 10 seconds. A five-second test that falls wholly inside a gap has no CSV record during its active interval. Sixteen of the 35 event-log commands have zero CSV samples during their respective five-second test windows. The absence of `vtThr` or other CSV data for those rows is therefore a sampling limitation; it does not show whether the motor test was accepted, rejected, or executed.

`vtThr at next CSV sample` is the requested motor's throttle in the first CSV sample at or after the event-log command. That next sample can occur after the five-second test has ended; it must not be treated as an in-window measurement when `CSV samples in 5s` is zero. `First CSV sample offset (s)` is the elapsed XComm `CpuTime` from the event-log command to the first CSV sample during that command's five-second interval. A value of `0.000` means no CSV sample occurred during the interval.

Thirteen rows are bold because their two observations disagree: `vtThr = 0.170` with zero CSV samples during the test, or `vtThr = 0.000` with one CSV sample during the test. These rows are not explained by this comparison alone. Several commands are also less than five seconds apart. A CSV sample during overlapping five-second windows cannot be attributed to one command without additional evidence.

## Command-path findings

XComm does not apply a rejection gate to `RCS_MOTOR`. Its `RCS_MOTOR` handler decodes the motor, pulse width, and duration, then calls `CommandMotorTest` unconditionally ([`xcomm_202_40/XComm/ApmParser.cpp`](../../../GIT/InWork/UAP/xcomm_202_40/XComm/ApmParser.cpp#L1537-L1546)). Thus, the `RCS_MOTOR 22404` entries for rows 9 and 10 establish that XComm received and forwarded both requests.

VTOL handles the resulting `MAV_CMD_DO_MOTOR_TEST` command through `mavlink_motor_test_start` ([`autopilot_202_40/Protocols/mavlink/ap_mavlink.c`](../../../GIT/InWork/UAP/autopilot_202_40/Protocols/mavlink/ap_mavlink.c#L2889-L2925)). It denies a request when the multicopter is armed, safe, flying, the motor is outside 1 through 8, or the throttle type is not PWM. The event log records `RCS_SAFE 0` before row 9 and `RCS_SAFE 1` after row 11, so rows 9 through 11 occurred during the unsafe interval ([`AAR_V1021_B35_20260819T165708Z/xc_xcevlog.txt`](AAR_V1021_B35_20260819T165708Z/xc_xcevlog.txt#L931-L983)). The available logs do not show a VTOL denial for rows 9 or 10.

The actuator implementation has a separate same-channel behavior: `actOverrideStart` returns without changing an override that is already active ([`autopilot_202_40/Actuator.c`](../../../GIT/InWork/UAP/autopilot_202_40/Actuator.c#L188-L202)). Row 10 arrived 2.321 seconds after row 9, inside row 9's five-second requested duration. If row 9 reached and activated the VTOL override, row 10 would therefore be silently ignored rather than extending or restarting the test.

The CSV cannot establish whether row 9 activated that override. Row 9's window was CpuTime 443.631 through 448.631, and row 10's was 445.952 through 450.952. The surrounding XComm CSV samples were at 442.277 (`vtThr4 = 0.000`) and 452.277 (`vtThr4 = 0.170`), leaving no sample inside either window. The original table used the nearest CSV sample, which selected the preceding 442.277 sample for both rows and therefore showed `vtThr4 = 0.000`. The current table uses the next sample, which selects 452.277 and shows `vtThr4 = 0.170`; because that sample is outside both windows, it cannot be attributed to row 9 or row 10.

| # | UTC | CpuTime | Command | Motor | vtThr at next CSV sample | CSV samples in 5s | First CSV sample offset (s) |
|---|---|---:|---|---:|---:|---:|---:|
| 1 | 16:54:15.828 | 405.828 | RCS_MOTOR 22401 | 1 | 0.000 | 0 | 0.000 |
| 2 | 16:54:17.640 | 407.640 | RCS_MOTOR 22404 | 4 | 0.170 | 1 | 4.637 |
| **3** | **16:54:22.346** | **412.346** | **RCS_MOTOR 22404** | **4** | **0.170** | **0** | **0.000** |
| 4 | 16:54:27.542 | 417.542 | RCS_MOTOR 22403 | 3 | 0.170 | 1 | 4.735 |
| 5 | 16:54:30.596 | 420.596 | RCS_MOTOR 22404 | 4 | 0.170 | 1 | 1.681 |
| 6 | 16:54:37.703 | 427.703 | RCS_MOTOR 22402 | 2 | 0.170 | 1 | 4.574 |
| 7 | 16:54:43.197 | 433.197 | RCS_MOTOR 22404 | 4 | 0.000 | 0 | 0.000 |
| 8 | 16:54:45.985 | 435.985 | RCS_MOTOR 22404 | 4 | 0.000 | 0 | 0.000 |
| **9** | **16:54:53.631** | **443.631** | **RCS_MOTOR 22404** | **4** | **0.170** | **0** | **0.000** |
| **10** | **16:54:55.952** | **445.952** | **RCS_MOTOR 22404** | **4** | **0.170** | **0** | **0.000** |
| 11 | 16:54:59.619 | 449.619 | RCS_MOTOR 22404 | 4 | 0.170 | 1 | 2.658 |
| 12 | 16:55:22.939 | 472.940 | RCS_MOTOR 22401 | 1 | 0.000 | 0 | 0.000 |
| 13 | 16:55:25.714 | 475.714 | RCS_MOTOR 22404 | 4 | 0.000 | 0 | 0.000 |
| 14 | 16:55:27.114 | 477.114 | RCS_MOTOR 22404 | 4 | 0.000 | 0 | 0.000 |
| **15** | **16:55:27.351** | **477.351** | **RCS_MOTOR 22404** | **4** | **0.000** | **1** | **4.926** |
| **16** | **16:55:27.567** | **477.567** | **RCS_MOTOR 22404** | **4** | **0.000** | **1** | **4.710** |
| **17** | **16:55:27.773** | **477.773** | **RCS_MOTOR 22404** | **4** | **0.000** | **1** | **4.504** |
| **18** | **16:55:27.971** | **477.971** | **RCS_MOTOR 22404** | **4** | **0.000** | **1** | **4.306** |
| **19** | **16:55:28.159** | **478.159** | **RCS_MOTOR 22404** | **4** | **0.000** | **1** | **4.118** |
| **20** | **16:55:28.352** | **478.352** | **RCS_MOTOR 22404** | **4** | **0.000** | **1** | **3.925** |
| **21** | **16:55:29.675** | **479.675** | **RCS_MOTOR 22404** | **4** | **0.000** | **1** | **2.602** |
| **22** | **16:55:29.854** | **479.854** | **RCS_MOTOR 22404** | **4** | **0.000** | **1** | **2.423** |
| **23** | **16:55:30.034** | **480.034** | **RCS_MOTOR 22404** | **4** | **0.000** | **1** | **2.243** |
| **24** | **16:55:30.238** | **480.238** | **RCS_MOTOR 22404** | **4** | **0.000** | **1** | **2.039** |
| 25 | 16:55:32.401 | 482.401 | RCS_MOTOR 22402 | 2 | 0.000 | 0 | 0.000 |
| 26 | 16:55:34.422 | 484.422 | RCS_MOTOR 22402 | 2 | 0.000 | 0 | 0.000 |
| 27 | 16:55:37.575 | 487.575 | RCS_MOTOR 22403 | 3 | 0.170 | 1 | 4.702 |
| 28 | 16:55:41.617 | 491.617 | RCS_MOTOR 22404 | 4 | 0.170 | 1 | 0.660 |
| 29 | 16:55:52.824 | 502.824 | RCS_MOTOR 22404 | 4 | 0.000 | 0 | 0.000 |
| 30 | 16:55:54.220 | 504.220 | RCS_MOTOR 22404 | 4 | 0.000 | 0 | 0.000 |
| 31 | 16:56:47.788 | 557.788 | RCS_MOTOR 22401 | 1 | 0.170 | 1 | 4.490 |
| 32 | 16:56:51.953 | 561.953 | RCS_MOTOR 22404 | 4 | 0.170 | 1 | 0.325 |
| 33 | 16:56:54.492 | 564.492 | RCS_MOTOR 22404 | 4 | 0.000 | 0 | 0.000 |
| 34 | 16:56:56.641 | 566.641 | RCS_MOTOR 22404 | 4 | 0.000 | 0 | 0.000 |
| 35 | 16:56:56.906 | 566.906 | RCS_MOTOR 22404 | 4 | 0.000 | 0 | 0.000 |
