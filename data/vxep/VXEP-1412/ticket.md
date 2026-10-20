# VXEP-1412: VXE 401 Aborted launch

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed, but added to Bermuda Triangle List
- **Resolution:** Cannot Reproduce
- **Priority:** Highest
- **Created:** 2025-07-16
- **Updated:** 2026-08-14
- **Resolved:** 2026-02-02
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Stephen Peters
- **Creator:** Alexander Alan Arnold
- **Labels:** HLB_bad_cell, PMA263, Weekly-incident-tracker, battery
- **Links:** relates to VXEP-1485 (VXE-499 Hard Landing/ HLB Cell Drop Out)
- **Customer:** PMA263
- **Vehicle Tail Number:** VXE 401
- **Vehicle Configuration:** VXE 30, battery config, Vidar, HD40
- **Plan:** Investigate HLB from incident to determine if it had the same issues as the other bad HLBs. @Stephen Peters
- **Root Cause:** suspected bad HLB, unable to determine since HLB cable was not plugged in
- **Severity:** 1 - Flight Critical

## Description

Operator statement
Operating Stalkers 398 and 401 out here in the Shoal Water Bay Training Area for exercise Talisman Sabre and had a failed launch today which resulted in an automated abort to a hard landing back on the vehicle stand cracking the tail boom. GCS software as well as all firmware up to date in compliance with the latest baseline configuration. The payload was the ViDAR V3 daytime system in conjunction with an HD-40LV; FDR and relevant photos attached. We suspect this was due to a bad HLB. Battery information attached in screenshots (note this was practically a brand new battery). The aircraft ascended smoothly to about 15-20 ft before the VTOL motors appeared to begin pulsing, self aborting, and descending back down. At this point the ground crew called for the AVO to manually abort. The abort launch button was the pressed on the user launch control panel. The aircraft failed to back up the usual 10 feet when aborting and thus landed firmly back on the vehicle stand, cracking the tail boom. No other major damage is evident at this point. Please note that the AVO hit the abort launch button AFTER the aircraft had already started descending back to the deck.

## Comments (15)

### Jackson Riley Curvin, 2025-07-16

[embedded: image-20250716-131456.png]

### Jackson Riley Curvin, 2025-07-16

[embedded: image-20250716-131534.png]

### Jackson Riley Curvin, 2025-07-16

[embedded: image-20250716-131720.png]

### Jackson Riley Curvin, 2025-07-16

First look seems to have lost Satellites, around the time of launch @David Grosher

### Jackson Riley Curvin, 2025-07-16

[embedded: image-20250716-132007.png]

### Jackson Riley Curvin, 2025-07-16

[embedded: image-20250716-132059.png]

### David Grosher, 2025-07-16

@Alexander Alan Arnold @Jackson Riley Curvin The abort appears to be from the GCS as reported in the operator statement. With no battery data, I’m not sure that any conclusions can be drawn regarding the HLB. @Stephen Peters Is there a way for the HLB to be tested on the ground under load?

### Jackson Riley Curvin, 2025-07-16

@David Grosher  I put a screen shot from the logs it looks like satellites dropped out around the time of launch.

### David Grosher, 2025-07-16

@Jackson Riley Curvin It looks to me like the nSats dropped to zero when the vehicle landed and hit the stand. I don’t think it was the cause of the abort.

### Alexander Alan Arnold, 2025-07-16

[embedded: image-20250716-190706.png]
From the vtevlog, 
Is the data log line sync buffer indicating a time out? 
Also, I see the user commanded abort, but they are saying it was aborting before he selected that.
Are you saying that the aircraft was not aborting until they commanded abort? 
@David Grosher

### David Grosher, 2025-08-15

@Alexander Alan Arnold Given the timing, I suspect this is another issue with the HLB but we don’t have any data to confirm it. We should RMA that battery just to be sure, if we know the SN. Otherwise we may need to close this one given the lack of data.

### Drew Hildreth, 2025-09-15

@Jackson Riley Curvin @Michael Mohr Has there been a determination on what happened here?  I know what we see in the plots, but there is no update to the Plan, or Issue Status or Root Cause. Has anybody made an attempt and had an engineer to bless off on the findings?

@David Grosher is there anything you need from us on this one?

### David Grosher, 2025-09-15

@Drew Hildreth There is a good chance given the HLB issues that this is related. Unfortunately, the HLB data connection was not hooked up during this flight so we don’t have any data to confirm it. I agree the HLB used should be RMA’d for further study. I don’t have any additional time to devote to this investigation.

### David Grosher, 2025-10-31

@Alexander Alan Arnold No this isn’t an issue. The File I/o was refactored and this is simply an error being logged.

### Scott Lovett, 2026-02-02

Customer did not have data cable plugged in, so needed cell data is not available for RCCA.

## Attachments (7)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V401_250715_203931_pack.zip | archive | 2481 | 2025-07-16 | listed only |
| image-20250716-131456.png | image | 19 | 2025-07-16 | listed only |
| image-20250716-131534.png | image | 20 | 2025-07-16 | listed only |
| image-20250716-131720.png | image | 26 | 2025-07-16 | listed only |
| image-20250716-132007.png | image | 64 | 2025-07-16 | listed only |
| image-20250716-132059.png | image | 53 | 2025-07-16 | listed only |
| image-20250716-190706.png | image | 80 | 2025-07-16 | listed only |
