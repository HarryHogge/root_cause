# VXEP-1977: VXE 1034 Crash during takeoff

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** High
- **Created:** 2026-08-06
- **Updated:** 2026-10-16
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Alexander Alan Arnold
- **Creator:** Alexander Alan Arnold
- **Labels:** Crash, PMA263, RCCA, Weekly-incident-tracker
- **Customer:** Air_PMO
- **Vehicle Tail Number:** VXE 1034
- **Vehicle Configuration:** standard vxe unknown config
- **Incident Type:** Aircraft Loss
- **Severity:** 1 - Flight Critical
- **Executive Summary:** Requesting equipment be returned for investigation; probable cause motor failure

## Description

No operator statement at this time attached AAR mission file and believed SA footage
the following was written in the GCS log file by operator
“all preflights with in lims. during launch AV climb to around 100ft AGL. the back right lift prop stop spinning and av lost control and hit the ground”

## Plan

8/6/2026- Recommend, at minimum, inspection of right rear motor for root cause determination. Ideally, inspection of all components from VTOL AP to right rear motor in event issue is not at the right rear motor itself.

## Issue Status

8/6/2026 awaiting hardware return / inspection to determine root cause.

8/6/2026 data review/findings
SA Cam shows a launch and at a higher altitude ~100ft a pitch up and roll right. During rapid vtol descent, aircraft is yawing right. 
AAR data confirms at ~100ft a pitch up and roll right (uncommanded) followed by rapid descent in VTOL with uncommanded yaw. 
Motor 3 throttle is sustained high when issue occurs. Indicating motor 3 (rear right motor) is likely the cause of issue. 
Additionally, it appears operator commanded a VTOL abort after the initial pitching/rolling (at 793sec). 
[embedded: image-20260806-161340.png]

## Comments (6)

### Cody Smisek, 2026-08-06

From SA cam, looks like lift motor or HLB failure. Uncontrolled yaw during VTOL launch (abort?)
HLB cell balances look normal

### Alexander Alan Arnold, 2026-08-06

was it on take off or landing? @Cody Smisek im assuming take off based on SA video

### Cody Smisek, 2026-08-06

@Alexander Alan Arnold SA cam also shows ground personnel rapidly approaching the aircraft after the collision with the ground. Would highly recommended at least giving a few more seconds before approaching in event of battery fires or potential system spin up. The motors began to home while the person was in between lift booms and fuse.

### Cody Smisek, 2026-08-06

@Alexander Alan Arnold issue status updated with answer.

### Alexander Alan Arnold, 2026-08-07

Will work with customer to get VXE returned to aid in investigation

### Drew Hildreth, 2026-09-18

@Alexander Alan Arnold Has this aircraft been requested?

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| DOD SAFE-81jE8tEstEQcmyP0.zip | archive | 8236 | 2026-08-06 | listed only |
| MISB-08052026-120823-1-0.mpg | video | 4686 | 2026-08-06 | listed only |
| T95_V1034_260805_120814_pack.zip | archive | 1385 | 2026-08-06 | listed only |
| image-20260806-161340.png | image | 85 | 2026-08-06 | listed only |
