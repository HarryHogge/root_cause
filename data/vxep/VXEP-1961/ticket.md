# VXEP-1961: Native app 1.4.1 will not control take control of AP

- **Issue type:** Bug
- **Status:** New
- **Priority:** Low
- **Created:** 2026-07-15
- **Updated:** 2026-09-04
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Ted Trowbridge
- **Creator:** Alexander Alan Arnold
- **Labels:** Redwire, Software

## Description

During this weeks IQT for Army cyber it was discovered that the native app is encountering a problem where after logging in the user is unable to control the AP. the windows cache clearing did not fix the issue

If the user connects via web app and releases AP the native app will still not connect to AP 
If you take control via web app the native app shows that the native app has control 
when the user had control in web app and attempted to conduct the launch wizard in native app they could not get past battery config

## Comments (7)

### Alexander Alan Arnold, 2026-07-15

@Ted Trowbridge The team will get a screen recording tomorrow and verify firewall config. Anything specific you want them to pull off the GCS laptop?

### Alexander Alan Arnold, 2026-07-16

[embedded: Video.805910644.861582_9306.mp4]
@Ted Trowbridge attached is a video of the issue

### Ted Trowbridge, 2026-07-16

@Alexander Alan Arnold I would like to grab logs from the native app, this can be done from the AAR page (package frontend logs).
The Native App works via multicast, it looks like it was receiving but not able to send messages.

### Alexander Alan Arnold, 2026-07-16

@Ted Trowbridge Thanks! ill have the guys grab one when they get a few minutes in-between training flights

### Alexander Alan Arnold, 2026-07-16

@Ted Trowbridge logs added, sorry for the delay. they had some issues during training, unrelated to VXE equipment.

### Ted Trowbridge, 2026-09-04

@Alan Burnsworth @Bethany Ponce 
When I looked into this it appeared the Windows multicast died with a generic error message.  Can you help investigate what might’ve happened?
We’d like to handle this more gracefully from the native app but can’t do much about an OS level error.

### Ted Trowbridge, 2026-09-04

@Alexander Alan Arnold It looks like the attached logs are corrupted - can you reupload or grab them again?

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| Video.805910644.861582_9306.mp4 | video | 11725 | 2026-07-16 | listed only |
| frontend-logs-2026-07-16T19-36-01-500Z.tar.gz | archive | 2114 | 2026-07-16 | listed only |
