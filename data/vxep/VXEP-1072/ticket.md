# VXEP-1072: Center wing 592 unable to connect

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** Low
- **Created:** 2025-03-05
- **Updated:** 2026-06-22
- **Reporter:** Cody Smisek
- **Assignee:** Cameron Chapman
- **Creator:** Cody Smisek
- **Links:** relates to FS2-3022 (Troubleshoot CW 592 in Engineering); relates to RMA-511 (VXE-592 Center Wing RMA 250207-1); relates to VXEP-1291 (VXE 592 Crash)
- **Vehicle Tail Number:** VXE 592
- **Plan:** EE decide if any further investigation required for VTOL AP failure
- **Root Cause:** VTOL AP failure, unknown why it will not function at this time.
- **Incident Type:** Squawk
- **Severity:** 3 - Degraded Performance - With Workaround

## Description

Unknown reporter: CW 592 is unresponsive after SD card update.  I think SWAP the SD card again and if that doesn’t work then VTOL AP.

## Issue Status

VTOL AP moved to hardware storage cabinet 3/13/2025
Center wing minus VTOL AP returned to RMA.
Latest Update 3/7/2025 - Smisek: checked for VTOL CW short via breakout harness to CW data cable. Checked OK. Tried powering on iron bird, interface only had one green light on (12v or 3v?) no other lights on interface or AP illuminated. Checked with IR for any obvious heat signatures. Component near USB connector was warmer than surrounding area. Removed avionics from CW and connected to iron bird, still unable to power. Removed AP from interface, powered interface by itself, interface powered up. Put VTOL AP on iron bird interface, unable to power either. Tried removing SD card given the situation occurred after a SD card swap. No improvement. 
Conclusion, VTOL AP is causing VTOL avionics to not power up. Some type of hardware failure on VTOL AP. 
VTOL AP red tagged and removed from cw. Currently on Smisek’s work bench. (3/7/2025)

Old update prior to 3/7/2025
Jason: I connected CW to my bench and powered it using an XComm PCB. The Power supply drops to 6V and the XComm PCB produces audible ringing sounds. I removed the CW and my XComm PCB functions properly on it’s own. I asked Connor his thoughts since he was standing nearby. He thinks the 12V regulator on the XComm PCB is current limiting due to something electrically wrong on the VTOL PCB. So before, we proceed with software checks, we should have an EE review the hardware.

## Comments (7)

### Cody Smisek, 2025-03-07

@Cameron Chapman see ticket status. Jason was assigned this ticket to troubleshoot for VTOL not working. I’ve narrowed it down to the VTOL AP but unknown what’s causing the VTOL AP itself to not power. Seems like microscope level work. Unsure if we need to further diagnose at this point, but assigned to you as it appears to be a EE/hardware issue.

### Cody Smisek, 2025-03-07

@Cameron Chapman looking at the RMA ticket, it looks like the failure occurred after an attempted SD card swap in the field. Seems probable that this was caused during that time.

### Cameron Chapman, 2025-03-12

Thanks @Cody Smisek we have a investigation cabinet for HW we are not working. You could store it in there and update location above.

### Cody Smisek, 2025-03-13

AP moved to cabinet.

### Christa Meck, 2026-06-22

@Pat Wells is this still an open investigation?  It’s from March 2025.

### Pat Wells, 2026-06-22

@Cody Smisek  over to you see @Christa Meck question below.  This wasn’t a Global support ticket.

### Cody Smisek, 2026-06-22

based on issue status this investigation is still open. I can’t speak to whether or not RDW wishes to pursue further investigation.

## Attachments (0)
