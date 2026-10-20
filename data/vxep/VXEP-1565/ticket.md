# VXEP-1565: New ADP - Skylink conflict

- **Issue type:** Problem
- **Status:** New
- **Priority:** Medium
- **Created:** 2025-10-21
- **Updated:** 2025-10-30
- **Reporter:** Artis Bertulis
- **Assignee:** Kurt Burian
- **Creator:** Artis Bertulis
- **Links:** relates to FS2-3867 (Investigation: SA camera combability with Trillium)

## Description

I wanted to bring up a couple of issues we've encountered while operating the new ADP system with the SA camera, integrated with the Trillium gimbal, and using SkyLink software.
Issue 1:
When SkyLink is launched, the “Media Client” (also referred to as “GCS VIDEO”) EDGE video player immediately loses the video feed from the SA camera. Attempts to manually reconnect or restart the Media Client do not restore the feed. However, once SkyLink is closed, the video feed can be recovered by reconnecting to the SA camera.
Issue 2:
This may already be on your radar, but the VXE-specific SkyLink software does not automatically detect the video feed from the new SA cameras, as it typically should. When SkyLink is used, the Media Client is generally not required, so this functionality is important. It appears this integration is handled on Trillium’s side, so someone may need to coordinate with them and provide the necessary details to address this in the next software release.
Additionally, while addressing this, it would be helpful to request the implementation of a camera switch button within SkyLink, allowing users to toggle between EO and IR feeds.
[embedded: image-20251021-195812.png]

## Comments (7)

### Artis Bertulis, 2025-10-21

@Greg Fryer @Grant Goodman @Mike DeJesus Not sure if this is the right avenue for reporting this, but please move, transfer, or report as required. I’m happy to assist in any way.

@Wes Bracken @Ruysser Gabler @Carson Buckley for awareness.

### Greg Fryer, 2025-10-23

@Scott Whitney I know we had some list of remaining issues with our overall SW config. Is there a specific bug list that already has these that Artis can track, or do we need the separate problem statement?

### Greg Fryer, 2025-10-23

@Artis Bertulis I put this on Scott W, as I think we know about the remaining issues.
@Grant Goodman and @Mike DeJesus since you were on here, you can hold until/unless Scott W says no.

### Scott Whitney, 2025-10-23

@Greg Fryer I don’t believe the new SA camera was tested with Trillium. We worked out all the bugs with an E140. This will be a new problem statement

### Scott Whitney, 2025-10-23

FYSA @Kurt Burian

### Kurt Burian, 2025-10-23

@Scott Whitney @Grant Goodman This will definitely require work on trilliums side to support the Dual SA. I’m going to draft up some documentation before anything else to get them rolling then I’ll start sniffing out specific issues regarding interaction with Media Client.

### Kurt Burian, 2025-10-28

@Grant Goodman @Mike DeJesus 
Item 2 - I created a “how to” for the skylink integrators. If you can point me to the Edge template, I’d be happy to reformat. I don't have contacts to forward this too, I was hoping either of you might know how to get this to the vendor.
[embedded: new_adp_software_integration.docx]

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20251021-195812.png | image | 921 | 2025-10-21 | listed only |
| [new_adp_software_integration.docx](attachments/33361_new_adp_software_integration.docx.md) | docx | 15 | 2025-10-28 | converted |
