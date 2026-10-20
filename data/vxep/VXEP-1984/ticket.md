# VXEP-1984: VXE 1039 did not detect left dropper pylon

- **Issue type:** Incident (8D)
- **Status:** D4 - Investigating Root Cause
- **Priority:** High
- **Created:** 2026-08-21
- **Updated:** 2026-10-12
- **Reporter:** Zachary Mann
- **Assignee:** David Grosher
- **Creator:** Zachary Mann
- **Labels:** LRR, RCCA, Weekly-incident-tracker
- **Customer:** LRR
- **Vehicle Tail Number:** 1039
- **Vehicle Configuration:** VXE35, OGCS, E140
- **Problem Type:** Other (explain in description)
- **Incident Type:** Mission Failure/Abort
- **Severity:** 2 - Degraded Performance - No Workaround
- **Executive Summary:** Left dropper pylon never recognized in OGCS, even though a dropper was mounted

## Description

Droppers were put on 1039 from 1021, it detected the right pylon and activated it correctly, but it did not ever see the left, even through multiple autopilot resets and power cycles, both in the payload power control and physical power cycle. 

The  1039 file and the 161143z file for 1021 relate to Drop Pylons

## Comments (11)

### Cody Smisek, 2026-08-21

when we performed the limited testing on B35/B40 droppers, it required numerous manual steps to configure and activate. Did we release new software that resolved these manual steps? What procedure is the customer following?
@Zachary Mann

### Zachary Mann, 2026-08-21

@Cody Smisek Good morning, Cody, I am unaware of that information. This was reported by one of our operators while out training.

### David Grosher, 2026-08-21

@John Clark Can you take a look at this?

### John Clark, 2026-08-21

@Cody Smisek the procedures for test and configuration have not changed. Newer Releases would just ensure support across more AC’s B35, B40 and so on with both new and old Pylon hardware.

### Cody Smisek, 2026-08-21

@John Clark I’m trying to track down what documentation they’re using/not using. Confirming they would need to re-enable / turn on the droppers via the xcomm webpages following any/all Launch wizard resets?

### John Clark, 2026-08-21

This is from 1039 and is correct for Pylon 2. The Pylon is now Armed…. Pylon 2 is the Righthand, Starboard (from the pilot’s perspective)
[embedded image-20260821-185212.png]
I see a second Arm for Payload 2… and then a Drop
[embedded image-20260821-190323.png]
The command was acknowledged so the Dropper should have released its Payload.
@Zachary Mann I see these too. 
[18:00:57.519 1216.519] ADVERT SENT
This suggests that the Lefthand, Port Dropper has not been detected. I am not sure what’s happening. The falure could be hardware related. But the firmware does not see the Pylon.

### John Clark, 2026-08-21

From 1021 I never see an ADVERT sent to either Dropper for Address assignment. Something is very wrong there. I do see a number of Commands sent from GCS/OGCS.@Zachary Mann

### John Clark, 2026-08-21

@Cody Smisek 1021 doesnt even send ADVERTs. That’s just weird.

### Zachary Mann, 2026-08-28

Reached out to @John Clark for file review

### Zachary Mann, 2026-10-01

Being shipped to SLO

### Zachary Mann, 2026-10-12

Tracking Number: 12116607107

## Attachments (4)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| AAR_V1021_B35_20260819T161143Z.zip | archive | 37951 | 2026-08-21 | listed only |
| AAR_V1039_B35_20260819T181458Z.zip | archive | 46127 | 2026-08-21 | listed only |
| image-20260821-185212.png | image | 41 | 2026-08-21 | listed only |
| image-20260821-190323.png | image | 7 | 2026-08-21 | listed only |
