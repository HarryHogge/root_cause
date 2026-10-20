# VXEP-1505: Incident Investigation:  Evaluate LM report of AV 767 landing 1.6 km away from LZ following Link Loss test

- **Issue type:** Bug
- **Status:** DONE
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-09-10
- **Updated:** 2026-01-15
- **Resolved:** 2025-09-10
- **Reporter:** Michael Mohr
- **Assignee:** Michael Mohr
- **Creator:** Michael Mohr
- **Labels:** TIQUILA, Weekly-incident-tracker
- **Customer:** TIQUILA
- **Vehicle Tail Number:** 767
- **Impacted Disciplines:** Software
- **Applicable Subsystem:** SGCS 1

## Description

From Garret’s email:
During lost comms tests, AV 767 landed 1.8 km away from the PLZ.
When Link Loss was set to Land at Active LZ a WO1 appeared at the 10 O'clock position of Orbit 2 in VCSi and a waypoint 1000 at the same location in OGCS (see WO1 and 1000 photo).  The AV flew to the waypoint, then flew east, then flew west directly toward it (see trail to north of Orbit 2 in Lost_Link_Land photo).  Before reaching WO1 again the AV was commanded to fly to Orbit 2 in the Route.  A waypoint parameter window opened in the lower-left corner of the VCSi map for 767 - LOSAuto-RTB - WO1 with MSL = 350 ft, AGL = -2160 ft, IAS = 0, Loiter = N/A (see Lost_Link_Land photo).  WO1/1000 could not be deleted in VCSi or OGCS. 
 
LL was set to Fly LOS Mission and Contingency A was uploaded to the AV, at which point WO1 disappeared in VCSi, but waypoint 1000 remained in OGCS.  LL was set back to Land at Active LZ and the lost comms exercise was repeated.  WO1 reappeared a few seconds after comms were disconnected.  Comms were not restored in order to see what the AV was going to do.  It flew the same pattern again: through WO1, east ~400 meters, west directly toward WO1, transitioned, and landed ~150 meters short of WO1 (at the intersection of the East/West and North/South runways).  It appears that WO1 was IP1 for a PLZ pattern that was not displayed.
 
Note: a PLZ pattern at that location with that approach direction had been created and uploaded to the AV during a previousstep 29 (see Previous PLZ photo).  Prior to launching the AV, VCSi was closed, the landing pattern file was deleted from the vcsi\stalker folder, and a saved PersistedLandingPatterns.json file was copied into the vcsi\stalker folder.  VCSi was restarted and the saved landing patterns were previewed and uploaded to the AV (WO1 and Lost Link photos).

## Comments (4)

### Michael Mohr, 2025-09-10

*From Craig Burton (in MS-885)*
From the VSM logs, this is release 1.3.0:

10:44:35.550292:  init            /mnt/edge/vsm/bin/vsmd build 'main/26b72df'

AAR data package uploaded to condor\Engineering\For Craig\Incidents\2025-09-08_TIQU-4318_001(A).zip

### David Grosher, 2025-09-10

@Michael Mohr @Drew Hildreth @Craig Burton My understanding is that this issue was determined to be operator error with an interaction within VCSi. @Craig Burton Can you confirm?

### Drew Hildreth, 2025-09-10

@David Grosher this was just a record keeping ticket based on your email yesterday. If in fact it wasn’t Operator Error, we can reopen.

### Craig Burton, 2025-09-10

Yes, per Garret’s comment below (via direct/individual email), the root cause was an incorrect workflow within the VCSi application which did not honor our STANAG message workflow for landing pattern support.
I think we figured out part of it.  Alex replicated it in the HIL.  After deleting the PreservedLandingZone.json file out of the LMCDL\vcsi\stalker folder and copying a saved file into the folder and re-starting VCSi, VCSi displayed the full patterns without having to Get Preview, so he (and likely I) was able to upload the LZs to the AV without them being previewed, and as we know from past experience, it doesn’t matter which LZ you select when you upload to an AV, it’s the last LZ that was previewed that gets uploaded.  This would explain why VCSi showed the new LZs while the old (last previewed) ones were uploaded, but it doesn’t explain why OGCS displayed the new LZs or why only IP1 was shown in both VCSi and OGCS (or why it’s possible to upload LZs that have not been previewed).

I will create a separate ticket to evaluate the last sentence in his reply, in blue, but this ticket can be closed.

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| 2025-09-08_TIQU-4318_001(A).zip | archive | 38837 | 2025-09-10 | listed only |
| Lost_Link_Land_at_Wrong_PLZ.jpg | image | 291 | 2025-09-10 | listed only |
| Previous PLZ.JPG | image | 119 | 2025-09-10 | listed only |
| WO1 and 1000  appear.JPG | image | 103 | 2025-09-10 | listed only |
