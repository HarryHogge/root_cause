# VXEP-11: TPTR-5 VXE 407: (VTOL-AP-WD) Unexpected Behavior Seen During Vertical Landing

- **Issue type:** Incident (8D)
- **Status:** Canceled
- **Resolution:** Done
- **Priority:** High
- **Created:** 2023-08-23
- **Updated:** 2024-03-04
- **Resolved:** 2024-03-04
- **Reporter:** Allen Gardner
- **Assignee:** David Grosher
- **Creator:** Allen Gardner
- **Labels:** VTOL-AP-WD
- **Links:** relates to ENG-2990 (VXE 407 Error during transition for landing); relates to VA-30 (Edge internal troubleshooting-VXE 407 -VTOL AP Froze-Error during transition for landing, VTOL AP WD); is blocked by FS2-749 (Embedded SW Robustness Initiative); is blocked by FS2-603 (Trace support); is blocked by FS2-751 (Speedgoat Test Capability Development); is blocked by FS2-806 (Embedded SW Evaluation of VTOL AP); relates to RMA-122 (VXE407 230519); relates to VXEP-41 (TPTR-74 VXE 510: (VTOL AP WD) Consolidated Watch Dog tracking); relates to VXEP-230 (Tail 499 crash during VTOL landing from 10-15', system disarm/re-arm and launch post-crash. NCR 1787)
- **Customer:** TIQUILA
- **Vehicle Tail Number:** VXE 407
- **Incident Type:** Near Miss
- **Severity:** 1 - Flight Critical
- **Impacted Disciplines:** Software

## Description

On the final day of the Demos, and on the final flight of the day (clear skies, 30C, minimal wind, around 13:30 on 27 April 23), a Stalker VXE30 with battery power source was flown with a ‘drop’ payload. The aircraft launched vertically without incident and flew for some time before successfully operating its ‘drop’ payload. Shortly following the start of its vertical descent to land, all four VTOL motors stopped. The aircraft tipped nose down and entered a short dive, gaining airspeed, before levelling off and regaining level flight. The aircraft then carried out a half circuit of the field before returning, with VTOL motors running, to above the original landing point, and then successfully landed vertically with no further incident. The aircraft was then recovered as normal. During this time, Matt ensured that visitors were kept away from the flight path of the UAV and Garret managed the safe landing and recovery of the UAV. Matt Curran confirmed by email today (15-May-23) the serial number of the Stalker on which the issue was detected; AC 407 with 407s wing. Impacted Requirement:  SRD-690 The [Air Platform] shall be able to land.

## Plan

Current assess this is the same WD issue as https://jenaero.atlassian.net/browse/VXEP-41 
Please see that issue for status (will be copied here on completion or if difference discovered.

## Issue Status

Current assess this is the same WD issue as https://jenaero.atlassian.net/browse/VXEP-41 
Please see that issue for status (will be copied here on completion or if difference discovered.

## Root Cause

Current assess this is the same WD issue as https://jenaero.atlassian.net/browse/VXEP-41 
Please see that issue for status (will be copied here on completion or if difference discovered.

## Comments (2)

### Cameron Chapman, 2023-12-04

Duplicating comment from the linked issue. @David Grosher here was the latest status for this aircraft. Is it still correct? 
@Pat Wells or @Greg Fryer do we need LM approval to do this, or are we approved to proceed. 
- Replace red AP board.
- Red AP board is red tagged, then installed into an upcoming HIL. The AP board and HIL should be labelled with this incident number. Add AP SN to this issue. Report if the issue ever happens again, and the circumstances of the occurrence.
- Return the 407 aircraft for RMA and SCO flight with new AP board.

### Pat Wells, 2023-12-05

@Cameron Chapman please proceed with Red AP board replacement

## Attachments (0)
