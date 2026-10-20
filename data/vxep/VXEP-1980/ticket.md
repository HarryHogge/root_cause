# VXEP-1980: VXE 1021 Rear Left VTOL motor would not spin while on ground

- **Issue type:** Incident (8D)
- **Status:** D4 - Release RCR
- **Priority:** High
- **Created:** 2026-08-19
- **Updated:** 2026-10-14
- **Reporter:** Stephan Johnson
- **Assignee:** Jeremy Kostel
- **Creator:** Stephan Johnson
- **Labels:** Hardware, LRR, RCCA, Weekly-incident-tracker
- **Links:** Cannot finish until linked issue is finished. XKIT-5382 (B40 974 VTOL motors not spinning in LW)
- **Customer:** LRR
- **Vehicle Tail Number:** VXE 1021
- **Vehicle Configuration:** Block 35
- **Problem Type:** Discovered Issue
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround
- **Executive Summary:** VXE 1021 Rear Left VTOL motor would not spin while on ground; Probable cause Operator Error

## Description

During Launch Wizard VTOL motor spin tests on VXE 1021, the Rear Left VTOL motor did not respond to commanded spins. The aircraft had just landed from a previous flight where all VTOL motors functioned normally during landing. Three of the four VTOL motors spun correctly in LW; only the Rear Left failed to respond.
This issue resembles another observed case on aircraft V974 during Sweden training. That ticket is linked for reference. Commands reached XCOM but were not acted on by the ESC, despite CAN health appearing nominal.
For 1021, ESC logs pulled from the boom do not show any missed commands. All logged input duty cycles correlate with motor duty output, current spikes, and RPM responses. This includes logs spanning multiple flights and LW test pulses. No instances were found where the ESC received a command and failed to spin the motor.
However, XC event logs show significantly more motor test commands than appear in the ESC CSV logs. Due to the XC sample rate (1 sample per 10 seconds), 5-second motor tests may not appear in the CSV files. Motor commands in VTOL logs appear more reliable, but iBatt data does not show corresponding current draw during some tests, likely due to log alignment issues.
A summary of RCS_MOTOR commands from XC indicates multiple test attempts on motor 4 (Rear Left) with expected “baseline” current values that do not reflect motor spin. This suggests motor commands may have been ignored at the aircraft level for 1021, despite the ESC not logging any missed commands.

## Plan

- ESC is still in the boom. Issue seen on a different aircraft in Sweden training. Can link.
- Aircraft in HSV.
- Reassemble aircraft. Run LW. See if issue repeats.
- If issue does not repeat, pull CAN logs from ESC to see if they received CAN commands when it didn’t spin. Per HSV, customer tried LW, didn’t work, sent back, so the failed LW should be the last log recorded. 
- https://jenaero.atlassian.net/wiki/x/FYCCCg
- @Jeremy Kostel Can we review CAN logs vs AAR to verify that the commands sent during LW match the commands received and logged on the ESC. Not clear if that was done below. 
- Last status of 974 investigation Scott H says no smoking gun.

## Issue Status

Hardware is currently assessed as healthy. All commands that reached the ESC were acted on correctly, and ESC logs show no instances of missed or ignored motor commands. CAN health appears nominal from both the ESC and autopilot perspectives. The failure path appears to be between XCOM and the ESCs: motor spin commands were observed at XCOM but never reached the ESCs for unknown reasons. Root cause is not yet identified. SW/FW investigation required to determine why commands did not propagate beyond XCOM.

## Comments (9)

### Christa Meck, 2026-08-24

Linked Problem is being actively worked.

### David Grosher, 2026-08-26

@Scott Hunter @Scott Whitney @Jeremy Kostel Has this issue been resolved? I’m not sure if updates are being provided here. The support team was asking about this.

### Zachary Mann, 2026-08-28

@Scott Hunter @Scott Whitney @Jeremy Kostel @Alexander Alan Arnold Ran the VTOL Motors while on ground, all 4 spun as expected. ESC P/N: 212344203 S/N: ES107597. Attempting to connect to ESC and download logs.

### Zachary Mann, 2026-08-28

@Scott Hunter @Scott Whitney @Jeremy Kostel @Alexander Alan Arnold logs downloaded. Adding to ticket

### Jeremy Kostel, 2026-09-01

FYSA @David Grosher, In the linked V974 ticket @Scott Hunter did some analysis about commands not really being sent to the ESC. They arrive at XCOM but no action detected after that. CAN health is clear from both the aircraft and ESC’s perspective. I cant see any signs of trouble in these ESC logs. They go back pretty far and capture what appears to be some flights and plenty of LW spins. There are no times logged on the ESC where it received a command and didn’t spin the motor. Input duty (orange) is command logged by the ESC (from aircraft) and motor duty is corresponding command sent to the motor from the ESC. They all seem to correlate to both current spike and RPM spike. 
[embedded: image-20260901-184412.png]
This second screenshot includes the last few flights recorded, and the pulse on the very far right I am assuming to be when HSV tried to recreate the issue there. There are 0 instances when the motor/ESC didnt respond to a given command according to ESC logs
[embedded: image-20260901-185442.png]

### Scott Whitney, 2026-09-01

@Jessica Henson - the AAR on this Jira issue comes from a CUI software build and may have CUI data on it.

### Scott Hunter, 2026-09-02

I’ve attached a write-up here and to the linked issue explaining why the data log appears to show the system not responding to motor-test commands.[embedded: MotorsNoSpinLW_V1021_CsvCapture.md]

### David Grosher, 2026-09-02

@Pat Wells @Drew Hildreth Could you remind your guys that v6.8.0 for Blk35 is CUI. Data should be put in Sphinx and the location pasted in Jira in text. In a future release we will add a label to the AAR package.

### Drew Hildreth, 2026-09-03

@David Grosher Will do, Dave.

## Attachments (5)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V1021_B35_20260819T165708Z.zip | archive | 36876 | 2026-08-19 | listed only |
| [2026-08-28_13-25-VH_CID-4-log.csv](attachments/64333_2026-08-28_13-25-VH_CID-4-log.csv.md) | csv | 51422 | 2026-08-28 | converted |
| image-20260901-184412.png | image | 111 | 2026-09-01 | listed only |
| image-20260901-185442.png | image | 98 | 2026-09-01 | listed only |
| [MotorsNoSpinLW_V1021_CsvCapture.md](attachments/64402_MotorsNoSpinLW_V1021_CsvCapture.md.md) | text | 7 | 2026-09-02 | converted |
