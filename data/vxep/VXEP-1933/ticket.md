# VXEP-1933: VXE 1038 VTOL motors failed to shut off after transition to fixed wing flight

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** Highest
- **Created:** 2026-06-24
- **Updated:** 2026-10-07
- **Reporter:** Zachary Mann
- **Assignee:** Jeremy Kostel
- **Creator:** Michael Mohr
- **Labels:** Hardware, LRR, RCCA, Weekly-incident-tracker
- **Links:** relates to XKIT-5529 (V1038 Troubleshooting Steps); relates to XKIT-5550 (SLO EE Troubleshooting Plan); Linked issue cannot finish until this issue finishes. RMA-1070 (VXE 1038 RMA 260728-2); relates to XKIT-5557 (B35/40 Lift Motor Wire Testing); relates to AV-1370 (SB35/40 Lift Motor Phase Lead Wear Investigation); relates to FS2-5032 (v882 (UAP) - CAN Launch abort investigation)
- **Customer:** Redwire
- **Vehicle Tail Number:** VXE-1038
- **Incident Type:** Near Miss
- **Severity:** 1 - Flight Critical
- **Executive Summary:** Aircraft needs SCO flights when back from EMI testing. Probable cause Hardware.

## Description

During launch and landing practice at the end of a training day, LRR aircraft 1038 (Block 35) transitioned to fixed‑wing flight while its VTOL motors remained running. The aircraft did not climb beyond approximately 200–250 ft.
The mission plan consisted of short launch/half‑orbit/landing cycles built in the OGCS Native App with 200‑ft transitions for both launch and landing.
On launch, the initial pause was unusually long. After the expected transition point, the instructor and operator were notified that the VTOL props were still active. They immediately issued a Land Immediately command, which the aircraft followed, landing off the runway with no visible damage.
Flight conditions:
Fort Carson, CO (38.64375730960418, -104.83618536253057), 77°F, elevation 6585 ft, winds 180° at 8 knots.
Additional AARs from the training event are available in the linked SharePoint folder.
Subsequent inspection in SLO revealed the following:
- The front-left boom showed evidence of thermal damage, and two ESC mounting screws were missing.
- During Launch Wizard testing, the front-left motor exhibited abnormal acoustic behavior and clicking.
- Manual rotation revealed mechanical irregularities consistent with issues previously reported by HSV.
- After removal, the motor showed catastrophic damage to one of the motor phase leads.
- The damaged lead had been contacting the carbon boom structure, and arcing marks were present.

This damage provides two plausible mechanisms for the CAN errors observed in flight:
- Phase-to-carbon conduction causing AC motor current to couple into the CAN shielding/carbon structure.
- ESC operation with one phase failed, causing degraded propulsion and abnormal ESC behavior (the ESC is a CAN node), while still allowing limited thrust.

The damaged phase lead is currently assessed as the most likely root cause.
Two potential initiating causes are under consideration:
- Wire damage during rework associated with the motor hot‑screw fix.
- A kink or routing issue that created localized mechanical/thermal stress, eventually burning through insulation and allowing conductor-to-carbon contact.

Investigation continues under linked ticket AV‑1370.
Location of other AARs from same training event https://jenaero.sharepoint.com/:f:/s/LRRSystemsEngineeringCollaboration/IgAjlr7a5xh-TKsOq5ZwotdJAf7Ha_pItEIYshHhG5QPsoE?e=bKhPQd

## Vehicle Configuration

BLOCK 35
4P Battery
E140Z G2 (with LASER)
VBN + AION
+2 Wing Shift Bracket, ~58 pounds TOW

## Corrective Action

Corrective actions will be implemented through AV‑1370
Aircraft 1038 will receive a boom rebuild per the latest production plan and complete a verification flight series prior to returning to field service.

## Plan

