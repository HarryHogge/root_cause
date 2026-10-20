# FS2-2852: CA for excluding erroneous LRF measurements

- **Issue type:** Task
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-02-11
- **Updated:** 2025-03-04
- **Resolved:** 2025-03-04
- **Reporter:** Scott Whitney
- **Assignee:** Ben Triplett
- **Creator:** Scott Whitney
- **Parent:** FS2-2851 VXE 500 Freezing fog caused issues with ADP LRF
- **Links:** relates to VXEP-978 (VXE 500 Freezing fog caused issues with ADP LRF)
- **Epic Link:** FS2-2851
- **Sprint:** FS2 Sprint 30

## Description

The simple fix is to exclude unreasonable LRF range measurements from the AGL estimate. This would be done in sensorAgl.c around line 684. A fix was already implemented to prevent this issue when in FW flight but is also now needed in VTOL flight. The current code looks like the following:
```
                // BIT: only consider LRF good when not in FW flight state - get too many erroneous readings in FW
                bool isFwFlight = (APVTOL_FWFLIGHT == mavGetHostVtolState());
				if(lrfstat && (lrfgood >= lrf_good_count) && (false == isFwFlight))		// laser deemed good
				{
```
so another check would be added that will ask if the system has
- been in FW flight
- is now in VTOL flight (e.g. landing)
- has ever had a reasonable measurement of LRF range. The LRF typically picks up ranges starting between 50 and 100 feet above the ground. If the first measurement is under 10 feet then it is likely erroneous and should be disregarded. Once a reasonable measurement (or say series of e.g. 10 measurements?) has been taken then assume all further measurements are good. This is a simple fix, but something more robust and complicated could also be implemented - i.e. some means of continuing to ensure that subsequent measurements are reasonable until touchdown.

## Comments (0)

## Attachments (0)
