# VXEP-1608: VXE 881 CW not detected but able to access .10 page and GPS Satellites displayed in SUAV

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-11-17
- **Updated:** 2026-08-05
- **Resolved:** 2026-08-05
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Connor Peebles
- **Creator:** Alexander Alan Arnold
- **Labels:** LRR, Weekly-incident-tracker
- **Links:** relates to RMA-854 (35x VXE-881 RMA 251120-3); relates to RMA-853 (LEMB 3-0042 RMA 251120-4); relates to FS2-4282 (NCR: No GPS Lock, No Sats); relates to ENG-3710 (2162931 - WIRE HARNESS, B30 LIFT BATTERY CAN BREAKOUT); relates to FS2-4335 (Display more information in failure messages); relates to FS2-4351 (Investigation: v881 not passing OGCS Sensor calibrate page); relates to VXEP-1880 (LEMB CAN EE Investigation)
- **Customer:** LRR
- **Vehicle Tail Number:** 881
- **Vehicle Configuration:** BLK35X, LEMB
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround

## Description

VXE 881 displayed characteristics of a failed SD card as the Soldier team was unable to obtain GPS fix on OGCS and when we asked them to connect in SUAV they received a “CW not Detected” message. 

Once we were able to retrieve the aircraft and conduct testing, we received the same warning and no GNSS fix in OGCS. 

We were able to access the .10 webpage, receive SA cam feed, and saw satellites in SUAV via the GPS status menu. I have attached screenshots and an AAR for the issue. 

UPDATE as of 20NOV25 
We attached the 881 CW to three different VXEs and were unable to connect to it in SUAV but were able to access the .10 page
We attached three separate CWs to 881s fuselage and were unable to connect to them in SUAV but could access the .10 page for each one. 

When testing in OGCS the aircraft never received a gnss fix and was unable to reset the VTOL Autopilot during the LW.

## Corrective Action

All boards on the CAN bus network were replaced.
XCOMM Board replaced in RMA ticket: [RMA-854] 35x VXE-881 RMA 251120-3 - Jira
GNSS Interface Board replaced: https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/NCR%20List/DispForm.aspx?ID=8462&e=BTNXzu
VTOL AP stack replaced: https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/NCR%20List/DispForm.aspx?ID=8367
ADP Replaced: https://jenaero.sharepoint.com/sites/JAI_Operations/Lists/NCR%20List/DispForm.aspx?ID=8855&e=MVezji
LEMB L3-0042 investigated in https://jenaero.atlassian.net/browse/VXEP-1880 

Long term corrective action is to replaced CAN chips across the airframe with ones more tolerant to faults, ESD, and temperature. Such example here: [AV-717] 2135413-01 - XCOMM UAP - REV A01 - Jira

## Issue Status

881 has been repaired and returned to service. LEMB L3-0042 is awaiting further investigation here https://jenaero.atlassian.net/browse/VXEP-1880

## Root Cause

Introduction of LEMB induced electrical stress to the vehicle’s CAN bus which severely degraded or disabled all CAN transceiver chips.

## Comments (24)

### Cody Smisek, 2025-11-18

That looks like a CAN issue not an SD card issue. Unless SD card issues look like CAN issues.

### Alexander Alan Arnold, 2025-11-20

Aircraft just arrived in HSV. We assembled it and got the same behavior, I was saying that at first, we thought it was CW SD Card issue due to the errors message, this is the first CW I have encountered where the SD card was fine but the aircraft did not recognize the CW as being connected, we will attach another CW to see if it's a possible fuselage cable issue. @Cody Smisek

### Ruysser Gabler, 2025-11-20

@David Grosher this seems like the same issue that we are having on 757 right now

### Alexander Alan Arnold, 2025-11-20

We tried another CW on the fuselage and got the same result. @David Grosher

### Lauren Velasquez, 2025-11-24

@Alexander Alan Arnold @David Grosher This Fuselage has arrived in SLO

### Cody Smisek, 2025-11-25

per @Connor Peebles 
looks like the same problem as 757, I would say replace the xcomm and we can troubleshoot the xcomm further independently
I recommend upgrading the can chip or pull more heat out of the avi box

