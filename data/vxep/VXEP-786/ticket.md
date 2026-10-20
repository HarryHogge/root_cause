# VXEP-786: VXE 732 Altitude Excursions

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2024-11-22
- **Updated:** 2026-03-02
- **Resolved:** 2024-12-10
- **Reporter:** Pat Wells
- **Assignee:** Craig Burton
- **Creator:** Pat Wells
- **Labels:** TIQUILA, Weekly-incident-tracker
- **Links:** relates to ENG-3125 (VXE(MCM) 732 Altitude Excursions); relates to OGCS-108 (VXEP-786 Investigation)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 732
- **Corrective Action:** None, addressed in v1.1
- **Incident Type:** Near Miss
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

VXE 732 with MCM
Statement received from LM FSR:
We were testing landing patterns VCSi (1.0.0.dev7)/OGCS(1.0.0). ELZ altitudes were 200 ft pattern, 300 ft IP1. V732’s altitude increased enroute to IP1, started to descend in IP2, but released out to IP4 at 450 ft. It then climbed in IP4 to over 900 ft AGL. I commanded the plane to Fly to a waypoint in the route to stop the climb.
Later (I believe the final pattern and landing) altitude increased to over 600 ft in IP2 before descending to normal altitudes and landing.
We are grounding flying VCSi/OGCS until we understand the cause.

AAR attached

## Root Cause

The LM pilots found a vulnerability in the 1.0 release of the VSM in which Landing Patterns could be Previewed prior to vehicle reference elevation being established by the OGCS.  As a result, the waypoints in the landing patterns were encoded approximately 2,500 feet higher than expected (the same amount as the reference elevation in MSL).  This defect was addressed in https://jenaero.atlassian.net/browse/MS-395 on September 4 and is now part of the 1.1 release.  @David Grosher

## Comments (14)

### Greg Fryer, 2024-11-22

@Ted Trowbridge Are you already aware of this incident by chance? If not, note that TIQ is grounding.
@Douglas Baker FYSA

### Douglas Baker, 2024-11-22

@David Grosher @Scott Whitney FYSA

### Pat Wells, 2024-11-22

VSM and OGCS logs added

### Craig Burton, 2024-11-22

I reached out to Dan and Garret regarding the 3000 foot spikes in commanded altitude in Garret’s original email.  A quick scan of the VSM logs show that the maximum altitude attained was 2,982 feet MSL, which would be 482 feet AGL at their flight location.

I’m going to dig into the altitudes recorded while flying the landing patterns, but I can’t yet reconcile how the maximum vehicle altitude that I’ve seen so far (482 feet) is less than what was reported by the operator (900 feet and 600 feet).
The vsm-info log was found to contain binary characters, which affected grep’s extraction of data.  Once that was dealt with, I do now see the altitude spikes that were cited:

[embedded: v732-19-Nov-2024.png]
The rapid climb in altitude that occurred at 12:01:56 is coincident with an operator command to Land ELZ.  The AltitudeSet jumps from 410 to 2863 at 12:00:26.
A similar jump occurs at 11:12:13 when the vehicle completes its Primary mission of a single waypoint and transitions to Land PLZ automatically, where AltitudeSet goes from 300 to 2873:

[embedded: altitude-set.png]

### Craig Burton, 2024-11-22

From the VSM logs, the vehicle was flown on two separate dates:  November 19 and 21.  One flight was completed on Nov 19 and two flights were completed on Nov 21.
(Edited to remove the reference to flight date 10/1, which was our FLOPS in Huasna.)

### Craig Burton, 2024-11-22

