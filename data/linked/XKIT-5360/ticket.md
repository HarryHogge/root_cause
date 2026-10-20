# XKIT-5360: B40 913 Crash (2026/03/04)

- **Issue type:** Incident (8D)
- **Status:** D5 - Creating Action Tasks
- **Priority:** High
- **Created:** 2026-03-04
- **Updated:** 2026-05-21
- **Reporter:** Scott Whitney
- **Assignee:** Eric Brewer
- **Creator:** Scott Whitney
- **Links:** relates to XKIT-5348 (B40 913 aircraft does not have CAN breakout tail harness); relates to XKIT-5343 (V913 Power Event-smoke observed when powering up gimbal); relates to VXEP-1687 (VXE-533 Failed to transition to fixed wing flight); relates to VXEP-1654 (VXE-799 aileron servo locked); relates to VXEP-944 (VXE 614 Erratic behavior and propulsion failure led to crash )

## Description

Flight Data: 20260304-913 Incident
Investigation Sheet: B40 v913 Crash Investigation
Word Summary Servo shaft position error.docx
Investigation Sheet: B40 v913 Crash Investigation.xlsx
Jira Link: https://jenaero.atlassian.net/browse/XKIT-5360 
Operator Report:
FYI for all. A bit ago we had an incident with 913 first flight. After what appeared to be transition to fixed wing flight, aircraft banked right towards mission orbit, and maintained bank in spiraling descent. During descending spiral, selected U-drive and input left stick, after a few seconds and no response, selected land immediately. Lift rotors spun up just prior to impact with ground. 
Aircraft is likely total loss, 3P battery is damaged, HLB unknown damage. unable to find one lift motor in field. 
Flight data was uploaded to 20260304-913 Incident. Data already provided to Dave to disseminate to his team. 

Initial Findings:
- VTOL Checksums do not match -Confirmed that manually changing the configs to reduce wobble match 776D 
- Expected: 7233
- Actual: 776D
- VTOL Webpage open in flight
- XCOMM http server turned on (Webpage not open in flight)
- Ailerons stuck up
- “ESC commands are still live, throttle and forward current are matching. chatted with Jeremy and scott and doesn't seem like any of the other indicators of bad can health are present. Direction of servo commands logged is consistent with what we would expect to correct from a bank (judging from previous b40 logs)” - Everett
- [embedded: image-20260304-232518.png]
“Hardware in hand. Regardless of position commanded, R aileron servo drives to max position -45 degrees (all the way "up"): -Jeremy

## Corrective Action

https://jenaero.atlassian.net/browse/XKIT-5362 
https://jenaero.atlassian.net/browse/XKIT-5363 
@Eric Brewer  are there any controls changes that could have detected this issue and transititioned to VTOL earlier?

## Plan

- Containment of primary issue complete. @Matt Philley  do you have a link for that?
- @Eric Brewer  are there any controls changes that could have detected this issue and transititioned to VTOL earlier?

## Issue Status

With support from Pegasus, issue isolated to mechanical mounting of the magnet used to support position feedback coming loose. Issue has been isolated to CAN-based servos (vs. PWM), freeing up Block 30 production.
Any “investigated” servos should be treated with care, as hand strength can be sufficient to overcome the intended torque.

## Root Cause

Draft: Insufficient locking applied by manufacturer (Pegasus). Details to follow in formal report.
See:
https://jenaero.atlassian.net/browse/XKIT-5408 
https://jenaero.sharepoint.com/:f:/s/ContinuousImprovement/IgALyosNmAzaTob-ABsBgphKAT9WjmyQGBFMvgXPmyL3bMA?e=7zSyBP

## Comments (21)

### Jeremy Kostel, 2026-03-04

Issue: Right aileron servo exhibits abnormal mechanical feel and control behavior on isolated CAN test setup.
Initial hardware observations
- Right (R) aileron moves with significantly less resistance than Left (L) aileron.
- ODU connector appears visually undamaged.

Test setup / repro
- Connected to isolated CAN test setup.
- On the first command after power-up (any commanded position), R aileron immediately drives to -45° (software max) and then becomes largely unresponsive (“frozen”) at that position (can move ~3 degrees closer to 0).

Expected / control comparison
- L aileron operates normally under the same setup and commands.

Power-up behavior difference
- R aileron: does not report actual position prior to first command (reads fixed 90°).
- L aileron: reports accurate live position immediately on power-up and before first command.

Post-command behavior
- R aileron: drives directly to -45° after any command; feedback position correctly reflects -45°.
- R aileron: Target reached remains 0, indicating servo recognizes it is not achieving the commanded position.
- L aileron (working): Target reached goes 1 when commanded position is achieved (can momentarily show 0 with rapid +/- commands).

Internal limit behavior
- Both L and R aileron can trigger Internal_Limit_Active when commands exceed configured +/-45° limits (manual limits set).

Video
Videos attached showing the commanded max deflection angle behavior for both the left and right aileron.
The right aileron hyperextends and flips the servo horn over center, causing the horn and action arm to contact the wingtip structure. Once flipped, the servo becomes effectively “stuck” because commanding back toward center drives the horn further into the wing composite/structure, increasing interference rather than relieving it.