### Connor Peebles, 2025-11-25

@Cody Smisek @David Grosher To truly confirm it is the can chip that is able to receive but not transmit, and that it is a failure of the FETs driving the Tx side, we can and should send the chips out to a lab to be decapsulated or cross sectioned

### Lauren Velasquez, 2025-12-01

@Cameron Chapman We have also received the LEMB for this AC for evaluation.

### Cameron Chapman, 2025-12-01

@Lauren Velasquez Thank you Lauren. Do you know why the LEMB was returned? I don’t see anything on this incident related to LEMB. Is that for 818 not 881? https://jenaero.atlassian.net/browse/VXEP-1568 FYI @Eric Brewer

### Lauren Velasquez, 2025-12-01

@Cameron Chapman The battery was causing CAN Bus issues; VXE-818 is traveling with a gimbal- No battery.

### Eric Brewer, 2025-12-01

@Lauren Velasquez @Cameron Chapman thanks.  What is the SN of the LEMB? Was it 3L0042?  Cameron that was one of the units that we traced down to some CAN-related aborts.  3L0030 was the other.

### Lauren Velasquez, 2025-12-01

@Eric Brewer Yes RMA Board -LEMB 3-L0042 RMA 251120-4

### Eric Brewer, 2025-12-01

@Lauren Velasquez thanks.  @Jeremy Kostel FYI.

### Lauren Velasquez, 2025-12-08

@Eric Brewer Do you know where this battery should be delivered?

### Eric Brewer, 2025-12-08

@Lauren Velasquez I think delivering to @Jeremy Kostel would makes sense.

### Connor Peebles, 2026-01-07

Assigning back to me

### Lauren Velasquez, 2026-01-07

Back in RMA

### Scott Whitney, 2026-02-13

From @Brandon Slater 
https://jenaero.atlassian.net/browse/FS2-4282?focusedCommentId=75138 
Steps so far:
- Confirmed correct firmware & configs for 6.6.1 BLK35X were on aircraft
- Checked GPS on VTOL webpage, No Sats shown only C/No value
- checked GPS on GCS, No Sats shown only C/No value
- Repushed firmware for 6.6.1
- Same results as above
- Checked GPS data from Putty and Novatel Application Suite, saw GPS data so data is getting to OEM7700

### Scott Whitney, 2026-02-13

@Brandon Slater - did you confirm the nov was config correctly?

### Brandon Slater, 2026-02-13

@Scott Whitney verified nov configs were correct as well when using the Novatel Application Suite

### Brandon Slater, 2026-02-13

attached logs from v881 [embedded: v881_investigation.zip]

### Cameron Chapman, 2026-02-17

We do not seem to have a cable made to do this troubleshooting. Desiray Johnston I discussed with Connor. It seems like damage is likely on the GNSS interface board, and it is most efficient to pull the box, swap the board, and test if working again. Is your team able to support that? I can update JIRA with that dispo

### Connor Peebles, 2026-02-27

Replacing GNSS Interface V3 inside avionics box resolved issue. Will acquire the removed part for further inspection.

### Connor Peebles, 2026-08-05

Vehicle was repaired after replacing all boards on the CAN bus network. All CAN chips were damaged from LEMB stress to the CAN bus network. Further LEMB investigation taking place on linked tasks.

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 881 Sats displayed SUAV.jpg | image | 307 | 2025-11-17 | listed only |
| AAR_V881_20251118T031007Z.zip | archive | 35359 | 2025-11-17 | listed only |
| OGCS no fixed wing Sats.jpg | image | 284 | 2025-11-17 | listed only |
| SA cam feed and No CW detected Warning.jpg | image | 365 | 2025-11-17 | listed only |
| VTOL no sats OGCS.jpg | image | 295 | 2025-11-17 | listed only |
| VXE SUAV faults page 881.jpg | image | 362 | 2025-11-17 | listed only |
| acessing the VTOL page 881.jpg | image | 471 | 2025-11-17 | listed only |
| v881_investigation.zip | archive | 3434 | 2026-02-13 | listed only |