Root‑Cause Investigation & Containment (AV‑1370)
All ongoing technical investigation, containment, and rework is being managed under the linked Jira ticket AV‑1370. This includes evaluation of phase-lead routing, insulation protection, boom construction, and inspection processes.
Aircraft Disposition & Next Steps
1038 has been reassembled, ground‑tested, and shipped to EMI testing. It has not flown since rework.
Once returned to SLO:
- Verify booms are rebuilt per current production standard.
- Complete a standard validation flight series before returning the aircraft to field operations.

## Issue Status

Status as of July 9, 2026
The team executed the test plan from AV‑1370. The issue could not be replicated; CANbus behavior remained nominal across all test configurations. Recommendation was to return the asset to SLO for deeper inspection.
JST inspections are deferred until after investigation to avoid altering evidence or obscuring root cause.
Status as of July 28, 2026 (Post‑Arrival in SLO)
- Aircraft arrived with reported CAN errors and front-left propulsion anomalies.
- Thermal damage observed on the front-left boom; two ESC mounting screws missing.
- Motor exhibited abnormal acoustic behavior when commanded without a prop.
- Mechanical irregularities confirmed via hand rotation.
- Motor removal revealed catastrophic phase lead damage with evidence of arcing to carbon boom structure.
- Damage explains CAN errors via conductor-to-carbon coupling or abnormal ESC behavior with a failed motor phase.

Root Cause (Current Best Assessment)
Most likely: phase lead insulation failure allowing conductor-to-carbon contact.
Initiating cause remains under investigation; leading candidates are rework-induced wire damage or stress/thermal concentration from improper routing.

## Root Cause

Current evidence indicates the failure originated from damage to a front-left motor phase lead, which ultimately allowed the conductor to contact the carbon boom structure and produce arcing. This condition is the most likely cause of the observed CAN errors and propulsion anomalies.
The initiating cause of the phase lead damage remains under investigation. Two primary scenarios are under consideration:
- Rework-induced damage during the motor hot-screw corrective process.
- Routing/bend‑radius stress causing localized mechanical or thermal concentration, eventually degrading insulation and leading to conductor exposure.

Root cause validation and detailed mechanism analysis are being tracked under AV‑1370.

## Comments (14)

### Cody Smisek, 2026-06-24

@Michael Mohr Please add location / temperature / elevation / wind if you have it.

### Anthony Hansen, 2026-06-24

@Cody Smisek Fort Carson, CO (take off spot 38.64375730960418, -104.83618536253057), 77 degrees F, 6585 feet elevation, 180 08 knots

### David Grosher, 2026-06-24

@Cody Smisek @Scott Hunter @Michael Mohr @Jeremy Kostel The CAN bus health appears to be degraded, I would imagine that some subset of commands sent to the VTOL AP or acknowledgements back were missed. 
[23:12:02.390 804.390] VTOL State Change (was is):  LCH_FLY WAITSAFE
[23:12:02.470 804.470] ap dbg: lch timeout: 2
[23:12:02.471 804.472] MESSAGE_VTOL 0  4
[23:12:02.473 804.473] MESSAGE_VTOL 0  4
[23:12:02.475 804.475] ap dbg: vt ack safe or timeout, lch complete
[23:12:02.476 804.476] MESSAGE_VTOL2:  16  0
[23:12:02.477 804.477] VTOL State Change (was is):  WAITSAFE LCH_IDLE
[23:12:03.367 805.367] Air Qual, Mag Qual, Att Qual: 100  100  40
[23:12:05.513 807.513] XCCAN: R/TEC=135/251 WARN R/Tx=1/1 BP R/Tx=1/1 BO=1

Having said that, despite the CAN bus issues the VTOL still seems to transition to FW Flight
[15:12:07.954 639.954] host vtol state was, is: APVTOL_ASSIST APVTOL_FWFLIGHT

