# GCSS-383: Incorrect MSL altitudes reported in the UI when operating without DTED

- **Issue type:** Bug
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2024-11-22
- **Updated:** 2026-09-23
- **Resolved:** 2026-09-23
- **Reporter:** Ted Trowbridge
- **Assignee:** Michael Berger
- **Creator:** Ted Trowbridge
- **Components:** GCS Application
- **Links:** causes VXEP-784 (VXE 637 aircraft altitude reporting incorrectly)

## Description

The GCS shows incorrect MSL altitudes in various places when the vehicle is launched without DTED.  The discrepancy seems to come from the difference in actual MSL altitude from the reference altitude set at calibrations which uses DTED (zero when missing).
Steps To Reproduce
- Temporarily remove DTED from the GCS 
- (e.g. rename C:\Users\Public\Documents\My GCS\DTED folder to something else so the GCS can’t find it)
- Launch the GCS and verify no DTED is available (map footer shows an ‘Elev: ---’ for the cursor position)
- Run a HIL sim where the vehicle in xplane is at a non-zero MSL altitude
- Launch and notice discrepancies in the UI where MSL is reported as different values.  Compare this to the GPS altitude.


[embedded: image-20241122-184205.png]

## Comments (1)

### Christa Meck, 2026-09-23

No work done in over a year.  Canceling.

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20241122-184205.png | image | 6007 | 2024-11-22 | listed only |
