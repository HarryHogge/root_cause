# GCSS-434: Mission simulation blocks UI thread

- **Issue type:** Bug
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2025-03-24
- **Updated:** 2026-09-23
- **Resolved:** 2026-09-23
- **Reporter:** Ted Trowbridge
- **Creator:** Ted Trowbridge
- **Links:** causes VXEP-220 (VXE 487 - GCS blocking resulting in multiple FWAP link losses )

## Description

The mission simulation uses the MFC UI thread which causes the UI to freeze during simulation.
The UI thread is also used for vehicle comms, which causes link faults.

## Comments (1)

### Christa Meck, 2026-09-23

No work done in over a year.  Canceling.

## Attachments (0)
