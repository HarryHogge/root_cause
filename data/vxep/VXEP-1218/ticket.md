# VXEP-1218: VXE-758 VXE SUAV "closing" during sync and sim

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-04-18
- **Updated:** 2025-10-29
- **Resolved:** 2025-10-29
- **Reporter:** Alexander Alan Arnold
- **Assignee:** Ted Trowbridge
- **Creator:** Alexander Alan Arnold
- **Labels:** Edge_Asset, Weekly-incident-tracker
- **Vehicle Tail Number:** 758
- **Vehicle Configuration:** VXE 30 standard battery config
- **Problem Type:** Discovered Issue
- **Incident Type:** Other (Record"Event Type: XXXXXX" in the description)
- **Severity:** 4 - Annoyance

## Description

During the launch wizard for VXE 758 when syncing and running the mission sim the VXE SUAV application will “close” and reopen.

## Comments (13)

### David Grosher, 2025-04-18

@Ted Trowbridge FYSA

### Ted Trowbridge, 2025-04-23

@Alexander Alan Arnold 
The video shows an unexpected and annoying flashing, but the application is not closing.  It is quickly switching the active window to a chrome browser tab and back, similar to doing a quick Alt + Tab in windows.  If you look in the taskbar at the  bottom, the chrome window still has focus and it’s not until the user clicks on the mission simulation results that it goes back to the GCS.
Questions:
- Does this happen every time on the laptop and is it still being experienced?
- Does it happen regardless of chrome being open?  Does it happen if chrome is on a different web page?  (it looks like it’s on the silvus config page)

I’m not overly concerned that this is a regression in recent GCS software, but if we can reproduce consistently we may be able to find a root cause.

### Alexander Alan Arnold, 2025-04-24

@Calvin Rogers Please see Ted’s questions and see how many times you can reproduce it.

### Calvin Rogers, 2025-04-24

@Ted Trowbridge I was just able to recreate the issue. It is only being experienced while other applications are open in the background. If I don't run any other applications or if I minimize an open application the flash does not occur. For example, I opened VXESUAV, created a mission and simulated the mission with no issues. I then opened Chrome, left it open when switching back to VXESUAV, and the flash occurred. When I minimized Chrome and went back to VXESUAV, I ran another simulation, and the flash did not occur.

### Calvin Rogers, 2025-04-24

@Ted Trowbridge I also was able to test this on two older GCS laptops we have lying around. They present the same issue.

### Ted Trowbridge, 2025-04-24

@Calvin Rogers and by older do you mean they had a previous GCS version installed?  Or did you install the latest in order to reproduce the issue?

### Calvin Rogers, 2025-04-24

@Ted Trowbridge Older model laptops. The test was still conducted on 6.4

### Ted Trowbridge, 2025-04-24

@Calvin Rogers Would it be possible to install a previous GCS and re-test?

### Calvin Rogers, 2025-04-24

@Ted Trowbridge To be clear, you want us to revert back to 6.3.4? Also, one thing I forgot to mention a min ago is that I also tried running the “Repair” option through the VXESUAV installer and that did not fix the issue either.

### Ted Trowbridge, 2025-04-24

@Calvin Rogers Yes.  I’d like to rule out this being a regression specific to 6.4.  I suspect the issue will also exist in 6.3.4, but if it doesn’t that will help us find the root cause.

### Calvin Rogers, 2025-04-24

@Ted Trowbridge I re-tested using 6.3.4 and did not experience the same issue.

### Ted Trowbridge, 2025-04-29

@Calvin Rogers Are there other versions between 6.3.4 and 6.4.0 that you could test on without too much disruption?  6.3.25 would be a good one but any other data points would be helpful.

### Jackson Riley Curvin, 2025-09-16

@Ted Trowbridge @Drew Hildreth do you see any issue with closing this ticket?

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| MicrosoftTeams-video.mp4 | video | 3118 | 2025-04-18 | listed only |
| T95_V758_250416_090549_pack.zip | archive | 595 | 2025-04-18 | listed only |
