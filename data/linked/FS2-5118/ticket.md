# FS2-5118: Low energy RTB in denied.

- **Issue type:** Task
- **Status:** To Do
- **Priority:** Low
- **Created:** 2026-09-16
- **Updated:** 2026-09-16
- **Reporter:** Eric Brewer
- **Assignee:** Eric Brewer
- **Creator:** Eric Brewer
- **Parent:** FS2-5098 Issues Identified at CANJAM
- **Epic Link:** FS2-5098

## Description

Were u-driving to return to base with a good bit of wind.  Selected dash, then shortly after it reported low energy RTB (battery showed 71% when they started dash), system forced them back into nav for RTB. It still said they were in u-drive but for a little bit it was not respecting their commands.  It's down safe now but they wanted to know what happened.  This was one of the Molson birds they were running with JGCS.
https://redwireglobal.sharepoint.com/sites/EdgeUSOnlyMaterial/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FEdgeUSOnlyMaterial%2FShared%20Documents%2FGeneral%2FVBN%5FINTEGRATION%2FKEF%2FKEF%5FEXTERNAL%5FSHARE%2FFlightData%2F2026%5F09%5FCANJAM%2F2026%5F09%5F08%2FLost%20UDrive%20during%20Dash&viewid=0c1aa895%2D9073%2D46b2%2Db705%2Dfcb1f8f035fb&d=w75f9d3ec67a04ed685411b0660880dbe&csf=1&ovuser=dffebc72%2Df052%2D46dc%2Db61d%2D6399783a9682%2Ceric%2Ebrewer%40rdw%2Ecom&TeamsCID=6483917f%2Dc050%2D4406%2Db357%2D9a18703a113e&OR=Teams%2DHL&CT=1788210771606&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiI0OS8yNjA4MDIwMDYyMCIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D&CID=7dbd36a2%2D405d%2D0000%2D03d7%2De9fec70add17&cidOR=SPO&FolderCTID=0x012000F5D068CBCFBB35489D6EA0C2215CC8DD

## Issue Status

Identified issue with DR position estimate in 6.6.1 release, it has since been fixed so we should retest this in 6.8.1.

Basically the 2d position jumps between DR and the INS estimate due to a bug in the code.
[embedded: image-20260916-153316.png]
When those jumps occur the position is very far from base triggering low energy RTB.

Summary — V954 Low Energy RTB Root Cause
Flight: T115_V954, 2026-09-08, AP firmware Ver. 6.05u (Build 0x6050015)
Symptom: Spurious "Low Energy RTB" triggered mid-flight.
Root cause: GPS-denied dead reckoning was active, but NewGpsPosition() in gpsnav.cpp continued unconditionally applying raw (and invalid) GPS lat/lon into posX/posY instead of being suppressed during DR. This produced a second, divergent position track that grew to ~138,000 ft off the true (DR-derived) position. When FixGood() transiently flickered true, this corrupted position was copied into PositionEst.X/Y and fed into HowFarToLz(), inflating the estimated distance-to-LZ from ~18,285 ft to ~105,326 ft. The corresponding energy recovery-time estimate (FCRecovery()) rose from ~37 min to ~166 min, exceeding BattEndurance() (~160 min) and latching fcbattrtb/LowEnergyRTB — a correct RTB decision made on corrupt position input.
Fix already present: Commit 3720904 ("Bug fix for DR position jumps", E. Brewer, 2025-08-29) in gpsnav.cpp, present in release/605y and later, not present in release_605u_dev (the version flown on V954):
```
-       NewGpsPosition(nmea->DegLat, nmea->DegLon, CurrentAltitude);
+       if(!DeadReckonFlag)
+               NewGpsPosition(nmea->DegLat, nmea->DegLon, CurrentAltitude);
```

Next step: Re-test the same GPS-denied scenario on 6.05y+ (or later) to confirm the DR position jumps and false low-energy RTB no longer occur.

## Comments (0)

## Attachments (1)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20260916-153316.png | image | 81 | 2026-09-16 | listed only |
