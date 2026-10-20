# GCSS-364: FTP of mission.txt does not use integrity checks

- **Issue type:** Bug
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2024-09-26
- **Updated:** 2026-09-23
- **Resolved:** 2026-09-23
- **Reporter:** Ted Trowbridge
- **Creator:** Ted Trowbridge
- **Links:** causes VXEP-556 (VXE 600 W1 disappeared after passing Mission Check in Launch Wizard)

## Description

Mission uploads to the autopilot include integrity checks.  Mission.txt uploads via FTP do not include integrity checks.  It is possible that mission.txt could be corrupted during transfer to or from the vehicle.

## Comments (2)

### Michael Berger, 2024-10-31

@Ted Trowbridge Not necessarily a bug/more of an improvement. But adding integrity checks could improve reliability.
Note that there are no integrity checks on any of our ftp file transfers.
mission.txt upload/download.
firmware and configuration updates
AAR log file downloads.
Any recommendations on how to check the integrity?

Manual Verification: You can manually compare the file sizes and contents before and after the transfer.
Checksum Files: Create a checksum of the file before transfer, then generate a checksum of the transferred file and compare the two
The manual would double the time.
Checksums would not be too slow.

### Christa Meck, 2026-09-23

No work done in over a year.  Canceling.

## Attachments (0)
