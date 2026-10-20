# VXEP-1313: VXE-734 Mishap aborted launch

- **Issue type:** Incident (8D)
- **Status:** D8 - Closed
- **Resolution:** Done
- **Priority:** Low
- **Created:** 2025-06-24
- **Updated:** 2026-06-30
- **Resolved:** 2026-06-30
- **Reporter:** Jackson Riley Curvin
- **Assignee:** David Grosher
- **Creator:** Jackson Riley Curvin
- **Labels:** EAASSET, GS_Closed, Link_Lost_Abort, Weekly-incident-tracker
- **Links:** relates to RMA-720 (VXE-734 RMA # 250627-1)
- **Customer:** EAASSET, EA_Asset, Edge_Asset
- **Vehicle Tail Number:** VXE-734
- **Problem Type:** Other (explain in description)
- **Issue Status:** Ongoing
- **Incident Type:** Aircraft Damage
- **Severity:** 2 - Degraded Performance - No Workaround
- **Components (EA Aircraft):** Aircraft, full assembly

## Description

The aircraft looked like it automatically aborted right after lifting off the ground resulting in its normal behavior of moving aft 10 feet which resulted in the front prop hitting the aircraft stand and the front left motor meeting the ground

## Plan

Investigate the clock roll over, or relative inaccurate timing resulting in a link loss launch abort as described in the comments.

## Comments (12)

### Jackson Riley Curvin, 2025-06-24

[embedded image-20250624-224535.png]

### Jackson Riley Curvin, 2025-06-24

[embedded image-20250624-224712.png]

### David Grosher, 2025-06-24

@Jason Scherer There is an RTC update directly before the lost link timeout. Could the system clock be getting updated, resulting in the timeout triggering prematurely? In this case there doesn’t seem to actually be 5 seconds for this event to be triggered from launch to the abort.  Is this something that is in other similar launch abort events?

### Jason Scherer, 2025-06-24

@Jackson Riley Curvin These sys cmd fail errors look similar to incidents where we noticed very large missions. Mission sim time seems to be a trigger for this type of behavior. Do you know anything about the mission that was configured?

### Jackson Riley Curvin, 2025-06-24

@Jason Scherer I can get it from the FLOPS team tomorrow morning

### Jason Scherer, 2025-06-24

@David Grosher You might be on to something here. The clock updates right before the link drop is declared. The puzzling part is that the link timeouts do not resolve for ~2 minutes (122 seconds). Anyway, I should be able to make the clock update a bunch in the HIL and watch for link drops to see if we can cause the same behavior.
[embedded image-20250625-015403.png]

As you can see from these two below charts with the x-axis extended, the link does not get better until 20590, and the FW gets a hit of GCS messages around 20501 briefly before timing out again.
[embedded image-20250625-015502.png]
[embedded image-20250625-015524.png]

### Jackson Riley Curvin, 2025-06-25

@Jason Scherer I just attached the mission file.

### Jason Scherer, 2025-06-25

@Jackson Riley Curvin Ok Yea this is a pretty basic mission. The other missions I have seen take ~5-10 seconds to simulate. This one simulated instantly on my laptop.

### David Grosher, 2025-06-25

@Jason Scherer The long period of time to recover sounds like there could be an issue with the clock rolling over as well.

### Drew Hildreth, 2025-06-27

@Jason Scherer @David Grosher I added in the operator's description of events above in the Description. Going forward I will continue to have this information provided with everything we know.

### Alexander Alan Arnold, 2026-01-20

No longer tracked on GS side due to low priority and internal asset

### Jackson Riley Curvin, 2026-06-30

Closing due to inactivity, its an internal aircraft and has been flying with no other issues.

## Attachments (8)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| T95_V734_250624_120852_01_pack.zip | archive | 1436 | 2025-06-24 | listed only |
| T95_V734_250624_120852_02_pack.zip | archive | 2776 | 2025-06-24 | listed only |
| image-20250624-224535.png | image | 18 | 2025-06-24 | listed only |
| image-20250624-224712.png | image | 24 | 2025-06-24 | listed only |
| image-20250625-015403.png | image | 278 | 2025-06-24 | listed only |
| image-20250625-015502.png | image | 5 | 2025-06-24 | listed only |
| image-20250625-015524.png | image | 6 | 2025-06-24 | listed only |
| collins3.vmis | other | 4 | 2025-06-25 | listed only |