Strangely, there is no printout in the VTOL log that says it is braking.  Which seems to indicate that the safe message was not received. I don’t really understand why if we know we are in FW Flight that we wouldn’t check that the motors have been safed, this could easily be done on transition into this mode. At this point we know that the lift system should have been disarmed as that is the VTOL state progression within the FW AP’s VTOL state machine.  Regardless, we should verify this given the MESSAGE_VTOL and MESSAGE_VTOL2 message seen above. 

For context:
[embedded image-20260625-024656.png]

### Michael Mohr, 2026-06-25

@David Grosher @Cody Smisek @Scott Hunter @Jeremy Kostel Additionally, this aircraft flew with the main battery that was in 1006 mishap (S/N M4-0015). We charged it, tested the cells balance, checked that the battery held voltage before using it again. It had flown two flights totaling approximately three hours before the VTOL anomaly.

### Jeremy Kostel, 2026-06-25

@Michael Mohr do we have any logs from post 1006 incident with this battery other than this one?

### Cody Smisek, 2026-06-25

@Jeremy Kostel They have been posting all AARs in the folder I linked in the flight test chat.

### Michael Mohr, 2026-06-25

@Jeremy Kostel I just attached AAR_V1038_B35_20260624T214645Z. A previous flight with battery 0015.

### Jeremy Kostel, 2026-06-25

FYI @David Grosher @Scott Hunter we have 9 V1038 flights from Ft. Carson efforts. CANbus looks completely healthy on the previous 8 flights

### David Grosher, 2026-06-25

@Jeremy Kostel Were these all different batteries from the incident?

### Jeremy Kostel, 2026-06-25

@David Grosher 
[embedded image-20260625-151556.png]
Heres a summary from a CAN health evaluation tool I have. The pass/fail metric is looking for any bus trouble (fail means any line with a non zero health message)
battery SN’s shown there as well. Looks like we have the flight right before this one with the same MB and have flown with that same HLB before as well with no issues

### David Grosher, 2026-06-25

@Jeremy Kostel Did we observe any CAN bus issues while on the ground before takeoff, could we get that same combination of batteries on the vehicle and retest the CAN bus health? Is that worthwhile without a load? 

Alternatively, I noticed that the Airdata and Magnetometer data was fine, could there be a bad connection on a specific node?

### Eric Brewer, 2026-06-25

@David Grosher Looks like there were some errors on the ground before takeoff. 
[embedded image-20260625-153017.png]

### David Grosher, 2026-07-15

@Eric Brewer @Jeremy Kostel Have we made any additional progress on this investigation? Were we able to isolate the issue to the battery or the bird? The program team needs to get at least some of their grounded aircraft back in the air.

### Eric Brewer, 2026-07-16

@David Grosher I haven’t looked into it recently.  It seems like some ground testing with the hardware makes sense to see if we can reproduce the issue and trace it to a specific battery etc.  Let me know if I can help with anything.  @Jeremy Kostel

## Attachments (13)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 1038 Video.MP4 | video | 20897 | 2026-06-24 | listed only |
| AAR_V1038_B35_20260624T231459Z.zip | archive | 96735 | 2026-06-24 | listed only |
| Landed 1.jpg | image | 3098 | 2026-06-24 | listed only |
| Landed 2.jpg | image | 2480 | 2026-06-24 | listed only |
| frontend-native-0052-2026-06-24.bin | other | 25330 | 2026-06-24 | listed only |
| image-20260625-024656.png | image | 165 | 2026-06-24 | listed only |
| AAR_V1038_B35_20260624T214645Z.zip | archive | 94582 | 2026-06-25 | listed only |
| image-20260625-151556.png | image | 173 | 2026-06-25 | listed only |
| image-20260625-153017.png | image | 38 | 2026-06-25 | listed only |
| Image (10).jpg | image | 653 | 2026-07-28 | listed only |
| Image (11).jpg | image | 418 | 2026-07-28 | listed only |
| Image (12).jpg | image | 475 | 2026-07-28 | listed only |
| Image (13).jpg | image | 801 | 2026-07-28 | listed only |
