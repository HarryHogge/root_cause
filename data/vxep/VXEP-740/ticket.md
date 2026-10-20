# VXEP-740: Feasibility of implementing 180* FOV camera with new encoder board

- **Issue type:** Task
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2024-10-23
- **Updated:** 2024-12-19
- **Resolved:** 2024-12-19
- **Reporter:** Grant Goodman
- **Assignee:** Brandon Slater
- **Creator:** Grant Goodman
- **Parent:** VXEP-93 Replace SA Camera EM18911 (100-100835) and EM19821 (100-101235) are obsolete. due February 2025.
- **Epic Link:** VXEP-93

## Description

As part of the camera system down select, we need to check feasibility and scope level of work to implement use of the main candidate.
The encoder company is the same, the board supports the same outputs ethernet, H.264 RTSP, UDP but there may be some changes due to the new encoder hardware or software.
Additionally, the camera used has a 180* all around FOV that needs to have a portion selected to de-warp to be practical for human use.
Investigate new software/firmware and ensure that there is a path forward to display an image similar to what is currently on the GCS through the legacy camera system and provide a rough scope of implementation effort for software/firmware to be ready to hand off to production.
@Rajesh Budhabhatti Has a unit on site that he is working through functionality that can be used for investigation and two more are due to arrive in SLO on 10/24
No implementation is required at this time, just verification of feasibility and scope.
Encoder board details:
ATOMAS-IOT-MICRO
https://www.ionodes.com/product/oem-modules/ 
Camera:
IONode ION CAM
https://intertest.com/products/ionodes-ion-cam-mipi-ov12a10-kit-4k-mipi-camera-with-lens

## Comments (0)

## Attachments (0)