### Jeremy Kostel, 2026-03-04

CAN Servo Feedback: 
[embedded: image-20260305-022148.png]
CAN Servo Config Tool
[embedded: image-20260305-022210.png]

### Jeremy Kostel, 2026-03-04

Requesting help from @Sanjay Menon in the morning to help evaluate

### David Grosher, 2026-03-04

@Jeremy Kostel @Scott Hunter Can we verify that the firmware version on the servo is correct and that it isn’t corrupted? And what triggers a fault for the servo, if it knows it hasn’t achieved its target for some period of time I would think that a fault is triggered. But the screenshot above doesn’t seem to indicate anything. Does the fault reset after a power cycle? 
Unrelated to the investigation, if -45° deflection causes the linkage to hit the structure, then shouldn’t the configured limits be reduced to prevent hardware damage? Perhaps we are depending on AP firmware limits?

### Jeremy Kostel, 2026-03-04

- @David Grosher
- Im not familiar with checking the FW version on the servos but ill get @Ben Norris to assist with that in the morning
- we are NOT seeing a fault trigger in the servo. We need to get in touch with Pegasus to see what they have to say
- -45 deflection angle should not hit the structure. Ill let Sanjay give his evaluation tomorrow but if you watch the L Aileron video that is how max deflection is supposed to look (not touching wing structure)

### Scott Hunter, 2026-03-04

@David Grosher Point of clarity. The “Target_reached” flag is never “1” for the R Aileron unless we match the command to the current position. That flag is generally “1” for the L Aileron. As mentioned in Jeremy’s write-up we can get the L Aileron to flash a “0” by commanding large steps to the position. I’ve been told by Pegasus that the flag is an internal controller flag and momentary “0” values are expected when the servo is moving. The system should reach the commanded position and set that flag to “1”. 
I also want to point out we don’t know if the hyper extension is a cause or effect the crash. You can see in the R Aileron video, towards the end, that the shaft is bent. Something put excessive force into the shaft and that could cause internal damage that explains our test results. On the other hand, if the shaft were bent by the crash, we’d expect to see more damage on the control surface or that area of the wing.

### Scott Hunter, 2026-03-04

Here are plots comparing aileron commands from today’s flight vs a test flight in November. Prior to FW flight they look very similar, commanding trailing-edge up for both ailerons. (We don’t understand why the good L Aileron is commanded to about 25 degrees instead of the 20 degrees for both servos from November’s flight.)
The steady commands for both servos are the expected TEU commands during VTOL. 
During today’s FW flight period, both ailerons are attempting to roll left starting at ~740 seconds.  The R Aileron is commanded TED but the attached image-20260304-232518.png shows the R Aileron still TEU
(Note: The glitch in the Nov flight’s data at ~3568 is a known/fixed bug)

November flight baseline:
[embedded: image-20260305-053949.png]
Today’s flight.
[embedded: image-20260305-054047.png]

### Jeremy Kostel, 2026-03-05

Findings (this morning):
- The servo appears to have lost its zero (0°) reference.
- Video attached: starts at commanded -45°, then 0°, then +45°. Servo moves as expected between these commands and the Target_Reached flag = “1” at each position.
- Total motion is correct (sweeps ~90° end-to-end), however the servo’s interpreted 0° position is ~135° offset from the intended physical neutral.

Implication / likely failure mode in-flight:
- With the servo installed in the wing, this offset means the commanded positions would have driven the horn/action arm into the wing structure.
- The servo likely attempted to reach commanded positions relative to its incorrect 0° reference, but was mechanically blocked by the wing, resulting in the “can’t reach target” behavior observed previously.

Related to earlier observations:
- When the servo is not blocked by the wing and is allowed to travel freely from -45° to +45°, it:
- Tracks/report position correctly before any command, and
- Has holding force comparable to V913 Left Aileron and V974 Right Aileron.
- These address two issues originally observed during initial wingtip checkout (no pre-command position reporting and reduced holding force).

Open questions:
- Root cause for loss of zero reference is unknown at this time.
- Unclear whether the current 0° reference is a default/fallback or was reset during troubleshooting.

Additional context:
- Vehicle previously passed SCO and pre-flight checks, so the system was functioning as intended at least at one point prior to this issue.

[embedded: V913_RIGHT_AILERON_FULL_ROTATION.mp4]

### Scott Hunter, 2026-03-05

Cody pointed out you can see the servo is in the correct trim for 0 deflection in the first second of S3410003.mp4. Then it goes TEU as expected. The settings seem correct at this moment at the start of the launch sequence
R Aileron at 0
[embedded: image-20260305-165552.png]

R Aileron TEU
[embedded: image-20260305-165506.png]

### Ben Norris, 2026-03-05

I am attaching the pdf from pegasus I used during the development of the configuring of the servos as well as a summary of my findings pertaining to this error and the email chain with Pegasus discussing this problem.[embedded: Servo shaft position error.docx] [embedded: PA-R- Industrial Series CAN data protocol FW2_2_2 rev1_00.pdf]  Re: Another servo question

### Cameron Chapman, 2026-03-05

