# FS2-3022: Troubleshoot CW 592 in Engineering

- **Issue type:** Story
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-02-24
- **Updated:** 2025-03-11
- **Resolved:** 2025-03-07
- **Reporter:** Jason Scherer
- **Assignee:** Jason Scherer
- **Creator:** Jason Scherer
- **Links:** relates to RMA-511 (VXE-592 Center Wing RMA 250207-1); relates to VXEP-1072 (Center wing 592 unable to connect)
- **Sprint:** FS2 Sprint 30, FS2 Sprint 31

## Description

Issue description: CW 592 is unresponsive after SD card update. It is in Engineering but there is no VXEP issue. I think SWAP the SD card again and if that doesn’t work then VTOL AP.
Investigation: I connected CW to my bench and powered it using an XComm PCB. The Power supply drops to 6V and the XComm PCB produces audible ringing sounds. I removed the CW and my XComm PCB functions properly on it’s own. I asked Connor his thoughts since he was standing nearby. He thinks the 12V regulator on the XComm PCB is current limiting due to something electrically wrong on the VTOL PCB. So before, we proceed with software checks, we should have an EE review the hardware.

## Comments (6)

### Jason Scherer, 2025-02-24

Looked for CW on Engineering floor, but I could not find it. Waiting for a POC to reach out to for it’s location.

### Jason Scherer, 2025-02-26

Need EE review. CW has electrical issues. See description.

### Cody Smisek, 2025-03-04

@Jason Scherer I’m going to open a ticket in the VXE Problems project for this.

### Pat Wells, 2025-03-05

@Cody Smisek did you open the VEXP ticket?

### Cody Smisek, 2025-03-05

@Pat Wells no, it’s on my list of things to do. feel free to create the ticket if you have time.

### Cody Smisek, 2025-03-06

@Jason Scherer opened VXEP ticket, track info there.
@Pat Wells

## Attachments (0)
