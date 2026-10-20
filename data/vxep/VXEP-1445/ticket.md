# VXEP-1445: Adjust altitude displayed in OGCS to work in GPS-denied.

- **Issue type:** Task
- **Status:** New
- **Priority:** Low
- **Created:** 2025-07-23
- **Updated:** 2025-07-23
- **Reporter:** Eric Brewer
- **Creator:** Eric Brewer
- **Parent:** VXEP-1237 Apex Must Haves (VBN)
- **Epic Link:** VXEP-1237

## Description

OGCS currently uses PayloadMetaGps.MSL that’s nested in NetworkMetadataAll.PayloadMetaAll​ for altitude display on the GCS.  The AGL is calculated using this MSL subtracted from the DTED MSL calculated based upon the current best estimate of position.  
The issue is that in the case where both GPS and VBN are invalid, the GPS-reported altitude will be incorrect and not what is used by the autopilot.  The autopilot uses a baro-derived altitude referenced to the takeoff point and corrected if GPS is available:
[embedded image-20250723-132653.png]
The baro-derived measurement is stored in 'm_currread.ss.Altitude'.  
The INS-derived MSL should be accurate if we have GPS or VBN available, but to avoid confusing pilots we should use the baro-derived solution.  Note: I believe the ss.Altitude value that comes down is effectively height above launch point, so you will need that GetReferenceElev() call to add back in the reference of the takeoff point (I think) to get a true MSL.
I’m not clear on what changes this drives into OGCS and/or VSM but lets' discuss.
@Ted Trowbridge @Craig Burton

## Comments (0)

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20250723-132653.png | image | 136 | 2025-07-23 | listed only |