@Ben Norris thanks for documenting that. I saved them to the sharepoint to enable updates, comments, etc. Please attach to sharepoint in the future. 20260304-913 Incident

### Jeremy Kostel, 2026-03-05

[embedded: IMG_0164.mov]
[embedded: 2026-03-05_13.43.26#000.btrc][embedded: SN2504212_CANLOG_T1.asc]
SN 2504212 was flagged by Ben as problematic during initial checkouts.
For this test, the servo was isolated on the bench with only a PCAN (for logging) and my laptop running Ben’s configuration tool. The procedure was a simple continuous sweep, repeatedly commanding the servo between -45° and +45°.
The servo was initially “zeroed” at 90° on the protractor. In the attached video, the final movement shows the servo’s new interpreted 0° position, which has shifted approximately 55° from the original zero in 5 minutes.

### Jeremy Kostel, 2026-03-05

SN 2511274 passed Ben’s initial screening process. It underwent the same ~5-minute bench sweep test (commanding -45° to +45°) and showed no evidence of “walking”—the zero reference remained stable, with 0° consistently aligned at 90° on the protractor. [embedded: SN_2511274_GS_CANLOG_T1.asc]

### Jeremy Kostel, 2026-03-05

@Jeremy Kostel Tried to repeat the same testing on this servo but was unable to reproduce the failure mode.
One important note: the servo’s current zero reference has drifted far enough from “true” zero that we can no longer offset it back to 90° on the protractor using the user offset alone. The user-adjustable offset limit is ±20°, and the servo is now outside that range.

### Jeremy Kostel, 2026-03-05

@Jeremy Kostel Adjusting the manufacturer offset (as Pegasus recommended to Ben) to align “0” with true mechanical zero triggered another apparent “walking” event. The servo first showed small incremental ticks, followed by a sudden large shift—approximately 60°—with no warning.
We did not capture CAN logs during the first occurrence. We are repeating the test with CAN logging enabled and video recording to document the behavior.

### Jeremy Kostel, 2026-03-05

@Jeremy Kostel 
[embedded: IMG_0167.mov]
[embedded: SN_2504212_CANLOG_T2.asc]
Attached are the video and CAN log from the repeated test described in the previous comment. For this run, the manufacturer calibration/neutral offset was set to 9800, and the user neutral/home offset was set to -5010.

### Cameron Chapman, 2026-03-05

@Sam Miller

### Cody Smisek, 2026-03-12

Horizontal and Vertical stab in acceptable condition and retained for spares.
All other composites scrapped. 
Avionics enclosure removed and retained. ADP removed and retained. Silvus enclosure removed and retained and placed in ITAR cabinet.

### Matt Philley, 2026-03-26

Ticket created to document the RCCA with pegasus and link to associated 8D and SCAR
https://jenaero.atlassian.net/browse/XKIT-5408

### Matt Philley, 2026-04-06

RCCA Complete and marked complete @Jeremy Kostel FYSA

### Matt Philley, 2026-05-19

@Christa Meck was looking at production stoppage board and this ticket is still showing. The issue has been resolved and production resumed back in March/April, so this can fall off the production stoppage list.

## Attachments (18)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| V913_LEFT_AILERON_MAX_DEFLECTION.mp4 | video | 815 | 2026-03-04 | listed only |
| V913_RIGHT_AILERON_MAX_DEFLECTION.mp4 | video | 1102 | 2026-03-04 | listed only |
| image-20260304-232518.png | image | 187 | 2026-03-04 | listed only |
| image-20260305-022148.png | image | 13 | 2026-03-04 | listed only |
| image-20260305-022210.png | image | 47 | 2026-03-04 | listed only |
| image-20260305-053949.png | image | 372 | 2026-03-04 | listed only |
| image-20260305-054047.png | image | 345 | 2026-03-04 | listed only |
| 2026-03-05_13.43.26#000.btrc | other | 1160 | 2026-03-05 | listed only |
| IMG_0164.mov | video | 542922 | 2026-03-05 | listed only |
| IMG_0167.mov | video | 57994 | 2026-03-05 | listed only |
| [PA-R- Industrial Series CAN data protocol FW2_2_2 rev1_00.pdf](attachments/47012_PA-R-%20Industrial%20Series%20CAN%20data%20protocol%20FW2_2_2%20rev1_00.pdf.md) | pdf | 354 | 2026-03-05 | converted |
| SN2504212_CANLOG_T1.asc | other | 2425 | 2026-03-05 | listed only |
| SN_2504212_CANLOG_T2.asc | other | 192 | 2026-03-05 | listed only |
| SN_2511274_GS_CANLOG_T1.asc | other | 2553 | 2026-03-05 | listed only |
| [Servo shaft position error.docx](attachments/47011_Servo%20shaft%20position%20error.docx.md) | docx | 16 | 2026-03-05 | converted |
| V913_RIGHT_AILERON_FULL_ROTATION.mp4 | video | 2102 | 2026-03-05 | listed only |
| image-20260305-165506.png | image | 158 | 2026-03-05 | listed only |
| image-20260305-165552.png | image | 161 | 2026-03-05 | listed only |
