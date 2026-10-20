# GCSS-345: Prevent "Pattern Altitude AGL" from being set to a very high altitude

- **Issue type:** Story
- **Status:** Canceled
- **Resolution:** Won't Do
- **Priority:** Low
- **Created:** 2024-08-21
- **Updated:** 2026-09-23
- **Resolved:** 2026-09-23
- **Reporter:** Jason Scherer
- **Creator:** Jason Scherer
- **Links:** relates to VXEP-546 (VXE 470 transitioned to VTOL at 2400 AGL then crashed)

## Description

The GCS will allow an operator to set a very high (3000' AGL) “Pattern Altitude AGL” when setting up a new PLZ mission. This causes the vehicle to transition from fixed wing flight to VTOL flight at that altitude which in this case would be 3000'. 
The GCS should not allow the operator to set the “Pattern Altitude AGL” higher than the vehicle VTOL battery (HLB) can support.
This issue was discovered in a customer incident (VXEP-546). You can see in the FDR that after the RTB is commanded the vehicle is commanded to climb from 1500' to 3000'. In the incident the vehicle transitions ~2300'. The customer then held the pause landing button down until the VTOL processor ignored the command due to low HLB. The vehicle finally crashed when the HLB was fully depleted. 
Here is the FDR with annotations:
[embedded: image-20240821-173530.png]
Here is the commanded versus actual altitude plotted from the same FDR:
[embedded: image-20240821-173604.png]
I was able to recreate this issue in the HIL by setting my “Pattern of Altitude AGL” to 3000' and my IP1 Altitude AGL to 3000'. On RTB my sim vehicle started climbed from 1500' (primary mission) to 3000' before transitioning to VTOL.

## Comments (2)

### Jason Scherer, 2024-08-21

@David Grosher

### Christa Meck, 2026-09-23

No work done in over a year.  Canceling.

## Attachments (2)

| File | Kind | KB | Added | Result |
| --- | --- | --- | --- | --- |
| image-20240821-173530.png | image | 586 | 2024-08-21 | listed only |
| image-20240821-173604.png | image | 27 | 2024-08-21 | listed only |