The times noted above, 11:12:13 and 12:00:26, are associated with the first times at which the landing patterns were executed.  At 11:12:13, the Primary pattern was automatically entered after the autopilot completed its single waypoint primary mission, and at 12:00:26 was the first time that the Emergency LP was commanded by the operator.  This suggests that the rapid climbs observed had to do with the altitudes loaded into the landing patterns themselves.
Reconciling the calibration time of the vehicle with the time at which the landing patterns were Previewed reveals the root cause of this incident:  the landing patterns were previewed prior to the vehicle having been calibrated.  This was a vulnerability in the 1.0 release prior to the extra validation to guard against this scenario (added in MS-395):
The landing patterns were Previewed (Purpose == 0) at 10:06:34 and 10:07:04:
10:06:34.708835:  cucs_req        a010133    Landing Pattern Request (#17000) ff000000 Type Alt
10:06:34.729324:  vsm_resp        ffffffff   Landing Pattern (#17001) ff000000 Pur 0, Type Alt
10:07:04.530041:  cucs_req        a010133    Landing Pattern Request (#17000) ff000000 Type Pri
10:07:04.550516:  vsm_resp        ffffffff   Landing Pattern (#17001) ff000000 Pur 0, Type Pri
But the vehicle wasn’t calibrated until 10:09:21:
10:09:13.092584:  oper            Vehicle reference altitude has been set to 2502 ft MSL.
10:09:21.741257:  oper            Vehicle reporting reference altitude of 2502 ft MSL.
10:09:43.560259:  oper            0x0a010133 uploaded waypoints 1, 2, 3, 4
10:09:43.737884:  ap_ack          Primary route upload has been acknowledged by the AP
10:09:52.804133:  ap_ack          Emergency Landing route upload has been acknowledged by the AP
10:09:58.544470:  ap_ack          Primary Landing route upload has been acknowledged by the AP
Due to the lack of calibration, the landing pattern altitude encodings would not have subtracted the reference elevation of roughly 2,500 feet.  The commanded altitudes of 2,863 and 2,873 feet represent the DTED elevation under IP1 plus the requested AGL value of 300 feet.

### Craig Burton, 2024-11-24

Addendum:  how did they ultimately end up landing successfully if the landing patterns were encoded improperly?  Fortunately, they were uploaded again in flight, 4 times each (PLZ, ELZ).  Because the calibration altitude had been set by the point of takeoff, any of the newly-uploaded patterns would have successfully guided the vehicle to safe landings.

### David Grosher, 2024-11-26

@Craig Burton There was a question from LMCO about whether both un-commanded climbs were analyzed. It looks like you analyzed both un-commanded climbs, but there appears to be a third climb which was un-commanded at the end of the flight where it reaches an AGL of greater than 600 feet, is there any indication in the logs regarding that climb?

### Craig Burton, 2024-12-03

@David Grosher In addition to the two previously discussed (unintentionally) commanded climbs (circled in blue), there was a third near the end of the flight (yellow highlight).  During this climb, the vehicle was flying a Primary landing approach.  The VSM’s logs indicate that the Operating Mode was RTB throughout the climb, from 12:20 to 12:21, with a rapid descent from 12:21 to 12:22.  The RTB operating mode results in the VSM commanding the landing, but inhibiting any further commands until a new mode is entered (i.e. all subsequent VCSi commands are filtered until changed).  Thus, this climb was not commanded by the VSM.
[embedded: v732-19-Nov-2024-annotated.png]
Looking at the AP logs, specifically the reading OLPwrCom from T95_V732_241119_092746_FDR00074.csv, we can see that during this time interval of 12:20 to 12:22, the commanded power (if I’m reading the column correctly), shows a marked reduction in throttle, dropping from 40% to under 10% for the duration of the rapid climb and descent.

[embedded: OLPwrCom.png]
Garret’s notes indicated that there were strong thermals encountered during their tests; I suspect that this uncommanded climb was the result of encountering one of these shortly before landing.

### David Grosher, 2024-12-04

@Craig Burton Great job on the investigation. Can you provide this analysis to LMCO? I’m not sure if Pat handled this communication or if it was informal, regardless let’s send it to them. @Pat Wells @Scott Whitney FYSA.

### Alexander Alan Arnold, 2024-12-10

@Ted Trowbridge Is the investigation analysis/report done? Can we move this item to done?

### Ted Trowbridge, 2024-12-10

@Alexander Alan Arnold @Craig Burton 
Assigning to Craig for closure as he performed the investigation.

### Craig Burton, 2024-12-10

@Alexander Alan Arnold Yes, the analysis is done and the results and root cause have been communicated to LMCO via https://jenaero.atlassian.net/browse/VIT2-501 and verbally, so Garret, Dan and Matt are all aware and have accepted the results.  Can be closed.

### Craig Burton, 2024-12-10

Closing (cancelling) without traversing through entire workflow.

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V732_241119_092746_pack.zip.allow | other | 9839 | 2024-11-22 | listed only |
| altitude-set.png | image | 116 | 2024-11-22 | listed only |
| ogcs-732-logs.tar.gz | archive | 16719 | 2024-11-22 | listed only |
| v732-19-Nov-2024.png | image | 165 | 2024-11-22 | listed only |
| vsm-732-logs.tar.gz | archive | 24499 | 2024-11-22 | listed only |
| OLPwrCom.png | image | 124 | 2024-12-03 | listed only |
| v732-19-Nov-2024-annotated.png | image | 275 | 2024-12-03 | listed only |
