# VXEP-1595: VXE-886 The "User Landing Control" populated and then auto closed

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Highest
- **Created:** 2025-11-11
- **Updated:** 2026-03-02
- **Resolved:** 2025-11-12
- **Reporter:** Jackson Riley Curvin
- **Assignee:** David Grosher
- **Creator:** Jackson Riley Curvin
- **Labels:** Edge_Asset
- **Customer:** Edge_Asset
- **Vehicle Tail Number:** VXE-886
- **Vehicle Configuration:** ADV NAV Main Battery
- **Severity:** 2 - Degraded Performance - No Workaround
- **Components (EA Aircraft):** Aircraft, full assembly

## Description

The aircraft went through the launch wizard nominally. When launch was selected, the operator selected "Activate User Landing Control". The "User Landing Control" populated and then auto closed within 5 seconds. The "Waiting to Detect Launch" window that populates when launch is selected never closed and the aircraft did not launch. Operator selected "cancel" on the "waiting to detect launch" window to cancel the sequence. Aircraft did not launch again as it was the end of the day.

## Comments (7)

### David Grosher, 2025-11-11

[embedded image-20251111-230953.png]
@Ted Trowbridge It was reported that there was no RC box, but it went into RC mode before takeoff. I checked a reference flight and there was no similar mode change prior to launch. Could this be a wrong ini file?
@Jackson Riley Curvin

### Jackson Riley Curvin, 2025-11-11

@David Grosher @Ted Trowbridge  does this mean that the operator clicked abort?
[embedded image-20251111-234242.png]

### Ted Trowbridge, 2025-11-11

@David Grosher @Jackson Riley Curvin 
The GCS logs indicate the operator aborted the launch using the abort button on the joystick.
Looking at the GCS.ini it does not appear that RC was enabled.
There was an XBOX controller plugged in.

### Jackson Riley Curvin, 2025-11-12

@Ted Trowbridge  I don't see a reason to keep this ticket open, do you?

### Ted Trowbridge, 2025-11-12

@Jackson Riley Curvin it appears to me that the user aborted launch via the joystick before the vehicle lifted off or the system detected launch.  Is that what we think happened?
If so, it seems like the system behaved as expected and briefly presented the landing controls before closing them due to the vehicle being safe on the ground.  I don’t see much else to investigate unless there’s a concern about the launch detection or the user claimed to have not aborted the launch.

### Jackson Riley Curvin, 2025-11-12

@Ted Trowbridge I talked with the instructor last night and they were fairly certain that the student clicked abort on the controller.

### Jackson Riley Curvin, 2025-11-12

Aircraft behaved as expected

## Attachments (3)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T115_V886_251111_155023_pack.zip | archive | 1140 | 2025-11-11 | listed only |
| image-20251111-230953.png | image | 56 | 2025-11-11 | listed only |
| image-20251111-234242.png | image | 47 | 2025-11-11 | listed only |
